c Function to be integrated with mint, used to generate
c non-singular contributions using standard mint-gen method
c These contributions arise from real graphs without singular regions,
c or, when damping of R/B value is adopted, from the remnant of the
c damping
      function sigremnant(iresgroup,xx,ww,ifirst,imode,retval,retval0)
c retval is the function return value
c retvavl0 is an 'avatar' function the has similar value, but is much
c easier to compute (i.e. the Born term in this case)
c imode = 0 compute retval0 only.
c imode = 1 compute retval, retval0
c return value: output, 0: success; 1: retval0 was not computed
c                 (this function does not support an avatar function)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_flg.h'
      include 'pwhg_math.h'
      integer sigremnant,iresgroup,imode
      real * 8 retval,retval0,xx(ndiminteg),ww
      integer ifirst
      real * 8 xrad(3)
      real * 8 xborn(ndiminteg-3)
      integer j,alr
      real * 8 ttt
      real * 8 jac_over_csi,jac_over_csi_p,jac_over_csi_m,
     1         jac_over_csi_s,jac_over_csi_coll
      real * 8, save ::  rrr_damp_rem_arr(maxalr),rrr_damp_rem_tot
      real * 8 xjac,suppfact_isr,suppfact_fsr
      logical valid_emitter
      external valid_emitter
      logical pwhg_isfinite
      external pwhg_isfinite
      flst_ibornresgroup = iresgroup
      call setup_resgroupstuff
      sigremnant = 1
      if(ifirst.eq.2) then
         retval=rrr_damp_rem_tot
         if(.not.flg_ingen) then
            call adduptotals(rrr_damp_rem_arr,flst_nalr)
         else
c the array is useful to pick a flavour configuration when generating events
            call storeradarray(rrr_damp_rem_arr)
         endif
         if(flg_nlotest) call pwhgaccumup
         return
      endif
      do j=1,ndiminteg-3
         xborn(j)=xx(j)
      enddo
      do j=1,3
         xrad(j)=xx(ndiminteg-3 + j)
         rad_xradremn(j)=xrad(j)
      enddo
      kn_emitter=0
      call gen_born_phsp(xborn)
c set scales
      call setscalesbtilde
c the following is needed to compute soft and collinear limits
      call allborn
      if(flg_withdamp) then
         if(valid_emitter(0).or.
     1        valid_emitter(1).or.valid_emitter(2)) then
            call gen_real_phsp_isr(xrad,
     1        jac_over_csi,jac_over_csi_p,jac_over_csi_m,jac_over_csi_s)
            xjac=jac_over_csi*kn_csi*kn_csimax*kn_jacborn*ww*hc2
c remnant suppression might depend of real-emission kinematics. For ISR it does
c not depend on the emitter and can be evaluated here
            call rmn_suppression(suppfact_isr)
         endif

         rrr_damp_rem_tot=0
         do alr=1,flst_nalr
            rrr_damp_rem_arr(alr)=0
         enddo
         do kn_emitter=0,nlegborn
            if(valid_emitter(kn_emitter)) then
               if(kn_emitter.le.2) then
c     No need to generate phase space; it is already available
                  call setscalesbtlreal
                  call sigreal_damp_rem(xjac,suppfact_isr,ttt,
     &                 rrr_damp_rem_arr)
                  if(flg_nlotest) then
                     call analysis_driver(ttt,1)
                  endif
                  rrr_damp_rem_tot=rrr_damp_rem_tot+ttt*suppfact_isr
               else
                  call gen_real_phsp_fsr(xrad,
     1                 jac_over_csi,jac_over_csi_coll,jac_over_csi_s)
                  xjac=jac_over_csi*kn_csi*kn_csimax
     2                *kn_jacborn*ww*hc2

                  call setscalesbtlreal
c remnant suppression might depend on real-emission kinematics. For FSR it might
c depend on the emitter need to be evaluated here
                  call rmn_suppression(suppfact_fsr)
                  call sigreal_damp_rem(xjac,suppfact_fsr,ttt,
     &                 rrr_damp_rem_arr)
                  if(flg_nlotest) then
                     call analysis_driver(ttt,1)
                  endif
                  rrr_damp_rem_tot=rrr_damp_rem_tot+ttt*suppfact_fsr
               endif
            endif
         enddo
      else
         rrr_damp_rem_tot=0
      endif

      if (.not.pwhg_isfinite(rrr_damp_rem_tot)) then
         rrr_damp_rem_tot=0d0
         rrr_damp_rem_arr=0d0
      endif

      retval = rrr_damp_rem_tot

      end

      subroutine sigreal_damp_rem(xjac,suppfact,sig,r1)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      real * 8 xjac,suppfact,sig
      real * 8 r0(maxalr),r1(maxalr)
      integer alr
      sig=0
      call sigreal_btl0(r0,1)
      do alr=1,flst_nalr
         if(kn_emitter.eq.flst_emitter(alr)) then
            if(kn_emitter.le.2) then
               r0(alr)=r0(alr)/((1-kn_y**2)*kn_csi**2)
            else
               r0(alr)=r0(alr)/((1-kn_y)*kn_csi**2)
            endif
            r0(alr)=r0(alr)*xjac
c     The integrated value r1 is suppressed
            r1(alr)=r1(alr)+r0(alr)*suppfact
c     sig is passed to the analysis (no suppression)
            sig=sig+r0(alr)
         endif
      enddo
      end

      
