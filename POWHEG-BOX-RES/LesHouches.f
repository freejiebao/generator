      subroutine gen_leshouches(id)
      implicit none
c id is either btilde or remn
      character * (*) id
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_em.h'
      include 'LesHouches.h'
      integer alr,em,rad,flem,flrad,coluborn(2),nrad
      integer nlegb,nlegr,j
      integer, save :: nnnb = 0
      real * 8  t,csi,y,azi,beams(0:3,2),masses(nlegborn),xb1,xb2,x1,x2,jacreal
      integer, allocatable, save :: reslistborn(:),reslistreal(:)
      real * 8, allocatable, save :: pborn(:,:),cmpborn(:,:),preal(:,:),cmpreal(:,:)
      logical, save :: ini=.true.
c When running with allrad set to 1, radiation generated in production and
c decays are all stored by the handle radiation routine
      if(id == 'btilde') then
         call handle_radiations('inquire',nrad,0d0,0d0,0d0,0d0)
      elseif(id == 'remn') then
c For remnants is like 1 radiation
         nrad = 1
      else
         write(*,*) ' gen_leshouches: got argument id=',id
         write(*,*) ' cannot handle, exiting ...'
         call exit(-1)
      endif
c For safety, call again the setup_resgroupstuff routine.
c rad_ubornsubp is set both for a btilde and for a remnant event.
      flst_ibornresgroup = flst_bornresgroup(rad_ubornsubp)
      call setup_resgroupstuff
c
      call born_lh
c set scalup to an invalid value. At the end it should have been set.
c If not, throw an error and exit.
      scalup = -1
c
      if(nrad.eq.0) then
c it is a Born event or a LO event
c first assign flavours and colours to the underlying Born process
         call momenta_lh(kn_pborn,flst_ibornlength)
         if (flg_LOevents) then
c     set default scalup to the sqrt of the center-of-mass energy of the event.
c     For processes that need different values, the scalup value can be
c     overridden in the finalize_lh user subroutine.
            scalup=2*kn_cmpborn(0,1)
         else
            if (em_rad_on) then
               scalup=sqrt(rad_ptsqmin_em)
            else
               scalup=sqrt(rad_ptsqmin)
            endif
         endif
      else
c It enters here for both btilde and remnant events
         nlegb = flst_ibornlength
         if(ini.or.nlegb+nrad-1.gt.nnnb) then
c     we typically need a born array for nlegb momenta, and a real array
c     with one more momentum. However, the number of legs is variable if there
c     are resonances; we must reallocate bigger arrays if needed, in this case.
            if(.not.ini) then
c deallocate them first!
               deallocate(pborn)
               deallocate(cmpborn)
               deallocate(reslistborn)
               deallocate(preal)
               deallocate(cmpreal)
               deallocate(reslistreal)
            endif
c we must make room for all available radiations         
            allocate(pborn(0:3,nlegb+nrad-1))
            allocate(cmpborn(0:3,nlegb+nrad-1))
            allocate(reslistborn(nlegb+nrad-1))
            allocate(preal(0:3,nlegb+nrad))
            allocate(cmpreal(0:3,nlegb+nrad))
            allocate(reslistreal(nlegb+nrad))
            nnnb = nlegb+nrad-1
            ini = .false.
         endif

         if(id == 'btilde') then
c     it is an event with radiation
            reslistreal(1:nlegb) =
     1           flst_bornres(1:nlegb,rad_ubornsubp)
c     initially we assign the Born kinematics to the real momenta.
c     When entering the following loop, the current real will be assigned to the Born
c     temporary array, and the real will be build from the temporary Born and
c     the stored radiation parameters. In the flg_allrad == .true. case, this operation
c     may be performed several times, building radiation from each resonance (that is why
c     the previous real becomes the next Born.)
c     Better to use slices always ...
            nlegr = nlegb
            preal(:,1:nlegb) = kn_pborn(:,1:nlegb)
            cmpreal(:,1:nlegb) = kn_cmpborn(:,1:nlegb)
            masses(1:nlegb) = kn_masses(1:nlegb)
            x1 = kn_xb1
            x2 = kn_xb2
