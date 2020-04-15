      subroutine buildjets(mjets,rr,pptmin,kt,eta,rap,phi,pjet)
c     arrays to reconstruct jets, radius parameter rr
      implicit none
      integer   maxtrack,maxjet
      parameter (maxtrack=2048,maxjet=2048)
      real * 8  ptrack(4,maxtrack),pj(4,maxjet)
      integer   jetvec(maxtrack),itrackhep(maxtrack)
      integer mjets
      real * 8  rr,pptmin,kt(maxjet),eta(maxjet),rap(maxjet),
     1     phi(maxjet),pjet(4,maxjet)
      include   'hepevt.h'
      include  'LesHouches.h'

      integer   ntracks,njets
      integer   j,k,mu,jb
      real * 8 r,ptmin,palg,pp,tmp
      logical xislepton,xisnu ,xisgamma
      external xislepton,xisnu,xisgamma
      logical istrack
c
      integer ini
      data ini/0/
      save ini
C - Initialize arrays and counters for output jets
      do j=1,maxtrack
         do mu=1,4
            ptrack(mu,j)=0d0
         enddo
         jetvec(j)=0
      enddo      
      ntracks=0
      do j=1,maxjet
         do mu=1,4
            pjet(mu,j)=0d0
            pj(mu,j)=0d0
         enddo
         kt(j)=-1d9
         eta(j)=-1d9
         rap(j)=-1d9
         phi(j)=-1d9
      enddo
c      print*, '--- NEW EVENT ---'

C     - Extract final state particles to feed to jet finder
c     first make sure we are not clustering leptons
      do j=1,nhep
         if(.not.xislepton(idhep(j)) .and. 
     C        .not.xisnu(idhep(j)).and.
     C        .not.xisgamma(idhep(j))) then
            
            istrack=.false.
            
c     to be tested
            if(isthep(j).eq.1) istrack=.true.

c            if(isthep(j).eq.1) then
c               write(*,*)'id tracks ',idhep(j),phep(1:4,j)
c            endif
            
c     if(isthep(j).gt.0) istrack=.true.
            
            if(istrack) then
               
               if(ntracks.eq.maxtrack) then
                  write(*,*) 'analyze: need to increase maxtrack!'
                  write(*,*) 'ntracks: ',ntracks
                  stop
               endif
               ntracks=ntracks+1
               ptrack(1:4,ntracks)=phep(1:4,j)
               itrackhep(ntracks)=j
            endif
         endif
      enddo
      
      if (ntracks.eq.0) then
         mjets=0
         return
      endif

c     palg=1 is standard kt, -1 is antikt
      palg=-1
      r=rr
      ptmin=pptmin

c      write(*,*)'pre',ntracks
c      do j=1,ntracks
c         write(*,*)ptrack(1:4,j)
c      enddo
      
      njets=0d0                 ! Just being very uberly safe ...
      pjet=0d0
c      call fastjetppgenkt(ptrack,ntracks,r,palg,ptmin,pjet,njets,
c     $                        jetvec)

c     prova
      
      call fastjetppgenkt(ptrack,ntracks,r,palg,pjet,njets)
      
      mjets=njets


c       write(*,*)'post',njets
c       do j=1,njets
c          write(*,*)pjet(1:4,j)
c       enddo

c      ini=ini+1
c      if(ini.eq.10) stop
      
c$$$      if(njets.eq.0) return
c$$$c check consistency
c$$$      do k=1,ntracks
c$$$         if(jetvec(k).gt.0) then
c$$$            do mu=1,4
c$$$               pj(mu,jetvec(k))=pj(mu,jetvec(k))+ptrack(mu,k)
c$$$            enddo
c$$$         endif
c$$$      enddo
c$$$      tmp=0
c$$$      do j=1,mjets
c$$$         do mu=1,4
c$$$            tmp=tmp+abs(pj(mu,j)-pjet(mu,j))
c$$$         enddo
c$$$      enddo
c$$$      if(tmp.gt.1d-4) then
c$$$         write(*,*) ' bug!'
c$$$      endif
C --------------------------------------------------------------------- C
C - Computing arrays of useful kinematics quantities for hardest jets - C
C --------------------------------------------------------------------- C
      do j=1,mjets
         kt(j)=sqrt(pjet(1,j)**2+pjet(2,j)**2)
         pp = sqrt(kt(j)**2+pjet(3,j)**2)
         eta(j)=0.5d0*log((pjet(4,j)+pjet(3,j))/(pjet(4,j)-pjet(3,j)))
         rap(j)=0.5d0*log((pjet(4,j)+pjet(3,j))/(pjet(4,j)-pjet(3,j)))
         phi(j)=atan2(pjet(2,j),pjet(1,j))

c         write(*,*)'XX',pjet(:,j),kt(j),eta(j)
         
      enddo
      end

      logical function xislepton(id)
      implicit none
      integer id
      xislepton=.false.
      if(abs(id).eq.11.or.abs(id).eq.13.or.abs(id).eq.15)then
         xislepton=.true.
      endif
      end 

      logical function xisnu(id)
      implicit none
      integer id
      xisnu=.false.
      if(abs(id).eq.12.or.abs(id).eq.14.or.abs(id).eq.16)then
         xisnu=.true.
      endif
      end 

      logical function xisgamma(id)
      implicit none
      integer id
      xisgamma=.false.
      if(abs(id).eq.22)then
         xisgamma=.true.
      endif
      end 

