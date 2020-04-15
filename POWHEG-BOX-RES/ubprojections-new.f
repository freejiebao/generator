c Find the underlying Born momenta from the real momenta and the
c emitter-radiated pair
      subroutine compubornx(em,rad,reslist,cmppborn)
      implicit none
      include 'nlegborn.h'
      integer em,rad,reslist(nlegreal)
      real * 8 cmppborn(0:3,nlegreal)
      if(em.lt.3) then
         call findubisrx(rad,cmppborn)
      else
         call findubfsrx(em,rad,reslist,cmppborn)
      endif
      end
      
      subroutine findubfsrx(em,rad,reslist,cmppborn)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer em,rad,reslist(nlegreal)
      real * 8 cmppborn(0:3,nlegreal)
      real * 8 krecv(3),q0,q2,krec,beta,      
     1     k0rec,k,vec(3)
      integer res,j
      real * 8 pcm(0:3,1:nlegreal)
      integer pcmlen
      common/local_pcm/pcm,pcmlen
      res=reslist(em)
      if(res.ne.reslist(rad)) then
         write(*,*) ' findubfsr: error'
         call pwhg_exit(-1)
      endif
      cmppborn=pcm
      if(res.ne.0) then
         call boost2reson(pcm(:,res),pcmlen,
     1        pcm,cmppborn)
         q0=cmppborn(0,res)
      else
         q0=2*cmppborn(0,1)
      endif
      q2=q0**2
c recoil system momentum 
      k0rec=q0-cmppborn(0,em)-cmppborn(0,rad)
      krecv=-cmppborn(1:3,em)-cmppborn(1:3,rad)
      krec=sqrt(krecv(1)**2+krecv(2)**2+krecv(3)**2)
      beta=(q2-(k0rec+krec)**2)/(q2+(k0rec+krec)**2)
      vec=krecv/krec
      if(res.eq.0) then
         call mboost(pcmlen-2,vec,beta,
     1        cmppborn(:,3:pcmlen),cmppborn(:,3:pcmlen))
      else
         do j=3,pcmlen
            if(reslist(j).eq.res) then
               call mboost(1,vec,beta,
     1              cmppborn(:,j:j),cmppborn(:,j:j))
            endif
         enddo
      endif
      k=(q2-(k0rec**2-krec**2))/(2*q0)
      cmppborn(0,em)=k
      cmppborn(1:3,em)=-vec*k
      cmppborn(:,rad)=0
      end

      subroutine findubisrx(j,cmppborn)
      implicit none
      integer j
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      real * 8 cmppborn(0:3,nlegreal)
      real * 8 krecv(3),q0,q2,krec,k0rec,
     1     krecperp,mrec2,beta,vec(3)
      real * 8 pcm(0:3,1:nlegreal)
      integer pcmlen
      common/local_pcm/pcm,pcmlen
      cmppborn(0:3,1)=pcm(0:3,1)
      cmppborn(0:3,2)=pcm(0:3,2)
      q0=2*cmppborn(0,1)
      q2=q0**2
c recoil system momentum 
      k0rec=q0-pcm(0,j)
      krecv=-pcm(1:3,j)
      krec=sqrt(krecv(1)**2+krecv(2)**2+krecv(3)**2)
      mrec2=(k0rec**2-krec**2)
      beta=-krecv(3)/k0rec
      vec(1)=0
      vec(2)=0
      vec(3)=1
      call mboost(pcmlen-2,vec,beta,
     1     pcm(:,3:pcmlen),cmppborn(:,3:pcmlen))
