
! Copyright 2014 Fabio Cascioli, Jonas Lindert, Philipp Maierhoefer, Stefano Pozzorini
!
! This file is part of OpenLoops.
!
! OpenLoops is free software: you can redistribute it and/or modify
! it under the terms of the GNU General Public License as published by
! the Free Software Foundation, either version 3 of the License, or
! (at your option) any later version.
!
! OpenLoops is distributed in the hope that it will be useful,
! but WITHOUT ANY WARRANTY; without even the implied warranty of
! MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
! GNU General Public License for more details.
!
! You should have received a copy of the GNU General Public License
! along with OpenLoops.  If not, see <http://www.gnu.org/licenses/>.


module ol_parameters_init_/**/REALKIND
  implicit none
  contains

subroutine masspowers(rM, Ga, M, M2, rM2)
  use KIND_TYPES, only: REALKIND
  use ol_parameters_decl_/**/REALKIND, only: CI
  use ol_parameters_decl_/**/DREALKIND, only: cms_on
  implicit none
  real(REALKIND),    intent(in)  :: rM, Ga
  complex(REALKIND), intent(out) :: M,  M2
  real(REALKIND),    intent(out) :: rM2
  M2  = rM*rM - CI*rM*Ga
  if (cms_on == 0) then
    M   = rM
    rM2 = rM*rM
  else
    M = sqrt(M2)
    rM2 = real(M2)
    if (rM < 0) M = -M
  end if
end subroutine masspowers



#ifdef PRECISION_dp

subroutine parameters_init(Mass_E, Mass_M, Mass_L, Mass_U, Mass_D, Mass_S, Mass_C, Width_C, Mass_B, Width_B, Mass_T, Width_T, &
                           Mass_W, Width_W, Mass_Z, Width_Z, Mass_H, Width_H, Coupl_Alpha_QED, Coupl_Alpha_QCD, &
                           last_switch, amp_switch, amp_switch_rescue, &
                           use_coli_cache, check_Ward_tree, check_Ward_loop, out_symmetry, leading_colour)
  ! Assign values of physical input patameters.
  ! Use this subroutine with named arguments, e.g. parameters_init(Mass_B=0._/**/REALKIND) to set
  ! the bottom-quark mass to zero without changing other parameters.
  !
  ! Direct calls of this routine are deprecated. Use set_parameter() interface in module openloops/ol_init instead!
  !
#ifdef USE_IFORT
  use IFPORT
#endif
  use KIND_TYPES, only: REALKIND
  use ol_generic, only: to_string, random_string
  use ol_parameters_decl_/**/REALKIND
#if defined(COLLIER_LEGACY) && defined(USE_COLLIER)
  use bt_TI_lib_switch, only: TI_library ! from COLI: module to switch between COLI and DD libraries
#endif
  use ol_version, only: splash_todo, print_welcome
  implicit none
  real(REALKIND), intent(in), optional :: Mass_E, Mass_M,  Mass_L ! physical (real) lepton masses
  real(REALKIND), intent(in), optional :: Mass_U, Mass_D,  Mass_S ! physical (real) light-quark masses
  real(REALKIND), intent(in), optional :: Mass_C, Width_C, Mass_B, Width_B, Mass_T, Width_T ! physical (real) heavy-quark masses and widths
  real(REALKIND), intent(in), optional :: Mass_W, Width_W, Mass_Z, Width_Z, Mass_H, Width_H ! physical (real) boson masses and widths
  real(REALKIND), intent(in), optional :: Coupl_Alpha_QED, Coupl_Alpha_QCD ! Coupling constants
  integer,  intent(in), optional :: last_switch, amp_switch, amp_switch_rescue ! set mode for check_last_[...] and loop_amp
  integer,  intent(in), optional :: use_coli_cache
  integer,  intent(in), optional :: check_Ward_tree, check_Ward_loop
  integer,  intent(in), optional :: out_symmetry
  integer,  intent(in), optional :: leading_colour

  if (parameters_status == 0) then
    pid_string = trim(to_string(getpid())) // "-" // random_string(4)
  end if

  if (splash_todo .and. .not. nosplash) then
    call print_welcome()
  end if

  ! Mode switches
  if (present(last_switch))       l_switch        = last_switch
  if (present(amp_switch))        a_switch        = amp_switch
  if (present(amp_switch_rescue)) a_switch_rescue = amp_switch_rescue

#if defined(COLLIER_LEGACY) && defined(USE_COLLIER)
  if (a_switch == 1) TI_library = 1 ! use COLI
  if (a_switch == 7) TI_library = 2 ! use DD
#endif

  if (present(use_coli_cache)) coli_cache_use = use_coli_cache
  if (present(check_Ward_tree)) Ward_tree = check_Ward_tree
  if (present(check_Ward_loop)) Ward_loop = check_Ward_loop
  if (present(out_symmetry)) out_symmetry_on = out_symmetry
  if (present(leading_colour)) LeadingColour = leading_colour
  ! Check for optional arguments
  if (present(Coupl_Alpha_QED)) alpha_QED = Coupl_Alpha_QED
  if (present(Coupl_Alpha_QCD)) alpha_QCD = Coupl_Alpha_QCD
  if (present(Mass_W))  rMW_unscaled = Mass_W
  if (present(Mass_Z))  rMZ_unscaled = Mass_Z
  if (present(Mass_H))  rMH_unscaled = Mass_H
  if (present(Width_C)) wMC_unscaled = Width_C
  if (present(Width_B)) wMB_unscaled = Width_B
  if (present(Width_T)) wMT_unscaled = Width_T
  if (present(Width_W)) wMW_unscaled = Width_W
  if (present(Width_W)) wMY_unscaled = Width_W
  if (present(Width_Z)) wMZ_unscaled = Width_Z
  if (present(Width_Z)) wMX_unscaled = Width_Z
  if (present(Width_H)) wMH_unscaled = Width_H
  if (present(Mass_E))  then
    rME_unscaled = Mass_E
    rYE_unscaled = Mass_M
  end if
  if (present(Mass_M))  then
    rMM_unscaled = Mass_M
    rYM_unscaled = Mass_M
  end if
  if (present(Mass_L))  then
    rML_unscaled = Mass_L
    rYL_unscaled = Mass_L
  end if
  if (present(Mass_U))  then
    rMU_unscaled = Mass_U
    rYU_unscaled = Mass_U
  end if
  if (present(Mass_D))  then
    rMD_unscaled = Mass_D
    rYD_unscaled = Mass_D
  end if
  if (present(Mass_S))  then
    rMS_unscaled = Mass_S
    rYS_unscaled = Mass_S
  end if
  if (present(Mass_C))  then
    rMC_unscaled = Mass_C
    rYC_unscaled = Mass_C
  end if
  if (present(Mass_B))  then
    rMB_unscaled = Mass_B
    rYB_unscaled = Mass_B
  end if
  if (present(Mass_T))  then
    rMT_unscaled = Mass_T
    rYT_unscaled = Mass_T
  end if

  ! set mass of V-auxiliary fields
  rMX_unscaled = rMZ_unscaled
  rMY_unscaled = rMW_unscaled

  rME = scalefactor * rME_unscaled
  wME = scalefactor * wME_unscaled
  rYE = scalefactor * rYE_unscaled
  rMM = scalefactor * rMM_unscaled
  wMM = scalefactor * wMM_unscaled
  rYM = scalefactor * rYM_unscaled
  rML = scalefactor * rML_unscaled
  wML = scalefactor * wML_unscaled
  rYL = scalefactor * rYL_unscaled
  rMU = scalefactor * rMU_unscaled
  wMU = scalefactor * wMU_unscaled
  rYU = scalefactor * rYU_unscaled
  rMD = scalefactor * rMD_unscaled
  wMD = scalefactor * wMD_unscaled
  rYD = scalefactor * rYD_unscaled
  rMS = scalefactor * rMS_unscaled
  wMS = scalefactor * wMS_unscaled
  rYS = scalefactor * rYS_unscaled
  rMC = scalefactor * rMC_unscaled
  wMC = scalefactor * wMC_unscaled
  rYC = scalefactor * rYC_unscaled
  rMB = scalefactor * rMB_unscaled
  wMB = scalefactor * wMB_unscaled
  rYB = scalefactor * rYB_unscaled
  wYB = scalefactor * wYB_unscaled
  rMT = scalefactor * rMT_unscaled
  wMT = scalefactor * wMT_unscaled
  rYT = scalefactor * rYT_unscaled
  wYT = scalefactor * wYT_unscaled
  rMW = scalefactor * rMW_unscaled
  wMW = scalefactor * wMW_unscaled
  rMZ = scalefactor * rMZ_unscaled
  wMZ = scalefactor * wMZ_unscaled
  rMX = scalefactor * rMX_unscaled
  wMX = scalefactor * wMX_unscaled
  rMY = scalefactor * rMY_unscaled
  wMY = scalefactor * wMY_unscaled
  rMH = scalefactor * rMH_unscaled
  wMH = scalefactor * wMH_unscaled

  rMA0 = scalefactor * rMA0_unscaled
  wMA0 = scalefactor * wMA0_unscaled
  rMHH = scalefactor * rMHH_unscaled
  wMHH = scalefactor * wMHH_unscaled
  rMHp = scalefactor * rMHp_unscaled
  wMHp = scalefactor * wMHp_unscaled

  MREG = scalefactor * MREG_unscaled

  Gmu  = Gmu_unscaled / scalefactor**2

