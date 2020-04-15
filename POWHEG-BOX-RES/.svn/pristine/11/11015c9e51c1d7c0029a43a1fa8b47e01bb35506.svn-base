      subroutine fullrwgt(weight)
c This subroutines reweights also the R/B exp[-int R/B] term in the
c Sudakov form factor.
c It needs to now the pdf's used in the original .lhe
c file. These are provided in a powheg.input "pdforig" entry.
c it computes all reweighting factors needed to update the R/B
c and Sudakov form factor (the last one in an approximate way).
      implicit none
      real * 8 weight
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_flg.h'
      include 'pwhg_st.h'
      include 'pwhg_pdf.h'
      include 'LesHouches.h'
c These are needed to call generipdfpar.
      integer iord,ih,iret
      real * 8 lam5l
      character * 2 scheme
c
      real * 8 mu2
      integer fl1b,fl2b,fl1r,fl2r
      real * 8 pdf(-pdf_nparton:pdf_nparton)
      real * 8 lumorig,lum,as,asorig,exponent,exponentorig,
     1         lumbornorig,lumborn,lumreal,lumrealorig,q2l,
     2         save_st_lambda5MSB,save_st_mufact2,x1r,x2r,fact
      real * 8 powheginput,dotp
      integer npdforig,npdf
      logical ini
      data ini/.true./
      integer mode
      save ini,npdforig,npdf,mode
      logical pwhg_isfinite
      external pwhg_isfinite

c These variables are the only ones accessed by the contained subroutines
      double precision mm,mm2,ym,ptm,q,ptm2,q2,mtm,mtm2,
     1     logtaumin,logtaumax,taumin,taumax,taubmin
      integer ngauss
      parameter (ngauss=16)
      double precision xgauss(ngauss),wgauss(ngauss)
      double precision shat,z,em,kmom,aslim,ycmmin,ycmmax,
     1  alphads

      double precision lam5,q2low,q2high
c end variables accessed by the contained subroutines

c two possibilities:
c A) HERWIG style Sudakov
c Radiation factor = Real(kt2)/Born(kt2) * Lumborn(kt2)/Lumborn(q2l) * Delta_Herwig
c The correction factor is
c alpha(kt2)/alpha_old(kt2) * (Lumreal(kt2)/Lumrealold(kt2))/(Lumborn(kt2)/Lumborn_old(kt2))
c Times (Lumborn(kt2)/Lumborn(q2l))/(Lumborn_old(kt2)/Lumborn_old(q2l)) Delta_Herwig/Delta_Herwig_old
c Equals to
c alpha(kt2)/alpha_old(kt2) * (Lumreal(kt2)/Lumreal_old(kt2)) Lumborn_old(q2l)/Lumborn(q2l)
c times Delta_Herwig/Delta_Herwig_old;
c B) Sjostrand style Sudakov
c Radiation factor = Real(kt2)/Born(kt2) * Delta_Sjostrand
c Correction factor:
c alpha(kt2)/alpha_old(kt2) * (Lumreal(kt2)/Lumreal_old(kt2))/(Lumborn(kt2)/Lumborn_old(kt2))
c Times Delta_Sjostrand/Delta_Sjostrand_old
c Equals to
c alpha(kt2)/alpha_old(kt2) * (Lumreal(kt2)/Lumreal_old(kt2)) * (Lumborn_old(kt2)/Lumborn(kt2))
c 

      if(ini) then
         mode = powheginput("#fullrwgtmode")
         if(mode.lt.0) mode = 4
         if(pdf_ndns1.ne.pdf_ndns2) then
            write(*,*) " fullpdfrwgt now works only for identical pdf's"
            write(*,*) " for the two beams ! exiting ..."
            call exit(-1)
         endif
         ini = .false.
      endif
      npdf = pdf_ndns1
      npdforig = pdf_ndns1lhe

      x1r = pup(4,1)/ebmup(1)
      x2r = pup(4,2)/ebmup(2)

      fl1b = flst_born(1,rad_ubornsubp)
      fl2b = flst_born(2,rad_ubornsubp)

      fl1r = idup(1)
      if(fl1r.eq.21) fl1r = 0
      fl2r = idup(2)
      if(fl2r.eq.21) fl2r = 0

