      subroutine init_couplings
      use recola
      implicit none
      include 'PhysPars.h'
      include 'pwhg_st.h'
      include 'pwhg_em.h'
      include 'mathx.h'
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      include 'pwhg_physpar.h'
ccc for lprup
      include 'LesHouches.h'
      include 'pwhg_ckm.h'
      integer i1
ccc for lprup
      real * 8 masswindow_low,masswindow_high
      real * 8 powheginput
      external powheginput
      logical verbose
      parameter(verbose=.true.)
      integer i,j
      real*8 mlep2
      complex*16 el2_scheme
      common/leptmass/mlep2
      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)
      real*8 complextmp
      real*8 virtasbornvar
      common/cvirtasbornvar/virtasbornvar
      save /cvirtasbornvar/
c     renormalization scheme
c     0 -> alpha(0)
c     1 -> gmu
      integer scheme
      common/sch/scheme
      real *8 fakevirt
      real *8 lepmass(3)
      common/clepmass/lepmass

      character*5 procisr(7),procfsr(7)
      character*25 proclep ! e+ nu_e mu+ nu_mu

      proclep=''
      procisr=''
      procfsr=''
      
c      only QED corrections
      flg_QEDonly = .true.


      ckm_diag=.true.
      
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccc   INDEPENDENT QUANTITIES       
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccc-mauro-mod
c
      flg_with_em = .true.

      flg_tiny_alphas = .true.


      if(powheginput("#taumass")>0) then
         lepmass(3)=powheginput("#taumass")
      endif


ccc-mauro-mod
      ph_Wmass = powheginput("#Wmass")
      if (ph_Wmass.le.0d0) ph_Wmass  = 80.357973609878d0     
      ph_Wwidth = powheginput("#Wwidth")
      if (ph_Wwidth.le.0d0) ph_Wwidth =  2.0842989982782d0
      
c     EW renormalization scale
!     em_muren2 = 1d0
      em_muren2 = pH_Wmass**2
      

      ph_Zmass = powheginput("#Zmass")
      if (ph_Zmass.le.0d0) ph_Zmass  = 91.1534806191827d0
      ph_Zwidth = powheginput("#Zwidth")
      if (ph_Zwidth.le.0d0) ph_Zwidth =  2.4942663787728d0
      
      ph_Hmass = powheginput("#Hmass")
      if (ph_Hmass.le.0d0) ph_Hmass  = 125.d0

      ph_mTop = powheginput("#Tmass")
      if (ph_mTop.le.0d0) ph_mTop = 173.2d0

      ph_gmu = powheginput("#gmu")
      if (ph_gmu.le.0) ph_gmu = 0.11663787d-4


c     number of light flavors
      st_nlight = 5

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccc mauro :: in POWHEG-BOX-RES 
ccc the order of the calls to init couplingss and init processes is 
ccc reversed !!!!!
c******************************************************
c     Choose the process to be implemented
c******************************************************
c    ID of vector boson produced
      idvecbos=powheginput('idvecbos')
c   decay products of the vector boson
      vdecaymode=powheginput('vdecaymode')
