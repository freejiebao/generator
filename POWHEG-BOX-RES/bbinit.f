      subroutine bbinit
      implicit none
      integer iret
      real * 8 powheginput
      integer parallelstages,xgriditeration
      external powheginput
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_rad.h'
      include 'pwhg_rnd.h'
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      real * 8 xx(ndiminteg)      
      integer mcalls,icalls,ind,j,l,iunstat
      character * 40 mergelabels
      character * 40 filename
      character * 10 contribs(3)
      character * 10 parlabel
      logical docontribs(3),nloplots,nlotest_save
      integer iretcontribs(3)
      integer btilde,sigremnant
      external btilde,sigremnant,mergelabels
      iretcontribs = -1
c btilde:
      contribs(1)='btilde'
      docontribs(1) = powheginput("#withbtilde") .ne. 0
c damp remnants
      contribs(2)='remn'
      docontribs(2) = flg_withdamp .and. .not. flg_bornonly
     1     .and. powheginput("#withremnants") .ne. 0
     2     .and. .not. flg_virtonly
c regulars:
      contribs(3)='reg'
      docontribs(3) = flg_withreg  .and. .not. flg_bornonly
     1     .and. powheginput("#withregular") .ne. 0
     2     .and. .not. flg_virtonly
c
c parallelstages:
c 1   prepare the importance sampling grids
c 2   prepare the upper bounding envelopes for the
c     generation of the b_tilde function
c 3   prepare the upper bound for the generation of radiation
c 4   generate events
      call getparallelparms(parallelstages,xgriditeration)

c     If rwl_add 1, force parallelstages to 4
      if(parallelstages < 4 .and. flg_rwl_add) then
         write(*,*) ' since rwl_add is set, we force parallelstages=4'
         parallelstages = 4
      endif

      call setparallellabel(parallelstages,xgriditeration,parlabel)
      if(parallelstages < 4) then
         call newunit(iunstat)
      endif
      open(unit=iunstat,file=mergelabels(pwgprefix,rnd_cwhichseed,
     1     parlabel,'stat.dat'),status='unknown')
      if(rnd_cwhichseed.ne.'none')
     1     call setrandom(rnd_initialseed,rnd_i1,rnd_i2)
      if (flg_nlotest) call init_hist
      if(parallelstages.le.0) then
c Do all stages in one go if needed;
c first look for fullgrid files:
c btilde:
         do j=1,3
            if(docontribs(j)) then
               call loadgrids(contribs(j),'fullgrid',iretcontribs(j))
               if(iretcontribs(j).ne.0) then
                  call loadgrids(contribs(j),'grid',iretcontribs(j))
               endif
            endif
         enddo

         if( any(iretcontribs .eq. 0) ) then
c at least one of them was loaded: do not do NLO plots (they would be incomplete)
            nloplots = .false.
            flg_nlotest = .false.
         elseif(flg_nlotest) then
            nloplots = .true.
         else
            nloplots = .false.
         endif

         if (nloplots) call init_hist
            
         do j=1,3
            if(iretcontribs(j).ne.0.and.docontribs(j)) then
               call loadxgridsn(contribs(j),-1,iret)
               if(iret.ne.0) then
c imode=0, doregrid=.true.
                  nlotest_save = flg_nlotest
                  flg_nlotest = .false.
                  call mintwrapper(contribs(j),0,.true.,iunstat)
c     second argument specifies xgriditeration in parallel runs, 0 here.
                  call storexgrids(contribs(j),0)
                  flg_nlotest = nlotest_save
               endif
            endif
         enddo
         do j=1,3
            if(iretcontribs(j).ne.0.and.docontribs(j)) then
               call mintwrapper(contribs(j),1,.false.,iunstat)
               if(flg_storemintupb) then
                  call loadmintupbwrapper(contribs(j))
                  write(*,*) ' Upper bounding envelope for '//trim(contribs(j))//' computed'
                  write(*,*) ' Efficiency for generation is printed above'
                  call storegrids(contribs(j),'grid')
               endif
c after all the calls to mintwrapper
               if (nloplots) call pwhgaddout
            endif
         enddo

         if (nloplots) then
            filename=mergelabels(pwgprefix,rnd_cwhichseed,'NLO',' ')
            call pwhgtopout(filename)
         endif
c write cross section information
         call writestat(iunstat)
         close(iunstat)
