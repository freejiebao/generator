c  The next subroutines, open some histograms and prepare them 
c      to receive data 
c  You can substitute these  with your favourite ones
c  init   :  opens the histograms
c  topout :  closes them
c  pwhgfill  :  fills the histograms with data

      subroutine init_hist
      implicit none
      include  'LesHouches.h'
      include 'pwhg_math.h'
      character * 1 cnum(9)
      data cnum/'1','2','3','4','5','6','7','8','9'/

      call inihists

      call bookupeqbins('total',1d0,-0.5d0,0.5d0)
      call bookupeqbins('totalcut',1d0,-0.5d0,0.5d0)
      call bookupeqbins('totalphotoncut',1d0,-0.5d0,0.5d0)

      call bookupeqbins('e_pt',20d0,0d0,6000d0)
      call bookupeqbins('e_y',0.25d0,-2.5d0,2.5d0)

      call bookupeqbins('mu_pt',20d0,0d0,6000d0)
      call bookupeqbins('mu_y',0.25d0,-2.5d0,2.5d0)

      call bookupeqbins('j1_pt',20d0,10d0,6010d0)
      call bookupeqbins('j1_y',0.25d0,-4.5d0,4.5d0)

      call bookupeqbins('j2_pt',20d0,10d0,6010d0)
      call bookupeqbins('j2_y',0.25d0,-4.5d0,4.5d0)

      call bookupeqbins('miss_pt',20d0,0d0,6000d0)

      call bookupeqbins('jj_m',50d0,0d0,13000d0)
      
      call bookupeqbins('jj_dy',0.25d0,-9d0,9d0)

      end
     
      subroutine analysis(dsig)
      implicit none
      real * 8 dsig
      include 'hepevt.h'
      include 'pwhg_math.h' 
      include  'LesHouches.h'
      integer   maxphot,nphot,maxnumg,maxnumlep
      parameter (maxphot=2048,maxnumlep=100)
      real * 8 pg(4,maxphot)
      character * 1 cnum(9)
      data cnum/'1','2','3','4','5','6','7','8','9'/
      save cnum
      integer j,k
c     we need to tell to this analysis file which program is running it
      character * 6 WHCPRG
      common/cWHCPRG/WHCPRG
      data WHCPRG/'NLO   '/
!      data WHCPRG/'PYTHIA'/
      real * 8 pw(4),pl(4),pnu(4),pjj(4)
      real * 8 pjet_temp(4)
      real * 8 pe(4), pmu(4), pnue(4), pnumu(4), pj1(4), pj2(4), pgamma(4,100)
      logical gamma(100)
      real * 8 pl03(0:3),pnu03(0:3)
      real * 8 y,eta,pt,m
      real * 8 y1,eta1,ptl1,m1
      real * 8 y2,eta2,ptl2,m2
      real * 8 dy,deta,delphi,dr
      real * 8 getpt,getdphi,getmass,geteta
      external getpt,getdphi,getmass,geteta
      integer ihep
      real * 8 powheginput,dotp
      external powheginput,dotp
      integer vdecaytemp,vdecay2temp
      real * 8 mtv
      real * 8 SUMALL(4)
      real * 8 yl,ptl,etal,ynu,ptnu,etanu,ml,mnu
      real*8 mw,mz
      real*8 cs
      real*8 getdeta,getdr,dphi,dr1,dr2
      real*8 cstar,phistar,phistar_report
c spin correlation observables
      real * 8 aspincor(0:7),lcos,genphi
      external cstar,phistar_report
      logical pwhg_isfinite
      external pwhg_isfinite
      integer nlep,nnu,ngamma,njet,i,oldngamma
      integer mu,nu,jnu,inu,igam,jgam,gam,il,jl,lep
      integer lepvec(maxnumlep),nuvec(maxnumlep),gammavec(maxphot)
      real*8 p_gamma(0:3)
      real*8 pt_nu,pt_nu_max
      real*8 pt_lep,pt_lep_max
      real*8 pt_gamma,pt_gamma_max
      real*8 ptlcut, ylcut, deltaRlcut, ptjcut, yjcut, ptmisscut, ydiffjcut, mjjcut
      real*8 delta_R, Rgamma
      real*8 ptgamma, deltatechgamma
      logical photoncut
      real*8 ye,etae,pte,ymu,etamu,ptmu,yj1,etaj1,ptj1,yj2,etaj2,ptj2,mjj,delta_ll
      logical ini
      data ini/.true./
      save ini

