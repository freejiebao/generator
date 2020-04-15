c TODO: decide form of resonance enhancement factors;
c should be (s+m^2)^2/((s-m^2)^2+...) rather than only m^4
c in the numerator


      subroutine realresweight_soft(alr,weight)
      integer alr
      real * 8 weight
      call realresweight0(0,alr,weight)
      end

      subroutine realresweight(alr,weight)
      integer alr
      real * 8 weight
      call realresweight0(1,alr,weight)
      end



      subroutine realresweight0(isoftflag,alr,weight)
      implicit none
      integer isoftflag,alr
      real * 8 weight
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      integer ihist
      integer numreshist,numsingreg,jsing,alrlen,ptr
      real * 8 res_pfactors(flst_numrhreal),res_pdfactors(flst_numrhreal),
     1     res_dijfactors(maxregions,flst_numrhreal)
      integer isoftflagc
      common/local_isoftflagc/isoftflagc
      real * 8  dijtermx
      procedure() :: dijtermx
      isoftflagc = isoftflag
      alrlen = flst_alrlength(alr)
      numreshist = flst_alrnumrhptrs(alr)
c go through all resonance histories
      do ihist = 1,numreshist
         ptr = flst_alrrhptrs(ihist,alr)
         numsingreg = flst_rhrealnumreg(ptr)
         if(numsingreg.eq.0.and.isoftflagc.eq.0) cycle
         call fillpcmblock(alrlen,flst_rhreallength(ptr),
     1                    flst_rhreal(:,ptr),
     2                    flst_rhrealres(:,ptr))
         call comprespfactor(flst_rhreal(:,ptr),res_pfactors(ihist))
         if(numsingreg.gt.0) then
            call compresdijfactors(flst_rhreal(:,ptr),
     1           flst_rhrealres(:,ptr),
     2           numsingreg,
     3           flst_rhrealreg(:,:,ptr),
     4           res_dijfactors(:,ihist))
            res_pdfactors(ihist) = res_pfactors(ihist) *
     1           sum(res_dijfactors(1:numsingreg,ihist))
         else
            res_pdfactors(ihist) = res_pfactors(ihist) / dijtermx(-1)
         endif
      enddo

      ptr = flst_alrrhptrs(1,alr)
      numsingreg = flst_rhrealnumreg(ptr)

      do jsing = 1,numsingreg
         if((flst_rhrealreg(1,jsing,ptr) .eq. flst_emitter(alr).and.flst_rhrealreg(2,jsing,ptr).eq.alrlen)
     1  .or.(flst_rhrealreg(2,jsing,ptr) .eq. flst_emitter(alr).and.flst_rhrealreg(1,jsing,ptr).eq.alrlen)) then
            exit
         endif
      enddo
      if(jsing.eq.numsingreg+1) then
         write(*,*) ' realresweight0: cannot find current region'
         write(*,*) ' exiting ...'
         call exit(-1)
      endif
c the first element in flst_alrrhptrs corresponds to the resonance structure of
c the current alr.
      weight = res_pfactors(1)*res_dijfactors(jsing,1)/sum(res_pdfactors(1:numreshist))

      end




      subroutine regularresweight(ireg,weight)
      implicit none
      integer ireg
      real * 8 weight
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_par.h'
      integer ihist
      integer numreshist,numsingreg,reglen,ptr
      real * 8 res_pfactors(flst_numrhreal),res_pdfactors(flst_numrhreal),
     1     res_dijfactors(maxregions,flst_numrhreal)
      integer isoftflagc
      common/local_isoftflagc/isoftflagc
      real * 8  dijtermx
      procedure() :: dijtermx
c This has side effects, now we need full real, no soft
      isoftflagc = 1
      reglen = flst_regularlength(ireg)
      numreshist = flst_regularnumrhptrs(ireg)
c go through all resonance histories
      do ihist = 1,numreshist
         ptr = flst_regularrhptrs(ihist,ireg)
         numsingreg = flst_rhrealnumreg(ptr)
         call fillpcmblock(reglen,flst_rhreallength(ptr),
     1                    flst_rhreal(:,ptr),
     2                    flst_rhrealres(:,ptr))
         call comprespfactor(flst_rhreal(:,ptr),res_pfactors(ihist))
         call compresdijfactors(flst_rhreal(:,ptr),
     1                          flst_rhrealres(:,ptr),
     2                          numsingreg,
     3                          flst_rhrealreg(:,:,ptr),
     4                          res_dijfactors(:,ihist))
         if(numsingreg.gt.0) then
            res_pdfactors(ihist) = res_pfactors(ihist) *
     1           sum(res_dijfactors(1:numsingreg,ihist))
         else
c dijterm called witjh -1 yields a typical scale of the process
            res_pdfactors(ihist) = res_pfactors(ihist) / dijtermx(-1)
         endif
      enddo

