      subroutine genphasespace(xxx,lflav,flav,res,beams,xjac,
     1     x1,x2,spcm,cmmoms,moms)
      implicit none
      include 'pwhg_physpar.h'
      include 'pwhg_math.h'
      real * 8 xxx(*)
      integer lflav,flav(lflav),res(lflav)
      real * 8 beams(0:3,2),xjac,x1,x2,spcm,
     1     cmmoms(0:3,lflav),moms(0:3,lflav)
c end argument list
      integer levels(lflav),maxlevel,ilevel,lplist,plist(lflav)
      real * 8 sbeams,ebeams,emin,masses(lflav),taumin,lntaumin,tau,r,
     1         r1,r2,epcm,ycm,p0(0:3),vec(3),beta,power
      integer jp,jr,currand
      logical isfinalstate
      external isfinalstate
c this is the previously used random number index
      currand = 0
      xjac = 1
      plist = 0
      
c reminder: particles produced at hard interaction are level 1;
c           those arising from the decay of a resonance at level n-1 are at level n.
      call find_levels(lflav,res,levels,maxlevel)

c we assume throughout that incoming momenta are along the third axis
      sbeams = (beams(0,1)+beams(0,2))**2 - (beams(3,1)+beams(3,2))**2
      ebeams = sqrt(sbeams)
      
c set up the masses array to be the phase space mass for fs particles,
c and the resonance virtuality (i.e. the invariant mass of the system of its
c decay products).
      masses=0d0
      do jp = 3,lflav
         if(isfinalstate(jp,lflav,res)) then
            masses(jp) = physpar_phspmasses(flav(jp))
         endif
      enddo

      call getresvirts(currand,xxx,lflav,flav,res,levels,maxlevel,
     1     ebeams,masses,xjac)

c Start building the phase space.
c Level 1 is special, as it includes the generation of the parton momentum
c fractions.
c Generate tau = x1*x2. Find the mimimum tau
      emin = 0
      lplist = 0
      do jp = 3,lflav
         if(levels(jp).eq.1) then
            emin = emin + masses(jp)
            lplist = lplist + 1
            plist(lplist) = jp
         endif
      enddo

      if(lplist > 1) then
         taumin = emin**2/sbeams
c TODO better:
         if(taumin.eq.0) taumin = 1/sbeams
         r = nextrandom()
         lntaumin = log(taumin)
c         power = 3.5d0
         power = 1d0
         tau = exp(lntaumin*(1-r**power))
         xjac = xjac * tau * abs(lntaumin)*power*r**(power-1)
c     partonic cm final state energy
         spcm = tau * sbeams
         epcm = sqrt(spcm)

c set up a level 0 momentum
         p0(0) = epcm
         p0(1:3) = 0
         
         call nbodyphasespace(currand,lplist,plist,xxx,p0,masses,cmmoms,xjac)
      else
c there is only one resonance in direct production.
c genresvirt generates according to d s / (2 pi) ; here we need d tau = ds / sbeams
c we must correct the jacobian
         xjac = xjac * 2*pi / sbeams
         tau = emin**2/sbeams
         cmmoms(1:3,plist(lplist)) = 0
         cmmoms(0,plist(lplist)) = emin
c partonic cm final state energy
         spcm = tau * sbeams
         epcm = sqrt(spcm)
      endif
c ycm
      r = nextrandom()
      call genrapidity(r,tau,ycm,xjac)

c do remaining levels
      do ilevel = 1,maxlevel
c go through the resonances of the current level, and generate the phase space
c for their direct decay products
         do jr = 3,lflav
            lplist = 0
            if(levels(jr).eq.ilevel.and.
     1           .not.isfinalstate(jr,lflav,res)) then
               do jp = 3,lflav
                  if(res(jp).eq.jr) then
                     lplist = lplist + 1
                     plist(lplist) = jp
                  endif
               enddo

               call nbodyphasespace(currand,lplist,plist,xxx,cmmoms(:,jr),masses,cmmoms,xjac)

            endif
         enddo
      enddo

      cmmoms(0,1)  = epcm/2
      cmmoms(3,1)  = cmmoms(0,1)
      cmmoms(1:2,1)= 0
      cmmoms(0,2)  = cmmoms(0,1)
      cmmoms(3,2)  = -cmmoms(0,1)
      cmmoms(1:2,2)= 0

