      subroutine btildeborn(res)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_br.h'
      include 'pwhg_flg.h'
      include 'pwhg_pdf.h'
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton)
      real * 8 res(flst_nborn),tot,rescfac
      integer j
      if(.not.flg_minlo) then
         rescfac = 1
         call pdfcall(1,kn_xb1,pdf1)
         call pdfcall(2,kn_xb2,pdf2)
      endif
      tot=0
      do j=1,flst_nborn
         if(flg_minlo) then
            call setlocalscales(j,1,rescfac)
            call pdfcall(1,kn_xb1,pdf1)
            call pdfcall(2,kn_xb2,pdf2)
         endif
         res(j)=br_born(j) *
     1  pdf1(flst_born(1,j))*pdf2(flst_born(2,j))*kn_jacborn*rescfac
         tot=tot+res(j)
c     if one wants to do only the integration over the whole phase space, then
c     uncomment the following (with or without the flux factor 1/(2*kn_sborn)
c        
c         res(j)=kn_jacborn/(2*kn_sborn)/flst_nborn
      enddo
      end

      subroutine sigborn_rad(born)
      implicit none
      real * 8 born
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_br.h'
      include 'pwhg_rad.h'
      include 'pwhg_pdf.h'
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton),
     2         bornjk(nlegborn,nlegborn),bmunu(0:3,0:3,nlegborn),
     3         suppfact
      call pdfcall(1,kn_xb1,pdf1)
      call pdfcall(2,kn_xb2,pdf2)
      flst_cur_iborn = rad_ubornsubp
      call setborn0(kn_cmpborn,rad_ubornsubp,born,
     1        bornjk,bmunu)
c Store in the br_born arrays; they are used to compute
c collinear and soft approximations, and affect the subtraction
c of the remnant component.
      br_born(rad_ubornsubp)=born
      br_bornjk(:,:,rad_ubornsubp)=bornjk
      br_bmunu(:,:,:,rad_ubornsubp)=bmunu

      call global_suppression('b',suppfact)
      br_born(rad_ubornsubp) = br_born(rad_ubornsubp) * suppfact
      br_bornjk(:,:,rad_ubornsubp) = br_bornjk(:,:,rad_ubornsubp) * suppfact
      br_bmunu(:,:,:,rad_ubornsubp) = br_bmunu(:,:,:,rad_ubornsubp) * suppfact

      born=born * suppfact *
     1  pdf1(flst_born(1,rad_ubornsubp))*pdf2(flst_born(2,rad_ubornsubp))
      end

      subroutine allborn
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_br.h'
      include 'pwhg_flg.h'
      include 'pwhg_cache.h'
      type(cache_pointer),save  :: cacheptr
      integer, save :: cacheind
      real * 8 coef,suppfact
      logical filled(flst_nborn)
      integer iborn,jborn
      logical ini
      data ini/.true./
      save ini
      if(ini) then
         if(flg_smartsig) then
            call init_cache_similar('allborn',flst_nborn)
            call get_cache_pointer('allborn',cacheind,cacheptr)
         endif
         ini=.false.
      endif
      filled = .false.
      do iborn=1,flst_nborn
c Debug; take away in future
         if(.not. flst_ibornresgroup.ge.1) then
            write(*,*) ' allborn: flst_ibornresgroup = ',flst_ibornresgroup
            call exit(-1)
         endif
c end Debug
         if(flst_ibornresgroup.ne.flst_bornresgroup(iborn)) then
            br_born(iborn) = 0
            br_bmunu(:,:,:,iborn)=0
            br_bornjk(:,:,iborn)=0
            cycle
         endif
         
         if(flg_smartsig) then
            call get_cache_value(cacheptr,iborn,jborn,coef)
         else
            jborn = - 1
         endif

         if(jborn.gt.0) then
            filled(iborn) = .true.
            if(coef == 0) then
               br_born(iborn) = 0
               br_bornjk(:,:,iborn) = 0
               br_bmunu(:,:,:,iborn) = 0
            elseif(.not.filled(jborn)) then
               write(*,*) ' sigborn: smartsig machinery failure ...'
               write(*,*) ' exiting ...'
               call exit(-1)
            else
               br_born(iborn)=br_born(jborn)*coef
               br_bornjk(:,:,iborn)=br_bornjk(:,:,jborn)*coef
               br_bmunu(:,:,:,iborn) = br_bmunu(:,:,:,jborn)*coef
            endif
         else
            filled(iborn) = .true.
            flst_cur_iborn = iborn
            call setborn0(kn_cmpborn,iborn,br_born(iborn),
     1           br_bornjk(:,:,iborn),br_bmunu(:,:,:,iborn))
         endif

      enddo

      if(flg_smartsig) then
         call store_cache_similar(cacheptr,br_born,filled)
      endif     

      call global_suppression('b',suppfact)
      br_born(1:flst_nborn) = br_born(1:flst_nborn) * suppfact
      br_bornjk(:,:,1:flst_nborn) = br_bornjk(:,:,1:flst_nborn) * suppfact
      br_bmunu(:,:,:,1:flst_nborn) = br_bmunu(:,:,:,1:flst_nborn) * suppfact

      end

      subroutine setborn0(p,iborn,born,bornjk,bmunu)
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
      real * 8 born,bornjk(nlegs,nlegs),bmunu(0:3,0:3,nlegs)
