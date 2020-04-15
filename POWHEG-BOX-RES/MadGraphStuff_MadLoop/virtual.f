      subroutine setvirtual(p,vflav,virtual)
c Virtual needs to be provided by the user and put here
      implicit none
      include 'pwhg_st.h'
      include 'pwhg_math.h'
      real * 8 p(0:3,*)
      integer vflav(*)
      real * 8 virtual,mu_r,as
      mu_r=sqrt(st_muren2)
      as=st_alpha
      call update_as_param2(mu_r,as)
      call svirt_proc(p,vflav,virtual)
c Cancel as/(2pi) associated with amp2
      virtual = virtual/(st_alpha/(2d0*pi))    
      end