c Now the array cmpborn is completely filled; set the other
c variables
      x1 = sqrt(tau)*exp(ycm)
      x2 = tau/x1
c Find boost of hadronic CM with respect to Lab CM
      ycm = ycm + 0.5d0*log((beams(0,1)+beams(3,1))/
     1                      (beams(0,2)-beams(3,2)))


      beta=tanh(ycm)
      vec(1)=0
      vec(2)=0
      vec(3)=1      
      call mboost(lflav,vec,beta,cmmoms,moms)




      contains

         real * 8 function nextrandom()
         currand = currand + 1
         nextrandom = xxx(currand)
         end function

      end


c Subroutine to randomly generate the virtuality of resonances in a compound phase space
      subroutine getresvirts(currand,xxx,lflav,flav,res,levels,maxlevel,
     1     ebeams,masses,xjac)
c we assume that the masses array has the mass of its final state particles
c already set
      implicit none
      include "nlegborn.h"
      include "pwhg_math.h"
      include 'pwhg_physpar.h'
      integer currand
      real * 8 xxx(*)
      integer lflav
      integer flav(lflav),res(lflav),levels(lflav),maxlevel
      real * 8 ebeams,masses(lflav)
      real * 8 xjac
      logical nores
      integer ilevel
      real * 8 minmass,massdec,etot,sss
      integer jp,jr
      logical isfinalstate
      external isfinalstate
      minmass = 0
      do jp=3,lflav
         if(isfinalstate(jp,lflav,res)) then
            minmass = minmass + masses(jp)
         endif
      enddo
      etot = ebeams - minmass
      if(etot.le.0) then
         xjac = 0
c set all resonance masses to zero and return
         return
      endif
      
      do ilevel = maxlevel-1,1,-1
         do jr = 3,lflav
            if(levels(jr).eq.ilevel) then
               massdec = 0
               nores = .true.
               do jp = 3,lflav
                  if(jr.eq.res(jp)) then
                     massdec = massdec + masses(jp)
                     nores = .false.
                  endif
               enddo
               if(nores) cycle
               etot = etot + massdec
               currand = currand + 1
               call breitplusconst(xxx(currand),massdec**2,etot**2,
     1              physpar_phspmasses(flav(jr)),
     2              physpar_phspwidths(flav(jr)), 
     3              sss,xjac)
               masses(jr) = sqrt(sss)
               xjac = xjac /(2*pi)
               etot = etot - masses(jr)
            endif
         enddo
      enddo

      end


      subroutine nbodyphasespace(currand,lplist,plist,xxx,p0,masses,cmmoms,xjac)
      implicit none
      integer currand,lplist
      integer plist(lplist)
      real * 8 xxx(*),p0(0:3),masses(*),cmmoms(0:3,*),xjac
c local variables
      real * 8 xm(lplist),pin4(1:4),p(4,lplist),wt,et,r1,r2
      integer n,j
      real * 8 momsq03
      external momsq03

      if(lplist.lt.2) then
         write(*,*) ' nbodyphasespace: got ',lplist,' particle phase space'
         write(*,*) ' cannot handle, exiting ...'
         call exit(-1)
      endif

      if(lplist.eq.2) then
         r1 = nextrandom()
         r2 = nextrandom()
         if(sum(abs(p0(1:3))).eq.0) then
            call twobodyphsp0(1,r1,r2,masses(plist(1)),masses(plist(2)),p0(0),
     1           xjac,cmmoms(:,plist(1)),cmmoms(:,plist(2)))
         else
            call twobodyphsp(r1,r2,masses(plist(1)),masses(plist(2)),
     1              p0,xjac,
     1              cmmoms(:,plist(1)),cmmoms(:,plist(2)))
         endif
         return
      endif

      do j=1,lplist
         xm(j) = masses(plist(j))
      enddo

      et = sqrt(momsq03(p0))
      call bambo(lplist,et,xm,xxx(currand+1),p,wt)

      if(sum(abs(p0(1:3))).ne.0) then
