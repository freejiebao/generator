c Mappings of the underlying born configuration in
c kn_cmpborn(0:3,nlegborn), and the xrad(1:3) variables
c in the unit cube, into kn_real(0:3,nlegreal).
c The factor jac_over_csi*csi*kn_csimax, multiplied
c by the Born phase space jacobian, yields the real phase
c space jacobian.
c More explicitly:
c d Phi_n = d^3 xrad jac_over_csi csi csimax d Phi_{n-1}
c Since
c  d Phi_n = d phi d y d csi Jrad d Phi_{n-1}
c (where Jrad is given in FNO2006) we get
c                                  d phi d y d csi
c csimax csi jac_over_csi = Jrad  ----------------
c                                    d^3 xrad
c Notice that using d csi=d csitilde csimax the csimax
c factor cancels, and jac_over_csi is as given in the
c code below (see notes on xscaled.tm).
c gen_real_phsp_fsr: provides the mapping for the final state
c radiation, assuming that the emitter is the kn_emitter-th
c particle, and the emitted particle is the nlegreal-th particle
c gen_real_phsp_isr: mapping for the initial state radiation
      subroutine gen_real_phsp_fsr(xrad,
     #   jac_over_csi,jac_over_csi_coll,jac_over_csi_soft)
      implicit none
      real * 8 xrad(3),jac_over_csi,
     #        jac_over_csi_coll,jac_over_csi_soft
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_par.h'
      include 'pwhg_flg.h'
      real * 8 betaem,ombetaem
c     local common block
      real * 8 q0,q2,e0em
      common/gen_real_phspc/q0,q2,e0em
      real * 8 xjac
c find rad_kinreg as function of kn_emitter
      rad_kinreg=kn_emitter+2-flst_lightpart
      if(flg_jacsing) then
         kn_csitilde=(1-par_fsrtinycsi)
     1        -(1-xrad(1))**2*(1-2*par_fsrtinycsi)
         xjac=2*(1-xrad(1))
      else
         kn_csitilde=xrad(1)*(1-2*par_fsrtinycsi)+par_fsrtinycsi
         xjac=1
      endif
c Importance sampling in case of massive emitter
c we need to sample at angles of order m/e (dead cone size)
      if(kn_masses(kn_emitter).gt.0) then
c compute (underlying born) beta of massive emitter
         call compbetaem(betaem,ombetaem)
         kn_y= 1.d0/betaem*
     +        ( 1d0 - (1d0+betaem) * 
     +        exp(-xrad(2)*log((1d0+betaem)/(ombetaem))) )
         xjac= xjac*( 1d0-betaem*kn_y )
     +        *(log((1.d0+betaem)/(ombetaem)))/betaem
      else
         kn_y=1-2*xrad(2)
         xjac=xjac*2
c importance sampling for kn_y
         xjac=xjac*1.5d0*(1-kn_y**2)
         kn_y=1.5d0*(kn_y-kn_y**3/3)*(1-par_fsrtinyy)
c Even more severe importance sampling at the endpoints (almost never needed)
c         xjac = xjac * 15*(kn_y-1)**2*(kn_y+1)**2/8
c         kn_y=(3*kn_y**5-10*kn_y**3+15*kn_y)/8.0
      endif
      kn_azi=2*pi*xrad(3)
      xjac=xjac*2*pi
      call compcsimaxfsr
      kn_csi=kn_csitilde*kn_csimax     
c remember: no csimax in the jacobian factor, we are integrating in csitilde 
c     if(flg_newrad) then
      call gen_real_phsp_fsr_rad_g
c     else
c     call gen_real_phsp_fsr_rad_old
c     endif
      jac_over_csi=xjac*kn_jacreal/kn_csi
      jac_over_csi_coll=xjac*q2/(4*pi)**3
     #                *(1-kn_csi/2*q0/e0em)
      jac_over_csi_soft=xjac*q2/(4*pi)**3
      end

      subroutine gen_real_phsp_fsr_rad0
c     Same as gen_real_phsp_fsr_rad, but for given kn_csitilde
c     instead of kn_csi.
c     Used in the generation of radiation
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
c Boost the underlying Born variables to their cm frame
      kn_emitter=flst_lightpart+rad_kinreg-2
      call compcsimaxfsr
      kn_csi=kn_csitilde*kn_csimax
c remember: no csimax in the jacobian factor, we are integrating in csitilde 
c     if(flg_newrad) then
      call gen_real_phsp_fsr_rad_g
c     else
c     call gen_real_phsp_fsr_rad_old
c     endif
      end

      subroutine printmom(iun)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      integer mu,j,iun
      character  * 2 ch(13)
      data ch/'+ ','- ','t ','t~','W+','W-','l+',
     1 'nu','l-','n~','b ','b~',' '/
      write(iun,*) '**********************************'
      write(iun,*) ' emitter ',kn_emitter
      write(iun,*) ' preal'
      do j=1,flst_ireallength
         write(iun,'(4(2x,d10.4),3x,a)')
     1        (kn_preal(mu,j),mu=1,3),kn_preal(0,j)
     1        ,ch(j)
      enddo
      write(iun,*) ' pborn'
      do j=1,flst_ibornlength
         write(iun,'(4(2x,d10.4),3x,a)')
     1        (kn_pborn(mu,j),mu=1,3),kn_pborn(0,j)
     1        ,ch(j)
      enddo
      write(iun,*) ' cmpreal'
      do j=1,flst_ireallength
         write(iun,'(4(2x,d10.4),3x,a)')
     1        (kn_cmpreal(mu,j),mu=1,3),kn_cmpreal(0,j)
     1        ,ch(j)
      enddo
      write(iun,*) ' cmpborn'
      do j=1,flst_ibornlength
         write(iun,'(4(2x,d10.4),3x,a)')
     1        (kn_cmpborn(mu,j),mu=1,3),kn_cmpborn(0,j)
     1        ,ch(j)
      enddo
      end


      logical function phsp_sonof(i,j)
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer i,j,jcur,mo
      jcur=j
 1    mo=flst_bornrescurr(jcur)
      if(mo.eq.i) then
         phsp_sonof=.true.
      elseif(mo.ne.0) then
        jcur=mo
        goto 1
      else
         phsp_sonof=.false.
      endif
      end

c This routine performs the inverse mapping from barred and radiation
c variables to the n+1 momenta, as in Sec. 5.2.1 in fno2006.
c All particle can have masses, except for the n+1-th and j-th.
c conventions: vector(4)=(x,y,z,t)
c Input:
c n           : number of final state barred momenta
c j           : the emitter
c q0          : CM energy
c barredk(4,n): the n barred-k 4-vectors
c csi,y,phi   : the radiation variables
c Output:
c xk(4,n+1)   : the n+1 real final state momenta
c jac         : jacobian factor on phirad
      subroutine barradmap(n,j,q0,barredk,csi,y,phi,xk,jac)
      implicit none
c parameters
      include 'pwhg_math.h'
      integer n,j
      real * 8 q0,barredk(0:3,n),csi,y,phi,xk(0:3,n+1),jac
C Local variables
      real * 8 q2,mrec2,k0np1,uknp1,ukj,uk,cpsi,cpsi1,ubkj,vec(3),
     #     norm,k0rec,ukrec,beta,k2
      integer i
c     according to fno2006: by k0 we mean the 0 component in the CM, by
c     uk (underlined k) we mean the modulus of its 3-momentum n and np1
c     in a variable name suggests n and n+1, etc.
      q2=q0**2
c (5.42) of fnw2006
      k0np1=csi*q0/2
      uknp1=k0np1
c compute Mrec^2 (5.45)
      mrec2=(q0-barredk(0,j))**2
     #     -barredk(1,j)**2-barredk(2,j)**2-barredk(3,j)**2
      ukj=(q2-mrec2-2*q0*uknp1)/(2*(q0-uknp1*(1-y)))
c compute the length of k (5.44)
      uk=sqrt(ukj**2+uknp1**2+2*ukj*uknp1*y)
c compute cos psi (angle between knp1 and k)
      cpsi=(uk**2+uknp1**2-ukj**2)/(2*uk*uknp1)
c get the cosine of the angle between kn and k
      cpsi1=(uk**2+ukj**2-uknp1**2)/(2*uk*ukj)
c Set k_j and k_n+1 parallel to kbar_n
      ubkj=barredk(0,j)
      do i=0,3
         xk(i,j)=ukj*barredk(i,j)/ubkj
         xk(i,n+1)=uknp1*barredk(i,j)/ubkj
      enddo
c Set up a unit vector orthogonal to kbar_n and to the z axis
      vec(3)=0
      norm=sqrt(barredk(1,j)**2+barredk(2,j)**2)
      vec(1)=barredk(2,j)/norm
      vec(2)=-barredk(1,j)/norm
c Rotate k_n+1 around vec of an amount psi
      call mrotate(vec,sqrt(abs(1-cpsi**2)),cpsi,xk(1,n+1))
c Rotate k_j around vec of an amount psi1 in opposite direction
      call mrotate(vec,-sqrt(abs(1-cpsi1**2)),cpsi1,xk(1,j))
c set up a unit vector parallel to kbar_j
      do i=1,3
         vec(i)=barredk(i,j)/ubkj
      enddo
c Rotate k_j and k_n+1 around this vector of an amount phi
      call mrotate(vec,sin(phi),cos(phi),xk(1,n+1))
      call mrotate(vec,sin(phi),cos(phi),xk(1,j))
c compute the boost velocity
      k0rec=q0-ukj-uknp1
c use abs to fix tiny negative root FPE
      ukrec=sqrt(abs(k0rec**2-mrec2))
      beta=(q2-(k0rec+ukrec)**2)/(q2+(k0rec+ukrec)**2)
c     Boost all other barred k (i.e. 1 to j-1,j+1 to n) along vec with velocity
c     beta in the k direction (same as barred k_j)
      do i=1,3
         vec(i)=barredk(i,j)/ubkj
      enddo
      if(j-1 > 0) call mboost(j-1,vec,beta,barredk(0,1),xk(0,1))
      if(n-j > 0) call mboost(n-j,vec,beta,barredk(0,j+1),xk(0,j+1))
      k2=2*ukj*uknp1*(1-y)
c returns jacobian of FNO 5.40 (i.e. jac*d csi * d y * d phi is phase space)
      jac=q2*csi/(4*pi)**3*ukj**2/ubkj/(ukj-k2/(2*q0))
      end

c This routine is as the previous one,
c in case the emitter is massive.
      subroutine barradmapmv8(n,j,m2,q0,barredk,csi,y,phi,xk,jac)
      implicit none
c parameters
      include 'pwhg_math.h'
      integer n,j
      real * 8 q0,barredk(0:3,n),csi,y,phi,xk(0:3,n+1),jac
C Local variables
      real * 8 m2,q2,mrec2,k0np1,uknp1,ukj,k0j,uk,cpsi,cpsi1,vec(3),
     1     norm,k0rec,ukrec,beta,ukj0,alpha,
     2     ubkj,bk0j,bk0rec,ubkrec,k0jmax,k0recmax,z,z1,z2
      integer i
      real * 8 cosjnp1soft,sinjnp1soft
      common/ccosjnp1soft/cosjnp1soft,sinjnp1soft
      jac=1
c     according to fno2006: by k0 we mean the 0 component in the CM, by
c     uk (underlined k) we mean the modulus of its 3-momentum n and np1
c     in a variable name suggests n and n+1, etc.
      q2=q0**2
c (5.42) of fnw2006
      k0np1=csi*q0/2
c our reference is the Dalitz phase space d k0jp1 dk0j
      jac=jac*q0/2
      uknp1=k0np1
c compute Mrec^2 (5.45)
      mrec2=(q0-barredk(0,j))**2
     #     -barredk(1,j)**2-barredk(2,j)**2-barredk(3,j)**2
      k0recmax = (q2-m2+mrec2)/(2*q0)
      k0jmax   = (q2+m2-mrec2)/(2*q0)
      z1=(k0recmax+sqrt(k0recmax**2-mrec2))/q0
      z2=(k0recmax-sqrt(k0recmax**2-mrec2))/q0
      z=z2-(z2-z1)*(1+y)/2
      jac=jac*(z1-z2)/2
      k0j=k0jmax-k0np1*z
      jac=jac*k0np1
      ukj=sqrt(k0j**2-m2)
      k0rec=q0-k0np1-k0j
      ukrec=sqrt(k0rec**2-mrec2)
      uk=ukrec
c compute cos psi (angle between knp1 and k)
      cpsi=(uk**2+uknp1**2-ukj**2)/(2*uk*uknp1)
c get the cosine of the angle between kj and k
      cpsi1=(uk**2+ukj**2-uknp1**2)/(2*uk*ukj)
c Set k_j and k_n+1 parallel to kbar_j
      ubkj=sqrt(barredk(1,j)**2+barredk(2,j)**2+barredk(3,j)**2)
      bk0j=barredk(0,j)
      do i=0,3
         xk(i,n+1)=uknp1*barredk(i,j)/ubkj
      enddo
      xk(0,n+1)= k0np1
      do i=1,3
         xk(i,j)=ukj*barredk(i,j)/ubkj
      enddo
      xk(0,j)=k0j
c Set up a unit vector orthogonal to kbar_n and to the z axis
      vec(3)=0
      norm=sqrt(barredk(1,j)**2+barredk(2,j)**2)
      vec(1)=barredk(2,j)/norm
      vec(2)=-barredk(1,j)/norm
c Rotate k_n+1 around vec of an amount psi
      call mrotate(vec,sqrt(abs(1-cpsi**2)),cpsi,xk(1,n+1))
c Rotate k_j around vec of an amount psi1 in opposite direction
      call mrotate(vec,-sqrt(abs(1-cpsi1**2)),cpsi1,xk(1,j))
c set up a unit vector parallel to kbar_j
      do i=1,3
         vec(i)=barredk(i,j)/ubkj
      enddo
c Rotate k_j and k_n+1 around this vector of an amount phi
      call mrotate(vec,sin(phi),cos(phi),xk(1,n+1))
      call mrotate(vec,sin(phi),cos(phi),xk(1,j))
c find boost of recoil system
      bk0rec=q0-bk0j
      ubkrec=ubkj
      alpha=(k0rec+ukrec)/(bk0rec+ubkrec)
      beta=(1-alpha**2)/(1+alpha**2)
c massless limit is
c     beta=(q2-(k0rec+ukrec)**2)/(q2+(k0rec+ukrec)**2)
c     Boost all other barred k (i.e. 1 to j-1,j+1 to n) along vec with velocity
c     beta in the k direction (same as barred k_j)
      do i=1,3
         vec(i)=barredk(i,j)/ubkj
      enddo
      if(j-1 > 0) call mboost(j-1,vec,beta,barredk(0,1),xk(0,1))
      if(n-j > 0) call mboost(n-j,vec,beta,barredk(0,j+1),xk(0,j+1))
c 
      jac=jac*q0/((2*pi)**3*2*ubkj)
c compute the cosine of the angle between kj and kn+1 IN THE SOFT LIMIT.
c this must replace kn_y when computing the soft limit vector
c since kn_y has a different meaning here
      cosjnp1soft=(2*q2*z-q2-mrec2+m2)/(sqrt(k0jmax**2-m2)*q0)/2
      end

c END FSR
c ISR:


      subroutine gen_real_phsp_isr(xrad,
     #    jac_over_csi,jac_over_csi_p,jac_over_csi_m,jac_over_csi_s)
      implicit none
      real * 8 xrad(3),
     #    jac_over_csi,jac_over_csi_p,jac_over_csi_m,jac_over_csi_s
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_par.h'
      real * 8 xjac
      rad_kinreg=1
      kn_csitilde=(3-2*xrad(1))*xrad(1)**2
      xjac=6*(1-xrad(1))*xrad(1)
      kn_csitilde=kn_csitilde*(1-2*par_isrtinycsi)+par_isrtinycsi
      kn_y=1-2*xrad(2)
      xjac=xjac*2
      xjac=xjac*1.5d0*(1-kn_y**2)
      kn_y=1.5d0*(kn_y-kn_y**3/3)*(1-par_isrtinyy)
      kn_azi=2*pi*xrad(3)
      xjac=xjac*2*pi
      call compcsimaxisr
      kn_csi=kn_csitilde*kn_csimax
      kn_csip=kn_csitilde*kn_csimaxp
      kn_csim=kn_csitilde*kn_csimaxm
c     if(flg_newrad) then
      call gen_real_phsp_isr_rad_g
c     else
c     call gen_real_phsp_isr_rad_old
c     endif
      jac_over_csi=xjac*kn_jacreal/kn_csi
      jac_over_csi_p=xjac*(kn_sborn/(1-kn_csip))/(4*pi)**3/(1-kn_csip)
      jac_over_csi_m=xjac*(kn_sborn/(1-kn_csim))/(4*pi)**3/(1-kn_csim)
c here we need the Born s (real s is function of Born s via csi)
      jac_over_csi_s=xjac*(kn_sborn)/(4*pi)**3
c      call checkmomzero(flst_ireallength,kn_preal)
      end

      subroutine compcsimaxisr
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      call compcsimaxisr_g
     1     (kn_xb1,kn_xb2,kn_y,kn_csimax,kn_csimaxp,kn_csimaxm)
      end

      subroutine comppt2fsrmv(y,csi,pt2)
c this subroutine computes the scale of the coupling in case
c of a massive final state emitter
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_mvem.h'
      real * 8 y,csi,pt2
      real * 8 z
      call setupmvemitter
      z=z2-(z2-z1)*(1+y)/2
      pt2=csi**2*q**3*(1-z)/(2*p0max-z*csi*q)
      end

      subroutine compubradmv(y,csi,ub)
      implicit none
      include 'pwhg_mvem.h'
      integer em
      real * 8 y,csi,ub
      real * 8 z
      call setupmvemitter
      z=z2-(z2-z1)*(1+y)/2
      ub=q/sqrt(p0max**2-m2)/(csi*(1-z))*(z1-z2)/2
      end


      subroutine compintub(t,integral)
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_mvem.h'
      real * 8 t,integral
      real * 8 csimin,csi1,csi
      call setupmvemitter
      if(t.gt.kt2max) then
         integral = 0
         return
      endif
      csimin=(sqrt(t*(t*z2**2+8*p0max*q*(1-z2)))-t*z2)/(2*q**2*(1-z2))
c      csi1=(sqrt(t*(t*z1**2+8*p0max*q*(1-z1)))-t*z1)/(2*q**2*(1-z1))
c The following form is equivalent to the above, but has no large rounding
c errors when z1->1
      csi1=4*p0max*t/q/
     1 (sqrt(t*(t*z1**2+8*p0max*q*(1-z1)))+t*z1)
      csi=min(csimax,csi1)
      if(csi*q**2-t.lt.0.or.2*p0max-csi*q.lt.0) goto 998
      integral=
     1     log(csi)*log((1-z2)*q/t)+log(csi)**2/2+pwhg_gfun(-t,q**2,csi)
     2     -pwhg_gfun(2*p0max,-q,csi)
      csi=csimin
      if(csi*q**2-t.lt.0.or.2*p0max-csi*q.lt.0) goto 998
      integral=integral - (
     1     log(csi)*log((1-z2)*q/t)+log(csi)**2/2+pwhg_gfun(-t,q**2,csi)
     2     -pwhg_gfun(2*p0max,-q,csi)
     3 )
      if(csimax.gt.csi1) then
         integral=integral+log(csimax/csi1)*log((1-z2)/(1-z1))
      endif
c don't forget q0/pvec d phi integration!
      integral=integral*q/sqrt(p0max**2-m2)*2*pi
      return
 998  continue
      write(*,*) ' negative!!!'
      contains
      function pwhg_gfun(a,b,csi)
c returns the indefinite integral
c Int d csi/csi log(a+b*csi), defined to vanish when a+b*csi=0,
c It assumes that a+b*csi>0 and csi>0 in the range of integration
      implicit none
      real * 8 pwhg_gfun,a,b,csi
      real * 8 pi
      parameter (pi=3.141592653589793d0)
      real * 8 ddilog
      external ddilog
      if(a.lt.0) then
         pwhg_gfun=log(b*csi+a)*log(1-(b*csi+a)/a)+ddilog((b*csi+a)/a)
      else
         pwhg_gfun=log(abs(b*csi/a))*log(a)-ddilog(-b*csi/a)+pi**2/6
      endif
      end function pwhg_gfun
      end

      subroutine gencsiymv(t,rv,csi,y)
      implicit none
      real * 8 t,rv,csi,y
      include 'pwhg_mvem.h'
      real * 8 csimin,csi1,csim,csimaxz,z
      call setupmvemitter
      csimin=(sqrt(t*(t*z2**2+8*p0max*q*(1-z2)))-t*z2)/(2*q**2*(1-z2))
      csi1=(sqrt(t*(t*z1**2+8*p0max*q*(1-z1)))-t*z1)/(2*q**2*(1-z1))
      csim=min(csimax,csi1)
      csi=(exp(log(csimin*q**2-t)
     1     +rv*log((csim*q**2-t)/(csimin*q**2-t)))+t)/q**2
      z=(csi**2*q**3-2*t*p0max)/(csi*q*(csi*q**2-t))
      y=2*(z-z2)/(z1-z2)-1
      csimaxz=-(q**2*z**2-2*q*k0recmax*z+mrec2)/(q**2*z*(1-z))
      if(csi.gt.csimaxz) then
c this signals if we are out of the relevant Dalitz region
         csi=2
      endif
      end

      subroutine setupmvemitter
c setup all quantities depending only upon the underlying born
c configuration for the massive emitter
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_mvem.h'
      integer em,ires
      real * 8 pres(0:3),pem(0:3)
      em=flst_lightpart+rad_kinreg-2
      kn_emitter = em
      if(flst_bornrescurr(em).ne.0) then
c Find four momentum of resonance
         ires=flst_bornrescurr(em)
         pres=kn_cmpborn(:,ires)
         pem=kn_cmpborn(:,em)
         q=sqrt(pres(0)**2-pres(1)**2-pres(2)**2-pres(3)**2)
         mrec2=(pres(0)-pem(0))**2-(pres(1)-pem(1))**2
     1        -(pres(2)-pem(2))**2-(pres(3)-pem(3))**2
      else
         q=kn_cmpborn(0,1)+kn_cmpborn(0,2)
         mrec2=(q-kn_cmpborn(0,em))**2
     1     -kn_cmpborn(1,em)**2-kn_cmpborn(2,em)**2-kn_cmpborn(3,em)**2
      endif
      mrec2=abs(mrec2)
      if(mrec2.lt.1d-10) mrec2=0
      m2=kn_masses(em)**2
      if(m2.gt.0) then
         csimax=1-(sqrt(m2)+sqrt(mrec2))**2/q**2
         k0recmax = (q**2-m2+mrec2)/(2*q)
         p0max   = (q**2+m2-mrec2)/(2*q)
         z1=(k0recmax+sqrt(k0recmax**2-mrec2))/q
         z2=(k0recmax-sqrt(k0recmax**2-mrec2))/q
         kt2max=csimax**2*q**3*(1-z2)/(2*p0max-z2*csimax*q)
      else
         csimax=1-mrec2/q**2
         kn_csimax=csimax
         k0recmax = (q**2+mrec2)/(2*q)
         p0max   = (q**2-mrec2)/(2*q)
         z1=1
         z2=1-csimax
         kt2max=(csimax*q)**2
      endif
      end



c     Same as gen_real_phsp_isr_rad, but for given kn_csitilde
c     instead of kn_csi.
      subroutine gen_real_phsp_isr_rad0
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      call compcsimaxisr
      kn_csi=kn_csitilde*kn_csimax
c     if(flg_newrad) then
      call gen_real_phsp_isr_rad_g
c     else
c     call gen_real_phsp_isr_rad_old
c     endif
      end


      subroutine compcmkin
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      real * 8 vecl(3),betal
      data vecl/0d0,0d0,1d0/
      save vecl
      betal=-(kn_preal(3,1)+kn_preal(3,2))/(kn_preal(0,1)+kn_preal(0,2))
      call mboost(flst_ireallength,vecl,betal,kn_preal,kn_cmpreal)
      end

      subroutine setsoftvecfsr
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      integer em,j
      real * 8 y,norm,dir(3)
      real * 8 pres(0:3),pem(0:3),vec(3),beta
      integer kres
      em=kn_emitter
      if(em.gt.2) then
         kres=flst_bornrescurr(em)
         if(kres.ne.0) then
            pres=kn_cmpborn(:,kres)
            beta=sqrt(pres(1)**2+pres(2)**2+pres(3)**2)/pres(0)
            if(beta > 1d-30) then
               vec(1)=pres(1)/(beta*pres(0))
               vec(2)=pres(2)/(beta*pres(0))
               vec(3)=pres(3)/(beta*pres(0))
               call mboost(1,vec,-beta,kn_cmpborn(:,em),pem)
            else
               pem=kn_cmpborn(:,em)
            endif
         else
            pem=kn_cmpborn(:,em)
         endif
c Now pem is the emitter in the resonance CM frame
      else
         kres=0
         pem=kn_cmpborn(:,em)
      endif
      y=kn_y
c set soft vector parallel to the emitter
      do j=0,3
         kn_softvec(j)=pem(j)/pem(0)
      enddo
c Set up a unit vector orthogonal to p_em and to the z axis
      dir(3)=0
      norm=sqrt(pem(1)**2+pem(2)**2)
      dir(1)=pem(2)/norm
      dir(2)=-pem(1)/norm
      call mrotate(dir,sqrt(1-y**2),y,kn_softvec(1))
      do j=1,3
         dir(j)=pem(j)/pem(0)
      enddo
c Rotate kn_softvec around dir of an amount azi
      call mrotate(dir,sin(kn_azi),cos(kn_azi),kn_softvec(1))
      if(em.gt.2.and.kres.ne.0) then
         if(beta > 1d-30) then
            call mboost(1,vec,beta,kn_softvec,kn_softvec)
         endif
      endif      
      end

      subroutine setsoftvecfsrmv
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      integer em,j
      real * 8 y,norm,dir(3),kem
      real * 8 cosjnp1soft,sinjnp1soft
      common/ccosjnp1soft/cosjnp1soft,sinjnp1soft
      real * 8 pres(0:3),pem(0:3),vec(3),beta
      integer kres
      em=kn_emitter
      if(em.gt.2) then
         kres=flst_bornrescurr(em)
         if(kres.ne.0) then
            pres=kn_cmpborn(:,kres)
            beta=sqrt(pres(1)**2+pres(2)**2+pres(3)**2)/pres(0)
            if(beta > 1d-30) then
               vec(1)=pres(1)/(beta*pres(0))
               vec(2)=pres(2)/(beta*pres(0))
               vec(3)=pres(3)/(beta*pres(0))
               call mboost(1,vec,-beta,kn_cmpborn(:,em),pem)
            else
               pem=kn_cmpborn(:,em)
            endif
         else
            pem=kn_cmpborn(:,em)
         endif
c Now pres is the emitter in the resonance CM frame
      else
         kres=0
         pem=kn_cmpborn(:,em)
      endif
      y=cosjnp1soft
c set soft vector parallel to the emitter
      kem=sqrt(pem(1)**2+pem(2)**2+pem(3)**2)
      do j=1,3
         kn_softvec(j)=pem(j)/kem
      enddo
      kn_softvec(0)=1
c Set up a unit vector orthogonal to p_em and to the z axis
      dir(3)=0
      norm=sqrt(pem(1)**2+pem(2)**2)
      dir(1)=pem(2)/norm
      dir(2)=-pem(1)/norm
      call mrotate(dir,sqrt(1-y**2),y,kn_softvec(1))
      do j=1,3
         dir(j)=pem(j)/kem
      enddo
c Rotate kn_softvec around dir of an amount azi
      call mrotate(dir,sin(kn_azi),cos(kn_azi),kn_softvec(1))
      if(em.gt.2.and.kres.ne.0) then
         if(beta > 1d-30) then
            call mboost(1,vec,beta,kn_softvec,kn_softvec)
         endif
      endif      
      end

      subroutine setsoftvecisr
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      real * 8 y
      y=kn_y
      kn_softvec(0)=1
      kn_softvec(1)=sqrt(1-y**2)*sin(kn_azi)
      kn_softvec(2)=sqrt(1-y**2)*cos(kn_azi)
      kn_softvec(3)=y
      end

      subroutine compbetaem8(betaem,ombeta)
      implicit none
      real * 8 betaem,ombeta
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      real * 8 q0,m2,mrec2,pj(0:3)
      real * 8 k0emmax
      integer j,kres
      real * 8 dotp
      external dotp
      j=kn_emitter
      if(j.gt.2) then
         kres=flst_bornrescurr(j)
      else
         kres=0
      endif
      if(kres.gt.0) then
         call boost2reson(kn_cmpborn(:,kres),1,
     1        kn_cmpborn(:,j),pj)
         q0=sqrt(dotp(kn_cmpborn(:,kres),kn_cmpborn(:,kres)))
      else
         pj=kn_cmpborn(:,j)
         q0=2*kn_cmpborn(0,1)
      endif
      kn_q0=q0
      mrec2=(q0-pj(0))**2-pj(1)**2-pj(2)**2-pj(3)**2
      m2=kn_masses(j)**2
      k0emmax = (q0**2-mrec2+m2)/(2*q0)
      betaem=sqrt(1-m2/k0emmax**2)
c 1-b=(1-b^2)/(1+b)
      ombeta=m2/k0emmax**2/(1+betaem)
      end

      subroutine gen_real_phsp_fsr_rad_g
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_flg.h'
      kn_emitter=flst_lightpart+rad_kinreg-2
      
      call gen_real_phsp_fsr_rad_g0(flst_ibornlength,
     1     flst_bornrescurr,kn_emitter,kn_csi,kn_y,kn_azi,
     2     kn_xb1,kn_xb2,kn_masses,kn_pborn,
     3     kn_cmpborn,kn_x1,kn_x2,kn_preal,kn_cmpreal,kn_jacreal)

      kn_sreal=kn_sborn
c     This is to set kn_csimax
      call compcsimaxfsr
c The dij are now computed in "ubprojections.f"
c      call compdij
      if(kn_masses(kn_emitter).eq.0) then
         call setsoftvecfsr
      else
         call setsoftvecfsrmv
      endif
c The dij are now computed in "ubprojections.f"
c      call compdijsoft
      end

c gen_real_phsp_fsr_rad: provides the mapping for the final state
c radiation, assuming that we are considering the region rad_kinreg
c and the emitted particle is the nlegreal-th particle,
c for given argcsi, argy, argazi. Sets the jacobian
c argjacreal so that argjacreal d argcsi d argy d argazi times
c the underlying Born jacobian is the phase space volume
      subroutine gen_real_phsp_fsr_rad_g0(
     1     argnlegb,argreslist,argemitter,argcsi,argy,argazi,
     2     argxb1,argxb2,argmasses,argpborn,
     3     argcmpborn,argx1,argx2,argpreal,argcmpreal,argjacreal)
      implicit none
      include 'pwhg_math.h'
      include 'pwhg_flg.h'
      integer argnlegb,argreslist(argnlegb),argemitter
      real * 8 argcsi,argy,argazi,argxb1,argxb2,argmasses(argnlegb),
     1         argpborn(0:3,argnlegb),argcmpborn(0:3,argnlegb),argx1,argx2,
     2         argcmpreal(0:3,argnlegb+1),argpreal(0:3,argnlegb+1),argjacreal
      real * 8 vec(3),beta,pres(0:3),
     1     moms(0:3,argnlegb),momso(0:3,argnlegb+1),betares,argcsimax
c     local common block
      real * 8 q0,q2,e0em
      common/gen_real_phspc/q0,q2,e0em
      integer i,j,ires,resemitter,lres,nlegr
      data vec/0d0,0d0,1d0/
      save vec

      nlegr = argnlegb + 1
      if(argreslist(argemitter).ne.0) then
c Find four momentum of resonance
         ires=argreslist(argemitter)
         pres=argcmpborn(:,ires)
         lres=0
         do j=3,argnlegb
            if(phsp_sonof(ires,j)) then
               lres=lres+1
               moms(:,lres)=argcmpborn(:,j)
               if(j.eq.argemitter) resemitter=lres
            endif
         enddo
c Find beta of resonance for boost
         betares=sqrt(pres(1)**2+pres(2)**2+pres(3)**2)/pres(0)
         if(betares > 1d-30) then
            vec(1)=pres(1)/(betares*pres(0))
            vec(2)=pres(2)/(betares*pres(0))
            vec(3)=pres(3)/(betares*pres(0))
            call mboost(lres,vec,-betares,moms,moms)
         endif
         e0em=moms(0,resemitter)
         q0=pres(0)*sqrt(1-betares**2)
         q2=q0**2
         if(argmasses(argemitter).eq.0) then
            call barradmap(lres,resemitter,q0,moms,
     1           argcsi,argy,argazi,momso,argjacreal)
         else
c massive case; here argy will assume a different meaning!
            call compcsimaxfsr_g(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
            if(argcsi.gt.argcsimax) then
c if this message never appears, remove the compcsimaxfsr_g call and all
c this check
               write(*,*) ' gen_real_phsp_fsr_rad_g0: bound violation'
     1         //': argcsi=',argcsi,'> argcsimax=', argcsimax 
               argjacreal=0
               return
            endif
            call barradmapmv(lres,resemitter,argmasses(argemitter)**2,
     1           q0,moms,argcsi,argy,argazi,momso,argjacreal)
         endif
         if(betares > 1d-30) then
            call mboost(lres+1,vec,betares,momso,momso)
         endif
c build real momenta out of momso
         lres=0
         do j=3,argnlegb
            if(phsp_sonof(ires,j)) then
               lres=lres+1
               argpreal(:,j)=momso(:,lres)
            else
               argpreal(:,j)=argcmpborn(:,j)
            endif
         enddo
         argpreal(:,nlegr)=momso(:,lres+1)
      else
         q0=2*argcmpborn(0,1)
         q2=q0**2
         e0em=argcmpborn(0,argemitter)
         if(argmasses(argemitter).eq.0) then
            call barradmap(argnlegb-2,argemitter-2,q0,argcmpborn(0,3),
     1           argcsi,argy,argazi,argpreal(0,3),argjacreal)
         else
c massive case; here argy will assume a different meaning!
            call compcsimaxfsr_g(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
            if(argcsi.gt.argcsimax) then
c if this message never appears, remove the compcsimaxfsr_g call and all
c this check
               write(*,*) ' gen_real_phsp_fsr_rad_g0: bound violation'
     1         //': argcsi=',argcsi,'> argcsimax=', argcsimax 
               argjacreal=0
               return
            endif
            call barradmapmv(argnlegb-2,argemitter-2,
     1           argmasses(argemitter)**2,q0,argcmpborn(0,3),
     2           argcsi,argy,argazi,argpreal(0,3),argjacreal)
         endif
c remember: no csimax factor, we are integrating in csitilde 
c         call barradmap(argnlegb-2,argemitter-2,q0,argcmpborn(0,3),
c     1        argcsi,argy,argazi,argpreal(0,3),argjacreal)
      endif
      vec(1)=0
      vec(2)=0
      vec(3)=1
      beta=(argxb1-argxb2)/(argxb1+argxb2)
      call mboost(nlegr-2,vec,beta,argpreal(0,3),argpreal(0,3))
      do i=0,3
         argpreal(i,1)=argpborn(i,1)
         argpreal(i,2)=argpborn(i,2)
      enddo
      argx1=argxb1
      argx2=argxb2
c      call checkmomzero(nlegr,argpreal)
      call compcmkin_g(nlegr,argpreal,argcmpreal)
c The dij are now computed in "ubprojections.f"
c      call compdij
cc The following does no longer belong here. Check that
c  these routines are called (if needed) after this soubroutine is called
c      if(argmasses(argemitter).eq.0) then
c         call setsoftvecfsr
c      else
c         call setsoftvecfsrmv
c      endif
c The dij are now computed in "ubprojections.f"
c      call compdijsoft
      contains

      logical function phsp_sonof(i,j)
      integer i,j,jcur,mo
      jcur=j
 1    mo=argreslist(jcur)
      if(mo.eq.i) then
         phsp_sonof=.true.
      elseif(mo.ne.0) then
        jcur=mo
        goto 1
      else
         phsp_sonof=.false.
      endif
      end function


      end

      subroutine compcsimaxfsr_g8(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
      implicit none
      include 'pwhg_flg.h'
      integer argnlegb,argemitter,argreslist(argnlegb)
      real * 8 argy,argmasses(argnlegb),argcmpborn(0:3,argnlegb),argcsimax
      real * 8 q0,m2,mrec2,k0recmax,knp1max,z1,z2,z,pj(0:3)
      integer j,kres
      real * 8 dotp
      external dotp
      j=argemitter
      kres=argreslist(j)
      if(kres.gt.0) then
         call boost2reson(argcmpborn(:,kres),1,
     1        argcmpborn(:,j),pj)
         q0=sqrt(dotp(argcmpborn(:,kres),argcmpborn(:,kres)))
      else
         pj=argcmpborn(:,j)
         q0=2*argcmpborn(0,1)
      endif
      mrec2=(q0-pj(0))**2-pj(1)**2-pj(2)**2-pj(3)**2
      m2=argmasses(j)**2
      if(m2.eq.0) then
         argcsimax=1-mrec2/q0**2
      else
         k0recmax = (q0**2-m2+mrec2)/(2*q0)
         z1=(k0recmax+sqrt(k0recmax**2-mrec2))/q0
c         z2=(k0recmax-sqrt(k0recmax**2-mrec2))/q0
         z2 = mrec2/(q0**2*z1)
         z=z2-(z2-z1)*(1+argy)/2
         knp1max=-(q0**2*z**2-2*q0*k0recmax*z+mrec2)/(2*q0*z*(1-z))
         argcsimax=2*knp1max/q0
      endif
      end

      subroutine gen_real_phsp_isr_rad_g
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      call gen_real_phsp_isr_rad_g0(
     1     flst_ibornlength,kn_csi,kn_y,kn_azi,kn_beams,
     2     kn_xb1,kn_xb2,kn_pborn,
     3     kn_cmpborn,kn_x1,kn_x2,kn_preal,kn_cmpreal,kn_jacreal)
      kn_sreal = kn_sborn/(1-kn_csi)
c This is to set kn_csimax,kn_csimaxp,kn_csimaxm
      call compcsimaxisr
c      call compdij
      call setsoftvecisr
c      call compdijsoft
      end

      subroutine gen_real_phsp_isr_rad_g0(
     1     argnlegb,argcsi,argy,argazi,argbeams,
     2     argxb1,argxb2,argpborn,
     3     argcmpborn,argx1,argx2,argpreal,argcmpreal,argjacreal)
      implicit none
      include 'pwhg_math.h'
      integer argnlegb
      real * 8 argcsi,argy,argazi,argbeams(0:3,2),argxb1,argxb2,
     1         argpborn(0:3,argnlegb),argcmpborn(0:3,argnlegb),argx1,argx2,
     2         argcmpreal(0:3,argnlegb+1),argpreal(0:3,argnlegb+1),argjacreal
      real * 8 y,xb1,xb2,x1,x2,betal,betat,vecl(3),vect(3),
     1         cth,sth,cph,sph,csi,pt2,argcsimax,argcsimaxp,argcsimaxm,
     2         argsborn,argsreal
      integer i,mu,nlegr
      real * 8 dotp
      external dotp
c the following call sets argcsimax, argcsimaxp, argcsimaxm
c also when gen_real_phsp_isr_rad is called directly
c (i.e. not through gen_real_phsp_isr_rad0)
      call compcsimaxisr_g(argxb1,argxb2,argy,argcsimax,argcsimaxp,argcsimaxm)
      nlegr = argnlegb + 1
      y=argy
      xb1=argxb1
      xb2=argxb2
      csi=argcsi
      cth=y
      sth=sqrt(1-cth**2)
      cph=cos(argazi)
      sph=sin(argazi)
      x1=xb1/sqrt(1-csi)*sqrt((2-csi*(1-y))/(2-csi*(1+y)))
      x2=xb2/sqrt(1-csi)*sqrt((2-csi*(1+y))/(2-csi*(1-y)))
      argx1=x1
      argx2=x2
      argsborn = (2*argcmpborn(0,1))**2
      do mu=0,3
         argpreal(mu,1)=argbeams(mu,1)*x1
         argpreal(mu,2)=argbeams(mu,2)*x2
      enddo
      argsreal=argsborn/(1-csi)
c Build k_n+1 in the rest frame of argpreal
      argpreal(0,nlegr)=sqrt(argsreal)*csi/2
      argpreal(1,nlegr)=argpreal(0,nlegr)*sth*sph
      argpreal(2,nlegr)=argpreal(0,nlegr)*sth*cph
      argpreal(3,nlegr)=argpreal(0,nlegr)*cth
c boost it to the frame of argpreal
      do i=1,3
         vecl(i)=(argpreal(i,1)+argpreal(i,2))
     #          /(argpreal(0,1)+argpreal(0,2))
      enddo      
      betal=sqrt(vecl(1)**2+vecl(2)**2+vecl(3)**2)
      do i=1,3
         vecl(i)=vecl(i)/betal
      enddo
      call mboost(1,vecl,betal,
     #    argpreal(0,nlegr),argpreal(0,nlegr))
c longitudinal boost of underlying Born to zero rapidity frame
      do i=1,3
         vecl(i)=(argpborn(i,1)+argpborn(i,2))
     #          /(argpborn(0,1)+argpborn(0,2))
      enddo
      betal=sqrt(vecl(1)**2+vecl(2)**2+vecl(3)**2)
      do i=1,3
         vecl(i)=vecl(i)/betal
      enddo
      call mboost(argnlegb-2,vecl,-betal,argpborn(0,3),argpreal(0,3))
c      call printtot(flst_ibornlength,argpreal(0,1))
c construct transverse boost velocity
      vect(3)=0
      vect(1)=argpreal(1,nlegr)
      vect(2)=argpreal(2,nlegr)
      pt2=vect(1)**2+vect(2)**2
      betat=1/sqrt(1+(argsreal*(1-csi))/pt2)
      vect(1)=vect(1)/sqrt(pt2)
      vect(2)=vect(2)/sqrt(pt2)
c      write(*,*) ' k+1: ',(argpreal(mu,nlegr),mu=0,3)
      call mboost(argnlegb-2,vect,-betat,argpreal(0,3),argpreal(0,3))
c      call printtot(flst_ibornlength,argpreal(0,1))
c longitudinal boost in opposite direction
      call mboost(argnlegb-2,vecl,betal,argpreal(0,3),argpreal(0,3))
c      call printtot(nlegr,argpreal(0,1))
      argjacreal=argsreal/(4*pi)**3*csi/(1-csi)
      call compcmkin_g(nlegr,argpreal,argcmpreal)
      end



      subroutine compcsimaxisr_g(xb1,xb2,argy,argcsimax,argcsimaxp,argcsimaxm)
      implicit none
      real * 8 xb1,xb2,argy,argcsimax,argcsimaxp,argcsimaxm
      real * 8 y
      y=argy
      argcsimax=1-max(2*(1+y)*xb1**2/
     #    (sqrt((1+xb1**2)**2*(1-y)**2+16*y*xb1**2)+(1-y)*(1-xb1**2)),
     #            2*(1-y)*xb2**2/
     #    (sqrt((1+xb2**2)**2*(1+y)**2-16*y*xb2**2)+(1+y)*(1-xb2**2)))
      argcsimaxp=1-xb1
      argcsimaxm=1-xb2
      end



      subroutine compcmkin_g(n,p,cmp)
      implicit none
      integer n
      real * 8 p(0:3,n),cmp(0:3,n)
      real * 8 vecl(3),betal
      data vecl/0d0,0d0,1d0/
      save vecl
      betal=-(p(3,1)+p(3,2))/(p(0,1)+p(0,2))
      call mboost(n,vecl,betal,p,cmp)
      end


c From now to the end the *16 improved subroutines for massive emitters
      subroutine compcsimaxfsr
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      integer, parameter :: argnlegb=nlegborn
      integer argemitter,argreslist(argnlegb)
      real * 8 argy,argmasses(argnlegb),argcmpborn(0:3,argnlegb),argcsimax
      argemitter = kn_emitter
      argreslist = flst_bornrescurr
      argy = kn_y
      argmasses = kn_masses(1:argnlegb)
      argcmpborn = kn_cmpborn
c could be called with argnlegb -> flst_ibornlength, but it is not necessary
      call compcsimaxfsr_g(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
      kn_csimax = argcsimax
      end

      subroutine compbetaem(betaem,ombetaem)
      implicit none
      real * 8 betaem,ombetaem
      include 'pwhg_flg.h'
      if(flg_mvemquadprec) then
         call compbetaem16(betaem,ombetaem)
      else
         call compbetaem8(betaem,ombetaem)
      endif
      end

      subroutine barradmapmv(n,j,m2,q0,barredk,csi,y,phi,xk,jac)
      implicit none
c parameters
      include 'pwhg_math.h'
      include 'pwhg_flg.h'
      integer n,j
      real * 8 m2,q0,barredk(0:3,n),csi,y,phi,xk(0:3,n+1),jac
      if(flg_mvemquadprec) then
         call barradmapmv16(n,j,m2,q0,barredk,csi,y,phi,xk,jac)
      else
         call barradmapmv8(n,j,m2,q0,barredk,csi,y,phi,xk,jac)
      endif
      end

      subroutine compcsimaxfsr_g(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
      implicit none
      include 'pwhg_flg.h'
      integer argnlegb,argemitter,argreslist(argnlegb)
      real * 8 argy,argmasses(argnlegb),argcmpborn(0:3,argnlegb),argcsimax
      if(flg_mvemquadprec) then
         call compcsimaxfsr_g16(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
      else
         call compcsimaxfsr_g8(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
      endif
      end


      subroutine compbetaem16(betaem,ombetaem)
      implicit none
      real * 8 betaem,ombetaem
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      real * 8 q0,m,m2,pj(0:3)
      real * 16 k0emmax,mrec2,x,qbetaem,qombetaem
      integer j,kres
      real * 8 dotp
      external dotp
      j=kn_emitter
      if(j.gt.2) then
         kres=flst_bornrescurr(j)
      else
         kres=0
      endif
      if(kres.gt.0) then
         call boost2reson(kn_cmpborn(:,kres),1,
     1        kn_cmpborn(:,j),pj)
         q0=sqrt(dotp(kn_cmpborn(:,kres),kn_cmpborn(:,kres)))
      else
         pj=kn_cmpborn(:,j)
         q0=2*kn_cmpborn(0,1)
      endif
      kn_q0=q0
      mrec2=(q0*1.q0-pj(0)*1.q0)**2
     +     -pj(1)**2*1.q0-pj(2)**2*1.q0-pj(3)**2*1.q0
      m=kn_masses(j)
      m2=kn_masses(j)**2
      k0emmax=(q0**2*1.q0-mrec2+m2*1.q0)/(2*q0)
      x=m*1.q0/k0emmax
      if(x.lt.1.q-7) then
         qbetaem=(1.q0 - x/2.q0 - x**2/8.q0 - x**3/16.q0)
     +          *(1.q0 + x/2.q0 - x**2/8.q0 + x**3/16.q0)
         qombetaem=x**2/2.d0 - 3.d0/16.d0*x**3
      else
         qbetaem=sqrt(1.q0-m*1.q0/k0emmax)*sqrt(1.q0+m*1.q0/k0emmax)
         qombetaem=1.q0-qbetaem
      endif
      betaem=qbetaem
      ombetaem=qombetaem
      end


c This routine is as the previous one,
c in case the emitter is massive.
      subroutine barradmapmv16(n,j,mm2,qq0,barredk,csi,y,phi,xk,jac)
      implicit none
c parameters
      include 'pwhg_math.h'
      integer n,j
      real * 8 mm2,qq0,barredk(0:3,n),csi,y,phi,xk(0:3,n+1),jac
C Local variables
      real * 16 m2,q0,q2,mrec2,k0np1,uknp1,ukj,k0j,uk,cpsi,cpsi1,
     1     norm,k0rec,ukrec,ukj0,alpha,
     2     ubkj,bk0j,bk0rec,ubkrec,k0jmax,k0recmax,z,z1,z2,
     3     qa,qb,qc,qq
      real * 8 vec(3),beta,cpsi8,spsi8,cpsi18,spsi18,dk0recmax
      integer i
      real * 8 cosjnp1soft,sinjnp1soft
      common/ccosjnp1soft/cosjnp1soft,sinjnp1soft
      jac=1
c     according to fno2006: by k0 we mean the 0 component in the CM, by
c     uk (underlined k) we mean the modulus of its 3-momentum n and np1
c     in a variable name suggests n and n+1, etc.
      q0=qq0
      m2=mm2
      q2=q0**2
c (5.42) of fnw2006
      k0np1=csi*q0/2
c our reference is the Dalitz phase space d k0jp1 dk0j
      jac=jac*q0/2
      uknp1=k0np1
c compute Mrec^2 (5.45)
      mrec2=(q0*1.q0-barredk(0,j)*1.q0)**2*1.q0
     #     -barredk(1,j)**2*1.q0
     #     -barredk(2,j)**2*1.q0
     #     -barredk(3,j)**2*1.q0
      k0recmax = (q2-m2+mrec2)/(2*q0)
      k0jmax   = (q2+m2-mrec2)/(2*q0)

      dk0recmax= k0recmax*1.d0
c solutions of the quadratic equation
c      z1=(k0recmax+sqrt(k0recmax**2-mrec2))/q0
c      z2=(k0recmax-sqrt(k0recmax**2-mrec2))/q0
      qa= q0/2.q0
      qb= -k0recmax
      qc= mrec2/2.q0/q0
      qq= -0.5q0*(qb-dsign(1.d0,dk0recmax)*sqrt(k0recmax**2-mrec2))
      z1= qq/qa
      z2= qc/qq
      z1=(k0recmax+sqrt(k0recmax**2-mrec2))/q0
      z2=(k0recmax-sqrt(k0recmax**2-mrec2))/q0
      z=z2-(z2-z1)*(1+y)/2
      jac=jac*(z1-z2)/2
      k0j=k0jmax-k0np1*z
      jac=jac*k0np1
      ukj=sqrt(k0j**2-m2)
      k0rec=q0-k0np1-k0j
      ukrec=sqrt(k0rec**2-mrec2)
      uk=ukrec
c compute cos psi (angle between knp1 and k)
      cpsi=(uk**2+uknp1**2-ukj**2)/(2*uk*uknp1)
      cpsi8=cpsi
      spsi8=sqrt(abs(1-cpsi**2))
c get the cosine of the angle between kj and k
      cpsi1=(uk**2+ukj**2-uknp1**2)/(2*uk*ukj)
      cpsi18=cpsi1
      spsi18 = sqrt(abs(1-cpsi1**2))
c Set k_j and k_n+1 parallel to kbar_j
      ubkj=sqrt(barredk(1,j)**2+barredk(2,j)**2+barredk(3,j)**2)
      bk0j=barredk(0,j)
      do i=0,3
         xk(i,n+1)=uknp1*barredk(i,j)/ubkj
      enddo
      xk(0,n+1)= k0np1
      do i=1,3
         xk(i,j)=ukj*barredk(i,j)/ubkj
      enddo
      xk(0,j)=k0j
c Set up a unit vector orthogonal to kbar_n and to the z axis
      vec(3)=0
      norm=sqrt(barredk(1,j)**2+barredk(2,j)**2)
      vec(1)=barredk(2,j)/norm
      vec(2)=-barredk(1,j)/norm
c Rotate k_n+1 around vec of an amount psi
      call mrotate(vec,spsi8,cpsi8,xk(1,n+1))
c Rotate k_j around vec of an amount psi1 in opposite direction
      call mrotate(vec,-spsi18,cpsi18,xk(1,j))
c set up a unit vector parallel to kbar_j
      do i=1,3
         vec(i)=barredk(i,j)/ubkj
      enddo
c Rotate k_j and k_n+1 around this vector of an amount phi
      call mrotate(vec,sin(phi),cos(phi),xk(1,n+1))
      call mrotate(vec,sin(phi),cos(phi),xk(1,j))
c find boost of recoil system
      bk0rec=q0-bk0j
      ubkrec=ubkj
      alpha=(k0rec+ukrec)/(bk0rec+ubkrec)
      beta=(1-alpha**2)/(1+alpha**2)
c massless limit is
c     beta=(q2-(k0rec+ukrec)**2)/(q2+(k0rec+ukrec)**2)
c     Boost all other barred k (i.e. 1 to j-1,j+1 to n) along vec with velocity
c     beta in the k direction (same as barred k_j)
      do i=1,3
         vec(i)=barredk(i,j)/ubkj
      enddo
      if(j-1 > 0) call mboost(j-1,vec,beta,barredk(0,1),xk(0,1))
      if(n-j > 0) call mboost(n-j,vec,beta,barredk(0,j+1),xk(0,j+1))
c 
      jac=jac*q0/((2*pi)**3*2*ubkj)
c compute the cosine of the angle between kj and kn+1 IN THE SOFT LIMIT.
c this must replace kn_y when computing the soft limit vector
c since kn_y has a different meaning here
      cpsi=(2*q2*z-q2-mrec2+m2)/(sqrt(k0jmax**2-m2)*q0)/2
      cosjnp1soft=cpsi
      sinjnp1soft=sqrt(1-cpsi**2)
      end


      subroutine compcsimaxfsr_g16(argnlegb,argemitter,argreslist,
     1     argy,argmasses,argcmpborn,argcsimax)
      implicit none
      include 'pwhg_flg.h'
      integer argnlegb,argemitter,argreslist(argnlegb)
      real * 8 argy,argmasses(argnlegb),argcmpborn(0:3,argnlegb),argcsimax
      real * 8 q0,m2,mrec2,k0recmax,knp1max,z1,z2,z,pj(0:3)
      integer j,kres
      real * 8 dotp
      external dotp
      real*16 qa,qb,qc,qq
      real*16 qk0recmax,qmrec2,qz1,qz2,qz,qknp1max,qkn_csimax
      j=argemitter
      kres=argreslist(j)
      if(kres.gt.0) then
         call boost2reson(argcmpborn(:,kres),1,
     1        argcmpborn(:,j),pj)
         q0=sqrt(dotp(argcmpborn(:,kres),argcmpborn(:,kres)))
      else
         pj=argcmpborn(:,j)
         q0=2*argcmpborn(0,1)
      endif
c calculation of mrec2 in quadruple precision 
      qmrec2= (q0*1.q0-pj(0)*1.q0)**2
     +       -        (pj(1)*1.q0)**2
     +       -        (pj(2)*1.q0)**2
     +       -        (pj(3)*1.q0)**2
      mrec2=(q0-pj(0))**2-pj(1)**2-pj(2)**2-pj(3)**2
      m2=argmasses(j)**2
      if(m2.eq.0) then
         argcsimax=1-mrec2/q0**2
      else
c calculation of kn_csimax in double precision
c         k0recmax = (q0**2-m2+mrec2)/(2*q0)
c         z1=(k0recmax+sqrt(k0recmax**2-mrec2))/q0
c         z2=(k0recmax-sqrt(k0recmax**2-mrec2))/q0
c         z=z2-(z2-z1)*(1+kn_y)/2
c         knp1max=-(q0**2*z**2-2*q0*k0recmax*z+mrec2)/(2*q0*z*(1-z))
c         kn_csimax=2*knp1max/q0
c calculation of kn_csimax in quadruple precision
         qk0recmax = (q0**2*1q0-m2*1q0+qmrec2)/(2*q0)
         qa= q0/2.q0
         qb= -qk0recmax
         qc= qmrec2/2.q0/q0
         qq= -0.5q0*(qb-dsign(1.d0,k0recmax)*sqrt(qk0recmax**2-qmrec2))
c         qz1=(qk0recmax+sqrt(qk0recmax**2-qmrec2))/q0
c         qz2=(qk0recmax-sqrt(qk0recmax**2-qmrec2))/q0
         qz1= qq/qa
         qz2= qc/qq
         qz=qz2-(qz2-qz1)*(1+argy)/2
         qknp1max=-(q0**2*qz**2-2*q0*qk0recmax*qz+qmrec2)/(2*q0*qz*(1-qz))
         qkn_csimax=2*qknp1max/q0
      endif
      argcsimax=qkn_csimax
      end

