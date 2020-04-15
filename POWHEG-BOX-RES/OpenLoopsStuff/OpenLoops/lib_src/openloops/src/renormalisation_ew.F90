
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


module ol_ew_renormalisation_/**/REALKIND
  use KIND_TYPES, only: REALKIND
  implicit none
  complex(REALKIND), save      ::   IRrational = -1 ! Rational contribution from IR divergent fermion self energies
  contains

! **********************************************************************
subroutine ew_renormalisation
! **********************************************************************
! EW renormalisation and R2 constants (in physical GeV units);
! conventions for UV/IR div. see subroutine loop_parameters_init.
! This subroutine is automatically (once) called by loop_parameters_init.
! **********************************************************************
  use KIND_TYPES, only: REALKIND
  use ol_debug, only: ol_msg, ol_error, ol_fatal
  use ol_generic, only: to_string
  use ol_parameters_decl_/**/REALKIND
#ifndef PRECISION_dp
  use ol_parameters_decl_/**/DREALKIND, only: LeadingColour, ew_renorm_scheme, cms_on, model
#endif
  use ol_loop_parameters_decl_/**/REALKIND
#ifndef PRECISION_dp
  use ol_loop_parameters_decl_/**/DREALKIND, only: &
    & nc, nf, N_lf, N_lu, N_ld, N_ll, nq_nondecoupl, CT_is_on, R2_is_on, TP_is_on, SwF, SwB
#endif
  implicit none

  real(REALKIND) :: deB_UV, deB_IR, deT_UV, deT_IR
  real(REALKIND) :: eps=1.e-17
  logical :: zeromasses(6)  ! maximal allowed number of quarks
  integer :: debug_ew_renorm = 0
#ifndef PRECISION_dp
  integer, parameter :: dp = selected_real_kind(15)
#endif

!for debugging with ABC
  real(REALKIND), save         :: debug_norm = 1._/**/REALKIND


! self energies
  complex(REALKIND), save      ::   Tadpole   = 0
  complex(REALKIND), save      ::   SiW    = 0
  complex(REALKIND), save      ::   SiW0  = 0
  complex(REALKIND), save      ::   dSiW   = 0
  complex(REALKIND), save      ::   SiZZ   = 0
  complex(REALKIND), save      ::   dSiZZ  = 0
  complex(REALKIND), save      ::   SiAZZ  = 0
  complex(REALKIND), save      ::   SiAZ0  = 0
  complex(REALKIND), save      ::   dSiAAheavy0  = 0
  complex(REALKIND), save      ::   dSiAA0  = 0
  complex(REALKIND), save      ::   PiAAlightZ  = 0
  complex(REALKIND), save      ::   dAlphaQED_MZ = 0
  complex(REALKIND), save      ::   dSiAAZ  = 0
  complex(REALKIND), save      ::   SiH    = 0
  complex(REALKIND), save      ::   dSiH   = 0
  complex(REALKIND), save      ::   SitL   = 0
  complex(REALKIND), save      ::   SitR   = 0
  complex(REALKIND), save      ::   SitS   = 0
  complex(REALKIND), save      ::   dSitL  = 0
  complex(REALKIND), save      ::   dSitR  = 0
  complex(REALKIND), save      ::   dSitS  = 0
  complex(REALKIND), save      ::   SibL   = 0
  complex(REALKIND), save      ::   SibR   = 0
  complex(REALKIND), save      ::   SibS   = 0
  complex(REALKIND), save      ::   dSibL  = 0
  complex(REALKIND), save      ::   dSibR  = 0
  complex(REALKIND), save      ::   dSibS  = 0
  complex(REALKIND), save      ::   SiuL   = 0
  complex(REALKIND), save      ::   SiuR   = 0
  complex(REALKIND), save      ::   SidL   = 0
  complex(REALKIND), save      ::   SidR   = 0
  complex(REALKIND), save      ::   SieL   = 0
  complex(REALKIND), save      ::   SieR   = 0
  complex(REALKIND), save      ::   SinL   = 0
  complex(REALKIND), save      ::   SilL   = 0
  complex(REALKIND), save      ::   SilR   = 0
  complex(REALKIND), save      ::   SilS   = 0
  complex(REALKIND), save      ::   dSilL  = 0
  complex(REALKIND), save      ::   dSilR  = 0
  complex(REALKIND), save      ::   dSilS  = 0

  complex(REALKIND), save      ::   dSitLRS = 0
  complex(REALKIND), save      ::   dSibLRS = 0

! one-point functions
  complex(REALKIND), save      ::   A0W = 0
  complex(REALKIND), save      ::   A0Z = 0
  complex(REALKIND), save      ::   A0H = 0
  complex(REALKIND), save      ::   A0T = 0
  complex(REALKIND), save      ::   A0B = 0

! two-point
  complex(REALKIND), save      ::  B0000   = 0
  complex(REALKIND), save      ::  B00WW   = 0
  complex(REALKIND), save      ::  dB00WW  = 0
  complex(REALKIND), save      ::  B00W0   = 0
  complex(REALKIND), save      ::  dB00W0  = 0
  complex(REALKIND), save      ::  B0WW0   = 0
  complex(REALKIND), save      ::  dB0WW0  = 0
  complex(REALKIND), save      ::  B0ZWW   = 0
  complex(REALKIND), save      ::  dB0ZWW  = 0
  complex(REALKIND), save      ::  B00HH   = 0
  complex(REALKIND), save      ::  B00ZZ   = 0
  complex(REALKIND), save      ::  B0ZZH   = 0
  complex(REALKIND), save      ::  dB0ZZH  = 0
  complex(REALKIND), save      ::  B00ZH   = 0
  complex(REALKIND), save      ::  B00WH   = 0
  complex(REALKIND), save      ::  dB00WH  = 0
  complex(REALKIND), save      ::  B0WWH   = 0
  complex(REALKIND), save      ::  dB0WWH  = 0
  complex(REALKIND), save      ::  B00WZ   = 0
  complex(REALKIND), save      ::  dB00WZ  = 0
  complex(REALKIND), save      ::  B0WWZ   = 0
  complex(REALKIND), save      ::  dB0WWZ  = 0
  complex(REALKIND), save      ::  B0HHH   = 0
  complex(REALKIND), save      ::  dB0HHH  = 0
  complex(REALKIND), save      ::  B0HWW   = 0
  complex(REALKIND), save      ::  dB0HWW  = 0
  complex(REALKIND), save      ::  B0HZZ   = 0
  complex(REALKIND), save      ::  dB0HZZ  = 0
  complex(REALKIND), save      ::  B0BTW   = 0
  complex(REALKIND), save      ::  dB0BTW  = 0
  complex(REALKIND), save      ::  B0TBW   = 0
  complex(REALKIND), save      ::  dB0TBW  = 0
  complex(REALKIND), save      ::  B0WTB   = 0
  complex(REALKIND), save      ::  dB0WTB  = 0
  complex(REALKIND), save      ::  B1TBW   = 0
  complex(REALKIND), save      ::  dB1TBW  = 0
  complex(REALKIND), save      ::  B1BTW   = 0
  complex(REALKIND), save      ::  dB1BTW  = 0
  complex(REALKIND), save      ::  B0TT0   = 0
  complex(REALKIND), save      ::  dB0TT0  = 0
  complex(REALKIND), save      ::  B00TT   = 0
  complex(REALKIND), save      ::  dB00TT  = 0
  complex(REALKIND), save      ::  B1TT0   = 0
  complex(REALKIND), save      ::  dB1TT0  = 0
  complex(REALKIND), save      ::  B0TTZ   = 0
  complex(REALKIND), save      ::  dB0TTZ  = 0
  complex(REALKIND), save      ::  B1TTZ   = 0
  complex(REALKIND), save      ::  dB1TTZ  = 0
  complex(REALKIND), save      ::  B0ZTT  = 0
  complex(REALKIND), save      ::  dB0ZTT  = 0
  complex(REALKIND), save      ::  B0TTH   = 0
  complex(REALKIND), save      ::  dB0TTH  = 0
  complex(REALKIND), save      ::  B0HTT   = 0
  complex(REALKIND), save      ::  dB0HTT  = 0
  complex(REALKIND), save      ::  B1TTH   = 0
  complex(REALKIND), save      ::  dB1TTH  = 0
  complex(REALKIND), save      ::  B0BB0   = 0
  complex(REALKIND), save      ::  dB0BB0  = 0
  complex(REALKIND), save      ::  B00BB   = 0
  complex(REALKIND), save      ::  dB00BB  = 0
  complex(REALKIND), save      ::  B1BB0   = 0
  complex(REALKIND), save      ::  dB1BB0  = 0
  complex(REALKIND), save      ::  B0BBZ   = 0
  complex(REALKIND), save      ::  dB0BBZ  = 0
  complex(REALKIND), save      ::  B1BBZ   = 0
  complex(REALKIND), save      ::  dB1BBZ  = 0
  complex(REALKIND), save      ::  B0BBH   = 0
  complex(REALKIND), save      ::  dB0BBH  = 0
  complex(REALKIND), save      ::  B0HBB   = 0
  complex(REALKIND), save      ::  dB0HBB  = 0
  complex(REALKIND), save      ::  B1BBH   = 0
  complex(REALKIND), save      ::  dB1BBH  = 0
  complex(REALKIND), save      ::  B00TB   = 0
  complex(REALKIND), save      ::  dB00TB  = 0
  complex(REALKIND), save      ::  B100W   = 0
  complex(REALKIND), save      ::  B1000   = 0
  complex(REALKIND), save      ::  B100Z   = 0
  complex(REALKIND), save      ::  B0Z00   = 0
  complex(REALKIND), save      ::  dB0Z00  = 0
  complex(REALKIND), save      ::  B0W00   = 0
  complex(REALKIND), save      ::  dB0W00  = 0
  complex(REALKIND), save      ::  B0ZBB   = 0
  complex(REALKIND), save      ::  dB0ZBB  = 0



  complex(REALKIND), save      ::   cTW = 0
  complex(REALKIND), save      ::   cTZ = 0
  complex(REALKIND), save      ::   cTH = 0
  complex(REALKIND), save      ::   cTT = 0
  complex(REALKIND), save      ::   cTB = 0

