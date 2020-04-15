      program main_pythia8
      implicit none
      include 'nlegborn.h'
      include 'LesHouches.h'
      include 'hepevt.h'
      include 'pwhg_rad.h'
      include 'pwhg_rwl.h'
      character * 100 inputfilename
      integer pythiamatching,pytune
      integer doqcdps
      logical * 1 use_photos,vetoqed,py8veto,nohad,savelhe,noQEDqopt
      common/si_data/pythiamatching,pytune,use_photos,vetoqed,py8veto,nohad,savelhe,noQEDqopt,doqcdps
      real * 8 kt2minqed
      real * 8 xphcut
      real * 8 vetoscale_isr, vetoscale_fsr,massres,vetoscale_isr_qed
      integer evtnumber,emitter_fsr,nfsres
      common/si_event_info/xphcut,vetoscale_isr,vetoscale_fsr(3),evtnumber,emitter_fsr(3),nfsres,massres(3),vetoscale_isr_qed
      real*8 mc_isr_scale,mc_fsr_scale
      integer mc_fsr_em
      common/mc_scale_lhe/mc_isr_scale,mc_fsr_scale(3),mc_fsr_em(3)


      character * 6 WHCPRG
      common/cWHCPRG/WHCPRG
      integer j,k,l,m,iret
      integer maxev,iun,maxshowerevents
      integer py8trial,py8trialmax
      integer photostrial,photostrialmax
      logical ok,savehistos
      real * 8 powheginput
      external powheginput
      real * 8 ptrel
      logical lepveto
      logical not_finite_kin_lh

      real*8 cm(1:4),scale
      integer i1,i2,i3
      logical qcdps
c Read options from powheg.input 
      real*8 dummy
      real * 8 ub_btilde_corr, ub_remn_corr, ub_corr

      
c Number of events to shower (also open powheg.input file)
      maxshowerevents = powheginput("#SI_maxshowerevents")
      write(*,*) 'SI: maxshowerevents: ', maxshowerevents

c Input file
      call powheginputstring_local('SI_inputfile',inputfilename,
     +     'pwgevents.lhe')
      write (*,*) 'SI: inputfilename: ', inputfilename      


c PYTHIA tune
      pytune=powheginput("#SI_pytune")
      write(*,*) 'SI PYTHIA tune: ', pytune

c PYTHIA QED shower from quarks
      noQEDqopt = powheginput("#SI_noQEDq").eq.1

      use_photos=.false.
      vetoqed=.true.
      py8veto=.true.
      pythiamatching = 2
      savelhe=.false.
      
c Hadronization in PYTHIA
      nohad = powheginput("#SI_nohad").eq.1
      write(*,*) 'SI nohad: ', nohad


c Save fortran based histograms for analysis
      savehistos = powheginput("#SI_savehistos").eq.1
      write(*,*) 'SI savehistos: ', savehistos



c Open file, set number of events to be read (maxev)
c The variable iun is assigned by the opencount_local function
      call opencount_local(inputfilename,maxev,iun)
      if(maxshowerevents.gt.0) maxev=maxshowerevents
      write (*,*) '*** SI: Number of events to be showered: ', maxev

      qcdps=powheginput("#SI_qcdps").ne.0d0
      if(qcdps) then
         doqcdps=1
      else
         doqcdps=0
      endif

      write(*,*)'doqcdps',doqcdps



      ub_btilde_corr = powheginput('#ub_btilde_corr')
      if (ub_btilde_corr < 0d0) then
        ub_btilde_corr = 1d0
      endif
      ub_remn_corr = powheginput('#ub_remn_corr')
      if (ub_remn_corr < 0d0) then
        ub_remn_corr = 1d0
      endif

      
      
c Read header of event file (do before initializing PYTHIA and PHOTOS)
      call lhefreadhdr(iun)

c Initialize PYTHIA (.cc file)
      call pythia_init
c number of retry for pythia8, to generate photon events
c that pass the veto.
      py8trialmax = 20


c Initialize PHOTOS (.cc file)
      if(use_photos) then
         write(*,*)'photos interface NOT implemented'
         stop
      endif
      
c     Print info about veto'es
      if (vetoqed) then
         if (py8veto) then
            write(*,*) '*** SI: Applying PYTHIA (UserHooks)'//
     +           ' based veto on PYTHIA QED emissions'
         else
            write(*,*) '*** SI: Applying independent fortran'//
     +           ' based veto on PYTHIA QED emissions'
         end if
      else 
         write(*,*) '*** SI: No veto will be done on QED emissions'
      end if

      
c Initialize Fortran based analysis (histograms)
      if (savehistos) then 
        WHCPRG='PYTHIA'
        call init_hist
      endif


 
c Main loop
      write (*,*) '*** SI: Showering events',maxev
      nevhep=0
      do l=1,maxev


         
         py8trial = 0

         mc_isr_scale = 0d0
         mc_fsr_scale = 0d0
         xphcut = 0d0;

 1       call lhefreadev(iun)

         

