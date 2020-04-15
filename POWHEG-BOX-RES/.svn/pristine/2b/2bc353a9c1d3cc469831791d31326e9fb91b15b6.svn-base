!!
!!  File cache.F90 is part of COLLIER
!!  - A Complex One-Loop Library In Extended Regularizations
!!
!!  Copyright (C) 2015, 2016   Ansgar Denner, Stefan Dittmaier, Lars Hofer
!!
!!  COLLIER is licenced under the GNU GPL version 3, see COPYING for details.
!!

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
!  ******************
!  *  module cache  *
!  *  by Lars Hofer *
!  ******************
!
!
!  provides a cache-system for the tensor-integral library COLLIER
!  based on routines by Markus Roth, adapted for use in COLI and DD
!  (in particular the cache now distinguishes between external master-calls
!   of tensor integrals and internal recursive calls)
!
!  HOW TO USE THE COLLIER-CACHE IN A MONTE-CARLO:
!  1) After the initialization of COLLIER put
!     call InitCacheSystem(mnc,Nmax)
!     mnc = number of different caches, 
!     Nmax: N-point tensor integrals are cached for N<=Nmax
!  2) Call InitCache(nc) ONCE for EVERY phase-space point BEFORE evaluating the complete set
!     of tensor integrals. nc is the number of the respective cache. The tensor integrals 
!     have to be evaluated in the same order for every phase-space point!
!    
!
!
!  global variables:
!  NCoefs, use_cache_system, use_cache
! 
!  functions and subroutines:
!  InitCacheSystem, 
!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




module cache

!  use collier_global
  use combinatorics
 
  implicit none

  ! variables/parameters accessed in COLI/DD
  logical :: use_cache_system=.false.
  integer, allocatable :: use_cache(:)
  ! internal variables of the cache-system
  integer :: ninfout_cache, infoutlev_cache
  double complex, allocatable :: CacheVals(:,:), CacheArgs(:,:), CacheVals_local(:,:)
  integer, allocatable :: CacheLib(:)
  integer, allocatable :: use_cache_cp(:)
  integer, allocatable :: nevent(:), cache_mode(:), cache_mode_cp(:), nopt(:), ncalc(:), catype(:)
  integer, allocatable :: casa(:,:), new_casa(:,:), cara(:,:), new_cara(:,:), CachePoint(:,:,:)
  integer, allocatable :: nval_max(:), narg_max(:), rankcached(:)
  integer :: ncache_max=0, ncall_max, ncalc_max, id_max, ncache, ncall, maxnval, nval_tmp, tencache, nval_local, id_local
  

