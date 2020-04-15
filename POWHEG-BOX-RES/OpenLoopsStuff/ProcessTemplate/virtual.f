      subroutine setvirtual(p,vflav,virtual)
c Wrapper subroutine to call OL Virtual
      implicit none
      include 'nlegborn.h'
      include 'pwhg_st.h'
      include 'pwhg_math.h'
      include 'PhysPars.h'
      integer, parameter :: nlegs=nlegbornexternal
      real * 8, intent(in)  :: p(0:3,nlegs)
      integer,  intent(in)  :: vflav(nlegs)
      real * 8, intent(out) :: virtual

      call openloops_virtual(p,vflav,virtual)
      end
