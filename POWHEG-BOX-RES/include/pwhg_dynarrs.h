c -*- Fortran -*-
      type intdynarr1
         sequence
         integer, pointer::i(:)
      end type intdynarr1
      type intdynarr2
         sequence
         integer, pointer::i(:,:)
      end type intdynarr2
      type intdynarr3
         sequence
         integer, pointer::i(:,:,:)
      end type intdynarr3
         
