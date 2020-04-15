c -*- Fortran -*-
      subroutine resize_array_int1(ar,newsize)
      implicit none
      include 'pwhg_dynarrs.h'
      type(intdynarr1):: ar
      integer, allocatable:: tmp(:)
      integer oldsize,newsize
      oldsize = size(ar%i)
      if(newsize < oldsize) then
         write(*,*) ' resize_array_int1: new size=', newsize
         write(*,*) ' resize_array_int1: old size=', oldsize
         write(*,*) ' not allowed: exiting ...'
         call exit(-1)
      endif
      allocate(tmp(oldsize))
      tmp = ar%i
      deallocate(ar%i)
      allocate(ar%i(newsize))
      ar%i(1:oldsize)=tmp
      deallocate(tmp)
      end

c -*- Fortran -*-
      subroutine resize_array_int2(ar,new1,new2)
      implicit none
      include 'pwhg_dynarrs.h'
      type(intdynarr2):: ar
      integer, allocatable:: tmp(:,:)
      integer new1,new2
      integer old1,old2
      old1 = size(ar%i,1)
      old2 = size(ar%i,2)
      if(new1 < old1 .or. new2 .lt. old2) then
         write(*,*) ' resize_array_int1: new size=(', new1,new2,')'
         write(*,*) ' resize_array_int1: old size=(', old1,old2,')'
         write(*,*) ' not allowed: exiting ...'
         call exit(-1)
      endif
      allocate(tmp(old1,old2))
      tmp = ar%i
      deallocate(ar%i)
      allocate(ar%i(new1,new2))
      ar%i(1:old1,1:old2)=tmp
      deallocate(tmp)
      end
