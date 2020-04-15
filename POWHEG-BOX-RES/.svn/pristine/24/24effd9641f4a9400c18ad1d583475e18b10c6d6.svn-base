      subroutine gen_btilde_subp
      implicit none
      call gen_btilde_subp_all('btilde')
      end

      subroutine gen_btildeborn_subp
      implicit none
      call gen_btilde_subp_all('btildeborn')
      end


      subroutine gen_btilde_subp_all(id)
      implicit none
      character *(*) id
      integer ibornsubp,isign
      call choosesubproc(id,ibornsubp,isign)
      call setradkinreg(ibornsubp,isign)
      end

      subroutine setradkinreg(ibornsubp,isign)
      implicit none
      integer ibornsubp,isign
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      integer j,alr,em
      rad_kinreg_on=.false.
      rad_nkinreg = 0
      rad_ubornsubp = ibornsubp
      rad_sign = isign
      rad_alr_nlist=flst_born2alr(0,rad_ubornsubp)
      do j=1,rad_alr_nlist
         alr=flst_born2alr(j,rad_ubornsubp)
         em=flst_emitter(alr)
         rad_alr_list(j)=alr
         if(em.le.2) then
            rad_kinreg_on(1)=.true.
            rad_nkinreg = max(rad_nkinreg,1)
         else
            rad_kinreg_on(em-flst_lightpart+2)=.true.
            rad_nkinreg = max(rad_nkinreg,em-flst_lightpart+2)
         endif
      enddo
      end

      subroutine gen_rad_subp
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      integer j
      call pick_random(rad_alr_nlist,rad_real_arr,j)
      rad_alrsubp=rad_alr_list(j)
      end

      subroutine pick_random(n,r,jret)
      implicit none
      integer n,jret
      real * 8 r(n)
      real * 8 tot(0:n)
      integer j
      real * 8 ran,random
      tot(0)=0
      do j=1,n
         tot(j)=tot(j-1)+r(j)
      enddo
      ran=tot(n)*random()
      do j=1,n
         if(tot(j).gt.ran) then
            jret=j
            return
         endif
      enddo
      write(*,*) ' ***********************************'
      write(*,*) ' POWHEGBOX:pick_random: could not pick a value'
      write(*,*) ' set choice to 1'
      write(*,*) ' ***********************************'
      jret=1
c      call exit(-1)
      end
      

      subroutine gen_remnant_subp
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      integer iret
      real * 8 dum1,dum2,dum3,dum4
      real * 8 random
      external random
      call choosesubproc('remn',rad_alrsubp,rad_sign)
      rad_ubornsubp=flst_alr2born(rad_alrsubp)
      kn_emitter=flst_emitter(rad_alrsubp)
      if(kn_emitter < 3) then
         rad_kinreg=1
      else
         rad_kinreg=kn_emitter+2-flst_lightpart
      endif
      if(kn_emitter.le.2) then
         call gen_real_phsp_isr(rad_xradremn,dum1,dum2,dum3,dum4)
      else
         call gen_real_phsp_fsr(rad_xradremn,dum1,dum2,dum3)
      endif
      end

      subroutine gen_regular_subp
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      integer iret
      real * 8 dum1,dum2,dum3,dum4
      real * 8 random
      external random
      call choosesubproc('reg',rad_regularsubp,rad_sign)
      end
