      subroutine setborn(p,bflav,born,bornjk,bmunu)
c Wrapper subroutine to call the MadGraph Borns
c and set the event-by-event couplings constant
      implicit none
      real * 8 p(0:3,*),bornjk(*,*)
      integer bflav(*)
      real * 8 bmunu(0:3,0:3,*),born
      call set_ebe_couplings
      call sborn_proc(p,bflav,born,bornjk,bmunu)
      end

      subroutine borncolour_lh
c Wrapper subroutine to call the MadGraph code to associate
c a (leading) color structure to an event.
      implicit none
      include 'nlegborn.h'
      include 'LesHouches.h'
      include 'pwhg_rad.h'
      include 'pwhg_flst.h'
      integer bflav(nlegborn),is_fs_flav(nlegborn),
     1     is_fs(nlegborn),isfslength,color(2,nlegborn)
      integer i,j,iret,icount,iprint,ifl

c This does not have problems due to smartsig. Before calling this function, POWHEG
c calls the setborn matrix element explicitly, bypassing smartsig, in such a way
c that colour subamplitudes are correctly stored by MadGraph.

      do i=1,flst_bornlength(rad_ubornsubp)
         bflav(i)=idup(i)
         if (bflav(i).eq.21) bflav(i)=0
      enddo
      call getisfsparticles(nup,bflav,flst_bornres(:,rad_ubornsubp),
     1     isfslength,is_fs)
      do j=1,isfslength
         is_fs_flav(j) = bflav(is_fs(j))
      enddo

      icount = 0
      iprint = 2

      call allow_all_colors

 1    continue
      icount = icount + 1
      if(icount.gt.1000000) then
         write(*,*) ' borncolour_lh : cannot find colour configuration '
         write(*,*) ' consistent with resonance assignment. Exiting ... '
         call exit(-1)
      elseif(icount.gt.iprint) then
         write(*,*) ' borncolour_lh : try another one '
         write(*,*) ' borncolour_lh:',iprint,' tries; keep trying'
         iprint = iprint*10
      endif

      call born_color_ifl(is_fs_flav,color,ifl)

      do j=1,isfslength
         icolup(:,is_fs(j))=color(:,j)
      enddo

      call complete_resonance_colours(iret)
      if(iret.lt.0) then
         call disallow_color(ifl)
         goto 1
      endif

      end

      subroutine finalize_lh
      implicit none
      call check_leshouches
      end


      subroutine complete_resonance_colours(iret)
      implicit none
      integer iret
      include 'LesHouches.h'
      integer iup,kup,moth,col(nup),acol(nup),ncol,nacol,jcol,jacol
      logical is_coloured
      external is_coloured
c Look for coloured resonances      
      do iup = 3,nup
         if(istup(iup).gt.1) then
            ncol = 0
            nacol = 0
            do kup = 3,nup
               if(istup(kup).eq.1) then
                  moth = mothup(1,kup)
                  do while (moth.ne.0)
                     if(moth.eq.iup) exit
                     moth = mothup(1,moth)
                  enddo
                  if(moth.ne.0) then
                     if(icolup(1,kup).ne.0) then
                        ncol = ncol + 1
                        col(ncol) = icolup(1,kup)
                     endif
                     if(icolup(2,kup).ne.0) then
                        nacol = nacol + 1
                        acol(nacol) = icolup(2,kup)
                     endif
                  endif
               endif
            enddo
            do jacol = 1,nacol
               do jcol = 1,ncol
                  if(col(jcol).eq.acol(jacol)) then
                     col(jcol) = 0
                     acol(jacol) = 0
                  endif
               enddo
            enddo
c at most one colour and one anticolour should be left
            icolup(:,iup) = 0
            do jcol = 1,ncol
               if(col(jcol).ne.0) then
                  icolup(1,iup) = col(jcol)
                  col(jcol) = 0
                  if(.not.all(col(1:ncol).eq.0)) then
                     iret = -1
                     return
                  else
                     exit
                  endif
               endif
            enddo
            do jacol = 1,nacol
               if(acol(jacol).ne.0) then
                  icolup(2,iup) = acol(jacol)
                  acol(jacol) = 0
                  if(.not.all(acol(1:nacol).eq.0)) then
                     iret = -1
                     return
                  else
                     exit
                  endif
               endif
            enddo
c TODO : check that the colour assignment is consistent with flavour
            if(( idup(iup).eq. 6 .and. .not. (icolup(1,iup).ne.0.and.icolup(2,iup).eq.0) ) .or.
     1         ( idup(iup).eq.-6 .and. .not. (icolup(2,iup).ne.0.and.icolup(1,iup).eq.0) ) .or.
     2         ( abs(idup(iup)) .ne. 6 .and. .not. (icolup(1,iup).eq.0.and.icolup(2,iup).eq.0) ) ) then
               iret = -1
               return
            endif
         endif
      enddo
      iret = 0
      end

      
      integer function allowed_color(ifl)
      implicit none
      integer ifl,iallowed
      call pilot_allow_color(ifl,'g',iallowed)
      allowed_color = iallowed
      end

      subroutine disallow_color(ifl)
      implicit none
      integer ifl,iallowed
      call pilot_allow_color(ifl,'s',iallowed)
      end

      subroutine allow_all_colors
      implicit none
      integer ifl,iallowed
      call pilot_allow_color(ifl,'r',iallowed)
      end
      
      subroutine pilot_allow_color(ifl,mode,iallowed)
      implicit none
c mode = g,s,r for get, set, reset
      integer ifl,iallowed
      character * 1 mode
c
      integer, save :: maxforbid=0
      integer, allocatable, save :: forbidden(:)
      integer, allocatable :: saveforbidden(:)
      integer, save :: nforbid=0
      integer k
      if(mode == 'r') then
         nforbid = 0
      elseif(mode == 'g') then
         do k=1,nforbid
            if(forbidden(k) == ifl) then
               iallowed = 0
               return
            endif
         enddo
         iallowed = 1
      elseif(mode == 's') then
         if(nforbid >= maxforbid) then
            if(allocated(forbidden)) then
               allocate(saveforbidden(maxforbid))
               saveforbidden = forbidden
               deallocate(forbidden)
               allocate(forbidden(maxforbid+10))
               forbidden(1:maxforbid) = saveforbidden
               deallocate(saveforbidden)
               maxforbid = maxforbid+10
            else
               maxforbid = maxforbid+10
               allocate(forbidden(maxforbid))
            endif
         endif
         nforbid = nforbid + 1
         forbidden(nforbid) = ifl
      else
         write(*,*) ' pilot_allow_color: mode ',mode,' not allowed!'
         write(*,*) ' exiting ...'
         call exit(-1)
      endif
      end