!  complex(REALKIND), save      ::   lambda  = 0   ! fictous photon mass. Not used atm.

  complex(REALKIND), save      ::   dZuLPole   = 0.
  complex(REALKIND), save      ::   dZuRPole   = 0.
  complex(REALKIND), save      ::   dZtLPole   = 0.
  complex(REALKIND), save      ::   dZtRPole   = 0.

  complex(REALKIND), save      ::   MREG2         ! light quark mass^2 regulator for dZAA

  complex(REALKIND), save      ::   dZeQEDEWPole, dcwEWPole, dswEWPole,dZAAEWPole, dZZAEWPole, dZAZEWPole
  complex(REALKIND), save      ::   dZMZ2EWPole, dZMW2EWPole, dZZZEWPole, dZWEWPole


  if (LeadingColour == 0) then
    cf = (nc**2-1)/(2.*nc)
    ca = nc
    tf = 0.5
  else
    cf = 0.5*nc
    ca = nc
    tf = 0
  end if

  zeromasses = [MU == 0, MD == 0, MS == 0, MC == 0, MB == 0, MT == 0]
  N_lf = count(zeromasses(:nf))

  zeromasses(1:3) = [MU == 0, MC == 0, MT == 0]
  N_lu = count(zeromasses(:3))

  zeromasses(1:3) = [MD == 0, MS == 0, MB == 0]
  N_ld = count(zeromasses(:3))

  zeromasses(1:3) = [ME == 0, MM == 0, ML == 0]
  N_ll = count(zeromasses(:3))

  Qf2sum = nc*N_lu*Qu2+nc*N_ld*Qd2+N_ll*Ql2

  if (N_lf /= 4 .and. N_lf /= 5) then
    call ol_error(2, 'in ew_renormalisation:')
    call ol_msg( 'N_lf = ' // to_string(N_lf) // 'is not supported.')
    call ol_fatal()
  end if

  Tadpole   = 0.
  SiW    = 0.
  SiW0   = 0.
  dSiW   = 0.
  SiZZ   = 0.
  dSiZZ  = 0.
  SiAZZ  = 0.
  SiAZ0  = 0.
  dSiAAheavy0  = 0.
  dSiAA0 = 0.
  PiAAlightZ  = 0.
  dSiAAZ  = 0.
  SiH    = 0.
  dSiH   = 0.
  SitL   = 0.
  SitR   = 0.
  SitS   = 0.
  dSitL  = 0.
  dSitR  = 0.
  dSitS  = 0.
  SibL   = 0.
  SibR   = 0.
  SibS   = 0.
  dSibL  = 0.
  dSibR  = 0.
  dSibS  = 0.
  SiuL   = 0.
  SiuR   = 0.
  SidL   = 0.
  SidR   = 0.
  SieL   = 0.
  SieR   = 0.
  SinL   = 0.
  SilL   = 0.
  SilR   = 0.
  SilS   = 0.
  dSilL  = 0.
  dSilR  = 0.
  dSilS  = 0.


! Do not use complex masses if CMS is not used --> only for debug & model=sm_vaux
  if ( cms_on == 0 ) then
    call masspowers(rME, 0._/**/REALKIND, ME, ME2, rME2)
    call masspowers(rMM, 0._/**/REALKIND, MM, MM2, rMM2)
    call masspowers(rML, 0._/**/REALKIND, ML, ML2, rML2)
    call masspowers(rMU, 0._/**/REALKIND, MU, MU2, rMU2)
    call masspowers(rMD, 0._/**/REALKIND, MD, MD2, rMD2)
    call masspowers(rMS, 0._/**/REALKIND, MS, MS2, rMS2)
    call masspowers(rMC, 0._/**/REALKIND, MC, MC2, rMC2)
    call masspowers(rMB, 0._/**/REALKIND, MB, MB2, rMB2)
    call masspowers(rMT, 0._/**/REALKIND, MT, MT2, rMT2)
    call masspowers(rMW, 0._/**/REALKIND, MW, MW2, rMW2)
    call masspowers(rMZ, 0._/**/REALKIND, MZ, MZ2, rMZ2)
    call masspowers(rMH, 0._/**/REALKIND, MH, MH2, rMH2)
  end if


  ! calculate one- and two-point functions
  A0W = calcA0(MW2)
  A0Z = calcA0(MZ2)
  A0H = calcA0(MH2)
  A0T = calcA0(MT2)
  A0B = calcA0(MB2)

  B0000   = calcB0(ZERO,ZERO,ZERO)
  B00WW   = calcB0(ZERO,MW2,MW2)
  dB00WW  = calcdB0(ZERO,MW2,MW2)
  B00W0   = calcB0(ZERO,MW2,ZERO)
  dB00W0  = calcdB0(ZERO,MW2,ZERO)
  B0WW0   = calcB0(MW2,MW2,ZERO)
  dB0WW0  = calcdB0(MW2,MW2,ZERO)
  B0ZWW   = calcB0(MZ2,MW2,MW2)
  dB0ZWW  = calcdB0(MZ2,MW2,MW2)
  B00HH   = calcB0(ZERO,MH2,MH2)
  B00ZZ   = calcB0(ZERO,MZ2,MZ2)
  B0ZZH   = calcB0(MZ2,MZ2,MH2)
  dB0ZZH  = calcdB0(MZ2,MZ2,MH2)
  B00ZH   = calcB0(ZERO,MZ2,MH2)
  B00WH   = calcB0(ZERO,MW2,MH2)
  dB00WH  = calcdB0(ZERO,MW2,MH2)
  B0WWH   = calcB0(MW2,MW2,MH2)
  dB0WWH  = calcdB0(MW2,MW2,MH2)
  B00WZ   = calcB0(ZERO,MW2,MZ2)
  dB00WZ  = calcdB0(ZERO,MW2,MZ2)
  B0WWZ   = calcB0(MW2,MW2,MZ2)
  dB0WWZ  = calcdB0(MW2,MW2,MZ2)
  B0HHH   = calcB0(MH2,MH2,MH2)
  dB0HHH  = calcdB0(MH2,MH2,MH2)
  B0HWW   = calcB0(MH2,MW2,MW2)
  dB0HWW  = calcdB0(MH2,MW2,MW2)
  B0HZZ   = calcB0(MH2,MZ2,MZ2)
  dB0HZZ  = calcdB0(MH2,MZ2,MZ2)
  B0BTW   = calcB0(MB2,MT2,MW2)
  dB0BTW  = calcdB0(MB2,MT2,MW2)
  B0TBW   = calcB0(MT2,MB2,MW2)
  dB0TBW  = calcdB0(MT2,MB2,MW2)
  B0WTB   = calcB0(MW2,MT2,MB2)
  dB0WTB  = calcdB0(MW2,MT2,MB2)
  B1TBW   = calcB1(MT2,MB2,MW2)
  dB1TBW  = calcdB1(MT2,MB2,MW2)
  B1BTW   = calcB1(MB2,MT2,MW2)
  dB1BTW  = calcdB1(MB2,MT2,MW2)
  B0TT0   = calcB0(MT2,MT2,ZERO)
  dB0TT0  = calcdB0(MT2,MT2,ZERO)
  B00TT   = calcB0(ZERO,MT2,MT2)
  dB00TT  = calcdB0(ZERO,MT2,MT2)
  B1TT0   = calcB1(MT2,MT2,ZERO)
  dB1TT0  = calcdB1(MT2,MT2,ZERO)
  B0TTZ   = calcB0(MT2,MT2,MZ2)
  dB0TTZ  = calcdB0(MT2,MT2,MZ2)
  B1TTZ   = calcB1(MT2,MT2,MZ2)
  dB1TTZ  = calcdB1(MT2,MT2,MZ2)
  B0ZTT   = calcB0(MZ2,MT2,MT2)
  dB0ZTT  = calcdB0(MZ2,MT2,MT2)
  B0TTH   = calcB0(MT2,MT2,MH2)
  dB0TTH  = calcdB0(MT2,MT2,MH2)
  B0HTT   = calcB0(MH2,MT2,MT2)
  dB0HTT  = calcdB0(MH2,MT2,MT2)
  B1TTH   = calcB1(MT2,MT2,MH2)
  dB1TTH  = calcdB1(MT2,MT2,MH2)
  B0BB0   = calcB0(MB2,MB2,ZERO)
  dB0BB0  = calcdB0(MB2,MB2,ZERO)
  B00BB   = calcB0(ZERO,MB2,MB2)
  dB00BB  = calcdB0(ZERO,MB2,MB2)
  B1BB0   = calcB1(MB2,MB2,ZERO)
  dB1BB0  = calcdB1(MB2,MB2,ZERO)
  B0BBZ   = calcB0(MB2,MB2,MZ2)
  dB0BBZ  = calcdB0(MB2,MB2,MZ2)
  B1BBZ   = calcB1(MB2,MB2,MZ2)
  dB1BBZ  = calcdB1(MB2,MB2,MZ2)
  B0BBH   = calcB0(MB2,MB2,MH2)
  dB0BBH  = calcdB0(MB2,MB2,MH2)
  B0HBB   = calcB0(MH2,MB2,MB2)
  dB0HBB  = calcdB0(MH2,MB2,MB2)
  B1BBH   = calcB1(MB2,MB2,MH2)
  dB1BBH  = calcdB1(MB2,MB2,MH2)
  B00TB   = calcB0(ZERO,MT2,MB2)
  dB00TB  = calcdB0(ZERO,MT2,MB2)
  B100W   = calcB1(ZERO,ZERO,MW2)
  B1000   = calcB1(ZERO,ZERO,ZERO)
  B100Z   = calcB1(ZERO,ZERO,MZ2)
  B0Z00   = calcB0(MZ2,ZERO,ZERO)
  dB0Z00  = calcdB0(MZ2,ZERO,ZERO)
  B0W00   = calcB0(MW2,ZERO,ZERO)
  dB0W00  = calcdB0(MW2,ZERO,ZERO)
  B0ZBB   = calcB0(MZ2,MB2,MB2)
  dB0ZBB  = calcdB0(MZ2,MB2,MB2)

  ! calculate renormalisation constants
    if (SwB /= 0 .and. CT_is_on /= 0) then
    ! non-fermionic!

    !Bosonic Tadpole. Agrees with eq. 12 in NP B 383 (1992) 73
    Tadpole   = 0.75*MH2/MW/sw*A0H                      &
              + (0.5*MH2/MW/sw+3.*MW/sw)*A0W            &
              + (0.25*MH2/MW/sw + 1.5*MW/sw/cw2)*A0Z

    !This is the bosonic part of page 105-107 from Denner92 evaluated in selfenergies.nb

    dSiAAheavy0=dSiAAheavy0-3*B00WW-4*MW2*dB00WW
    dSiAA0 = dSiAAheavy0

    if (ew_renorm_scheme == 2) then
      dSiAAZ=dSiAAZ-3*B0ZWW-(4*MW2+3*rMZ2)*dB0ZWW
    end if

    SiAZ0=SiAZ0+(2*MW2*B00WW)/(cw*sw)

    SiAZZ=SiAZZ+(rMZ2/3. - (-2 + 12*cw2)*MW2*B00WW &
        + ((4 + 12*cw2)*MW2 + (0.5 + 9*cw2)*rMZ2)*B0ZWW)/(3.*cw*sw)

    SiZZ=SiZZ-(((-1 + 4*cw2)*rMZ2)/3. - (2 - 8*cw2 + 24*cw4)*MW2*B00WW  &
        + ((-10 + 16*cw2 + 24*cw4)*MW2 + (-0.5 + 2*cw2 + 18*cw4)*rMZ2)*B0ZWW)/(6.*cw2*sw2) &
        - ((-2*rMZ2)/3. - 2*MH2*B00HH - 2*MZ2*B00ZZ + (2*MH2 - 10*MZ2 - rMZ2)*B0ZZH &
        - ((-MH2 + MZ2)**2*(-B00ZH + B0ZZH))/rMZ2)/(12.*cw2*sw2)

    dSiZZ=dSiZZ+(2._/**/REALKIND/3. &
        + ((MH2 - MZ2)**2*(B00ZH - B0ZZH))/rMZ2**2 + B0ZZH &
        + (2 - 8*cw2 - 3*(-1 + 4*cw2 + 36*cw4)*B0ZWW &
        - 3*(4*(-5 + 8*cw2 + 12*cw4)*MW2 + (-1 + 4*cw2 + 36*cw4)*rMZ2)*dB0ZWW)/3.  &
        - (2*MH2 - 10*MZ2 - rMZ2)*dB0ZZH &
        + ((MH2 - MZ2)**2*dB0ZZH)/rMZ2)/(12.*cw2*sw2)

    SiW=SiW+(-8*(rMW2/3. - 2*MW2*B00WW + (MW2**2*(B00W0 - B0WW0))/rMW2 &
        + (2*MW2 + 5*rMW2)*B0WW0) - ((-2*rMW2)/3. - 2*MH2*B00HH - 2*MW2*B00WW  &
        + ((MH2 - MW2)**2*(B00WH - B0WWH))/rMW2 + (2*MH2 - 10*MW2 - rMW2)*B0WWH)/sw2  &
        - ((2*(-1 + 4*cw2)*rMW2)/3. - 2*(1 + 8*cw2)*(MW2*B00WW + MZ2*B00ZZ) &
        + ((1 + 8*cw2)*(MW2 - MZ2)**2*(B00WZ - B0WWZ))/rMW2 &
        + ((54 - 10/cw2 + 16*cw2)*MW2 + (-1 + 40*cw2)*rMW2)*B0WWZ)/sw2)/12.

    dSiW=dSiW+(-2*(1._/**/REALKIND/3. + 5*B0WW0 + (MW2**2*(-B00W0 + B0WW0))/rMW2**2  &
        - (MW2**2*dB0WW0)/rMW2 + (2*MW2 + 5*rMW2)*dB0WW0))/3. &
        - (-2._/**/REALKIND/3. - B0WWH + ((-MH2 + MW2)**2*(-B00WH + B0WWH))/rMW2**2 &
        + (2*MH2 - 10*MW2 - rMW2)*dB0WWH - ((-MH2 + MW2)**2*dB0WWH)/rMW2)/(12.*sw2) &
        - ((2*(-1 + 4*cw2))/3. + (-1 + 40*cw2)*B0WWZ &
        + ((1 + 8*cw2)*(MW2 - MZ2)**2*(-B00WZ + B0WWZ))/rMW2**2 &
        - ((1 + 8*cw2)*(MW2 - MZ2)**2*dB0WWZ)/rMW2 + ((54 - 10/cw2 + 16*cw2)*MW2 &
        + (-1 + 40*cw2)*rMW2)*dB0WWZ)/(12.*sw2)

    if (ew_renorm_scheme == 1) then
      SiW0=SiW0+(-8*(2*MW2*B00W0 - 2*MW2*B00WW - MW2**2*dB00W0) &
          - (-2*MH2*B00HH + (2*MH2 - 10*MW2)*B00WH - 2*MW2*B00WW - (MH2 - MW2)**2*dB00WH)/sw2 &
          - ((54 - 10/cw2 + 16*cw2)*MW2*B00WZ - 2*(1 + 8*cw2)*(MW2*B00WW + MZ2*B00ZZ) &
          - (1 + 8*cw2)*(MW2 - MZ2)**2*dB00WZ)/sw2)/12.
    end if

    SiH=SiH+((3*MH2*(A0H + 3*MH2*B0HHH))/MW2 &
        + (2*(-12*MW2**2 + (MH2 + 6*MW2)*A0W  &
        + (MH2**2 + 12*MW2**2 - 4*MW2*rMH2)*B0HWW))/MW2 &
        + (-12*MZ2**2 + (MH2 + 6*MZ2)*A0Z  &
        + (MH2**2 + 12*MZ2**2 - 4*MZ2*rMH2)*B0HZZ)/(cw2*MZ2))/(8.*sw2)

    dSiH=dSiH+((9*MH2**2*lambdaHHH**2*dB0HHH)/MW2 + 4*(-2*B0HWW &
        + (MH2**2/(2.*MW2) + 6*MW2 - 2*rMH2)*dB0HWW) +(2*(-2*B0HZZ &
        + (MH2**2/(2.*MZ2) + 6*MZ2 - 2*rMH2)*dB0HZZ))/cw2)/(8.*sw2)

    SitL=SitL-(1 + (2 + MB2/MW2)*B1TBW)/(2.*sw2) - (4*(1 + 2*B1TT0))/9. &
        - (MT2*(B1TTH + B1TTZ))/(4.*MW2*sw2) - (1 + 2*B1TTZ)*gZu(2)**2

    SitR=SitR-(MT2*B1TBW)/(2.*MW2*sw2) - (4*(1 + 2*B1TT0))/9. &
        - (MT2*(B1TTH + B1TTZ))/(4.*MW2*sw2) - (1 + 2*B1TTZ)*gZu(1)**2

    SitS=SitS-(MB2*B0TBW)/(2.*MW2*sw2) - (4*(-2 + 4*B0TT0))/9. &
        - (MT2*(-B0TTH + B0TTZ))/(4.*MW2*sw2) - (-2 + 4*B0TTZ)*gZu(1)*gZu(2)

    dSitL=dSitL-((2 + MB2/MW2)*dB1TBW)/(2.*sw2) - (8*dB1TT0)/9. &
        - (MT2*(dB1TTH + dB1TTZ))/(4.*MW2*sw2) - 2*dB1TTZ*gZu(2)**2

    dSitR=dSitR-(MT2*dB1TBW)/(2.*MW2*sw2) - (8*dB1TT0)/9. &
        - (MT2*(dB1TTH + dB1TTZ))/(4.*MW2*sw2) - 2*dB1TTZ*gZu(1)**2

    dSitS=dSitS-(MB2*dB0TBW)/(2.*MW2*sw2) - (16*dB0TT0)/9. &
        - (MT2*(-dB0TTH + dB0TTZ))/(4.*MW2*sw2) - 4*dB0TTZ*gZu(1)*gZu(2)

    SibL=SibL+(-1 - 2*B1BB0)/9. - (MB2*(B1BBH + B1BBZ))/(4.*MW2*sw2) &
        - (1 + (2 + MT2/MW2)*B1BTW)/(2.*sw2) - (1 + 2*B1BBZ)*gZd(2)**2

    SibR=SibR+(-1 - 2*B1BB0)/9. - (MB2*(B1BBH + B1BBZ))/(4.*MW2*sw2) &
        - (MB2*B1BTW)/(2.*MW2*sw2) - (1 + 2*B1BBZ)*gZd(1)**2

    SibS=SibS+(2 - 4*B0BB0)/9. - (MB2*(-B0BBH + B0BBZ))/(4.*MW2*sw2) -  &
        (MT2*B0BTW)/(2.*MW2*sw2) - (-2 + 4*B0BBZ)*gZd(1)*gZd(2)

    dSibL=dSibL+(-2*dB1BB0)/9. - (MB2*(dB1BBH + dB1BBZ))/(4.*MW2*sw2) &
       - ((2 + MT2/MW2)*dB1BTW)/(2.*sw2) - 2*dB1BBZ*gZd(2)**2

    dSibR=dSibR+(-2*dB1BB0)/9. - (MB2*(dB1BBH + dB1BBZ))/(4.*MW2*sw2) &
       - (MB2*dB1BTW)/(2.*MW2*sw2) - 2*dB1BBZ*gZd(1)**2

    dSibS=dSibS+(-4*dB0BB0)/9. - (MB2*(-dB0BBH + dB0BBZ))/(4.*MW2*sw2) &
       - (MT2*dB0BTW)/(2.*MW2*sw2) - 4*dB0BBZ*gZd(1)*gZd(2)

    SiuL=SiuL+(-4.*(1. + IRrational + 2.*B1000))/9. &  ! Photon
             - (1 + 2*B100W)/(2.*sw2) &                ! W
             - (1 + 2*B100Z)*gZu(2)**2                 ! Z

    SiuR=SiuR+(-4.*(1. + IRrational + 2.*B1000))/9. &  ! Photon
               - (1 + 2*B100Z)*gZu(1)**2               ! Z

    SidL=SidL+(-1. - IRrational - 2.*B1000)/9. &       ! Photon
             - (1 + 2*B100W)/(2.*sw2) &                ! W
             - (1 + 2*B100Z)*gZd(2)**2                 ! Z

    SidR=SidR+(-1. - IRrational - 2.*B1000)/9. &       ! Photon
             - (1 + 2*B100Z)*gZd(1)**2                 ! Z

    SieL=SieL-1. - IRrational - 2.*B1000 &             ! Photon
             - (1 + 2*B100W)/(2.*sw2) &                ! W
             - (1 + 2*B100Z)*gZl(2)**2                 ! Z

    SieR=SieR-1. - IRrational - 2.*B1000 &             ! Photon
             - (1 + 2*B100Z)*gZl(1)**2                 ! Z

    SinL=SinL-(1. + 2.*B100W)/(2.*sw2) &               ! W
             - (1 + 2*B100Z)*gZn(2)**2                 ! Z

  end if

  if (SwF /= 0 .and. CT_is_on /= 0) then
    ! fermionic

    !Fermionic Tadpole. Agrees with eq. 12 in NP B 383 (1992) 73
    Tadpole   = Tadpole + 3*2*MT2/MW/sw*A0T + 3*2*MB2/MW/sw*A0B

!This is the fermionic part of page 105-107 from Denner92 evaluated in selfenergies.nb

  MREG2=MREG**2

    ! contributions from light fermions incl. bottom
    PiAAlightZ=PiAAlightZ + (4*(-6*MB2*nc*B00BB  &
      + rMZ2*(-27 - 11*nc + (81 + 30*nc)*B0Z00)  &
      + 3*nc*(2*MB2 + rMZ2)*B0ZBB))/(81.)

    ! contributions from heavy fermions = top-quark
    dSiAAheavy0=dSiAAheavy0+(16*nc*(-1+3*B00TT+6*MT2*dB00TT))/81.

    if (ew_renorm_scheme == 2) then
      dSiAAZ=dSiAAZ+(4* (-9 - 5*nc + (27d0 + 10*nc)*B0Z00  &
        + nc*B0ZBB + 4*nc*B0ZTT  &
        + 27*rMZ2*dB0Z00 + 10*nc*rMZ2*dB0Z00  &
        + 2*MB2*nc*dB0ZBB + nc*rMZ2*dB0ZBB  &
        + 8*MT2*nc*dB0ZTT + 4*nc*rMZ2*dB0ZTT))/27.
    end if

    ! contribution from heavy + light fermions (in dimreg)
    dSiAA0=dSiAA0+(4.*(-9 - 5*nc + 27d0*B0000 + 10d0*nc*B0000  &
          + nc*B00BB + 2*MB2*nc*dB00BB &
          + 4d0*nc*B00TT +  8*MT2*nc*dB00TT))/27.

!      SiAZ0=SiAZ0+0 !no fermionic contribution

    SiAZZ=SiAZZ+(-2*((2*nc*(rMZ2/3. - rMZ2*B0Z00)*(gZd(1) + gZd(2)))/3.  &
        + (nc*(rMZ2/3. + 2*MB2*B00BB + (-2*MB2 - rMZ2)*B0ZBB)*(gZd(1) + gZd(2)))/3. &
        + 3*(rMZ2/3. - rMZ2*B0Z00)*(gZl(1) + gZl(2))  &
        - (4*nc*(rMZ2/3. - rMZ2*B0Z00)*(gZu(1) + gZu(2)))/3. - (2*nc*(rMZ2/3. + 2*MT2*B00TT &
        + (-2*MT2 - rMZ2)*B0ZTT)*(gZu(1) + gZu(2)))/3. ))/3.

    SiZZ=SiZZ+(-2*((-2*rMZ2*nc*(-1 + 3*B0Z00)*(gZd(1)**2 + gZd(2)**2))/3.  &
        + nc*((3*MB2*B0ZBB)/(4.*cw2*sw2) + (rMZ2/3. + 2*MB2*B00BB  &
        - (2*MB2 + rMZ2)*B0ZBB)*(gZd(1)**2 + gZd(2)**2)) &
        - rMZ2*(-1 + 3*B0Z00)*(gZl(1)**2 + gZl(2)**2) &
        - rMZ2*(-1 + 3*B0Z00)*(gZn(1)**2 + gZn(2)**2) &
        - (2*rMZ2*nc*(-1 + 3*B0Z00)*(gZu(1)**2 + gZu(2)**2))/3. &
        + nc*((3*MT2*B0ZTT)/(4.*cw2*sw2) + (rMZ2/3. + 2*MT2*B00TT &
        - (2*MT2 + rMZ2)*B0ZTT)*(gZu(1)**2 + gZu(2)**2))))/3.

    dSiZZ=dSiZZ+(-2*((-2*nc*(-1 + 3*B0Z00 + 3*rMZ2*dB0Z00)*(gZd(1)**2 + gZd(2)**2))/3. &
        + nc*((3*MB2*dB0ZBB)/(4.*cw2*sw2) &
        - ((-1 + 3*B0ZBB + 3*(2*MB2 + rMZ2)*dB0ZBB)*(gZd(1)**2 + gZd(2)**2))/3.) &
        - (-1 + 3*B0Z00 + 3*rMZ2*dB0Z00)*(gZl(1)**2 + gZl(2)**2) &
        - (-1 + 3*B0Z00 + 3*rMZ2*dB0Z00)*(gZn(1)**2 + gZn(2)**2) &
        - (2*nc*(-1 + 3*B0Z00 + 3*rMZ2*dB0Z00)*(gZu(1)**2 + gZu(2)**2))/3. &
        + nc*((3*MT2*dB0ZTT)/(4.*cw2*sw2) - ((-1 + 3*B0ZTT &
        + 3*(2*MT2 + rMZ2)*dB0ZTT)*(gZu(1)**2 + gZu(2)**2))/3.)))/3.

    SiW=SiW-(rMW2 - 3*rMW2*B0W00 &
         + nc*(rMW2 + MB2*B00BB + MT2*B00TT  &
         - 2*rMW2*B0W00 &
         + ((MB2 + MT2 - 2*rMW2)*B0WTB)/2.  &
         + ((MB2 - MT2)**2*(-B00TB + B0WTB))/(2.*rMW2)))/(3.*sw2)

    dSiW=dSiW+(-1 + 3*B0W00 +  &
         3*rMW2*dB0W00 - (nc*(2 - 4*B0W00 +  &
          ((MB2 - MT2)**2* (B00TB - B0WTB))/rMW2**2 -  &
          2*B0WTB - 4*rMW2*dB0W00 +  &
          (MB2 + MT2 - 2*rMW2)*dB0WTB +  &
          ((MB2 - MT2)**2*dB0WTB)/rMW2))/2.)/(3.*sw2)

    if (ew_renorm_scheme == 1) then
      SiW0=SiW0-nc/(3.*sw2)*(MB2*B00BB + ((MB2 + MT2)*B00TB)/2. +  &
          MT2*B00TT +  ((MB2 - MT2)**2*dB00TB)/2.)
    end if

    SiH=SiH-(MB2*nc*(2*A0B +(4*MB2 - rMH2)*B0HBB))/(2.*MW2*sw2) -  &
        (MT2*nc*(2*A0T + (4*MT2 - rMH2)*B0HTT))/(2.*MW2*sw2)

    dSiH=dSiH-(MB2*nc*(-B0HBB + (4*MB2 - rMH2)*dB0HBB))/(2.*MW2*sw2) &
      - (MT2*nc*(-B0HTT + (4*MT2 - rMH2)*dB0HTT))/(2.*MW2*sw2)

  end if


! set RCs

!gauge bosons
  dZWEW   = -real(dSiW)
  if (imag(MW2) == 0) then
    dZMW2EW = real(SiW)
  else if (imag(MW2) /= 0 .and. cms_on == 1) then !CMS
    cTW     = -(rMW2-MW2)*dSiW-4.*(rMW2-MW2)  ! 1st order expansion & C^w term
    dZMW2EW = SiW + cTW
  else
    call ol_fatal('on-shell EW renormalization with finite width not supported!')
  end if

  dZZAEW  = 2.*SiAZ0/MZ2
  dZZZEW  = -real(dSiZZ)
  if (imag(MZ2) == 0 .or. (cms_on == 0 .and. trim(model) == "sm_vaux")) then
    dZAZEW  = -2.*real(SiAZZ/MZ2)
    dZMZ2EW = real(SiZZ)
  else if (imag(MZ2) /= 0 .and. cms_on == 1) then !CMS
    dZAZEW  = real(-2.*SiAZZ+(MZ2-rMZ2)*dZZAEW)/rMZ2
    cTZ = -(rMZ2-MZ2)*dSiZZ ! 1st order expansion
    dZMZ2EW = SiZZ + cTZ
  else
    call ol_fatal('on-shell EW renormalization with finite width not supported!')
  end if
  dZZAEW  = real(dZZAEW)

!Higgs
  dtEW    = -Tadpole
  dZHEW   = -real(dSiH)
  if (imag(MH2) == 0) then
    dZMH2EW = real(SiH)
  else if (imag(MH) /= 0 .and. cms_on == 1) then !CMS
    cTH = -(rMH2-MH2)*dSiH ! 1st order expansion
    dZMH2EW = SiH + cTH
  else
    call ol_fatal('on-shell EW renormalization with finite width not supported!')
  end if


!Fermions
  !leptons
  dZeLEW = -real(SieL)
  dZeREW = -real(SieR)
  dZnLEW = -real(SinL)
! massive tau no supported yet
!   if (ML /= 0) then
!     dZLLEW = -SigmalL-ML2*(dSigmalL+dSigmalR+2.*dSigmalS)
!     dZLREW = -SigmalR-ML2*(dSigmalL+dSigmalR+2.*dSigmalS)
!     dZMLEW = 0.5*ML*(SigmalL+SigmalR+2.*SigmalS)
!   else
!     dZLLEW = -SigmaeL
!     dZLREW = -SigmaeR
!     dZMLEW = 0
!  end if

  !light quarks
  dZuLEW = -real(SiuL)
  dZuREW = -real(SiuR)
  dZdLEW = -real(SidL)
  dZdREW = -real(SidR)

  !heavy quarks
  !Top
  dSitLRS = dSitL+dSitR+2.*dSitS
  dZtLEW = -real(SitL+rMT2*dSitLRS)
  dZtREW = -real(SitR+rMT2*dSitLRS)
  if (imag(MT2) == 0) then
    dZMTEW  = 0.5*MT*real(SitL+SitR+2.*SitS) ! on-shell
  else if (imag(MT) /= 0 .and. cms_on == 1) then !CMS
    cTT     = -0.5*(rMT2-MT2)*dSitLRS+(rMT2-MT2)/rMT2*16./9. ! 1st order expansion & C^t term
    dZMTEW  = MT*(0.5*(SitL+SitR+2.*SitS) + cTT)
  else
    call ol_fatal('on-shell EW renormalization with finite width not supported!')
  end if

  !Bottom
  if (MB /= 0._/**/REALKIND) then
    dSibLRS = dSibL+dSibR+2.*dSibS
    dZbLEW = -real(SibL+rMB2*dSibLRS)
    dZbREW = -real(SibR+rMB2*dSibLRS)
    if (imag(MB2) == 0) then ! on-shell
      dZMBEW  = 0.5*MB*real(SibL+SibR+2.*SibS) !on-shell
    else if (imag(MB) /= 0 .and. cms_on == 1) then !CMS
      cTB     = -0.5*(rMB2-MB2)*dSibLRS+(rMB2-MB2)/rMB2*4./9. ! 1st order expansion & C^b term
      dZMBEW  = MB*(0.5*(SibL+SibR+2.*SibS) + cTB)
    else
      call ol_fatal('on-shell EW renormalization with finite width not supported!')
    end if
  else
    dZMBEW = 0.
    dZbLEW = -real(SidL)
    dZbREW = -real(SidR)
  end if

  dZtLEWcc = dZtLEW
  dZtREWcc = dZtREW
  dZbLEWcc = dZbLEW
  dZbREWcc = dZbREW
  dZuLEWcc = dZuLEW
  dZuREWcc = dZuREW
  dZdLEWcc = dZdLEW
  dZdREWcc = dZdREW
  dZeLEWcc = dZeLEW
  dZeREWcc = dZeREW
  dZnLEWcc = dZnLEW

! weak mixing angle
  dcwEW     = cw/2.*(dZMW2EW/MW2-dZMZ2EW/MZ2)
  dswEW     =  -1.*cw/sw*dcwEW

  dAlphaQED_MZ=4*pi/alpha_QED*(1-alpha_QED_0/alpha_QED_MZ)  ! running of alpha from 0 to MZ

! charge renormalization
  if (ew_renorm_scheme == 0 ) then ! on-shell scheme = alpha(0) scheme
    dZAAEW  = -real(dSiAAheavy0 + PiAAlightZ/rMZ2 + dAlphaQED_MZ)
    dZeQEDEW = -0.5*dZAAEW - sw/cw*SiAZ0/MZ2
  else if (ew_renorm_scheme == 1) then ! Gmu scheme
!    dZAAEW  = -real(dSiAAheavy0 + PiAAlightZ/rMZ2 + dAlphaQED_MZ)
    dZAAEW = -real(dSiAA0) ! Note: light fermions in dim.reg.
    dZeQEDEW = dswEW/sw - 1./sw/cw*SiAZ0/MZ2
    dZeQEDEW = dZeQEDEW - 0.5/sw2*(6.+(7.-4.*sw2)/(2.*sw2)*log(cw2))
    dZeQEDEW = dZeQEDEW +  0.5*(dZMW2EW-SiW0)/MW2
  else if (ew_renorm_scheme == 2) then ! alpha(mZ) scheme
!    dZAAEW  = -real(dSiAAheavy0 + PiAAlightZ/rMZ2 + dAlphaQED_MZ)  ! as in a(0)
!    dZeQEDEW = -0.5*(dZAAEW+dAlphaQED_MZ) - sw/cw*SiAZ0/MZ2   !NB: dAlphaQED_MZ drops out
    dZAAEW = -real(dSiAA0) ! Note: light fermions in dim.reg.
    dZeQEDEW = 0.5*dSiAAZ - sw/cw*SiAZ0/MZ2
  else
    call ol_error(2, 'in ew_renormalisation: ew_renorm_scheme= ' // to_string(ew_renorm_scheme) // ' not supported!')
    call ol_fatal()
  end if
  dZeQEDEW = real(dZeQEDEW)

!pure pole contributions for debugging
!     dZuRPole=-gZu(1)**2*de1_UV - 4.*cONE*(de1_UV-de1_IR)/9.
!     dZuLPole=-(gZu(2)**2+1/(2*sw2))*de1_UV - 4.*cONE*(de1_UV-de1_IR)/9.
!
!     dZtRPole=- gZu(1)**2*de1_UV - 4.*cONE*de1_UV/9. - 2d0*(MT2/4d0/sw2/MW2)*de1_UV-8d0/9d0*de1_IR
!     dZtLPole=- (gZu(2)**2+1/(2*sw2))*de1_UV - 4*cONE*de1_UV/9. - (MT2/4d0/sw2/MW2)*de1_UV-8d0/9d0*de1_IR
!
!     dZAAEWPole = -32d0/3d0*(de1_UV-de1_IR)+3d0*de1_UV-16d0/9d0*de1_IR
!     dZAAEWPole = -32d0/3d0*(de1_UV)+3d0*de1_UV   !pure UV
!     dZZAEWPole = 4d0*cw/sw*de1_UV
!     dZAZEWPole = -1d0*(30d0*cw2+1)/3d0/sw/cw*de1_UV & !Bosonic
!                   -8d0/3d0*de1_UV*(8d0*sw2-3d0)/sw/cw   !Fermionic
!     dZZZEWPole = de1_UV/6d0/sw2/cw2*(18d0*cw4+2d0*cw2-1d0) & !& !Bosonic
!                   -de1_UV*2d0/3d0*(6d0-12d0*sw2+16d0*sw**4)/cw2/sw2  !Fermionic
!     dZWEWPole = 10d0/3d0*de1_UV+1d0/12d0/sw2*(40*cw2-2)*de1_UV-2d0*de1_IR - 4d0/sw2*de1_UV
!     dZeQEDEWPole = -0.5d0*dZAAEWPole-0.5*sw/cw*dZZAEWPole     ! on-shell scheme
!
!     dZMZ2EWPole = -1d0/3d0/sw2/cw2*de1_UV*(MZ2*(9d0*cw**4+cw2-7d0/2d0)+MW2*(12*cw2-6d0)) & !Bosonic
!                  + 2d0/3d0*de1_UV*(MZ2*(6d0-12d0*sw2+16d0*sw**4)/cw2/sw2-9d0/4d0*MT2/sw2/cw2)  !Fermionic
!
!     dZMW2EWPole = -10d0/3*MW2*de1_UV - 1d0/12d0/sw2*((40d0*cw2+38d0)*MW2-(16d0*cw2+12d0)*MZ2)*de1_UV & !Bosonic
!                   + 1d0/3d0/sw2*de1_UV*(12*MW2 - 9d0/2d0*MT2) !Fermionic
!     dcwEWPole     = cw/2.*(dZMW2EWPole/MW2-dZMZ2EWPole/MZ2)

! check explicit poles for debugging
!      print*, de1_UV, de1_IR, dZuREW-dZuRPole, dZuLEW-dZuLPole
!      print*, de1_UV, de1_IR, dZtREW-dZtRPole, dZtLEW-dZtLPole
!      print*, de1_UV, de1_IR, dZeQEDEW-dZeQEDEWPole
!      print*, de1_UV, de1_IR, dcwEW-dcwEWPole
!      print*, de1_UV, de1_IR, dZAAEW-dZAAEWPole
!      print*, de1_UV, de1_IR, dZZAEW-dZZAEWPole
!      print*, de1_UV, de1_IR, dZAZEW-dZAZEWPole
!      print*, de1_UV, de1_IR, dZZZEW-dZZZEWPole
!      print*, de1_UV, de1_IR, dZWEW-dZWEWPole
!      print*, de1_UV, de1_IR, dZMZ2EW-dZMZ2EWPole
!      print*, de1_UV, de1_IR, dZMW2EW-dZMW2EWPole


! print rs constans
  if (debug_ew_renorm .ge. 1) then
    debug_norm = alpha_QED/4/pi
    print*, "==================================="
    print*, "==             DEBUG             =="
    print*, "==  EW renormalization constants =="
    print*, "==================================="
    print*, "loop_parameters_status", loop_parameters_status
    print*, "de1_UV", de1_UV
    print*, "de1_IR", de1_IR
    print*, "ew_renorm_scheme: ", ew_renorm_scheme
    print*, "Tadpole", Tadpole
    print*, "WF_V"
    print*, "dZAAEW" , dZAAEW*debug_norm
    print*, "dZAZEW" , dZAZEW*debug_norm
    print*, "dZZAEW" , dZZAEW*debug_norm
    print*, "dZZZEW" , dZZZEW*debug_norm
    print*, "dZWEW" , dZWEW*debug_norm
    print*, "dZHEW" , dZHEW*debug_norm
    print*, "M_V"
    print*, "dZMW2EW" , dZMW2EW*debug_norm
    print*, "dZMZ2EW" , dZMZ2EW*debug_norm
    print*, "dZMH2EW" , dZMH2EW*debug_norm
    print*, "WF_F"
    print*, "dZuREW" , dZuREW*debug_norm
    print*, "dZuLEW" , dZuLEW*debug_norm
    print*, "dZdREW" , dZdREW*debug_norm
    print*, "dZdLEW" , dZdLEW*debug_norm
    print*, "dZbREW" , dZbREW*debug_norm
    print*, "dZbLEW" , dZbLEW*debug_norm
    print*, "dZtREW" , dZtREW*debug_norm
    print*, "dZtLEW" , dZtLEW*debug_norm
    print*, "dZeREW" , dZeREW*debug_norm
    print*, "dZeLEW" , dZeLEW*debug_norm
    print*, "dZnLEW" , dZnLEW*debug_norm
    print*, "M_F"
    print*, "dZMBEW" , dZMBEW*debug_norm
    print*, "dZMTEW" , dZMTEW*debug_norm
    print*, "C"
    print*, "dZeQEDEW" , dZeQEDEW*debug_norm
    print*, "dcwEW" , dcwEW*debug_norm, dcwEW/cw*debug_norm
    print*, "dswEW" , dswEW*debug_norm, dswEW/sw*debug_norm
    print*, "==================================="
   end if
!   if (debug_ew_renorm .ge. 2) then
!     debug_norm = alpha_QED/4/pi
!     print*, "==================================="
!     print*, "==             DEBUG             =="
!     print*, "==    EW renorm. self energies   =="
!     print*, "==================================="
!     print*, "SitL" , SitL*debug_norm
!     print*, "SitR" , SitR*debug_norm
!     print*, "SitS" , SitS*debug_norm
!     print*, "dSitL" , dSitL*debug_norm
!     print*, "dSitR" , dSitR*debug_norm
!     print*, "dSitS" , dSitS*debug_norm
!     print*, "==================================="
!   end if

! calculate counterterms & R2

  ! some abbreviations
  ! Sum of squared quark masses
  sumMQ2 = MU2 + MD2 + MS2 + MC2
  sumMQ2Q2 = 4._/**/REALKIND/9.*MU2 + 1._/**/REALKIND/9.*MD2 + 4._/**/REALKIND/9.*MS2 + 1._/**/REALKIND/9.*MC2
  sumMQ2QI = 2._/**/REALKIND/6.*MU2 + 1._/**/REALKIND/6.*MD2 + 2._/**/REALKIND/6.*MS2 + 1._/**/REALKIND/6.*MC2
  sumMQ2QUD = 2._/**/REALKIND/3.*MD2+1._/**/REALKIND/3.*MU2 + 2._/**/REALKIND/3.*MS2+1._/**/REALKIND/3.*MC2   ! Sum(Qu*mD2 - Qd*mU2)
  sumMQ4 = MU2**2 + MD2**2 + MS2**2 + MC2**2
  sumMUD = MU*MD + MC*MS
  sumMUD2 = (MU2+MD2)**2 + (MC2+MS2)**2
  sumMU2 = MU2 + MC2
  sumMD2 = MD2 + MD2
  sumMU4 = MU2**2 + MC2**2
  sumMD4 = MD2**2 + MD2**2
  if (nf > 4) then
    sumMQ2 = sumMQ2 + MB2
    sumMQ2Q2 = sumMQ2Q2 + 1._/**/REALKIND/9.*MB2
    sumMQ2QI = sumMQ2QI + 1._/**/REALKIND/6.*MB2
    sumMQ2QUD = sumMQ2QUD + 2._/**/REALKIND/3.*MB2
    sumMQ4 = sumMQ4 + MB2**2
    sumMD2 = sumMD2 + MB2
    sumMD4 = sumMD4 + MB2**2
  end if
  if (nf > 5) then
    sumMQ2 = sumMQ2 + MT2
    sumMQ2Q2 = sumMQ2Q2 + 4._/**/REALKIND/9.*MT2
    sumMQ2QI = sumMQ2QI + 2._/**/REALKIND/6.*MT2
    sumMQ2QUD = sumMQ2QUD + 1._/**/REALKIND/3.*MT2
    sumMQ4 = sumMQ4 + MT2**2
    sumMUD = sumMUD + MT*MB
    sumMUD2 = sumMUD2 + (MT2+MB2)**2
    sumMU2 = sumMU2 + MT2
    sumMU4 = sumMU4 + MT2**2
  end if
!  sumQ = 1.
!  sumQI = 3._/**/REALKIND/2.
!  sumQ2 = 5._/**/REALKIND/3.
!  sumI2 = 3._/**/REALKIND/2.


  ! firt set all counterterms to zero
    EWctWW = 0
    EWctZZ = 0
    EWctAZ = 0.
    EWctAA = 0.
    EWctHH = 0.
    EWctXX = 0.
    EWctPP = 0.
    EWctXA = 0.
    EWctXZ = 0.
    EWctPW = 0.
    EWctuu   = 0.
    EWctdd   = 0.
    EWcttt   = 0.
    EWctbb   = 0.
    EWctee   = 0.
    EWctLL   = 0.
    EWctnn   = 0.
    EWctWWWW = 0.
    EWctWWZZ = 0.
    EWctWWAZ = 0.
    EWctWWAA = 0.
    EWctR2AAAZ = 0.
    EWctR2AAZZ = 0.
    EWctR2AZZZ = 0.
    EWctR2ZZZZ = 0.
    EWctAWW = 0.
    EWctZWW = 0.
    EWctSSSS1 = 0.
    EWctSSSS2 = 0.
    EWctSSSS3 = 0.
    EWctHHH = 0.
    EWctHXX = 0.
    EWctHPP = 0.
    EWctWWXX = 0.
    EWctWWHH = 0.
    EWctZZPP = 0.
    EWctZAPP = 0.
    EWctAAPP = 0.
    EWctZZHH = 0.
    EWctZZXX = 0.
    EWctZAHH = 0.
    EWctWZPH = 0.
    EWctWAPH = 0.
    EWctWZPX = 0.
    EWctWAPX = 0.
    EWctAXH = 0.
    EWctZXH = 0.
    EWctAPP = 0.
    EWctZPP = 0.
    EWctWPH = 0.
    EWctWPX = 0.
    EWctHWW = 0.
    EWctHZZ = 0.
    EWctHZA = 0.
    EWctPWZ = 0.
    EWctPWA = 0.
    EWctHAA = 0.
    EWctAuu  = 0.
    EWctAdd  =  0.
    EWctAtt  =  0.
    EWctAbb  = 0.
    EWctAee  = 0.
    EWctALL  = 0.
    EWctAnn  = 0.
    dgZu = 0.
    dgZd = 0.
    dgZl = 0.
    dgZn = 0.
    EWctVuu  = 0.
    EWctVdd  = 0.
    EWctVtt  = 0.
    EWctVbb  = 0.
    EWctVee  = 0.
    EWctVLL  = 0.
    EWctVnn  = 0.
    EWctVdu  = 0.
    EWctVbt  = 0.
    EWctVen  = 0.
    EWctVLn  = 0.
    EWctVud  = 0.
    EWctVtb  = 0.
    EWctVne  = 0.
    EWctVnL  = 0.
    EWctGuu  = 0.
    EWctGdd  = 0.
    EWctGtt  = 0.
    EWctGbb  = 0.
    EWctHtt = 0.
    EWctHbb = 0.
    EWctHLL = 0.
    EWctXtt = 0.
    EWctXbb = 0.
    EWctXLL = 0.
    EWctPdu = 0.
    EWctPud = 0.
    EWctPtb = 0.
    EWctPbt = 0.
    EWctPnL = 0.
    EWctPLn = 0.
    EWctAUWUW = 0.
    EWctZUWUW = 0.
    EWctWUWUZ = 0.
    EWctWUZUW = 0.
    EWctWUWUA = 0.
    EWctWUAUW = 0.
    EWctHUZUZ = 0.
    EWctHUWUW   = 0.
    EWctXUWUW   = 0.
    EWctPUZUW  = 0.
    EWctPUWUZ  = 0.
    EWctPUWUA  = 0.



  ! set UV counterterms
  if (CT_is_on /= 0) then
    ! Only UV counterterms

    ! VV Vector propagators
    EWctWW = [ dZWEW  , -1.*MW2*dZWEW  - dZMW2EW , ZERO ]
    EWctZZ = [ dZZZEW , -1.*MZ2*dZZZEW - dZMZ2EW , ZERO ]
    EWctAZ = [ 0.5*dZAZEW+0.5*dZZAEW , -0.5*MZ2*dZZAEW  , ZERO ]
    EWctAA = [ dZAAEW , ZERO , ZERO ]

    ! SS scalar propagators
    EWctHH = [ dZHEW , MH2*dZHEW + dZMH2EW ]
    EWctXX = [ ZERO, - eQED/2./sw*dtEW/MW + dZMZ2EW ]
    EWctPP = [ ZERO, - eQED/2./sw*dtEW/MW + dZMW2EW ]

    EWctXA = dZZAEW
    EWctXZ = dZZZEW + dZMZ2EW/MZ2
    EWctPW = dZWEW + dZMW2EW/MW2

    ! FF fermionic propagators
    EWctuu   = [ 0.5*(dZuREW+dZuREWcc), 0.5*(dZuLEW+dZuLEWcc), ZERO , ZERO ]
    EWctdd   = [ 0.5*(dZdREW+dZdREWcc), 0.5*(dZdLEW+dZdLEWcc), ZERO , ZERO ]
    EWcttt   = [ 0.5*(dZtREW+dZtREWcc), 0.5*(dZtLEW+dZtLEWcc), MT/2.*(dZtREW+dZtLEWcc)+dZMTEW , MT/2.*(dZtLEW+dZtREWcc)+dZMTEW ]
    EWctbb   = [ 0.5*(dZbREW+dZbREWcc), 0.5*(dZbLEW+dZbLEWcc), MB/2.*(dZbREW+dZbLEWcc)+dZMBEW , MB/2.*(dZbLEW+dZbREWcc)+dZMBEW ]
    EWctee   = [ 0.5*(dZeREW+dZeREWcc), 0.5*(dZeLEW+dZeLEWcc), ZERO , ZERO ]
    EWctLL   = [ 0.5*(dZLREW+dZLREWcc), 0.5*(dZLLEW+dZLLEWcc), ML/2.*(dZLREW+dZLLEWcc)+dZMLEW , ML/2.*(dZLLEW+dZLREWcc)+dZMLEW ]
    EWctnn   = [ ZERO , 0.5*(dZnLEW+dZnLEWcc) , ZERO , ZERO ]

    !VVVV
    EWctWWWW = 1./sw2*(2*dZeQEDEW - 2.*dswEW/sw + 2.*dZWEW) * [2,-1]
    EWctWWZZ = (-cw2/sw2*(2*dZeQEDEW - 2./cw2*dswEW/sw + dZWEW + dZZZEW) + cw/sw*dZAZEW)*[2,-1]
    EWctWWAZ = (cw/sw*(2*dZeQEDEW - 1./cw2*dswEW/sw + dZWEW + 0.5*dZZZEW + 0.5*dZAAEW) &
    - 0.5*dZAZEW- 0.5*cw2/sw2*dZZAEW) * [2,-1]
    EWctWWAA = (-1.*(2*dZeQEDEW + dZWEW + dZAAEW) + cw/sw*dZZAEW) * [2,-1]

    !VVV
    EWctAWW = (dZeQEDEW + dZWEW + 0.5*dZAAEW - 0.5*cw/sw*dZZAEW)
    EWctZWW = -cw/sw * (dZeQEDEW - dswEW/cw2/sw + dZWEW + 0.5*dZZZEW) + 0.5*dZAZEW

    !SSSS
    EWctSSSS1 = 2.*dZeQEDEW - 2.*dswEW/sw + dZMH2EW/MH2 + eQED/2./sw * dtEW/MW/MH2 - dZMW2EW/MW2
    EWctSSSS2 = EWctSSSS1 + 2.*dZHEW
    EWctSSSS3 = EWctSSSS1 + dZHEW

    EWctHHHH = 3*EWctSSSS2
    EWctHHXX = EWctSSSS3
    EWctHHPP = EWctSSSS3
    EWctXXXX = 3*EWctSSSS1
    EWctXXPP = EWctSSSS1
    EWctPPPP = 2*EWctSSSS1

    !SSS
    EWctHHH = dZeQEDEW - dswEW/sw + dZMH2EW/MH2 + 0.5*eQED/sw * dtEW/MW/MH2 - 0.5*dZMW2EW/MW2 + 1.5*dZHEW
    EWctHXX = EWctHHH - dZHEW
    EWctHPP = EWctHHH - dZHEW

    !VVSS
    EWctWWXX = 0.5/sw2*(2.*dZeQEDEW - 2.*dswEW/sw + dZWEW)
    EWctWWHH = EWctWWXX + 0.5/sw2*dZHEW
    EWctZZPP = (sw2-cw2)**2/2./sw2/cw2*(2*dZeQEDEW + 2./(sw2-cw2)/cw2*dswEW/sw + dZZZEW) + (sw2-cw2)/sw/cw*dZAZEW
    EWctZAPP = (sw2-cw2)/sw/cw*(2*dZeQEDEW + 1./(sw2-cw2)/cw2*dswEW/sw + 0.5*dZZZEW + 0.5*dZAAEW) + &
                (sw2-cw2)**2/4./sw2/cw2*dZZAEW + dZAZEW
    EWctAAPP = 2.*(2.*dZeQEDEW + dZAAEW) + (sw2-cw2)/sw/cw*dZZAEW
    EWctZZXX = 0.5/sw2/cw2*(2.*dZeQEDEW + 2.*(sw2-cw2)/cw2*dswEW/sw + dZZZEW )
    EWctZZHH = EWctZZXX + 0.5/sw2/cw2*dZHEW
    EWctZAHH = 0.25/sw2/cw2*dZZAEW
    EWctWZPH = -0.5/cw*(2.*dZeQEDEW - dcwEW/cw + 0.5*dZWEW + 0.5*dZHEW + 0.5*dZZZEW) - 0.25/sw*dZAZEW
    EWctWAPH = -0.5/sw*(2.*dZeQEDEW - dswEW/sw + 0.5*dZWEW + 0.5*dZHEW + 0.5*dZAAEW) - 0.25/cw*dZZAEW
    EWctWZPX = -1*CI/2./cw* ( 2.*dZeQEDEW - dcwEW/cw + 0.5*dZWEW + 0.5*dZZZEW ) - CI*0.25/sw*dZAZEW
    EWctWAPX = -1*CI/2./sw* ( 2.*dZeQEDEW - dswEW/sw + 0.5*dZWEW + 0.5*dZAAEW ) - CI*0.25/cw*dZZAEW

    !VSS
    EWctAXH = -0.25*CI/cw/sw*dZZAEW
    EWctZXH = -0.5*CI/cw/sw* ( dZeQEDEW + (sw2-cw2)/cw2*dswEW/sw + 0.5*dZHEW + 0.5*dZZZEW )
    EWctAPP = -1.*( dZeQEDEW + 0.5*dZAAEW + 0.25*(sw2-cw2)/sw/cw*dZZAEW )
    EWctZPP = -0.25*(sw2-cw2)/sw/cw*( dZeQEDEW + dswEW/sw/cw2/(sw2-cw2) + 0.5*dZZZEW) - 0.5*dZAZEW
    EWctWPH = -0.5/sw*( dZeQEDEW - dswEW/sw + 0.5*dZWEW + 0.5*dZHEW )
    EWctWPX = -0.5*CI/sw*( dZeQEDEW - dswEW/sw + 0.5*dZWEW )

    !SVV
    EWctHWW = MW/sw * ( dZeQEDEW - dswEW/sw + 0.5*dZMW2EW/MW2 + 0.5*dZHEW + dZWEW )
    EWctHZZ = MW/sw/cw2 * ( dZeQEDEW + (2.*sw2-cw2)/cw2*dswEW/sw + 0.5*dZMW2EW/MW2 + 0.5*dZHEW + &
              dZZZEW )
    EWctHZA = 0.5*MW/sw/cw2 * dZZAEW
    EWctPWZ = -1.*MW*sw/cw * ( dZeQEDEW + dswEW/cw2/sw + 0.5*dZMW2EW/MW2 + 0.5*dZWEW + 0.5*dZZZEW )-&
              0.5*MW*dZAZEW
    EWctPWA = -1.*MW * ( dZeQEDEW + 0.5*dZMW2EW/MW2 + 0.5*dZWEW + 0.5*dZAAEW ) - 0.5*MW*sw/cw*dZZAEW

    !VFF
    ! Gff
    EWctGuu  = [ dZuREW , dZuLEW ]
    EWctGdd  = [ dZdREW , dZdLEW ]
    EWctGtt  = [ dZtREW , dZtLEW ]
    EWctGbb  = [ dZbREW , dZbLEW ]
    ! Aff
    EWctAuu  = [ -2._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZuREW+dZuREWcc))  + gZu(1)/2.*dZZAEW , &
                 -2._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZuLEW+dZuLEWcc))  + gZu(2)/2.*dZZAEW ]
    EWctAdd  = [  1._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZdREW+dZdREWcc))  + gZd(1)/2.*dZZAEW , &
                  1._/**/REALKIND/3. * (dZeQEDEW+  0.5*dZAAEW + 0.5*(dZdLEW+dZdLEWcc))  + gZd(2)/2.*dZZAEW ]
    EWctAtt  = [ -2._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZtREW+dZtREWcc))  + gZu(1)/2.*dZZAEW , &
                 -2._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZtLEW+dZtLEWcc))  + gZu(2)/2.*dZZAEW ]
    EWctAbb  = [  1._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZbREW+dZbREWcc))  + gZd(1)/2.*dZZAEW , &
                  1._/**/REALKIND/3. * (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZbLEW+dZbLEWcc))  + gZd(2)/2.*dZZAEW ]
    EWctAee  = [  (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZeREW+dZeREWcc))  + gZl(1)/2.*dZZAEW , &
                  (dZeQEDEW + 0.5*dZAAEW + 0.5*(dZeLEW+dZeLEWcc))  + gZl(2)/2.*dZZAEW ]
    EWctAnn  = [ ZERO , gZn(2)*0.5*dZZAEW ]