c boost momenta to resonance frame
         pin4(4) = p0(0)
         pin4(1:3) = p0(1:3)
         call boost2resoninv4(pin4,lplist,p,p)
      endif

      do j=1,lplist
         cmmoms(0,plist(j))   = p(4,j)
         cmmoms(1:3,plist(j)) = p(1:3,j)
      enddo
      xjac = xjac * wt
      currand = currand+(3*lplist-4)

      contains

         real * 8 function nextrandom()
         currand = currand + 1
         nextrandom = xxx(currand)
         end function

      end

c 
c Maps 3n-4 dimensional unit cube into n-particle phase space,
c and computes jacobian.
c Phase space is normalized in standard way (as (2.8) in fno2006)
c
c n: number of particles
c et: CM energy
c xm(n): masses
c xpar(3n-4): the 3n-4 parameters between zero and 1 that parametrize the phase space
c p(4,n): output 5 vectors: px py pz energy
c wt: output weight, wt d xpar_1 ... d xpar_{3n-4} is the phase space element
      subroutine bambo(n,et,xm,xpar,p,wt)
      implicit none
      integer n
      real * 8 et,xm(n),p(4,n),xpar(3*n-4),wt
      integer m,ipar,j,nn
      real * 8 esys,beta,vec(3),recm(4),mrec2,mrec,mrmax,mrmin,mr,
     #   mrecmin,x,xmin,xmax,phi,cth,sth,km,em,xjac,tmp
      real * 8 pi
      parameter (pi=3.141592653589793d0)

      if(n.lt.2) then
         write(*,*) ' error: cannot do 1 body phase space'
         stop
      endif

      xjac=1
c initial energy of subsystem
      esys=et
c initial boost parameters of subsystem
      beta=0
      vec(1)=1
      vec(2)=0
      vec(3)=0

c phasespace parametrized by xpar(ipar)
      ipar=1
c minimum mass of subsystem
      mrecmin=0
      do j=1,n
         mrecmin=mrecmin+xm(j)
      enddo

      do m=1,n-1
c mass of recoil system
         mrecmin=mrecmin - xm(m)
c     Recoil sistem must have mass >= sum j=2,m-1 m_j
         if(et.lt.xm(m)+mrecmin) then
            wt=0
            return
         endif
c     generate uniform 2-body phase space as if recoil system was a single
c     particle of mass from mrec to maximum, scaling as if massless
c     n-m phase space: mrec^(2*nn-2)/(2*nn-2) - mrec^(2*nn) Esys^(-2) /(2*nn)
         if(m.lt.n-1) then
            nn=(n-m)
c mr is mrec^2/esys^2
            mrmax = ((esys-xm(m))/esys)**2

c 2 body massless phase space is proportional to
c (E^2-mrec^2)*mrec^(2nn-4) d mrec^2
c      \propto Esys^2 mrec^(2*nn-2)/(2*nn-2) - mrec^(2*nn) /(2*nn)

            xmax = mrmax**(nn-1)/(nn-1)-mrmax**nn/nn
            mrmin = (mrecmin/esys)**2
            xmin = mrmin**(nn-1)/(nn-1)-mrmin**nn/nn
            x = xmax*xpar(ipar)+(1-xpar(ipar))*xmin
            xjac=xjac*(xmax-xmin)
c solves m^(n-1)/(n-1)-m^(n) / n =x
            call solvespec(nn,x,mr)
