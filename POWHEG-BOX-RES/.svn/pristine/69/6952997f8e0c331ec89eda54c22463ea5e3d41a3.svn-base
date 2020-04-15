c generic cache system to identify proportional subamplitudes.
c The user does:
c     include 'pwhg_cache.h'
c     type(cache_pointer), save :: ptr
c     integer, save :: ind
c     if(ini) then
c         call init_cache_similar('test',20)
c to initialize a cache with 20 subprocesses
c         call get_cache_pointer('test',ind,ptr)
c         ini=.false.
c     endif
c     Now loop through the subprocesses in order; for each subprocess j do:
c     get_cache_value(ptr,j,k,coef)
c     If k<0 the result for subprocess j is not equivalent to any previous 1, and
c     it must be computed.
c     If k>0 then
c     if coef = 0 the subprocess in question is zero.
c     if coef /=0 the subprocess in question is proportional to the subprocess k<j
c     with a proportionality factor coef.
c     Set filled(j) = .true. for all processes that have been computed in the loop,
c     .false. if the process was not considered in this loop.
c     After having gone through all subprocesses to be computed, call:
c     call store_cache_similar(ptr,rrr,filled), where rrr are the value of the subprocesses.




      subroutine test_cache_similar
      implicit none
c test it;
c assume we have 20 entries, even, multiples of 3 and remaining are called together
      include 'pwhg_cache.h'
      real * 8 rrr(20),xxx,coef,random
      integer igr,l,k,j,ind
      logical filled(20)
      type(cache_pointer) :: ptr
      procedure() :: random
      call randomsave
c initialize a cache. Do it just once for each function to cache.
      call init_cache_similar('test',20)

c get a cache pointer. Do it every time you enter the function, or just after
c the previous call if you save it.
      call get_cache_pointer('test',ind,ptr)

c test
      do l=1,10000
         igr = random()*3
         filled = .false.
         xxx = random()
         do k=1,21
            if(k.lt.7*igr) cycle
            if(k.ge.7*(igr+1)) cycle
c if status is 1 (cache filled) get a pointer and a coefficient
c to already computed values.
            call get_cache_value(ptr,k,j,coef)
            filled(k) = .true.
            if(2*(k/2).eq.k) then
               rrr(k) = xxx
            else
               rrr(k) = 2*xxx
            endif
            if(j.gt.0) then
               write(*,*)  rrr(k)/(coef*rrr(j))
            endif
         enddo
      enddo
      call randomrestore
      end

      
c     initialize a cache for arrays of num elements,
c     with character identifier id
      subroutine init_cache_similar(id,num)
      implicit none
      character *(*) id
      integer num
      include 'pwhg_cache.h'
      type(cache_pointer) :: ptr
      integer ind
      logical ini
      data ini/.true./
      save ini
      if(ini) then
         cache_nptrs = 0
         ini = .false.
      endif
      call get_cache_pointer(id,ind,ptr)
      if(ind.gt.0) then
         write(*,*) ' init_cache_similar: intialized twice!'
         write(*,*) ' exiting ...'
         call exit(-1)
      endif
      cache_nptrs = cache_nptrs + 1
      call allocate_cache(cache_ptrs(cache_nptrs),id,num)
      end

      subroutine store_cache_similar(ptr,resvals,filled)
      implicit none
      include 'pwhg_cache.h'
      type(cache_pointer) :: ptr
      real * 8 resvals(*)
      logical filled(*)
      integer whichgroup,ncalls,j
      if(ptr%status == 1) return
      whichgroup = -1
      do j=1,ptr%num
         if(filled(j)) then
            if(whichgroup.eq.-1) then
c This is the first filled entry
               whichgroup = ptr%whichgroup(j)
               ncalls = ptr%ncalls(j)
               if(whichgroup.eq.0) then
c This is the first time that this group is hit;
                  ptr%numgroups = ptr%numgroups + 1
               endif
            elseif(ptr%whichgroup(j).ne.whichgroup
     1              .or. ptr%ncalls(j).ne.ncalls) then
c if whichgroup is zero (first time this group was hit), all elements of the
c group must have ptr%whichgroup = 0. Same if whichgroup was already set.
               write(*,*) '  store_cache_similar: entries do not match'
               call exit(-1)
            endif
            if(whichgroup.eq.0) then