contains

  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine InitCacheSystem_cll(mnc,Nmax)
  !
  !  initialization of the cache-system:
  !  mnc = number of caches;  mnc<=0 --> cache-system switched off
  !  Nmax: N-point tensor integrals cached for N<=Nmax
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine InitCacheSystem_cll(mnc,Nmax)

    integer, intent(in) :: mnc,Nmax
    integer :: ncache
    logical :: onlyinternal,infwri
    character(len=*),parameter :: fmt90 = "(A15,I3,A28,I3)"

    if (Nmax.le.0) then    
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('InitCacheSystem_cll','Nmax has to be a positive integer',infwri)    
      if(infwri) write(ninfout_cache,*) '--> cache has not been initialized!'    
      return
    end if

    if (mnc.lt.0) then
      use_cache_system = .false.
      return
    else if (mnc.eq.0) then
      use_cache_system = .true.
      ncache_max = 1
      onlyinternal = .true.
    else
      use_cache_system = .true.
      ncache_max = mnc
      onlyinternal = .false.    
    end if  

    if (allocated(use_cache)) then
      deallocate(use_cache)
    end if
    allocate(use_cache(ncache_max))
    use_cache = Nmax

    if (allocated(use_cache_cp)) then
      deallocate(use_cache_cp)
    end if
    allocate(use_cache_cp(ncache_max))
    use_cache_cp = Nmax

    if (allocated(cache_mode)) then
      deallocate(cache_mode)
    end if
    allocate(cache_mode(ncache_max))
    if (onlyinternal) then
      cache_mode = -1
    else
      cache_mode = -99
    end if

    if (allocated(cache_mode_cp)) then
      deallocate(cache_mode_cp)
    end if
    allocate(cache_mode_cp(ncache_max))
    cache_mode_cp = -99

    if (allocated(nevent)) then
      deallocate(nevent)
    end if
    allocate(nevent(ncache_max))
    nevent = 0

    if (allocated(ncalc)) then
      deallocate(ncalc)
    end if
    allocate(ncalc(ncache_max))
    ncalc = 0

    if (allocated(narg_max)) then
      deallocate(narg_max)
    end if
    allocate(narg_max(ncache_max))
    narg_max = 0

    if (allocated(nval_max)) then
      deallocate(nval_max)
    end if
    allocate(nval_max(ncache_max))
    nval_max = 0

    if (allocated(casa)) then
      deallocate(casa)
    end if
    allocate(casa(1,ncache_max))
    casa = 0

    if (allocated(new_casa)) then
      deallocate(new_casa)
    end if
    allocate(new_casa(1,ncache_max))
    new_casa = 0

    if (allocated(cara)) then
      deallocate(cara)
    end if
    allocate(cara(1,ncache_max))
    cara = 0

    if (allocated(new_cara)) then
      deallocate(new_cara)
    end if
    allocate(new_cara(1,ncache_max))
    new_cara = 0

    if (allocated(CachePoint)) then
      deallocate(CachePoint)
    end if
    allocate(CachePoint(0:0,1,ncache_max))
    CachePoint = 0

    if (allocated(nopt)) then
      deallocate(nopt)
    end if
    allocate(nopt(ncache_max))
    nopt = 10

    if (allocated(CacheVals_local)) then
      deallocate(CacheVals_local)
    end if
    allocate(CacheVals_local(1,1))    
    
    ncache = 1
    ncall = 0
    ncall_max = 0
    ncalc_max = 0
    id_local = 0
    id_max = 0
    maxnval = 0
    nval_local = 1

    infwri = .false.
    if (infoutlev_cache.ge.1) call InfOut_cache('InitCacheSystem_cll','cache system initialized',infwri)    
    if(infwri) write(ninfout_cache,fmt90) 'COLLIER-Cache:', mnc, ' caches initialized at level', Nmax

  end subroutine InitCacheSystem_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine Setninfout_cache(ninfout)
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine Setninfout_cache(ninfout)

    integer, intent(in) :: ninfout

    ninfout_cache = ninfout

  end subroutine Setninfout_cache





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine Setinfoutlev_cache(infoutlev)
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine Setinfoutlev_cache(infoutlev)

    integer, intent(in) :: infoutlev

    infoutlev_cache = infoutlev

  end subroutine Setinfoutlev_cache





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOffCacheSystem_cll
  !
  !  switches off temporarily the whole cache-system
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOffCacheSystem_cll

    integer :: i
    logical :: infwri
    
    do i=1,ncache_max
      call SetCacheMode_cll(i,1)
    end do
    
    if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOffCacheSystem_cll','cache system switched off',infwri)    

  end subroutine SwitchOffCacheSystem_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOnCacheSystem_cll
  !
  !  used to switch on the cache-system again after it had 
  !  been switched off temporarily
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOnCacheSystem_cll

    integer :: i
    logical :: infwri

    if (ncache_max.le.0) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SwitchOnCacheSystem_cll','cache has not been initialized',infwri)    
      if(infwri)  write(ninfout_cache,*) '--> it cannot be switched on' 
    else  
      do i=1,ncache_max
        call SetCacheMode_cll(i,2)
      end do
      if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOffCacheSystem_cll','cache system switched on',infwri) 
    end if

  end subroutine SwitchOnCacheSystem_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOffCache_cll(ncache_in)
  !
  !  switches off temporarily the cache ncache_in
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOffCache_cll(ncache_in)

    integer, intent(in) :: ncache_in
    logical :: infwri

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SwitchOffCache_cll','individual cache cannot be switched off',infwri)    
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'
    else      
      call SetCacheMode_cll(ncache_in,1)
      infwri = .false.
      if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOffCache_cll','individual cache switched off',infwri)       
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'switched off'
    end if

  end subroutine SwitchOffCache_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOnCache_cll(ncache_in)
  !
  !  used to switch on the cache ncache_in again after it had 
  !  been switched off temporarily
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOnCache_cll(ncache_in)

    integer, intent(in) :: ncache_in
    logical :: infwri

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SwitchOnCache_cll','individual cache cannot be switched on',infwri)       
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'
    else 
      call SetCacheMode_cll(ncache_in,2)
      infwri = .false.
      if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOnCache_cll','individual cache switched on',infwri)       
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'switched on'      
    end if

  end subroutine SwitchOnCache_cll

  



  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOffCacheSystem0_cll
  !
  !  switches off temporarily the whole cache-system
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOffCacheSystem0_cll
  
    logical :: infwri

    use_cache_system = .false.
    if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOffCacheSystem0_cll', &
                                              'cache system (+internal cache) switched off',infwri)       

  end subroutine SwitchOffCacheSystem0_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOnCacheSystem0_cll
  !
  !  used to switch on the cache-system again after it had 
  !  been switched off temporarily
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOnCacheSystem0_cll

    logical :: infwri
  
    if (ncache_max.le.0) then
       infwri = .false.
       if (infoutlev_cache.ge.1) call InfOut_cache('SwitchOnCacheSystem0_cll','cache has not been initialized',infwri)    
       if(infwri)  write(ninfout_cache,*) '--> it cannot be switched on'         
    else  
      use_cache_system = .true.
      if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOnCacheSystem0_cll', &
                                                'cache system (+internal cache) switched on',infwri)         
    end if

  end subroutine SwitchOnCacheSystem0_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOffCache0_cll(ncache_in)
  !
  !  switches off temporarily the cache ncache_in
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOffCache0_cll(ncache_in)

    integer, intent(in) :: ncache_in
    logical :: infwri

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SwitchOffCache0_cll','individual cache cannot been switched off',infwri)    
      if(infwri)  write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'
    else      
      use_cache_cp(ncache_in) = use_cache(ncache_in)
      use_cache(ncache_in) = 0
      infwri = .false.
      if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOffCache0_cll','individual cache switched off (also internally)',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'switched off'
    end if

  end subroutine SwitchOffCache0_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SwitchOnCache0_cll(ncache_in)
  !
  !  used to switch on the cache ncache_in again after it had 
  !  been switched off temporarily
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SwitchOnCache0_cll(ncache_in)

    integer, intent(in) :: ncache_in
    logical :: infwri

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SwitchOnCache0_cll','individual cache cannot be switched on',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'    
    else 
      use_cache(ncache_in) = use_cache_cp(ncache_in)
      infwri = .false.
      if (infoutlev_cache.ge.2) call InfOut_cache('SwitchOnCache0_cll','individual cache switched on',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'switched on'     
    end if

  end subroutine SwitchOnCache0_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SetCacheMode_cll(ncache_in,mode_in)
  !
  !  set the mode of cache ncache_in to
  !  1: only internal calls are cached
  !  2: internal and external calls are cached
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SetCacheMode_cll(ncache_in,mode_in)

    integer, intent(in) :: ncache_in,mode_in
    logical :: infwri

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SetCacheMode_cll','cache cannot be modified',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'
      
    else if ((mode_in.lt.1).or.(mode_in.gt.2)) then
      if (infoutlev_cache.ge.1) call InfOut_cache('SetCacheMode_cll', &
                              'cache can only be set to mode 1 (internal) or 2 (internal + external)!',infwri) 
    else
      if (mode_in.eq.1) then
        if (cache_mode(ncache_in).ne.-1) then
          cache_mode_cp(ncache_in) = cache_mode(ncache_in)
        end if
        cache_mode(ncache_in) = -1
!        onlyinternal = .true.
!        if (infoutlev_cache.ge.2) then
!          write(ninfout_cache,*) 'COLLIER-Cache: cache no.', ncache_in, 'set to mode 1 (internal)'
!        end if
      else
        cache_mode(ncache_in) = cache_mode_cp(ncache_in)
!        onlyinternal = .false.
!        if (infoutlev_cache.ge.2) then
!          write(ninfout_cache,*) 'COLLIER-Cache: cache no.', ncache_in, 'set to mode 2 (internal + external)'
!        end if
      end if       
    end if

  end subroutine SetCacheMode_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SetCacheLevel_cll(ncache_in,Nmax)
  !
  !  can be called after InitCacheSystem to set the level
  !  of an individual cache ncache_in to the value Nmax:
  !  N-point tensor integrals are cache in nache_in for N<=Nmax 
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SetCacheLevel_cll(ncache_in,Nmax)

    integer, intent(in) :: ncache_in,Nmax
    logical :: infwri
    character(len=*),parameter :: fmt90 = "(A10,I3,A24,I3)"
    character(len=*),parameter :: fmt91 = "(A10,I3,A29)"      

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SetCacheLevel_cll','cache cannot be modified',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'    
    else
      if (cache_mode(ncache_in).ne.-99) then
        infwri = .false.
        if(infoutlev_cache.ge.1) call InfOut_cache('SetCacheLevel_cll','cache-level cannot be modified at this stage',infwri) 
        if(infwri) then
          if(cache_mode(ncache_in).eq.-1) then 
            write(ninfout_cache,fmt91) 'cache no.', ncache_in, 'only used for internal calls'
          else
            write(ninfout_cache,fmt90) 'cache no.', ncache_in, 'already in use at level', use_cache(ncache_in)
          end if
        end if
      else
        use_cache(ncache_in) = Nmax
        use_cache_cp(ncache_in) = Nmax
        infwri = .false.
        if (infoutlev_cache.ge.2) call InfOut_cache('SetCacheLevel_cll','cache level modified',infwri) 
        if(infwri) write(ninfout_cache,*) 'COLLIER-Cache: level of cache no.', ncache_in, 'set to ', Nmax
      end if
    end if

  end subroutine SetCacheLevel_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SetTenCache_cll(Nten)
  !
  !  tensors are cached for N>=Nten
  !  coefficients are cached for N<Nten 
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SetTenCache_cll(Nten)

    integer, intent(in) :: Nten

    tencache = Nten

  end subroutine SetTenCache_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine SetNopt_cll(ncache_in,no)
  !
  !  can be called after InitCacheSystem to set the number
  !  of optimization runs no for an individual cache 
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine SetNopt_cll(ncache_in,no)

    integer, intent(in) :: ncache_in,no
    logical :: infwri

    if ((ncache_in.le.0).or.(ncache_in.gt.ncache_max)) then 
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('SetNopt_cll','optimization level cannot be set',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist!'    
    else if (no.lt.0) then
      if (infoutlev_cache.ge.1) call InfOut_cache('SetNopt_cll','argument no has to be a non-negative integer!',infwri)     
    else
      nopt(ncache_in) = no
      infwri = .false.
      if (infoutlev_cache.ge.2) call InfOut_cache('SetNopt_cll','optimization level set',infwri) 
      if(infwri) write(ninfout_cache,*) 'COLLIER-Cache: number of optimization points for cache no.', &
                                        ncache_in, 'set to ', no
    end if

  end subroutine SetNopt_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine InitCache_cll(ncache_in)
  !
  !  to be called for each phase-space point before
  !  the evaluation of the tensor-integrals
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine InitCache_cll(ncache_in)

    integer, intent(in) :: ncache_in
    integer, allocatable :: casa_swap(:,:), cara_swap(:,:), new_casa_swap(:,:) 
    integer, allocatable :: CachePoint_swap(:,:,:), new_cara_swap(:,:)
    integer :: i,nsize,nc_max
    logical :: infwri
 
    if ((.not.use_cache_system).or.(ncache_max.lt.ncache_in)) then
      infwri = .false.
      if (infoutlev_cache.ge.1) call InfOut_cache('InitCache_cll','cache cannot be initialized for new phase-space point',infwri) 
      if(infwri) write(ninfout_cache,*) 'cache no.', ncache_in, 'does not exist or is switched off!'       
      return
    end if

    ncache = ncache_in
    if (cache_mode(ncache).eq.-1) return

    nevent(ncache) = nevent(ncache)+1
    ! write(*,*) 'COLLIER: cache no.', ncache_in, 'reinitialized for event no.', nevent(ncache)

    if (nevent(ncache).ge.nopt(ncache)+4) then
      ! fully optimized runs
      cache_mode(ncache) = 0

      deallocate(CacheVals)
      allocate(CacheVals(nval_max(ncache),ncalc(ncache)))
      nval_tmp = nval_max(ncache)

    else if (nevent(ncache).eq.1) then
      ! initialization run no.1
      cache_mode(ncache) = 1
      ncalc(ncache) = 0


    else if (nevent(ncache).eq.2) then
      ! initialization run no.2
      cache_mode(ncache) = 2

      if (allocated(CacheLib)) then
        deallocate(CacheLib)
      end if
      allocate(CacheLib(ncalc(ncache)))

      if (allocated(CacheArgs)) then
        deallocate(CacheArgs)
      end if
      allocate(CacheArgs(narg_max(ncache),ncalc(ncache)))

      if (allocated(catype)) then
        deallocate(catype)
      end if
      allocate(catype(ncalc(ncache)))


      nc_max = maxval(ncalc)
      if (size(casa,1).ne.nc_max) then
        allocate(casa_swap(size(casa,1),ncache_max))
        casa_swap = casa

        deallocate(casa)
        allocate(casa(nc_max,ncache_max))
        casa = 0
        nsize = min(size(casa_swap,1),nc_max)
        casa(1:nsize,1:ncache_max) = casa_swap(1:nsize,1:ncache_max)
      end if

      if (size(cara,1).ne.nc_max) then
        allocate(cara_swap(size(cara,1),ncache_max))
        cara_swap = cara

        deallocate(cara)
        allocate(cara(nc_max,ncache_max))
        cara = 0
        nsize = min(size(cara_swap,1),nc_max)
        cara(1:nsize,1:ncache_max) = cara_swap(1:nsize,1:ncache_max)
      end if

      if ((size(CachePoint,1).le.id_max).or.(size(CachePoint,2).lt.ncall_max)) then
        allocate(CachePoint_swap(0:size(CachePoint,1)-1,size(CachePoint,2),ncache_max))
        CachePoint_swap = CachePoint
        deallocate(CachePoint)
        allocate(CachePoint(0:id_max,ncall_max,ncache_max))
        CachePoint = 0
        CachePoint(0:size(CachePoint_swap,1)-1,1:size(CachePoint_swap,2),1:ncache_max) = CachePoint_swap
      end if
          
      ncalc(ncache) = 0


    else if (nevent(ncache).eq.3) then
      ! first optimization run
      cache_mode(ncache) = 3

      if (allocated(CacheLib)) then
        deallocate(CacheLib)
      end if
      if (allocated(CacheArgs)) then
        deallocate(CacheArgs)
      end if
      if (allocated(catype)) then
        deallocate(catype)
      end if

      if (allocated(CacheVals)) then
        deallocate(CacheVals)
      end if
      maxnval = nval_max(ncache)
      allocate(CacheVals(maxnval,ncalc(ncache)))

      nc_max = maxval(ncalc)
      if (size(casa,1).ne.nc_max) then
        allocate(casa_swap(size(casa,1),ncache_max))
        casa_swap = casa

        deallocate(casa)
        allocate(casa(nc_max,ncache_max))
        casa = 0
        nsize = min(size(casa_swap,1),nc_max)
        casa(1:nsize,1:ncache_max) = casa_swap(1:nsize,1:ncache_max)
      end if

      if (size(cara,1).ne.nc_max) then
        allocate(cara_swap(size(cara,1),ncache_max))
        cara_swap = cara

        deallocate(cara)
        allocate(cara(nc_max,ncache_max))
        cara = 0
        nsize = min(size(cara_swap,1),nc_max)
        cara(1:nsize,1:ncache_max) = cara_swap(1:nsize,1:ncache_max)
      end if

      if (size(new_casa,1).ne.nc_max) then
        allocate(new_casa_swap(size(new_casa,1),ncache_max))
        new_casa_swap = new_casa

        deallocate(new_casa)
        allocate(new_casa(nc_max,ncache_max))
        new_casa = 0
        nsize = min(size(new_casa_swap,1),nc_max)
        new_casa(1:nsize,1:ncache_max) = new_casa_swap(1:nsize,1:ncache_max)
      end if

      if (size(new_cara,1).ne.nc_max) then
        allocate(new_cara_swap(size(new_cara,1),ncache_max))
        new_cara_swap = new_cara

        deallocate(new_cara)
        allocate(new_cara(nc_max,ncache_max))
        new_cara = 0
        nsize = min(size(new_cara_swap,1),nc_max)
        new_cara(1:nsize,1:ncache_max) = new_cara_swap(1:nsize,1:ncache_max)
      end if

      nval_tmp = nval_max(ncache)     


    else if ((nevent(ncache).ge.4).and.(nevent(ncache).le.nopt(ncache)+3)) then
      ! further optimization runs
      cache_mode(ncache) = 3

      deallocate(CacheVals)
      maxnval = nval_max(ncache)
      allocate(CacheVals(maxnval,ncalc(ncache)))

      do i=1,ncalc(ncache)
        if (new_casa(i,ncache).gt.casa(i,ncache)) then
          casa(i,ncache) = new_casa(i,ncache)
        end if
        if (new_cara(i,ncache).lt.cara(i,ncache)) then
          cara(i,ncache) = new_cara(i,ncache)
        end if
      end do
      
      nval_tmp=maxnval

    end if

    ncall = 0
    new_casa(:,ncache) = 0
    new_cara(:,ncache) = 0
    

  end subroutine InitCache_cll





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine ReadCache(vals,nval,args,narg,lib,id,N,r,nocalc,wrica)
  !
  !  check if the nval N-point coefficients up to rank r 
  !  with the narg arguments args are already cached or have to be cached:
  !
  !  1) if they are cached already:
  !     read them from the cache --> the nval values vals are returned
  !     nocalc = .true. and wrica = .false. is returned
  !  2) if they are not yet cached but are needed more than once und thus should be 
  !     written to the cache:
  !     .nocalc = .false. and wrica = .true. is returned
  !  3) if they are only needed once and thus do not have to be cached:
  !      nocalc = .false. and wrica = .false. is returned
  !
  !  Identical function calls are identified assuming a fixed order of the function calls.
  !  The required rank r up to which the respective coefficients have to be cached is 
  !  optimized during the first nopt(ncache) optimization runs.  
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine ReadCache(vals,nval,args,narg,lib,id,N,r,nocalc,wrica)

    integer, intent(in) :: id,lib,N,nval,narg
    integer, intent(inout) :: r
    double complex, intent(in) :: args(narg)
    double complex, intent(out) :: vals(nval) 
    logical, intent(out) :: nocalc,wrica
    logical :: nohit
    integer :: i,j,nca

    nocalc = .false.
    wrica = .false.

    if (use_cache_system) then
      if ((cache_mode(ncache).eq.-1).and.(lib.eq.2)) return
      
      if (id.eq.0) then
        if (cache_mode(ncache).eq.-1) then
          id_local = max(id_local,2**N-3)
          if (allocated(rankcached)) then
            deallocate(rankcached)
          end if
          allocate(rankcached(0:id_local))
          rankcached = -1
          if (nval.gt.nval_local) nval_local = nval         
          if (allocated(CacheVals_local)) then
            deallocate(CacheVals_local)
          end if
          allocate(CacheVals_local(nval_local,id_local))
          return
        else
          ncall = ncall+1
          if (cache_mode(ncache).eq.1) then
            id_max = max(id_max,2**N-3)
          end if
        end if
      end if

      if(use_cache(ncache).ge.N) then

        select case(cache_mode(ncache))
 
          case(0)
            ! fully optimized run

            nca = CachePoint(id,ncall,ncache)
            if (nca.eq.0) return
 
            if (casa(nca,ncache).gt.1) then
              ! coefficient has to be written or
              ! can be read from cache
              new_casa(nca,ncache) = new_casa(nca,ncache)+1

              if (new_casa(nca,ncache).gt.1) then
                if (r.le.new_cara(nca,ncache)) then
                  ! coefficient can be read from cache
                  vals(1:nval) = CacheVals(1:nval,nca)
                  nocalc = .true.
                else
                  ! coefficient has to be written to cache          
                  wrica = .true.                 
                end if

              else
                ! coefficient has to be stored in cache for the first time
                r = max(cara(nca,ncache),r)          
                wrica = .true.

              end if

            end if


          case(1)
            ! initialization run no.1
            ! determine maximum size of args and id 
            narg_max(ncache) = max(narg_max(ncache),narg)
            ncall_max = max(ncall_max,ncall)
            ncalc(ncache) = ncalc(ncache)+1


          case(2)
            ! initialization run no.2
            ! determine # of calculations for each coefficient
            nca=0
            nohit = .true.
            do while (nohit.and.(nca.lt.ncalc(ncache)-1))
              nca = nca+1
              if ((N.eq.catype(nca)).and.(lib.eq.CacheLib(nca))) then
                nohit = .false.
                do j=1,narg
                  if (args(j).ne.CacheArgs(j,nca)) then
                    nohit = .true.
                  end if
                end do
              end if
            end do

            if (nohit) then
              ncalc(ncache) = ncalc(ncache)+1 
              casa(ncalc(ncache),ncache) = 1
              cara(ncalc(ncache),ncache) = r
              catype(ncalc(ncache)) = N
              CacheLib(ncalc(ncache)) = lib
              CacheArgs(1:narg,ncalc(ncache)) = args
              CachePoint(id,ncall,ncache) = ncalc(ncache)
            else
              casa(nca,ncache) = casa(nca,ncache)+1
              cara(nca,ncache) = max(cara(nca,ncache),r)
              CachePoint(id,ncall,ncache) = nca
            end if

            nval_max(ncache) = max(nval_max(ncache),nval)


          case(3)
            ! optimization run
            ! try to maximize casa and minimize cara
            nca = CachePoint(id,ncall,ncache)
            if (nca.eq.0) return
