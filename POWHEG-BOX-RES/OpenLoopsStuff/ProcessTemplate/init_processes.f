      subroutine init_processes
      use openloops, only: set_parameter
      implicit none
      include "nlegborn.h"
      include "pwhg_flst.h"
      include "pwhg_st.h"
      include 'pwhg_ckm.h'
      include 'pwhg_physpar.h'
      include 'pwhg_res.h'
      integer i, int(maxprocreal), ickm
      integer nmaxres_real,nmaxres_born,dim_integ
      real * 8 powheginput

      do i=1,maxprocreal
         int(i)=i
      enddo

      ickm = 2   !   0,1,2 for general, ckm_cabibbo, ckm_diag
      ckm_diag = .false.
      ckm_cabibbo = .true.
      if(ickm.eq.2) then
         ckm_diag = .true.
      elseif(ickm.eq.1) then
         ckm_cabibbo = .true.
      endif

c     init couplings and flavour structures
      call init_couplings
      call init_processes_born
      call init_processes_real

      ! determine number of light flavours
      st_nlight = 0
      do i=1,6
        if (physpar_pdgmasses(i) == 0) st_nlight=st_nlight+1
      end do

c     set electroweak and strong couplings os the Born amplitude (i.e. the powers of g and g_s)
      res_powew=<ORDEREW>
      res_powst=<ORDERQCD>
      if(powheginput("#nores") /= 1) then
         call build_resonance_histories
      endif

      write(*,*) ' ***********   FINAL POWHEG    ***************'
      write(*,*) ' ***********     BORN          ***************'
      do i=1,flst_nborn
         write(*,'(a,100i4)')'                  ',int(1:flst_bornlength(i))
         write(*,'(a,i3,a,100i4)')'flst_born(',i,')   =',flst_born(1:flst_bornlength(i),i)
         write(*,'(a,i3,a,100i4)')'flst_bornres(',i,')=',flst_bornres(1:flst_bornlength(i),i)
         write(*,*)
      enddo
      write(*,*) 'max flst_bornlength: ',maxval(flst_bornlength(1:flst_nborn))



      write(*,*) ' ***********     REAL          ***************'
      do i=1,flst_nreal
         write(*,'(a,100i4)')'                  ',int(1:flst_reallength(i))
         write(*,'(a,i3,a,100i4)')'flst_real(',i,')   =',flst_real(1:flst_reallength(i),i)
         write(*,'(a,i3,a,100i4)')'flst_realres(',i,')=',flst_realres(1:flst_reallength(i),i)
         write(*,*)
      enddo
      write(*,*) 'max flst_reallength: ',maxval(flst_reallength(1:flst_nreal))

      call buildresgroups(flst_nborn,nlegborn,flst_bornlength,
     1     flst_born,flst_bornres,flst_bornresgroup,flst_nbornresgroup)


      call buildresgroups(flst_nreal,nlegreal,flst_reallength,
     1     flst_real,flst_realres,flst_realresgroup,flst_nrealresgroup)

      write(*,*)
      write(*,*) '*********   SUMMARY  *********'
      write(*,*) 'set nlegborn to: ',maxval(flst_bornlength(1:flst_nborn))
      write(*,*) 'set nlegreal to: ',maxval(flst_reallength(1:flst_nreal))

      nmaxres_real = maxval(flst_realres(1:flst_reallength(flst_nreal),1:flst_nreal)) - 2
      nmaxres_born = maxval(flst_bornres(1:flst_bornlength(flst_nborn),1:flst_nborn)) - 2
      write(*,*) 'max number of resonances: ',max(nmaxres_real,nmaxres_born)

c     add (-1) for overall azimuthal rotation of the event around the beam axis
      dim_integ = (flst_numfinal+1)*3 - 4 + 2 + max(nmaxres_real,nmaxres_born)
      write(*,*) 'set ndiminteg to: ',dim_integ


      write(*,*) 'flst_nbornresgroup ',flst_nbornresgroup
      write(*,*) 'flst_nrealresgroup ',flst_nrealresgroup

      write(*,*) '*********   END SUMMARY  *********'
      write(*,*)


cccccccccccccccccccccccccOpenLoops Initcccccccccccccccccccccccccccccccccc

! increase phase-space tolerance
!      call set_parameter("psp_tolerance", 0.0001)

! Coupling order: order_ew -> NLO QCD
      call set_parameter("order_ew", res_powew)

! make sure complex mass scheme is switched on
      call set_parameter("use_cms",1)

! select EW input scheme: MZ, MW, alpha (ew_scheme=2, default) VS. MZ, MW, Gmu (ew_scheme=1)
      if (powheginput('#ewscheme')>0) then
        call set_parameter("ew_scheme", powheginput('#ewscheme'))
      end if

! set number of active flavours in aS renormalization:
! if minnf_alphasrun is set to a value larger then the number of massless
! quark flavours, also the corresponding heavy quarks are assumed to contribute
! to the running of the strong coupling (above the respective thresholds).
! see: http://openloops.hepforge.org/parameters.html
      call set_parameter("minnf_alphasrun", st_nlight)

! write stability log files
      if (powheginput('#openloops-stability')>0) then
        call set_parameter("stability_log", 2)
      end if


! Initialize OpenLooos
      call openloops_init
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc


      end




      subroutine init_processes_born
        implicit none
        include "nlegborn.h"
        include "pwhg_flst.h"
c     set the number of final-state paricles at the Born-level WITHOUT any resonance
        flst_bornlength = nlegbornexternal
        flst_numfinal=nlegborn-2

        flst_nborn= 1 ! number of born flavour structures

! put born flavour structures here:
        flst_born(   1,   1)=          -1
        flst_born(   2,   1)=           1
        flst_born(   3,   1)=         -11
        flst_born(   4,   1)=          11

        return
      end



      subroutine init_processes_real
        implicit none
        include "nlegborn.h"
        include "pwhg_flst.h"
        flst_reallength =  nlegrealexternal

        flst_nreal=  1 ! number of real flavour structures

! put real flavour structures here:
        flst_real(   1,   1)=          -1
        flst_real(   2,   1)=           1
        flst_real(   3,   1)=         -11
        flst_real(   4,   1)=          11
        flst_real(   5,   1)=           0

        return
      end