c flst_numfsr is the number of final state particles in the real
c graph. flst_numfb+2 is the number of initial state plus final state
c particles in the Born graph.
      real * 8 pborn(0:3,flst_numfsb+2)
      real * 8 bornjk0(flst_numfsb+2,flst_numfsb+2),bmunu0(0:3,0:3,flst_numfsb+2)
      real * 8 resweight
      integer j,k,mu,nu
      logical pwhg_isfinite
      external pwhg_isfinite
      integer bflav(nlegborn),is_fs(nlegborn),isfslength
      call getisfsparticles(flst_bornlength(iborn),flst_born(:,iborn),flst_bornres(:,iborn),
     1     isfslength,is_fs)
      if(isfslength /= flst_numfsb+2) then
         write(*,*) ' Error in setborn0: length mismatch'
         call exit(-1)
      endif
      do j=1,isfslength
         bflav(j)=flst_born(is_fs(j),iborn)
         pborn(:,j)=p(:,is_fs(j))
      enddo
      call setborn(pborn,bflav,born,bornjk0,bmunu0)
c     check if born, bornjk and bmunu are finite
      if (.not.pwhg_isfinite(born)) born=0d0
      do j=1,isfslength
         do mu=0,3
            do nu=0,3
               if (.not.pwhg_isfinite(bmunu0(mu,nu,j))) 
     $               bmunu0(mu,nu,j)=0d0
            enddo
         enddo
      enddo
      do j=1,isfslength
         do k=1,isfslength
            if (.not.pwhg_isfinite(bornjk0(j,k))) bornjk0(j,k)=0d0
         enddo
      enddo
c
      born = born / (2*kn_sborn)
      bmunu0 = bmunu0 / (2*kn_sborn)
      bornjk0 = bornjk0 / (2*kn_sborn)

      bmunu = 0
      bornjk = 0
      do j=1,isfslength
         bmunu(:,:,is_fs(j))=bmunu0(:,:,j)
         do k=1,isfslength
            bornjk(is_fs(j),is_fs(k))=bornjk0(j,k)
         enddo
      enddo

      call bornresweight(iborn,resweight)
      born = born * resweight * flst_bornmult(iborn)
      bmunu = bmunu * resweight * flst_bornmult(iborn)
      bornjk = bornjk * resweight * flst_bornmult(iborn)

      end

      subroutine getisfsparticles(length,flav,res,isfslength,is_fs)
      implicit none
c given a flavour list with resonance assignment, strip away the resonances
      integer length,flav(length),res(length),isfslength,is_fs(length)
      logical markres(length)
      integer j
      markres = .false.
      do j=1,length
         if(res(j).ne.0) markres(res(j))=.true.
      enddo
      isfslength = 0
      do j=1,length
         if(.not.markres(j)) then
            isfslength = isfslength + 1
            is_fs(isfslength) = j
         endif
      enddo
      end


c     Given a flavour list of length "length", its resonance structure
c     and its kinematics, returns the flavour structure and momenta of
c     the final-state particles, i.e. resonances have been stripped off
      subroutine get_fs_particles_momenta(length,flav,res,p,
     $     length_out,flav_out,p_out)
      implicit none
      integer length,flav(length),res(length)
      real * 8 p(0:3,length)
      integer length_out,flav_out(length)
      real * 8 p_out(0:3,length)
      integer is_fs(length),j     
      is_fs = 0
      p_out = 0
      flav_out = 0
      length_out = 0
      call getisfsparticles(length,flav,res,length_out,is_fs)
      do j=1,length_out
         flav_out(j) = flav(is_fs(j))
         p_out(:,j) = p(:,is_fs(j))
      enddo
      end