c If it has Born kinematics, it is already reweighted by the standard POWHEG reweighter.
c However, it must be reweighted with the Sudakov form factor for not emitting below the cutoff scale
c Check that it has Born kinematics by requiring the same flavours and same x_1/2 for real and born.
c Reals are written to the LH file with a precision of 1d-9
      if(fl1r .eq. fl1b .and. fl2r .eq. fl2b .and.
     1     abs((kn_xb1-x1r)/x1r) .lt. 2d-9   .and. 
     2     abs((kn_xb2-x2r)/x2r) .lt. 2d-9)   then
         if(mode.eq.4) then
c we must compute the Sudakov form factor at the current scale with current pdf's
            mu2=rad_ptsqmin
            save_st_lambda5MSB = st_lambda5MSB
            save_st_mufact2 = st_mufact2
c     Sudakov, Sjostrand kind, exact phase space
            call sudakovxxx(mu2,exponent)
c     Compute the same for original pdf's
            pdf_ndns1 = npdforig
            pdf_ndns2 = npdforig
            call genericpdfpar(npdforig,ih,lam5l,scheme,iord,iret)
            st_lambda5MSB = lam5l
c     Sudakov, Sjostrand kind, exact phase space
            call sudakovxxx(mu2,exponentorig)
            fact = exp(exponent-exponentorig)
            if(pwhg_isfinite(fact)) then
               weight = weight * fact
            endif
c Set parameters affecting pdf's as in the current settings
            st_lambda5MSB = save_st_lambda5MSB
            st_mufact2 = save_st_mufact2
            pdf_ndns1 = npdf
            pdf_ndns2 = npdf
            call genericpdfpar(npdf,ih,lam5l,scheme,iord,iret)
         endif
         return
      endif
c Set scale equal to boson pt; take real kinematics from LH event;
c the kn_*real variables are undefined during reweighting.
      mu2 = pup(1,nup)**2 + pup(2,nup)**2
      q2l = dotp(kn_cmpborn(:,3)+kn_cmpborn(:,4),
     1          kn_cmpborn(:,3)+kn_cmpborn(:,4))

      save_st_mufact2 = st_mufact2
c Compute Born lum for current pdf's

      call genericpdfpar(npdf,ih,lam5l,scheme,iord,iret)

      if(mode.ne.3.and.mode.ne.4) then
c in these mode, it is assumed that HERWIG style Sudakovs is a good approximation
         st_mufact2 = max(pdf_q2min,q2l)
      else
c Sjostrand style Sudakov; must supply the ratio of born luminosities computed at kt2
         st_mufact2 = max(pdf_q2min,mu2)
         call pdfcall(1,kn_xb1,pdf)
         lumborn = pdf(fl1b)
         call pdfcall(2,kn_xb2,pdf)
         lumborn = lumborn * pdf(fl2b)
      endif

c Compute Real lum for current pdf's

      st_mufact2 =  max(pdf_q2min,mu2)
      call pdfcall(1,x1r,pdf)
      lumreal = pdf(fl1r)
      call pdfcall(2,x2r,pdf)
      lumreal = lumreal * pdf(fl2r)

c Get as to compute radiation for current pdf's
      as = mcalphas(mu2,lam5l)
      save_st_lambda5MSB = st_lambda5MSB
      st_lambda5MSB = lam5l
      if(q2l.gt.mu2) then
         if(mode.eq.1) then
c Sudakov MiNLO style (HERWIG kind)
            call sudakov_exponent(mu2,q2l,q2l,exponent,.true.,
     1                            2,.false.)
         elseif(mode.eq.2) then
c Sudakov sikmplified (HERWIG kind)
            exponent = simplesudakov(lam5l,mu2,q2l)
         elseif(mode.eq.3) then