c     
            beams = kn_beams
            rad_kinreg = 0
            do j=1,nrad
               call handle_radiations('next',alr,t,csi,y,azi)
               if(t.lt.0) then
c no more acceptable radiations are found; leave the loop
                  exit
               endif
c the emitter is always withing the original flst_ibornlength position
               em = flst_emitter(alr)
c     rad_kinreg may be printed at the end of the event for debugging purposes.
c     the following scheme works as usual for a single radiation, i.e. rad_kinreg=1
c     for isr, and from 2 on for final state radiation, depending upon which line is
c     radiating.
c     In case there are multiple radiation (with allrad present), the radiation
c     regions are shifted two digits left. This assumes that there are less than 99
c     radiation regions. If there are two many radiating resonances, we must stop so that
c     rad_kinreg does not overflow.
               if(rad_kinreg < 2147483647/100) then
                  if(em < 3) then
                     rad_kinreg = rad_kinreg*100 + 1
                  else
                     if(em+2-flst_lightpart < 99) then
                        rad_kinreg = rad_kinreg*100 + (em+2-flst_lightpart)
                     endif
                  endif
               endif
               if(nlegr.gt.nnnb) then
                  write(*,*) ' gen_leshouches: nlegr>nnnb, should not be here!'
                  write(*,*) ' exiting ...'
                  call exit(-1)
               endif
c     the current real becomes the new Born.
               nlegb = nlegr
               reslistborn(1:nlegb) = reslistreal(1:nlegb)
               pborn(:,1:nlegb) = preal(:,1:nlegb)
               cmpborn(:,1:nlegb) = cmpreal(:,1:nlegb)
               xb1 = x1
               xb2 = x2
               nlegr = nlegb + 1
               if(em.le.2) then
                  call gen_real_phsp_isr_rad_g0(
     1                 nlegb,csi,y,azi,beams,
     2                 xb1,xb2,pborn(:,1:nlegb),
     3                 cmpborn(:,1:nlegb),x1,x2,preal(:,1:nlegr),cmpreal(:,1:nlegr),jacreal)
               else
                  call gen_real_phsp_fsr_rad_g0(
     1                 nlegb,reslistborn,em,csi,y,azi,
     2                 xb1,xb2,masses,pborn(:,1:nlegb),
     3                 cmpborn(:,1:nlegb),x1,x2,preal(:,1:nlegr),cmpreal(:,1:nlegr),jacreal)
               endif
               reslistreal(1:nlegb) = reslistborn(1:nlegb)
               if(em <= 2) then
                  reslistreal(nlegr) =  0
               else
                  reslistreal(nlegr) =  flst_alrres(em,alr)
               endif
c     In case flg_allrad is not set, we should set scalup=t. If flg_allrad, there
c     are several radiations to handle in the shower. No provision is given in the LH
c     interface to handle this. The most reasonable choice for scalup (although a bit improper)
c     is the scale for radiation in production. If there is no radiation in production we should
c     set it to sqrt(rad_ptsqmin). We do this in the final check.
               if(flg_allrad) then
                  if(reslistreal(nlegr).eq.0) then
                     scalup = sqrt(t)
                  endif
               else
                  scalup=sqrt(t)
               endif
               nup=nlegr
               call setup_real_lh
            enddo
            call momenta_lh(preal,nlegr)
         elseif(id == 'remn') then
c     for the remnant:
            alr = rad_alrsubp
            em = flst_emitter(alr)
            nlegr = flst_alrlength(alr)
            nup = nlegr
            reslistreal(1:nlegr) = 
     1           flst_alrres(1:nlegr,alr)            
            call setup_real_lh
            call momenta_lh(kn_preal,nlegr)
            scalup = sqrt(rad_pt2max)
         endif
      endif
