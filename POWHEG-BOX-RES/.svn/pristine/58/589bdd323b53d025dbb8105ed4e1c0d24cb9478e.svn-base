      program main_pythia
      implicit none
      include 'LesHouches.h'
      include 'hepevt.h'
 
      integer iev,temp,i
      external pydata
      character * 6 WHCPRG
      common/cWHCPRG/WHCPRG
      integer maxpr
      parameter (maxpr=6)
c     mcmaxev
      integer maxev
      common/mcmaxev/maxev

c     WHCPRG tells the analysis subroutine which program is calling the
c     analysis
      WHCPRG='PYTHIA'

      call getmaxev(maxev)

c Set up tune
      call setup_PYTHIA_tune

c Set up PYTHIA to accept user processes
      call PYINIT('USER','','',0d0)
      
c Set up initial parameter      
      call setup_PYTHIA_parameters
      
      call PYABEG
      nevhep=0
      do iev=1,maxev
         call pyevnt
         if(nup.eq.0) then
            write(*,*) ' no event generated; skipping'
            goto 111
         endif
c     Convert from PYJETS event record to HEPEVT event record
         temp=nevhep
         call pyhepc(1)
         nevhep=temp
C     Print out the event record
         IF (IEV.le.maxpr) THEN 
c     list the event
c            call pystat(2)      ! print cross sections, widths, branchings,...
c            CALL PYLIST(7)      ! print the HEPEUP common block
             CALL PYLIST(5)      ! print the HEPEVT common block
c            CALL PYLIST(2)      ! print the event
c            call PYLIST(1)      ! as PYLIST(2) but with less information
         ENDIF
         
         call PYANAL
          IF(nevhep.gt.0.and.MOD(nevhep,20000).EQ.0) THEN
            WRITE(*,*)'# of events processed=',iev
            WRITE(*,*)'# of events generated=',NEVHEP
            CALL PYAEND
         ENDIF 
      enddo
 111  continue
      write(*,*) 'At the end NEVHEP is ',nevhep
!:      write(*,*) 'At the end: #warnings= ',mstu(27),' #errors= ',mstu(23)
C---USER'S TERMINAL CALCULATIONS
      call PYAEND
      END


      subroutine savelhe
      call saverestorelhe(0)
      end

      subroutine restorelhe
      call saverestorelhe(1)
      end

      subroutine saverestorelhe(j)
      integer j
      include 'LesHouches.h'
      integer, save :: s_idbmup(2),s_pdfgup(2),s_pdfsup(2),s_idwtup,s_nprup,s_lprup(maxpup)
      double precision s_ebmup(2),s_xsecup(maxpup),s_xerrup(maxpup),s_xmaxup(maxpup)
      integer s_nup,s_idprup,s_idup(maxnup),s_istup(maxnup),s_mothup(2,maxnup),s_icolup(2,maxnup)
      double precision s_xwgtup,s_scalup,s_aqedup,s_aqcdup,s_pup(5,maxnup),s_vtimup(maxnup),s_spinup(maxnup)
      integer, save:: s_jheprup(12+7*maxpup),s_jhepeup(10+20*maxnup)
      integer jheprup(12+7*maxpup),jhepeup(10+20*maxnup)
      equivalence (jheprup(1),idbmup(1)), (jhepeup(1),nup)
      integer itmp
      integer ispinup(2)
      equivalence (ispinup,spinup(maxnup))
c     check that we counted right
      itmp = lprup(maxpup)
      jheprup(size(jheprup))=23244512
      if(lprup(maxpup) /= 23244512) then
         write(*,*) ' saverestorelhe: error in jheprup, exiting ...'
      endif
      lprup(maxpup)=itmp

      itmp = ispinup(2)
      jhepeup(size(jhepeup))=23244512
      if(ispinup(2) /= 23244512) then
         write(*,*) ' saverestorelhe: error in jheprup, exiting ...'
      endif
      ispinup(2)=itmp

      if(j==0) then
         s_idbmup=idbmup
         s_pdfgup=pdfgup
         s_pdfsup=pdfsup
         s_idwtup=idwtup
         s_nprup=nprup
         s_lprup=lprup
         s_ebmup=ebmup
         s_xsecup=xsecup
         s_xerrup=xerrup
         s_xmaxup=xmaxup

         s_nup=nup
         s_idprup=idprup
         s_idup=idup
         s_istup=istup
         s_mothup=mothup
         s_icolup=icolup
         s_xwgtup=xwgtup
         s_scalup=scalup
         s_aqedup=aqedup
         s_aqcdup=aqcdup
         s_pup=pup
         s_vtimup=vtimup
         s_spinup=spinup

         s_jheprup = jheprup
         s_jhepeup = jhepeup
      else
c     restore:
         idbmup=s_idbmup
         pdfgup=s_pdfgup
         pdfsup=s_pdfsup
         idwtup=s_idwtup
         nprup=s_nprup
         lprup=s_lprup
         ebmup=s_ebmup
         xsecup=s_xsecup
         xerrup=s_xerrup
         xmaxup=xmaxup

         nup=s_nup
         idprup=s_idprup
         idup=s_idup
         istup=s_istup
         mothup=s_mothup
         icolup=s_icolup
         xwgtup=s_xwgtup
         scalup=s_scalup
         aqedup=s_aqedup
         aqcdup=s_aqcdup
         pup=s_pup
         vtimup=s_vtimup
         spinup=s_spinup

         do k=1,size(jheprup)
            if(jheprup(k) /= s_jheprup(k)) then
               write(*,*) ' saverestorelhe: error in jheprup, exiting ...'
               call exit(-1)
            endif
         enddo
         do k=1,size(jhepeup)
            if(jhepeup(k) /= s_jhepeup(k)) then
               write(*,*) ' saverestorelhe: error in jheprup, exiting ...'
               call exit(-1)
            endif
         enddo
      endif
      end
      