c Sudakov sikmplified (Sjostrand kind)
            exponent =
     1           simplesudakovx(lam5l,mu2,q2l,kn_xb1,kn_xb2,fl1b,fl2b)
         endif
      else
         exponent = 0
      endif
      if(mode.eq.4) then
c Sudakov, Sjostrand kind, exact phase space
         call sudakovxxx(mu2,exponent)
         exponent = exponent/2
      endif
c Compute the same for original pdf's
      pdf_ndns1 = npdforig
      pdf_ndns2 = npdforig
      call genericpdfpar(npdforig,ih,lam5l,scheme,iord,iret)

      if(mode.ne.3.and.mode.ne.4) then
         st_mufact2 = max(pdf_q2min,q2l)
         call pdfcall(1,kn_xb1,pdf)
         lumbornorig = pdf(fl1b)
         call pdfcall(2,kn_xb2,pdf)
         lumbornorig = lumbornorig * pdf(fl2b)
      else
c Sjostrand style Sudakov; must supply the ratio of luminosities computed at kt2
         st_mufact2 = max(pdf_q2min,mu2)
         call pdfcall(1,kn_xb1,pdf)
         lumbornorig = pdf(fl1b)
         call pdfcall(2,kn_xb2,pdf)
         lumbornorig = lumbornorig * pdf(fl2b)
      endif

      st_mufact2 = max(pdf_q2min,mu2)
      call pdfcall(1,x1r,pdf)
      lumrealorig = pdf(fl1r)
      call pdfcall(2,x2r,pdf)
      lumrealorig = lumrealorig * pdf(fl2r)

c Get as to compute radiation for original pdf's
      asorig = mcalphas(mu2,lam5l)
      st_lambda5MSB = lam5l

      if(q2l.gt.mu2) then
         if(mode.eq.1) then
c Sudakov MiNLO style (HERWIG kind)
            call sudakov_exponent(mu2,q2l,q2l,exponentorig,.true.,
     1           2,.false.)
         elseif(mode.eq.2) then
c Sudakov sikmplified (HERWIG kind)
            exponentorig = simplesudakov(lam5l,mu2,q2l)
         elseif(mode.eq.3) then
c Sudakov sikmplified (Sjostrand kind)
            exponentorig =
     1           simplesudakovx(lam5l,mu2,q2l,kn_xb1,kn_xb2,fl1b,fl2b)
         endif
      else
         exponentorig = 0
      endif
      if(mode.eq.4) then
c Sudakov, Sjostrand kind, exact phase space
         call sudakovxxx(mu2,exponentorig)
         exponentorig = exponentorig/2
      endif
c Set parameters affecting pdf's as in the current settings
      st_lambda5MSB = save_st_lambda5MSB
      st_mufact2 = save_st_mufact2
      pdf_ndns1 = npdf
      pdf_ndns2 = npdf
      call genericpdfpar(npdf,ih,lam5l,scheme,iord,iret)
c Compute reweighting factor:
      
      fact =   as/asorig                               ! as for radiation updated
      if(mode.ne.3.and.mode.ne.4) then
         fact = fact * lumbornorig/lumborn             ! pdf ratio arising
                                                       ! from Sudakov form factors
      else
         fact = fact * lumbornorig/lumborn             ! Factor due to R/B in radiation
                                                       ! this time evaluated at kt2
      endif

      fact = fact * lumreal/lumrealorig                ! new pdf's in radiation
      fact = fact * exp(2*(exponent-exponentorig))     ! Sudakov form factors

      if(pwhg_isfinite(fact)) then
         weight = weight * fact
      endif

      contains


      double precision function
     1     simplesudakovx(lam5,q2low,q2high,x1,x2,fl1,fl2)
      implicit none
      double precision lam5,q2low,q2high,x1,x2
      integer fl1,fl2
      integer ngauss
      parameter (ngauss=16)
      double precision xgauss(ngauss),wgauss(ngauss),xxx(2)
      integer j,k
c      double precision simplesudakovx0,
      double precision res
      logical ini
      data ini/.true./
      save ini,xgauss,wgauss
