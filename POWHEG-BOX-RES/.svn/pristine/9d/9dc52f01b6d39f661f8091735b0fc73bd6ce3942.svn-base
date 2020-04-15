      subroutine init_couplings
      implicit none
      include 'pwhg_par.h'
      include 'PhysPars.h'
      real * 8 powheginput
      external powheginput
c Avoid multiple calls to this subroutine. The parameter file is opened
c but never closed ...
      logical called
      data called/.false./
      save called
      if(called) then
         return
      else
         called=.true.
      endif

      if(powheginput("#verytinypars").eq.1) then
         par_isrtinycsi = 1d-12
         par_isrtinyy = 1d-12
         par_fsrtinycsi = 1d-12
         par_fsrtinyy = 1d-12
      endif

      call param_readin()
      call tophys()

*********************************************************
* Print out of all the relevant couplings
* so that they are in a log file
*********************************************************
      write(*,*) '**************************************************'
      write(*,*) '* init_couplings.f writeout'
      write(*,*) '**************************************************'
      write(*,*) 'alpha=', alpha
      write(*,*) 'gfermi=', gfermi
      write(*,*) 'alfas=', alfas
      write(*,*) 'zmass=', zmass
      write(*,*) 'tmass=', tmass
      write(*,*) 'tmass_phsp=', ph_tmass_phsp
      write(*,*) 'lmass=', lmass
      write(*,*) 'cmass=', cmass
      write(*,*) 'bmass=', bmass
      write(*,*) 'lmass=', lmass
      write(*,*) 'wmass=', wmass
      write(*,*) 'zwidth=', zwidth
      write(*,*) 'wwidth=', wwidth
      write(*,*) 'twidth=', twidth
      write(*,*) 'hmass=', hmass
      write(*,*) 'hwidth=', hwidth
      write(*,*) 'Vud=', Vud
      write(*,*) 'Vus=', Vus
      write(*,*) 'Vub=', Vub
      write(*,*) 'Vcd=', Vcd
      write(*,*) 'Vcs=', Vcs
      write(*,*) 'Vcb=', Vcb
      write(*,*) 'Vtd=', Vtd
      write(*,*) 'Vts=', Vts
      write(*,*) 'Vtb=', Vtb
      write(*,*) '**************************************************'
      end

      subroutine param_readin
        implicit none
        include 'PhysPars.h'
        include 'pwhg_st.h'
        include 'pwhg_flg.h'

        double precision, parameter :: Pi = 3.14159265358979323846d0
        integer             :: ewscheme
        real * 8, external  :: powheginput
        complex * 8         :: cwmass2, czmass2


        zmass=powheginput('#zmass')
        if(zmass<0d0) zmass = 91.188d0
        tmass=powheginput('#tmass')
        if(tmass<0d0) tmass=172.5d0
        ph_tmass_phsp=powheginput('#tmass_phsp')
        if(ph_tmass_phsp<0d0) ph_tmass_phsp=tmass
        wmass=powheginput('#wmass')
        if(wmass<0d0) wmass = 80.419d0
        bmass=powheginput('#bmass')
        if(bmass<0d0) bmass = 4.75d0
        hmass=powheginput('#hmass')
        if(hmass<0d0) hmass = 125d0

        zwidth=powheginput('#zwidth')
        if(zwidth<0d0) zwidth=2.441d0
        wwidth=powheginput('#wwidth')
        if(wwidth<0d0) wwidth=2.04807d0
        hwidth=powheginput('#hwidth')
        if(hwidth<0d0) hwidth=0.403d-2


        ewscheme=powheginput('#ewscheme')
        if(ewscheme<1.or.ewscheme>2) ewscheme = 2

        if (ewscheme.eq.1) then  ! MW, MZ, Gmu scheme
          gfermi=powheginput('#gfermi')
          if(gfermi<0d0) gfermi = 1.1658029175194381d-5
          if (powheginput("#complexGFermi").eq.0) then
            alpha=sqrt(2d0)/pi*gfermi*abs(wmass**2*(1d0-(wmass/zmass)**2))
          else
            cwmass2=CMPLX(wmass**2,-wwidth*wmass)
            czmass2=CMPLX(zmass**2,-zwidth*zmass)
            alpha=sqrt(2d0)/pi*gfermi*abs(cwmass2*(1d0-cwmass2/czmass2))
          endif
        else  ! MW, MZ, alpha scheme
          alpha=powheginput('#alpha')
          if(alpha<0d0) alpha = 1/132.50698d0
          if (powheginput("#complexGFermi").eq.0) then
            gfermi=alpha/sqrt(2d0)*pi/(1d0-(wmass/zmass)**2)/wmass**2
          else
            cwmass2=CMPLX(wmass**2,-wwidth*wmass)
            czmass2=CMPLX(zmass**2,-zwidth*zmass)
            gfermi=alpha/sqrt(2d0)*pi/abs((1d0-cwmass2/czmass2)*cwmass2)
          endif
        end if


        twidth=powheginput('#twidth')
        if(twidth<0d0) then
          if (flg_bornonly) then
            twidth=1.4753661509944636d0
        else
            twidth=1.3478781380381690d0
          end if
        end if


        alfas = 0.119d0
        lmass = 0d0
        cmass = 0d0

