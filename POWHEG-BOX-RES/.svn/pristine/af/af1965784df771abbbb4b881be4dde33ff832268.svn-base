
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


module ol_loop_routines_/**/REALKIND
  use ol_debug, only: ol_fatal, ol_msg, ol_error
  implicit none
  contains

! ****************************************************
subroutine tensor_integral(rank, momenta, masses_2, TI)
! ****************************************************
  use KIND_TYPES, only: REALKIND
  use ol_debug, only: ol_error, ol_msg
  use ol_generic, only: to_string
#ifdef USE_COLLIER
  use ol_parameters_decl_/**/DREALKIND, only: current_processname
  use ol_loop_parameters_decl_/**/DREALKIND, only: tensor_reduction_error
  use ol_external_decl_/**/REALKIND, only: nParticles, P_ex, crossing, inverse_crossing
  use ol_tensor_bookkeeping, only: rank_to_size, tensor_size
  use ol_Std2LC_converter_/**/REALKIND, only: lorentz2lc_tensor
  use ol_kinematics_/**/REALKIND, only: LC2Std_Rep_cmplx, momenta_invariants
#ifdef COLLIER_LEGACY
  use bt_Interface, only: CalcTensorTNr, CalcTensorFr ! direct reduction routines
  use bt_TI_lib_switch, only: TI_library
  use dd_interface, only: dd_get_error_code
#else
  use collier, only: tnten_cll
#endif
#endif
  implicit none
  integer,           intent(in)  :: rank
  complex(REALKIND), intent(in)  :: momenta(:,:), masses_2(:)
  complex(REALKIND), intent(out) :: TI(:)
#ifdef USE_COLLIER
  complex(REALKIND), allocatable :: T2dim(:,:)
  complex(REALKIND) :: momenta_TI(0:3,size(momenta,2)), T_Lor(size(TI))
  integer           :: l, r
  integer, external :: coli_get_error_code

  do l = 1, size(momenta,2)
    call LC2Std_Rep_cmplx(momenta(:,l), momenta_TI(:,l))
  end do