c the first element in flst_regularrhptrs corresponds to the resonance structure of
c the current reg.
      weight = res_pfactors(1)/ dijtermx(-1)/sum(res_pdfactors(1:numreshist))

      end



      subroutine fillpcmblock(alrlen,alen,a,ares)
      implicit none
      integer alrlen,alen,a(alen),ares(alen)
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'      
      real * 8 pcm(0:3,1:nlegreal)
      integer pcmlen
      common/local_pcm/pcm,pcmlen
      integer isoftflagc
      common/local_isoftflagc/isoftflagc
      integer firstfs,firstfsalr,k,moth
      pcmlen = alen
      firstfs = alen - flst_numfsr + 1
      firstfsalr = alrlen - flst_numfsr + 1
      if(isoftflagc.eq.0) then
c soft limit case
         pcm(:,1:2) = kn_cmpborn(:,1:2)
         pcm(:,firstfs:alen-1) = kn_cmpborn(:,firstfsalr:alrlen-1)
         pcm(:,alen) = kn_softvec
         if(firstfs >=4) then
            pcm(:,3:firstfs-1) = 0         
         endif
      else
         pcm(:,1:2) = kn_cmpreal(:,1:2)
         pcm(:,firstfs:alen) = kn_cmpreal(:,firstfsalr:alrlen)
         if(firstfs >=4) then
            pcm(:,3:firstfs-1) = 0
         endif
      endif
c Sum momenta of each final state particle to all its ancestors.
      do k=firstfs,alen
         if(isoftflagc.eq.0.and.k.eq.alen) cycle
         moth = ares(k)
         do while(moth.ne.0)
            pcm(:,moth) = pcm(:,moth) + pcm(:,k)
            moth = ares(moth)
         enddo
      enddo
      end



      subroutine comprespfactor(a,factor)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_physpar.h'
      real * 8 pcm(0:3,1:nlegreal)
      integer pcmlen
      common/local_pcm/pcm,pcmlen
      integer a(pcmlen)
      integer firstfs,k
      real * 8 factor
      real * 8 mass,width,virt
      real * 8 momsq03
      external momsq03
      factor = 1
      firstfs = pcmlen - flst_numfsr + 1
c Now all resonances have the correct 4-momentum
      do k = 3,firstfs-1
         mass = physpar_pdgmasses(a(k))
         width = physpar_pdgwidths(a(k))
         virt = momsq03(pcm(:,k))
         factor = factor*mass**4/((virt-mass**2)**2 + (mass*width)**2)
      enddo
      end

      subroutine compresdijfactors(a,ares,nregions,regions,factors)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      real * 8 pcm(0:3,1:nlegreal)
      integer pcmlen
      common/local_pcm/pcm,pcmlen
      integer a(pcmlen),ares(pcmlen),nregions,regions(2,nregions)
      real * 8 factors(nregions)
      real * 8  dijtermx
      external dijtermx
      integer iregion,em1,em2
      integer isoftflagc
      common/local_isoftflagc/isoftflagc
      do iregion = 1,nregions
         em1 = regions(1,iregion)
         em2 = regions(2,iregion)
         if(isoftflagc.eq.0) then
            if(em2 .eq. pcmlen) then
               factors(iregion) = 1/dijtermx(em1,em2,a,ares)
            elseif(em1.eq.pcmlen) then
               factors(iregion) = 1/dijtermx(em2,em1,a,ares)
            else
               factors(iregion) = 0
            endif
         else
            factors(iregion) = 1/dijtermx(em1,em2,a,ares)
         endif
      enddo
      end

      subroutine bornresweight(iborn,weight)
      implicit none
      integer iborn
      real * 8 weight
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      integer len0,len,numreshist,ihist,ptr
      real * 8 factor,factortmp,factortot
      factortot = 0
      len0 = flst_bornlength(iborn)
      numreshist = flst_bornnumrhptrs(iborn)
      do ihist=1,numreshist
         ptr = flst_bornrhptrs(ihist,iborn)
         len = flst_rhbornlength(ptr)
         call  comprespfactorborn(len0,len,flst_rhborn(:,ptr),flst_rhbornres(:,ptr),factortmp)
         if(ihist.eq.1) factor = factortmp
         factortot = factortot + factortmp
      enddo
      weight = factor / factortot
      end

      subroutine comprespfactorborn(len0,lenb,a,ares,factor)
      implicit none
      integer len0,lenb,a(lenb),ares(lenb)
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_physpar.h'
      real * 8 factor
      integer firstfs,firstfs0,moth,k
      real * 8 mass,width,virt,pcm(0:3,1:lenb)
      real * 8 momsq03
      external momsq03
      factor = 1
      firstfs = lenb - flst_numfsb + 1
      firstfs0 = len0 - flst_numfsb + 1
      pcm(:,1:2) = kn_cmpborn(:,1:2)
      pcm(:,firstfs:lenb) = kn_cmpborn(:,firstfs0:len0)
      pcm(:,3:firstfs-1) = 0
c Sum momenta of each final state particle to all its ancestors.
      do k=firstfs,lenb
         moth = ares(k)
         do while(moth.ne.0)
            pcm(:,moth) = pcm(:,moth) + pcm(:,k)
            moth = ares(moth)
         enddo
      enddo
c Now all resonances have the correct 4-momentum
      do k = 3,firstfs-1
         mass = physpar_pdgmasses(a(k))
         width = physpar_pdgwidths(a(k))
         virt = momsq03(pcm(:,k))
         factor = factor*mass**4/((virt-mass**2)**2 + (mass*width)**2)
      enddo
      end