!      integer dbg
!      data dbg/0/
!      save dbg
      
      integer i1
      
      real*8 dummy

      if(dsig.eq.0) return

      if(.not.pwhg_isfinite(dsig)) then 
         print*,'dsig in analysis not finite: ',dsig
         return
      endif
      
      if (ini) then
          vdecaytemp = lprup(1)-10000
          if(vdecaytemp.lt.0) then
              vdecay2temp = -vdecaytemp+1
          else
              vdecay2temp = -vdecaytemp-1
          endif
          ini=.false.
      endif

      pw     = 0d0
      pe     = 0d0
      pmu    = 0d0
      pnue   = 0d0
      pnumu  = 0d0
      pj1    = 0d0
      pj2    = 0d0
      pgamma = 0d0
      nphot = 0

      gamma=.false.


!      dbg=dbg+1

!      write(*,*)'--------------------------',dbg
      
      nlep=0
      nnu=0
      njet=0
      ngamma=0
!     do i=1,maxnumlep
!     lepvec(i) = 0
!     nuvec(i) = 0
!     enddo
!     maxnumg=maxphot
!     do i=1,1
!     gammavec(i) = 0
!     enddo

!     if NLO only 1 gamma, if LHE allow for more than one gamma::
c     define an array
c NB for pythia we MUST include fastjet for the jet def
         
      do ihep=1,nhep
         if(isthep(ihep).eq.1) then
C     Scan over final state particle and record the entries
            if(abs(idhep(ihep)).eq.12) then
C     neutrino electron
               nnu=nnu+1
               pnue = phep(1:4,ihep)
            elseif(abs(idhep(ihep)).eq.14) then
C     neutrino muon
               nnu=nnu+1
               pnumu = phep(1:4,ihep)
            elseif(abs(idhep(ihep)).eq.11) then
C     positron
               nlep=nlep+1
               pe = phep(1:4,ihep)
            elseif(abs(idhep(ihep)).eq.13) then
C     anti-muon
               nlep=nlep+1
               pmu = phep(1:4,ihep)
            elseif(abs(idhep(ihep)).eq.22) then
C     photons
               ngamma=ngamma+1
               pgamma(1:4,ngamma) = phep(1:4,ihep)
               gamma(ngamma) =.true.
            elseif(abs(idhep(ihep)).le.6) then
C     jets
               njet=njet+1
               if(njet == 1) then
                  pj1 = phep(1:4,ihep)
               elseif(njet == 2) then
                  pj2 = phep(1:4,ihep)
               else
                  write(*,*) "This is not possible!"
                  stop
               endif
            endif
         endif
      enddo
      
      if(nlep.ne.2.or.nnu.ne.2.or.njet.ne.2) then
c            write(*,*)" not enough leptons or gamma! drop event"
            call exit(1)
            return
      endif

      ! Recombine the photon if necessary. Note that this algorithm is working with only a particular set of cuts (Delta R in particular).

      call filld('total',0d0,dsig) ! Cross seciton before the cuts.

      ptgamma = 30d0
      deltatechgamma = 0.5d0
      photoncut = .false.


      do i1=1,ngamma ! if ngamma ==0 does not enter here
         if(getpt(pgamma(:,i1)) .gt. ptgamma) then
            
            call getdydetadphidr(pe,pgamma(:,i1),dy,deta,dphi,dr)
            if(dr.le.deltatechgamma) then
               goto 30
            endif
            
            call getdydetadphidr(pmu,pgamma(:,i1),dy,deta,dphi,dr)
            if(dr.le.deltatechgamma) then
               goto 30
            endif
            
            call getdydetadphidr(pj1,pgamma(:,i1),dy,deta,dphi,dr)
            if(dr.le.deltatechgamma) then
               goto 30
            endif
            
            call getdydetadphidr(pj2,pgamma(:,i1),dy,deta,dphi,dr)
            if(dr.le.deltatechgamma) then
               goto 30
            endif
            
            photoncut = .true.
         
         endif
      enddo
      
 30   continue
      
c      write(*,*) "Before recombination"
      
      Rgamma = 0.1d0            ! Recombinaiton parameter for the photons.
       
c      write(*,*) "gamma", ngamma