c
      if(scalup.lt.0) then
         if(flg_allrad.and.nrad.gt.0) then
            scalup = sqrt(rad_ptsqmin)
         else
c should never get here ...
            write(*,*) ' gen_leshouches: error, scalup was not set ...'
            write(*,*) ' exiting  ...'
            call exit(-1)
         endif
      endif
c if there are resonances, setup up appropriate LH pointers
c (but this is done earlier)
c      call lh_resonances_real
c add resonances, perform decays, put particles on shell, etc.(or nothing!)
      call finalize_lh
      contains
         subroutine setup_real_lh
         implicit none
         istup(nup)=1
         spinup(nup)=9
         vtimup(nup)=0
         if(reslistreal(nup).eq.0) then
            mothup(1,nup)=1
            mothup(2,nup)=2
         else
            mothup(1,nup)=reslistreal(nup)
            mothup(2,nup)=reslistreal(nup)
         endif
         rad=nup
         if(em.eq.0) then
            if(kn_y.gt.0) then
               em=1
            else
               em=2
            endif
         endif
         flem=flst_alr(em,alr)
         flrad=flst_alr(flst_alrlength(alr),alr)
         coluborn(1)=icolup(1,em)
         coluborn(2)=icolup(2,em)
         if(em.le.2) then
c     setcolour_rad works with all incoming (or all outgoing) flavours and colours;
c     for ISR make everything outgoing:
c     thus in input change the sign of the emitter flavour, to make it outgoing
c     and conjugate its colour in output, to make it incoming.
            call setcolour_rad(coluborn,-flem,flrad,
     1           icolup(1,em),icolup(1,rad))
            call colour_conj(icolup(1,em))
         else
c     For ISR make everything incoming;
c     Change the sign of the emitter and radiated flavours in input,
c     to make it incoming;
c     conjugate their colours in the output, to make them outgoing.
            if (flrad.ne.22) then
               call setcolour_rad(coluborn,-flem,-flrad,
     1              icolup(1,em),icolup(1,rad))
            else
               call setcolour_rad(coluborn,-flem,flrad,
     1              icolup(1,em),icolup(1,rad))
            endif
            call colour_conj(icolup(1,rad))
            call colour_conj(icolup(1,em))
         endif
         if(flrad.eq.0) flrad=21
         idup(rad)=flrad
         if(flem.eq.0) flem=21
         idup(em)=flem
         end subroutine setup_real_lh
         
      end


