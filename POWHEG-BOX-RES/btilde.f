      function btilde(iresgroup,xx,www0,ifirst,imode,
     1     retval,retval0)
c retval is the function return value
c retvavl0 is an 'avatar' function the has similar value, but is much
c easier to compute (i.e. the Born term in this case)
c imode = 0 compute retval0 only.
c imode = 1 compute retval, retval0
c return value: 0: success; 1: retval0 was not computed
c                 (this function does not support an avatar function)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_flg.h'
      include 'pwhg_math.h'
c     independent variables for real graph: number of final state
c     legs times 3, take away 4 for 4-momentum conservation, add 2
c     for x_1 and x_2, and take away an overall azimuth
      integer iresgroup
      real * 8 xx(ndiminteg),www0,retval,retval0
      real * 8 xrad(3)
      real * 8 xborn(ndiminteg-3)
      integer btilde,ifirst,imode,iret
      real * 8 resborn(maxprocborn),resvirt(maxprocborn),
     1     resreal(maxprocborn),rescoll(maxprocborn),resmis(maxprocborn)
      real * 8 results(maxprocborn)
      real * 8 tmp,suppfact,www,wwwtot
      integer j
      save results,resborn,resvirt,wwwtot,suppfact
      real * 8 seconds
      real *8 totborn,totvirt,ptotborn
      logical pwhg_isfinite 
      external pwhg_isfinite
      real * 8 powheginput
      logical ini,btildebornon,btildevirton,btildecollon,btilderealon,
     1     softmismchon
      data ini/.true./
      save ini,btildebornon,btildevirton,btildecollon,btilderealon,
     1     softmismchon
      if(ini) then
         btildebornon = flg_bornonly .or.
     1        .not.(powheginput("#btildeborn").eq.0 .or. flg_virtonly)
         btildevirton = flg_virtonly .or.
     1        .not.(powheginput("#btildevirt").eq.0)
         btildecollon = .not.(powheginput("#btildecoll").eq.0
     1        .or. flg_virtonly)
         btilderealon = .not.(powheginput("#btildereal").eq.0
     1        .or. flg_virtonly)
         softmismchon = .not.(powheginput("#softmismch").eq.0
     1        .or. flg_virtonly)
         ini = .false.
      endif
      flst_ibornresgroup = iresgroup
      call setup_resgroupstuff
      btilde=0
      www=www0*hc2
      do j=1,ndiminteg-3
         xborn(j)=xx(j)
      enddo
      do j=1,3
         xrad(j)=xx(ndiminteg-3 + j)
      enddo
      if(ifirst.eq.0) then
         wwwtot=www
c     sets born momenta in kin. common block
         call gen_born_phsp(xborn)
         call born_suppression(suppfact)
c set scales
         call setscalesbtilde
         call allborn
c     sets xscaled, y, phi in kinematics common block
         call btildeborn(resborn)
         if(.not.btildebornon) resborn = 0
         if (.not.flg_bornonly.and..not.imode.eq.0) then
            call reset_timer
            if(btildevirton) then
               call btildevirt(resvirt)
            else
               resvirt = 0
            endif
            call get_timer(seconds)
            call addtocnt('virt time (sec)',seconds)
            call reset_timer
            if(btildecollon) then
               call btildecoll(xrad,rescoll,www)
            else
               rescoll = 0
            endif
            if(softmismchon) then
               call softmismatchres(xrad,resmis,www)
            else
               resmis = 0
            endif
            if(btilderealon) then
               call btildereal(xrad,resreal,www)
            else
               resreal = 0
            endif
            call get_timer(seconds)
            call addtocnt('real time (sec)',seconds)
         endif
c     accumulate values
         retval=0
         do j=1,flst_nborn
c     jacobians are already included in rescoll and resreal
            tmp=resborn(j)
            if (.not.flg_bornonly.and..not.imode.eq.0) then
               tmp = tmp   
     1              + resvirt(j)
     2              + rescoll(j) 
     3              + resmis(j)
     4              + resreal(j)
            endif