c rescale the weight of the event depending on the rad_type (1..btilde, 2..remn)
c   using the ub_..._corr factors
         if (rwl_type == 1) then
            ub_corr = ub_btilde_corr
         else if (rwl_type == 2) then
            ub_corr = ub_remn_corr
         else 
            ub_corr = 1d0
         endif
         xwgtup=ub_corr*xwgtup

         

c     find number of external resonances (different fot t or s channel)

         vetoscale_isr_qed=mc_isr_scale
         if(qcdps) then
            vetoscale_isr=scalup ! scale
         else
            vetoscale_isr=mc_isr_scale
         endif

c         write(*,*)'vetoscale_isr',vetoscale_isr

         
         nfsres=0
         massres=-10d0
         emitter_fsr=-1
         vetoscale_fsr=-1d0
         do i1=nup,1,-1         ! for s channel events the first W is attacched to the IS, not a decaying res
            if(abs(idup(i1)).eq.24) then
               nfsres=nfsres+1
               massres(nfsres)=abs(pup(4,i1)**2-pup(1,i1)**2
     +              -pup(2,i1)**2-pup(3,i1)**2)
               do i2=1,3
                  if(mc_fsr_em(i2).lt.0) cycle
                  if(mothup(1,mc_fsr_em(i2)).eq.i1) then
                     emitter_fsr(nfsres)=mc_fsr_em(i2)
                     if(qcdps.and.abs(idup(mc_fsr_em(i2))).lt.6) then ! quark, W > q qbar
                        vetoscale_fsr(nfsres)=scalup ! scale
                     else
                        vetoscale_fsr(nfsres)=mc_fsr_scale(i2)
                     endif
                  endif
               enddo
               if(vetoscale_fsr(nfsres).lt.0d0) then ! no radiation from powheg, set the right minimum
c     if the resonance is mother of leptons use sqrt(rad_ptsqmin_em) (or if there is only qed ps)
c     if the resonance decays in quarks and there is qcd ps, use cm energy
c NOTE that mc_fsr_scale was not negative, but vetoscale_fsr is if there is no emitter                  
                  do i3=1,nup
                     if(mothup(1,i3).eq.i1) then
                        if(  abs(idup(i3)).ge.11.and.
     +                       abs(idup(i3)).le.16) then
                           vetoscale_fsr(nfsres)=sqrt(rad_ptsqmin_em)
                           goto 20
                        elseif(abs(idup(i3)).lt.6) then
                           if(qcdps) then
                              vetoscale_fsr(nfsres)=scalup ! scale
                           else
                              vetoscale_fsr(nfsres)=sqrt(rad_ptsqmin_em)
                           endif
                           goto 20
                        endif
                     endif
                  enddo
               endif
 20            continue
               if(nfsres.eq.3) goto 30
            endif
         enddo
 30      continue
         if(nfsres.ne.2.and.nfsres.ne.3) then
            write(*,*)'error in veto 1'
            stop
         endif


         
         if(powheginput("#LOevents").gt.0) then
c     do not appply any veto
            vetoscale_fsr=scalup
            vetoscale_isr=scalup
         endif
         

c         emitter_fsr(1)=1
c         emitter_fsr(2)=2
c         emitter_fsr(3)=3
         
         if(not_finite_kin_lh()) goto 1

         evtnumber= l


 888     continue
         do m=1,5
c     Insist to shower this event
c     Process event with PYTHIA (.cc file)
            call pythia_next(iret)
            
            
            if(iret.ne.1) then
               if(m.eq.1) then
                  write(*,*) '*** SI: Pythia could not'//
     +                 ' shower this event'
                  call printleshouches
               endif
               write(*,*) '*** SI: retrying'
            else
               exit
            endif
         enddo
         
c If event has been showered, proceed
         if(iret.eq.1) then
