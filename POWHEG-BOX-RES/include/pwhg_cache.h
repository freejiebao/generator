c -*- Fortran -*-
      
      type cache_pointer
         sequence
c Character label of stored caches       
         character * 20, pointer :: id
         real * 8, pointer :: values(:,:),equivcoef(:)
         integer, pointer :: equivto(:),ncalls(:),whichgroup(:),
     1        zerosofar(:)
c     status = 0: cache not yet filled; =1: cache full, ready to return
c     equivalent entries
c     num: size of arrays to check for equivalent entries
c     numgroups: number of groups in the array. We check for
c     equivalence only among entries belonging to the same group
         integer, pointer :: status,num,numgroups
         integer :: tries
      end type cache_pointer
      integer maxcacheptrs,maxcheckvalues,maxtries,maxzeros
      parameter (maxcacheptrs = 20, maxcheckvalues = 20, maxtries = 5,
     1     maxzeros = 100)
      type(cache_pointer) :: cache_ptrs(maxcacheptrs)
c Number of stored pointers
      integer cache_nptrs
      common/c_cache_ptrs/cache_ptrs,cache_nptrs