c     idvecbos=24 or -24
c     vdecatmode = 1 (opposite flav), 2 (same flav e), 3 (same flav mu)
      
      if(idvecbos.eq.24) then
         isign=1d0
         
         procisr(1)(:)='s~ d~'
         procisr(2)(:)='s~ u '
         procisr(3)(:)='d~ d~'
         procisr(4)(:)='d~ u '
         procisr(5)(:)='u u  '
         procisr(6)(:)='u c  '
         procisr(7)(:)='u d~ '

         procfsr(1)(:)='c~ u~'
         procfsr(2)(:)='c~ d '
         procfsr(3)(:)='u~ u~'
         procfsr(4)(:)='u~ d '
         procfsr(5)(:)='d d  '
         procfsr(6)(:)='d s  '
         procfsr(7)(:)='c~ s '
         
         Write(*,*) 
         write(*,*) ' POWHEG: W+ W+ production and decay ' 
         if (vdecaymode.eq.1) then
            proclep=' e+ nu_e mu+ nu_mu '
            lepflav=(/-11,12,-13,14/)
            write(*,*) '         to e+ ve mu+ vmu '
         elseif (vdecaymode.eq.2) then
            lepflav=(/-11,12,-11,12/)
            proclep=' e+ nu_e e+ nu_e '
            write(*,*) '         to e+ ve e+ vme '
         elseif (vdecaymode.eq.3) then
            lepflav=(/-13,14,-13,14/)
            proclep=' mu+ nu_mu mu+ nu_mu '
            write(*,*) '         to mu+ vmu mu+ vmu '            
         else
            write(*,*) 'ERROR: The decay mode you selected' /
     $           /' is not allowed '
            call exit(-1)
         endif
      elseif(idvecbos.eq.-24) then

         isign=-1d0
         
         procisr(1)(:)='s d'
         procisr(2)(:)='s u~'
         procisr(3)(:)='d d'
         procisr(4)(:)='d u~'
         procisr(5)(:)='u~ u~'
         procisr(6)(:)='u~ c~'
         procisr(7)(:)='u~ d'

         procfsr(1)(:)='c u'
         procfsr(2)(:)='c d~'
         procfsr(3)(:)='u u'
         procfsr(4)(:)='u d~'
         procfsr(5)(:)='d~ d~'
         procfsr(6)(:)='d~ s~'
         procfsr(7)(:)='c s~'


         
         write(*,*) 
         write(*,*) ' POWHEG: Single W- W- production and decay '
         if (vdecaymode.eq.1) then
            lepflav=(/11,-12,13,-14/)
            proclep=' e- nu_e~ mu- nu_mu~ '
            write(*,*) '         to e- ve~ mu- vmu~ '
         elseif (vdecaymode.eq.2) then
            lepflav=(/11,-12,11,-12/)
            proclep=' e- nu_e~ e- nu_e~ '
            write(*,*) '         to e- ve~ e- vme~ '
         elseif (vdecaymode.eq.3) then
            lepflav=(/13,-14,13,-14/)
            proclep=' mu- nu_mu~ mu- nu_mu~ '
            write(*,*) '         to mu- vmu~ mu- vmu~ '            
         else
            write(*,*) 'ERROR: The decay mode you selected' /
     $           /' is not allowed '
            call exit(-1)
         endif
      else
         write(*,*) 'ERROR: The ID of vector boson you selected' 
     $        //' is not allowed (24: W+ -24: W-)'
         stop
      endif

c     change the LHUPI id of the process according to vector boson id
c     and decay
      lprup(1)=10000+vdecaymode ! 10000+idup of charged decay product of the W
      

c     Set here lepton and quark masses for momentum reshuffle in the LHE event file
      do j=1,st_nlight         
         physpar_mq(j)=0d0
      enddo
      do j=1,3
         physpar_ml(j)=lepmass(j)
      enddo
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
ccc-mauro-mod
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      fakevirt=powheginput("#fakevirt") 
      ph_Hwidth = 4.07d-03 ! Added by Mathieu
      do i1=-physpar_npdg,physpar_npdg
         physpar_pdgmasses(i1)=0d0
         physpar_pdgwidths(i1)=0d0
         physpar_phspmasses(i1)=0d0
         physpar_phspwidths(i1)=0d0
      enddo
      physpar_pdgmasses(-24) = ph_Wmass
      physpar_pdgmasses( 24) = ph_Wmass
      physpar_pdgmasses( 23) = ph_Zmass
      physpar_pdgmasses( 25) = ph_Hmass
      physpar_pdgmasses( -6) = ph_mTop
      physpar_pdgmasses(  6) = ph_mTop
c leptons are just a trial
      physpar_pdgmasses(-11) = physpar_ml(1)
      physpar_pdgmasses(-13) = physpar_ml(2)
      physpar_pdgmasses(-15) = physpar_ml(3)
      physpar_pdgmasses( 11) = physpar_ml(1)
      physpar_pdgmasses( 13) = physpar_ml(2)
      physpar_pdgmasses( 15) = physpar_ml(3)
c
      physpar_pdgwidths(-24) = ph_Wwidth
      physpar_pdgwidths( 23) = ph_Zwidth
      physpar_pdgwidths( 24) = ph_Wwidth
      physpar_pdgwidths( 25) = ph_Hwidth
c      physpar_pdgwidths(6) = ph_twidth
ccc
      physpar_phspmasses(-24) = ph_Wmass
      physpar_phspmasses( 24) = ph_Wmass
      physpar_phspmasses( 23) = ph_Zmass
      physpar_phspmasses( 25) = ph_Hmass
      physpar_phspmasses( -6) = ph_mTop
      physpar_phspmasses(  6) = ph_mTop