c Setup gaussian weights and points
      if(ini) then
         call dgset(0d0,1d0,ngauss,xgauss,wgauss)
         ini = .false.
      endif
      res = 0
      do j=1,ngauss
         xxx(1) = xgauss(j)
         do k=1,ngauss
            xxx(2) = xgauss(k)
            res = res + wgauss(j)*wgauss(k)*
     1           simplesudakovx0(lam5,q2low,q2high,x1,x2,fl1,fl2,xxx)
         enddo
      enddo
      simplesudakovx = res
      end function simplesudakovx

      double precision function
     1     simplesudakovx0(lam5,q2low,q2high,x1,x2,fl1,fl2,xxx)
      implicit none
      double precision lam5,q2low,q2high,x1,x2,xxx(2)
      integer fl1,fl2,fl,j
      include 'pwhg_math.h'
      include 'pwhg_pdf.h'
      include 'pwhg_st.h'
      real * 8 kt2,x,xjac,lq2,as,eta,xi,ximax,ximin,y,ymax,z,xx
      real * 8 fxr(-pdf_nparton:pdf_nparton),
     1         fxb(-pdf_nparton:pdf_nparton)
c      real * 8 mcalphas
c      external mcalphas
      xjac = 1
      lq2 = log(q2high/q2low)
      kt2 = exp(xxx(1)*lq2)*q2low
      xjac = xjac * kt2 * lq2
      eta = 4*kt2/q2high
      simplesudakovx0 = 0
      do j=1,2
         if(j.eq.1) then
            xx = x1
            fl = fl1
         else
            xx = x2
            fl = fl2
         endif
         if((1-xx)**2.gt.eta) then
c define y=sqrt((1-x)^2-eta);
c y d y = (1-x) dx, dx = y dy /(1-x)
c y goes from 0 to sqrt((1-x1)**2-eta). Needs importance sampling
c near the upper bound, and also near the lower bound if x1 is small.
c Take xi = log((y+eta)/(1-y)) as sampling variable xi
            ymax = sqrt((1-xx)**2-eta)
            ximax = log((ymax+eta)/(1-ymax))
            ximin = log(eta)
            xi = (ximax-ximin)*xxx(2) + ximin
            xjac = xjac*(ximax-ximin)
            z=exp(xi)
            xjac = xjac * z
            y = (z-eta)/(1+z)
            xjac = xjac * (1+eta) / (1+z)**2
            x = 1 - sqrt( y**2 + eta )
            xjac = xjac * y/(1-x)
            st_mufact2 = max(pdf_q2min,kt2)
            as =  mcalphas(kt2,lam5)
            call pdfcall(1,xx,fxb)
            call pdfcall(1,xx/x,fxr)
            simplesudakovx0 = simplesudakovx0 + (
     1           ( cf * (1+x**2)/(1-x) * fxr(fl) +
     2           tf * (x**2+(1-x)**2) * fxr(0)  )/fxb(fl)   )
     3           *  as/(2*pi) /kt2/x *xjac
     4           / sqrt(1-eta/(1-x)**2)
         endif
      enddo
c we divide by two simply because we multiply by 2 in the main program
      simplesudakovx0 = - simplesudakovx0 / 2
      end function simplesudakovx0

      double precision function simplesudakov(lam50,q2low0,q2high0)
      implicit none
      double precision lam50,q2low0,q2high0
      double precision dgauss

      lam5 = lam50
      q2low = q2low0
      q2high = q2high0
      simplesudakov = dgauss(simplesudakov0,0d0,1d0,1d-4)
      end function simplesudakov

      double precision function simplesudakov0(x)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_math.h'
      include 'pwhg_st.h'
      include 'pwhg_rad.h'
      double precision x
      double precision dgauss      
      real * 8 as,lqlow,l,q2
      integer nf
      lqlow = log(q2high/q2low)
      l = x*lqlow
      q2 = q2low*exp(l)
      as = mcalphas(q2,lam5)