#ifdef COLLIER_LEGACY
  allocate(T2dim(rank_to_size(rank),0:rank))
  if (size(masses_2) == 6 .and. rank >= 6) then
    T2dim = CalcTensorFr(rank, momenta_TI, masses_2, momenta_invariants(momenta_TI))
  else
    T2dim = CalcTensorTNr(size(masses_2), rank, momenta_TI, masses_2, momenta_invariants(momenta_TI))
  end if

  if (TI_library == 1) then
    tensor_reduction_error = coli_get_error_code()
  else if (TI_library == 2) then
    tensor_reduction_error = dd_get_error_code()
  end if
  ! Error handling should be in a separate routine which handles errors from all reduction libraries.
  ! Call might be moved to the process code.
  if (tensor_reduction_error > 0) then
    call ol_error("=== TENSOR INTEGRAL REDUCTION ERROR ===")
    if (TI_library == 1) then
      call ol_msg(1,"library: Coli")
    else if (TI_library == 2) then
      call ol_msg(1,"library: DD")
    end if
    call ol_msg(1,"process: " // current_processname )
    call ol_msg(1,"phase space point:")
    do l = 1, nParticles
      print*, P_ex(:,l)
      crossing(inverse_crossing(l)) = l
    end do
    call ol_msg(1,"crossing:" // to_string(crossing(1:nParticles)))
    T2dim = 0
  end if

  do r = 0, rank
    do l = 1, rank_to_size(r)
      T_Lor(l+tensor_size(r-1)) = T2dim(l,r)
    end do
  end do
  deallocate(T2dim)
#else
#ifdef PRECISION_dp
  call tnten_cll(T_Lor, TI, momenta_TI, momenta_invariants(momenta_TI), masses_2, size(masses_2), rank)
#else
  T_Lor = 0
#endif
#endif

  call lorentz2lc_tensor(rank, T_Lor, TI)
#else
  TI = 0 ! prevent compiler warning
  call ol_fatal('in tensor_integral: Collier is not available')
#endif
end subroutine tensor_integral



! ****************************************************
subroutine tensor_integral_contract(rank, momenta, masses_2, Gtensor, M2)
! ****************************************************
  use KIND_TYPES, only: REALKIND
  implicit none
  integer,           intent(in)  :: rank
  complex(REALKIND), intent(in)  :: momenta(:,:), masses_2(:), Gtensor(:)
  complex(REALKIND), intent(out) :: M2
  complex(REALKIND) :: TI(size(Gtensor))
  call tensor_integral(rank, momenta, masses_2, TI)
  M2 = tensor_contract(Gtensor, TI)
end subroutine tensor_integral_contract



! ****************************************************
subroutine scalar_integral(momenta, masses_2)
! ****************************************************
  use KIND_TYPES, only: REALKIND
#ifdef USE_COLLIER
  use ol_kinematics_/**/REALKIND, only: LC2Std_Rep, momenta_invariants
#ifdef COLLIER_LEGACY
  use bt_Interface, only: CalcTensorTNr
#else
  use collier, only: tnten_cll
#endif
#endif
  implicit none
  complex(REALKIND), intent(in)  :: momenta(:,:), masses_2(:)
#ifdef USE_COLLIER
  complex(REALKIND) :: T2dim(1,0:0), tuv(0:0)
  complex(REALKIND) :: momenta_TI(0:3,size(momenta,2))
  real(REALKIND)    :: mom(0:3)
  integer           :: l
  do l = 1, size(momenta,2)
    call LC2Std_Rep(momenta(:,l), mom)
    momenta_TI(:,l) = mom
  end do

#ifdef COLLIER_LEGACY
  T2dim = CalcTensorTNr(size(masses_2), 0, momenta_TI, masses_2, momenta_invariants(momenta_TI))
#else
#ifdef PRECISION_dp
  call tnten_cll(T2dim(1,:), tuv, momenta_TI, momenta_invariants(momenta_TI), masses_2, size(masses_2), 0)
#endif
#endif

#else
  call ol_fatal('in scalar_integral: Collier is not available')
#endif
end subroutine scalar_integral



! ****************************************************
subroutine covariant_coefficients(rank, momenta, masses_2)
! ****************************************************
  use KIND_TYPES, only: REALKIND
#if defined(COLLIER_LEGACY) && defined(USE_COLLIER)
  use ol_kinematics_/**/REALKIND, only: LC2Std_Rep, momenta_invariants
  use bt_ColiCombinatorics, only: BinomTable
  use bt_Interface, only: CalcTNrPVco
#endif
  implicit none
  integer,           intent(in)  :: rank
  complex(REALKIND), intent(in)  :: momenta(:,:), masses_2(:)
#if defined(COLLIER_LEGACY) && defined(USE_COLLIER)
  complex(REALKIND), allocatable :: Coefs(:,:,:)
  complex(REALKIND) :: momenta_TI(0:3,size(momenta,2))
  real(REALKIND)    :: mom(0:3)
  integer           :: l

  do l = 1, size(momenta,2)
    call LC2Std_Rep(momenta(:,l), mom)
    momenta_TI(:,l) = mom
  end do

  allocate(Coefs(BinomTable(rank,rank+size(masses_2)-2),0:rank/2,0:rank))

  Coefs = CalcTNrPVco(size(masses_2),rank,masses_2, momenta_invariants(momenta_TI))

  deallocate(Coefs)
#else
  call ol_fatal('in covariant_coefficients: Collier (legacy) is not available')
#endif
end subroutine covariant_coefficients



! ***************************************************
subroutine fake_tensor_integral(rank, momenta, masses_2, Gtensor, M2)
! Build a tensor as the direct product of the loop momentum with itself up to rank 'rank',
! divided by the denominator of the corresponding tensor integral.
! ***************************************************
! rank     = highest rank in the loop
! momenta  = list of the N-1 momenta flowing inside the loop without the loop momentum.
!            momenta(N) = 0 is not included.
! masses_2 = list of the N squared masses of the loop propagators
! TI       = array containing all independent tensor components up to highest rank (contravariant light-cone);
!            divided by the denominator 'den' corresponding to the loop with 'momenta' and 'masses_2'.
! den      = product((momenta(i)+Qloop)^2 - masses_2(i), i=1..N)
! The loop momentum 'pseudotree_momentum' is taken from the module pseudotree
! QloopLC  = loop momentum in light-cone representation
! ***************************************************
  use KIND_TYPES, only: REALKIND
  use ol_tensor_bookkeeping, only: HR, tensor_size
  use ol_pseudotree_/**/REALKIND, only: pseudotree_momentum
  use ol_contractions_/**/REALKIND, only: cont_V
  use ol_kinematics_/**/REALKIND, only: Std2LC_Rep
  implicit none
  integer,           intent(in)  :: rank
  complex(REALKIND), intent(in)  :: momenta(:,:), masses_2(:), Gtensor(:)
  complex(REALKIND), intent(out) :: M2
  complex(REALKIND) :: TI(size(Gtensor)), QloopLC(4), den
  integer           :: i, l

  call Std2LC_Rep(pseudotree_momentum, QloopLC)
  den = cont_V(QloopLC) - masses_2(1)
  do i = 1, size(masses_2)-1
    den = den * (cont_V(momenta(:,i) + QloopLC) - masses_2(i+1))
  end do
  TI(1) = 1 / den
  do l = 1, tensor_size(rank-1)
    do i = 1,4
      TI(HR(i,l)) = QloopLC(i)*TI(l)
    end do
  end do

  M2 = tensor_contract(Gtensor, TI)

end subroutine fake_tensor_integral



! ***************************************************
subroutine TI_call(rank, momenta, masses_2, Gsum, M2)
! ***************************************************
  use KIND_TYPES, only: REALKIND
  use ol_parameters_decl_/**/DREALKIND, only: a_switch, &
    & ti_monitor, pid_string, stability_logdir, max_parameter_length
  use ol_kinematics_/**/REALKIND, only: LC2Std_Rep_cmplx, momenta_invariants
  use ol_generic, only: to_string
  implicit none
  integer,           intent(in)    :: rank
  complex(REALKIND), intent(in)    :: momenta(:,:), masses_2(:), Gsum(:)
  real(REALKIND),    intent(inout) :: M2
  complex(REALKIND) :: M2add
  integer :: outunit = 44, k
  character(len=max_parameter_length) :: outfile
  complex(REALKIND) :: momenta_TI(0:3,size(momenta,2))
  if (a_switch == 0) then
    call fake_tensor_integral(rank, momenta, masses_2, Gsum, M2add)
  else if (a_switch == 1 .or. a_switch == 7) then
    ! COLI/DD: full tensor integral
    call tensor_integral_contract(rank, momenta, masses_2, Gsum, M2add)
  else if (a_switch == 2) then
    ! COLI/DD: only covariant coefficients, no tensor contruction
    call covariant_coefficients(rank, momenta, masses_2)
    M2add = sum(Gsum)
  else if (a_switch == 3) then
    ! COLI/DD: only scalar integrals
    call scalar_integral(momenta, masses_2)
    M2add = sum(Gsum)
  else if (a_switch == 4) then
    ! Do nothing
    M2add = sum(Gsum)
  else if (a_switch == 5) then
    ! CutTools
    call cuttools_interface(rank, momenta, masses_2, Gsum, M2add)
  else if (a_switch == 6) then
    ! Samurai
    call samurai_interface(rank, momenta, masses_2, Gsum, M2add)
  else
    call ol_fatal('in TI_call: amp_switch out of range: ' // to_string(a_switch))
  end if
  M2 = M2 + real(M2add)
  if (ti_monitor > 0) then
    outfile = trim(stability_logdir) // "/ti_monitor_" // trim(to_string(a_switch)) // ".log"
    open(unit=outunit, file=outfile, form='formatted', position='append')
    if (ti_monitor > 1) write(outunit,*) ''
    write(outunit,*) 'm2add= ', real(M2add), M2
    if (ti_monitor > 1) then
      write(outunit,*) 'rank= ', rank
      write(outunit,*) 'masses2= ', masses_2
      do k = 1, size(momenta,2)
        call LC2Std_Rep_cmplx(momenta(:,k), momenta_TI(:,k))
        write(outunit,*) 'p= ', real(momenta_TI(:,k))
      end do
      write(outunit,*) 'mominv= ', real(momenta_invariants(momenta_TI))
    end if
    close(outunit)
  end if
end subroutine TI_call



! ****************************************************
function TI2_call(rank, momenta, masses_2, Gsum, TI)
! TI_call with precalculated tensor integrals.
! Used for loop^2 processes.
! Returns the contribution to the amplitude
! ****************************************************
  use KIND_TYPES, only: REALKIND
  use ol_debug, only: ol_fatal, ol_msg, ol_error
  use ol_parameters_decl_/**/DREALKIND, only: a_switch
  use ol_generic, only: to_string
  implicit none
  integer,           intent(in)    :: rank
  complex(REALKIND), intent(in)    :: momenta(:,:), masses_2(:), Gsum(:), TI(:)
  complex(REALKIND) :: TI2_call
  if (a_switch == 0) then
    call fake_tensor_integral(rank, momenta, masses_2, Gsum, TI2_call)
  else if (a_switch == 1 .or. a_switch == 7) then
    ! COLI/DD: contract with precalculated tensor integral
    TI2_call = tensor_contract(Gsum, TI)
  else if (a_switch == 4) then
    ! Do nothing
    TI2_call = sum(Gsum)
  else if (a_switch == 5) then
    ! CutTools
    call cuttools_interface(rank, momenta, masses_2, Gsum, TI2_call)
  else if (a_switch == 6) then
    ! Samurai
    call samurai_interface(rank, momenta, masses_2, Gsum, TI2_call)
  else
    call ol_error(2, 'in TI2_call: amp_switch out of range: ' // to_string(a_switch))
    call ol_msg('note that modes 2 and 3 are not supported in loop^2.')
    call ol_fatal()
  end if
end function TI2_call



! **********************************************************************
function tensor_contract(G, TI)
! Contract two tensors from rank 0 to the highest rank of G.
! TI must be of equal or higher rank as G.
! **********************************************************************
  use KIND_TYPES, only: REALKIND
  implicit none
  complex(REALKIND), intent(in) :: G(:), TI(:)
  complex(REALKIND) :: tensor_contract
  tensor_contract = sum(G*TI(1:size(G)))
end function tensor_contract



! ****************************************
subroutine loop_trace(G_in, Gtensor)
! ****************************************
! Close spinor or vector loop line after all vertex insertions
! Gtensor(l) = Tr[G_in(beta,l,alpha)] = Sum(G_in(alpha,l,alpha), alpha=1..4)
! alpha = covariant (light-cone)
! beta  = contravariant (light-cone)
  use KIND_TYPES, only: REALKIND
  implicit none
  complex(REALKIND), intent(in)  :: G_in(:,:,:)
  complex(REALKIND), intent(out) :: Gtensor(:)
  Gtensor = G_in(1,:,1) + G_in(2,:,2) + G_in(3,:,3) + G_in(4,:,4)
end subroutine loop_trace



! *********************************************
subroutine loop_cont_VV(G_in, J_V2, J_V1, G_out)
! *********************************************
! contraction of tensor coefficients with vector currents for pseudo-tree
! G_out(l) =  J_V1(alpha) * G_in(beta,l,alpha) * J_V2(beta)
! J_Vi  = CONTRAVARIANT current
! alpha = COVARIANT index
! beta  = CONTRAVARIANT index
  use KIND_TYPES, only: REALKIND
  use ol_contractions_/**/REALKIND, only: cont_VV
  implicit none
  complex(REALKIND), intent(in)  :: G_in(:,:,:), J_V1(4), J_V2(4)
  complex(REALKIND), intent(out) :: G_out(:)
  integer :: l

  do l = 1, size(G_in,2)
    G_out(l) = J_V1(1) * cont_VV(G_in(:,l,1), J_V2) + J_V1(2) * cont_VV(G_in(:,l,2), J_V2) &
             + J_V1(3) * cont_VV(G_in(:,l,3), J_V2) + J_V1(4) * cont_VV(G_in(:,l,4), J_V2)
  end do

end subroutine loop_cont_VV



! *************************************
subroutine loop_cont_QA(G_in, Q, A, G_out)
! *************************************
! Contraction of tensor coefficients with quark-antiquark currents (attach loop line)
! G_out(l) = Q(alpha) * G_in(beta,l,alpha) * A(beta)
  use KIND_TYPES, only: REALKIND
  implicit none
  complex(REALKIND), intent(in)  :: G_in(:,:,:), Q(4), A(4)
  complex(REALKIND), intent(out) :: G_out(:)

  G_out = Q(1)*A(1)*G_in(1,:,1) + Q(2)*A(1)*G_in(2,:,1) + Q(3)*A(1)*G_in(3,:,1) + Q(4)*A(1)*G_in(4,:,1) &
        + Q(1)*A(2)*G_in(1,:,2) + Q(2)*A(2)*G_in(2,:,2) + Q(3)*A(2)*G_in(3,:,2) + Q(4)*A(2)*G_in(4,:,2) &
        + Q(1)*A(3)*G_in(1,:,3) + Q(2)*A(3)*G_in(2,:,3) + Q(3)*A(3)*G_in(3,:,3) + Q(4)*A(3)*G_in(4,:,3) &
        + Q(1)*A(4)*G_in(1,:,4) + Q(2)*A(4)*G_in(2,:,4) + Q(3)*A(4)*G_in(3,:,4) + Q(4)*A(4)*G_in(4,:,4)

end subroutine loop_cont_QA



! *****************************
subroutine G0initialisation(G0)
! *****************************
! Initialise the rank 0 tensor coefficient of the cut spinor or vector loop line;
! parameterised only by loop momentum
! G0(beta,1,alpha) = delta(alpha,beta)
! index notation: G0(beta,l,alpha)
! l = tensor index
! alpha = covariant (light-cone) "frozen" open index, is untouched till the last contraction in the loop
! beta  = contravariant (light-cone) "active" index contracted with vertices/props to build the loop
  use KIND_TYPES, only: REALKIND
  implicit none
  complex(REALKIND), intent(out) :: G0(4,1,4)
  G0 = 0
  G0(1,1,1) = 1
  G0(2,1,2) = 1
  G0(3,1,3) = 1
  G0(4,1,4) = 1
end subroutine G0initialisation



subroutine cts_numerator(q, amp)
  use KIND_TYPES, only: REALKIND
  use ol_loop_momentum_/**/REALKIND, only: loop_mom_tens
  use ol_tensor_storage_/**/REALKIND
  implicit none
  complex(REALKIND), intent(in)  :: q(0:3)
  complex(REALKIND), intent(out) :: amp
  complex(REALKIND) :: Qtensor(array_length_stored), QloopLC(1:4)

  call loop_mom_tens(q, Qtensor)
  amp = tensor_contract(Qtensor, tensor_stored) ! contract up to the length of Qtensor

end subroutine cts_numerator



function samurai_num(ncut, q, mu2)
  use KIND_TYPES, only: REALKIND
  use ol_loop_momentum_/**/REALKIND, only: loop_mom_tens
  use ol_tensor_storage_/**/REALKIND
  implicit none
  complex(REALKIND), intent(in) :: q(4) ! q = [p_x,p_y,p_z,E]
  complex(REALKIND), intent(in) :: mu2
  integer,           intent(in) :: ncut
  complex(REALKIND) :: samurai_num
  complex(REALKIND) :: Qtensor(array_length_stored), q_tmp(0:3)

  q_tmp(0)   = q(4)
  q_tmp(1:3) = q(1:3)

  call loop_mom_tens(q_tmp, Qtensor)
  samurai_num = tensor_contract(Qtensor, tensor_stored) ! contract up to the length of Qtensor

end function samurai_num



subroutine cuttools_interface(rank, momenta, masses2, Gtensor, M2)
  use KIND_TYPES, only: REALKIND, DREALKIND
  use ol_loop_parameters_decl_/**/DREALKIND, only: opprootsvalue, mureg, de1_UV, de1_IR, de2_i_IR
  use ol_kinematics_/**/REALKIND, only: LC2Std_Rep
  use ol_tensor_storage_/**/REALKIND
  use ol_tensor_bookkeeping, only: tensor_size
#ifdef USE_CUTTOOLS
  use cts_numdummies, only: dpnumdummy, mpnumdummy
#endif
  implicit none

  integer,           intent(in)  :: rank
  complex(REALKIND), intent(in)  :: momenta(:,:), masses2(:), Gtensor(:)
  complex(REALKIND), intent(out) :: M2
#ifdef USE_CUTTOOLS
  complex(DREALKIND) :: cts_amp_array(0:2), cts_ampcc, cts_ar1
  real(REALKIND)     :: mom(0:3)
  complex(DREALKIND) :: masses2_dp(size(masses2))
  real(DREALKIND)    :: cts_pp(0:3,0:size(masses2)-1)
  integer            :: l
  logical            :: cts_stable

  if (de1_UV /= de1_IR) then
    call ol_fatal('pole1_UV != pole1_IR is not allowed with CutTools.')
  end if

  tensor_stored(:size(Gtensor)) = Gtensor
  rank_stored = rank
  array_length_stored = tensor_size(rank)

  masses2_dp = masses2

  cts_pp(:,0) = 0
  do l = 1, size(momenta,2)
    call LC2Std_Rep(momenta(:,l), mom)
    cts_pp(:,l) = mom
  end do

#ifdef PRECISION_dp
  call ctsxcut(3, opprootsvalue, mureg, size(masses2), cts_numerator, mpnumdummy, rank, &
             & cts_pp, masses2_dp, cts_amp_array, cts_ampcc, cts_ar1, cts_stable)
#else
  call ctsxcut(6, opprootsvalue, mureg, size(masses2), dpnumdummy, cts_numerator, rank, &
             & cts_pp, masses2_dp, cts_amp_array, cts_ampcc, cts_ar1, cts_stable)
#endif

  M2 = cts_amp_array(0) + cts_amp_array(1)*de1_IR + cts_amp_array(2)*de2_i_IR
#else
  M2 = 0 ! prevent compiler warning
  call ol_fatal('cuttools_interface: CutTools is not available')
! #ifdef USE_CUTTOOLS
#endif
end subroutine cuttools_interface



subroutine samurai_interface(rank, momenta, masses2, Gtensor, M2)
  use KIND_TYPES, only: REALKIND
  use ol_loop_parameters_decl_/**/REALKIND, only: &
    & mureg2, de1_UV, de1_IR, de2_i_IR
  use ol_kinematics_/**/REALKIND, only: LC2Std_Rep
  use ol_tensor_storage_/**/REALKIND
  use ol_tensor_bookkeeping, only: tensor_size
#ifdef USE_SAMURAI
  use msamurai, only: samurai
#endif
  implicit none

  integer,           intent(in)  :: rank
  complex(REALKIND), intent(in)  :: momenta(:,:), masses2(:), Gtensor(:)
  complex(REALKIND), intent(out) :: M2
#if defined(USE_SAMURAI) && defined(PRECISION_dp)
  complex(REALKIND) :: sam_amp_array(-2:0), sam_r1
  real(REALKIND)    :: mom(0:3), sam_pp(0:size(masses2)-1,4)
  integer           :: l
  logical           :: sam_test

  if (de1_UV /= de1_IR) then
    call ol_fatal('pole1_UV != pole1_IR is not allowed with Samurai.')
  end if

  tensor_stored(:size(Gtensor)) = Gtensor
  rank_stored = rank
  array_length_stored = tensor_size(rank)

  sam_pp(0,:) = 0
  do l = 1, size(momenta,2)
    call LC2Std_Rep(momenta(:,l), mom)
    sam_pp(l,1:3) = mom(1:3)
    sam_pp(l,4) = mom(0)
  end do

  call samurai(samurai_num, sam_amp_array, sam_r1, sam_pp, masses2, size(masses2), rank, 1, mureg2, sam_test) !, cache_flag, scalar_cache)

  M2 = sam_amp_array(0) + sam_amp_array(-1)*de1_IR + sam_amp_array(-2)*de2_i_IR
! #if defined(USE_SAMURAI) && defined(PRECISION_dp)
#else
  M2 = 0 ! prevent compiler warning
#endif
#ifdef USE_SAMURAI
#ifndef PRECISION_dp
  call ol_fatal('in samurai_interface: Samurai only supports double precision')
#endif
#else
  call ol_fatal('in samurai_interface: Samurai is not available')
#endif
end subroutine samurai_interface

end module ol_loop_routines_/**/REALKIND
