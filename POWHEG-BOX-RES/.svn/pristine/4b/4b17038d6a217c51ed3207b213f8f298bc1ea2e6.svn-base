
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


module ol_version
  implicit none
  character(16) :: version = VERSION
  character(4) :: revision = REVISION
  logical :: splash_todo = .true.
  integer, parameter :: welcome_length = 800

  contains

  subroutine welcome(outstring)
    implicit none
    character(welcome_length), intent(out) :: outstring
    character, parameter :: LF = char(10)
    outstring = &
      & " #########################################################" // LF // &
      & " #     ___                              " // adjustr(version) // " #" // LF // &
      & " #    /   \ ___  ____  _  _  |     __   __  ___   __     #" // LF // &
      & " #    |   | |__| |__   |\ |  |    /  \ /  \ |__| /__     #" // LF // &
      & " #    \___/ |    |___  | \|  |___ \__/ \__/ |    __/     #" // LF // &
      & " #                                                       #" // LF // &
      & " #########################################################" // LF // &
      & " #  You are using OpenLoops to evaluate loop amplitudes  #" // LF // &
      & " #                     Authors:                          #" // LF // &
      & " # F. Cascioli, J. Lindert, P. Maierhoefer, S. Pozzorini #" // LF // &
      & " #    Please cite Phys. Rev. Lett. 108 (2012) 111601     #" // LF // &
      & " #########################################################" // LF
    splash_todo = .false.
  end subroutine welcome

  subroutine welcome_c(outstring) bind(c,name="ol_welcome")
    use, intrinsic :: iso_c_binding, only: c_char
    implicit none
    character(kind=c_char), intent(out) :: outstring(welcome_length)
    character(welcome_length) :: welcome_str
    integer :: i
    call welcome(welcome_str)
    do i = 1, len(trim(welcome_str))
      outstring(i) = welcome_str(i:i)
    end do
    outstring(i) = char(0)
  end subroutine welcome_c

  subroutine print_welcome()
    use ol_debug, only: ol_write_msg
    implicit none
    character(welcome_length) :: welcome_string
    call welcome(welcome_string)
    call ol_write_msg(trim(welcome_string))
  end subroutine print_welcome

end module ol_version


module openloops_version
  use ol_version, only: version, revision, splash_todo
end module openloops_version


! legacy welcome for "old" Sherpa interface
subroutine openloops_welcome(outstring)
  use openloops_version, only: version, splash_todo
  implicit none
  character(1200), intent(out), optional :: outstring
  character(1200) :: welcome
  character, parameter :: LF = char(10)
  !
  welcome = LF // &
    & " #########################################################" // LF // &
    & " #     ___                              " // adjustr(version) // " #" // LF // &
    & " #    /   \ ___  ____  _  _  |     __   __  ___   __     #" // LF // &
    & " #    |   | |__| |__   |\ |  |    /  \ /  \ |__| /__     #" // LF // &
    & " #    \___/ |    |___  | \|  |___ \__/ \__/ |    __/     #" // LF // &
    & " #                                                       #" // LF // &
    & " #########################################################" // LF // &
    & " #  You are using OpenLoops to evaluate loop amplitudes  #" // LF // &
    & " #                     Authors:                          #" // LF // &
    & " # F. Cascioli, J. Lindert, P. Maierhoefer, S. Pozzorini #" // LF // &
    & " #    Please cite Phys. Rev. Lett. 108 (2012) 111601     #" // LF // &
    & " #########################################################" // LF // &
!     &                                                                LF // &
!     &                                                                LF // &
!     & " ########################################################" // LF // &
!     & " #                    C O L L I E R                     #" // LF // &
!     & " ########################################################" // LF // &
!     & " # You are using COLLIER to evaluate one-loop integrals #" // LF // &
!     & " # Authors: A. Denner, S. Dittmaier, L. Hofer           #" // LF // &
!     & " # Please cite Nucl. Phys. B844 (2011) 199              #" // LF // &
!     & " #             Nucl. Phys. B734 (2006)  62              #" // LF // &
!     & " #             Nucl. Phys. B658 (2003) 175              #" // LF // &
!     & " ########################################################" // LF // &
    & char(0)
  !
  if (present(outstring)) then
    outstring = welcome
  else
    write(*,*) welcome
  end if
  splash_todo = .false.
end subroutine openloops_welcome