c Sudakov exponent is (for each leg)
c              d q2   C_f       [      Q2       ]
c      \int   -----  ---- as(q) [ log --- + B1  ],  B1 = -3/2 = -1.5
c               q2   2 pi       [      q2       ]

c lqlow is the jacobian
      simplesudakov0 = - cf/(2*pi)*as*(l-1.5d0) * lqlow

      end function simplesudakov0

      

      double precision function mcalphas(q2,lam5)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_math.h'
      include 'pwhg_rad.h'
      include 'pwhg_st.h'
      real * 8 q2
      real * 8 lam5
      integer nf
      real * 8 as,pwhg_alphas
      external pwhg_alphas
      if(q2.lt.rad_charmthr2) then
         nf=3
      elseif(st_muren2.lt.rad_bottomthr2) then
         nf=4
      else
         nf=5
      endif
      as = pwhg_alphas(q2,lam5,-1)
      as = as * (1+as/(2*pi)*((67d0/18-pi**2/6)*ca-5d0/9*nf))
      mcalphas = as
      end function mcalphas

      
      subroutine sudakovxxx(kt2max,result)
      implicit none
      real * 8 result,kt2max
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      include 'pwhg_st.h'
      include 'pwhg_pdf.h'
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton)
      double precision deltasud,tau0,tau1,eta,pm(0:3)
      real * 8 dotp
      logical ini
      data ini/.true./
      save ini
c Setup gaussian weights and points
      if(ini) then
         call dgset(0d0,1d0,ngauss,xgauss,wgauss)
         ini = .false.
      endif
c the vector meson rapidity and virtuality is the same in the Born and Real kinematics
      pm = kn_pborn(:,3)+kn_pborn(:,4)
      mm2 = dotp(pm,pm)
      mm=sqrt(mm2)
      ym = 0.5d0*log((pm(0)+pm(3))/(pm(0)-pm(3)))
      ptm2 = kt2max
      ptm = sqrt(kt2max)
      q2 = kn_sbeams
      q  = sqrt(q2)
      taubmin=mm2/q2
      mtm2 = mm2+ptm2
      mtm = sqrt(mtm2)
      eta=exp(-2*abs(ym))
      tau0 = (ptm+mtm)**2/q2
      tau1 = ((eta*q2-mm2)*sqrt(eta*q2*mtm2)+eta*q2*ptm2)
     1     /(q2*(eta*q2-mtm2))
      if(tau0.lt.eta) then
         if(tau1.lt.eta) then
            taumin=tau0
            taumax=1
            logtaumin = log(tau0)
            logtaumax = 0
         else
            write(*,*) 'bmass_in_minlo: tau0<eta and tau1>eta !!!'
            write(*,*) "can't be, exiting ..."
            call exit(-1)
         endif
      else
         if(tau1.lt.tau0) then
            write(*,*) 'bmass_in_minlo: tau1<tau0 !!!'
            write(*,*) "can't be, exiting ..."
            call exit(-1)
         endif
         if(tau1.gt.1) then
            write(*,*) 'bmass_in_minlo: tau1>1 !!!'
            write(*,*) "can't be, exiting ..."
            call exit(-1)
         endif
         taumin=tau1
         taumax=1
         logtaumin = log(tau1)
         logtaumax = 0
      endif
C      alphads = st_alpha ! fixed coupling 
      call dointdeltasud(result)

c      call plotdeltasud

      end subroutine sudakovxxx

      function deltasud0(ycm,tau) result(res)
      implicit none
      include 'LesHouches.h'
      include 'pwhg_math.h'
      include 'pwhg_st.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      double precision, intent(in) :: ycm,tau
      double precision res
      double precision kt2,xjac,x1,x2,taub,gg,gq,qg,att,auu,
     1     kl,alphas,x,x1b,x2b,k0
      include 'pwhg_pdf.h'