! massive tau no supported yet
!    EWctALL  = [  (dZeQEDEW + 0.5*dZAAEW + dZLREW)  + gZl(1)/2.*dZZAEW ,  (dZeQEDEW + &
!                0.5*dZAAEW + dZLLEW)  + gZl(2)/2.*dZZAEW ]
    ! Zff
    dgZu =  [ gZu(1) * (dZeQEDEW + dswEW/cw2/sw) , 0.5*gZLH * (dZeQEDEW + (sw2-cw2)/cw2*dswEW/sw) + &
                gZu(1) * (dZeQEDEW + dswEW/cw2/sw) ]
    dgZd =  [ gZd(1) * (dZeQEDEW + dswEW/cw2/sw) , -0.5*gZLH * (dZeQEDEW + (sw2-cw2)/cw2*dswEW/sw) + &
                gZd(1) * (dZeQEDEW + dswEW/cw2/sw) ]
    dgZl =  [ gZl(1) * (dZeQEDEW + dswEW/cw2/sw) , -0.5*gZLH * (dZeQEDEW + (sw2-cw2)/cw2*dswEW/sw) + &
                gZl(1) * (dZeQEDEW + dswEW/cw2/sw) ]
    dgZn =  [ ZERO , 0.5*gZLH * (dZeQEDEW + (sw2-cw2)/cw2*dswEW/sw) ]
    EWctVuu  = [ dgZu(1) + gZu(1) * (0.5*dZZZEW + 0.5*(dZuREW+dZuREWcc)) - 2._/**/REALKIND/6.*dZAZEW , &
                 dgZu(2) + gZu(2) * (0.5*dZZZEW + 0.5*(dZuLEW+dZuLEWcc)) - 2._/**/REALKIND/6.*dZAZEW ]
    EWctVdd  = [ dgZd(1) + gZd(1) * (0.5*dZZZEW + 0.5*(dZdREW+dZdREWcc)) + 1._/**/REALKIND/6.*dZAZEW , &
                 dgZd(2) + gZd(2) * (0.5*dZZZEW + 0.5*(dZdLEW+dZdLEWcc)) + 1._/**/REALKIND/6.*dZAZEW ]
    EWctVtt  = [ dgZu(1) + gZu(1) * (0.5*dZZZEW + 0.5*(dZtREW+dZtREWcc)) - 2._/**/REALKIND/6.*dZAZEW , &
                 dgZu(2) + gZu(2) * (0.5*dZZZEW + 0.5*(dZtLEW+dZtLEWcc)) - 2._/**/REALKIND/6.*dZAZEW ]
    EWctVbb  = [ dgZd(1) + gZd(1) * (0.5*dZZZEW + 0.5*(dZbREW+dZbREWcc)) + 1._/**/REALKIND/6.*dZAZEW , &
                 dgZd(2) + gZd(2) * (0.5*dZZZEW + 0.5*(dZbLEW+dZbLEWcc)) + 1._/**/REALKIND/6.*dZAZEW ]
    EWctVee  = [ dgZl(1) + gZl(1) * (0.5*dZZZEW + 0.5*(dZeREW+dZeREWcc)) + 0.5*dZAZEW , &
                 dgZl(2) + gZl(2) * (0.5*dZZZEW + 0.5*(dZeLEW+dZeLEWcc)) + 0.5*dZAZEW ]
    EWctVnn  = [ ZERO , dgZn(2) + gZn(2)* (0.5*dZZZEW + 0.5*(dZnLEW+dZnLEWcc)) ]