c---------------------------------added on 07.05

      subroutine buildjets_gamma(ngamma,gamma,pgamma,mjets,rr,pptmin,kt,eta,rap,phi,pjet)
c     arrays to reconstruct jets, radius parameter rr
      implicit none
      integer   maxtrack,maxjet
      parameter (maxtrack=2048,maxjet=2048)
      real * 8  ptrack(4,maxtrack),pj(4,maxjet)
      integer   jetvec(maxtrack),itrackhep(maxtrack)
      integer mjets
      real * 8  rr,pptmin,kt(maxjet),eta(maxjet),rap(maxjet),
     1     phi(maxjet),pjet(4,maxjet)
      include   'hepevt.h'
      include  'LesHouches.h'

      integer   ntracks,njets
      integer   j,k,mu,jb
      real * 8 r,ptmin,palg,pp,tmp
      logical xislepton,xisnu ,xisgamma
      external xislepton,xisnu,xisgamma
      logical istrack
c
      integer ini
      data ini/0/
      save ini

      integer ngamma
      real*8 pgamma(4,100)
      logical gamma(100)
      
C - Initialize arrays and counters for output jets
      do j=1,maxtrack
         do mu=1,4
            ptrack(mu,j)=0d0
         enddo
         jetvec(j)=0
      enddo      
      ntracks=0
      do j=1,maxjet
         do mu=1,4
            pjet(mu,j)=0d0
            pj(mu,j)=0d0
         enddo
         kt(j)=-1d9
         eta(j)=-1d9
         rap(j)=-1d9
         phi(j)=-1d9
      enddo

C     - Extract final state particles to feed to jet finder
c     first make sure we are not clustering leptons
      do j=1,nhep
         if(  .not.xislepton(idhep(j)) .and. 
     C        .not.xisnu(idhep(j)).and.
     C        .not.xisgamma(idhep(j))) then
            
            istrack=.false.
            
c     to be tested
            if(isthep(j).eq.1) istrack=.true.

c            if(isthep(j).eq.1) then
c               write(*,*)'id tracks ',idhep(j),phep(1:4,j)
c            endif
            
c     if(isthep(j).gt.0) istrack=.true.
            
            if(istrack) then
               
               if(ntracks.eq.maxtrack) then
                  write(*,*) 'analyze: need to increase maxtrack!'
                  write(*,*) 'ntracks: ',ntracks
                  stop
               endif
               ntracks=ntracks+1
               ptrack(1:4,ntracks)=phep(1:4,j)
               itrackhep(ntracks)=j
            endif
         endif
      enddo

! add to the tracks the photons that survived the lepton-gamma recomb

      do j=1,ngamma
         if(gamma(j)) then
            ntracks=ntracks+1
            if(ntracks.eq.maxtrack) then
               write(*,*) 'analyze: need to increase maxtrack!'
               write(*,*) 'ntracks: ',ntracks
               stop
            endif

            ptrack(1:4,ntracks)=pgamma(1:4,j)
            itrackhep(ntracks)=j
         endif
      enddo
      
      if (ntracks.eq.0) then
         mjets=0
         return
      endif

c     palg=1 is standard kt, -1 is antikt
      palg=-1
      r=rr
      ptmin=pptmin

c      write(*,*)'pre',ntracks
c      do j=1,ntracks
c         write(*,*)ptrack(1:4,j)
c      enddo
      
      njets=0d0                 ! Just being very uberly safe ...
      pjet=0d0
c      call fastjetppgenkt(ptrack,ntracks,r,palg,ptmin,pjet,njets,
c     $                        jetvec)

c prova
      call fastjetppgenkt(ptrack,ntracks,r,palg,pjet,njets)
      
      mjets=njets


c       write(*,*)'post',njets
c       do j=1,njets
c          write(*,*)pjet(1:4,j)
c       enddo

c      ini=ini+1
c      if(ini.eq.10) stop
      
c$$$      if(njets.eq.0) return
c$$$c check consistency
c$$$      do k=1,ntracks
c$$$         if(jetvec(k).gt.0) then
c$$$            do mu=1,4
c$$$               pj(mu,jetvec(k))=pj(mu,jetvec(k))+ptrack(mu,k)
c$$$            enddo
c$$$         endif
c$$$      enddo
c$$$      tmp=0
c$$$      do j=1,mjets
c$$$         do mu=1,4
c$$$            tmp=tmp+abs(pj(mu,j)-pjet(mu,j))
c$$$         enddo
c$$$      enddo
c$$$      if(tmp.gt.1d-4) then
c$$$         write(*,*) ' bug!'
c$$$      endif
C --------------------------------------------------------------------- C
C - Computing arrays of useful kinematics quantities for hardest jets - C
C --------------------------------------------------------------------- C
      do j=1,mjets
         kt(j)=sqrt(pjet(1,j)**2+pjet(2,j)**2)
         pp = sqrt(kt(j)**2+pjet(3,j)**2)
         eta(j)=0.5d0*log((pjet(4,j)+pjet(3,j))/(pjet(4,j)-pjet(3,j)))
         rap(j)=0.5d0*log((pjet(4,j)+pjet(3,j))/(pjet(4,j)-pjet(3,j)))
         phi(j)=atan2(pjet(2,j),pjet(1,j))

c         write(*,*)'XXV2',pjet(:,j),kt(j),eta(j)
         
      enddo
      end
