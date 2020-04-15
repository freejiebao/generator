      subroutine born_phsp(xborn)
      implicit none
      real * 8 xborn(*)
      real * 8 powheginput
      procedure() :: powheginput
      logical, save :: ini=.true.
      integer, save :: whichphsp

      call born_phsp1(xborn)

      end

      

      subroutine born_phsp1(xborn)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      include 'pwhg_flst.h'
      include 'pwhg_physpar.h'
      include 'PhysPars.h'
      real * 8 xborn(*)
      integer iborn,j
!     real * 8 p(0:3,5),cmp(0:3,5),masses(5)
      real * 8 p(0:3,nlegborn),cmp(0:3,nlegborn),masses(nlegborn)
      
      
      
      
      do iborn=1,flst_nborn
         if(flst_bornresgroup(iborn).eq.flst_ibornresgroup) exit
      enddo
      
      flst_ibornlength = flst_bornlength(iborn)
      flst_ireallength = flst_ibornlength + 1
      
      do j=1,flst_ibornlength
         kn_masses(j) = physpar_phspmasses(flst_born(j,iborn))
      enddo
      
!     write(*,*) "input psp", xborn(ndiminteg),flst_ibornlength,flst_born(:,iborn)
      
      call genphasespace(xborn,flst_ibornlength,flst_born(:,iborn),
     1     flst_bornres(:,iborn),kn_beams,kn_jacborn,
     1     kn_xb1,kn_xb2,kn_sborn,kn_cmpborn,kn_pborn)
      
!     write(*,*) "output psp", kn_cmpborn
      
      kn_minmass = 1d-6  
      
      
      end
      


      subroutine born_suppression(fact)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      logical ini
      data ini/.true./
      real * 8 fact,pt
      real * 8 powheginput
      external powheginput
      if (ini) then
         pt = powheginput("#ptsupp")         
         if(pt.gt.0) then
            write(*,*) ' ******** WARNING: ptsupp is deprecated'
            write(*,*) ' ******** Replace it with bornsuppfact'
         else
            pt = powheginput("#bornsuppfact")
         endif
         if(pt.ge.0) then
            write(*,*) '**************************'
            write(*,*) 'No Born suppression factor'
            write(*,*) '**************************'
         endif
         ini=.false.
      endif
      fact=1d0
      end


      subroutine set_fac_ren_scales(muf,mur)
      use recola
      implicit none
      include 'PhysPars.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_em.h'
      include 'mathx.h'
      real * 8 muf,mur
      logical ini
      data ini/.true./
      real *8 muref
      real *8 dotp
      external dotp
      logical runningscales
      save runningscales
      real * 8 pt2
      real * 8 powheginput
      external powheginput
      real*8 ptmp(0:3,nlegborn),ptj1,ptj2
      integer nn,i1
      if(ini) then
         if(powheginput('#runningscale').ge.1) then
            runningscales=.true.
         else
            runningscales=.false.
         endif
      endif
      if (runningscales) then
         if (ini) then
            write(*,*) '*************************************'
            write(*,*) '    Factorization and renormalization '
            if (powheginput('#runningscale').eq.1) then
               write(*,*) '  scales set to sqrt(ptj1*ptj2) virtuality '
            else 
               write(*,*) "runningscale value not allowed"
               call exit(1)
            endif
            write(*,*) '*************************************'
            ini=.false.
         endif
c     to be checked
         nn=0
         do i1=1,nlegborn
            if(sqrt(abs(dotp(kn_cmpborn(0:3,i1),
     +           kn_cmpborn(0:3,i1)))).lt.1d-3) then ! skip resonances
               nn=nn+1
               ptmp(0:3,nn)=kn_cmpborn(0:3,i1)
            endif
         enddo