! massive tau no supported yet
!    EWctVLL  = [ gZl(1) * (dgZl(1)/gZl(1) + dZZZEW/2. + dZLREW) + 1./2.*dZAZEW , gZl(2) * &
!                (dgZl(2)/gZl(2) + dZZZEW/2. + dZLLEW) + 0.5*dZAZEW ]
    ! Wff
    EWctVdu  = dZeQEDEW-dswEW/sw+0.5*dZWEW+0.5*(dZuLEW + dZdLEWcc)
    EWctVud  = dZeQEDEW-dswEW/sw+0.5*dZWEW+0.5*(dZuLEWcc + dZdLEW)
    EWctVbt  = dZeQEDEW-dswEW/sw+0.5*dZWEW+0.5*(dZtLEW + dZbLEWcc)
    EWctVtb  = dZeQEDEW-dswEW/sw+0.5*dZWEW+0.5*(dZtLEWcc + dZbLEW)
    EWctVen  = dZeQEDEW-dswEW/sw+0.5*dZWEW+0.5*(dZeLEW + dZnLEWcc)
    EWctVne  = dZeQEDEW-dswEW/sw+0.5*dZWEW+0.5*(dZeLEWcc + dZnLEW)


! massive tau no supported yet
!    EWctVLn  = dZeQEDEW-dswEW/sw+dZWEW/2.+(dZLLEW)

    !SFF
    EWctHtt = -0.5/sw*( dZeQEDEW - dswEW/sw + dZMTEW/MT - 0.5*dZMW2EW/MW2 + 0.5*dZHEW) &
              -0.5/sw*0.5*[dZtREW+dZtLEWcc,dZtREWcc+dZtLEW ]
    if (MB /= 0._/**/REALKIND) then
      EWctHbb = -0.5/sw*( dZeQEDEW - dswEW/sw + dZMBEW/MB - 0.5*dZMW2EW/MW2 + 0.5*dZHEW) &
                -0.5/sw*0.5*[dZbREW+dZbLEWcc,dZbREWcc+dZbLEW ]
    else
      EWctHbb = 0.
    end if

