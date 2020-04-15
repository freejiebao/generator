      subroutine setborn(p,bflav,born,bornjk,bmunu)
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer nlegs
ccc-mauro-mod
      parameter (nlegs=nlegbornexternal)
c      parameter (nlegs=flst_numfsb+2) is the meaninig of the line above
ccc-mauro-mod
      real * 8 p(0:3,nlegs),bornjk(nlegs,nlegs)
      integer bflav(nlegs)
      real * 8 bmunu(0:3,0:3,nlegs),bbmunu(0:3,0:3),born,colcf
      integer j,k,mu,nu
c Colour factors for colour-correlated Born amplitudes;
c Rule from 2.98 in FNO2007, leads to B_ij=Cj * B,
c where i#j

      call compborn(p,bflav,born,bbmunu)

c      write(*,*) "Born", born      

      if(born /= born) then
         write(*,*) "This matrix element is NaN ", born
         write(*,*) "The momenta is ", p, bflav, bbmunu
         stop
      endif


      colcf = 0d0
      bmunu = 0
      bornjk = 0
      do j=1,nlegs
         if(abs(bflav(j)).le.6) then
            if(bflav(j).eq.0) then
               do mu=0,3
                  do nu=0,3
                     bmunu(mu,nu,j)=bbmunu(mu,nu)
                  enddo
               enddo
            endif
            do k=j+1,nlegs
               if(abs(bflav(k)).le.6) then
                  colcf=cf
               endif
               bornjk(j,k)=born*colcf/3d0 ! factor 3 is added by hand in order to avoid warning in the checking of the coll./sof limit.
               ! The QCD is here irrelevant as it is not computed.
               bornjk(k,j)=bornjk(j,k)
            enddo
         endif
      enddo
      end


c     Example
c     q q'-> e+ ve~
      subroutine compborn(p,bflav,born,bmunu)
      use recola
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'PhysPars.h'
      integer nleg
ccc-mauro-mod
      parameter (nleg=8) 
ccc-mauro-mod
      real * 8 p(0:3,nleg)
      real * 8 ptemp(0:3,nleg), pin(0:3,nleg)
      integer bflav(nleg)
      real * 8 born,bmunu(0:3,0:3)
      integer i,mu,nu
      real*8 virtasbornvar
      common/cvirtasbornvar/virtasbornvar
      integer mbornflav(20,1:4)
      save mbornflav
      integer ini
      data ini/0/
      save ini
      integer i_flav, i_master, i_cross
      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)


      
      if(ini.eq.0) then
      
         mbornflav(1,:)  = (/-3,-3,-4,-4/)
         mbornflav(2,:)  = (/-3,-1,-4,-2/)
         mbornflav(3,:)  = (/-3,2,-4,1/)
         mbornflav(4,:)  = (/-3,4,-4,3/)
         mbornflav(5,:)  = (/-1,-3,-2,-4/)
         mbornflav(6,:)  = (/-1,-1,-2,-2/)
         mbornflav(7,:)  = (/-1,2,-2,1/)
         mbornflav(8,:)  = (/-1,4,-2,3/)
         mbornflav(9,:)  = (/2,-3,1,-4/)
         mbornflav(10,:) = (/2,-1,1,-2/)
         mbornflav(11,:) = (/2,2,1,1/)
         mbornflav(12,:) = (/2,4,1,3/)
         mbornflav(13,:) = (/4,-3,3,-4/)
         mbornflav(14,:) = (/4,-1,3,-2/)
         mbornflav(15,:) = (/4,2,3,1/)
         mbornflav(16,:) = (/4,4,3,3/)
         mbornflav(17,:) = (/2,-1,-4,3/)
         mbornflav(18,:) = (/-1,2,-4,3/)
         mbornflav(19,:) = (/4,-3,-2,1/)
         mbornflav(20,:) = (/-3,4,-2,1/)

         mbornflav=isign*mbornflav
         
         ini=1
      endif

      pin = p                   ! change of variable
      
      do i =1,20
         if((bflav(1)==mbornflav(i,1)) .and. (bflav(2)==mbornflav(i,2)) .and.
     &        (bflav(7)==mbornflav(i,3))
     &        .and. (bflav(8)==mbornflav(i,4))) then
            
!     write(*,*) "i", i
            
! This is to merge different channels and hence use less memory in Recola     
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
            
! This is using the crossing of the initial state.
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
               write(*,*) "Born: There is a problem, one channel is not implemented"
               stop
            endif
            
!  "

            
            call compute_process_rcl(i_master,pin,'LO')
            call get_squared_amplitude_rcl(i_master,0,'LO',born)
            
         endif
      enddo
      
      do mu=0,3
         do nu=0,3
            bmunu(mu,nu)=0d0
         enddo
      enddo

      end

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

      subroutine borncolour_lh
c Sets up the colour for the given flavour configuration
c already filled in the Les Houches interface.
c In case there are several colour structure, one
c should pick one with a probability proportional to
c the value of the corresponding cross section, for the
c kinematics defined in the Les Houches interface
      include 'LesHouches.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      real*8 r ! random number
      real*8 random
      external random