! ifdef PRECISION_dp
#else

subroutine parameters_init()
  ! non-dp initialisation: synchronise with dp parameters
  use KIND_TYPES, only: REALKIND
  use ol_parameters_decl_/**/REALKIND
  use ol_parameters_decl_/**/DREALKIND, only: &
    & model, parameters_verbose, scalefactor_dp => scalefactor, cms_on => cms_on, ew_scheme => ew_scheme, &
    & parameters_status_dp => parameters_status,  alpha_QCD_dp => alpha_QCD, &
    & alpha_QED_0_dp => alpha_QED_0, alpha_QED_MZ_dp => alpha_QED_MZ, Gmu_dp => Gmu, &
    & rME_dp => rME, wME_dp => wME, rMM_dp => rMM, wMM_dp => wMM, rML_dp => rML, wML_dp => wML, &
    & rMU_dp => rMU, wMU_dp => wMU, rMD_dp => rMD, wMD_dp => wMD, rMS_dp => rMS, wMS_dp => wMS, &
    & rMC_dp => rMC, wMC_dp => wMC, rMB_dp => rMB, wMB_dp => wMB, rMT_dp => rMT, wMT_dp => wMT, &
    & rMW_dp => rMW, wMW_dp => wMW, rMZ_dp => rMZ, wMZ_dp => wMZ, rMH_dp => rMH, wMH_dp => wMH, &
    & rMX_dp => rMX, wMX_dp => wMX, rMY_dp => rMY, wMY_dp => wMY, &
    & rYE_dp => rYE, rYM_dp => rYM, rYL_dp => rYL, rYU_dp => rYU, rYD_dp => rYD, rYS_dp => rYS, &
    & rYC_dp => rYC, rYB_dp => rYB, wYB_dp => wYB, rYT_dp => rYT, wYT_dp => wYT, &
    & rMA0_dp => rMA0, wMA0_dp => wMA0, rMHH_dp => rMHH, wMHH_dp => wMHH, rMHp_dp => rMHp, wMHp_dp => wMHp, &
    & thdmTB_dp => thdmTB, thdmSBA_dp => thdmSBA, thdmL5_dp => thdmL5
  implicit none

  scalefactor = scalefactor_dp

  alpha_QED_0  = alpha_QED_0_dp
  alpha_QED_MZ = alpha_QED_MZ_dp
  Gmu          = Gmu_dp
  alpha_QCD    = alpha_QCD_dp

  rME = rME_dp
  wME = wME_dp
  rMM = rMM_dp
  wMM = wMM_dp
  rML = rML_dp
  wML = wML_dp
  rMU = rMU_dp
  wMU = wMU_dp
  rMD = rMD_dp
  wMD = wMD_dp
  rMS = rMS_dp
  wMS = wMS_dp
  rMC = rMC_dp
  wMC = wMC_dp
  rMB = rMB_dp
  wMB = wMB_dp
  rMT = rMT_dp
  wMT = wMT_dp
  rMW = rMW_dp
  wMW = wMW_dp
  rMZ = rMZ_dp
  wMZ = wMZ_dp
  rMX = rMX_dp
  wMX = wMX_dp
  rMY = rMY_dp
  wMY = wMY_dp
  rMH = rMH_dp
  wMH = wMH_dp

  rYE = rYE_dp
  rYM = rYM_dp
  rYL = rYL_dp
  rYU = rYU_dp
  rYD = rYD_dp
  rYS = rYS_dp
  rYC = rYC_dp
  rYB = rYB_dp
  wYB = wYB_dp
  rYT = rYT_dp
  wYT = wYT_dp

  thdmTB = thdmTB_dp
  thdmSBA = thdmSBA_dp
  thdmL5 = thdmL5_dp

  rMA0 = rMA0_dp
  wMA0 = wMA0_dp
  rMHH = rMHH_dp
  wMHH = wMHH_dp
  rMHp = rMHp_dp
  wMHp = wMHp_dp