c jacobian from dx to d mr:
            xjac = xjac/(mr**(nn-2) - mr**(nn-1))
            mrec2=mr*esys**2
            xjac=xjac*esys**2
c divide by 2 pi, when introducing 2 pi delta(prec^2-mrec^2) d mrec^2/(2 pi)
            xjac=xjac/(2 * pi)
            mrec=sqrt(mrec2)
            ipar=ipar+1
         else
            mrec=mrecmin
         endif
         phi=xpar(ipar)*2*pi
         xjac=xjac*2*pi
         ipar=ipar+1
         cth=1-xpar(ipar)*2
         ipar=ipar+1
         xjac=xjac*2
         sth=sqrt(1-cth**2)
c energy of mth particle
         em=(esys**2-mrec**2+xm(m)**2)/(2*esys)
c its momentum
         km=sqrt(em**2-xm(m)**2)
c     include two body phase space factor
c     
         xjac=xjac*km/esys /(16*pi**2)
c     
         p(3,m)=km*cth
         p(1,m)=km*sth*cos(phi)
         p(2,m)=km*sth*sin(phi)
         p(4,m)=em
c     recoil momentum
         recm(1)=-p(1,m)
         recm(2)=-p(2,m)
         recm(3)=-p(3,m)
         recm(4)=esys-p(4,m)
         if(beta.ne.0) then
c     Boost p_m and recm according to beta of current system
            call mboost4(1,vec,beta,p(:,m),p(:,m))
            call mboost4(1,vec,beta,recm,recm)
         endif
         if(m.eq.n-1) then
c nothing else to be done! last momentum is recoil momentum
            p(1,n)=recm(1)
            p(2,n)=recm(2)
            p(3,n)=recm(3)
            p(4,n)=recm(4)
         else
c     Compute velocity of recoil system; at next iteration
c     we compute the phase space of recoil system, so esys=mrec.
            tmp=sqrt(recm(1)**2+recm(2)**2+recm(3)**2)
            vec(1)=recm(1)/tmp
            vec(2)=recm(2)/tmp
            vec(3)=recm(3)/tmp
            beta=tmp/recm(4)
            esys=mrec
         endif
      enddo
      if(ipar.ne.3*n-3) then
         write(*,*) '?'
      endif
      wt=xjac
      end


      subroutine solvespec(n,x,m)
      implicit none
      real * 8 x,m,m0,dm0,vm0
      integer n
      integer icount,maxcount
      parameter (maxcount=1000)
c solves the equation
c     m^(n-1)/(n-1)-m^(n) / n =x
c for integer n
      icount = 0
      if(x.lt.0.or.x.gt.1d0/(n-1)-1d0/n) then
         m=-1
         return
      endif
      if(n.eq.2) then
         m=1-sqrt(1-2*x)
      else
         m0=0.5d0
 1       continue
         dm0=m0**(n-2)-m0**(n-1)
         vm0=m0**(n-1)/(n-1)-m0**n/n
c solve vm0+(m-m0)*dm0=x
         m=(x-vm0)/dm0+m0
         if(m.gt.1) then
            m=1
         elseif(m.lt.0) then
            m=0
         endif
         if(abs(m-m0)/(abs(m)+abs(m0)).lt.1d-13) then
            return
         else
            icount = icount + 1
            if(icount.gt.maxcount) then
               write(*,*) ' solvespec: more than 1000 iterations,'
               write(*,*) ' precision reached:',
     1              abs(m-m0)/(abs(m)+abs(m0))
               return
            endif
            m0=m
            goto 1
         endif
      endif
      end



c     Inverse mapping from p(0:3,n) -> pb(0:3,n-1), following      
c     Sec 5.1.1 of arXiv:0709.2092      
c     The n-th momentum is interpreted as the radiated particle in ISR
      subroutine inverseISRmapping(p,n,pb)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_kn.h'
