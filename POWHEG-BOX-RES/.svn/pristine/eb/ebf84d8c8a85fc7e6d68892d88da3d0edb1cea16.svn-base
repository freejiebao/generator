      subroutine sigvirtual(virt_arr)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_br.h'
      include 'pwhg_flg.h'
      include 'pwhg_cache.h'
      type(cache_pointer), save :: cacheptr
      integer, save :: cacheind
      real * 8 coef,resweight,suppfact
      logical filled(flst_nborn)
      integer jborn

      real * 8 virt_arr(flst_nborn)
      integer iborn,ibornpr,mu,nu,k,j,iret
      logical ini
      data ini/.true./
      save ini
      logical pwhg_isfinite
      external pwhg_isfinite
c Debug; take away in future
      if(flg_novirtual) then
         write(*,*) ' sigvirtual: flg_novirtual = ',flg_novirtual
         call exit(-1)
      endif
c end Debug
      if(ini) then
         if(flg_smartsig) then
            call init_cache_similar('sigvirtual',flst_nborn)
            call get_cache_pointer('sigvirtual',cacheind,cacheptr)
         endif         
         ini=.false.
      endif
      filled = .false.
      do iborn=1,flst_nborn
         if(flst_ibornresgroup.ne.flst_bornresgroup(iborn)) then
            virt_arr(iborn) = 0
            cycle
         endif
         if(flg_smartsig) then
            call get_cache_value(cacheptr,iborn,jborn,coef)
         else
            jborn = - 1
         endif
         
         if(jborn.lt.0) then
            flst_cur_iborn = iborn
            call setvirtual0(kn_cmpborn,iborn,virt_arr(iborn))
c     check if virt_arr(iborn) is finite
                  if (.not.pwhg_isfinite(virt_arr(iborn))) 
     1                 virt_arr(iborn)=0d0
            virt_arr(iborn)=virt_arr(iborn)/(2*kn_sborn)
            filled(iborn) = .true.
            call bornresweight(iborn,resweight)
            virt_arr(iborn)=virt_arr(iborn) * resweight * flst_bornmult(iborn)
         else
            if(coef == 0) then
               virt_arr(iborn) = 0
            elseif(.not.filled(jborn)) then
               write(*,*) ' sigborn: smartsig machinery failure ...'
               write(*,*) ' exiting ...'
               call exit(-1)
            else
               virt_arr(iborn)=virt_arr(jborn)*coef
            endif
            filled(iborn) = .true.
         endif
      enddo

      if(flg_smartsig) then
         call store_cache_similar(cacheptr,virt_arr,filled)
      endif     

      call global_suppression('b',suppfact)
      virt_arr(1:flst_nborn) = virt_arr(1:flst_nborn) * suppfact

      end

      subroutine setvirtual0(p,iborn,virt)
c provide the flux factor to the user Born routine
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      integer nlegs
      parameter (nlegs=nlegborn)
      real * 8 p(0:3,nlegs)
      integer iborn
      real * 8 virt
c
      real * 8 pborn(0:3,nlegs)
      integer j,k,mu,nu
      logical pwhg_isfinite
      external pwhg_isfinite
      integer bflav(nlegborn),isfsparticles(nlegborn),isfslength
      call getisfsparticles(flst_bornlength(iborn),flst_born(:,iborn),flst_bornres(:,iborn),
     1     isfslength,isfsparticles)
      do j=1,isfslength
         bflav(j)=flst_born(isfsparticles(j),iborn)
         pborn(:,j)=p(:,isfsparticles(j))
      enddo
      call setvirtual(pborn,bflav,virt)
      end