c      do i1=1,ngamma
c         write(*,*)pgamma(:,i1)
c      enddo
      
      oldngamma=ngamma

      do i1=oldngamma,1,-1
         if(gamma(i1)) then

c            write(*,*)'pg',pgamma(1:4,i1)
            
            call getdydetadphidr(pe,pgamma(1:4,i1),dy,deta,dphi,dr)
            if(dr.le.Rgamma) then

c               write(*,*)'pe',pe
               
               pe=pe+pgamma(1:4,i1)
               ngamma=ngamma-1
               gamma(i1)=.false.
               goto 29
            endif
            
            call getdydetadphidr(pmu,pgamma(1:4,i1),dy,deta,dphi,dr)
            if(dr.le.Rgamma) then

c               write(*,*)'pmu',pmu
               
               pmu=pmu+pgamma(1:4,i1)
               ngamma=ngamma-1
               gamma(i1)=.false.
               goto 29
            endif
            
            call getdydetadphidr(pj1,pgamma(1:4,i1),dy,deta,dphi,dr)
            if(dr.le.Rgamma) then

c               write(*,*)'pj1',pj1
               
               pj1=pj1+pgamma(1:4,i1)
               ngamma=ngamma-1
               gamma(i1)=.false.
               goto 29
            endif
            
            call getdydetadphidr(pj2,pgamma(1:4,i1),dy,deta,dphi,dr)
            if(dr.le.Rgamma) then

c               write(*,*)'pj2',pj2
               
               pj2=pj2+pgamma(1:4,i1)
               ngamma=ngamma-1
               gamma(i1)=.false.
               goto 29
            endif
         endif
 29      continue
      enddo
c      write(*,*) "after recombinaiton"
c      write(*,*)'ngamma',ngamma,'oldngamma',oldngamma
c      do i1=1,oldngamma
c         if(gamma(i1)) write(*,*)pgamma(:,i1)
c      enddo

      
! Ordering of the jets according to the tranverse momentum.
      if(getpt(pj2) .ge. getpt(pj1)) then
         pjet_temp=pj1
         pj1=pj2
         pj2=pjet_temp
      endif
      
!     write(*,*) "after ordering of the jets"
      
      ptlcut = 20d0
      ylcut = 2.5d0
      deltaRlcut = 0.3d0 
      ptjcut = 30d0
      yjcut = 4.5d0
      ptmisscut = 40d0
      ydiffjcut = 2.5d0
      mjjcut = 500d0

!      ptlcut = 10d0
!      ylcut = 2.5d0
!      deltaRlcut = 0.3d0 
!      ptjcut = 10d0
!      yjcut = 4.5d0
!      ptmisscut = 10d0
!      ydiffjcut = 0.5d0
!      mjjcut = 100d0

!      write(*,*) "beginning of the cuts"

!      pl = phep(1:4,lepvec(1))
!      write(*,*) "pl", pl
      call getyetaptmass(pe,ye,etae,pte,ml)
      
      if(pte .lt. ptlcut) return
      if(abs(ye) .gt. ylcut) return

!      write(*,*) "cut 1"

!      pnu = phep(1:4,lepvec(2))
      call getyetaptmass(pmu,ymu,etamu,ptmu,ml)
      
      
      if(ptmu .lt. ptlcut) return
      if(abs(ymu) .gt. ylcut) return

!      write(*,*) "cut 2"

      delphi = getdphi(pe,pmu)
      delta_ll = dsqrt(delphi**2 + (ye-ymu)**2)

      if(delta_ll .lt. deltaRlcut) return

!      write(*,*) "cut 3"

      pnu = pnue + pnumu
      ptnu=getpt(pnu)

!      ptnu = getpt(pnue) + getpt(pnumu) ! I think this is not correct
      
      if(ptnu .lt. ptmisscut) return
      
!      write(*,*) "cut 4"
      
!      pl = phep(1:4,gammavec(1))
      call getyetaptmass(pj1,yj1,etaj1,ptj1,ml)
      
      if(ptj1 .lt. ptjcut) return
      if(abs(yj1) .gt. yjcut) return

!      write(*,*) "cut 5"

!      pnu = phep(1:4,gammavec(2))
      call getyetaptmass(pj2,yj2,etaj2,ptj2,ml)
      
      if(ptj2 .lt. ptjcut) return
      if(abs(yj2) .gt. yjcut) return
      if(abs(yj1-yj2) .le. ydiffjcut) return

