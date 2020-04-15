      subroutine setreal(p,fermion_flav,amp2)
      use recola
      implicit none
      include 'nlegborn.h'
      include 'pwhg_math.h'
      include 'pwhg_st.h'
cc-mnauro-mod
      include 'pwhg_flst.h'
c*
!      real * 8 p(0:3,nlegreal-1)
!      integer fermion_flav(nlegreal-1)
      real * 8 p(0:3,9), ptemp(0:3,9), pin(0:3,9)
      integer fermion_flav(9)
c      real * 8 p(0:3,flst_numfsb+3) ! meaning of the line above
c      integer fermion_flav(flst_numfsb+3) ! meaning of the line above
ccc-mauro-mod
      logical pwhg_isfinite
      integer i_flav, i_master, i_cross, i,j
      integer mrealflav(20,1:5)
      save mrealflav
      integer ini
      data ini/0/
      save ini
      external pwhg_isfinite
      real * 8 amp2, realm
ccc-mauro-mod
      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)

      integer i1


      
         
      if(ini.eq.0) then
         mrealflav(1,:)  = (/-3,-3,-4,-4,22/)
         mrealflav(2,:)  = (/-3,-1,-4,-2,22/)
         mrealflav(3,:)  = (/-3,2,-4,1,22/)
         mrealflav(4,:)  = (/-3,4,-4,3,22/)
         mrealflav(5,:)  = (/-1,-3,-2,-4,22/)
         mrealflav(6,:)  = (/-1,-1,-2,-2,22/)
         mrealflav(7,:)  = (/-1,2,-2,1,22/)
         mrealflav(8,:)  = (/-1,4,-2,3,22/)
         mrealflav(9,:)  = (/2,-3,1,-4,22/)
         mrealflav(10,:) = (/2,-1,1,-2,22/)
         mrealflav(11,:) = (/2,2,1,1,22/)
         mrealflav(12,:) = (/2,4,1,3,22/)
         mrealflav(13,:) = (/4,-3,3,-4,22/)
         mrealflav(14,:) = (/4,-1,3,-2,22/)
         mrealflav(15,:) = (/4,2,3,1,22/)
         mrealflav(16,:) = (/4,4,3,3,22/)
         mrealflav(17,:) = (/2,-1,-4,3,22/)
         mrealflav(18,:) = (/-1,2,-4,3,22/)
         mrealflav(19,:) = (/4,-3,-2,1,22/)
         mrealflav(20,:) = (/-3,4,-2,1,22/)
         ini=1

         do i=1,20
            do j=1,4
               mrealflav(i,j)=isign*mrealflav(i,j)
            enddo
         enddo
         
      endif
      
      pin = p
      
      if(fermion_flav(9).eq.22) then
         
         do i =1,20
            if((fermion_flav(1)==mrealflav(i,1)) .and. (fermion_flav(2)==mrealflav(i,2)) .and.
     &           (fermion_flav(7)==mrealflav(i,3)) .and. (fermion_flav(8)==mrealflav(i,4)) 
     &           .and. (fermion_flav(9)==mrealflav(i,5))) then
               
!     This is to merge different channels and hence use less memory in Recola     
               if(i == 16) then
                  i_flav = 11
               elseif (i == 1) then
                  i_flav = 6
               elseif (i == 13) then
                  i_flav = 10
               elseif (i == 4) then
                  i_flav = 7
               elseif (i == 8) then
                  i_flav = 3
               elseif (i == 14) then
                  i_flav = 9
               elseif (i == 19) then
                  i_flav = 17
               elseif (i == 20) then
                  i_flav = 18
               else
                  i_flav = i
               endif
               
!     write(*,*) "i_flav", i_flav
                  
!     This is using the crossing of the initial state.
               if(i_flav == 5) then
                  i_cross = 2
                  pin(:,1) = p(:,2)
                  pin(:,2) = p(:,1)
                  pin(:,7) = p(:,8)
                  pin(:,8) = p(:,7)
               elseif (i_flav == 9) then
                  i_cross = 3
                  pin(:,1) = p(:,2)
                  pin(:,2) = p(:,1)
                  pin(:,7) = p(:,8)
                  pin(:,8) = p(:,7)
               elseif (i_flav == 10) then
                  i_cross = 7
                  pin(:,1) = p(:,2)
                  pin(:,2) = p(:,1)
                  pin(:,7) = p(:,8)
                  pin(:,8) = p(:,7)
               elseif (i_flav == 15) then
                  i_cross = 12
                  pin(:,1) = p(:,2)
                  pin(:,2) = p(:,1)
                  pin(:,7) = p(:,8)
                  pin(:,8) = p(:,7)
               elseif (i_flav == 18) then
                  i_cross = 17
                  pin(:,1) = p(:,2)
                  pin(:,2) = p(:,1)
               else
                  i_cross = i_flav
               endif
               
!     write(*,*) "i_cross", i_cross
               
               if(i_cross == 2) then
                  i_master = 1
               elseif (i_cross == 3) then
                  i_master = 2
               elseif (i_cross == 6) then
                  i_master = 3
               elseif (i_cross == 7) then
                  i_master = 4
               elseif (i_cross == 11) then
                  i_master = 5
               elseif (i_cross == 12) then
                  i_master = 6
               elseif (i_cross == 17) then
                  i_master = 7
               else
                  write(*,*) "There is a problem,"
     x                 //" one channel is not implemented"
                  stop
               endif
               
            endif
         enddo
         
         
         call compute_process_rcl(i_master+7,pin,'LO') ! +7 is to account for the id number in Recola
         call get_squared_amplitude_rcl(i_master+7,0,'LO',realm) ! +7 is to account for the id number in Recola
         
      else
         write(*,*) "We do not compute QCD corrections here"
         stop
      endif


      amp2 = realm/(st_alpha/(2d0*pi))


      if(.not.pwhg_isfinite(amp2)) amp2=0.d0

      end

c
c-----
      subroutine regularcolour_lh
      write(*,*) 'regularcolour_lh: NOT YET IMPLEMENTED !'
      write(*,*) 'exiting ...'
      call exit(-1)
      end


