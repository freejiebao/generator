c     Bornresgroups
c     1 = only fs leptons from Ws
c     2 = s-channel Higgs: qq' -> (W -> l+ nu_l) (H -> l'+ nu_l' q'' q''')
c     3 = s-channel Higgs: qq' -> (W -> q'' q''') (H -> l+ nu_l l'+ nu_l')
c     4 = s-channel Z    : qq' -> (W -> l+ nu_l) (Z -> l'+ nu_l' q'' q''')
c     5 = s-channel Z    : qq' -> (W -> q'' q''') (Z -> l+ nu_l l'+ nu_l')
      
      subroutine t_channel_resonance(xi1,xi2,xf1,xf2)
      implicit none 
      integer xi1, xi2, xf1, xf2
      integer i1, i2, f1, f2
      include 'nlegborn.h'
      include 'pwhg_flst.h'   
      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)
      

      i1=isign*xi1
      i2=isign*xi2
      f1=isign*xf1
      f2=isign*xf2
      
      
         flst_nborn=flst_nborn+1
         flst_born(1,flst_nborn) = i1     ! flavour structure
         flst_born(2,flst_nborn) = i2
         flst_born(3,flst_nborn) = 24*isign
         flst_born(4,flst_nborn) = 24*isign
         flst_born(5,flst_nborn) = lepflav(1)
         flst_born(6,flst_nborn) = lepflav(2)
         flst_born(7,flst_nborn) = lepflav(3)
         flst_born(8,flst_nborn) = lepflav(4)
         flst_born(9,flst_nborn) = f1
         flst_born(10,flst_nborn) = f2

         flst_bornlength(flst_nborn) = 10 ! maximum number of particules including the virtual particle

         flst_bornresgroup(flst_nborn)=1!flst_nborn

         flst_bornres(1,flst_nborn) = 0  ! flavour structure
         flst_bornres(2,flst_nborn) = 0
         flst_bornres(3,flst_nborn) = 0
         flst_bornres(4,flst_nborn) = 0  
         flst_bornres(5,flst_nborn) = 3  
         flst_bornres(6,flst_nborn) = 3 
         flst_bornres(7,flst_nborn) = 4  
         flst_bornres(8,flst_nborn) = 4 
         flst_bornres(9,flst_nborn) = 0
         flst_bornres(10,flst_nborn) = 0