!      write(*,*) "cut 6"
      
      pjj = pj1 + pj2
      mjj=getmass(pjj)

      if(mjj .lt. mjjcut) return

!      write(*,*) "cut 7"

      delphi = getdphi(pe,pj1)
      if(dsqrt(delphi**2 + (ye-yj1)**2) .le. deltaRlcut) return

      delphi = getdphi(pe,pj2)
      if(dsqrt(delphi**2 + (ye-yj2)**2) .le. deltaRlcut) return

      delphi = getdphi(pmu,pj1)
      if(dsqrt(delphi**2 + (ymu-yj1)**2) .le. deltaRlcut) return

      delphi = getdphi(pmu,pj2)
      if(dsqrt(delphi**2 + (ymu-yj2)**2) .le. deltaRlcut) return

!      write(*,*) "Filling histograms ################################"
      
      call filld('totalcut',0d0,dsig)
      
      if(photoncut) call filld('totalphotoncut',0d0,dsig)

      call filld('e_pt',pte,dsig)
      call filld('e_y',ye,dsig)

      call filld('mu_pt',ptmu,dsig)
      call filld('mu_y',ymu,dsig)

      call filld('j1_pt',ptj1,dsig)
      call filld('j1_y',yj1,dsig)

      call filld('j2_pt',ptj2,dsig)
      call filld('j2_y',yj2,dsig)

      call filld('miss_pt',ptnu,dsig)

      call filld('jj_m',mjj,dsig)
      
      call filld('jj_dy',yj1-yj2,dsig)

!      write(*,*) "End of it ################################"
!      stop

      return
      end