! massive tau no supported yet
!    EWctHLL = -1./2./sw*ML*( dZeQEDEW - dswEW/sw + dZMLEW/ML - 0.5*dZMW2EW/MW2 + 0.5*dZHEW + &
!              0.5*(dZbREW+dZbLEW) ) * [1,1]
    EWctXtt = CI/sw*0.5*( dZeQEDEW - dswEW/sw + dZMTEW/MT - 0.5*dZMW2EW/MW2 ) + &
              CI/sw*0.25*[(dZtREW+dZtLEWcc),-1.*(dZtREWcc+dZtLEW)]
    if (MB /= 0._/**/REALKIND) then
      EWctXbb = CI/sw*0.5*( dZeQEDEW - dswEW/sw + dZMBEW/MB - 0.5*dZMW2EW/MW2 ) + &
                CI/sw*0.25*[(dZbREW+dZbLEWcc),-1.*(dZbREWcc+dZbLEW)]
    else
      EWctXbb = 0.
    end if
! massive tau no supported yet
!     EWctXLL = -CI/sw*ML*0.5*( dZeQEDEW - dswEW/sw + dZMLEW/ML - 0.5*dZMW2EW/MW2 + &
!               0.5*(dZLREW+dZLLEW) ) * [1.,-1.]
    if (MB /= 0._/**/REALKIND) then
      EWctPtb = 1./sqrt2/sw*[ -1*MB*(dZeQEDEW - dswEW/sw + dZMBEW/MB - 0.5*dZMW2EW/MW2 + 0.5*(dZtLEWcc+dZbREW)), &
                MT*(dZeQEDEW - dswEW/sw + dZMTEW/MT - 0.5*dZMW2EW/MW2 + 0.5*(dZtREWcc+dZbLEW)) ]
      EWctPbt = 1./sqrt2/sw*[  MT*(dZeQEDEW - dswEW/sw + dZMTEW/MT - 0.5*dZMW2EW/MW2 + 0.5*(dZtREW+dZbLEWcc)), &
                -1*MB*(dZeQEDEW - dswEW/sw + dZMBEW/MB - 0.5*dZMW2EW/MW2 + 0.5*(dZtLEW+dZbREWcc)) ]
    else
      EWctPtb = 1./sqrt2/sw*[ ZERO , &
                MT*(dZeQEDEW - dswEW/sw + dZMTEW/MT - 0.5*dZMW2EW/MW2 + 0.5*(dZtREWcc+dZbLEW)) ]
      EWctPbt = 1./sqrt2/sw*[  MT*(dZeQEDEW - dswEW/sw + dZMTEW/MT - 0.5*dZMW2EW/MW2 + 0.5*(dZtREW+dZbLEWcc)), &
                ZERO ]
    end if

    ! massive tau no supported yet
!     EWctPnL = 1./sqrt2/sw* [ -1*ML*(dZeQEDEW - dswEW/sw + dZMLEW/ML - 0.5*dZMW2EW/MW2  &
!               + 0.5*(dZnLEW+dZLREW)) , ZERO ]
!     EWctPLn = [ZERO, EWctPnL(1)]

    ! VUU
    EWctAUWUW = ( dZeQEDEW + 0.5*dZAAEW ) - 0.5*cw/sw*dZZAEW
    EWctZUWUW = -1*cw/sw*( dZeQEDEW - dswEW/cw2/sw + 0.5*dZZZEW ) + 0.5*dZAZEW
    EWctWUWUZ = cw/sw * ( dZeQEDEW - dswEW/cw2/sw + 0.5*dZWEW )
    EWctWUZUW = -1.*EWctWUWUZ
    EWctWUWUA = -1.*(dZeQEDEW + 0.5*dZWEW )
    EWctWUAUW = -1.*EWctWUWUA

    ! SUU
    EWctHUZUZ  =  ( dZeQEDEW + (2.*sw2-cw2)/cw2*dswEW/sw + 0.5*dZMW2EW/MW2 + 0.5*dZHEW )
    EWctHUWUW  =  ( dZeQEDEW - dswEW/sw + 0.5*dZMW2EW/MW2 + 0.5*dZHEW )
    EWctXUWUW  =  (dZeQEDEW - dswEW/sw + 0.5*dZMW2EW/MW2)
    EWctPUZUW  =  (dZeQEDEW + (sw2-cw2)/cw2*dswEW/sw + 0.5*dZMW2EW )
    EWctPUWUZ  =  ( dZeQEDEW + dswEW/(sw2-cw2)/cw2/sw + 0.5*dZMW2EW/MW2 )
    EWctPUWUA  =  ( dZeQEDEW + 0.5*dZMW2EW/MW2 )

  end if


  ! add R2
  if (R2_is_on /= 0) then