c set the whichgroup label for all elements of the current group
               ptr%whichgroup(j) = ptr%numgroups
            else
               if(ptr%ncalls(j).ge.maxcheckvalues) cycle
c The group is complete; skip all of them (but goes through the above check, i.e.
c ncalls and whichgroup must match
            endif
            ptr%ncalls(j) = ptr%ncalls(j) + 1
            ptr%values(ptr%ncalls(j),j) = resvals(j)
            if(resvals(j) == 0) then
               if(ptr%zerosofar(j) >=0) then
                  ptr%zerosofar(j) = ptr%zerosofar(j) + 1
                  if(ptr%zerosofar(j) > maxzeros) then
                     write(*,*) ' amplitude ',j,' in ',trim(ptr%id)//
     1                    ' was zero for over ',maxzeros,
     2                    ' calls; set to zero.'
                     ptr%equivto(j) = 1
                     ptr%equivcoef(j) = 0
                     ptr%zerosofar(j) = -1
                  endif
               endif
            else
               ptr%zerosofar(j) = -1
            endif
         endif
      enddo
c Before we checked that all filled=.true. entries belong to the same group.
c Now check that all entries of the same group have filled=.true.. This
c makes sense only if whichgroup>0, i.e.
      if(whichgroup > 0) then
         do j=1,ptr%num
            if(ptr%whichgroup(j) == whichgroup) then
               if(.not. filled(j)) then
                  write(*,*)
     1                 '  store_cache_similar: missing entry for this group'
                  call exit(-1)
               endif
            endif
         enddo
      endif

c if the current group is full, set up pointers
      if(whichgroup > 0) then
         do j=1,ptr%num
            if(filled(j)) then
               if(ptr%ncalls(j) == maxcheckvalues) then
                  call store_cache_compute(ptr,whichgroup)
c as a side effect the cache could be completed, and ptr%ncalls deallocated;
c return in this case
                  if(ptr%status == 1) return
               else
                  return
               endif
            endif
         enddo
      endif

      end


      subroutine store_cache_compute(ptr,whichgroup)
      implicit none
      include 'pwhg_cache.h'
      type(cache_pointer) :: ptr
      integer whichgroup
      real * 8 tiny
      parameter (tiny = 1d-10)
      integer i,j,k,l
      real * 8 ratios(maxcheckvalues)
      logical pwhg_isfinite
      procedure() :: pwhg_isfinite
      do j=1,ptr%num
         if(ptr%whichgroup(j) .eq. whichgroup ) then
            if(ptr%equivto(j) >= -1) cycle
            if(all(ptr%values(:,j) /= 0)
     1           .and. all(pwhg_isfinite_arr(ptr%values(:,j)))) then
               do k=j+1,ptr%num
                  if(ptr%whichgroup(k) .ne. whichgroup ) cycle
                  if(ptr%equivto(k) >= -1) cycle
                  if(.not. (all(ptr%values(:,k) /= 0)
     1                 .and. all(pwhg_isfinite_arr(ptr%values(:,k))))) cycle
                  do i=1,maxcheckvalues
                     ratios(i) = ptr%values(i,k)/ptr%values(i,j)
                  enddo
                  do i=2,maxcheckvalues
                     if(abs(1-ratios(i)/ratios(1)).gt.tiny) exit
                  enddo
                  if(i.eq.maxcheckvalues + 1) then
                     ptr%equivto(k) = j
                     ptr%equivcoef(k) = ratios(1)
                  endif
               enddo
c The j element is all non-zero and finite. Its ptr%equivto was not set.
c so, it is not equivalent to any previous element.
               ptr%equivto(j) = -1
            endif
         endif
      enddo
c If there are finite entries anywhere
c The only remanining elements (i.e., those with ptr%equivto(j) = -1000000) have either zero or not
c finite values in their value list.
c Now all subamplitude with non vanishing entries have been compared for equivalence
c and, if equivalent, pointers have been set.
c If either both are zero or both are NaN, discard this entry
 5    do j=1,ptr%num
         if(ptr%whichgroup(j) .eq. whichgroup ) then
            if(ptr%equivto(j) >= -1) cycle
            do i=1,ptr%ncalls(j)
               if( (ptr%values(i,j).eq.0) .or.
     1              .not.pwhg_isfinite(ptr%values(i,j))   ) then
c     there are two zero or NaN values at entry i. They cannot be compared. We refuse them,
c     deleting the corresponding i entry for all elements of the current whichgroup
c                  write(*,*) 'cache ',trim(ptr%id),': entry',j,'zero or undefined;'
c     1                 //' delete one call in group ',whichgroup
c                  write(*,*) ptr%values(1:ptr%ncalls(j),j)
c                  write(*,*) ptr%zerosofar(j)
c                  write(*,*) ptr%ncalls(j) - 1,' calls remaining.'
                  do l=1,ptr%num
                     if(ptr%whichgroup(l) .eq. whichgroup .and. ptr%equivto(j) < -1 ) then
                        ptr%values(i:ptr%ncalls(l)-1,l) = ptr%values(i+1:ptr%ncalls(l),l)
                        ptr%ncalls(l) = ptr%ncalls(l) - 1
                     endif
                  enddo
c     restart the loop; need to eliminate all calls that have unusable pairs of entries
                  goto 5
               endif
            enddo
         endif
      enddo
c See if all equivto are set (i.e. all >=-1). If so the cache is completed
      do j=1,ptr%num
         if(ptr%equivto(j) < -1) exit
      enddo
      if(j == ptr%num + 1) then
         write(*,*) ' cache ',trim(ptr%id),' completed'
c call deallocate on stuff that is no longer needed
c status 1 means cache is full
         ptr%status = 1
c deallocate unneded arrays
         deallocate(ptr%values)
         deallocate(ptr%ncalls)
         deallocate(ptr%whichgroup)
         deallocate(ptr%zerosofar)
         call printequiv_by_id(ptr%id)
      endif
      contains
      function  pwhg_isfinite_arr(arr)
      real * 8 arr(:)
      logical pwhg_isfinite_arr(size(arr))
      integer j
      do j=1,size(arr)
         pwhg_isfinite_arr(j) = pwhg_isfinite(arr(j))
      enddo
      end function pwhg_isfinite_arr
      end

                        
c     returns the index of the given cache in icurrent, and
c     its pointer in ptr. If it does not exist, icurrent = -1
      subroutine get_cache_pointer(id,icurrent,ptr)
      implicit none
      character *(*) id
      integer icurrent
      include 'pwhg_cache.h'
      type(cache_pointer) :: ptr
      integer j
      do j=1,cache_nptrs
         if(id.eq.cache_ptrs(j)%id) then
            icurrent = j
            ptr = cache_ptrs(j)
            return
         endif
      enddo
      icurrent = -1
      end

      subroutine get_cache_value(ptr,k,j,coef)
      implicit none
      include 'pwhg_cache.h'
      type(cache_pointer) :: ptr
      integer j,k
      real * 8 coef
      if(ptr%equivto(k).gt.0) then
         j = ptr%equivto(k)
         coef = ptr%equivcoef(k)
         call increasecnt(trim(ptr%id)//' cache hit')
      else
         j = -1
         call increasecnt(trim(ptr%id)//' cache miss')
      endif
      end

      subroutine allocate_cache(ptr,id,num)
      implicit none
      character *(*) id
      integer num
      include 'pwhg_cache.h'
      type(cache_pointer) :: ptr
      allocate(ptr%id)
      allocate(ptr%status)
      allocate(ptr%num)
      allocate(ptr%numgroups)
c if some entries are zero, discard them and try again, no more than tries times
      ptr%tries = 0
c number of different entries to compare for proportionality
      ptr%num = num
c status = 0: cache not yet filled; =1: cache full, ready to return equivalent entries
      ptr%status = 0
c numgroups is the total number of groups of entries within which we can compare values
      ptr%numgroups = 0
c identifier
      ptr%id = id
      allocate(ptr%values(maxcheckvalues,num))
c      ptr%values = 0
c proportionality coefficient
      allocate(ptr%equivcoef(num))
      ptr%equivcoef = 0
c pointer to proportional entry
      allocate(ptr%equivto(num))
      ptr%equivto = -1000000
c number of hits in a given group
      allocate(ptr%ncalls(num))
      ptr%ncalls = 0
c This number denotes at which call an entry was hit.
c It is used to distinguish groups of entries that can be checked for
c proportionality.
      allocate(ptr%whichgroup(num))
      ptr%whichgroup = 0
c This keeps the count of how many times this entries gave zero.
c It applies only to entries that never turned out different from zero.
c If the count is above maxzeros, the entry is assumed to be zero.
      allocate(ptr%zerosofar(num))
      ptr%zerosofar = 0
      end



c     This depends upon other POWHEG BOX stuff. Take it away if
c     you need cache similar for purposes other than POWHEG-RES,
c     or if you want to compile the test_cache_similar only.
      subroutine printequiv(id,nflav,num,flav,res,lflav)
      implicit none
      character *(*) id
      integer nflav,num,flav(nflav,num),res(nflav,num),lflav(num)
      include 'pwhg_cache.h'
      integer, save :: cacheind
      type(cache_pointer),save  :: cacheptr
      integer iun,j,k,l,itmp
      logical nonzeros
      real * 8 coef
      call get_cache_pointer(id,cacheind,cacheptr)
      if(cacheind == -1) then
         write(*,*) " printequiv: should'nt be here!"
         write(*,*) trim(id)//" cache does not exist!"
         call exit(-1)
      endif
      call newunit(iun)
      open(unit=iun,file=trim(id)//'_equiv',status='unknown')
      write(*,*) 'Writing '//trim(id)//'_equiv file...'
      do j=1,num
         call get_cache_value(cacheptr,j,itmp,coef)
         if(itmp == -1) then
            l=lflav(j)
            write(iun,'(a)')
     1           'Beginning sequence of equivalent amplitudes'
            write(iun,100) 1d0,j, flav(1:l,j)
            write(iun,101) '            resptrs:', res(1:l,j)
            do k=1,num
               call get_cache_value(cacheptr,k,itmp,coef)
               if(itmp == j .and. coef /= 0) then
                  if(l /= lflav(k)) then
                     write(*,*) ' printequiv: two equivalent processes'
                     write(*,*) ' with different lengths!'
                     call exit(-1)
                  endif
                  write(iun,100)  coef,k, flav(1:l,k)
                  write(iun,101) '            resptrs:', res(1:l,k)
               endif
            enddo
         endif
      enddo
      nonzeros = .true.
      do j = 1,num
         call get_cache_value(cacheptr,j,itmp,coef)
         l=lflav(j)
         if(coef == 0) then
            if(nonzeros) then
               write(iun,'(a)') 'Vanishing amplitudes:'
               nonzeros = .false.
            endif
            write(iun,100) coef,j, flav(1:l,j)
            write(iun,101) '            resptrs:', res(1:l,j)
         endif
      enddo
      close(iun)
 100  format(d11.4,5x,i4,5x,100(i4,1x))
 101  format(a,5x,100(i4,1x))
      end

      subroutine printequiv_by_id(id)
      implicit none
      character *(*) id
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      select case(id)
      case ( 'allborn', 'sigvirtual')
         call printequiv(id,nlegborn,flst_nborn,
     1        flst_born,flst_bornres,flst_bornlength)
      case ( 'sigreal_rad','sigreal_btl0' )
         call printequiv(id,nlegreal,flst_nalr,
     1        flst_alr,flst_alrres,flst_alrlength)
      case ( 'sigregular' )
         call printequiv(id,nlegreal,flst_nregular,
     1        flst_regular,flst_regularres,flst_regularlength)
      case default
         write(*,*) ' printequiv_by_id: unknown id',id
         call exit(-1)
      end select
      end

      subroutine get_index_live_subp(id,index_in,index_out)
      implicit none
      include 'pwhg_cache.h'
      character(len=*) id
      integer, intent(in) :: index_in
      integer, intent(out) :: index_out
      type(cache_pointer) :: ptr
      integer ind
      call get_cache_pointer(id,ind,ptr)
      index_out = ptr%equivto(index_in)
      if(index_out .le. 0) index_out = index_in
      end
