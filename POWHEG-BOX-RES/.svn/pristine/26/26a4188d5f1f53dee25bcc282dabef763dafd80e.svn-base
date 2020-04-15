c     Setup to test the integrator and the mintwrapper routine.
c     In order to compile it, copy it to a subprocess (any) directory, together
c     with the fake btilde.f file. Setup the Makefile so that the pwhg_init.f
c     file is replaced by the present file, than make.
c     So, you have then a pwhg_main, with the pwhg_main.f and btilde.f files
c     replaced by the current ones. The following main tests independently mint
c     and the mintwrapper, depending upon the domint flag value.

      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer, parameter :: nintervals=50,ndimmax=ndiminteg
      integer ncall,imode
      logical doregrid
      integer, parameter :: nind=2,ndim=1
      integer ind
      real * 8 wind(nind+1)
      integer indhits(nind)
      real * 8 accind(nind),yindmax(nind),yindmaxrat(nind)
      real * 8 xgrid(0:nintervals,ndim),xint,ymax(nintervals,ndim),
     1  ymaxrat(nintervals,ndim),ans,xerr
      real * 8 x(ndimmax),vol
      real * 8 xacc(0:nintervals,ndim)
      real * 8 xmmm(nintervals,ndim),xindmmm(nind)
      integer icell(ndimmax),ncell(ndimmax)
      integer ifold(ndimmax),kfold(ndimmax)
      integer nhits(1:nintervals,ndimmax)
      integer itmx
      integer kint,kdim,j,mcalls,icalls
      integer fun,btilde
      external fun,btilde

      real * 8 sigma, sigma2
      integer isigma
      common/gencommon/sigma,sigma2,isigma
      real * 8 xsigma,xsigma2,xisigma
      logical, parameter :: domint=.false.
      
      if(domint) then
      ncall = 10000000
      itmx=5
      imode=0
      ifold=1
      do kdim=1,ndim
         do kint=0,nintervals
            xgrid(kint,kdim)=dble(kint)/nintervals
         enddo
      enddo

      do j=1,nind
         wind(j) = dble(j-1) / nind
      enddo
      wind(nind+1) = 1


      
      call mint(fun,ndim,ncall,itmx,ifold,imode,doregrid,
     1     nind,wind,accind,indhits,yindmax,yindmaxrat,
     2     xgrid,xint,xacc,nhits,ymax,ymaxrat,ans,xerr)

      imode=1
      call mint(fun,ndim,ncall,itmx,ifold,imode,doregrid,
     1     nind,wind,accind,indhits,yindmax,yindmaxrat,
     2     xgrid,xint,xacc,nhits,ymax,ymaxrat,ans,xerr)

      write(*,*) ans,xerr

      imode=0
      call gen(fun,ndim,xgrid,ymax,ymaxrat,nind,wind,yindmax,yindmaxrat,
     1     xmmm,xindmmm,ifold,imode,mcalls,icalls,x,ind)

      imode=1
      xsigma=0
      xsigma2=0
      xisigma=0
      do j=1,ncall
         call gen(fun,ndim,xgrid,ymax,ymaxrat,nind,wind,yindmax,yindmaxrat,
     1        xmmm,xindmmm,ifold,imode,mcalls,icalls,x,ind)
         xsigma = xsigma + sigma
         xsigma2= xsigma2+ sigma2
         xisigma = xisigma + isigma
      enddo


      call write_counters
      write(*,*) xsigma/xisigma,sqrt(((xsigma2/xisigma)-(xsigma/xisigma)**2)/
     3          xisigma)


      else

      flst_nborn = 2
      flst_nbornresgroup = 2
      call mintwrapper('btilde',0,.true.,11)
      call mintwrapper('btilde',1,.false.,11)

      call genwrapper('btilde',0,mcalls,icalls,x,ind)
      do j=1,1000000
         call genwrapper('btilde',1,mcalls,icalls,x,ind)
      enddo
      call write_counters

      endif
      
      end


      
      function fun(ind,x,vol,ifirst,imode,vfun,vfun0)
      implicit none
      integer fun,ind,ifirst,imode
      real * 8 x,vol,vfun,vfun0
      fun = 1
      if(ind == 1) then
         vfun=x**2 * vol
      elseif(ind == 2) then
         vfun=x**3 * vol
      endif
      end
      
