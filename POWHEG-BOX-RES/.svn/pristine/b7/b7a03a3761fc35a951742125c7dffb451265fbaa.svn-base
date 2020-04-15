      subroutine gen_leshouches_reg
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'LesHouches.h'
      integer j,moth
      integer is_fs(nlegreal),isfslength
      real * 8 p0(0:3,flst_numfsb+3)
      integer rflav0(flst_numfsb+3)
      real * 8 dumamp2      
      call momenta_lh(kn_preal,flst_ireallength)
c Take half of the CM energy
      scalup = sqrt(rad_pt2max)
      nup = flst_ireallength
      do j=1,nup
         idup(j) = flst_regular(j,rad_regularsubp)
         if(idup(j).eq.0) idup(j) = 21
         if(j.le.2) then
            istup(j) = -1
            mothup(:,j) = 0
         else
c resonances are marked later
            istup(j) = 1
         endif
      enddo
      do j=3,nup
         moth =  flst_regularres(j,rad_regularsubp)
         if(moth.ne.0) then
            mothup(1,j) = moth
            mothup(2,j) = moth
            istup(moth) = 2
         else
            mothup(1,j)=1
            mothup(2,j)=2            
         endif
      enddo

      call regularcolour_lh

      end