! ifdef PRECISION_dp
#endif

  ! Complex masses and squared masses
  call masspowers(rME, wME, ME, ME2, rME2)
  call masspowers(rMM, wMM, MM, MM2, rMM2)
  call masspowers(rML, wML, ML, ML2, rML2)
  call masspowers(rMU, wMU, MU, MU2, rMU2)
  call masspowers(rMD, wMD, MD, MD2, rMD2)
  call masspowers(rMS, wMS, MS, MS2, rMS2)
  call masspowers(rMC, wMC, MC, MC2, rMC2)
  call masspowers(rMB, wMB, MB, MB2, rMB2)
  call masspowers(rMT, wMT, MT, MT2, rMT2)
  call masspowers(rMW, wMW, MW, MW2, rMW2)
  call masspowers(rMZ, wMZ, MZ, MZ2, rMZ2)
  call masspowers(rMX, wMX, MX, MX2, rMX2)
  call masspowers(rMY, wMY, MY, MY2, rMY2)
  call masspowers(rMH, wMH, MH, MH2, rMH2)

  call masspowers(rYE, rZERO, YE, YE2, rYE2)
  call masspowers(rYM, rZERO, YM, YM2, rYM2)
  call masspowers(rYL, rZERO, YL, YL2, rYL2)
  call masspowers(rYU, rZERO, YU, YU2, rYU2)
  call masspowers(rYD, rZERO, YD, YD2, rYD2)
  call masspowers(rYS, rZERO, YS, YS2, rYS2)
  call masspowers(rYC, rZERO, YC, YC2, rYC2)
  call masspowers(rYB, wYB, YB, YB2, rYB2)
  call masspowers(rYT, wYT, YT, YT2, rYT2)

  call masspowers(rMA0, wMA0, MA0, MA02, rMA02)
  call masspowers(rMHH, wMHH, MHH, MHH2, rMHH2)
  call masspowers(rMHp, wMHp, MHp, MHp2, rMHp2)

  ! Dependent couplings

  !QCD
  G2_QCD = 4*pi*alpha_QCD
  gQCD   = sqrt(G2_QCD)

  !EW
  if ( cms_on == 0 ) then
    cw   = rMW/rMZ
  else
    cw   = MW/MZ
  end if
  cw2    = cw**2
  cw3    = cw**3
  cw4    = cw2**2
  sw2    = 1. - cw2
  sw     = sqrt(sw2)
  sw3    = sw**3
  sw4    = sw2**2
  sw6    = sw2**3

  if (ew_scheme == 0) then ! alpha(0) OS scheme
    alpha_QED = alpha_QED_0
  else if (ew_scheme == 1) then ! Gmu scheme
    alpha_QED = sqrt2/pi*Gmu*abs(MW2*sw2)
  else if (ew_scheme == 2) then ! alpha(MZ) scheme
    alpha_QED = alpha_QED_MZ
  end if

  E2_QED = 4*pi*alpha_QED
  eQED   = sqrt(E2_QED)

  ! (1) Right-handed Z-fermion couplings = gf^+ = gZRH*Qf in Denner's FRs
  ! (2) Left-handed  Z-fermion couplings = gf^- = gZLH*(I3f-sw2*Qf) in Denner's FRs
  gZRH = -sw/cw
  gZLH = 1/(sw*cw)
  gZn  = [    ZERO   , gZLH*( 0.5_/**/REALKIND            ) ] ! neutrino
  gZl  = [   -gZRH   , gZLH*(-0.5_/**/REALKIND +    sw2   ) ] ! lepton
  gZu  = [ (2*gZRH)/3, gZLH*( 0.5_/**/REALKIND - (2*sw2)/3) ] ! up
  gZd  = [   -gZRH /3, gZLH*(-0.5_/**/REALKIND +    sw2 /3) ] ! down
  ! Right- (1) and left-handed (2) couplings of scalars to fermions
  ! gPud = P+ u~ d; gPdu = P- d~ u; gPnl = P+ n~ l; gPln = P- l~ n (all incoming)
  gPud = [   -YD,   YU ]
  gPus = [   -YS,   YU ]
  gPub = [   -YB,   YU ]
  gPcd = [   -YD,   YC ]
  gPcs = [   -YS,   YC ]
  gPcb = [   -YB,   YC ]
  gPtd = [   -YD,   YT ]
  gPts = [   -YS,   YT ]
  gPtb = [   -YB,   YT ]
  gPdu = [   -YU,   YD ]
  gPdc = [   -YC,   YD ]
  gPdt = [   -YT,   YD ]
  gPsu = [   -YU,   YS ]
  gPsc = [   -YC,   YS ]
  gPst = [   -YT,   YS ]
  gPbu = [   -YU,   YB ]
  gPbc = [   -YC,   YB ]
  gPbt = [   -YT,   YB ]

  if (trim(model) == "2hdm") call thdm_parameters_init()

  if (trim(model) == "higgspo") call model_higgspo_parameters_init()


  ! Number of time this function has been called:
#ifdef PRECISION_dp
  parameters_status = parameters_status + 1
#else
  parameters_status = parameters_status_dp
#endif

  ! write parameters
  if (parameters_verbose == 1 ) then
    call parameters_write()
  end if

end subroutine parameters_init



subroutine thdm_parameters_init()
  use ol_debug, only: ol_fatal
  use ol_parameters_decl_/**/REALKIND
  implicit none
  ! mixing angles
  thdm_b = atan(thdmTB)
  thdm_a = thdm_b - asin(thdmSBA)
  thdmCA  = cos(thdm_a)
  thdmSA  = sin(thdm_a)
  thdmCB  = cos(thdm_b)
  thdmSB  = sin(thdm_b)
  thdmC2A = cos(2*thdm_a)
  thdmS2A = sin(2*thdm_a)
  thdmC2B = cos(2*thdm_b)
  thdmS2B = sin(2*thdm_b)
  thdmCAB = cos(thdm_a+thdm_b)
  thdmSAB = sin(thdm_a+thdm_b)
  thdmCBA = cos(thdm_b-thdm_a)
  if (thdmTB == 0) then
    call ol_fatal("2HDM model parameter ill defined: tan(beta) = 0")
  end if
  ! 2HDM Type I or Type II
  if (thdm_type == 1) then
    if (thdmSB == 0) then
      call ol_fatal("2HDM-Type-I model parameter ill defined: sin(beta) = 0")
    end if
    thdmYuk1 = thdmCA/thdmSB
    thdmYuk2 = thdmSA/thdmSB
    thdmYuk3 = -1/thdmTB
  else if (thdm_type == 2) then
    if (thdmCB == 0) then
      call ol_fatal("2HDM-Type-II model parameter ill defined: cos(beta) = 0")
    end if
    thdmYuk1 = -thdmSA/thdmCB
    thdmYuk2 = thdmCA/thdmCB
    thdmYuk3 = thdmTB
  end if
  ! 2HDM charged higgs quark couplings
  thdmHpud = [-YD*(-thdmYuk3), YU/thdmTB]
  thdmHpcs = [-YS*(-thdmYuk3), YC/thdmTB]
  thdmHptb = [-YB*(-thdmYuk3), YT/thdmTB]
  thdmHpdu = [-YU/thdmTB, YD*(-thdmYuk3)]
  thdmHpsc = [-YC/thdmTB, YS*(-thdmYuk3)]
  thdmHpbt = [-YT/thdmTB, YB*(-thdmYuk3)]
end subroutine thdm_parameters_init


! *********************************************************************
! parameters_init for HiggsPO model
! *********************************************************************
#ifdef PRECISION_dp
subroutine model_higgspo_parameters_init()
  use ol_parameters_decl_/**/REALKIND
  implicit none
  complex(REALKIND) :: gRL
  HPOvev = scalefactor * HPOvev_unscaled
#else
subroutine model_higgspo_parameters_init()
  use ol_parameters_decl_/**/REALKIND
  use ol_parameters_decl_/**/DREALKIND, only: scalefactor_dp => scalefactor, &
    &  HPOvev_dp => HPOvev, ThetaCabi_dp => ThetaCabi, &
    &  HPOgZeL_dp => HPOgZeL, HPOgZeR_dp => HPOgZeR, HPOgZv_dp => HPOgZv, HPOgZuL_dp => HPOgZuL, &
    &  HPOgZuR_dp => HPOgZuR, HPOgZdL_dp  => HPOgZdL, HPOgZdR_dp => HPOgZdR, &
    &  HPOgWeL_dp => HPOgWeL, HPOgWmL_dp => HPOgWmL, HPOgWlL_dp => HPOgWlL, HPOgWqL_dp => HPOgWqL, &
    &  HPOkapWW_dp  => HPOkapWW, HPOkapZZ_dp  => HPOkapZZ, HPOepsWW_dp  => HPOepsWW, &
    &  HPOaepsWW_dp => HPOaepsWW, HPOepsZZ_dp  => HPOepsZZ, HPOaepsZZ_dp => HPOaepsZZ, &
    &  HPOepsZA_dp  => HPOepsZA, HPOaepsZA_dp => HPOaepsZA, HPOepsAA_dp  => HPOepsAA, &
    &  HPOaepsAA_dp => HPOaepsAA, HPOepsZnn_dp => HPOepsZnn, HPOepsZll_dp => HPOepsZll, &
    &  HPOepsZdd_dp => HPOepsZdd, HPOepsZuu_dp => HPOepsZuu, HPOepsWqq_dp => HPOepsWqq, HPOepsWln_dp => HPOepsWln, &
    &  HPOphiWeL_dp => HPOphiWeL, HPOphiWmL_dp => HPOphiWmL, HPOphiWlL_dp => HPOphiWlL, HPOphiWqL_dp => HPOphiWqL
  implicit none
  complex(REALKIND) :: gRL
  scalefactor = scalefactor_dp
  ThetaCabi = ThetaCabi_dp
  HPOvev    = HPOvev_dp
  HPOgZeL   = HPOgZeL_dp
  HPOgZeR   = HPOgZeR_dp
  HPOgZv    = HPOgZv_dp
  HPOgZuL   = HPOgZuL_dp
  HPOgZuR   = HPOgZuR_dp
  HPOgZdL   = HPOgZdL_dp
  HPOgZdR   = HPOgZdR_dp
  HPOgWeL   = HPOgWeL_dp
  HPOgWmL   = HPOgWmL_dp
  HPOgWlL   = HPOgWlL_dp
  HPOgWqL   = HPOgWqL_dp
  HPOkapWW  = HPOkapWW_dp
  HPOkapZZ  = HPOkapZZ_dp
  HPOepsWW  = HPOepsWW_dp
  HPOaepsWW = HPOaepsWW_dp
  HPOepsZZ  = HPOepsZZ_dp
  HPOaepsZZ = HPOaepsZZ_dp
  HPOepsZA  = HPOepsZA_dp
  HPOaepsZA = HPOaepsZA_dp
  HPOepsAA  = HPOepsAA_dp
  HPOaepsAA = HPOaepsAA_dp
  HPOepsZnn = HPOepsZnn_dp
  HPOepsZll = HPOepsZll_dp
  HPOepsZdd = HPOepsZdd_dp
  HPOepsZuu = HPOepsZuu_dp
  HPOepsWqq = HPOepsWqq_dp
  HPOepsWln = HPOepsWln_dp
  HPOphiWeL = HPOphiWeL_dp
  HPOphiWmL = HPOphiWmL_dp
  HPOphiWlL = HPOphiWlL_dp
  HPOphiWqL = HPOphiWqL_dp