c     initialize gen
         do j=1,3
            if(docontribs(j)) then
               call genwrapper(contribs(j),0,mcalls,icalls,xx,ind)
            endif
         enddo
         if (.not.flg_LOevents) then
            call do_maxrat(mcalls,icalls,-1,iret)
         endif
         return
      endif

      if(parallelstages.eq.1) then
         flg_nlotest = .false.
         call setrandomseed(xgriditeration)
         do j=1,3
            if(docontribs(j)) then         
               if(xgriditeration.gt.1) then
                  call loadxgridsn(contribs(j),xgriditeration-1,iret)
                  if(iret.lt.0) then
                     write(*,*) ' bbinit: cannot find grid files'
                     write(*,*) ' for iteration ',xgriditeration-1
                     write(*,*) ' exiting ...'
                     call pwhg_exit(iret)
                  endif
               endif
c imode=0,doregrid=.false.
               call mintwrapper(contribs(j),0,.false.,iunstat)
               call storexgrids(contribs(j),xgriditeration)
            endif
         enddo
         call pwhg_exit(0)
      endif

c now for parallestages = 2
      if(parallelstages.eq.2) then
c before the first call to mintwrapper, reset all histograms for NLO analysis
         if (flg_nlotest) call init_hist
         do j=1,3
            if(docontribs(j)) then         
c     The line below should fail. If you are trying to redo a stage 2 run, the fullgrid
c     file should be regenerated
               call loadgrids(contribs(j),'fullgrid',iret)
               if(iret.eq.0) then
                  write(*,*) ' bbinit: '//
     1                 ' you are redoing the stage 2 run for '//trim(contribs(j)),
     2                 ' but the fullgrid file from a previous run is there.'
                  write(*,*) ' Do: rm *fullgrid*.dat and restart. Exiting ...'
                  call pwhg_exit(-1)
               endif
               call loadxgridsn(contribs(j),-1,iret)
               if(iret.ne.0) then
                  write(*,*) ' cannot load xgrid or gridinfo files for ',trim(contribs(j))
                  write(*,*) ' cannot perform stage 2'
                  call pwhg_exit(-1)
               endif

               call mintwrapper(contribs(j),1,.false.,iunstat)
               call storegrids(contribs(j),'grid')
c this should be after each call to mintwrapper
               if (flg_nlotest) call pwhgaddout
            endif
         enddo
c after all the calls to mintwrapper
         if (flg_nlotest) then
            filename=mergelabels(pwgprefix,rnd_cwhichseed,'NLO',' ')
            call pwhgtopout(filename)
         endif
         call writestat(iunstat)
         call pwhg_exit(0)
      endif

      if(parallelstages.eq.3) then
         do l=1,3
c     if rnd_iwhichseed == 1, j goes from 1 to 2 to 3;   
c     if rnd_iwhichseed == 2, j goes from 2 to 3 to 1;   
c     if rnd_iwhichseed == 3, j goes from 3 to 1 to 2;
c     This is such that, if there are at least three processes, the time-consuming
c     part of assemling the stored mint up-bounds and processing them is done by
c     one process for each contribution, rather than by a single process for all contributions.
            j= mod(rnd_iwhichseed + l - 2,3) + 1
            if(docontribs(j)) then
