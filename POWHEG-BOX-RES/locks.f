      subroutine createlock(lockfile0)
      implicit none
      include 'pwhg_rnd.h'
      character *(*) lockfile0
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      character * 100 lockfile
      integer iun,istat
      logical first
      call newunit(iun)
      istat = -1
      first = .true.
      lockfile = pwgprefix(1:lprefix)//'-'//lockfile0
      do while(istat.ne.0)
         open(unit=iun,file=lockfile,status='new',iostat=istat)
         if(istat.ne.0) then
            if(first) then
               write(*,*) ' createlock, process',rnd_cwhichseed,': ',
     1              trim(lockfile),' already there, waiting ...' 
               first = .false.
            endif
            call sleep(1)
         else
            call locks_stack('push',lockfile)
         endif
      enddo
      write(iun,*) rnd_cwhichseed
      close(iun)
      write(*,*) ' createlock, process ',rnd_cwhichseed,': created the lock ', trim(lockfile)
      end

      subroutine deletelock(lockfile0)
      implicit none
      include 'pwhg_rnd.h'
      character *(*) lockfile0
      integer lprefix
      character * 20 pwgprefix
      common/cpwgprefix/pwgprefix,lprefix
      character * 100 lockfile
      character * 4 chtmp
      integer iun,istat
      call newunit(iun)
      istat = -1
      lockfile = pwgprefix(1:lprefix)//'-'//lockfile0
      open(unit=iun,file=lockfile,status='old',iostat=istat)
      if(istat.ne.0) then
         write(*,*) ' deletelock, process ',rnd_cwhichseed,': ',
     1              ' cannot open the lock ',trim(lockfile),' for deletion',
     2              ' exiting ...'
         call exit(-1)
      endif
      read(iun,*) chtmp
      if(chtmp.eq.rnd_cwhichseed) then
         close(iun,status='delete')
         call locks_stack('pop',lockfile)
         write(*,*) ' deletelock, process ',rnd_cwhichseed,': deleted the lock ', trim(lockfile)         
      else
         write(*,*) ' deletelock, process',rnd_cwhichseed,': ',
     1              ' The lock ',trim(lockfile),' is from process '//chtmp,
     2              ' something wrong ... exiting'
      endif
      end


      subroutine locks_stack(command,lockname)
      implicit none
      character *(*) command,lockname
      integer, parameter :: max_locks=100
      type lock_pointer
      character(len=:), pointer :: ptr
      end type lock_pointer
      type(lock_pointer), dimension(max_locks), save :: locks
      integer, save :: top_lock=0
      integer j,iun,istat
      if(command == 'push') then
         if(top_lock == max_locks) then
            write(*,*) 'lock_stack: no more slots left'
            write(*,*) ' exiting ...'
            call exit(-1)
         endif
         top_lock = top_lock + 1
         allocate(character(len(lockname))::locks(top_lock)%ptr)
         locks(top_lock)%ptr=lockname
      elseif(command == 'pop') then
         if(top_lock == 0) then
             write(*,*) 'lock_stack: iunvoked with pop command,'
             write(*,*) 'but no lockfiles in stack,'
             write(*,*) 'exiting ...'
             call exit(-1)
          endif
          if(lockname /= locks(top_lock)%ptr) then
             write(*,*) 'lock_stack: iunvoked with pop command,'
             write(*,*) 'but top lockfiles in stack does not match,'
             write(*,*) 'exiting ...'
             call exit(-1)
          endif
          deallocate(locks(top_lock)%ptr)
          top_lock = top_lock - 1
      elseif(command == 'del') then
c     delete all locks
         do j=1,top_lock
            open(unit=iun,file=locks(j)%ptr,status='old',iostat=istat)
            if(istat /= 0) then
               write(*,*)
     1              'lock_stack: could not open lock '//locks(j)%ptr//
     2          ' for deletion'
               cycle
            endif
            close(iun,status='delete')
         enddo
      else
         write(*,*) 'lock_stack: command '//command//' not found'
         write(*,*) ' exiting ...'
      endif
      end