c     Read the block of particles after the Pythia shower
c     Store the block in the hepevt common block (to be used in the veto's and analysis)
            call pythia_to_hepevt(nmxhep,nhep,isthep,idhep,jmohep,
     1           jdahep,phep,vhep)
            
            nevhep=nevhep+1
            if (savehistos) then
              call pyanal
            endif
            if(nevhep.gt.0.and.mod(nevhep,100000).eq.0) then
               write(*,*)'*** SI: # of events processed: ',nevhep
               if(savehistos) call pyaend
            endif 

         endif
         if(iret.ne.1) then
           if (savehistos) call pwhgaccumup
         endif

      enddo

      if (savehistos) then
        call pyaend
      endif

      call pythia_close

      write(*,*) '*** SI: Number of input events: ', maxev
      write(*,*) '*** SI: Number of event processed (NEVHEP): ', nevhep
      write(*,*) '*** SI: Success'

      end


      subroutine pyanal
      implicit none
      include 'LesHouches.h'
      include 'hepevt.h'
c     check parameters
      logical verbose
      parameter (verbose=.false.)

c If events are unweighted (have weight 1.0), multiply current weight (xwgtup) by cross section 
c of the current process (xsecup(1))
      if(abs(idwtup).eq.3) xwgtup=xwgtup*xsecup(1)
      call analysis(xwgtup)
      call pwhgaccumup 
      end

      subroutine pyaend
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      include 'pwhg_rnd.h'
      character * 100 infl
      integer nchar
      common/otherfilename/infl,nchar

      call pwhgsetout
      call pwhgtopout(infl(1:nchar)//'output_py8_histos')

      end

      logical function not_finite_kin_lh()
      implicit none
      include 'LesHouches.h'
      logical pwhg_isfinite
      integer j,mu
      do j=1,nup
         do mu=1,5
            if(.not.pwhg_isfinite(pup(mu,j))) goto 998
         enddo
      enddo
      if(.not.pwhg_isfinite(scalup)) goto 998
      not_finite_kin_lh = .false.
      return
 998  not_finite_kin_lh = .true.
      end

      subroutine printleshouches
c useful for debugging
      call lhefwritev(6)
      end

c...lhefeader(nlf)
c...writes event information to a les houches events file on unit nlf. 
      subroutine lhefwritev(nlf)
      implicit none
      integer nlf
      include 'LesHouches.h'
      include 'pwhg_flg.h'
      integer i,j
      write(nlf,'(a)')'<event>'
      write(nlf,210) nup,idprup,xwgtup,scalup,aqedup,aqcdup
      do 200 i=1,nup
         write(nlf,220) idup(i),istup(i),mothup(1,i),
     & mothup(2,i),icolup(1,i),icolup(2,i),(pup(j,i),j=1,5),
     & vtimup(i),spinup(i)
 200  continue
      write(nlf,'(a)')'</event>'      
 210  format(1p,2(1x,i8),4(1x,e12.5))
 220  format(1p,i8,5(1x,i5),5(1x,e16.9),1x,e12.5,1x,e10.3)
      end



c Local version of opencount, based on the box version
c adding flexibility (choose the input file name)
      subroutine opencount_local(inputfilename,maxev,iun)
      implicit none
      character * 100 infl
      integer nchar
      common/otherfilename/infl,nchar
      save /otherfilename/
      integer maxev
      character * 100 inputfilename
      integer ios
      character * 7 string
      integer nev,j,iun,iret
      maxev=0
      call pwhg_io_open_read(trim(inputfilename),iun,ios)

      if(ios.ne.0) then
         write(*,*)' file not found:',inputfilename
         write(*,*)' enter name of event file'
         read(*,'(a)') inputfilename

         infl=trim(inputfilename)
         call charnum(infl,nchar)

         call pwhg_io_open_read(trim(inputfilename),iun,ios)
         if(ios.ne.0) then
            write(*,*) 'cannot open; aborting ...'
            call exit(-1)
         endif
      endif
      write(*,*) ' Opened event file ',inputfilename
      write(*,*) ' Counting events in ', inputfilename
      write(*,*) ' This may take some time...'
 1    continue
      call pwhg_io_read(iun,string,iret)
      if(iret /= 0) goto 2
      if(string.eq.'</event') then
         maxev=maxev+1
         goto 1
      endif
      goto 1
 2    continue
      write(*,*) ' Found ',maxev,' events in file ',inputfilename
      if (maxev.eq.0) then
         write(*,*) ' NO EVENTS!! Program exits'
         call exit(3)
      endif

      call pwhg_io_rewind(iun)
      end


c Local version
      subroutine powheginputstring_local(stringa,stringout,default_value)
      implicit none
      character * (*) stringa,stringout,default_value
      include 'pwhg_pwin.h'
      character * (maxkey) string
      integer j,imode,iret

c     Using input mode 1
      imode = 1

      call assignstring(stringa(2-imode:),string,iret)
      if(iret.lt.0) then
         write(*,*) '*** SI: powheginputstring: keyword too long'
         call exit(-1)
      endif

      do j=1,pwin_numvalues
         if(string.eq.pwin_keywords(j)) then
            if(pwin_stringptr(j) == 0) then
               write(*,*) '*** SI: powheginputstring: error, keyword ',
     1              trim(pwin_keywords(j)),
     2              ' is not associated to a string, exiting ...'
               call exit(-1)
            endif
            
            call assignstring(pwin_strings(pwin_stringptr(j)),
     1           stringout,iret)
            if(iret.lt.0) then
               write(*,*) '*** SI: output string too short'
               call exit(-1)
            endif
            pwin_used(j)=.true.
            write(*,*) '*** SI: powheginput keyword ',string,
     1                    ' set to ','"'//trim(stringout)//'"'
            goto 999
         endif
      enddo

      write(*,*) '*** SI: Keyword ', trim(string), ' not found, ', 
     1      'setting it to: ', default_value
      stringout = default_value

 999  continue

      end

      subroutine charnum(strng,n)
      implicit none
      character*100 strng
      integer n
      do n=1,100
         if(strng(n:n).eq.' ') goto 10
      enddo
 10   n=n-1
      end subroutine charnum