!            new_cara(nca,ncache) = max(new_cara(nca,ncache),r)

            if (casa(nca,ncache).gt.1) then
              ! coefficient has to be written or
              ! can be read from cache
              new_casa(nca,ncache) = new_casa(nca,ncache)+1

! AD 18.3.15  cara replaced by new_cara twice

              if (new_casa(nca,ncache).gt.1) then
                ! coefficient can be read from cache
                if (r.le.new_cara(nca,ncache)) then
                  vals(1:nval) = CacheVals(1:nval,nca)
                  nocalc = .true.
                end if

              else
                ! coefficient has to be stored in cache
                r = max(new_cara(nca,ncache),r)          
                wrica = .true.

              end if      

            end if

 
          case(-1)
            ! cache only internal calls

            if (r.le.rankcached(id)) then
              ! coefficient can be read from cache
              vals(1:nval) = CacheVals_local(1:nval,id)
              nocalc = .true.
            else
              ! coefficient has to be written to cache          
              wrica = .true.                 
            end if

        end select

      end if

    end if


  end subroutine ReadCache





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine WriteCache(vals,nval,id,N,r)
  !
  !  write the nval coefficients vals to the cache
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  subroutine WriteCache(vals,nval,id,N,r)

    integer, intent(in) :: nval,id,N,r
    double complex, intent(in) :: vals(nval)
    double complex, allocatable :: CacheVals_aux(:,:)
    integer :: nvalwri,nca,nvalold

    if (use_cache_system.and.(use_cache(ncache).ge.N)) then

      if ((cache_mode(ncache).eq.0).or.(cache_mode(ncache).eq.3)) then
        
        nca = CachePoint(id,ncall,ncache)
        new_cara(nca,ncache) = r 

        if (nval.gt.nval_tmp) then
          ! increase size of cache
          nvalold = nval_tmp
          allocate(CacheVals_aux(nvalold,ncalc(ncache)))    
          CacheVals_aux = CacheVals
          deallocate(CacheVals)
          nval_tmp = nval
          nval_max(ncache) = nval_tmp
          allocate(CacheVals(nval_tmp,ncalc(ncache)))
          CacheVals(1:nvalold,1:ncalc(ncache)) = CacheVals_aux(1:nvalold,1:ncalc(ncache))
        end if

        CacheVals(1:nval,nca) = vals(1:nval)

      else if (cache_mode(ncache).eq.-1) then
        
        rankcached(id) = r

        if (nval.gt.nval_local) then
          ! increase size of cache
          nvalold = nval_local
          allocate(CacheVals_aux(nvalold,id_local))    
          CacheVals_aux = CacheVals_local
          deallocate(CacheVals_local)
          nval_local = nval
          allocate(CacheVals_local(nval_local,id_local))
          CacheVals_local(1:nvalold,1:id_local) = CacheVals_aux(1:nvalold,1:id_local)
        end if

        CacheVals_local(1:nval,id) = vals(1:nval)
      
      end if

    end if

  end subroutine WriteCache





  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  !  subroutine InfOut_cache(sub,inf,flag)
  !
  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