!extracted from Form files


! twopoint
        EWctAA=EWctAA+[cONE*(-3. - (10._/**/REALKIND*nc)/9.), &
                2.*MW2 + 4*nc*sumMQ2Q2,cONE*(2._/**/REALKIND/3.)]

        EWctAZ=EWctAZ+[1./(2.*cw*sw) + cw/sw + nc/(2.*cw*sw) - (2.*sw)/cw -  &
                (10.*nc*sw)/(9.*cw),(-2.*cw*MW2)/sw - (2.*nc*sumMQ2QI)/(cw*sw) +  &
                (4.*nc*sumMQ2Q2*sw)/cw,(-2.*cw)/(3.*sw)]

        EWctZZ=EWctZZ+[1./cw2 + nc/cw2 - 1/(2.*cw2*sw2) - cw2/sw2 -  &
                nc/(2.*cw2*sw2) - (2.*sw2)/cw2 - (10.*nc*sw2)/(9.*cw2), &
               (-4.*nc*sumMQ2QI)/cw2 + (2.*cw2*MW2)/sw2 +  &
                (nc*sumMQ2)/(2.*cw2*sw2) + (4.*nc*sumMQ2Q2*sw2)/cw2, &
               (2.*cw2)/(3.*sw2)]

        EWctWW=EWctWW+[-(3 + nc)/(2*sw2),(2*MW2)/sw2 + (nc*sumMQ2)/(2.*sw2),2/(3.*sw2)]

        EWctHH=EWctHH+[-1/(12.*sw2) - 1/(24.*cw2*sw2) -  &
                (nc*sumMQ2)/(6.*MW2*sw2), &
               (5.*MW2)/(2.*sw2) + (11.*MW2)/(8.*cw4*sw2) - MZ2/(8.*cw2*sw2) -  &
                (nc*sumMQ4)/(MW2*sw2)]

        EWctXX=EWctXX+[-1./(12.*sw2) - 1./(24.*cw2*sw2) -  &
                (nc*sumMQ2)/(6.*MW2*sw2), &
               -MH2/(8.*cw2*sw2) + MW2/(2.*sw2) + (3.*MW2)/(8.*cw4*sw2) -  &
                (nc*sumMQ4)/(MW2*sw2)]

        EWctPP=EWctPP+[-1._/**/REALKIND/12. - 1./(12.*sw2) - cw2/(24.*sw2) -  &
                (nc*sumMQ2)/(6.*MW2*sw2) - sw2/(24.*cw2), &
               (7.*MW2)/4. - (3.*MW2)/(4.*cw2) - MH2/(8.*sw2) + (9*MW2)/(8.*sw2) -  &
                (cw2*MW2)/(8.*sw2) - MZ2/(8.*sw2) - (nc*sumMUD2)/(2.*MW2*sw2) +  &
                (15*MW2*sw2)/(8.*cw2) + (3*MW2*sw2)/(8.*cw4)]

        EWctdd=EWctdd+[1/(9.*cw2),(9. + 18.*cw2 - 8.*sw2)/(36.*cw2*sw2),ZERO,ZERO]*(-1.)

        EWctbb=EWctbb+[1/(9.*cw2),(9 + 18*cw2 - 8*sw2)/(36.*cw2*sw2), &
               -MB/(9.*cw2),-MB/(9.*cw2)]*(-1)

        EWctuu=EWctuu+[4./(9.*cw2),(9. + 18.*cw2 - 8.*sw2)/(36.*cw2*sw2),ZERO,ZERO]*(-1.)

        EWcttt=EWcttt+[4./(9.*cw2),(9. + 18.*cw2 - 8.*sw2)/(36.*cw2*sw2), &
               (2.*MT)/(9.*cw2),(2.*MT)/(9.*cw2)]*(-1.)

        EWctee=EWctee+[1./cw2,(1. + 2*cw2)/(4.*cw2*sw2),ZERO,ZERO]*(-1.)

! ! massive tau no supported yet
!         EWctLL=[1/cw2,(1 + 2*cw2)/(4.*cw2*sw2),(-4 + 5/cw2)*ML, &
!                (-4 + 5/cw2)*ML]*(-1.)

        EWctnn=EWctnn+[ZERO,(1. + 2.*cw2)/(4.*cw2*sw2),ZERO,ZERO]*(-1.)


! three-point
        EWctHtt=EWctHtt+[(2.*cw2*(9.*MB2 + MW2*(9. + 64.*sw2)) +  &
                    MW2*(9. - 96.*sw2 + 128.*sw4))/(144.*cw2*MW2*sw3), &
                    (2.*cw2*(9.*MB2 + MW2*(9. + 64.*sw2)) +  &
                    MW2*(9. - 96.*sw2 + 128.*sw4))/(144.*cw2*MW2*sw3)]

        EWctHbb=EWctHbb+[(2.*cw2*(9.*MT2 + MW2*(9. + 16.*sw2)) +  &
                    MW2*(9. - 48.*sw2 + 32.*sw4))/(144.*cw2*MW2*sw3), &
                    (2.*cw2*(9.*MT2 + MW2*(9. + 16.*sw2)) +  &
                    MW2*(9. - 48.*sw2 + 32.*sw4))/(144.*cw2*MW2*sw3)]

! ! massive tau no supported yet
!         EWctHLL=[(ML*(1 - 16*sw2 + cw2*(2 + 32*sw2) + 32*sw4))/ &
!                 (16.*cw2*sw3),(ML*(1 - 16*sw2 + cw2*(2 + 32*sw2) + 32*sw4))/ &
!                 (16.*cw2*sw3)] &

        EWctXtt=EWctXtt+[(CI*(2.*cw2*(9*MB2 + MW2*(9 + 64*sw2)) +  &
                    MW2*(9 - 96*sw2 + 128*sw4)))/(144.*cw2*MW2*sw3), &
               -(CI*(2*cw2*(9*MB2 + MW2*(9 + 64*sw2)) +  &
                     MW2*(9 - 96*sw2 + 128*sw4)))/(144.*cw2*MW2*sw3)]

        EWctXbb=EWctXbb+[-(CI* &
                   (2*cw2*(9*MT2 + MW2*(9 + 16*sw2)) + MW2*(9 - 48*sw2 + 32*sw4)) &
                   )/(144.*cw2*MW2*sw3), &
               (CI*(2*cw2*(9*MT2 + MW2*(9 + 16*sw2)) +  &
                    MW2*(9 - 48*sw2 + 32*sw4)))/(144.*cw2*MW2*sw3)]

! ! massive tau no supported yet
!         EWctXll=[-(CI*ML*(1 - 16*sw2 + cw2*(2 + 32*sw2) + 32*sw4))/ &
!                 (16.*cw2*sw3),(CI*ML*(1 - 16*sw2 + cw2*(2 + 32*sw2) + 32*sw4))/ &
!                 (16.*cw2*sw3)]

        EWctPbt=EWctPbt+[(MB*(cw2*(18*MT2 + MW2*(27 - 46*sw2)) +  &
                    MW2*(39 - 46*sw2)*sw2))/(72.*cw2*MW2*sqrt2*sw3), &
               (MT*(MW2*sw2*(-87 + 46*sw2) +  &
                    cw2*(-18*MB2 + MW2*(-27 + 46*sw2))))/(72.*cw2*MW2*sqrt2*sw3)]

        EWctPtb=EWctPtb+[(23*MT)/(36.*sqrt2*sw) -  &
                (29*MT)/(24.*cw2*sqrt2*sw) + (23*MT*sw)/(36.*cw2*sqrt2) -  &
                (3*MT)/(8.*sqrt2*sw3) - (MB2*MT)/(4.*MW2*sqrt2*sw3), &
               (-23*MB)/(36.*sqrt2*sw) + (13*MB)/(24.*cw2*sqrt2*sw) -  &
                (23*MB*sw)/(36.*cw2*sqrt2) + (3*MB)/(8.*sqrt2*sw3) +  &
                (MB*MT2)/(4.*MW2*sqrt2*sw3)]

! ! massive tau no supported yet
!         EWctPln=[(ML*(cw2*(3 + 2*sw2) + sw2*(15 + 2*sw2)))/ &
!                 (8.*cw2*sqrt2*sw3),ZERO]

! ! massive tau no supported yet
!         EWctPnl=[ZERO,ML/(4.*sqrt2*sw) + (15*ML)/(8.*cw2*sqrt2*sw) +  &
!                 (ML*sw)/(4.*cw2*sqrt2) + (3*ML)/(8.*sqrt2*sw3)]

        EWctAuu=EWctAuu+[16/(27.*cw2),-8/(27.*cw2) + 2/(3.*sw2) + 1/(3.*cw2*sw2)]

        EWctAdd=EWctAdd+[-2/(27.*cw2),4/(27.*cw2) - 1/(3.*sw2) - 1/(6.*cw2*sw2)]

        EWctAtt=EWctAtt+[16/(27.*cw2) + MT2/(12.*MW2*sw2), &
               -8/(27.*cw2) + 2/(3.*sw2) + 1/(3.*cw2*sw2) - MB2/(12.*MW2*sw2) +  &
                MT2/(6.*MW2*sw2)]

        EWctAbb=EWctAbb+[-2/(27.*cw2) + MB2/(12.*MW2*sw2), &
               4/(27.*cw2) - 1/(3.*sw2) - 1/(6.*cw2*sw2) - MB2/(12.*MW2*sw2) +  &
                MT2/(6.*MW2*sw2)]

        EWctAee=EWctAee+[-2/cw2,-(1/sw2) - 1/(2.*cw2*sw2)]

! ! massive tau no supported yet
!         EWctAll=[-2/cw2 - ML2/(4.*MW2*sw2), &
!                -(1/sw2) - 1/(2.*cw2*sw2) - ML2/(4.*MW2*sw2)]

        EWctVuu=EWctVuu+[(16*sw)/(27.*cw3), &
               -7/(9.*cw*sw) + 1/(cw3*sw) + (16*sw)/(27.*cw) - (4*sw)/(3.*cw3) +  &
                1/(2.*cw*sw3) - cw/sw3 - 1/(4.*cw3*sw3) + (16*sw3)/(27.*cw3)]

        EWctVdd=EWctVdd+[(-2*sw)/(27.*cw3), &
               7/(9.*cw*sw) - 1/(2.*cw3*sw) - (2*sw)/(27.*cw) + sw/(3.*cw3) -  &
                1/(2.*cw*sw3) + cw/sw3 + 1/(4.*cw3*sw3) - (2*sw3)/(27.*cw3)]

        EWctVtt=EWctVtt+[MT2/(12.*cw*MW2*sw) + (16*sw)/(27.*cw) +  &
                (16*sw3)/(27.*cw3),-7/(9.*cw*sw) + 1/(cw3*sw) -  &
                MB2/(12.*cw*MW2*sw) + MT2/(6.*cw*MW2*sw) + (16*sw)/(27.*cw) -  &
                (4*sw)/(3.*cw3) + 1/(2.*cw*sw3) - cw/sw3 - 1/(4.*cw3*sw3) +  &
                (16*sw3)/(27.*cw3)]

        EWctVbb=EWctVbb+[MB2/(12.*cw*MW2*sw) - (2*sw)/(27.*cw) -  &
                (2*sw3)/(27.*cw3),7/(9.*cw*sw) - 1/(2.*cw3*sw) -  &
                MB2/(12.*cw*MW2*sw) + MT2/(6.*cw*MW2*sw) - (2*sw)/(27.*cw) +  &
                sw/(3.*cw3) - 1/(2.*cw*sw3) + cw/sw3 + 1/(4.*cw3*sw3) -  &
                (2*sw3)/(27.*cw3)]

        EWctVee=EWctVee+[(-2*sw)/cw3, &
               1/(cw*sw) - 3/(2.*cw3*sw) - (2*sw)/cw + (3*sw)/cw3 -  &
                1/(2.*cw*sw3) + cw/sw3 + 1/(4.*cw3*sw3) - (2*sw3)/cw3]

        EWctVnn=EWctVnn+[ZERO,-(1/(cw*sw)) + 1/(2.*cw*sw3) - cw/sw3 - 1/(4.*cw3*sw3)]

        EWctVdu=EWctVdu-5/(9.*cw2) - 2/sw2 + 1/(2.*cw2*sw2)

        EWctVbt=EWctVbt-5/(9.*cw2) - 2/sw2 + 1/(2.*cw2*sw2)

        EWctVen=EWctVen-(1/cw2) - 2/sw2 + 1/(2.*cw2*sw2)

        EWctVud=EWctVud-5/(9.*cw2) - 2/sw2 + 1/(2.*cw2*sw2)

        EWctVtb=EWctVtb-5/(9.*cw2) - 2/sw2 + 1/(2.*cw2*sw2)

        EWctVne=EWctVne-(1/cw2) - 2/sw2 + 1/(2.*cw2*sw2)

        EWctHHH=EWctHHH-1/(4.*sw2) - 1/(8.*cw2*sw2) + (3*MW2)/(2.*MH2*sw2) +  &
               (3*MW2)/(4.*cw4*MH2*sw2) - (nc*sumMQ4)/(MH2*MW2*sw2)

        EWctHXX=EWctHXX-1/(4.*sw2) - 1/(8.*cw2*sw2) + (3*MW2)/(2.*MH2*sw2) +  &
               (3*MW2)/(4.*cw4*MH2*sw2) - (nc*sumMQ4)/(MH2*MW2*sw2)

        EWctHPP=EWctHPP-0.125 + (7*MW2)/(2.*MH2) - (2*MW2)/(cw2*MH2) -  &
               3/(8.*sw2) + (9*MW2)/(4.*MH2*sw2) - (nc*sumMQ4)/(MH2*MW2*sw2) -  &
               sw2/(8.*cw2) + (7*MW2*sw2)/(2.*cw2*MH2) + (3*MW2*sw2)/(4.*cw4*MH2)

        EWctAXH=EWctAXH+(-5*CI)/(12.*sw2)

        EWctZXH=EWctZXH+(CI*(MW2 + 22*cw4*MW2 + 2*cw2*(4*nc*sumMQ2 + MW2*sw2)))/ &
               (48.*cw3*MW2*sw3)

        EWctAPP=EWctAPP+1/(24.*cw2) + 13/(24.*sw2) + (nc*sumMQ2)/(3.*MW2*sw2)

        EWctZPP=EWctZPP+(nc*sumMQ2)/(3.*cw*MW2*sw) + sw/(48.*cw) +  &
               1/(24.*cw*sw3) - (25*cw)/(48.*sw3) -  &
               (nc*sumMQ2)/(6.*cw*MW2*sw3) + sw3/(48.*cw3)

        EWctWPH=EWctWPH+1/(48.*cw2*sw) + 23/(48.*sw3) + (nc*sumMQ2)/(6.*MW2*sw3)

        EWctWPX=EWctWPX+CI/(48.*cw2*sw) + (23*CI)/(48.*sw3) +  &
               (CI*nc*sumMQ2)/(6.*MW2*sw3)

        EWctHAA=EWctHAA-(MW/sw) - (2*nc*sumMQ2Q2)/(MW*sw)

        EWctHZA=EWctHZA+MW/(2.*cw) - (2*nc*sumMQ2Q2)/(cw*MW) +  &
               (3*cw*MW)/(2.*sw2) + (nc*sumMQ2QI)/(cw*MW*sw2)

        EWctHZZ=EWctHZZ+MW/sw + (2*nc*sumMQ2QI)/(cw2*MW*sw) -  &
               (2*nc*sumMQ2Q2*sw)/(cw2*MW) - (2*MW)/sw3 -  &
               (nc*sumMQ2)/(2.*cw2*MW*sw3)

        EWctHWW=EWctHWW+(-2*MW)/sw3 - (nc*sumMQ2)/(2.*MW*sw3)

        EWctPWA=EWctPWA+MW/(2.*sw2) + (nc*sumMQ2QUD)/(2.*MW*sw2)

        EWctPWZ=EWctPWZ+MW/(2.*cw*sw) + (nc*sumMQ2QUD)/(2.*cw*MW*sw)

        EWctAWW=EWctAWW - (17+6*nc)/(6.*sw2)

        EWctZWW=EWctZWW + cw*(17+6*nc)/(6.*sw3)