c the program will sleep until a lock is created
               call createlock(trim(contribs(j))//'-fullgrid.lock')
c now the lock is in place; try to load a fullgrid
               call loadgrids(contribs(j),'fullgrid',iret)
               if(iret.lt.0) then
                  call loadgrids(contribs(j),'grid',iret)
                  if(iret.lt.0) then
                     write(*,*) ' cannot load grid files for '//trim(contribs(j))
                     call pwhg_exit(-1)
                  endif
                  if(flg_storemintupb) then
                     call loadmintupbwrapper(contribs(j))
                     write(*,*) ' Upper bounding envelope for '//trim(contribs(j))//' computed'
                     write(*,*) ' Efficiency for generation is printed above'
                  endif
                  call storegrids(contribs(j),'fullgrid')
               endif
               call deletelock(trim(contribs(j))//'-fullgrid.lock')
            endif
         enddo
      
         call writestat(iunstat)

c initialize gen
         call genwrapper('btilde',0,mcalls,icalls,xx,ind)
         call setrandom(rnd_initialseed,rnd_i1,rnd_i2)
         if (.not.flg_LOevents) then
c do_maxrat with third argument = 0
c forces compute upper bound for radiation (iret ignored)
            call do_maxrat(mcalls,icalls,0,iret)
         endif
         call pwhg_exit(0)
      endif

      if(parallelstages .ne. 4) then
         write(*,*) ' bbinit: called with parallelstages=',parallelstages
         write(*,*) ' Not allowed. Exiting ...'
         call pwhg_exit(-1)
      endif

      do j=1,3
         if(docontribs(j)) then
            call loadgrids(contribs(j),'fullgrid',iret)
            if(iret.lt.0) then
               write(*,*) ' bbinit: called with parallelstages 4'
               write(*,*) ' but no fullgrid files for '//trim(contribs(j))//' are found'
               write(*,*) ' Should run stage 3 instead. Exiting ...'
               call pwhg_exit(-1)
            endif
         endif
      enddo

      call setrandom(rnd_initialseed,rnd_i1,rnd_i2)
      if (.not.flg_LOevents) then
c do_maxrat with third argument = 1
c forces loading upper bound for radiation
         call do_maxrat(mcalls,icalls,1,iret)
         if(iret.lt.0) then
            write(*,*) ' bbinit: cannot load upper bound for radiation'
            write(*,*) " Should'nt you rerun stage 3?"
            write(*,*) ' exiting ...'
            call exit(-1)
         endif
      endif

c initialize gen; the array xmmm is set up at this stage.
      
      do j=1,3
         if(docontribs(j)) then
            call genwrapper(contribs(j),0,mcalls,icalls,xx,ind)
         endif
      enddo

      call setrandom(rnd_initialseed,rnd_i1,rnd_i2)
      end


      subroutine setstage2init
      implicit none
      real * 8 powheginput
      if(powheginput("#stage2init").eq.1d0) then
         call resetrandom
      endif
      end

      subroutine gen_btilde(mcalls,icalls)
      implicit none
      include 'nlegborn.h'
      integer mcalls,icalls
      real * 8 xx(ndiminteg)      
      integer ind
      real * 8 btilde
      external btilde
      call genwrapper('btilde',1,mcalls,icalls,xx,ind)
      end

      subroutine gen_sigremnant
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'cgengrids.h'
      real * 8 xx(ndiminteg)
      integer mcalls,icalls,ind
      logical savelogical
      real * 8 sigremnant
      external sigremnant
c communicate file to load upper bound data
      savelogical=flg_fastbtlbound
      flg_fastbtlbound=.false.
      call genwrapper('remn',1,mcalls,icalls,xx,ind)
      flg_fastbtlbound=savelogical
      end

      subroutine gen_sigregular
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'cgengrids.h'
      real * 8 xx(ndiminteg)
      integer mcalls,icalls,ind
      logical savelogical
      real * 8 sigremnant
      external sigremnant
c communicate file to load upper bound data
      savelogical=flg_fastbtlbound
      flg_fastbtlbound=.false.
      call genwrapper('reg',1,mcalls,icalls,xx,ind)
      flg_fastbtlbound=savelogical
      end

      function mergelabels(lab1,lab2,lab3,lab4)
c puts together up to 4 labels, separating them with '-'.
c Empty labels are ignored.
      character * 40 mergelabels
      character *(*) lab1,lab2,lab3,lab4
      integer where
      mergelabels=' '
      if(lab1.ne.' '.and.lab1.ne.'none') then
         mergelabels=adjustl(lab1)
         where=index(mergelabels,' ')
         if(where.eq.0) goto 999
      endif
      if(lab2.ne.' '.and.lab2.ne.'none') then
         mergelabels(where:)='-'//adjustl(lab2)
         where=index(mergelabels,' ')
         if(where.eq.0) goto 999
      endif
      if(lab3.ne.' '.and.lab3.ne.'none') then
         mergelabels(where:)='-'//adjustl(lab3)
         where=index(mergelabels,' ')
         if(where.eq.0) goto 999
      endif
      if(lab4.ne.' '.and.lab4.ne.'none') then
         mergelabels(where:)='-'//adjustl(lab4)
         where=index(mergelabels,' ')
         if(where.eq.0) goto 999
      endif
c get rid of hiphen before extension
      where=index(mergelabels,'-.',.true.)
      if(where.ne.0) then
         mergelabels(where:)=mergelabels(where+1:)
      endif
      return
 999  write(*,*) ' mergelabels: strings too long'
      call pwhg_exit(-1)
      end


      subroutine setrandomseed(index)
      implicit none
      integer index
      include 'pwhg_rnd.h'
      integer itmp,j
      real * 8 random
      external random
      if(index.lt.0) then
         itmp = 0
      else
         call resetrandom
         do j=1,index
            itmp = random()*1d9
         enddo
      endif
      call setrandom(rnd_initialseed+itmp,rnd_i1,rnd_i2)
      end

      subroutine setparallellabel(parallelstages,xgriditeration,parlabel)
      implicit none
      integer parallelstages,xgriditeration
      character *(*) parlabel
      parlabel = ' '
      if(parallelstages.gt.0) then
         if(parallelstages.eq.1) then
            write(parlabel,'(a,i3)') 'xg',xgriditeration
            parlabel(3:)=adjustl(parlabel(3:))
         else
            write(parlabel,'(a,i1)') 'st',parallelstages
         endif
      endif
      end
