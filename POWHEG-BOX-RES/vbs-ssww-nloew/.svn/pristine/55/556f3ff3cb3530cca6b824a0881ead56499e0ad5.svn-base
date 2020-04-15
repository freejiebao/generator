      subroutine analysis_driver(dsig0,ikin)
      implicit none
      real * 8 dsig0
      integer ikin
      integer jpart,mu
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'hepevt.h'
      integer iborn,ireg
      real * 8 powheginput

      real*8  test_kine
      common/ctest_kine/test_kine
      save /ctest_kine/

      integer ini
      data ini/0/
      save ini

      if(ini.eq.0) then
         test_kine=powheginput("#test-kine")
         ini=1
      endif

      if(.not.flg_nlotest) return

!      write(*,*)'driver',ikin
      
      if(ikin.eq.0) then
         nhep=flst_ibornlength
         do jpart=1,nhep
            do mu=1,3
               phep(mu,jpart)=kn_pborn(mu,jpart)
            enddo
            phep(4,jpart)=kn_pborn(0,jpart)
            phep(5,jpart)=sqrt(abs(phep(4,jpart)**2-
     #           phep(1,jpart)**2-phep(2,jpart)**2-phep(3,jpart)**2))
            if(jpart.le.2) then
               isthep(jpart)=-1
            else
               isthep(jpart)=1
            endif
         enddo
      else
c real or regular
         nhep=flst_ireallength
         do jpart=1,nhep
            do mu=1,3
               phep(mu,jpart)=kn_preal(mu,jpart)
            enddo
            phep(4,jpart)=kn_preal(0,jpart)
            phep(5,jpart)=sqrt(abs(phep(4,jpart)**2-
     #           phep(1,jpart)**2-phep(2,jpart)**2-phep(3,jpart)**2))
            if(jpart.le.2) then
               isthep(jpart)=-1
            else
               isthep(jpart)=1
            endif
         enddo
c mauro togli
         if(test_kine.gt.0d0) then

            nhep=flst_ibornlength
            do jpart=1,nhep
               do mu=1,3
                  phep(mu,jpart)=kn_pborn(mu,jpart)
               enddo
               phep(4,jpart)=kn_pborn(0,jpart)
               phep(5,jpart)=sqrt(abs(phep(4,jpart)**2-
     #phep(1,jpart)**2-phep(2,jpart)**2-phep(3,jpart)**2))
               if(jpart.le.2) then
                  isthep(jpart)=-1
               else
                  isthep(jpart)=1
               endif
            enddo
         endif
c mauro togli         
      endif

      if(ikin.ne.2) then
c Born or real
         do iborn=1,flst_nborn
            if(flst_bornresgroup(iborn).eq.flst_ibornresgroup) then
               exit
            endif
         enddo
         do jpart=1,flst_ibornlength
            if(flst_bornres(jpart,iborn).gt.0) then
               isthep(flst_bornres(jpart,iborn)) = 3
               jmohep(:,jpart) = flst_bornres(jpart,iborn)
            endif
            idhep(jpart) = flst_born(jpart,iborn)            
         enddo
         if(ikin.eq.1.and.test_kine.le.0d0) then
            if(kn_emitter.gt.0) then
               jmohep(:,flst_ireallength) = flst_bornres(kn_emitter,iborn)
            else
               jmohep(1,flst_ireallength) = 1
               jmohep(2,flst_ireallength) = 2
            endif
            idhep(flst_ireallength) = 22 !0 mauro
         endif
!         write(*,*)'flst_born(jpart,iborn)',flst_born(:,iborn)
!         write(*,*)'flst_born(jpart,iborn)',idhep(flst_ireallength)
!         write(*,*)'flst_ibornlenght,ral',flst_ibornlength,flst_ireallength
         
      else
c Regular
         do ireg = 1,flst_nregular
            if(flst_regularresgroup(ireg).eq.flst_iregularresgroup) then
               exit
            endif
         enddo
         do jpart=1,nhep
            if(flst_regularres(jpart,ireg).gt.0) then
               isthep(flst_regularres(jpart,ireg)) = 3
               jmohep(:,jpart) = flst_regularres(jpart,ireg)
            endif
            idhep(jpart) = flst_regular(jpart,ireg)
         enddo

!         write(*,*)'flst_regular(jpart,ireg)',flst_regular(1:nhep,ireg)
      
         write(*,*)"we don't have regulars"
         stop
   
      endif

      
      
c     call analysis routine
      call analysis(dsig0)

      end



     
      subroutine lhtohep
      implicit none
      include 'hepevt.h'
      include 'LesHouches.h'
      integer j
      nhep=nup
      do j=1,nup
         idhep(j)=idup(j)
         isthep(j)=istup(j)
         phep(:,j)=pup(:,j)
         jmohep(:,j)=mothup(:,j)
      enddo
      end