! EWctGff see V2
        EWctGuu=EWctGuu + [8/(9.*cw2),-4/(9.*cw2) + 1/sw2 + 1/(2.*cw2*sw2)]*(-1.)

        EWctGdd=EWctGdd + [2/(9.*cw2),-4/(9.*cw2) + 1/sw2 + 1/(2.*cw2*sw2)]*(-1.)

        EWctGtt=EWctGtt + [8/(9.*cw2) + MT2/(2.*MW2*sw2), &
                  -4/(9.*cw2) + 1/sw2 + 1/(2.*cw2*sw2) + MB2/(4.*MW2*sw2) +  &
                  MT2/(4.*MW2*sw2)]*(-1.)

        EWctGbb=EWctGbb + [2/(9.*cw2) + MB2/(2.*MW2*sw2), &
                  -4/(9.*cw2) + 1/sw2 + 1/(2.*cw2*sw2) + MB2/(4.*MW2*sw2) +  &
                  MT2/(4.*MW2*sw2)]*(-1.)

! four-point

        EWctHHHH=EWctHHHH-3/(2.*sw2) - 3/(4.*cw2*sw2) + (11*MW2)/(2.*MH2*sw2) +  &
               (11*MW2)/(4.*cw4*MH2*sw2) - (5*nc*sumMQ4)/(MH2*MW2*sw2)

        EWctXXXX=EWctXXXX-3/(2.*sw2) - 3/(4.*cw2*sw2) + (11*MW2)/(2.*MH2*sw2) +  &
               (11*MW2)/(4.*cw4*MH2*sw2) - (5*nc*sumMQ4)/(MH2*MW2*sw2)

        EWctHHXX=EWctHHXX-3/(2.*sw2) - 3/(4.*cw2*sw2) + (11*MW2)/(2.*MH2*sw2) +  &
               (11*MW2)/(4.*cw4*MH2*sw2) - (5*nc*sumMQ4)/(MH2*MW2*sw2)

        EWctHHPP=EWctHHPP-3/(2.*sw2) - 3/(4.*cw2*sw2) + (11*MW2)/(2.*MH2*sw2) +  &
               (11*MW2)/(4.*cw4*MH2*sw2) - (5*nc*sumMQ4)/(MH2*MW2*sw2)

        EWctXXPP=EWctXXPP-0.125 + (41*MW2)/(12.*MH2) - (2*MW2)/(cw2*MH2) -  &
               5/(8.*sw2) - 1/(8.*cw2*sw2) + (7*MW2)/(3.*MH2*sw2) +  &
               (5*MW2)/(12.*cw2*MH2*sw2) - (5*nc*sumMQ4)/(3.*MH2*MW2*sw2) -  &
               sw2/(8.*cw2) + (41*MW2*sw2)/(12.*cw2*MH2) +  &
               (11*MW2*sw2)/(12.*cw4*MH2)

        EWctPPPP=EWctPPPP-0.5 + (11*MW2)/(3.*MH2) - 3/(2.*sw2) +  &
               (11*MW2)/(2.*MH2*sw2) - (10*nc*sumMQ4)/(3.*MH2*MW2*sw2) -  &
               sw2/(2.*cw2) + (11*MW2*sw2)/(2.*MH2) +  &
               (22*MW2*sw4)/(3.*cw2*MH2) + (11*MW2*sw6)/(6.*cw4*MH2)

        EWctAAHH=EWctAAHH+1/(12.*sw2) - (nc*sumMQ2Q2)/(MW2*sw2)

        EWctAAXX=EWctAAXX+1/(12.*sw2) - (nc*sumMQ2Q2)/(MW2*sw2)

        EWctZAHH=EWctZAHH+2./(3.*cw*sw) - (nc*sumMQ2Q2)/(cw*MW2*sw) - 1/(2.*sw2) +  &
               cw/(12.*sw3) + (nc*sumMQ2QI)/(2.*cw*MW2*sw3)

!        EWctZAXX=2/(3.*cw*sw) - (nc*sumMQ2Q2)/(cw*MW2*sw) - 1/(2.*sw2) +  &
!               cw/(12.*sw3) + (nc*sumMQ2QI)/(2.*cw*MW2*sw3)

        EWctZZHH=EWctZZHH-1/(24.*cw2) - (nc*sumMQ2Q2)/(cw2*MW2) - 1/(8.*sw2) +  &
               (nc*sumMQ2QI)/(cw2*MW2*sw2) - 19/(24.*sw4) - 1/(48.*cw4*sw4) -  &
               (nc*sumMQ2)/(3.*cw2*MW2*sw4)

        EWctZZXX=EWctZZXX-1/(24.*cw2) - (nc*sumMQ2Q2)/(cw2*MW2) - 1/(8.*sw2) +  &
               (nc*sumMQ2QI)/(cw2*MW2*sw2) - 19/(24.*sw4) - 1/(48.*cw4*sw4) -  &
               (nc*sumMQ2)/(3.*cw2*MW2*sw4)

        EWctWWHH=EWctWWHH-19/(24.*sw4) - 1/(48.*cw2*sw4) - (nc*sumMQ2)/(3.*MW2*sw4)

        EWctWWXX=EWctWWXX-19/(24.*sw4) - 1/(48.*cw2*sw4) - (nc*sumMQ2)/(3.*MW2*sw4)

        EWctWAPH=EWctWAPH+1/(2.*sw) + 1/(48.*cw2*sw) - cw/(2.*sw2) +  &
               11/(48.*sw3) + (nc*sumMD2)/(4.*MW2*sw3) + (nc*sumMU2)/(6.*MW2*sw3)

        EWctWAPX=EWctWAPX-CI/(2.*sw) - CI/(48.*cw2*sw) + (CI*cw)/(2.*sw2) -  &
               (11*CI)/(48.*sw3) - (CI*nc*sumMD2)/(4.*MW2*sw3) -  &
               (CI*nc*sumMU2)/(6.*MW2*sw3)

        EWctWZPH=EWctWZPH+1/(24.*cw3) + 1/(2.*sw) + 5/(48.*cw*sw2) +  &
               cw/(2.*sw2) - 1/(48.*cw3*sw2) + (nc*sumMD2)/(4.*cw*MW2*sw2) +  &
               (nc*sumMU2)/(6.*cw*MW2*sw2) + 7/(48.*cw*sw4) - (7*cw)/(48.*sw4)

        EWctWZPX=EWctWZPX-CI/(24.*cw3) - CI/(2.*sw) - (5*CI)/(48.*cw*sw2) -  &
               (CI*cw)/(2.*sw2) + CI/(48.*cw3*sw2) -  &
               (CI*nc*sumMD2)/(4.*cw*MW2*sw2) - (CI*nc*sumMU2)/(6.*cw*MW2*sw2) -  &
               (7*CI)/(48.*cw*sw4) + (7*CI*cw)/(48.*sw4)

        EWctAAPP=EWctAAPP-1._/**/REALKIND/12. - 11/(6.*sw2) -  &
               (10*nc*sumMQ2)/(9.*MW**2*sw2) - sw2/(12.*cw2)

        EWctZAPP=EWctZAPP-0.25 - 1/(2.*cw*sw) - (10*nc*sumMD2)/(9.*cw*MW2*sw) -  &
               (10*nc*sumMU2)/(9.*cw*MW2*sw) + sw/(12.*cw) - 1/(4.*sw2) -  &
               sw2/(4.*cw2) + (7*cw)/(6.*sw3) + (7*nc*sumMD2)/(12.*cw*MW2*sw3) +  &
               (nc*sumMU2)/(2.*cw*MW2*sw3) + sw3/(12.*cw3)

        EWctZZPP=EWctZZPP+1._/**/REALKIND/48. -  &
               (10*nc*sumMD2)/(9.*cw**2*MW**2) -  &
               (10*nc*sumMU2)/(9.*cw**2*MW**2) - 37/(48.*sw**4) -  &
               1/(24.*cw**2*sw**4) - (nc*sumMD2)/(3.*cw**2*MW**2*sw**4) -  &
               (nc*sumMU2)/(3.*cw**2*MW**2*sw**4) + 43/(24.*sw**2) +  &
               (7*nc*sumMD2)/(6.*cw**2*MW**2*sw**2) +  &
               (nc*sumMU2)/(cw**2*MW**2*sw**2) - sw**4/(48.*cw**4)

        EWctWWPP=EWctWWPP-0.25 - 1/(768.*cw2) + cw/(4.*sw) + 119/(768.*sw2) -  &
               15/(256.*sw4) - (nc*sumMQ2)/(48.*MW2*sw4)

        EWctR2AAAA=(4*(80._/**/REALKIND + (17*nc)/27._/**/REALKIND))/3.

        EWctR2AAAZ=-9/(cw*sw) + (4*cw)/(3.*sw) - nc/(3.*cw*sw) +  &
                (108*sw)/cw + (68*nc*sw)/(81.*cw)

        EWctR2AAZZ=4._/**/REALKIND/3. - 18/cw2 - (2*nc)/(3.*cw2) -  &
                4/(3.*sw2) + 1/(2.*cw2*sw2) + (5*nc)/(18.*cw2*sw2) +  &
                (108*sw2)/cw2 + (68*nc*sw2)/(81.*cw2)

        EWctR2AZZZ=(-4*cw)/(3.*sw) + 3/(2.*cw3*sw) +  &
                (5*nc)/(6.*cw3*sw) - (27*sw)/cw3 - (nc*sw)/cw3 +  &
                (4*cw)/(3.*sw3) - 1/(4.*cw3*sw3) - nc/(4.*cw3*sw3) +  &
                (108*sw3)/cw3 + (68*nc*sw3)/(81.*cw3)

        EWctR2ZZZZ=-4._/**/REALKIND/3. + 3/cw4 + (5._/**/REALKIND*nc)/(3.*cw4) +  &
                8/(3.*sw2) - 1/(cw4*sw2) - nc/(cw4*sw2) - (36*sw2)/cw4 -  &
                (4*nc*sw2)/(3.*cw4) - 4/(3.*sw4) + 1/(6.*cw4*sw4) +  &
                (108*sw4)/cw4 + (68*nc*sw4)/(81.*cw4)

        EWctWWAA=EWctWWAA+[19/(3.*sw2) + (25*nc)/(9.*sw2), &
               -10/(3.*sw2) - (11*nc)/(9.*sw2)]

        EWctWWAZ=EWctWWAZ+[3/(cw*sw) + (25*nc)/(9.*cw*sw) - 11/(4.*cw*sw3) -  &
                (10*cw)/(3.*sw3) - (11*nc)/(4.*cw*sw3), &
               -(1/(cw*sw)) - (11*nc)/(9.*cw*sw) + 5/(4.*cw*sw3) +  &
                (7*cw)/(3.*sw3) + (5*nc)/(4.*cw*sw3)]

        EWctWWZZ=EWctWWZZ+[3/cw2 + (25*nc)/(9.*cw2) - 10/(3.*sw2) -  &
                11/(2.*cw2*sw2) - (11*nc)/(2.*cw2*sw2) + 10/(3.*sw4) +  &
                11/(6.*cw2*sw4),-(1/cw2) - (11*nc)/(9.*cw2) + 7/(3.*sw2) +  &
                5/(2.*cw2*sw2) + (5*nc)/(2.*cw2*sw2) - 7/(3.*sw4) -  &
                5/(6.*cw2*sw4)]

        EWctWWWW=EWctWWWW+[-17./(2.*sw4) - (5.*nc)/(2.*sw4), &
               19/(6.*sw4) + (3*nc)/(2.*sw4)]

  end if



! add twopoint-Tadpoles (calculated in D=4)

  if (TP_is_on /= 0) then

    EWctAA = EWctAA + [ ZERO, 8.*A0W, ZERO ]

    EWctZZ = EWctZZ + [ ZERO, 0.25/(sw2*cw2)*(A0Z+A0H) + &
                      ((sw2-cw2)**2/(2.*sw2*cw2)+6.*cw2/sw2)*A0W, ZERO]

    EWctAZ = EWctAZ + [ ZERO, ((sw2-cw2)/(sw*cw)-6.*cw/sw)*A0W, ZERO]

    EWctWW = EWctWW + [ ZERO, (0.25/sw2+3.*cw2/sw2)*A0Z + 3.5/sw2*A0W + &
                               0.25/sw2*A0H, ZERO]


    EWctHH = EWctHH+[ZERO, -1./(2.*sw2)*(4.*A0W+2./cw2*A0Z+ &
                    (3*MH2)/(4*MW2)*A0H+MH2/(4*MW2)*A0Z+MH2/(2*MW2)*A0W)]

    EWctXX = EWctXX+[ZERO, -1./(2.*sw2)*(4.*A0W+2./cw2*A0Z+ &
                    MH2/(4*MW2)*A0H+(3.*MH2)/(4*MW2)*A0Z+MH2/(2*MW2)*A0W)]

    EWctPP = EWctPP+[ZERO, -1./(2.*sw2)*(4.*A0W+2.*(sw2-cw2)**2/cw2*A0Z+ &
                    MH2/(4*MW2)*A0H+MH2/(4*MW2)*A0Z+MH2/MW2*A0W)]


  end if


        if (debug_ew_renorm .eq. 2) then
          print*, "DEBUG"
          print*, "DEBUG EWctHH=", EWctHH
          print*, "DEBUG EWctXX=", EWctXX
          print*, "DEBUG EWctPP=", EWctPP
          print*, "DEBUG EWctAA=", EWctAA
          print*, "DEBUG EWctAZ=", EWctAZ
          print*, "DEBUG EWctZZ=", EWctZZ
          print*, "DEBUG EWctWW=", EWctWW
          print*, "DEBUG EWctuu=", EWctuu
          print*, "DEBUG EWctdd=", EWctdd
          print*, "DEBUG EWcttt=", EWcttt
          print*, "DEBUG EWctbb=", EWctbb
          print*, "DEBUG EWctee=", EWctee
          print*, "DEBUG EWctnn=", EWctnn
          print*, "DEBUG EWctVbt=", EWctVbt
          print*, "DEBUG EWctVdu=", EWctVdu
        end if