c     i1<i2
      subroutine add_resonance(idpdg,i1,i2)
      implicit none
      include 'LesHouches.h'
      integer iduptmp(maxnup),istuptmp(maxnup),mothuptmp(2,maxnup),
     #     icoluptmp(2,maxnup)
      real * 8 puptmp(5,maxnup),vtimuptmp(maxnup),
     #     spinuptmp(maxnup)
      integer idpdg,i1,i2,i,j
      if (i1.ge.i2) then
         write(*,*) 'wrong sequence in add_resonance'
         stop
      endif
      do i=i1,nup
         iduptmp(i) = idup(i)
         istuptmp(i) = istup(i)
         mothuptmp(1,i) = mothup(1,i)
         mothuptmp(2,i) = mothup(2,i)
         icoluptmp(1,i) = icolup(1,i)
         icoluptmp(2,i) = icolup(2,i)
         do j=1,5
            puptmp(j,i)=pup(j,i)
         enddo
         vtimuptmp(i)=vtimup(i)
         spinuptmp(i)=spinup(i)
      enddo
      idup(i1)=idpdg
      istup(i1)=+2
      mothup(1,i1)=1
      mothup(2,i1)=2
      icolup(1,i1)=0
      icolup(2,i1)=0
      do j=1,4
         pup(j,i1)=puptmp(j,i1)+puptmp(j,i2)
      enddo
      pup(5,i1)=sqrt(pup(4,i1)**2-
     #     (pup(1,i1)**2+pup(2,i1)**2+pup(3,i1)**2))
      vtimup(i1)=0
      spinup(i1)=9
c     change mothers of decaying particles
      mothuptmp(1,i1)=i1
      mothuptmp(2,i1)=i1
      mothuptmp(1,i2)=i1
      mothuptmp(2,i2)=i1
      nup=nup+1      
      do i=i1+1, nup
         idup(i) = iduptmp(i-1)
         istup(i) = istuptmp(i-1)
         mothup(1,i) = mothuptmp(1,i-1)
         mothup(2,i) = mothuptmp(2,i-1)
         icolup(1,i) = icoluptmp(1,i-1)
         icolup(2,i) = icoluptmp(2,i-1)
         do j=1,5
            pup(j,i)=puptmp(j,i-1)
         enddo
         vtimup(i)=vtimuptmp(i-1)
         spinup(i)=spinuptmp(i-1)         
      enddo
      end
      


      subroutine colour_conj(icol)
      implicit none
      integer icol(2)
      integer itmp
      itmp=icol(2)
      icol(2)=icol(1)
      icol(1)=itmp
      end

      subroutine momenta_lh(p,n)
      implicit none
      integer n
      real * 8 p(0:3,n)
      integer k,mu
      include 'LesHouches.h'
      do k=1,n
         do mu=1,3
            pup(mu,k)=p(mu,k)
         enddo
         pup(4,k)=p(0,k)
         pup(5,k)=sqrt(abs(p(0,k)**2-p(1,k)**2
     #       -p(2,k)**2-p(3,k)**2))
      enddo
      end

      subroutine born_lh
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'LesHouches.h'
c      include 'PhysPars.h'
      include 'pwhg_st.h'
      integer k,fl,subp
      nup=flst_bornlength(rad_ubornsubp)
c id of the event
      idprup=lprup(1)
ccccc CAVEAT: aqedup must not be set here
ccccc since otherwise a dependence on the
ccccc process-dependent PhysPars.h must be
ccccc introduced
      aqedup=-1                 ! ph_alphaem
cccccccccccccccccccccccccccccccccccccccccccccccccccccc
      aqcdup=st_alpha

      do k=1,nup
         fl=flst_born(k,rad_ubornsubp)
c gluons are numbered 21 in pdg
         if(fl.eq.0) fl=21
         idup(k)=fl
         if(k.gt.2) then
            istup(k)=1
            mothup(1,k)=1
            mothup(2,k)=2
         else
            istup(k)=-1
            mothup(1,k)=0
            mothup(2,k)=0
         endif
         spinup(k)=9
         vtimup(k)=0
      enddo
      call lh_resonances_born
c     before calling the colour setting subroutine, find
c     a subprocess that was actually computed even if the
c     smartsig mechanism is at work. This is needed, for exmaple,
c     in Madgraph generated amplitude, where the call to the Born
c     sets up cached informatin to generate the colour structure.
c     If smartsig is active, this cached information may be incorrect.
      if(flg_smartsig) then
         call get_index_live_subp('allborn',rad_ubornsubp,subp)
      else
         subp = rad_ubornsubp
      endif
      call borncolour_lh(subp)
      end

      subroutine lh_resonances_born
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'LesHouches.h'
      integer moth,j,iub
      iub = rad_ubornsubp
      do j=1,nup
         moth=flst_bornres(j,iub)
         if(moth.ne.0) then
            mothup(1,j)=moth
            mothup(2,j)=moth
            istup(moth)=2
         endif
      enddo
      end


c  fix nlegreal in the following, if  lh_resonances_real is needed
c$$$      subroutine lh_resonances_real
c$$$      implicit none

      subroutine getnewcolor(newcolor)
      implicit none
      integer newcolor
      include 'LesHouches.h'
      integer j,k
      newcolor=511
 1    continue
      do j=1,nup
         do k=1,2
            if(icolup(k,j).eq.newcolor) then
               newcolor=newcolor+1
               goto 1
            endif
         enddo
      enddo
      end

c Given a vertex with 3 partons, the first parton with incoming colour
c colin, the second and third partons with incoming flavours fl2, fl3,
c it assigns the incoming colours of the second and third partons
c colout2, colout3. The colour assignment is unambiguous in all cases, but in
c the one where both fl2 and fl3 are gluons, where a 50% random choice is made
c over the two possible colour connections.
      subroutine setcolour_rad(colin,fl2,fl3,colout2,colout3)
      implicit none
      integer colin(2),fl2,fl3,colout2(2),colout3(2)
      integer newcolor
      real * 8 random
      logical is_coloured
      external random,is_coloured
      call getnewcolor(newcolor)
c First handle photon case
      if(fl2.eq.22) then
         colout2=0
         colout3(1)=colin(2)
         colout3(2)=colin(1)
      elseif(fl3.eq.22) then
         colout3=0
         colout2(1)=colin(2)
         colout2(2)=colin(1)
      elseif(colin(1).eq.0.and.colin(2).eq.0) then
         if(is_coloured(fl2)) then
            if(fl2.gt.0) then
               colout2(1)=newcolor
               colout2(2)=0
               colout3(2)=newcolor
               colout3(1)=0
            elseif(fl3.gt.0) then
               colout2(1)=0
               colout2(2)=newcolor
               colout3(2)=0
               colout3(1)=newcolor
            else
               goto 998
            endif
         else
            colout2=0
            colout3=0
         endif
      else
c now handle all coloured particles
         if(colin(1).ne.0.and.colin(2).ne.0) then
            if(fl2.eq.0.and.fl3.eq.0) then
               if(random().gt.0.5d0) then
                  colout2(1)=colin(2)
                  colout2(2)=newcolor
                  colout3(1)=newcolor
                  colout3(2)=colin(1)
               else
                  colout3(1)=colin(2)
                  colout3(2)=newcolor
                  colout2(1)=newcolor
                  colout2(2)=colin(1)
               endif
            elseif(fl2.gt.0.and.fl3.lt.0) then
               colout2(2)=0
               colout2(1)=colin(2)
               colout3(1)=0
               colout3(2)=colin(1)
            elseif(fl2.lt.0.and.fl3.gt.0) then
               colout2(1)=0
               colout2(2)=colin(1)
               colout3(2)=0
               colout3(1)=colin(2)
            else
               goto 998
            endif
         elseif(colin(2).eq.0) then
            if(fl2.eq.0) then
               colout3(1)=0
               colout3(2)=newcolor
               colout2(1)=newcolor
               colout2(2)=colin(1)
            elseif(fl3.eq.0) then
               colout2(1)=0
               colout2(2)=newcolor
               colout3(1)=newcolor
               colout3(2)=colin(1)
            else
               goto 998
            endif
         elseif(colin(1).eq.0) then
            if(fl2.eq.0) then
               colout3(1)=newcolor
               colout3(2)=0
               colout2(2)=newcolor
               colout2(1)=colin(2)
            elseif(fl3.eq.0) then
               colout2(1)=newcolor
               colout2(2)=0
               colout3(1)=colin(2)
               colout3(2)=newcolor
            else
               goto 998
            endif
         else
            goto 998
         endif
      endif
      return
 998  continue
      write(*,*)
     #     ' Error in setcolour_rad: inconsistent colour flavour input'
      write(*,*) 'colin[1:2] ',colin(1),' ',colin(2)
      write(*,*) 'fl2, fl3 ',fl2,' ',fl3
      write(*,*) 'newcolor ',newcolor
      call pwhg_exit(1)
      end


      subroutine displeshouches
      include 'LesHouches.h'
      integer mark(200),icol(200),j,k,ilist,icur
      write(*,*) 'incoming beams:', idbmup(1), idbmup(2)
      write(*,*) 'number of partons in subprocess',nup
      write(*,'(a,10(i3,1x))') 'ist:',(istup(j),j=1,nup)
      write(*,'(a,10(i3,1x))') 'ids:',(idup(j),j=1,nup)
      do j=1,nup
         write(*,'(5(d10.4,1x))') (pup(k,j),k=1,5)
      enddo
c check that quarks have zero anticolour, and antiquarks
c have zero colour
      do j=1,nup
         if(idup(j).ge.1.and.idup(j).le.6.and.icolup(2,j).ne.0) then
            write(*,*) ' error: anticolor in quark'
         elseif(idup(j).ge.-6.and.idup(j).le.-1.and.icolup(1,j).ne.0)
     #           then
            write(*,*) ' error: color in quark'
         endif
      enddo
c Print color linked lists
c first conjugate incoming colors
      call colour_conj(icolup(1,1))
      call colour_conj(icolup(1,2))
      do j=1,nup
         mark(j)=1
      enddo
      imarked=0
      do j=1,nup
         if(istup(j).eq.2.or.
     #        (icolup(1,j).eq.0.and.icolup(2,j).eq.0)) then
            mark(j)=0
            imarked=imarked+1
         endif
         if(istup(j).ne.2.and.idup(j).gt.0.and.idup(j).lt.6) then
            icur=j
         endif
      enddo
      mark(icur)=0
      ilist=1
      imarked=imarked+1
      icol(ilist)=icur
 12   continue
      do j=1,nup
         if(istup(j).ne.2.and.
     #        (icolup(1,j).ne.0.or.icolup(2,j).ne.0)) then
         if(mark(j).ne.0.and.icolup(1,icur).eq.icolup(2,j)) then
            ilist=ilist+1
            imarked=imarked+1
            icol(ilist)=j
            mark(j)=0
            icur=j
            if(imarked.eq.nup) goto 22
            if(icolup(1,icur).eq.0) then
               do k=1,nup
                  if(mark(k).ne.0.and.icolup(2,k).eq.0) then
                     ilist=ilist+2
                     icol(ilist)=k
                     icol(ilist-1)=0
                     imarked=imarked+1
                     icur=k
                     mark(k)=0
                     goto 12
                  endif
               enddo
               write(*,*) ' inconsistent colors!'
            endif
            goto 12
         endif
         endif
      enddo
      write(*,*) ' inconsistent colors!'
 22   continue
      call colour_conj(icolup(1,1))
      call colour_conj(icolup(1,2))
      write(*,*) (icol(j),j=1,ilist)
      end


      subroutine pdfreweightinfo(id1,id2,x1,x2,xmufact,xf1,xf2)
      implicit none
      integer id1,id2
      real * 8 x1,x2,xf1,xf2,xmufact
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_pdf.h'
      include 'pwhg_st.h'
      include 'LesHouches.h'
      real * 8 pdf(-pdf_nparton:pdf_nparton)
      if(rad_type.eq.1) then
c Btilde event: pass x1 and x2, id1, id2 etc. of the current underlying Born
         id1=flst_born(1,rad_ubornsubp)
         id2=flst_born(2,rad_ubornsubp)
         x1=kn_xb1
         x2=kn_xb2
         call setscalesbtilde
      elseif(rad_type.eq.2.or.rad_type.eq.3) then
         id1=idup(1)
         id2=idup(2)
         if(id1.eq.21) id1=0
         if(id2.eq.21) id2=0         
         x1=kn_x1
         x2=kn_x2
         call setscalesbtilde
      endif
      xmufact=sqrt(st_mufact2)
      call pdfcall(1,x1,pdf)
      xf1=x1*pdf(id1)
      call pdfcall(2,x2,pdf)
      xf2=x2*pdf(id2)
      if(id1.eq.0) id1=21
      if(id2.eq.0) id2=21
      end