c      real * 8 p(0:3,nlegrealexternal)
      integer n
      real * 8 p(0:3,n)
      real * 8 pb(0:3,n-1)
      real * 8 ktot(0:3),ktotl(0:3),prad(0:3)
      real * 8 betalvec(3), betal
      real * 8 betatvec(3), betat,mod
      real * 8 pCM(0:3,n)
      integer i,mu
      real * 8 dotp
      external dotp
      real * 8 ecm, xplus, xminus, y, csi, xplusbar, xminusbar,v,ebeam
      real * 8 zero
      
      ktot = p(:,1) + p(:,2) - p(:,n)
c     longitudinal boost
      betalvec(1) = 0d0
      betalvec(2) = 0d0
      betalvec(3) = 1d0
      betal = - ktot(3)/ktot(0)
      v = ktot(3)/ktot(0)
      call mboost(1,betalvec,betal,ktot,ktot)

c     transverse boost
      mod = sqrt(ktot(1)**2+ktot(2)**2)
      betatvec(1) = ktot(1)/mod
      betatvec(2) = ktot(2)/mod
      betatvec(3) = 0d0
      betat = -mod/ktot(0)
      call mboost(1,betatvec,betat,ktot,ktot)

c     apply  BL^(-1) BT BL
      call mboost(n-3,betalvec,betal,p(:,3),pb(:,3))
      call mboost(n-3,betatvec,betat,pb(:,3),pb(:,3))
      call mboost(n-3,betalvec,-betal,pb(:,3),pb(:,3))
      ktot=0d0
      do i=3,n-1
         ktot=ktot+pb(:,i)
      enddo

      ebeam=sqrt(kn_sbeams)
      goto 100
      
      xplus  = p(0,1)/(ebeam/2)
      xminus = p(0,2)/(ebeam/2)
c     longitudinal boost in the partonic CM frame
      betal = (xplus-xminus)/(xplus+xminus)

      
c     boost radiated parton in the partonic CM frame
      call mboost(1,betalvec,-betal,p(:,n),prad(:))

      ecm = ebeam*sqrt(xplus*xminus)
      csi = 2*prad(0)/ecm
      y = prad(3)/prad(0)
            
c     compute xplusbar and xminusbar
      
      xplusbar = xplus*sqrt(1-csi)*sqrt((2-csi*(1+y))/(2-csi*(1-y)))
      xminusbar = xminus*sqrt(1-csi)*sqrt((2-csi*(1-y))/(2-csi*(1+y)))

      pb(0,1) = ebeam/2*xplusbar
      pb(1,1) = 0
      pb(2,1) = 0
      pb(3,1) = ebeam/2*xplusbar

      pb(0,2) = ebeam/2*xminusbar
      pb(1,2) = 0
      pb(2,2) = 0
      pb(3,2) = -ebeam/2*xminusbar
      

 100  continue
c     use the fact that
c     xplusbar * Kplus + xminusbar * Kminus = ktot (after boosts)!
      xplusbar = (ktot(0)+ktot(3))/ebeam
      xminusbar = (ktot(0)-ktot(3))/ebeam

      pb(0,1) = ebeam/2*xplusbar
      pb(1,1) = 0
      pb(2,1) = 0
      pb(3,1) = ebeam/2*xplusbar

      pb(0,2) = ebeam/2*xminusbar
      pb(1,2) = 0
      pb(2,2) = 0
      pb(3,2) = -ebeam/2*xminusbar

      
c     boost in the CM partonic frame
      betal = (xplusbar-xminusbar)/(xplusbar+xminusbar)
      call mboost(n-1,betalvec,-betal,pb(:,1),pb(:,1))

c      do i=1, n-1
c         write(*,*) (pb(mu,i),mu=0,3)
c      enddo
      
      return
      
c     check momentum conservation
      ktot=ktot-pb(:,1)-pb(:,2)
      zero = 0d0
      do mu=0, 3
         zero = zero + ktot(mu)**2
      enddo
      if (zero.gt.1d-12) then
         write(*,*) 'VIOLATION MOM CONSER ', zero
      endif
      
      end
      