! set back possible complex masses
  if ( cms_on == 0 ) then
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
  end if


!interfaces for scalar one-point & two-point functions
  contains

  function calcA0(m2_in)
    implicit none
    complex(REALKIND) calcA0
    complex(REALKIND), intent(in) :: m2_in

    if (abs(m2_in) > eps) then
      calcA0 = m2_in*(de1_UV+log(mureg2/m2_in)+1)
    else
      calcA0 = 0
    endif

    return
  end function calcA0


  function calcB0(p2_in,m12_in,m22_in)
    use ol_parameters_decl_/**/DREALKIND, only: ew_renorm_switch, coli_cache_use
    use ol_loop_parameters_decl_/**/DREALKIND, only: a_switch
#if defined(USE_COLLIER) && !defined(COLLIER_LEGACY)
    use collier, only: setmode_cll
    use collier_coefs, only: B0_cll
    use cache, only: SwitchOffCacheSystem_cll, SwitchOnCacheSystem_cll
#endif
#ifdef USE_ONELOOP
    use avh_olo_/**/REALKIND
#endif
    implicit none
    complex(REALKIND) calcB0
    complex(REALKIND), intent(in) :: p2_in
    complex(REALKIND), intent(in) :: m12_in
    complex(REALKIND), intent(in) :: m22_in
    complex(REALKIND) p2q
    complex(DREALKIND) p2
    complex(DREALKIND) m12
    complex(DREALKIND) m22
    complex(DREALKIND) B0_coli
#if defined(COLLIER_LEGACY)
    complex(DREALKIND) B0,B1(1),B2(0:1,0:1),B3(0:1,0:1,0:1)
    complex(DREALKIND) B4(0:1,0:1,0:1,0:1),B5(0:1,0:1,0:1,0:1,0:1)
    complex(DREALKIND) B6(0:1,0:1,0:1,0:1,0:1,0:1)
#endif
#ifdef USE_ONELOOP
    complex(REALKIND) :: rslt(0:2)
#endif

    calcB0 = 0

    p2  = p2_in
    m12 = m12_in
    m22 = m22_in

#if defined(USE_COLLIER)
#if defined(COLLIER_LEGACY)
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      p2 = real(p2)
      calcB0 = B0_coli(p2,m12,m22)
      if (ew_renorm_switch == 99) then
        print*, "B0 CO:  ", calcB0
      end if
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call xB012345_(real(p2),m12,m22,B0,B1,B2,B3,B4,B5,B6,0,0)
      calcB0 = B0
      if (ew_renorm_switch == 99) then
        print*, "B0 DD:  ", calcB0
      end if
    end if
#else
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOffCacheSystem_cll
    end if
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      call setmode_cll(1)
      p2 = real(p2)
      call B0_cll(B0_coli,p2,m12,m22)
      calcB0 = B0_coli
      if (ew_renorm_switch == 99) then
        print*, "B0 CO:  ", B0_coli
      end if
      if (a_switch == 7) call setmode_cll(2)
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call setmode_cll(2)
      p2 = real(p2)
      call B0_cll(B0_coli,p2,m12,m22)
      calcB0 = B0_coli
      if (ew_renorm_switch == 99) then
        print*, "B0 DD:  ", B0_coli
      end if
      if (a_switch == 1) call setmode_cll(1)
    end if
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOnCacheSystem_cll
    end if
#endif
#endif

#ifdef USE_ONELOOP
    if (ew_renorm_switch == 3 .or. ew_renorm_switch == 99) then
      p2q = real(p2_in)
      call olo_b0(rslt,real(p2q),m12_in,m22_in)
      calcB0 = rslt(0) + rslt(1)*de1_IR + rslt(2)*de2_i_IR
      if (ew_renorm_switch == 99) then
        print*, "B0 OLO: ", calcB0
      end if
    end if
#endif

      return
  end function calcB0


  function calcdB0(p2_in,m12_in,m22_in)
    use ol_parameters_decl_/**/DREALKIND, only: ew_renorm_switch, coli_cache_use
    use ol_loop_parameters_decl_/**/DREALKIND, only: a_switch
#if defined(USE_COLLIER) && !defined(COLLIER_LEGACY)
    use collier, only: setmode_cll
    use collier_coefs, only: DB0_cll
    use cache, only: SwitchOffCacheSystem_cll, SwitchOnCacheSystem_cll
#endif
#ifdef USE_ONELOOP
    use avh_olo_/**/REALKIND
#endif
    implicit none
    complex(REALKIND) calcdB0
    complex(REALKIND), intent(in) :: p2_in
    complex(REALKIND), intent(in) :: m12_in
    complex(REALKIND), intent(in) :: m22_in
    complex(REALKIND) :: p2q
    complex(DREALKIND) :: p2
    complex(DREALKIND) :: m12
    complex(DREALKIND) :: m22
    complex(DREALKIND) DB0_coli
#if defined(COLLIER_LEGACY)
    complex(DREALKIND) DB0,DB1
#endif
#ifdef USE_ONELOOP
    complex(REALKIND) :: rslt(0:2)
#endif

    calcdB0 = 0

    p2  = p2_in
    m12 = m12_in
    m22 = m22_in

#if defined(USE_COLLIER)
#if defined(COLLIER_LEGACY)
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      p2 = real(p2)
      calcdB0 = DB0_coli(p2,m12,m22)
      if (ew_renorm_switch == 99) then
        print*, "dB0 CO:  ", calcdB0
      end if
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call DB_dd(DB0,DB1,real(p2),m12,m22,0)
      calcdB0 = DB0
      if (ew_renorm_switch == 99) then
        print*, "dB0 DD:  ", calcdB0
      end if
    end if
#else
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOffCacheSystem_cll
    end if
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      call setmode_cll(1)
      p2 = real(p2)
      call DB0_cll(DB0_coli,p2,m12,m22)
      calcdB0 = DB0_coli
      if (ew_renorm_switch == 99) then
        print*, "dB0 CO:  ", DB0_coli
      end if
      if (a_switch == 7) call setmode_cll(2)
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call setmode_cll(2)
      p2 = real(p2)
      call DB0_cll(DB0_coli,p2,m12,m22)
      calcdB0 = DB0_coli
      if (ew_renorm_switch == 99) then
        print*, "dB0 DD:  ", DB0_coli
      end if
      if (a_switch == 1) call setmode_cll(1)
    end if
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOnCacheSystem_cll
    end if
#endif
#endif

#ifdef USE_ONELOOP
    if (ew_renorm_switch == 3 .or. ew_renorm_switch == 99) then
      p2q = real(p2_in)
      if (p2q == 0. .and. m12 == 0. .and. m22 == 0. ) then
        calcdB0 = 0.
      else
        call olo_db0(rslt,real(p2q),m12_in,m22_in)
        calcdB0 = rslt(0) + rslt(1)*de1_IR + rslt(2)*de2_i_IR
      end if
      if (ew_renorm_switch == 99) then
        print*, "dB0 OLO: ", calcdB0
      end if
    end if
#endif

    return
  end function calcdB0


  function calcB1(p2_in,m12_in,m22_in)
    use ol_parameters_decl_/**/DREALKIND, only: ew_renorm_switch, coli_cache_use
    use ol_loop_parameters_decl_/**/DREALKIND, only: a_switch
#if defined(USE_COLLIER) && !defined(COLLIER_LEGACY)
    use collier, only: setmode_cll
    use collier_coefs, only: B_cll
    use cache, only: SwitchOffCacheSystem_cll, SwitchOnCacheSystem_cll
#endif
#ifdef USE_ONELOOP
    use avh_olo_/**/REALKIND
#endif
    implicit none
    complex(REALKIND) calcB1
    complex(REALKIND), intent(in) :: p2_in
    complex(REALKIND), intent(in) :: m12_in
    complex(REALKIND), intent(in) :: m22_in
    complex(DREALKIND) :: p2
    complex(DREALKIND) :: m12
    complex(DREALKIND) :: m22
    complex(DREALKIND) B1_coli
#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
    complex(DREALKIND) B0,B1(1),B2(0:1,0:1),B3(0:1,0:1,0:1)
    complex(DREALKIND) B4(0:1,0:1,0:1,0:1),B5(0:1,0:1,0:1,0:1,0:1)
    complex(DREALKIND) B6(0:1,0:1,0:1,0:1,0:1,0:1)
#endif
#if defined(USE_COLLIER) && !defined(COLLIER_LEGACY)
    complex(DREALKIND) B(0:1,0:1), Buv(0:1,0:1)
#endif
#ifdef USE_ONELOOP
    complex(REALKIND) :: rslt_b11(0:2), rslt_b00(0:2), rslt_b1(0:2), rslt_b0(0:2)
#endif

    calcB1 = 0

    p2  = p2_in
    m12 = m12_in
    m22 = m22_in

#if defined(USE_COLLIER)
#if defined(COLLIER_LEGACY)
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      p2 = real(p2)
      calcB1 = B1_coli(p2,m12,m22)
      if (ew_renorm_switch == 99) then
        print*, "B1 CO:  ", calcB1
      end if
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call xB012345_(real(p2),m12,m22,B0,B1,B2,B3,B4,B5,B6,1,0)
      calcB1 = B1(1)
      if (ew_renorm_switch == 99) then
        print*, "B1 DD:  ", calcB1
      end if
    end if
#else
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOffCacheSystem_cll
    end if
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      call setmode_cll(1)
      p2 = real(p2)
      call B_cll(B,Buv,p2,m12,m22,1)
      calcB1 = B(1,0)
      if (ew_renorm_switch == 99) then
        print*, "B1 CO:  ", calcB1
      end if
      if (a_switch == 7) call setmode_cll(2)
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call setmode_cll(2)
      p2 = real(p2)
      call B_cll(B,Buv,p2,m12,m22,1)
      calcB1 = B(1,0)
      if (ew_renorm_switch == 99) then
        print*, "B1 DD:  ", calcB1
      end if
      if (a_switch == 1) call setmode_cll(1)
    end if
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOnCacheSystem_cll
    end if
#endif
#endif

#ifdef USE_ONELOOP
    if (ew_renorm_switch == 3 .or. ew_renorm_switch == 99) then
      call olo_b11(rslt_b11,rslt_b00,rslt_b1,rslt_b0,real(p2_in),m12_in,m22_in)
      calcB1 = rslt_b1(0) + rslt_b1(1)*de1_IR + rslt_b1(2)*de2_i_IR
      if (ew_renorm_switch == 99) then
        print*, "B1 OLO: ", calcB1
      end if
    end if
#endif

    return
  end function calcB1

  function calcdB1(p2_in,m12_in,m22_in)
    use ol_parameters_decl_/**/DREALKIND, only: ew_renorm_switch, coli_cache_use
    use ol_loop_parameters_decl_/**/DREALKIND, only: a_switch
#if defined(USE_COLLIER) && !defined(COLLIER_LEGACY)
    use collier, only: setmode_cll
    use collier_coefs, only: DB1_cll
    use cache, only: SwitchOffCacheSystem_cll, SwitchOnCacheSystem_cll
#endif
    implicit none
    complex(REALKIND) calcdB1
    complex(REALKIND), intent(in) :: p2_in
    complex(REALKIND), intent(in) :: m12_in
    complex(REALKIND), intent(in) :: m22_in
    complex(REALKIND) :: p2q
    complex(DREALKIND) :: p2, m12, m22
    complex(DREALKIND) DB1_coli
#if defined(USE_COLLIER) && defined(COLLIER_LEGACY)
    complex(REALKIND) DB0,DB1
#endif

    calcdB1 = 0

    p2  = p2_in
    m12 = m12_in
    m22 = m22_in

#if defined(USE_COLLIER)
#if defined(COLLIER_LEGACY)
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      p2 = real(p2)
      calcdB1 = DB1_coli(p2,m12,m22)
      if (ew_renorm_switch == 99) then
        print*, "dB1 CO:  ", calcdB1
      end if
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call DB_dd(DB0,DB1,real(p2),m12,m22,0)
      calcdB1 = DB1
      if (ew_renorm_switch == 99) then
        print*, "dB1 DD:  ", calcdB1
      end if
    end if
#else
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOffCacheSystem_cll
    end if
    if (ew_renorm_switch == 1 .or. ew_renorm_switch == 99) then
      call setmode_cll(1)
      p2 = real(p2)
      call DB1_cll(DB1_coli,p2,m12,m22)
      calcdB1 = DB1_coli
      if (ew_renorm_switch == 99) then
        print*, "dB1 CO:  ", calcdB1
      end if
      if (a_switch == 7) call setmode_cll(2)
    end if
    if (ew_renorm_switch == 7 .or. ew_renorm_switch == 99) then
      call setmode_cll(2)
      p2 = real(p2)
      call DB1_cll(DB1_coli,p2,m12,m22)
      calcdB1 = DB1_coli
      if (ew_renorm_switch == 99) then
        print*, "dB1 DD:  ", calcdB1
      end if
      if (a_switch == 1) call setmode_cll(1)
    end if
    if ((ew_renorm_switch == 1 .or. ew_renorm_switch == 7 .or. ew_renorm_switch == 99) &
          .and. coli_cache_use == 1) then
      call SwitchOnCacheSystem_cll
    end if
#endif
#endif

#ifdef USE_ONELOOP
    if (ew_renorm_switch == 3 .or. ew_renorm_switch == 99) then
      p2 = real(p2_in)
      if (abs(p2) > eps) then
        calcdB1 = - (m22_in-m12_in)/2/p2**2*(calcB0(p2_in,m12_in,m22_in)-calcB0(ZERO,m12_in,m22_in)) &
       &          + (m22_in-m12_in-p2)/2/p2*calcdB0(p2_in,m12_in,m22_in)
      else
        if (abs(m12_in) < eps .and. abs(m22_in) < eps) then
          calcdB1 = 0
        else if (abs(m12_in) < eps .and. abs(m22_in) > eps) then
          calcdB1 = -1/m22_in/6
        else if (abs(m12_in) > eps .and. abs(m22_in) < eps) then
          calcdB1 = -1/m12_in/6
        else if (m12_in == m22_in) then
          calcdB1 = -1/m12_in/12
        else
          calcdB1 = -(2.*m12_in**3+3.*m12_in**2*m22_in-6.*m12_in*m22_in**2+m22_in**3 &
       &              +6.*m12_in**2*m22_in*log(m22_in/m12_in))/6./(m12_in-m22_in)**4
        end if
      end if
      if (ew_renorm_switch == 99) then
        print*, "dB1 OLO: ", calcdB1
      end if
    end if
#endif

    return
  end function calcdB1



  subroutine masspowers(rM, Ga, M, M2, rM2)
    use KIND_TYPES, only: REALKIND
    use ol_parameters_decl_/**/REALKIND, only: CI
    implicit none
    real(REALKIND),    intent(in)  :: rM, Ga
    complex(REALKIND), intent(out) :: M,  M2
    real(REALKIND),    intent(out) :: rM2
    M2  = rM*rM - CI*rM*Ga
    M   = sqrt(M2)
    rM2 = real(M2)
  end subroutine masspowers

end subroutine ew_renormalisation

end module ol_ew_renormalisation_/**/REALKIND
