      subroutine born_phsp(xborn)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_kn.h'
      include 'pwhg_flst.h'
      include 'pwhg_physpar.h'
      include 'PhysPars.h'
      integer iborn,j
      real * 8 xborn(ndiminteg-3)
c     compute resonance weights for this group
      do iborn=1,flst_nborn
         if(flst_bornresgroup(iborn).eq.flst_ibornresgroup) exit
      enddo
         
      flst_ibornlength = flst_bornlength(iborn)
      flst_ireallength = flst_ibornlength + 1
         
      do j=1,flst_ibornlength
         kn_masses(j) = physpar_phspmasses(flst_born(j,iborn))
      enddo
      
      call genphasespace(xborn,flst_ibornlength,flst_born(:,iborn),
     1     flst_bornres(:,iborn),kn_beams,kn_jacborn,
     1     kn_xb1,kn_xb2,kn_sborn,kn_cmpborn,kn_pborn)
      
      end



      subroutine born_suppression(fact)
      implicit none
      real * 8 fact
      fact=1d0
      end


      subroutine regular_suppression(fact)
      implicit none
      real * 8 fact
      fact=1d0
      end


      subroutine global_suppression(fact)
      implicit none
      real * 8 fact
      fact=1d0
      end


      subroutine set_fac_ren_scales(muf,mur)
      implicit none
      real * 8 muf,mur
      muf=100d0
      mur=100d0
      end