c sing1 and sing2 will stand for the singlet on the 1 and 2 incoming particles
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton),sing1,sing2
      integer j,fl1r,fl2r

      real * 8 born
      integer  bflav(4)
      real * 8 ppp(0:3,4) ! Partonic COM frame momenta
      real * 8 R_t,R_tb,R_tb_int,R_tb_int_fact,R_tb_int_non_fact
      real * 8 B_t,B_tb,B_t_inf,B_tb_inf
      real * 8 powheginput
      external powheginput
      real * 8 savemfer
      real * 8 approx_result
      integer  saveafer
      logical ini
      data    ini/.true./
      save    ini
      integer approx
      save    approx
c      double precision mcalphas,as
      double precision as

      kl = em * tanh(ym-ycm)
      kt2 = kmom**2-kl**2

      as = mcalphas(kt2,st_lambda5MSB)
c
      xjac = z/(4*pi)*(mm2+kt2)/(mm2*(1+z))
c
      x1 = sqrt(tau)*exp(ycm)
      x2 = sqrt(tau)*exp(-ycm)

c      shat = q2*tau

      x = mm2/shat

      k0 = sqrt(shat)*(1-x)/2
c
C      call checkkin(x1,x2,kt2)

      st_mufact2 = max(kt2,pdf_q2min)
      call pdfcall(1,x1,pdf1)
      call pdfcall(2,x2,pdf2)

c Get underlyinng Born flavours for current event
      fl1r = flst_born(1,rad_ubornsubp)
      fl2r = flst_born(2,rad_ubornsubp)

c the factors (k0-kl)/(2k0) and (k0+kl)/(2k0) select the regions with backward and forward
c emission respectively

      if(fl1r .ne. 0 .and. fl2r .ne. 0) then
         res = - ( cf * (1+x**2)/(1-x) * (pdf1(fl1r)*pdf2(fl2r))
     2     +   tf * (x**2+(1-x)**2) *
     3 (pdf1(0)*pdf2(fl2r)*(k0+kl)+pdf1(fl1r)*pdf2(0)*(k0-kl))/(2*k0))
     4     *  as*(8*pi) /(kt2/(1-x)) 
      elseif(fl1r .eq. 0 .and. fl2r .eq. 0) then
         sing1 = sum(pdf1(-6:-1)) + sum(pdf1(1:6))
         sing2 = sum(pdf2(-6:-1)) + sum(pdf2(1:6))
         res = - ( 2*ca * (x/(1-x)+(1-x)/x+x*(1-x))
     2      * (pdf1(fl1r)*pdf2(fl2r)) +   cf * (1+(1-x)**2)/x *
     3 (sing1*pdf2(fl2r)*(k0+kl)+pdf1(fl1r)*sing2*(k0-kl))/(2*k0) )
     4     *  as*(8*pi) /(kt2/(1-x))
      elseif(fl1r .eq. 0 .and. fl2r .ne. 0) then
         sing1 = sum(pdf1(-6:-1)) + sum(pdf1(1:6))
         res = - (
     1        (2*ca * (x/(1-x)+(1-x)/x+x*(1-x)) * (k0+kl)
     2         + cf * (1+x**2)/(1-x) * (k0-kl))
     3        * (pdf1(fl1r)*pdf2(fl2r))
     4     +  cf * (1+(1-x)**2)/x * sing1*pdf2(fl2r)*(k0+kl)
     5     +  tf * (x**2+(1-x)**2) * pdf1(fl1r)*pdf2(0)*(k0-kl) )/(2*k0)
     6     *  as*(8*pi) /(kt2/(1-x))
      elseif(fl1r .ne. 0 .and. fl2r .eq. 0) then
         sing2 = sum(pdf2(-6:-1)) + sum(pdf2(1:6))
         res = - (
     1        (cf * (1+x**2)/(1-x) * (k0+kl)) +
     2         2*ca * (x/(1-x)+(1-x)/x+x*(1-x)) * (k0-kl) 
     3        * (pdf1(fl1r)*pdf2(fl2r))
     4     +  tf * (x**2+(1-x)**2) * pdf1(0)*pdf2(fl2r)*(k0+kl)
     5     +  cf * (1+(1-x)**2)/x * pdf1(fl1r)*sing2*(k0-kl)    )/(2*k0)
     6     *  as*(8*pi) /(kt2/(1-x))
      endif