c Now the transverse boost
      krecperp=sqrt(krecv(1)**2+krecv(2)**2)
      vec(3)=0
      vec(1:2)=krecv(1:2)/krecperp
      beta=-krecperp/sqrt(mrec2+krecperp**2)
      call mboost(pcmlen-2,vec,beta,
     1     cmppborn(:,3:pcmlen),cmppborn(:,3:pcmlen))
      cmppborn(:,j)=0
      end

      function dijtermx(em,rad,rflav0,reslist)
      implicit none
      real * 8 dijtermx
      include 'nlegborn.h'
      integer em,rad,rflav0(nlegreal),reslist(nlegreal)
      integer rflav(nlegreal)
      include 'pwhg_flst.h'
      include 'pwhg_par.h'
      integer res
      real * 8 cmppborn(0:3,nlegreal)
      real * 8 avub,getdistancex,dalr,tmp
      integer nub,mergeisrx,mergefsrx,i,j,k,ifl1,ifl2,onem
      parameter (onem=1000000)
      logical ini,olddij
      data ini/.true./
      save ini,olddij
      real * 8 powheginput
      external powheginput
      real * 8 pcm(0:3,1:nlegreal)
      integer pcmlen
      common/local_pcm/pcm,pcmlen
c isoftflagc = 0: soft limit; 1: full
      integer isoftflagc
      common/local_isoftflagc/isoftflagc
      if(em.lt.0) then
c only the first and last arguments are used, if the first is -1
         dijtermx = getdistancex(-1,rad,rflav,res,pcm)
         return
      endif
c      if(ini) then
c         if(powheginput("#olddij").eq.1) then
c            olddij=.true.
c         else
c            olddij=.false.
c         endif
c         ini=.false.
c      endif
c      if(olddij) then
c         dijterm=kn_dijterm(em,rad)
c         return
c      endif
c we only consider singularities within the same
c resonance decay (or in production)
      rflav = rflav0
      if(em.eq.0) then
         res = 0
      else
         res=reslist(em)
      endif
c find UB flavour
      if(em.eq.0) then
         continue
      elseif(em.eq.1) then
         rflav(1)=mergeisrx(rflav(1),rflav(rad))
      elseif(em.eq.2) then
         rflav(2)=mergeisrx(rflav(2),rflav(rad))
      else
         rflav(em)=mergefsrx(rflav(em),rflav(rad))
      endif
      dalr=getdistancex(em,rad,rflav0,res,pcm)
c invalidater rad parton with impossible pdg code
      rflav(rad)=onem
      if(isoftflagc.eq.1) then
         call compubornx(em,rad,reslist,cmppborn)
      else
         cmppborn(:,1:pcmlen-1) = pcm(:,1:pcmlen-1)
      endif
c looop over all possible singularities
c      if(abs(dalr/kn_dijterm(em,rad)-1).gt.1d-6) then
c         write(*,*) 'dalr', dalr/kn_dijterm(em,rad)
c         write(*,*) 'This may imply that running the program ',
c     1              'with olddij is wrong; it may also imply ',
c     2              'that kn_dijterm_soft() are incorrect.',
c     3              'A dijterm_soft() function should be built instead'
c         call pwhg_exit(-1)
c      endif
c get average singularity from underlying Born
      if(isoftflagc.eq.1) then
         avub=1
         nub=0
         do j=pcmlen-flst_numfsr+1,pcmlen
            if(reslist(j).ne.res) cycle
            if(res.eq.0) then
               ifl1=mergeisrx(rflav(1),rflav(j))
               ifl2=mergeisrx(rflav(2),rflav(j))
               if(ifl1.eq.rflav(1).and.ifl2.eq.rflav(2)) then
                  tmp = getdistancex(0,j,rflav,res,cmppborn)
                  if(tmp.eq.0) goto 999
                  avub=avub*(1+dalr/tmp)
                  nub=nub+1
               else
                  if(ifl1.ne.onem) then
                     tmp = getdistancex(1,j,rflav,res,cmppborn)
                     if(tmp.eq.0) goto 999
                     avub=avub*(1+dalr/tmp)
                     nub=nub+1
                  endif
                  if(ifl2.ne.onem) then
                     tmp = getdistancex(2,j,rflav,res,cmppborn)
                     if(tmp.eq.0) goto 999
                     avub=avub*(1+dalr/tmp)
                     nub=nub+1
                  endif
               endif
            endif
            do k=j+1,pcmlen
               if(reslist(k).ne.res) cycle
               if(mergefsrx(rflav(j),rflav(k)).ne.onem) then
                  tmp = getdistancex(j,k,rflav,res,cmppborn)
                  if(tmp.eq.0) goto 999
                  avub=avub*(1+dalr/tmp)
                  nub=nub+1
               endif
            enddo
         enddo
      else
         avub = 1
      endif
      dijtermx=dalr*avub
      return
 999  continue
      dijtermx = 1d200
      if(dalr.eq.0) then
         call increasecnt("dalr and ub distance = 0 in ubprojections")
      else
         call increasecnt("ub distance = 0 in ubprojections")
      endif
      end

      function getdistancex(em,rad,a,res,cmp)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      include 'pwhg_par.h'
      include 'pwhg_physpar.h'
      real * 8 getdistancex
      integer em,rad,res,a(*)
      real * 8 cmp(0:3,nlegreal),y,e_em,e_rad,mass_em,mass_rad
      real * 8 dotp
      external dotp
