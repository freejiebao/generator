      integer function sigregular(iresgroup,xx,ww,ifirst,imode,retval,retval0)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      include 'pwhg_pdf.h'
      include 'pwhg_math.h'
      include 'pwhg_cache.h'
      include 'pwhg_physpar.h'
      type(cache_pointer), save :: cacheptr
      integer iresgroup,ifirst,imode
      real * 8 retval,retval0,xx(ndiminteg),ww,weight
      real * 8, save ::  results(maxprocreal)
      real * 8 jacreal
      logical filled(flst_nregular)
      integer ireg,jreg,j
      real * 8 coef
      logical need_phsp
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton)
      real * 8 realsupp,regsupp,regvalue_plot
      save regsupp
      integer, save :: cacheind
      logical ini
      data ini/.true./
      save ini
      logical pwhg_isfinite
      procedure() :: pwhg_isfinite
      if(ini) then
         if(flg_smartsig) then
            call init_cache_similar('sigregular',flst_nregular)
            call get_cache_pointer('sigregular',cacheind,cacheptr)
         endif
         ini = .false.
      endif

      flst_iregularresgroup = iresgroup
      sigregular = 1
      if(ifirst.eq.2) then
         if(.not.flg_ingen) then
            call adduptotals(results,flst_nregular)
         else
c the array is useful to pick a flavour configuration when generating events
            call storeradarray(results)
         endif
         retval = sum(results)
c     use saved regsupp
         regvalue_plot = retval/regsupp
         call analysis_driver(regvalue_plot,2)
         retval = sum(abs(results))
         if(flg_nlotest) call pwhgaccumup
         return
      endif

      need_phsp = .true.

      filled = .false.

      do ireg = 1,flst_nregular
         if(flst_regularresgroup(ireg).eq.flst_iregularresgroup) then
            flst_ireallength = flst_regularlength(ireg)
            if(need_phsp) then
               call genphasespace(xx,flst_regularlength(ireg),flst_regular(:,ireg),
     1              flst_regularres(:,ireg),kn_beams,jacreal,
     1              kn_x1,kn_x2,kn_sreal,kn_cmpreal,kn_preal)
               call setscalesregular
               call pdfcall(1,kn_x1,pdf1)
               call pdfcall(2,kn_x2,pdf2)
               do j=1,flst_ireallength
                  kn_masses(j) = physpar_phspmasses(flst_regular(j,ireg))
               enddo
               need_phsp = .false.
            endif
            if(flg_smartsig) then
               call get_cache_value(cacheptr,ireg,jreg,coef)
            else
               jreg = - 1
            endif
            if(jreg.gt.0) then
               if(coef == 0) then
                  results(ireg) = 0
               elseif(.not.filled(jreg)) then
                  write(*,*) ' sigregular: smartsig machinery failure ...'
                  write(*,*) ' exiting ...'
                  call exit(-1)
               else
                  results(ireg) = results(jreg) * coef
               endif
            else
               filled(ireg) = .true.
               call realgr(flst_regularlength(ireg),flst_regular(:,ireg),
     1           flst_regularres(:,ireg),kn_cmpreal,results(ireg))
c the resweight factor should be added here.
               call regularresweight(ireg,weight)
               results(ireg) = results(ireg) * weight
               if(.not.pwhg_isfinite(results(ireg))) then
                  results = 0
                  return
               endif
            endif
         else
            results(ireg) = 0
         endif
      enddo

      if(flg_smartsig) then
         call store_cache_similar(cacheptr,results,filled)
      endif

      call global_suppression('r',realsupp)

      call regular_suppression(regsupp)

      do ireg = 1,flst_nregular
         results(ireg) = results(ireg) *
     1        pdf1(flst_regular(1,ireg))*pdf2(flst_regular(2,ireg))
     2        * jacreal * hc2 * ww * realsupp * regsupp *
     3        flst_regularmult(ireg)
      enddo

      end