c leptons are just a trial
      physpar_phspmasses(-11) = physpar_ml(1)
      physpar_phspmasses(-13) = physpar_ml(2)
      physpar_phspmasses(-15) = physpar_ml(3)
      physpar_phspmasses( 11) = physpar_ml(1)
      physpar_phspmasses( 13) = physpar_ml(2)
      physpar_phspmasses( 15) = physpar_ml(3)
c
      physpar_phspwidths(-24) = ph_Wwidth
      physpar_phspwidths( 23) = ph_Zwidth
      physpar_phspwidths( 24) = ph_Wwidth
      physpar_phspwidths( 25) = ph_Hwidth
      
      ! Recola input parameters



      
      write(*,*) "########################"
      write(*,*) "Initialisation of Recola"
      write(*,*) "########################"
      
      call set_output_file_rcl('*') ! Standard output

      call set_print_level_squared_amplitude_rcl (0)                         !

      if(powheginput('#runningscale').ge.1) then
         call set_dynamic_settings_rcl(1)
      endif
      
      call set_pole_mass_tau_rcl(0d0,0d0)
      call set_pole_mass_bottom_rcl(0d0,0d0)
      call set_light_fermions_rcl(1d-3)

      
      call set_pole_mass_h_rcl (ph_Hmass,ph_Hwidth)
      call set_pole_mass_z_rcl (ph_Zmass,ph_Zwidth)
      call set_pole_mass_w_rcl (ph_Wmass,ph_Wwidth)

      call set_pole_mass_top_rcl (ph_mTop,0d0)
      
      call use_gfermi_scheme_rcl(ph_gmu)

      call get_alpha_rcl(em_alpha)
      if(.not.flg_with_em) then
         em_alpha = 0
      endif
      
      
      ! FIXME: This is only for the fixed scale.
      call set_alphas_rcl (0.12255084585511782d0,ph_Wmass,st_nlight)
      
      
      ! Masses used for the computation of the strong coupling counterterm
!      call set_alphas_masses_rcl(0d0,0d0,173.21d0,0d0,0d0,0d0)
      
      ! Convention to match the usual convention for example in [1001.1307]
	call set_mu_uv_rcl (ph_Wmass)
	call set_mu_ir_rcl (ph_Wmass) ! FIXME This should be dynamical

        
      virtasbornvar=powheginput("#virtasborn") ! Used for the test of the virtual integration

      if(virtasbornvar .eq. 1d0) then
            call set_delta_ir_rcl(0d0,0d0)
      else
            call set_delta_ir_rcl(0d0,pi**2/6d0)
      endif

      
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
cccccc   DEPENDENT QUANTITIES       
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      if((fakevirt .le. 0d0) .and. (.not.flg_bornonly)) then


         
         do i=1,7
            call define_process_rcl(i,procisr(i)(:)//' -> '//proclep//
     +           ' '//procfsr(i)(:),'NLO')
            call unselect_all_gs_powers_BornAmpl_rcl(i)
            call select_gs_power_BornAmpl_rcl(i,0)
            call unselect_all_gs_powers_LoopAmpl_rcl(i)
            call select_gs_power_LoopAmpl_rcl(i,0)
            call split_collier_cache_rcl(i,10) ! This is added to reduce the memory consuption.
         enddo


         write(*,*) "Initialisation of the NLO process"
      elseif(fakevirt == 1d0 .or. (flg_bornonly)) then
         do i=1,7
            call define_process_rcl(i,procisr(i)(:)//' -> '//proclep//
     +           ' '//procfsr(i)(:),'LO')

            call unselect_all_gs_powers_BornAmpl_rcl(i)
            call select_gs_power_BornAmpl_rcl(i,0)
         enddo
         write(*,*) "Initialisation of the LO process"
      else
         write(*,*) "There is a problem with the fakevirt flag"
         stop
      endif
      

      do i = 8, 14
         j=i-7
         call define_process_rcl(i,procisr(j)(:)//' -> '//proclep//' '//procfsr(j)(:)//' A','LO') 
         call unselect_all_gs_powers_BornAmpl_rcl(i)
         call select_gs_power_BornAmpl_rcl(i,0)
      enddo
      
      
      call generate_processes_rcl
      
      end