c isoftflagc = 0: soft limit; 1: full
      integer isoftflagc
      common/local_isoftflagc/isoftflagc
      real * 8 powheginput,enhancereg
      procedure() :: powheginput
      logical ini
      data ini/.true./
      save ini,enhancereg
      if(ini) then
         enhancereg = powheginput("#enhancereg")
         if(enhancereg.lt.0) enhancereg = 1
         ini = .false.
      endif
      if(em.lt.0) then
         getdistancex=((enhancereg*cmp(0,1))**2)**par_diexp
      elseif(em.lt.3) then
         y=1-dotp(cmp(:,1),cmp(:,rad))/(cmp(0,1)*cmp(0,rad))
         if(em.eq.0) then
            getdistancex=(cmp(0,rad)**2*(1-y**2))**par_diexp
         elseif(em.eq.1) then
            getdistancex=(cmp(0,rad)**2*2*(1-y))**par_diexp
         elseif(em.eq.2) then
            getdistancex=(cmp(0,rad)**2*2*(1+y))**par_diexp
         endif
      else
         if(res.eq.0) then
            e_em=cmp(0,em)
            e_rad=cmp(0,rad)
         else
            e_em=dotp(cmp(:,res),cmp(:,em))
            e_rad=dotp(cmp(:,res),cmp(:,rad))
         endif
c This perhaps is not good enough, especially if we need lepton masses in EW radiation
c         if(abs(a(em)).eq.11.or.abs(a(rad)).eq.11) then
c            write(*,*)
c     1   '  getdistance: should be upgraded to treat '//
c     2           'electrons      ! exiting ...'
c            call exit(-1)
c         endif
         mass_em = physpar_pdgmasses(a(em))
         mass_rad = physpar_pdgmasses(a(rad))
         if(mass_em.gt.0.and.mass_rad.eq.0) then
            getdistancex=(2*dotp(cmp(:,em),cmp(:,rad))*
     1        e_rad/e_em
     2        )**par_dijexp
         elseif(mass_rad.gt.0.and.mass_em.eq.0) then
            write(*,*) ' getdistancex: should never get '//
     1           'here ... exiting ...'
            call exit(-1)
         else
            if(isoftflagc.eq.0) then
               getdistancex=(2*dotp(cmp(:,em),cmp(:,rad))*
     1              e_em*e_rad/e_em**2
     2              )**par_dijexp
            else
               getdistancex=(2*dotp(cmp(:,em),cmp(:,rad))*
     1              e_em*e_rad/(e_em+e_rad)**2
     2              )**par_dijexp
            endif
         endif
      endif
      end

      function mergeisrx(i,j)
      implicit none
      integer mergeisrx,i,j,onem,itag,ibornfl,iret,mmm
      parameter (onem = 1000000)
      call same_splitting0('isr',i,j,1,1,itag,ibornfl,iret)
      if(iret == -1) then
         mergeisrx = onem
      else
         mergeisrx = ibornfl
      endif
      end

      function mergefsrx(i,j)
      implicit none
      integer mergefsrx,i,j,onem,itag,ibornfl,iret,mmm
      parameter (onem = 1000000)
      call same_splitting0('fsr',i,j,1,1,itag,ibornfl,iret)
      if(iret == -1) then
         mergefsrx = onem
      else
         mergefsrx = ibornfl
      endif
      end