#endif
  cCabi = cos(ThetaCabi)
  sCabi = sin(ThetaCabi)
!  gRL = 1/(cw*sw)
  gRL = 2*MZ/HPOvev
  gZn  = [  ZERO      , gRL*HPOgZv ] ! neutrino
  gZl  = gRL*[ HPOgZeR, HPOgZeL    ] ! lepton
  gZu  = gRL*[ HPOgZuR, HPOgZuL    ] ! up
  gZd  = gRL*[ HPOgZdR, HPOgZdL    ] ! down

  HPOcpWeL = cos(HPOphiWeL)
  HPOspWeL = sin(HPOphiWeL)
  HPOcpWmL = cos(HPOphiWmL)
  HPOspWmL = sin(HPOphiWmL)
  HPOcpWlL = cos(HPOphiWlL)
  HPOspWlL = sin(HPOphiWlL)
  HPOcpWqL = cos(HPOphiWqL)
  HPOspWqL = sin(HPOphiWqL)
end subroutine model_higgspo_parameters_init




subroutine ensure_mp_init()
  ! synchronise non-dp parameters with dp if they are not up to date
  ! should be called after parameters_init()
  ! and in tree matrix element routines before anything is done
#ifndef PRECISION_dp
  use ol_parameters_decl_/**/REALKIND, only: parameters_status
  use ol_parameters_decl_/**/DREALKIND, only: &
    & parameters_status_dp => parameters_status
  implicit none
  if (parameters_status_dp /= parameters_status) call parameters_init()
#endif
end subroutine ensure_mp_init



#ifdef PRECISION_dp
! **********************************************************************
subroutine channel_on(ch)
! If ch = -1 generate new channel number ch > 0 and switch channel ch on.
! Otherwise initialise the existing channel ch to compute a new phase space point.
! **********************************************************************
  use ol_parameters_decl_/**/DREALKIND, only: &
    next_channel_number, coli_cache_use, a_switch
  use ol_generic, only: to_string
  use ol_debug, only: ol_error, ol_fatal
#ifdef USE_COLLIER
#ifndef COLLIER_LEGACY
  use collier, only: initevent_cll
#endif
#endif
  implicit none
  integer, intent(inout) :: ch