!      subroutine yetaptmassplot(p,dsig,prefix)
!      implicit none
!      real * 8 p(4),dsig
!      character *(*) prefix
!      real * 8 y,eta,pt,m
!      call getyetaptmass(p,y,eta,pt,m)
!      call filld(prefix//'_y',y,dsig)
!      call filld(prefix//'_eta',eta,dsig)
!      call filld(prefix//'_pt',pt,dsig)
!      call filld(prefix//'_m',m,dsig)
!      end

!      subroutine deltaplot(p1,p2,dsig,prefix)
!      implicit none
!      real * 8 p1(4),p2(4),dsig
!      character *(*) prefix
!      real * 8 dy,deta,delphi,dr
!      call getdydetadphidr(p1,p2,dy,deta,delphi,dr)
!      call filld(prefix//'_dy',dy,dsig)
!      call filld(prefix//'_deta',deta,dsig)
!      call filld(prefix//'_delphi',delphi,dsig)
!      call filld(prefix//'_dr',dr,dsig)
!      end


      subroutine getyetaptmass(p,y,eta,pt,mass)
      implicit none
      real * 8 p(4),y,eta,pt,mass
      real * 8 gety,getpt,geteta,getmass
      external gety,getpt,geteta,getmass
      y  = gety(p)
      pt = getpt(p)
      eta = geteta(p)
      mass = getmass(p)
      end


      function gety(p)
      implicit none
      real * 8 gety,p(4)
      real * 8 tiny
!      parameter (tiny=1.d-5)
      parameter (tiny=1.d-10)

      if (abs(p(4)-p(3)).lt.tiny) then
         gety=sign(1.d0,p(3))*1.d8
      elseif (abs(p(4)+p(3)).lt.1d-5*abs( p(4)-p(3)) ) then ! mauro ? (e~-pz=> large negative rap ~log0)
         gety=sign(1.d0,p(3))*1.d8
      else
         gety=0.5d0*log((p(4)+p(3))/(p(4)-p(3)))
      endif
      end

      function getpt(p)
      implicit none
      real * 8 getpt,p(4)
      getpt = sqrt(p(1)**2+p(2)**2)
      end

      function getmass(p)
      implicit none
      real * 8 getmass,p(4)
      getmass=sqrt(abs(p(4)**2-p(3)**2-p(2)**2-p(1)**2))
      end

      function geteta(p)
      implicit none
      real * 8 geteta,p(4),pv
      real * 8 tiny
      parameter (tiny=1.d-5)
      pv = sqrt(p(1)**2+p(2)**2+p(3)**2)
      if(pv.lt.tiny)then
         geteta=sign(1.d0,p(3))*1.d8
      else
         geteta=0.5d0*log((pv+p(3))/(pv-p(3)))
      endif
      end



      subroutine getdydetadphidr(p1,p2,dy,deta,dphi,dr)
      implicit none
!      real * 8 p1(*),p2(*),dy,deta,dphi,dr
      real * 8 p1(4),p2(4),dy,deta,dphi,dr
      real * 8 getdy,getdeta,getdphi,getdr
      external getdy,getdeta,getdphi,getdr
      dy=getdy(p1,p2)
      deta=getdeta(p1,p2)
      dphi=getdphi(p1,p2)

c      write(*,*)'dy',dy,'deta',deta,'dphi',dphi
      
      dr=getdr(deta,dphi)

c      write(*,*)'dr',dr
      end

      function getdy(p1,p2)
      implicit none
!      real*8 p1(*),p2(*),getdy
      real*8 p1(4),p2(4),getdy
      real*8 y1,y2
      real*8 gety
      external gety
      y1 = gety(p1)
      y2 = gety(p2)
      getdy = y1-y2
      end

      function getdeta(p1,p2)
      implicit none
!      real*8 p1(*),p2(*),getdeta
      real*8 p1(4),p2(4),getdeta
      real*8 eta1,eta2
      real*8 geteta
      external geteta
      eta1 = geteta(p1)
      eta2 = geteta(p2)
      getdeta = eta1-eta2
      end

      function getdphi(p1,p2)
      implicit none
      include 'pwhg_math.h' 
!      real*8 p1(*),p2(*),getdphi
      real*8 p1(4),p2(4),getdphi
      real*8 phi1,phi2
      real*8 geteta
      external geteta
      phi1=atan2(p1(2),p1(1))
      phi2=atan2(p2(2),p2(1))
      getdphi=abs(phi1-phi2)
      getdphi=min(getdphi,2d0*pi-getdphi)
      end

      function getdr(deta,dphi)
      implicit none
      real*8 getdr,deta,dphi 
      getdr=sqrt(deta**2+dphi**2)
      end

      function islept(j)
      implicit none
      logical islept
      integer j
      if(abs(j).ge.11.and.abs(j).le.15) then
         islept = .true.
      else
         islept = .false.
      endif
      end


      real*8 function cstar(p1,p2)
      implicit none
      real*8 p1(4),p2(4),psum(4)
*
      real*8 dotp
      external dotp
*
      real*8 rq2,cs1p,cs2p,cs1m,cs2m,qmass,pt2,sig
      integer k
*
      psum = p1 + p2
      rq2 = sqrt(2.d0)
! Collins - Soper momenta for particle 1 and 2 
      cs1p = (p1(4) + p1(3))/rq2
      cs2p = (p2(4) + p2(3))/rq2
      cs1m = (p1(4) - p1(3))/rq2
      cs2m = (p2(4) - p2(3))/rq2
      qmass = sqrt(psum(4)**2-psum(1)**2-psum(2)**2-psum(3)**2)
      pt2 = psum(1)**2 + psum(2)**2
      cstar = 2.d0/qmass/sqrt(qmass**2 + pt2)*(cs1p*cs2m - cs1m*cs2p)
! for a ppbar should end here
c      if (hadr1.eq.hadr2) then
         sig = 1.d0
         if (psum(3).ne.0.d0) sig = abs(psum(3))/psum(3)
         cstar = cstar * sig
c      endif
      return
      end
*
      real*8 function phistar_report(p2,p1)
      implicit none
      include 'pwhg_math.h' 
      real*8 p1(4),p2(4)
*
      real*8 phim,phip,dphi,dphio2,etam,etap,detao2
      real*8 cthetastar,sthetastar
      real*8 geteta
      external geteta
*
      phim= atan2(p2(2),p2(1))
      phip= atan2(p1(2),p1(1))
      dphi= phim-phip
      dphio2= (pi - dphi)/2.d0
      etam= geteta(p2)
      etap= geteta(p1)
      detao2= (etam-etap)/2.d0
      cthetastar= tanh(detao2)
      sthetastar= sqrt(1.d0-cthetastar**2)
      phistar_report= tan(dphio2) * sthetastar

      return
      end



      subroutine get_ang_coeffs(p1,p2,dsig)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      real * 8 dsig
      real *8 p1(0:3),p2(0:3),res(0:3)
      real *8 a(0:7)
      real *8 theta,lcos,genphi,ptvb
      real *8 mom0,mom1,mom2,mom3,mom4,mom5,mom6,mom7
c //==========================================================
c     // <m0> = <(1/2)*(1-3cos^2(tjeta))> = (3/20)*(A0 - (2/3))
c     // <m1> = <sin(2*theta)*cos(phi)> = (1/5)*A1
c     // <m2> = <sin^2(theta)*cos(2*phi)> = (1/10)*A2
c     // <m3> = <sin(theta)*cos(phi)> = (1/4)*A3
c     // <m4> = <cos(theta)> - (1/4)*A4
c     // <m5> = <sin^2(theta)*sin(2*phi)> = (1/5)*A5
c     // <m6> = <sin(2*theta)*sin(phi)> = (1/5)*A6
c     // <m7> = <sin(theta)*sin(phi)> = (1/4)*A7
c     //======================================================
      
      call calCSVariables(p1,p2,res,.false.)
      
      theta=dacos(res(0))
c      if(abs(res(0)-kn_cthdec).gt.1d-16) then
c         write(*,*) ' cos theta: ', res(0), kn_cthdec,res(0)/kn_cthdec
c      endif
      lcos=res(0)
      genphi=res(3)

      mom0 = 0.5d0*(1-3*lcos*lcos)
      mom1 = dsin(2d0*theta)*dcos(genphi)
      mom2 = dsin(theta)*dsin(theta)*dcos(2d0*genphi)
      mom3 = dsin(theta)*dcos(genphi)
      mom4 = lcos                 
      mom5 = dsin(theta)*dsin(theta)*dsin(2d0*genphi)
      mom6 = dsin(2d0*theta)*dsin(genphi)
      mom7 = dsin(theta)*dsin(genphi)

      a(0)   = (20d0/3d0)*mom0 + (2d0/3d0)
      a(1)   = 5*mom1
      a(2)   = 10*mom2
      a(3)   = 4*mom3
      a(4)   = 4*mom4
      a(5)   = 5*mom5
      a(6)   = 5*mom6
      a(7)   = 4*mom7



      ptvb = sqrt((p1(1)+p2(1))**2 + (p1(2)+p2(2))**2)

      if (ptvb.le.5d0) call filld('lcos5',lcos,dsig)
      if ((ptvb.gt.5d0).and.(ptvb.le.10d0))  call filld('lcos10',
     $    lcos,dsig)
      if ((ptvb.gt.10d0).and.(ptvb.le.20d0)) call filld('lcos20',
     $     lcos,dsig)
      if ((ptvb.gt.20d0).and.(ptvb.le.40d0)) call filld('lcos40',
     $     lcos,dsig)
      if (ptvb.gt.40d0) call filld('lcosg40',lcos,dsig)
c
      if (ptvb.le.5d0) call filld('genphi5',genphi,dsig)
      if ((ptvb.gt.5d0).and.(ptvb.le.10d0))  call filld('genphi10',
     $     genphi,dsig)
      if ((ptvb.gt.10d0).and.(ptvb.le.20d0)) call filld('genphi20',
     $     genphi,dsig)
      if ((ptvb.gt.20d0).and.(ptvb.le.40d0)) call filld('genphi40',
     $     genphi,dsig)
      if (ptvb.gt.40d0) call filld('genphig40',genphi,dsig)
      

      call filld('a0',ptvb,dsig*a(0))

      call filld('a1',ptvb,dsig*a(1))

      call filld('a2',ptvb,dsig*a(2))

      call filld('a3',ptvb,dsig*a(3))

      call filld('a4',ptvb,dsig*a(4))

      call filld('a5',ptvb,dsig*a(5))

      call filld('a6',ptvb,dsig*a(6))

      call filld('a7',ptvb,dsig*a(7))


      end




      subroutine calCSVariables(p1,p2,res,swap)
      implicit none
      include '../include/LesHouches.h'
      include 'nlegborn.h'
      include '../include/pwhg_kn.h'
      real *8 p1(0:3),p2(0:3),res(0:3)
      logical swap
      real *8 Pbeam(0:3),Ptarget(0:3),Q(0:3)
      real *8 p1plus,p1minus,p2plus,p2minus,costheta
      integer nu
      real *8 Qmag,Qpt
      real *8 D(0:3),dt_qt,sin2theta,Dpt
      real *8 R(3),Rmag,Runit(3),Qt(3),Qtunit(3),Dt(3),tanphi,phi
      real *8 dotp,dotp3
      external dotp,dotp3

      do nu=0,3
         Pbeam(nu)=0
         Ptarget(nu)=0
         Q(nu)=p1(nu)+p2(nu)
      enddo
      Pbeam(0)=ebmup(1)
      Ptarget(0)=ebmup(2)
      Pbeam(3)=ebmup(1)
      Ptarget(3)=-ebmup(2)

      Qmag=sqrt(dotp(Q,Q))
      Qpt=sqrt(Q(1)**2+Q(2)**2)
c*********************************************************************
c*
c* 1) cos(theta) = 2 Q^-1 (Q^2+Qt^2)^-1/2 (p1^+ p2^- - p1^- p2^+)
c*
c*
c*********************************************************************
    
      p1plus=1d0/sqrt(2d0) * (p1(0) + p1(3))
      p1minus = 1d0/sqrt(2d0) * (p1(0) - p1(3))
      p2plus=1d0/sqrt(2d0) * (p2(0) + p2(3))
      p2minus = 1d0/sqrt(2d0) * (p2(0) - p2(3))

      costheta = 2d0 / Qmag / sqrt(Qmag**2 + 
     $     Qpt**2) * (p1plus * p2minus - p1minus * p2plus)

      if (swap) costheta = -costheta

c/********************************************************************
c*
c* 2) sin2(theta) = Q^-2 Dt^2 - Q^-2 (Q^2 + Qt^2)^-1 * (Dt dot Qt)^2
c*
c********************************************************************
      do nu=0,3
         D(nu)=p1(nu)-p2(nu)
      enddo
      Dpt=sqrt(D(1)**2+D(2)**2)
      dt_qt = D(1)*Q(1) + D(2)*Q(2)
      sin2theta=(DPt/QMag)**2 -1d0/QMag**2/(QMag**2 + QPt**2)*dt_qt**2

c      if (abs(sin2theta+(costheta*costheta)-1d0).gt.1d-6) then
c         write (*,*) "HAHA",abs(sin2theta+(costheta*costheta)-1d0),Qpt
c         stop
c      endif

c/********************************************************************
c*
c* 3) tanphi = (Q^2 + Qt^2)^1/2 / Q (Dt dot R unit) /(Dt dot Qt unit)
c*
c*********************************************************************
c// unit vector on R direction

      if(Qpt.gt.0d0) then
         call cross3(pbeam(1),Q(1),R)
         Rmag=sqrt(dotp3(R,R))

         Runit(1)=R(1)/Rmag
         Runit(2)=R(2)/Rmag
         Runit(3)=R(3)/Rmag

         Qt(1)=Q(1)
         Qt(2)=Q(2)
         Qt(3)=0

         Qtunit(1)=Qt(1)/Qpt
         Qtunit(2)=Qt(2)/Qpt
         Qtunit(3)=0
    
      
         Dt(1)=D(1)
         Dt(2)=D(2)
         Dt(3)=0

      
         tanphi=sqrt( Qmag**2 + Qpt**2) / Qmag * dotp3(Dt,Runit)/
     $        dotp3(Dt,Qtunit)

         if (swap) tanphi = -tanphi

         phi=atan2(sqrt(Qmag**2 + Qpt**2 )* dotp3(Dt,Runit),QMag
     $        *dotp3(Dt,Qtunit))


         if (swap) phi = atan2(-sqrt(QMag**2+ QPt**2)*dotp3(Dt,Runit)
     $        ,QMag*dotp3(Dt,Qtunit))

      else
         tanphi=0
         phi=0
      endif

      res(0)=costheta
      res(1)=sin2theta
      res(2)=tanphi
      res(3)=phi
      end

      function dotp3(p1,p2)
      implicit none
      real * 8 dotp3,p1(3),p2(3)
      dotp3 = p1(1)*p2(1) + p1(2)*p2(2) + p1(3)*p2(3)
      end

      subroutine cross3(p1,p2,p3)
      implicit none
      real * 8 p3(3),p1(3),p2(3)
      p3(1) = p1(2)*p2(3)-p1(3)*p2(2)
      p3(2) = p1(3)*p2(1)-p1(1)*p2(3)
      p3(3) = p1(1)*p2(2)-p1(2)*p2(1)
      end