! #### real resonance    

         flst_nreal=flst_nreal+1
         flst_real(1,flst_nreal) = i1     ! flavour structure
         flst_real(2,flst_nreal) = i2
         flst_real(3,flst_nreal) = 24*isign
         flst_real(4,flst_nreal) = 24*isign
         flst_real(5,flst_nreal) = lepflav(1)
         flst_real(6,flst_nreal) = lepflav(2)
         flst_real(7,flst_nreal) = lepflav(3)
         flst_real(8,flst_nreal) = lepflav(4)
         flst_real(9,flst_nreal) = f1
         flst_real(10,flst_nreal) = f2
         flst_real(11,flst_nreal) = 22
         
         flst_reallength(flst_nreal) = 11 ! maximum number of particules including the virtual particle

         flst_realres(1,flst_nreal) = 0  ! 2 ! flavour structure
         flst_realres(2,flst_nreal) = 0 ! 2
         flst_realres(3,flst_nreal) = 0 ! lepflav(1)
         flst_realres(4,flst_nreal) = 0 ! lepflav(1)
         flst_realres(5,flst_nreal) = 3  ! lepflav(1)
         flst_realres(6,flst_nreal) = 3  ! 12
         flst_realres(7,flst_nreal) = 4  ! lepflav(3)
         flst_realres(8,flst_nreal) = 4  ! 14
         flst_realres(9,flst_nreal) = 0  ! 1
         flst_realres(10,flst_nreal) = 0  ! 1
         flst_realres(11,flst_nreal) = 0 ! 22

         flst_nreal=flst_nreal+1
         flst_real(1,flst_nreal) = i1     ! flavour structure
         flst_real(2,flst_nreal) = i2
         flst_real(3,flst_nreal) = 24*isign
         flst_real(4,flst_nreal) = 24*isign
         flst_real(5,flst_nreal) = lepflav(1)
         flst_real(6,flst_nreal) = lepflav(2)
         flst_real(7,flst_nreal) = lepflav(3)
         flst_real(8,flst_nreal) = lepflav(4)
         flst_real(9,flst_nreal) = f1
         flst_real(10,flst_nreal) = f2
         flst_real(11,flst_nreal) = 22
         
         flst_reallength(flst_nreal) = 11 ! maximum number of particules including the virtual particle

         flst_realres(1,flst_nreal) = 0  ! 2 ! flavour structure
         flst_realres(2,flst_nreal) = 0 ! 2
         flst_realres(3,flst_nreal) = 0 ! lepflav(1)
         flst_realres(4,flst_nreal) = 0 ! lepflav(1)
         flst_realres(5,flst_nreal) = 3  ! lepflav(1)
         flst_realres(6,flst_nreal) = 3  ! 12
         flst_realres(7,flst_nreal) = 4  ! lepflav(3)
         flst_realres(8,flst_nreal) = 4  ! 14
         flst_realres(9,flst_nreal) = 0  ! 1
         flst_realres(10,flst_nreal) = 0  ! 1
         flst_realres(11,flst_nreal) = 3 ! 22

         flst_nreal=flst_nreal+1
         flst_real(1,flst_nreal) = i1     ! flavour structure
         flst_real(2,flst_nreal) = i2
         flst_real(3,flst_nreal) = 24*isign
         flst_real(4,flst_nreal) = 24*isign
         flst_real(5,flst_nreal) = lepflav(1)
         flst_real(6,flst_nreal) = lepflav(2)
         flst_real(7,flst_nreal) = lepflav(3)
         flst_real(8,flst_nreal) = lepflav(4)
         flst_real(9,flst_nreal) = f1
         flst_real(10,flst_nreal) = f2
         flst_real(11,flst_nreal) = 22
         
         flst_reallength(flst_nreal) = 11 ! maximum number of particules including the virtual particle

         flst_realres(1,flst_nreal) = 0  ! 2 ! flavour structure
         flst_realres(2,flst_nreal) = 0 ! 2
         flst_realres(3,flst_nreal) = 0 ! lepflav(1)
         flst_realres(4,flst_nreal) = 0 ! lepflav(1)
         flst_realres(5,flst_nreal) = 3  ! lepflav(1)
         flst_realres(6,flst_nreal) = 3  ! 12
         flst_realres(7,flst_nreal) = 4  ! lepflav(3)
         flst_realres(8,flst_nreal) = 4  ! 14
         flst_realres(9,flst_nreal) = 0  ! 1
         flst_realres(10,flst_nreal) = 0  ! 1
         flst_realres(11,flst_nreal) = 4  ! 22

      end

! ------------------------------------------------------

      subroutine s_channel_richer_resonance(xi1,xi2,xf1,xf2)
      implicit none 
      integer i1, i2, f1, f2
      integer xi1, xi2, xf1, xf2
      include 'nlegborn.h'
      include 'pwhg_flst.h'      
      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)


      i1=isign*xi1
      i2=isign*xi2
      f1=isign*xf1
      f2=isign*xf2

      
! i1 i2 -> e+ nu_e mu+ nu_mu f1 f2

!1    ####################### Higgs exchange
      flst_nborn=flst_nborn+1   

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 25
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 6 
      flst_bornres(11,flst_nborn) = 6  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7


      flst_bornresgroup(flst_nborn)=2
      
! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5  
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

!2    ####################### Higgs exchange (exchange of the lepton lines)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 25
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2


      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 6
      flst_bornres(9,flst_nborn) = 6
      flst_bornres(10,flst_nborn) = 4 
      flst_bornres(11,flst_nborn) = 4  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7


      flst_bornresgroup(flst_nborn)=3
      
! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0
      
!3    #######################       Z exchange 
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 6 
      flst_bornres(11,flst_nborn) = 6  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7


      flst_bornresgroup(flst_nborn)=4
      
! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

!4    #######################       Z exchange (exchange of the lepton lines)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 6
      flst_bornres(9,flst_nborn) = 6
      flst_bornres(10,flst_nborn) = 4 
      flst_bornres(11,flst_nborn) = 4  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

      flst_bornresgroup(flst_nborn)=5
      
! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

      
      end
      
c####################################################

      subroutine s_channel_all_resonance(xi1,xi2,xf1,xf2)
      implicit none 
      integer i1, i2, f1, f2
      integer xi1, xi2, xf1, xf2
      include 'nlegborn.h'
      include 'pwhg_flst.h'      

      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)
      

      i1=isign*xi1
      i2=isign*xi2
      f1=isign*xf1
      f2=isign*xf2

! i1 i2 -> e+ nu_e mu+ nu_mu f1 f2

!1    ####################### Higgs exchange
      flst_nborn=flst_nborn+1   

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 25
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 6 
      flst_bornres(11,flst_nborn) = 6  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5  
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

!2    ####################### Higgs exchange (exchange of the lepton lines)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 25
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2


      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 6
      flst_bornres(9,flst_nborn) = 6
      flst_bornres(10,flst_nborn) = 4 
      flst_bornres(11,flst_nborn) = 4  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0
      
!3    #######################       Z exchange 
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 6 
      flst_bornres(11,flst_nborn) = 6  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

!4    #######################       Z exchange (exchange of the lepton lines)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 6
      flst_bornres(9,flst_nborn) = 6
      flst_bornres(10,flst_nborn) = 4 
      flst_bornres(11,flst_nborn) = 4  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 4 
      flst_realres(11,flst_nreal) = 4  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