c 8 pi as (1-x) shat/(tk uk) according to MNR, = 8 pi as (1-x)/kt2

c
c
c Born pdf
      x1b = mm/q*exp(ym)
      x2b = mm2/q2/x1b
      call pdfcall(1,x1b,pdf1)
      call pdfcall(2,x2b,pdf2)

c divide by 2*pi/q2, that arises from the Born phase space in the denominator
      res = res/(pdf1(fl1r)*pdf2(fl2r)) * xjac /(2*pi/q2)

      end function deltasud0

      function deltasud1(xx) result(res)
      implicit none
c this constructs the kinematics starting from x(1) and (x2),
c and ym, ptm, ptm2 (in phspsudint.h), computes ycm,tau 
c and a jacobian to go from xx(1:2) to ycm,tau
      double precision, intent(in) :: xx(2)
      double precision res
      double precision xjac,tau,llmin,llmax,ll,ycm,zzz
c integration limit
c      tau = exp(xx(1)**2*(logtaumax-logtaumin)+logtaumin)
c      xjac = tau*(logtaumax-logtaumin)*2*xx(1)

      llmin = log(taumin-taubmin)
      llmax = log(taumax-taubmin)
      ll = xx(1)*(llmax-llmin)+llmin
      xjac = (llmax-llmin)
      tau = exp(ll)+taubmin
      xjac = xjac * exp(ll)

c range in ycm
      shat = tau*q2
      z = mm2/shat
      em = mm*(1+z)/(2*sqrt(z))
      kmom = mm*(1-z)/(2*sqrt(z))
      aslim = atanh(sqrt(kmom**2-ptm2)/em)
      ycmmin = max(log(tau)/2,
     1     ym-aslim)
      ycmmax = min(-log(tau)/2,
     1     ym+aslim)
      if(ycmmin.gt.ycmmax) then
         write(*,*) 'deltasud1:  Worry!'
         write(*,*) 'ycmmmin>ycmmax!!'
         call exit(-1)
      endif
      zzz = 6*(xx(2)**2/2-xx(2)**3/3)
      xjac = xjac * 6*xx(2)*(1-xx(2))
      ycm = zzz*(ycmmax-ycmmin)+ycmmin
      xjac = xjac*(ycmmax-ycmmin)
      res = deltasud0(ycm,tau)*xjac
      end function deltasud1

      subroutine dointdeltasud(res)
      implicit none
      real * 8 res
      real * 8 xx(2),random
      integer j,k,ncalls
      parameter (ncalls=100000)
      res = 0
c      do j=1,ncalls
c         xx(1)=random()
c         xx(2)=random()
c         res = res + deltasud1(xx)/ncalls
c      enddo
c      return

      do j = 1,ngauss
         xx(1) = xgauss(j)
         do k = 1,ngauss
            xx(2) = xgauss(k)
            res = res + deltasud1(xx)*wgauss(j)*wgauss(k)
         enddo
      enddo
      end subroutine dointdeltasud