c     POWHEG CKM matrix
c
c        d     s     b
c    u
c    c
c    t

!       Vud=0.97428d0
!       Vus=0.2253d0
!       Vub=0.00347d0
!       Vcd=0.2252d0
!       Vcs=0.97345d0
!       Vcb=0.0410d0
!       Vtd=0.00862d0
!       Vts=0.0403d0
!       Vtb=0.999152d0

        Vud=1d0
        Vus=1d-10
        Vub=1d-10
        Vcd=1d-10
        Vcs=1d0
        Vcb=1d-10
        Vtd=1d-10
        Vts=1d-10
        Vtb=1d0

      end subroutine param_readin


      subroutine tophys
        implicit none
        include 'PhysPars.h'
        include 'pwhg_math.h'
        include 'pwhg_physpar.h'
        real * 8 e_em,g_weak
        real * 8 powheginput
        external powheginput
        integer j
        real * 8 tmass_phsp

        ph_alphaem=alpha
        ph_gfermi=gfermi

        ph_Zmass = zmass
        ph_Wmass = wmass
        ph_Hmass = hmass
        ph_tmass = tmass
        ph_bmass = bmass

        ph_Zwidth = zwidth
        ph_Wwidth = wwidth
        ph_Hwidth = hwidth
        ph_twidth = twidth

        ph_CKM(1,1)=Vud
        ph_CKM(1,2)=Vus
        ph_CKM(1,3)=Vub
        ph_CKM(2,1)=Vcd
        ph_CKM(2,2)=Vcs
        ph_CKM(2,3)=Vcb
        ph_CKM(3,1)=Vtd
        ph_CKM(3,2)=Vts
        ph_CKM(3,3)=Vtb

c set up masses and widths for resonance damping factors
        physpar_pdgmasses(24) = ph_Wmass
        physpar_pdgmasses(23) = ph_Zmass
        physpar_pdgmasses(5) = ph_bmass
        physpar_pdgmasses(6) = ph_tmass
        physpar_pdgmasses(22) = 0
        physpar_pdgwidths(24) = ph_Wwidth
        physpar_pdgwidths(23) = ph_Zwidth
        physpar_pdgwidths(6) = ph_twidth
        physpar_pdgwidths(22) = 0

        do j=1,physpar_npdg
           physpar_pdgmasses(-j) = physpar_pdgmasses(j)
           physpar_pdgwidths(-j) = physpar_pdgwidths(j)
        enddo

        physpar_phspmasses = physpar_pdgmasses
        physpar_phspwidths = physpar_pdgwidths

        physpar_phspmasses(6) = ph_tmass_phsp
        physpar_phspmasses(-6) = ph_tmass_phsp

      end subroutine tophys