c.....mauro-fix-b
      integer i1,nr,q(2),nq
      integer cc1(2),cc2(2)
      logical tchannel_diagCKMallowd
c.....mauro-fix-e
      
      icolup = 0

      if(nup .eq. 10) then      ! This corresponds to t/u or t channels: 2 initial state + 6 final states + 2 resonances
         
         
         if(idup(1).gt.0) then
            icolup(1,1)=501
            icolup(2,1)=0
         else
            icolup(1,1)=0
            icolup(2,1)=501
         endif
         
         if(idup(2).gt.0) then
            icolup(1,2)=502
            icolup(2,2)=0
         else
            icolup(1,2)=0
            icolup(2,2)=502
         endif
         
         if(idup(1) .eq. idup(2)) then ! This corresponds to a t/u channel.
            r=random()
            if(r < 0.5d0) then
               do i=1,2
                  icolup(i,9)=icolup(i,1)
                  icolup(i,10)=icolup(i,2)
               enddo
            else
               do i=1,2
                  icolup(i,9)=icolup(i,2)
                  icolup(i,10)=icolup(i,1)
               enddo
            endif
         else                   ! This is a t channel
c.....mauro-fix-b
            nr=0
            do i1=1,nup
               if(abs(idup(i1)).gt.22) nr=nr+1
            enddo
            if(nr.ne.2) then
               write(*,*)'error in color fixing'
               stop
            endif
            
            q=-1
            nq=0
            do i=3,nup
               if(abs(idup(i)).lt.6) then
                  nq=nq+1
                  q(nq)=i
               endif
            enddo
            if(nq.ne.2) then
               write(*,*)'error in corretcolour',nq
            endif
            
            cc1(:)=icolup(:,1)
            cc2(:)=icolup(:,2)
            
            nq=0
            if(tchannel_diagCKMallowd(idup(1),idup(q(1)))) then
               if(.not.tchannel_diagCKMallowd(idup(2),idup(q(2)))) then
                  write(*,*)'not 2 ws,stop'
                  stop
               endif
               nq=1
               icolup(:,q(1))=cc1(:)
               icolup(:,q(2))=cc2(:)
            endif
            
            if(tchannel_diagCKMallowd(idup(1),idup(q(2)))) then
               if(.not.tchannel_diagCKMallowd(idup(2),idup(q(1)))) then
                  write(*,*)'not 2 ws,stop'
                  stop
               endif
               nq=0
               icolup(:,q(2))=cc1(:)
               icolup(:,q(1))=cc2(:)
            endif
            
            if(nq.ne.1) then
               write(*,*)'color not reassigned'
               stop
            endif
c.....mauro-fix-e           
         endif
      elseif(nup .gt. 10) then
         
         if(idup(1).gt.0) then
            icolup(1,1)=501
            icolup(2,1)=0
            icolup(1,2)=0
            icolup(2,2)=501
         else
            icolup(1,1)=0
            icolup(2,1)=501
            icolup(1,2)=501
            icolup(2,2)=0
         endif
         
         if(idup(nup-1).gt.0) then
            icolup(1,nup-1)=502
            icolup(2,nup-1)=0
            icolup(1,nup)=0
            icolup(2,nup)=502
         else
            icolup(1,nup-1)=0
            icolup(2,nup-1)=502
            icolup(1,nup)=502
            icolup(2,nup)=0
         endif
      endif
      
      end


      subroutine finalize_lh
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'LesHouches.h'
c     Set up the resonances whose mass must be preserved
c     on the Les Houches interface.
c     
c     vector boson id and decay

      real * 8 powheginput
      external powheginput
      integer idvecbos,vdecaymode,isign,lepflav
      common/cvecbos/idvecbos,vdecaymode,isign,lepflav(4)



      call lhefinitemasses

      end
c.....mauro-fix-b
      function tchannel_diagCKMallowd(i1,i2)
      implicit none
      integer i1,i2
      logical tchannel_diagCKMallowd
      tchannel_diagCKMallowd=.false.
      if(i1.eq.1.and.i2.eq.2) tchannel_diagCKMallowd=.true.
      if(i1.eq.2.and.i2.eq.1) tchannel_diagCKMallowd=.true.
      if(i1.eq.3.and.i2.eq.4) tchannel_diagCKMallowd=.true.
      if(i1.eq.4.and.i2.eq.3) tchannel_diagCKMallowd=.true.

      if(i1.eq.-1.and.i2.eq.-2) tchannel_diagCKMallowd=.true.
      if(i1.eq.-2.and.i2.eq.-1) tchannel_diagCKMallowd=.true.
      if(i1.eq.-3.and.i2.eq.-4) tchannel_diagCKMallowd=.true.
      if(i1.eq.-4.and.i2.eq.-3) tchannel_diagCKMallowd=.true.
      
      end

c.....mauro-fix-e      
