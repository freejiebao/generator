c     returns 2 Re(M_B * M_V)/(as/(2pi)), 
c     where M_B is the Born amplitude and 
c     M_V is the finite part of the virtual amplitude
c     The as/(2pi) factor is attached at a later point
      subroutine setvirtual(px,vflavx,virtual)
      use recola
      implicit none
      include 'nlegborn.h'
      include 'pwhg_st.h'
      include 'pwhg_flg.h'
!      include 'mathx.h'
      include 'pwhg_math.h'
!      include 'pwhg_physpar.h'
      real * 8 px(0:3,nlegborn), pin(0:3,8)
      integer vflavx(nlegborn)
!      real * 8 p(0:3,nlegborn-1)
!      integer vflav(nlegborn-1)
      real * 8 p(0:3,8)
      integer vflav(8)
c      real * 8 p(0:3,flst_numfsb+2)!meaning of the line above
c      integer vflav(flst_numfsb+2)!meaning of the line above
ccc-mauro-mod
      real * 8 virtual, virt
      real *8 dotp
      integer i_flav, i_master, i_cross, i
      integer mvirtflav(20,1:4)
      save mvirtflav
      integer ini
      data ini/0/
      save ini
      external dotp
      logical pwhg_isfinite
      external pwhg_isfinite

! Copied from the VBFNLO code to avoid computing the virtual in stage one.
      real *8 powheginput
      external powheginput 
      logical, save :: firsttime = .true. 

      real *8 fakevirt
      save fakevirt 

      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)

      integer i1

      

      
      virtual = 0d0
      
      
      if (firsttime) then
         fakevirt=powheginput("#fakevirt")
         if (fakevirt == 1) write(*,*) 'WARNING: Using fakevirt !'
         firsttime = .false.
      endif

C--

      p(0:3,1:8) = px(0:3,1:8)
      vflav(1:8) = vflavx(1:8)

      
      i_master = 0 ! Initialisation

      
      if(ini.eq.0) then
         mvirtflav(1,:)  = (/-3,-3,-4,-4/)
         mvirtflav(2,:)  = (/-3,-1,-4,-2/)
         mvirtflav(3,:)  = (/-3,2,-4,1/)
         mvirtflav(4,:)  = (/-3,4,-4,3/)
         mvirtflav(5,:)  = (/-1,-3,-2,-4/)
         mvirtflav(6,:)  = (/-1,-1,-2,-2/)
         mvirtflav(7,:)  = (/-1,2,-2,1/)
         mvirtflav(8,:)  = (/-1,4,-2,3/)
         mvirtflav(9,:)  = (/2,-3,1,-4/)
         mvirtflav(10,:) = (/2,-1,1,-2/)
         mvirtflav(11,:) = (/2,2,1,1/)
         mvirtflav(12,:) = (/2,4,1,3/)
         mvirtflav(13,:) = (/4,-3,3,-4/)
         mvirtflav(14,:) = (/4,-1,3,-2/)
         mvirtflav(15,:) = (/4,2,3,1/)
         mvirtflav(16,:) = (/4,4,3,3/)
         mvirtflav(17,:) = (/2,-1,-4,3/)
         mvirtflav(18,:) = (/-1,2,-4,3/)
         mvirtflav(19,:) = (/4,-3,-2,1/)
         mvirtflav(20,:) = (/-3,4,-2,1/)

         mvirtflav=isign*mvirtflav
         
         ini=1
      endif
      
      
      pin = p                   ! Change of variables
      
      do i =1,20
         
         
         if((vflav(1)==mvirtflav(i,1)) .and. (vflav(2)==mvirtflav(i,2)) .and.
     &        (vflav(7)==mvirtflav(i,3))
     &        .and. (vflav(8)==mvirtflav(i,4))) then
            
            
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
               write(*,*) "There is a problem, one channel is not implemented"
               stop             !"
            endif
         endif
      enddo
      
      if(fakevirt .le. 0d0) then
         
         if(flg_with_em) then
            call compute_process_rcl(i_master,pin,'NLO')
            call get_squared_amplitude_rcl(i_master,0,'NLO',virt)
         else
            virt = 0
         endif
         
      elseif(fakevirt == 1d0) then
            
         if(flg_with_em) then
            call compute_process_rcl(i_master,pin,'LO')
            call get_squared_amplitude_rcl(i_master,0,'LO',virt)
            virt = virt * 0.001d0 ! In order to account for the ""numerical" value of alpha.

c              write(*,*) "virt", virt, vflav
            
         else
!     virtual_ew = 0
            virt = 0
         endif
         
         
      else
         write(*,*) "There is a problem with the fakevirt flag"
         stop
      endif
         
      virtual = virt/(st_alpha/(2d0*pi))

      if(.not.pwhg_isfinite(virtual)) virtual=0.d0

c      write(*,*) "out", virt, st_alpha
!      stop

      end

*