c$$$
c$$$      subroutine plotdeltasud
c$$$      implicit none
c$$$      real * 8 res
c$$$      integer ncalls
c$$$      parameter (ncalls=100000)
c$$$      character * 20 str
c$$$      real * 8 xx(2),random
c$$$      integer j,k
c$$$      logical ini
c$$$      data ini/.true./
c$$$      save ini
c$$$      write(str,'(f4.1,"-",i3)') ym,int(ptm)
c$$$      do j=1,15
c$$$         do k=1,2
c$$$            if(str(j:j).eq.' ') str(j:)=str(j+1:)
c$$$         enddo
c$$$      enddo
c$$$      write(*,*) '!'//str//'!'
c$$$
c$$$      call inihists
c$$$      call bookupeqbins('x1',0.01d0,0d0,1d0)
c$$$      call bookupeqbins('x2',0.01d0,0d0,1d0)
c$$$
c$$$      res = 0
c$$$      do k = 1,ncalls
c$$$         xx(1) = random()
c$$$         xx(2) = random()
c$$$         res = deltasud1(xx)
c$$$         call filld('x1',xx(1),res)
c$$$         call filld('x2',xx(2),res)
c$$$         call pwhgaccumup
c$$$      enddo
c$$$      call pwhgsetout
c$$$      call pwhgtopout("deltasudhists-"//trim(str))
c$$$      end subroutine plotdeltasud
c$$$

      subroutine checkkin(x1,x2,kt2)
      implicit none
      real * 8 x1,x2,kt2,ycm,p,p0,ppar,ycmm,shat_lcl
      if(x1.lt.0.or.x1.gt.1) then
         write(*,*) ' checkkin: x1=',x1
         call exit(-1)
      endif
      if(x2.lt.0.or.x2.gt.1) then
         write(*,*) ' checkkin: x2=',x2
         call exit(-1)
      endif
      if(kt2.lt.0) then
         write(*,*) ' checkkin: kt2=',kt2
         call exit(-1)
      endif
      ycm = 0.5d0*log(x1/x2)
      shat_lcl = q2*x1*x2
      ycmm = ym-ycm
      p0 = (shat_lcl + mm2)/(2*sqrt(shat_lcl))
      p = (shat_lcl - mm2)/(2*sqrt(shat_lcl))
      ppar = p0*tanh(ycmm)
      if(abs(p**2-kt2-ppar**2).gt.1d-6) then
         write(*,*) ' checkkin: kinematics do not check'
         call exit(-1)
      endif
      end subroutine checkkin

      end
      

      subroutine readpowheginputinfo(nlf)
c If any information from the current lhe file is desired, get it here.
c In this case, we set the pdf's used for generating the file, that may
c be needed for reweighting.
      implicit none
      integer nlf
      character * 300 string
      character * 3 whichpdf
      include 'pwhg_pdf.h'
      integer iret,j,ndns1,ndns2,lhans1,lhans2
      call pwhg_io_rewind(nlf)
      do j=1,1000000
         call pwhg_io_read(nlf,string,iret)
         if(iret /= 0) goto 999
         string = adjustl(string)
         if(string(1:5) .eq. 'ndns1') then
            read(string(6:),*) ndns1
         elseif(string(1:5) .eq. 'ndns2') then
            read(string(6:),*) ndns2
         elseif(string(1:6) .eq. 'lhans1') then
            read(string(7:),*) lhans1
         elseif(string(1:6) .eq. 'lhans2') then
            read(string(7:),*) lhans2
         elseif(string(1:12) .eq. 'PDF package:') then
            if(adjustl(string(13:)) .eq. 'lha') then
               pdf_ndns1lhe = lhans1
               pdf_ndns2lhe = lhans1
               whichpdf = 'lha'
            elseif(adjustl(string(13:)) .eq. 'mlm') then
               pdf_ndns1lhe = ndns1
               pdf_ndns2lhe = ndns2
               whichpdf = 'mlm'
            else
               write(*,*) ' readpowheginputinfo: cannot identify'
               write(*,*) ' psf package ',trim(adjustl(string))
               call exit(-1)
            endif
            call pwhg_io_rewind(nlf)
            if(pdf_ndns1lhe .ne. pdf_ndns2lhe) then
               write(*,*)
     1      ' readpowheginputinfo: got two different pdf sets',
     2     ' for the two imcoming hadrons: ',
     3              pdf_ndns1lhe, pdf_ndns2lhe
               write(*,*) ' cannot handle that! exiting ...'
               call exit(-1)
            endif
            write(*,*) 
     1         ' readpowheginputinfo: got ',whichpdf,' set ',
     1         pdf_ndns1lhe,' from input lhe file: '
            return
         endif
      enddo
 999  continue
      write(*,*) ' readpowheginputinfo: something wrong reading'
      call exit(-1)
      end