#ifdef USE_COLLIER
#ifdef COLLIER_LEGACY
  integer :: maxcache
  external :: cacheon, cachereonch, cacheinit ! from COLI
  if (coli_cache_use /= 0 .and. (a_switch == 1 .or. a_switch == 2 .or. a_switch == 3)) then
    call getmaxcache(maxcache)
    if (ch == -1) then
      ch = next_channel_number
      next_channel_number = next_channel_number + 1
      if (ch > maxcache) then
        ! maximum number of channels exceeded
        call ol_error(2, 'subroutine channel_on:')
        call ol_error(2, 'next channel = ' // to_string(next_channel_number) // '/' // to_string(maxcache))
        call ol_error(2, 'to handle more channels increase maxcache')
        call ol_error(2,  'in collier/src/coli_params_cache.h')
        call ol_fatal()
      else
        call cacheon(ch)
      end if
    end if

    call cachereonch(ch)  ! cache channel reactivated
    call cacheinit(0,ch) ! cache channel initialised for new PS point
  end if
#else
  if (coli_cache_use /= 0 .and. (a_switch == 1 .or. a_switch == 2 .or. a_switch == 3 .or. a_switch == 7)) then
    if (ch == -1) then
      ch = next_channel_number
      next_channel_number = next_channel_number + 1
    end if
    if (a_switch == 7) then
      call initevent_cll(2*ch)
    else
      call initevent_cll(2*ch-1)
    end if
  end if
#endif
#endif
end subroutine channel_on



! **********************************************************************
subroutine channel_off(ch)
! switch cache for channel ch temporarily off
! **********************************************************************
  use ol_parameters_decl_/**/DREALKIND, only: coli_cache_use, a_switch
  implicit none
  integer, intent(in) :: ch
#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
  external :: cachetempoffch
  if (coli_cache_use /= 0 .and. (a_switch == 1 .or. a_switch == 2 .or. a_switch == 3)) then
    call cachetempoffch(ch)
  end if
#endif
end subroutine channel_off
! #ifdef PRECISION_dp
#endif


subroutine init_kin_arrays(Npart)
  use ol_momenta_decl_/**/REALKIND, only: Q, QInvariantsMatrix
  use ol_external_decl_/**/REALKIND, only: P_ex, binom2, crossing, inverse_crossing, gf_array, Ward_array
  use ol_external_decl_/**/REALKIND, only: allocatedNpart
  implicit none
  integer, intent(in) :: Npart
  integer :: n_
  if (Npart > allocatedNpart) then
    if (allocatedNpart /= 0) then
      call clean_kin_arrays()
    end if
    allocate(Q(5,0:2**Npart-1))
    Q = 0
    allocate(QInvariantsMatrix(Npart,Npart))
    QInvariantsMatrix = 0

    allocate(binom2(Npart))
    binom2 = [((n_*(n_-1))/2, n_=1, size(binom2))]

    allocate(P_ex(0:3,Npart))  ! uncleaned external 2->n-2 momenta, set by conv_mom_scatt2in
    allocate(crossing(Npart))
    crossing = 0        ! only used if a reduction error occurs
    allocate(inverse_crossing(Npart))
    inverse_crossing = 0 ! set by conv_mom_scatt2in
    !
    allocate(gf_array(Npart))
    gf_array = 0
    allocate(Ward_array(Npart))
    Ward_array = 0

    allocatedNpart = Npart
  end if
end subroutine init_kin_arrays

subroutine clean_kin_arrays
  use ol_external_decl_/**/REALKIND, only: allocatedNpart
  use ol_momenta_decl_/**/REALKIND, only: Q, QInvariantsMatrix
  use ol_external_decl_/**/REALKIND, only: P_ex, binom2, crossing, inverse_crossing, gf_array, Ward_array
  implicit none
  if (allocated(Q)) deallocate(Q)
  if (allocated(QInvariantsMatrix)) deallocate(QInvariantsMatrix)
  if (allocated(binom2)) deallocate(binom2)
  if (allocated(P_ex)) deallocate(P_ex)
  if (allocated(crossing)) deallocate(crossing)
  if (allocated(inverse_crossing)) deallocate(inverse_crossing)
  if (allocated(gf_array)) deallocate(gf_array)
  if (allocated(Ward_array)) deallocate(Ward_array)
  allocatedNpart = 0
end subroutine

#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
! *************************
subroutine tensor_ints_init()
! *************************
  use bt_BuildTensors_/**/REALKIND, only: init_tables
  implicit none
  call init_tables(6,6)
end subroutine tensor_ints_init
#endif



subroutine tensorrank_init(rank)
  use ol_generic, only: binomial
  use ol_tensor_storage_/**/REALKIND, only: tensor_stored, tensor_storage_maxrank
  use ol_tensor_bookkeeping, only: initialised_rank, init_tensorbookkeeping
  implicit none
  integer, intent(in) :: rank
  if (rank > initialised_rank) call init_tensorbookkeeping(rank)
  if (allocated(tensor_stored)) deallocate(tensor_stored)
  allocate(tensor_stored(binomial(rank+4,4)))
  tensor_storage_maxrank = rank
end subroutine tensorrank_init



#ifdef PRECISION_dp
! **********************************************************************
subroutine loop_parameters_init(renscale, fact_UV, fact_IR, pole1_UV, pole1_IR, pole2_IR, polenorm_swi, &
                                N_quarks, nq_nondecoupled, &
                                opp_rootsvalue, opp_limitvalue, opp_thrs, opp_idig, opp_scaloop, &
                                sam_isca, sam_verbosity, sam_itest, fermion_loops, nonfermion_loops, &
                                CT_on, R2_on, IR_on, polecheck, set_C_PV_threshold, &
                                set_D_PV_threshold, set_dd_red_mode)
! **********************************************************************
! Assign values of dimensional regularisation parameters. Use this subroutine
! with named arguments, e.g. parameters_init(pole1_UV=0._/**/REALKIND) to set the
! single UV pole to zero without changing other parameters. Always use this
! routine to change parameters, otherwise factors which contain these
! parameters will not be recalculated.
! **********************************************************************
! renscale = renormalisation scale
! ----------------------------------------------------------------------
! mu2_UV = (fact_UV*renscale)^2 = UV dim-reg scale (squared)
! mu2_IR = (fact_IR*renscale)^2 = IR dim-reg scale (squared)
! ----------------------------------------------------------------------
! numerical values of poles in D=4-2*eps dimensions
! pole1_UV -> de1_i_UV= K_i(eps_UV)/eps_UV   = de1_UV
! pole1_IR -> de1_i_IR= K_i(eps_IR)/eps_IR   = de1_IR
! pole2_IR -> de2_i_IR= K_i(eps_IR)/eps_IR^2   (depends on K_i)
! ----------------------------------------------------------------------
! results of loop/dipole routines based on generic normalisation
! K_i(eps) = (4Pi)^eps/Gamma(1-eps) + de2_i_shift*eps^2 +  O(esp^3)
! ----------------------------------------------------------------------
! polenorm_swi = 0 <=> Binoth-Les-Houches accord normalisation (default)
! de2_i_shift  = de2_0_shift = 0
! K_i(eps)     = K_0(eps)    = (4Pi)^eps/Gamma(1-eps)
! ----------------------------------------------------------------------
! polenorm_swi = 1 <=> normalisation employed by COLI library
! de2_i_shift  = de2_1_shift = Pi^2/6
! K_i(eps)     = K_1(eps)    = (4Pi)^eps*Gamma(1+eps)
! ----------------------------------------------------------------------
! Normalisation dependence of IR-divergent Laurent series
! in D=4-2*eps dimensions (i=0,1,...)
!
! F        = K_i(eps)*[F_i(0) + F(1)/eps       + F(2)/eps**2]
!          =           F_i(0) + F(1)*de1_IR    + F(2)*de2_i_IR
!          = independent of de2_i_shift normalisation convention
!
! de2_i_IR = de2_0_IR + de2_i_shift
!          = de2_j_IR + de2_i_shift - de2_j_shift
!
! F_i(0)   = F_0(0) - F(2)*de2_i_shift
!          = F_j(0) - F(2)*[de2_i_shift-de2_j_shift]
! **********************************************************************
  use KIND_TYPES, only: REALKIND
  use ol_generic, only: to_string
  use ol_debug, only: ol_error, ol_fatal, olodebug_unit
  use ol_cwrappers, only: stdout_off, stdout_on
  use ol_tensor_storage_/**/REALKIND, only: tensor_storage_maxrank
  use ol_parameters_decl_/**/REALKIND
  use ol_loop_parameters_decl_/**/REALKIND
  use ol_qcd_renormalisation_/**/REALKIND, only: qcd_renormalisation
  use ol_ew_renormalisation_/**/REALKIND, only: ew_renormalisation
#ifdef USE_COLLIER
#ifdef COLLIER_LEGACY
  use dd_init_/**/REALKIND, only: dd_setmode, dd_setparam
#else
  use collier, only: init_cll, initcachesystem_cll, setmode_cll, setmuuv2_cll, &
    & setmuir2_cll, setdeltauv_cll, setdeltair_cll, settenred_cll, setaccuracy_cll, &
    & initmonitoring_cll
#endif
#endif
#ifdef USE_ONELOOP
  use avh_olo, only: olo_scale, olo_onshell, olo_unit
#endif
#ifdef USE_SAMURAI
  use msamurai, only: initsamurai
#endif
  implicit none

  real(REALKIND), intent(in), optional :: renscale, fact_UV, fact_IR, pole1_UV, pole1_IR, pole2_IR
  integer,        intent(in), optional :: polenorm_swi, N_quarks, nq_nondecoupled

  ! DD parameters
  real(REALKIND), intent(in), optional :: set_C_PV_threshold, set_D_PV_threshold
  integer,        intent(in), optional :: set_dd_red_mode

  ! CutTools parameters
  real(REALKIND), intent(in), optional :: opp_rootsvalue, opp_limitvalue, opp_thrs
  integer,        intent(in), optional :: opp_idig, opp_scaloop

  ! Samurai parameters
  integer,        intent(in), optional :: sam_isca, sam_verbosity, sam_itest
  ! Switches for counter terms and R2
  integer,        intent(in), optional :: fermion_loops, nonfermion_loops, polecheck
  integer,        intent(in), optional :: CT_on, R2_on, IR_on

  real(REALKIND) :: mp2(10)

  if (present(renscale)) then
    if (mureg_unscaled /= renscale) reset_mureg = .true.
    mureg_unscaled = renscale
    muren_unscaled = renscale
  end if
  if (present(fact_UV))         x_UV          = fact_UV
  if (present(fact_IR))         x_IR          = fact_IR
  if (present(pole1_UV))        de1_UV        = pole1_UV
  if (present(pole1_IR))        de1_IR        = pole1_IR
  if (present(pole2_IR))        de2_i_IR      = pole2_IR
  if (present(polenorm_swi))    norm_swi      = polenorm_swi
  if (present(N_quarks))        nf            = N_quarks
  if (present(nq_nondecoupled)) nq_nondecoupl = nq_nondecoupled

  if (present(set_C_PV_threshold)) C_PV_threshold = set_C_PV_threshold
  if (present(set_D_PV_threshold)) D_PV_threshold = set_D_PV_threshold
  if (present(set_dd_red_mode))    dd_red_mode    = set_dd_red_mode

  if (present(opp_rootsvalue)) then
    if (opprootsvalue_unscaled /= opp_rootsvalue) cuttools_not_init = .true.
    opprootsvalue_unscaled = opp_rootsvalue
  end if
  if (present(opp_limitvalue)) then
    if (opplimitvalue /= opp_limitvalue) cuttools_not_init = .true.
    opplimitvalue = opp_limitvalue
  end if
  if (present(opp_thrs)) then
    if (oppthrs /= opp_thrs) reset_opp = .true.
    oppthrs = opp_thrs
  end if
  if (present(opp_idig)) then
    if (oppidig /= opp_idig) cuttools_not_init = .true.
    oppidig = opp_idig
  end if
  if (present(opp_scaloop)) then
    if (oppscaloop /= opp_scaloop) cuttools_not_init = .true.
    oppscaloop = opp_scaloop
  end if
  if (present(sam_isca)) then
    if (set_isca /= sam_isca) samurai_not_init = .true.
    set_isca = sam_isca
  end if
  if (present(sam_verbosity)) then
    if (set_verbosity /= sam_verbosity) samurai_not_init = .true.
    set_verbosity = sam_verbosity
  end if
  if (present(sam_itest)) then
    if (set_itest /= sam_itest) samurai_not_init = .true.
    set_itest = sam_itest
  end if

  if (present(fermion_loops))    SwF = fermion_loops
  if (present(nonfermion_loops)) SwB = nonfermion_loops


  if (present(CT_on)) CT_is_on = CT_on
  if (present(R2_on)) R2_is_on = R2_on
  if (present(IR_on)) IR_is_on = IR_on
  if (present(polecheck)) polecheck_is = polecheck

  if (reset_scalefactor) then
    reset_mureg = .true.
    reset_opp = .true.
    reset_scalefactor = .false.
  end if

  opprootsvalue = scalefactor * opprootsvalue_unscaled
  mureg = scalefactor * mureg_unscaled
  muren = scalefactor * muren_unscaled
  muyc = scalefactor * muyc_unscaled
  muyb = scalefactor * muyb_unscaled
  muyt = scalefactor * muyt_unscaled

  ! convention for dim-reg Poles K_i(eps)/eps^N
  if (norm_swi == 0) then ! Les-Houches Accord normalisation (default)
    de2_i_shift = 0
    norm_name   = 'LH-accord '
  else if (norm_swi == 1) then ! COLI normalisation
    de2_i_shift = pi2_6
    norm_name   = 'COLI      '
  else
    call ol_error(2,'routine loop_parameters_init: ')
    call ol_error(2,'norm_swi = ' // to_string(norm_swi) // ' not allowed.')
    call ol_fatal()
  end if

! ifdef PRECISION_dp
#else

subroutine loop_parameters_init
  ! non-dp initialisation: synchronise with dp parameters
  use ol_tensor_storage_/**/REALKIND, only: tensor_storage_maxrank
  use ol_parameters_decl_/**/REALKIND, only: pi2_6
  use ol_loop_parameters_decl_/**/REALKIND
  use ol_loop_parameters_decl_/**/DREALKIND, only: &
    & loop_parameters_status_dp => loop_parameters_status, norm_swi, a_switch, a_switch_rescue, redlib_qp, &
    & dd_qp_not_init, tensorlib_qp_not_init, mureg_dp => mureg, muren_dp => muren, fact_UV_dp => x_UV, fact_IR_dp => x_IR, &
    & pole1_UV_dp => de1_UV, pole1_IR_dp => de1_IR, pole2_IR_dp => de2_i_IR, do_ew_renorm, maxrank
#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
  use dd_init_/**/REALKIND, only: dd_setmode, dd_setparam
#endif
  use ol_qcd_renormalisation_/**/REALKIND, only: qcd_renormalisation
  use ol_ew_renormalisation_/**/REALKIND, only: ew_renormalisation
  implicit none

  if (norm_swi == 0) then
    de2_i_shift = 0
  else if (norm_swi == 1) then
    de2_i_shift = pi2_6
  end if

  mureg    = mureg_dp
  muren    = muren_dp

  x_UV     = fact_UV_dp
  x_IR     = fact_IR_dp
  de1_UV   = pole1_UV_dp
  de1_IR   = pole1_IR_dp
  de2_i_IR = pole2_IR_dp

! ifdef PRECISION_dp
#endif

  if (maxrank > tensor_storage_maxrank) call tensorrank_init(maxrank)

  de2_0_IR = de2_i_IR - de2_i_shift         ! LH-norm double pole
  de2_1_IR = de2_i_IR - de2_i_shift + pi2_6 ! COLI-norm double pole
  ! renormalisation & regularization scale
  mureg2 = mureg**2
  muren2 = muren**2

  if (muyc /= 0) then
    muyc2 = muyc**2
  else
    muyc2 = YC2
  end if
  if (muyb /= 0) then
    muyb2 = muyb**2
  else
    muyb2 = YB2
  end if
  if (muyt /= 0) then
    muyt2 = muyt**2
  else
    muyt2 = YT2
  end if

  ! dim reg scale in UV-div loops
  mu2_UV = (x_UV**2)*mureg2
  mu2_IR = (x_IR**2)*mureg2

#ifdef PRECISION_dp
  ! initialise reduction libraries only in double precision
  ! (quad precision initialisation is handled within these libraries if applicable)

#ifdef USE_COLLIER
#ifdef COLLIER_LEGACY
  ! COLI initialisation
  if (a_switch == 1 .or. a_switch_rescue == 1 .or. a_switch == 2 .or. a_switch == 3) then
    if (coli_not_init) then
      call defcoli ! assign default values to parameters of loop library
      coli_not_init = .false.
      call unsetinfo_coli ! turn off printed information for coli parameters setting
    end if
    call setdeltauv_coli(de1_UV)
    call setdeltair_coli(de1_IR,de2_1_IR)
    call setmuuv2_coli(mu2_UV)
    call setmuir2_coli(mu2_IR)
! #else
!     write(*,*) 'ERROR: Collier (Coli) is deactivated.'
  end if

  ! DD initialisation
  if (a_switch == 7 .or. a_switch_rescue == 7) then
    if (dd_not_init) then
      mp2 = 0
!     cacc         threshold precision to activate 3-point alternative reductions
!     dacc         threshold precision to activate 4-point alternative reductions
!     mode34 = 2   PV or alternative 3/4-point reductions
!     mode34 = 0   PV 3/4-point reduction only
!     mode5  = 0   best 5-point reduction
!     mode6  = 0   best 6-point reduction
!     outlevel = 0 no output
      call dd_setmode(C_PV_threshold,D_PV_threshold,dd_red_mode,0,0,0) ! cacc,dacc,mode34,mode5,mode6,outlevel
      dd_not_init = .false.
    end if
    call dd_setparam(de1_UV,mu2_UV,de2_1_IR,de1_IR,mu2_IR,mp2)
! #else
!     write(*,*) 'ERROR: Collier (DD) is deactivated.'
  end if
! #ifdef COLLIER_LEGACY
#else
  if (a_switch == 1 .or. a_switch_rescue == 1 .or. a_switch == 2 .or. a_switch == 3 .or. &
    & a_switch == 7 .or. a_switch_rescue == 7) then
    if (maxpoint > maxpoint_active .or. maxrank > maxrank_active .or. cll_channels > cll_channels_active) then
      if (maxpoint > maxpoint_active .or. maxrank > maxrank_active) then
        if (nosplash) call stdout_off()
        if (cll_log == 0) then
          call init_cll(maxpoint, rmax=maxrank, folder_name="", noreset=.true.)
        else
          call init_cll(maxpoint, rmax=maxrank, noreset=.true.)
        end if
        if (nosplash) call stdout_on()
      end if
      if (coli_cache_use /= 0) then
        ! cache channel number in OL is per process; cll requires caches per reduction library (coli/dd)
        call initcachesystem_cll(2*cll_channels,maxpoint)
        cll_channels_active = cll_channels
      end if
      maxpoint_active = maxpoint
      maxrank_active = maxrank
    end if
    if (a_switch == 1) call setmode_cll(1)
    if (a_switch == 7) call setmode_cll(2)
    call setmuuv2_cll(mu2_UV)
    call setmuir2_cll(mu2_IR)
    call setdeltauv_cll(de1_UV)
    call setdeltair_cll(de1_IR,de2_1_IR)
    call settenred_cll(cll_tenred)
    call setaccuracy_cll(cll_pvthr,cll_accthr,cll_mode3thr)
    if (cll_log == 2) call initmonitoring_cll()
  end if
! #ifdef COLLIER_LEGACY
#endif
! #ifdef USE_COLLIER
#endif

  ! Initialisation of CutTools
  if ((a_switch == 5 .or. a_switch_rescue == 5) .and. cuttools_not_init) then
#ifdef USE_CUTTOOLS
    if (nosplash) call stdout_off()
    call ctsinit(opplimitvalue, oppscaloop, .true.)
    if (nosplash) call stdout_on()
    cuttools_not_init = .false.
! #else
!     write(*,*) 'ERROR: CutTools is deactivated.'
#endif
  end if
  ! Initialisation of Samurai
  if ((a_switch == 6 .or. a_switch_rescue == 6) .and. samurai_not_init) then
#if defined(USE_SAMURAI) && defined(PRECISION_dp)
    call initsamurai(set_imeth, set_isca, set_verbosity, set_itest)
    samurai_not_init = .false.
! #else
!     write(*,*) 'ERROR: Samurai is deactivated.'
#endif
  end if
  ! Set AvH OneLOop parameters
  if (a_switch == 5 .or. a_switch == 6 .or. a_switch_rescue == 5 .or. a_switch_rescue == 6) then
#ifdef USE_ONELOOP
    ! Silencing with stdout_off() not necessary, because CutTools/Samurai already called olo routines.
    if (reset_opp) then
      if (nosplash) call stdout_off()
      call olo_unit(-1)
      if (nosplash) call stdout_on()
      olodebug_unit = -1
      if (olo_verbose > 0) call olo_unit(olo_outunit, "error")
      if (olo_verbose > 1) call olo_unit(olo_outunit, "warning")
      if (olo_verbose > 2) then
        call olo_unit(olo_outunit, "message")
        olodebug_unit = olo_outunit
      end if
      if (olo_verbose > 3) call olo_unit(olo_outunit, "printall")
      call olo_onshell(oppthrs)
      reset_opp = .false.
    end if
    if (reset_mureg) then
      call olo_scale(mureg)
      reset_mureg = .false.
    end if
! #else
!     write(*,*) 'ERROR: CutTools and Samurai are both deactivated.'
#endif
  end if

  ! Initialisation of BuildTensors library
  if (tensorlib_not_init .and. (a_switch == 1 .or. a_switch == 2 .or. a_switch == 3 .or. a_switch == 7 &
  & .or. a_switch_rescue == 1 .or. a_switch_rescue == 7)) then
#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
    call tensor_ints_init()
    tensorlib_not_init = .false.
! #else
!     write(*,*) 'ERROR: Collier (BuildTensors) is deactivated.'
#endif
  end if

! ifdef PRECISION_dp
#else

  ! DD qp initialisation
!  if (a_switch == 7 .or. a_switch_rescue == 7) then
  if ( redlib_qp == 7 ) then
#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
    if (dd_qp_not_init) then
      call dd_setmode(1._qp, 1._qp, 0, 0, 0, 0)
      dd_qp_not_init = .false.
    end if
    if (tensorlib_qp_not_init) then
      call tensor_ints_init()
      tensorlib_qp_not_init = .false.
    end if
    call dd_setparam(de1_UV, mu2_UV, de2_1_IR, de1_IR, mu2_IR, [0,0,0,0,0,0,0,0,0,0]*0._qp)
#endif
  end if

! ifdef PRECISION_dp
#endif

  call qcd_renormalisation
  if (do_ew_renorm /= 0) then
    call ew_renormalisation
  end if

  ! Increment number of time this function has been called:
#ifdef PRECISION_dp
  loop_parameters_status = loop_parameters_status + 1
#else
  loop_parameters_status = loop_parameters_status_dp
#endif

end subroutine loop_parameters_init



subroutine ensure_mp_loop_init()
  ! synchronise non-dp parameters with dp if they are not up to date
  ! should be called after loop_parameters_init()
  ! and in loop matrix element routines before anything is done
#ifndef PRECISION_dp
  use ol_parameters_decl_/**/REALKIND, only: parameters_status
  use ol_loop_parameters_decl_/**/REALKIND, only: loop_parameters_status
  use ol_parameters_decl_/**/DREALKIND, only: &
    & parameters_status_dp => parameters_status
  use ol_loop_parameters_decl_/**/DREALKIND, only: &
    & loop_parameters_status_dp => loop_parameters_status
  implicit none
  if (parameters_status_dp /= parameters_status) &
    & call parameters_init()
  if (loop_parameters_status_dp /= loop_parameters_status) &
    & call loop_parameters_init()
#endif
end subroutine ensure_mp_loop_init



!#ifdef PRECISION_dp
!subroutine parameters_write(filename) bind(c,name="ol_parameters_write")
!#else
subroutine parameters_write(filename)
!#endif
  use, intrinsic :: iso_fortran_env, only : stdout=>output_unit
  use KIND_TYPES, only: REALKIND
  use ol_generic, only: to_string
  use ol_debug, only: ol_error, ol_msg
  use ol_parameters_decl_/**/REALKIND
#ifndef PRECISION_dp
  use ol_parameters_decl_/**/DREALKIND, only: model, ew_scheme, ew_renorm_scheme
#endif
  use ol_loop_parameters_decl_/**/REALKIND
  implicit none
  character(len=*), optional :: filename
  integer :: outid, ios
  outid = stdout
  if (present(filename)) then
    if (len_trim(filename) > 0) then
      outid = 10
      open(outid, file=filename, status="replace", iostat=ios)
      if (ios /= 0) then
        call ol_error("ol_printparameter: error opening file " // trim(filename))
        call ol_msg("iostat =" // to_string(ios))
        return
      end if
    end if
  end if

  write(outid,*) '===================================================='
  write(outid,*) '================OpenLoops Parameters================'
  write(outid,*) '===================================================='
  write(outid,*) 'model =', trim(model)
  write(outid,*)
  write(outid,*) 'coupling constants'
  write(outid,*) 'alpha_s      =', alpha_QCD
  write(outid,*) 'alpha_qed    =', alpha_QED,    '  1/alpha_qed    =', 1/alpha_QED
  write(outid,*)
  write(outid,*) 'ew_scheme    =', ew_scheme
  write(outid,*) 'alpha_qed_0  =', alpha_QED_0,  '  1/alpha_qed_0  =', 1/alpha_QED_0
  write(outid,*) 'alpha_qed_MZ =', alpha_QED_MZ, '  1/alpha_qed_MZ =', 1/alpha_QED_MZ
  write(outid,*) 'Gmu          =', Gmu
  write(outid,*)
  write(outid,*) 'derived couplings'
  write(outid,*) 'sw           =', sw,           '  sw2            =', sw2
  write(outid,*) 'vev          =', 2*MW*sw/eQED
  if (trim(model) == "2hdm") then
    write(outid,*)
    write(outid,*) '2HDM tan(beta) =', thdmTB
    write(outid,*) '2HDM sin(beta-alpha) =', thdmSBA
  end if
  write(outid,*)
  write(outid,*) 'particle masses and widths'
  write(outid,*) 'ME = ', ME, 'rME =', rME, 'wME =', wMU, 'YE =', YE
  write(outid,*) 'MM = ', MM, 'rMM =', rMM, 'wMM =', wMU, 'YM =', YM
  write(outid,*) 'ML = ', ML, 'rML =', rML, 'wML =', wMU, 'YL =', YL
  write(outid,*) 'MU = ', MU, 'rMU =', rMU, 'wMU =', wMU, 'YU =', YU
  write(outid,*) 'MD = ', MD, 'rMD =', rMD, 'wMD =', wMD, 'YD =', YD
  write(outid,*) 'MS = ', MS, 'rMS =', rMS, 'wMS =', wMS, 'YS =', YS
  write(outid,*) 'MC = ', MC, 'rMC =', rMC, 'wMC =', wMC, 'YC =', YC
  write(outid,*) 'MB = ', MB, 'rMB =', rMB, 'wMB =', wMB, 'YB =', YB
  write(outid,*) 'MT = ', MT, 'rMT =', rMT, 'wMT =', wMT, 'YT =', YT
  write(outid,*) 'MW = ', MW, 'rMW =', rMW, 'wMW =', wMW
  write(outid,*) 'MZ = ', MZ, 'rMZ =', rMZ, 'wMZ =', wMZ
  write(outid,*) 'MH = ', MH, 'rMH =', rMH, 'wMH =', wMH
  write(outid,*) 'MX = ', MX, 'rMX =', rMX, 'wMX =', wMX
  write(outid,*) 'MY = ', MY, 'rMY =', rMY, 'wMY =', wMY
  if (trim(model) == "2hdm") then
    write(outid,*) 'MA0 = ', MA0, 'rMA0 =', rMA0, 'wMA0 =', wMA0
    write(outid,*) 'MHH = ', MHH, 'rMHH =', rMHH, 'wMHH =', wMHH
    write(outid,*) 'MHp = ', MHp, 'rMHp =', rMHp, 'wMHp =', wMHp
  end if
  if (trim(model) == "higgspo") then
    write(outid,*)
    write(outid,*) '==Higgs PO effective couplings=='
    write(outid,*) 'vev     = ', HPOvev
    write(outid,*) 'kapZZ   = ', HPOkapZZ,             'kapWW   = ', HPOkapWW
    write(outid,*) 'epsZZ   = ', HPOepsZZ,             'aepsZZ  = ',HPOaepsZZ
    write(outid,*) 'epsWW   = ', HPOepsWW,             'aepsWW  = ', HPOaepsWW
    write(outid,*) 'epsAA   = ', HPOepsAA,             'aepsAA  = ', HPOaepsAA
    write(outid,*) 'epsZA   = ', HPOepsZA,             'aepsZA  = ', HPOaepsZA
    write(outid,*) 'epsZuR  = ', real(HPOepsZuu(1,1)), 'epsZuL  = ', real(HPOepsZuu(1,2))
    write(outid,*) 'epsZdR  = ', real(HPOepsZdd(1,1)), 'epsZdL  = ', real(HPOepsZdd(1,2))
    write(outid,*) 'epsZcR  = ', real(HPOepsZuu(2,1)), 'epsZcL  = ', real(HPOepsZuu(2,2))
    write(outid,*) 'epsZsR  = ', real(HPOepsZdd(2,1)), 'epsZsL  = ', real(HPOepsZdd(2,2))
    write(outid,*) 'epsZtR  = ', real(HPOepsZuu(3,1)), 'epsZtL  = ', real(HPOepsZuu(3,2))
    write(outid,*) 'epsZbR  = ', real(HPOepsZdd(3,1)), 'epsZbL  = ', real(HPOepsZdd(3,2))
    write(outid,*) 'epsZneR = ', real(HPOepsZnn(1,1)), 'epsZneL = ', real(HPOepsZnn(1,2))
    write(outid,*) 'epsZeR  = ', real(HPOepsZll(1,1)), 'epsZeL  = ', real(HPOepsZll(1,2))
    write(outid,*) 'epsZnmR = ', real(HPOepsZnn(2,1)), 'epsZnmL = ', real(HPOepsZnn(2,2))
    write(outid,*) 'epsZmR  = ', real(HPOepsZll(2,1)), 'epsZmL  = ', real(HPOepsZll(2,2))
    write(outid,*) 'epsZnlR = ', real(HPOepsZnn(3,1)), 'epsZnlL = ', real(HPOepsZnn(3,2))
    write(outid,*) 'epsZlR  = ', real(HPOepsZll(3,1)), 'epsZlL  = ', real(HPOepsZll(3,2))
    write(outid,*) 'epsWlne = ', HPOepsWln(1),         'epsWdu  = ', HPOepsWqq(1)
    write(outid,*) 'epsWlnm = ', HPOepsWln(2),         'epsWsc  = ', HPOepsWqq(2)
    write(outid,*) 'epsWlnl = ', HPOepsWln(3),         'epsWbt  = ', HPOepsWqq(3)
  end if

  write(outid,*)
    write(outid,*) '==Technical Parameters=='
  write(outid,*) 'muren             =', muren
  write(outid,*) 'mureg             =', mureg
  write(outid,*) 'pole1_UV          =', de1_UV
  write(outid,*) 'pole1_IR          =', de1_IR
  write(outid,*) 'pole2_IR          =', de2_i_IR
  write(outid,*) 'fact_UV           =', x_UV
  write(outid,*) 'fact_IR           =', x_IR
  write(outid,*) 'ew_renorm_scheme  =', ew_renorm_scheme
#ifdef PRECISION_dp
  write(outid,*) 'N_quarks          =', nf
  write(outid,*) 'light quarks      =', N_lf
  write(outid,*) 'nq_nondecoupled   =', nq_nondecoupl
  write(outid,*) 'fermion_loops     =', SwF
  write(outid,*) 'nonfermion_loops  =', SwB
  write(outid,*) 'CT_on             =', CT_is_on
  write(outid,*) 'R2_on             =', R2_is_on
  write(outid,*) 'IR_on             =', IR_is_on
  write(outid,*) 'polecheck         =', polecheck_is
  write(outid,*) 'polenorm_swi      =', norm_swi
  write(outid,*) 'i-operator mode   =', ioperator_mode
  write(outid,*) 'last_switch       =', l_switch
  write(outid,*) 'ew_renorm_switch  =', ew_renorm_switch
  write(outid,*) 'use_coli_cache    =', coli_cache_use
  write(outid,*) 'use_me_cache      =', use_me_cache
  write(outid,*) 'check_Ward_tree   =', Ward_tree
  write(outid,*) 'check_Ward_loop   =', Ward_loop
  write(outid,*) 'out_symmetry      =', out_symmetry_on
  write(outid,*) 'stability_mode         =', stability_mode
  write(outid,*) 'deviation_mode         =', deviation_mode
  write(outid,*) 'stability_triggerratio =', trigeff_targ
  write(outid,*) 'stability_unstable     =', abscorr_unst
  write(outid,*) 'stability_kill         =', ratcorr_bad
  write(outid,*) 'stability_kill2        =', ratcorr_bad_L2
  write(outid,*) 'redlib1                =', a_switch
  write(outid,*) 'redlib2                =', a_switch_rescue
  write(outid,*) 'redlib_qp              =', redlib_qp
  write(outid,*)
  write(outid,*) '===================================================='
#endif
! opp_rootsvalue, opp_limitvalue, opp_thrs, opp_idig, opp_scaloop
! sam_isca, sam_verbosity, sam_itest
! set_C_PV_threshold, set_D_PV_threshold, set_dd_red_mode

  if (outid == 10) then
    call ol_msg("Parameters written to file " // trim(filename))
    close(outid, iostat=ios)
    if (ios /= 0) then
      call ol_error("Error writing parameters to file " // trim(filename))
      call ol_msg("iostat =" // to_string(ios))
      return
    end if
  end if
end subroutine parameters_write

end module ol_parameters_init_/**/REALKIND