c     the first 8 should be the true FS momenta
         ptj1=sqrt(ptmp(1,7)**2+ptmp(1,7)**2)
         ptj2=sqrt(ptmp(1,8)**2+ptmp(1,8)**2)
         muref=sqrt(ptj1*ptj2)

         call set_mu_ir_rcl (muref)
      else
         if (ini) then
            write(*,*) '*************************************'
            write(*,*) '    Factorization and renormalization '
            write(*,*) '    scales set to the W mass '
            write(*,*) '*************************************'
            ini=.false.
         endif
         muref=ph_Wmass
      endif


      
      if(muref.lt.1) muref = 1
      muf=muref
      mur=muref
      mudim2=em_muren2
      end

CC regular_suppression and global_suppression subroutines
CC taken from Born_phsp.f in t-mg 
ccc-mauro-mod IT HAS TO BE A DUMMY ROUTINE !!!
      subroutine regular_suppression(fact)
      implicit none
      real*8 fact

      call rmn_suppression(fact)

      end

      subroutine rmn_suppression(fact)
      implicit none
      real*8 fact

      fact = 1.d0
      end

      subroutine global_suppression(c,fact)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      character * 1 c
      real * 8 fact
      integer if1,if2,ib
      real * 8 wmass2,yb,yw,momsq03,ptb2
      real * 8 powheginput
      procedure() :: momsq03
      procedure() :: powheginput
      logical ini,dosuppress
      data ini/.true./
      save ini,dosuppress
      if(ini) then
         dosuppress = powheginput("#globalsuppression").eq.1
         if(dosuppress) then
            write(*,*) ' performing global suppression'
         endif
         ini = .false.
      endif

      if(dosuppress.or.c == 'g') then
ccc-mauro-mod
         write(*,*)'entered in global_suppression'
         write(*,*)'NOT YET DEFINET FOR W prod -> stop'
         stop
ccc-mauro-mod
         if(c.eq.'r'.or.c == 'g') then
            if1 = flst_ireallength-2
            if2 = flst_ireallength-3
            ib = flst_ireallength-4
            ptb2 = kn_cmpreal(1,ib)**2 + kn_cmpreal(2,ib)**2
            wmass2 = momsq03(kn_cmpreal(:,if1)+kn_cmpreal(:,if2))
            call getrapidity(kn_cmpreal(:,if1)+kn_cmpreal(:,if2),yw)
            call getrapidity(kn_cmpreal(:,ib),yb)
         elseif(c.eq.'b') then
            if1 = flst_ibornlength-1
            if2 = flst_ibornlength-2
            ib = flst_ibornlength-3
            ptb2 = kn_cmpborn(1,ib)**2 + kn_cmpborn(2,ib)**2
            wmass2 = momsq03(kn_cmpborn(:,if1)+kn_cmpborn(:,if2))
            call getrapidity(kn_cmpborn(:,if1)+kn_cmpborn(:,if2),yw)
            call getrapidity(kn_cmpborn(:,ib),yb)
         else
            write(*,*) ' global_suppression: mode '//c//' not known'
            write(*,*) ' exiting ...'
            call exit(-1)
         endif
c         fact = (wmass2/(wmass2+40d0**2))**3
c     1        * 20d0/(exp((yb-yw)**2)+20d0)
         fact = ptb2/(ptb2+20)
      else
         fact = 1
      endif

      contains
      subroutine getrapidity(p,y)
      implicit none
      real * 8 p(0:3),y
      real *8 tiny
      parameter (tiny=1.d-8)
c     !: protect for small p(0)-p(3) values
      if(dabs(p(0)-p(3)).lt.tiny) then
         y=sign(1.d0,p(3))*1.d8
      else
         y=0.5d0*log((p(0)+p(3))/(p(0)-p(3)))
      endif
      end subroutine

      end


      subroutine exchange_momenta(p1,p2)
      implicit none
      real * 8 p1(0:3),p2(0:3)
      real * 8 tmp(0:3)
      integer mu
      do mu=0,3
         tmp(mu) = p1(mu)
         p1(mu) = p2(mu)
         p2(mu) = tmp(mu)
      enddo
      end

      