! Suppression of output must be implemented in calling routines!

  subroutine InfOut_cache(sub,inf,flag)

    character(len=*), intent(in) :: sub, inf
    logical, intent(out) :: flag
!    integer, parameter :: maxErrOut=100
  
    flag = .false.
    if (infoutlev_cache.eq.0) return

    InfCnt_cll = InfCnt_cll + 1      
    if(ninfout_cache.ne.-1) then
      if (InfCnt_cll.le.MaxInfOut_cll) then
        write(ninfout_cache,*)
        write(ninfout_cache,*)
        write(ninfout_cache,*)
        write(ninfout_cache,*) '***********************************************************'
        write(ninfout_cache,*) 'Info-output NO.', InfCnt_cll
        write(ninfout_cache,*) 'in routine: ', trim(sub)
        write(ninfout_cache,*) trim(inf)
!        call WriteMaster_cll(nerrout_cll)
        flag=.true.
      elseif (InfCnt_cll.eq.MaxInfOut_cll+1) then
        write(ninfout_cache,*)
        write(ninfout_cache,*)
        write(ninfout_cache,*)
        write(ninfout_cache,*) '***********************************************************'
        write(ninfout_cache,*)
        write(ninfout_cache,*) ' Further output of information will be suppressed '
        write(ninfout_cache,*)
      endif
    endif

  end subroutine InfOut_cache  



end module cache

