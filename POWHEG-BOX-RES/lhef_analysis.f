      program leshouchesanal
      implicit none
      include "nlegborn.h"
      include 'LesHouches.h'
      include "pwhg_rad.h"
      include "pwhg_rwl.h"
      integer j,nev
      character * 6 WHCPRG
      common/cWHCPRG/WHCPRG
      integer iun
      common/c_unit/iun
      real * 8 ub_btilde_corr,ub_remn_corr,ub_corr
      real * 8 powheginput
      external powheginput
      
c     let the analysis subroutine know that it is run by this program
      WHCPRG='LHE   '

      ub_btilde_corr = powheginput('#ub_btilde_corr')
      if (ub_btilde_corr < 0d0) then
         ub_btilde_corr = 1d0
      endif
      ub_remn_corr = powheginput('#ub_remn_corr')
      if (ub_remn_corr < 0d0) then
         ub_remn_corr = 1d0
      endif
      
      call opencountunit(nev,iun)
      call upinit
      call init_hist 
      do j=1,nev
         call upevnt
         if(nup.eq.0) then
            write(*,*) ' nup = 0 skipping event'
            goto 111
         endif
c rescale the weight of the event depending on the rad_type (1..btilde, 2..remn)
c   using the ub_..._corr factors
         if (rad_type == 1) then
            ub_corr = ub_btilde_corr
         else if (rad_type == 2) then
            ub_corr = ub_remn_corr
         else 
            ub_corr = 1d0
         endif
         if (rwl_num_weights.gt.0) then
            rwl_weights(1:rwl_num_weights)=
     $           ub_corr * rwl_weights(1:rwl_num_weights)
         endif
         xwgtup = ub_corr * xwgtup
         call lhuptohepevt(j)
         if(abs(idwtup).eq.3) xwgtup=xwgtup*xsecup(1)
         call analysis(xwgtup)
         call pwhgaccumup
         if (mod(j,20000).eq.0) then
            write(*,*) "# of events processed =",j
            call lheanend
         endif
111     continue
      enddo
      call lheanend
      write(*,*) 'EVENTS FOUND : ',nev
      end

      subroutine lheanend
      character * 20 pwgprefix
      character * 100 filename
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      include 'pwhg_rnd.h'
      if(rnd_cwhichseed.ne.'none') then
         filename=pwgprefix(1:lprefix)//'LHEF_analysis-'
     1        //rnd_cwhichseed
      else
         filename=pwgprefix(1:lprefix)//'LHEF_analysis'
      endif
      call pwhgsetout
      call pwhgtopout(filename)
      end
      
      subroutine UPINIT
      implicit none
      integer iun
      common/c_unit/iun
      call lhefreadhdr(iun)
      end

      subroutine UPEVNT
      integer iun
      common/c_unit/iun
      call lhefreadev(iun)
      end

      subroutine lhuptohepevt(n)
      implicit none
      include 'hepevt.h'
      include 'LesHouches.h'
      integer ihep,mu,n
      
      nhep=nup
      nevhep=n
      do ihep=1,nhep
         isthep(ihep)=istup(ihep)
         idhep(ihep)=idup(ihep)
         do mu=1,2
            jmohep(mu,ihep)=mothup(mu,ihep)
         enddo
         do mu=1,5
            phep(mu,ihep)=pup(mu,ihep)
         enddo
      enddo
      end