!5    #######################       Z exchange but from the fermion line (different fermion line)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 23
      flst_born(5,flst_nborn) = 24*isign
      flst_born(6,flst_nborn) = -24*isign
      flst_born(7,flst_nborn) = lepflav(1)
      flst_born(8,flst_nborn) = lepflav(2)
      flst_born(9,flst_nborn) = lepflav(3)
      flst_born(10,flst_nborn) = lepflav(4)
      flst_born(11,flst_nborn) = f1
      flst_born(12,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 12
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 4  
      flst_bornres(6,flst_nborn) = 4 
      flst_bornres(7,flst_nborn) = 3
      flst_bornres(8,flst_nborn) = 3
      flst_bornres(9,flst_nborn) = 5 
      flst_bornres(10,flst_nborn) = 5  
      flst_bornres(11,flst_nborn) = 6 
      flst_bornres(12,flst_nborn) = 6

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 5 
      flst_realres(10,flst_nreal) = 5  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 3

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 5 
      flst_realres(10,flst_nreal) = 5  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 5 
      flst_realres(10,flst_nreal) = 5  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 6

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 5 
      flst_realres(10,flst_nreal) = 5  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 0
      
!6    #######################       Z exchange but from the fermion line (different fermion line)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 23
      flst_born(5,flst_nborn) = 24*isign
      flst_born(6,flst_nborn) = -24*isign
      flst_born(7,flst_nborn) = lepflav(1)
      flst_born(8,flst_nborn) = lepflav(2)
      flst_born(9,flst_nborn) = lepflav(3)
      flst_born(10,flst_nborn) = lepflav(4)
      flst_born(11,flst_nborn) = f1
      flst_born(12,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 12
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 4  
      flst_bornres(6,flst_nborn) = 4 
      flst_bornres(7,flst_nborn) = 5
      flst_bornres(8,flst_nborn) = 5
      flst_bornres(9,flst_nborn) = 3 
      flst_bornres(10,flst_nborn) = 3  
      flst_bornres(11,flst_nborn) = 6 
      flst_bornres(12,flst_nborn) = 6

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 3 
      flst_realres(10,flst_nreal) = 3  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 3

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 3 
      flst_realres(10,flst_nreal) = 3  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 3 
      flst_realres(10,flst_nreal) = 3  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 6

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = -24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4  
      flst_realres(6,flst_nreal) = 4 
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 3 
      flst_realres(10,flst_nreal) = 3  
      flst_realres(11,flst_nreal) = 6 
      flst_realres(12,flst_nreal) = 6
      flst_realres(13,flst_nreal) = 0
      
!7    #######################       Z exchange from the W in decay chain

      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = lepflav(1)
      flst_born(8,flst_nborn) = lepflav(2)
      flst_born(9,flst_nborn) = lepflav(3)
      flst_born(10,flst_nborn) = lepflav(4)
      flst_born(11,flst_nborn) = f1
      flst_born(12,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 12
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3  
      flst_bornres(6,flst_nborn) = 5 
      flst_bornres(7,flst_nborn) = 4
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 6
      flst_bornres(10,flst_nborn) = 6  
      flst_bornres(11,flst_nborn) = 5
      flst_bornres(12,flst_nborn) = 5

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 6  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 6  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 6  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 6
      flst_realres(10,flst_nreal) = 6  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 0
      
!8    #######################       Z exchange from the W in decay chain (different fermion line)
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = lepflav(1)
      flst_born(8,flst_nborn) = lepflav(2)
      flst_born(9,flst_nborn) = lepflav(3)
      flst_born(10,flst_nborn) = lepflav(4)
      flst_born(11,flst_nborn) = f1
      flst_born(12,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 12
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3  
      flst_bornres(6,flst_nborn) = 5 
      flst_bornres(7,flst_nborn) = 6
      flst_bornres(8,flst_nborn) = 6
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 4  
      flst_bornres(11,flst_nborn) = 5
      flst_bornres(12,flst_nborn) = 5

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 6
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 4  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 6
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 4  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 6
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 4  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = lepflav(1)
      flst_real(8,flst_nreal) = lepflav(2)
      flst_real(9,flst_nreal) = lepflav(3)
      flst_real(10,flst_nreal) = lepflav(4)
      flst_real(11,flst_nreal) = f1
      flst_real(12,flst_nreal) = f2
      flst_real(13,flst_nreal) = 22

      flst_reallength(flst_nreal) = 13
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3  
      flst_realres(6,flst_nreal) = 5 
      flst_realres(7,flst_nreal) = 6
      flst_realres(8,flst_nreal) = 6
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 4  
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      flst_realres(13,flst_nreal) = 0
      
!9    #######################       Decay chain

      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 23
      flst_born(5,flst_nborn) = 24*isign
      flst_born(6,flst_nborn) = lepflav(1)
      flst_born(7,flst_nborn) = lepflav(2)
      flst_born(8,flst_nborn) = lepflav(3)
      flst_born(9,flst_nborn) = lepflav(4)
      flst_born(10,flst_nborn) = f1
      flst_born(11,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 11
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 4 
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5
      flst_bornres(8,flst_nborn) = 3
      flst_bornres(9,flst_nborn) = 3  
      flst_bornres(10,flst_nborn) = 4
      flst_bornres(11,flst_nborn) = 4

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 3

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 0
      
!10    #######################       Decay chain (exchange lepton lines)

      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 23
      flst_born(5,flst_nborn) = 24*isign
      flst_born(6,flst_nborn) = lepflav(1)
      flst_born(7,flst_nborn) = lepflav(2)
      flst_born(8,flst_nborn) = lepflav(3)
      flst_born(9,flst_nborn) = lepflav(4)
      flst_born(10,flst_nborn) = f1
      flst_born(11,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 11
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 4 
      flst_bornres(6,flst_nborn) = 3
      flst_bornres(7,flst_nborn) = 3
      flst_bornres(8,flst_nborn) = 5
      flst_bornres(9,flst_nborn) = 5  
      flst_bornres(10,flst_nborn) = 4
      flst_bornres(11,flst_nborn) = 4

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 5
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 5  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 3

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 5  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = 24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 5
      flst_realres(9,flst_nreal) = 5  
      flst_realres(10,flst_nreal) = 4
      flst_realres(11,flst_nreal) = 4
      flst_realres(12,flst_nreal) = 0

!11   #######################       Decay chain

      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 23
      flst_born(5,flst_nborn) = -24*isign
      flst_born(6,flst_nborn) = lepflav(1)
      flst_born(7,flst_nborn) = lepflav(2)
      flst_born(8,flst_nborn) = lepflav(3)
      flst_born(9,flst_nborn) = lepflav(4)
      flst_born(10,flst_nborn) = f1
      flst_born(11,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 11
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 4 
      flst_bornres(6,flst_nborn) = 4
      flst_bornres(7,flst_nborn) = 4
      flst_bornres(8,flst_nborn) = 3
      flst_bornres(9,flst_nborn) = 3  
      flst_bornres(10,flst_nborn) = 5
      flst_bornres(11,flst_nborn) = 5

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 4
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 4
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 3

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 4
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 4
      flst_realres(7,flst_nreal) = 4
      flst_realres(8,flst_nreal) = 3
      flst_realres(9,flst_nreal) = 3  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 0
      
!12    #######################       Decay chain (exchange lepton lines)

      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 23
      flst_born(5,flst_nborn) = -24*isign
      flst_born(6,flst_nborn) = lepflav(1)
      flst_born(7,flst_nborn) = lepflav(2)
      flst_born(8,flst_nborn) = lepflav(3)
      flst_born(9,flst_nborn) = lepflav(4)
      flst_born(10,flst_nborn) = f1
      flst_born(11,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 11
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 4 
      flst_bornres(6,flst_nborn) = 3
      flst_bornres(7,flst_nborn) = 3
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4  
      flst_bornres(10,flst_nborn) = 5
      flst_bornres(11,flst_nborn) = 5

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4 
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 3

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4 
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 23
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 4 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4 
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 0


      
!13    #######################       Tri-boson

      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = -24*isign
      flst_born(6,flst_nborn) = lepflav(1)
      flst_born(7,flst_nborn) = lepflav(2)
      flst_born(8,flst_nborn) = lepflav(3)
      flst_born(9,flst_nborn) = lepflav(4)
      flst_born(10,flst_nborn) = f1
      flst_born(11,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 11
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 0
      flst_bornres(5,flst_nborn) = 0 
      flst_bornres(6,flst_nborn) = 3
      flst_bornres(7,flst_nborn) = 3
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4 
      flst_bornres(10,flst_nborn) = 5
      flst_bornres(11,flst_nborn) = 5

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 0
      flst_realres(5,flst_nreal) = 0 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 3
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 0
      flst_realres(5,flst_nreal) = 0 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 4
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 0
      flst_realres(5,flst_nreal) = 0 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 5
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = -24*isign
      flst_real(6,flst_nreal) = lepflav(1)
      flst_real(7,flst_nreal) = lepflav(2)
      flst_real(8,flst_nreal) = lepflav(3)
      flst_real(9,flst_nreal) = lepflav(4)
      flst_real(10,flst_nreal) = f1
      flst_real(11,flst_nreal) = f2
      flst_real(12,flst_nreal) = 22

      flst_reallength(flst_nreal) = 12
      
      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 0
      flst_realres(5,flst_nreal) = 0 
      flst_realres(6,flst_nreal) = 3
      flst_realres(7,flst_nreal) = 3
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4  
      flst_realres(10,flst_nreal) = 5
      flst_realres(11,flst_nreal) = 5
      flst_realres(12,flst_nreal) = 0
      
      end      
      
c####################################################

      subroutine s_channel_one_resonance(xi1,xi2,xf1,xf2)
      implicit none 
      integer i1, i2, f1, f2
      integer xi1, xi2, xf1, xf2
      include 'nlegborn.h'
      include 'pwhg_flst.h'      

      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)
      

      i1=isign*xi1
      i2=isign*xi2
      f1=isign*xf1
      f2=isign*xf2

! i1 i2 -> e+ nu_e mu+ nu_mu f1 f2

!1    ####################### Higgs exchange
      flst_nborn=flst_nborn+1   

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 25
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 6 
      flst_bornres(11,flst_nborn) = 6  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5  
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 25
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0


      
!3    #######################       Z exchange 
      flst_nborn=flst_nborn+1      

      flst_born(1,flst_nborn) = i1
      flst_born(2,flst_nborn) = i2
      flst_born(3,flst_nborn) = 24*isign
      flst_born(4,flst_nborn) = 24*isign
      flst_born(5,flst_nborn) = 23
      flst_born(6,flst_nborn) = 24*isign
      flst_born(7,flst_nborn) = -24*isign
      flst_born(8,flst_nborn) = lepflav(1)
      flst_born(9,flst_nborn) = lepflav(2)
      flst_born(10,flst_nborn) = lepflav(3)
      flst_born(11,flst_nborn) = lepflav(4)
      flst_born(12,flst_nborn) = f1
      flst_born(13,flst_nborn) = f2

      flst_bornlength(flst_nborn) = 13
      
      flst_bornres(1,flst_nborn) = 0  ! flavour structure
      flst_bornres(2,flst_nborn) = 0
      flst_bornres(3,flst_nborn) = 0  
      flst_bornres(4,flst_nborn) = 3
      flst_bornres(5,flst_nborn) = 3
      flst_bornres(6,flst_nborn) = 5
      flst_bornres(7,flst_nborn) = 5 
      flst_bornres(8,flst_nborn) = 4
      flst_bornres(9,flst_nborn) = 4
      flst_bornres(10,flst_nborn) = 6 
      flst_bornres(11,flst_nborn) = 6  
      flst_bornres(12,flst_nborn) = 7 
      flst_bornres(13,flst_nborn) = 7

! ----real process * 3 ------
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 4

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 6
      
      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 7

      flst_nreal=flst_nreal+1
      
      flst_real(1,flst_nreal) = i1
      flst_real(2,flst_nreal) = i2
      flst_real(3,flst_nreal) = 24*isign
      flst_real(4,flst_nreal) = 24*isign
      flst_real(5,flst_nreal) = 23
      flst_real(6,flst_nreal) = 24*isign
      flst_real(7,flst_nreal) = -24*isign
      flst_real(8,flst_nreal) = lepflav(1)
      flst_real(9,flst_nreal) = lepflav(2)
      flst_real(10,flst_nreal) = lepflav(3)
      flst_real(11,flst_nreal) = lepflav(4)
      flst_real(12,flst_nreal) = f1
      flst_real(13,flst_nreal) = f2
      flst_real(14,flst_nreal) = 22
         
      flst_reallength(flst_nreal) = 14

      flst_realres(1,flst_nreal) = 0  ! flavour structure
      flst_realres(2,flst_nreal) = 0
      flst_realres(3,flst_nreal) = 0  
      flst_realres(4,flst_nreal) = 3
      flst_realres(5,flst_nreal) = 3
      flst_realres(6,flst_nreal) = 5
      flst_realres(7,flst_nreal) = 5 
      flst_realres(8,flst_nreal) = 4
      flst_realres(9,flst_nreal) = 4
      flst_realres(10,flst_nreal) = 6 
      flst_realres(11,flst_nreal) = 6  
      flst_realres(12,flst_nreal) = 7 
      flst_realres(13,flst_nreal) = 7
      flst_realres(14,flst_nreal) = 0

      
      end