c     initial value in results
            results(j)=tmp*www*suppfact
            retval=retval+tmp*www*suppfact
         enddo
      elseif(ifirst.eq.1) then
c     subsequent calls:
c     In case of folding the call to btildeborn and btildevirt can be
c     avoided, since results are the same.
c     If the NLO calculation is performed also (flg_nlotest is set)
c     we need to accumulate all weight within a single folding sequence
c     in order to later output the correct Born and Virtual contribution
c     to the NLO analysis routine.
         wwwtot=wwwtot+www
         if (.not.flg_bornonly.and..not.imode.eq.0) then
c btildecoll and btildereal take care themselves to invoke the NLO
c analysis if required.
            call reset_timer
c in case btlscalereal is set, we need to reset the scales
c to the underlying Born value for the computation of the
c collinear remnants.
            call setscalesbtilde
            if(btildecollon) then
               call btildecoll(xrad,rescoll,www)
            else
               rescoll = 0
            endif
            if(softmismchon) then
               call softmismatchres(xrad,resmis,www)
            else
               resmis = 0
            endif
            if(btilderealon) then
               call btildereal(xrad,resreal,www)
            else
               resreal = 0
            endif
            call get_timer(seconds)
            call addtocnt('real time (sec)',seconds)
         endif
         retval=0
         do j=1,flst_nborn
            tmp=resborn(j)
            if (.not.flg_bornonly.and..not.imode.eq.0) then
               tmp = tmp   
     1              + resvirt(j)
     2              + rescoll(j) 
     3              + resmis(j)
     4              + resreal(j)
            endif
c     accumulate values in results
            results(j)=results(j)+tmp*www*suppfact
            retval=retval+tmp*www*suppfact
         enddo
      elseif(ifirst.eq.2) then
         totborn=0d0
c compute Born, to return in retval0
         ptotborn=0
         do j=1,flst_nborn
            totborn=totborn+resborn(j)
            ptotborn=ptotborn+abs(resborn(j))
         enddo
         totborn=totborn*wwwtot
         ptotborn=ptotborn*wwwtot
         if (.not.pwhg_isfinite(totborn)) then 
            totborn = 0d0
            ptotborn = 0d0
            resborn = 0d0 
         endif
         if(flg_nlotest) then
c     output Born
            if(.not.imode.eq.0) then
               call analysis_driver(totborn,0)
            endif
            if(.not.flg_bornonly.and..not.imode.eq.0) then
c     output virtual + soft mismatch
               totvirt=0d0
               do j=1,flst_nborn
                  totvirt=totvirt+resvirt(j)+resmis(j)
               enddo
               totvirt=totvirt*wwwtot
               if (.not.pwhg_isfinite(totvirt)) then 
                  totvirt = 0d0 
                  resvirt = 0d0 
               endif
               call analysis_driver(totvirt,0)
            endif
            call pwhgaccumup
         endif
c Make the born part of the result available;
c (to test, if bornonly is set, should equal the output btilde when ifirst=2)
         retval0=ptotborn*suppfact
         btilde=0
c closing call to end a sequence of correlated events in the
c analysis routines.
c     closing call: accumulate values with correct signs
         retval=0
         if(.not.flg_ingen) then
            call adduptotals(results,flst_nborn)
         else
c the array is useful to pick a flavour configuration when generating events
            call storeradarray(results)
         endif
         do j=1,flst_nborn
c this is only useful if withnegweights on (i.e. =1 in powheg.input,
c logical true here). However, better set a default (Les Houches
c interface will simply output this sign for the event.)
            if(flg_withnegweights) then
               if(results(j).lt.0) then
                  results(j)=-results(j)
               endif                  
            else
               if(results(j).lt.0) then
                  results(j)=0
               endif
            endif
            retval=retval+results(j)
         enddo
      else
         write(*,*) 'wrong value of ifirst in btilde => ',ifirst
         call exit(-1)
      endif
      end
      

