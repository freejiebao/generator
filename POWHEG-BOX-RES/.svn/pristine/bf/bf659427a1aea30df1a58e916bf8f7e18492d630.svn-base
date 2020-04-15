      subroutine btildereal(xrad,resreal,www)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      include 'pwhg_par.h'
      real * 8 xrad(3),resreal(maxprocborn),www
      real * 8 r0(maxalr),rc(maxalr),rp(maxalr),rm(maxalr),
     1 r0s(maxalr),rcs(maxalr),rps(maxalr),rms(maxalr),xl,xlp,xlm,
     2 jac_over_csi,jac_over_csi_coll,jac_over_csi_soft,
     3 jac_over_csi_p,jac_over_csi_m,rrr0,rrrc,rrr0s,rrrcs,
     4 rrrp,rrrps,rrrm,rrrms,remnant,out0,out1
      integer j,iuborn
      logical valid_emitter
      external valid_emitter
      logical pwhg_isfinite
      external pwhg_isfinite
      do j=1,flst_nborn
         resreal(j)=0
      enddo
      do kn_emitter=0,nlegborn
c output values for analysis_driver
         out0=0
         out1=0
c check that emitter is valid
         if(valid_emitter(kn_emitter)) then
            if(kn_emitter.gt.2) then
c     final state radiation.
c     Once we know the emitter, we know the resonance region.
               call gen_real_phsp_fsr(xrad,jac_over_csi,
     1              jac_over_csi_coll,jac_over_csi_soft)
c This subroutine may set the scales with values depending
c upon the real emission kinematics
               call setscalesbtlreal
c sigreal fills the array r0 with the value of the R_alpha contribution
c that have emitter equal to kn_emitter. All other contributions are set
c to zero. 
               call sigreal_btl(r0)
               if(flg_withsubtr) then
c We may prefer to set the counterterms scales different from the real scales
                  call setscalesbtlct
                  call collfsr(rc)
c     soft subtraction
                  call soft(r0s)
                  call softcollfsr(rcs)
c     in final state radiation csimax is independent of y
                  xl=log(kn_csimax)
               endif
               do j=1,flst_nalr
                  iuborn=flst_alr2born(j)
                  rrr0=r0(j)*kn_jacborn
     1                 *jac_over_csi/(1-kn_y)/kn_csitilde
                  if(flg_withsubtr) then
                     rrrc=rc(j)*kn_jacborn
     1                 *jac_over_csi_coll/(1-kn_y)/kn_csitilde
                     rrr0s=r0s(j)*kn_jacborn
     1                    *jac_over_csi_soft/(1-kn_y)/kn_csitilde
c     In case of massive (fermion) emitter, the subtraction term is very large.
c     If we are generating events for subsequent reweighting, we reduce it in size
c     by making it closer to the AP splitting, and neglecting logs (xl) arising
c     from the limit in csitilde.
                     if(flg_for_reweighting. and.
     1                    kn_masses(kn_emitter) > 0) then
                        rrr0s = rrr0s * (1+(1-kn_csitilde)**2)/2
                        xl=0
                     endif
                     rrrcs=rcs(j)*kn_jacborn
     1                 *jac_over_csi_soft/(1-kn_y)/kn_csitilde
                     remnant=(rrr0s-rrrcs)*xl*kn_csitilde
                  endif
                  if(flg_withsubtr) then
                     resreal(iuborn)= resreal(iuborn)+rrr0-rrrc
     1                    -rrr0s+rrrcs+remnant
                  else
c     provide a damping factor for the singular region,
c     to avoid divergent integral (25 is an ad hoc value
                     resreal(iuborn)= resreal(iuborn)
     1               +rrr0*(1-kn_y**2)*kn_csi/
     2                  (25/kn_sbeams+(1-kn_y**2)*kn_csi)
                  endif
                  if(flg_nlotest) then
                     out1=out1+rrr0
                     if(flg_withsubtr) then
                        out0=out0-rrrc-rrr0s+rrrcs+remnant
                     endif
                  endif
               enddo
            else
c     initial state singularities.
c     Regions that have only + (-) collinear singularity should return
c     zero rm (rp).
               call gen_real_phsp_isr
     #(xrad,jac_over_csi,jac_over_csi_p,jac_over_csi_m,
     #jac_over_csi_soft)
               call setscalesbtlreal
               call sigreal_btl(r0)
               if(flg_withsubtr) then
                  call setscalesbtlct
                  call soft(r0s)
                  if(kn_emitter.ne.2) then
                     call collisrp(rp)
                     call softcollisrp(rps)
                  endif
                  if(kn_emitter.ne.1) then
                     call collisrm(rm)
                     call softcollisrm(rms)
                  endif
c     remnants (see xscaled.pdf in docs directory)
                  xl =log(kn_csimax)
                  xlp=log(kn_csimaxp)
                  xlm=log(kn_csimaxm)
               endif
               do j=1,flst_nalr
                  rrr0=r0(j)*kn_jacborn
     #                 *jac_over_csi/(1-kn_y**2)/kn_csitilde
                  if(flg_withsubtr) then
                     rrr0s=r0s(j)*kn_jacborn
     #                 *jac_over_csi_soft/(1-kn_y**2)/kn_csitilde
                     remnant=rrr0s*xl*kn_csitilde
                     if(kn_emitter.ne.2) then
                        rrrp=rp(j)*kn_jacborn
     #                 *jac_over_csi_p/(1-kn_y)/kn_csitilde/2
                        rrrps=rps(j)*kn_jacborn
     #                 *jac_over_csi_soft/(1-kn_y)/kn_csitilde/2
                        remnant=remnant-rrrps*xlp*kn_csitilde
                     else
                        rrrp=0
                        rrrps=0
                     endif
                     if(kn_emitter.ne.1) then
                        rrrm=rm(j)*kn_jacborn
     #                 *jac_over_csi_m/(1+kn_y)/kn_csitilde/2
                        rrrms=rms(j)*kn_jacborn
     #                 *jac_over_csi_soft/(1+kn_y)/kn_csitilde/2
                        remnant=remnant-rrrms*xlm*kn_csitilde
                     else
                        rrrm=0
                        rrrms=0
                     endif
                  endif
                  iuborn=flst_alr2born(j)
                  if(flg_withsubtr) then
                     resreal(iuborn)= resreal(iuborn)+rrr0
     #              -rrr0s-rrrp-rrrm+rrrps+rrrms+remnant
                  else
c     provide a damping factor for the singular region,
c     to avoid divergent integral (25 is an ad hoc value)
                     resreal(iuborn)= resreal(iuborn)
     #               +rrr0*(1-kn_y**2)*kn_csi/
     #                  (25/kn_sbeams+(1-kn_y**2)*kn_csi)
                  endif
                  if(flg_nlotest) then
                     out1=out1+rrr0
                     if(flg_withsubtr) then
                        out0=out0-rrr0s-rrrp-rrrm+rrrps+rrrms+remnant
                     endif
                  endif
               enddo
            endif
         endif
         if (.not.pwhg_isfinite(out0).or..not.pwhg_isfinite(out1)) then
            out0 = 0d0 
            out1 = 0d0 
            resreal = 0d0 
         endif
         if(flg_nlotest) then
            out0=out0*www
            out1=out1*www
            if(out0.ne.0d0) call analysis_driver(out0,0)
            if(out1.ne.0d0) call analysis_driver(out1,1)
         endif
      enddo
      end

      subroutine checklims(iun)
      implicit none
      integer iun
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_par.h'
      include 'pwhg_kn.h'
      include 'pwhg_dbg.h'
      include 'pwhg_rnd.h'
      external sigreal_btl,soft,collfsr,softcollfsr, collisrp,
     $     softcollisrp,collisrm,softcollisrm
      integer iresgroup_save
      real * 8 powheginput
      logical valid_emitter, savewithdamp
      real * 8 tinyforlims, save_isrtinycsi,save_isrtinyy,
     1 save_fsrtinycsi,save_fsrtinyy 
      procedure() :: valid_emitter
      savewithdamp = flg_withdamp
      flg_withdamp = .false.
      call randomsave
      if(rnd_cwhichseed /= 'none') then
         call setrandom(rnd_initialseed,rnd_i1,rnd_i2)
      endif
      if(powheginput("#chklimseed") .gt. 0) then
         call setrandom(nint(powheginput("#chklimseed")),0,0)
      endif
      tinyForLims=powheginput("#tinyForLims")
      if(tinyForLims .ge. 0) then
         save_isrtinycsi = par_isrtinycsi
         save_isrtinyy   = par_isrtinyy  
         save_fsrtinycsi = par_fsrtinycsi
         save_fsrtinyy   = par_fsrtinyy  
         
         par_isrtinycsi = tinyforlims 
         par_isrtinyy   = tinyforlims 
         par_fsrtinycsi = tinyforlims 
         par_fsrtinyy   = tinyforlims 
      endif

      do flst_ibornresgroup = 1,flst_nbornresgroup
         if(flst_nbornresgroup.gt.1) then
            write(iun,*) '******************************************'   
            write(iun,*) ' Resonance group ', flst_ibornresgroup,
     1           ' out of ',flst_nbornresgroup
            write(iun,*) '******************************************'   
         endif
         call setup_resgroupstuff
         if(dbg_softtest) then
            write(iun,*) '******************************************'   
            write(iun,*) '           CHECK  SOFT LIMITS             '     
            write(iun,*)
            do kn_emitter=0,flst_ibornlength
               call checksoft(sigreal_btl,soft,' soft',iun)
            enddo
            write(iun,*) '******************************************'
            write(iun,*)
         endif
      
         if(dbg_colltest) then
            write(iun,*) '******************************************'   
            write(iun,*) '      CHECK  COLL. LIMITS FOR FSR       '         
            write(iun,*)
            do kn_emitter=3,flst_ibornlength
               if(valid_emitter(kn_emitter)) then
                  if(kn_masses(kn_emitter) == 0) then
                     call checkcoll(sigreal_btl,collfsr,1,' coll',iun)
                  else
                     write(iun,*) ' emitter ',kn_emitter,' is massive, '//
     1                    ' no collinear test performed.'
                  endif
               endif
            enddo
            write(iun,*) '******************************************'   
            write(iun,*)
            write(iun,*) '******************************************'   
            write(iun,*) '      CHECK  COLL. LIMITS FOR ISR       '         
            write(iun,*)
            do kn_emitter=0,2
c     call randomsave
               if(kn_emitter.ne.2) call checkcoll(sigreal_btl,collisrp,1
     $              ,' coll-plus',iun)
c     call randomrestore
               if(kn_emitter.ne.1) call checkcoll(sigreal_btl,collisrm,-1
     $              ,' coll-minus',iun)
            enddo
            write(iun,*) '******************************************'   
            write(iun,*)
         endif
      
         if(dbg_softtest.and.dbg_colltest) then  
            write(iun,*) '******************************************'   
            write(iun,*) '   CHECK  SOFT-COLL. LIMITS FOR FSR     '         
            write(iun,*)
            do kn_emitter=3,flst_ibornlength
               if(valid_emitter(kn_emitter)) then
                  if(kn_masses(kn_emitter) == 0) then
                     call checksoft(collfsr,softcollfsr,' soft-coll',iun)
                  else
                     write(iun,*) ' emitter ',kn_emitter,' is massive, '//
     1                    ' no soft-collinear test performed.'
                  endif
               endif
            enddo
            write(iun,*) '******************************************'
            write(iun,*)
            write(iun,*) '******************************************'   
            write(iun,*) '   CHECK  SOFT-COLL. LIMITS FOR ISR +   '         
            write(iun,*)
            do kn_emitter=0,2
               if(kn_emitter.ne.2)call checksoft(collisrp,softcollisrp,
     $              ' soft-coll-plus',iun)
            enddo
            write(iun,*) '******************************************'
            write(iun,*)
            write(iun,*) '******************************************'   
            write(iun,*) '   CHECK  SOFT-COLL. LIMITS FOR ISR -   '         
            write(iun,*)
            do kn_emitter=0,2
               if(kn_emitter.ne.1)call checksoft(collisrm,softcollisrm,
     $              ' soft-coll-minus',iun)
            enddo
            write(iun,*) '******************************************'
            write(iun,*)
            
         
            write(iun,*) '******************************************'   
            write(iun,*) '   CHECK  COLL.-SOFT LIMITS FOR FSR     '         
            write(iun,*)
            do kn_emitter=3,flst_ibornlength
               if(valid_emitter(kn_emitter)) then
                  if(kn_masses(kn_emitter) == 0) then
                     call checkcoll(soft,softcollfsr,1,' coll-soft',iun)
                  else
                     write(iun,*) ' emitter ',kn_emitter,' is massive, '//
     1                    ' no coll-soft test performed.'
                  endif
               endif
            enddo
            write(iun,*) '******************************************'
            write(iun,*)
            write(iun,*) '******************************************'   
            write(iun,*) '   CHECK  COLL.-SOFT LIMITS FOR ISR     '         
            write(iun,*)
            do kn_emitter=0,2
               if(kn_emitter.ne.2) call checkcoll(soft,softcollisrp,1
     $              ,' coll-plus-soft',iun)
               if(kn_emitter.ne.1) call checkcoll(soft,softcollisrm,-1
     $              ,' coll-minus-soft',iun)
            enddo
         endif
      enddo
      call randomrestore
      write(iun,*) ' ****************** End Checks *****************'
      flst_ibornresgroup = iresgroup_save
      flg_withdamp = savewithdamp
      if(tinyForLims .ge. 0) then
         par_isrtinycsi = save_isrtinycsi
         par_isrtinyy   = save_isrtinyy  
         par_fsrtinycsi = save_fsrtinycsi
         par_fsrtinyy   = save_fsrtinyy  
      endif
      end

      subroutine checkborn(iun)
c Check if Born, colour correlated born and spin correlated Born
c are consistent with total Born
      implicit none
      integer iun
      include 'nlegborn.h'
      include 'pwhg_math.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_br.h'
      include 'pwhg_st.h'
      integer  iborn,j,k,mu,kres,ires,lenb
      real * 8 tot,ttt
      real * 8 gtens(0:3,0:3),ap
      data gtens/1d0, 0d0, 0d0, 0d0,
     #           0d0,-1d0, 0d0, 0d0,
     #           0d0, 0d0,-1d0, 0d0,
     #           0d0, 0d0, 0d0,-1d0/
      save gtens
      logical colcorr,isfinalstate,is_coloured
      external colcorr,isfinalstate,is_coloured
      do ires=1,flst_nreson         
         do iborn=1,flst_nborn
            if(flst_ibornresgroup .ne. flst_bornresgroup(iborn)) cycle
            lenb = flst_bornlength(iborn)
            kres=flst_reslist(ires)
            do j=1,lenb
               if(colcorr(j,iborn,kres)) then
                  tot=0
                  do k=1,lenb
                     if(colcorr(k,iborn,kres)) then
                        if(k.ne.j) then
                           tot=tot+br_bornjk(j,k,iborn)
                        endif
                     endif
                  enddo
                  if(br_born(iborn) /= 0) then
                     if(flst_born(j,iborn).eq.0) then
                        tot=tot/(ca*br_born(iborn))
                     else
                        tot=tot/(cf*br_born(iborn))
                     endif
                     if(abs((tot-1)/tot).gt.1d-8) then
                        write(iun,'(f6.3,a,20(i3,1x))') tot,
     1                       ' colour check fails for flav. struct:',kres,
     2                       (flst_born(k,iborn),k=1,lenb)
                     endif
                  elseif(tot /= 0) then
                        write(iun,'(f6.3,a,20(i3,1x))') tot,
     1                       ' colour check fails for flav. struct:',kres,
     2                       (flst_born(k,iborn),k=1,lenb)
                     
                  endif
               endif
            enddo
         enddo
      enddo
      do iborn=1,flst_nborn
         lenb = flst_bornlength(iborn)
         do j=1,lenb
            if(flst_born(j,iborn).eq.0) then
               tot=0
               do mu=0,3
                  tot=tot-gtens(mu,mu)*br_bmunu(mu,mu,j,iborn)
               enddo
               if(br_born(iborn) /= 0) then
                  ttt=tot/br_born(iborn)
               elseif(tot == 0) then
                  ttt=1
               else
                  ttt=0
               endif
               if(abs((ttt-1)/ttt).gt.1d-8) then
                  write(iun,'(f6.3,a,i2,a,20(i3,1x))')
     1                 ttt, ' spin correlated amplitude'//
     2                 ' wrong for leg', j, ' flavour struct:',
     3                 (flst_born(k,iborn),k=1,lenb)
               endif
            endif
         enddo
      enddo
c$$$      else
c$$$         do iborn=1,flst_nborn
c$$$            lenb = flst_bornlength(iborn)
c$$$            do j=1,lenb
c$$$               if( (j.le.2.or.isfinalstate(j,lenb,flst_bornres(:,iborn)))
c$$$     1              .and.is_coloured(flst_born(j,iborn)) ) then
c$$$                  tot=0
c$$$                  do k=1,lenb
c$$$                     if( (k.le.2.or.isfinalstate(k,lenb,flst_bornres(:,iborn)))
c$$$     1                    .and.is_coloured(flst_born(K,iborn)) ) then
c$$$                        if(k.ne.j) then
c$$$                           tot=tot+br_bornjk(j,k,iborn)
c$$$                        endif
c$$$                     endif
c$$$                  enddo
c$$$                  if(flst_born(j,iborn).eq.0) then
c$$$                     tot=tot/(ca*br_born(iborn))
c$$$                  else
c$$$                     tot=tot/(cf*br_born(iborn))
c$$$                  endif
c$$$                  if(abs((tot-1)/tot).gt.1d-8) then
c$$$                     write(iun,'(f6.3,a,20(i3,1x))') tot,
c$$$     1                    ' colour check fails for flav. struct:',
c$$$     2                    (flst_born(k,iborn),k=1,nlegborn)
c$$$                  endif
c$$$               endif
c$$$            enddo
c$$$         enddo
c$$$         do iborn=1,flst_nborn
c$$$            do j=1,lenb
c$$$               if(j.le.2.or.isfinalstate(j,lenb,flst_bornres(:,iborn))) then
c$$$                  if(flst_born(j,iborn).eq.0) then
c$$$                     tot=0
c$$$                     do mu=0,3
c$$$                        tot=tot-gtens(mu,mu)*br_bmunu(mu,mu,j,iborn)
c$$$                     enddo
c$$$                     tot=tot/br_born(iborn)
c$$$                     if(abs((tot-1)/tot).gt.1d-8) then
c$$$                        write(iun,'(f6.3,a,i2,a,20(i3,1x))')
c$$$     1                       tot, ' spin correlated amplitude'//
c$$$     2                       ' wrong for leg', j, ' flavour struct:',
c$$$     3                       (flst_born(k,iborn),k=1,nlegborn)
c$$$                     endif
c$$$                  endif
c$$$               endif
c$$$            enddo
c$$$         enddo
c$$$      endif
c$$$

      end



      subroutine checksoft(sig,sigs,label,iun)
      implicit none
      include 'pwhg_dbg.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_st.h'
      character *(*) label
      integer iun
      real * 8 xborn(ndiminteg-3),xrad(3)
      integer nexp
      parameter (nexp=5)
      real * 8 jac_over_csi,
     1 jac_over_csi_coll,jac_over_csi_soft,r0(maxalr,nexp),
     2 r0s(maxalr,nexp),jac_over_csi_p,jac_over_csi_m,weight(nexp,maxalr),weights(nexp,maxalr)
      integer k,itmp,j,jexp,alr,alrp
      character * 15 flag
      character * 32 fff
      logical donotdo(maxalr)
      real * 8 random,dotp
      external random,dotp
      logical valid_emitter,iszero,isnonzero,isequal,bad_born_kin,bad_real_kin
      external valid_emitter
      real * 8 tolpar
 
      do alr=1,flst_nalr
c only radiated gluons or photons
c and only in current resgroup (borns are zero otherwise)
         if( (flst_alr(flst_ireallength,alr).ne.0 .and.
     1        flst_alr(flst_ireallength,alr).ne.22)
     2        .or. flst_ibornresgroup .ne. flst_bornresgroup(flst_alr2born(alr))
     3        .or. kn_emitter .ne. flst_emitter(alr)) then
            donotdo(alr) = .true.
         else
            donotdo(alr)=.false.
         endif
      enddo
c     The tolpar parameter sets the minimum in the ratio (transverse momentum)/(total energy)
c     for a kinematic configuration to be accepted for collinear tests. It is started
c     at 1, and for each failed configuration it is reduced by a factor 0.95 until an
c     acceptable configuration is found
      tolpar = 1
 19   continue
      tolpar = tolpar * 0.95d0

      do j=1,ndiminteg-3
         xborn(j)=random()
      enddo
      call gen_born_phsp(xborn)
      if(bad_born_kin(tolpar)) goto 19
      call setscalesbtilde
      call allborn
      call checkborn(iun)
c      write(iun,*)' mass',sqrt(2*dotp(kn_pborn(0,3),kn_pborn(0,4)))
      tolpar = 1
 20   continue
      do j=1,3
         xrad(j)=random()
      enddo
      tolpar = tolpar * 0.95d0
c Check soft limits
      if(valid_emitter(kn_emitter)) then
         do jexp=1,nexp
            xrad(1)=10d0**(-jexp)
            if(kn_emitter.gt.2) then
               call gen_real_phsp_fsr(xrad,jac_over_csi,
     $              jac_over_csi_coll,jac_over_csi_soft)
            else
               call gen_real_phsp_isr (xrad,jac_over_csi,jac_over_csi_p,
     $              jac_over_csi_m,jac_over_csi_soft)
            endif
            if(jexp == 1) then
               if(bad_real_kin(tolpar)) goto 20
               write(iun,*) ' Random Born variables ====> ',xborn
               write(iun,*) ' Random radiation variables ====> ',xrad
            endif
c     write(iun,*) '### Check soft',xrad(1)
            call sig(r0(1,jexp))
            call sigs(r0s(1,jexp))
            do alr=1,flst_nalr
               if(.not.donotdo(alr)) then
                  call realresweight_soft(alr,weights(jexp,alr))
                  call realresweight(alr,weight(jexp,alr))
               endif
            enddo
         enddo
         do alr=1,flst_nalr
            if(.not.donotdo(alr)) then
               write(10,*) '***********'
               write(10,*) ' emitter:',flst_emitter(alr)
               write(10,'(20(1x,i3))') flst_alr(1:flst_ireallength,alr)
               write(10,'(20(1x,i3))') flst_alrres(1:flst_ireallength,alr)
               do jexp=1,nexp
                  write(10,*) ' checksoft weight:',
     1                 weight(jexp,alr),' soft:',weights(jexp,alr),' ratio:',weight(jexp,alr)/weights(jexp,alr)
               enddo
            endif
         enddo

         do alr=1,flst_nalr
            if(donotdo(alr)) cycle
            fff = '(a,1x,i3,1x,a, 20(1x,i3),a,a,a)'
            write(fff(15:17),'(i3)') flst_ireallength
            write(iun,fff)
     $           ' emitter ',kn_emitter, ', process ',
     $           (flst_alr(j,alr),j=1,flst_ireallength) !,', ',label,':'
c look for equivalent alr's, write them out, and mark them for no checking             
            do alrp=alr+1,flst_nalr
               if(donotdo(alrp)) cycle
               isequal=.true.
               do jexp=1,nexp
                  if(r0(alr,jexp).ne.r0(alrp,jexp).or. r0s(alr,jexp)
     $                 .ne.r0s(alrp,jexp)) isequal=.false.
               enddo
               if(isequal) then
                     write(iun,'(2a,i2,a,20(1x,i3))') label,' emitter ',
     1                    flst_emitter(alrp),', process ',(flst_alr(j,alrp),j=1,nlegreal)
                     write(iun,'(2a,i2,a,20(1x,i3))') ' ==  ',' emitter ',
     1                    flst_emitter(alr),', process ',(flst_alr(j,alr),j=1,nlegreal)
                  donotdo(alrp)=.true.
               endif
            enddo
            do jexp=1,nexp
               call setwarnflag(
     1            r0s(alr,jexp),r0(alr,jexp),jexp,2,flag)
               if(r0s(alr,jexp) == 0 .or. r0(alr,jexp) /= r0(alr,jexp)
     1              .or. r0s(alr,jexp) /= r0s(alr,jexp)) then
                  write(iun,*) 'alr=',alr,r0(alr,jexp),'/',r0s(alr,jexp),flag
               else
                  write(iun,*) 'alr=',alr,r0(alr,jexp)/r0s(alr,jexp),flag
               endif
            enddo
         enddo
      endif
      end


      subroutine checkcoll(sig,sigc,idir,label,iun)
      implicit none
      integer iun
      include 'pwhg_dbg.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      character *(*) label
      integer idir
      real * 8 xborn(ndiminteg-3),xrad(3)
      integer nexp
      parameter (nexp=8)
      real * 8 jac_over_csi,
     1jac_over_csi_coll,jac_over_csi_soft,r0(maxalr,nexp),
     2r0c(maxalr,nexp),jac_over_csi_p,jac_over_csi_m,
     3 weight(nexp,maxalr),bornweight
      integer j,jexp,alr,alrp
      real * 8 random
      external random
      logical donotdo(maxalr)
      character * 15 flag
      logical valid_emitter,iszero,isnonzero,isequal,bad_born_kin,bad_real_kin
      external valid_emitter
      real * 8 grealsupp,gbornsupp
c     The tolpar parameter sets the minimum in the ratio (transverse momentum)/(total energy)
c     for a kinematic configuration to be accepted for collinear tests. It is started
c     at 1, and for each failed configuration it is reduced by a factor 0.95 until an
c     acceptable configuration is found
      real * 8 tolpar
      tolpar = 1
 19   continue
      tolpar = tolpar * 0.95d0
      do alr=1,flst_nalr
c only radiated gluons or photons
c and only in current resgroup (borns are zero otherwise)
         if( 
     2        flst_ibornresgroup .ne. flst_bornresgroup(flst_alr2born(alr))
     3        .or. kn_emitter .ne. flst_emitter(alr)) then
            donotdo(alr) = .true.
         else
            donotdo(alr)=.false.
         endif
      enddo
      do j=1,ndiminteg-3
         xborn(j)=random()
      enddo
      call gen_born_phsp(xborn)
      if(bad_born_kin(tolpar)) goto 19
      call setscalesbtilde
      call allborn
      call global_suppression('b',gbornsupp)
      tolpar = 1
 29   continue
      tolpar = tolpar * 0.95d0

      do j=1,3
         xrad(j)=random()
      enddo
      if(valid_emitter(kn_emitter)) then
         do jexp=1,nexp
            if(idir.ne.-1) then
               xrad(2)=10d0**(-jexp)
            else
               xrad(2)=1-10d0**(-jexp)
            endif
            if(kn_emitter.gt.2) then
               call gen_real_phsp_fsr(xrad,jac_over_csi,
     1              jac_over_csi_coll,jac_over_csi_soft)
            else
               call gen_real_phsp_isr
     1              (xrad,jac_over_csi,jac_over_csi_p,jac_over_csi_m,
     2              jac_over_csi_soft)
            endif
            if(jexp == 1) then
               if(bad_real_kin(tolpar)) goto 29
               write(iun,*) ' Random Born variables ====> ',xborn
               write(iun,*) ' Random radiation variables ====> ',xrad
            endif
            call global_suppression('r',grealsupp)
            write(iun,*) ' checkcoll, jexp=',jexp, ' realsupp/bornsupp',grealsupp/gbornsupp
            write(iun,*) '######### Check coll',xrad(2)
            call sig(r0(1,jexp))
            call sigc(r0c(1,jexp))
            do alr=1,flst_nalr
               if(.not.donotdo(alr)) then
                  call realresweight(alr,weight(jexp,alr))
               endif
            enddo
         enddo

         do alr=1,flst_nalr
            call bornresweight(flst_alr2born(alr),bornweight)
            if(donotdo(alr)) cycle
            write(10,*) '---',alr
            do jexp=1,nexp
               write(10,*) ' coll. weights: ',weight(jexp,alr),' born:',
     1             bornweight, ' born/coll. weights:',
     2              bornweight/weight(jexp,alr)
               if(r0c(alr,jexp).ne.r0c(alr,1)) then
                  write(iun,*)
     1                 ' checklims error : coll lim depends upon coll variable'
               endif
            enddo
         enddo
         do alr=1,flst_nalr
            if(donotdo(alr)) cycle
            write(iun,'(2a,i2,a,i4,a,20(1x,i3))') label,'  emitter ',
     1           kn_emitter,', alr=',alr,', process ',(flst_alr(j,alr),j=1,flst_ireallength)
            do alrp=alr+1,flst_nalr
               if(donotdo(alrp)) cycle
               isequal=.true.
               do jexp=1,nexp
                  if(r0(alr,jexp).ne.r0(alrp,jexp).or.
     #r0c(alr,jexp).ne.r0c(alrp,jexp)) isequal=.false.
               enddo
               if(isequal) then
c     write(iun,'(2a,i2,a,20(1x,i3))') label,' emitter ',
c     # kn_emitter,', process ',(flst_alr(j,alrp),j=1,flst_ireallength)
                  write(iun,'(2a,i2,a,20(1x,i3))') label,' emitter ',
     1                 flst_emitter(alrp),', process ',(flst_alr(j,alrp),j=1,nlegreal)
                  write(iun,'(2a,i2,a,20(1x,i3))') ' ==  ',' emitter ',
     1                 flst_emitter(alr),', process ',(flst_alr(j,alr),j=1,nlegreal)
                  donotdo(alrp)=.true.
               endif
            enddo
            do jexp=1,nexp
               call setwarnflag(r0c(alr,jexp),r0(alr,jexp),
     1              jexp,1,flag)
c     Added this 'if' to be sure that no division by zero occurs
c     if((r0(alr,jexp-1)-r0c(alr,jexp-1)).ne.0d0) then
c     write(iun,*) (r0(alr,jexp)-r0c(alr,jexp))/
c     #(r0(alr,jexp-1)-r0c(alr,jexp-1)),r0c(alr,jexp)/r0(alr,jexp),flag
c     endif
               if(r0c(alr,jexp) == 0 .or. r0(alr,jexp) /= r0(alr,jexp)
     1              .or. r0c(alr,jexp) /= r0c(alr,jexp)) then
                  write(iun,*) 'alr=',alr,r0(alr,jexp),'/',r0c(alr,jexp),flag
               else
                  write(iun,*) 'alr=',alr,r0(alr,jexp)/r0c(alr,jexp),flag
               endif
 1          enddo
         enddo
      endif
      end

      subroutine setwarnflag(r1,r2,jexp,jexpfirst,flag)
      implicit none
      character * 15 flag
      real * 8 r1,r2,dist
      integer jexp,jexpfirst
      if(r1 == 0 .and. r2 /= 0 .or. r1 /= 0 .and. r2 == 0) then
         dist = 1
      elseif(r1 == 0 .and. r2 == 0) then
         dist = 0
      else
         dist = abs(r1/r2-1)
      endif
      flag=' '
      if(dist.gt.0.01) then
         if(jexp.eq.jexpfirst) then
            if(dist.lt.0.1) then
               flag='*-WARN-*'
            else
               flag='*-WWARN-*'
            endif
         elseif(jexp.eq.3) then
            if(dist.lt.0.1) then
               flag='*-WWARN-*'
            else
               flag='*-WWWARN-*'
            endif
         elseif(jexp.ge.4) then
            if(dist.lt.0.1) then
               flag='*-WWWARN-*'
            elseif(dist.lt.0.3) then
               flag='*-WWWWARN-*'
            else
               flag='*-WWWWWARN-*'
            endif
         endif
      endif
      end


      logical function bad_born_kin(tolpar)
      implicit none
      real * 8 tolpar
      include 'pwhg_dbg.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_st.h'
      include 'pwhg_pdf.h'
      logical isnotres(nlegborn)
      real * 8 p(0:3,nlegborn)
      real * 8 pdf(-pdf_nparton:pdf_nparton), save_stmufact2, e
      integer m,l,k
      bad_born_kin = .true.
c     In V2 the resonance structure is the same for all.
      isnotres = .true.
      do k=3,nlegborn
         if(flst_bornres(k,1)/=0) then
            isnotres(flst_bornres(k,1)) = .false.
         endif
      enddo
      l=0    
      do k=1,nlegborn
         if(isnotres(k)) then
            l=l+1
            p(:,l) = kn_cmpborn(:,k)
         endif
      enddo
c     exclude zero pdf's
      e = p(0,1)+p(0,2)
      save_stmufact2=st_mufact2
      st_mufact2 = e**2
      call pdfcall(1,kn_xb1,pdf)
      do k=-3,3
         if(pdf(k) == 0) return
      enddo
      call pdfcall(2,kn_xb2,pdf)
      st_mufact2 = save_stmufact2
      do k=-3,3
         if(pdf(k) == 0) return
      enddo

c     if any transverse momentum is too small, return
      if(l > 3) then ! exclude single resonance production!
         do k=3,l
            if(p(1,k)**2+p(2,k)**2 < (e*tolpar)**2) return
            if(l > 2 .and. k < l) then
c     any transverse momentum of a pair is too small
               do m=k+1,l
                  if((p(1,k)+p(1,m))**2+(p(2,k)+p(2,m))**2
     1                 < (e*tolpar)**2) return
               enddo
            endif
         enddo
      endif
      bad_born_kin = .false.
      end

      logical function bad_real_kin(tolpar)
      implicit none
      real * 8 tolpar
      include 'pwhg_dbg.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_st.h'
      include 'pwhg_pdf.h'
      logical isnotres(nlegreal)
      real * 8 p(0:3,nlegreal)
      real * 8 pdf(-pdf_nparton:pdf_nparton), save_stmufact2, e
      integer m,l,k
      
      bad_real_kin = .true.
c     In V2 the resonance structure is the same for all.
      isnotres = .true.
      do k=3,nlegreal
         if(flst_realres(k,1)/=0) then
            isnotres(flst_realres(k,1)) = .false.
         endif
      enddo
      l=0    
      do k=1,nlegreal
         if(isnotres(k)) then
            l=l+1
            p(:,l) = kn_cmpreal(:,k)
         endif
      enddo
c     exclude zero pdf's
      e = p(0,1)+p(0,2)
      save_stmufact2=st_mufact2
      st_mufact2 = e**2
      call pdfcall(1,kn_x1,pdf)
c tolerate zero pdf only for heavy quarks
      do k=-3,3
         if(pdf(k) == 0) return
      enddo
      call pdfcall(2,kn_x2,pdf)
      st_mufact2 = save_stmufact2
      do k=-3,3
         if(pdf(k) == 0) return
      enddo

c     if any transverse momentum is too small, return
      if(l > 3) then ! exclude single resonance production!
         do k=3,l
            if(p(1,k)**2+p(2,k)**2 < (e*tolpar)**2) return
            if(l > 2 .and. k < l) then
c     any transverse momentum of a pair is too small
               do m=k+1,l
                  if((p(1,k)+p(1,m))**2+(p(2,k)+p(2,m))**2
     1                 < (e*tolpar)**2) return
               enddo
            endif
         enddo
      endif
      bad_real_kin = .false.
      end

      subroutine sigreal_rad(sig)
      implicit none
      real * 8 sig
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_flg.h'
      include 'pwhg_par.h'
      include 'pwhg_pdf.h'
      include 'pwhg_cache.h'
      type(cache_pointer), save :: cacheptr
      integer, save :: cacheind
      real * 8 coef
      logical filled(flst_nalr)
      integer jalr

      real * 8 r0(flst_nalr),rc(flst_nalr),rs(flst_nalr),rcs(flst_nalr),
     1         dampandcuts(flst_nalr)
      integer alr,alrpr,iret,em
      integer j,k
      real * 8 dampfac,weight,r
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton)
      real * 8 ptsq,pwhg_pt2
      logical condition
      logical ini
      data ini/.true./
      save ini
      external pwhg_pt2
      integer alrlen
      if(ini) then
         if(flg_smartsig) then
            call init_cache_similar('sigreal_rad',flst_nalr)
            call get_cache_pointer('sigreal_rad',cacheind,cacheptr)
         endif
         ini=.false.
      endif
c End initialization phase; compute graphs
      r0 = 0
      dampandcuts = 1
      call pdfcall(1,kn_x1,pdf1)
      call pdfcall(2,kn_x2,pdf2)
      if(flg_withdamp) then
         call collrad(rc)
         call collsoftrad(rcs)
         call softrad(rs)
      endif
      filled = .false.
      do j=1,rad_alr_nlist
         alr=rad_alr_list(j)
         em=flst_emitter(alr)
         alrlen=flst_alrlength(alr)
c check if emitter corresponds to current radiation region (i.e. rad_kinreg):
         if((rad_kinreg.eq.1.and.em.le.2).or.(em.gt.2.and.
     #       flst_lightpart+rad_kinreg-2.eq.em))then
c check if we have a g -> Q Qbar splitting below threshold:
            if(em.gt.0) then
               if(flst_alr(em,alr)+flst_alr(alrlen,alr).eq.0.and.
     #abs(flst_alr(em,alr)).ge.4) then
                  ptsq=pwhg_pt2()
                  if(abs(flst_alr(em,alr)).eq.4
     #  .and.ptsq.lt.rad_charmthr2.or.
     # abs(flst_alr(em,alr)).eq.5.and.ptsq.lt.rad_bottomthr2) then
                     dampandcuts(alr)=0
                  endif
               endif
            endif
            if(flg_smartsig) then
               call get_cache_value(cacheptr,alr,jalr,coef)
            else
               jalr = - 1
            endif
            if(jalr.lt.0) then
               if(kn_emitter.eq.0) then
                  kn_resemitter=0
               else
                  kn_resemitter=flst_alrres(alrlen,alr)
               endif
               flst_cur_alr = alr
               call realgr(flst_alrlength(alr),flst_alr(:,alr),
     1              flst_alrres(:,alr),kn_cmpreal,r0(alr))
               call realresweight(alr,weight)
               r0(alr)=r0(alr)*weight
               if(em.gt.2) then
                  if(flg_doublefsr) then
c    supply a factor E_em/(E_em+E_rad), times 2 if both gluons
                     r0(alr)=r0(alr)
     1                    *kn_cmpreal(0,kn_emitter)**par_2gsupp/
     2                    (kn_cmpreal(0,kn_emitter)**par_2gsupp
     3                    +kn_cmpreal(0,alrlen)**par_2gsupp)
                     if(flst_alr(kn_emitter,alr).eq.0.and.
     1                    flst_alr(alrlen,alr).eq.0) then
                        r0(alr)=r0(alr)*2
                     endif
                  else
c     If the emitter is in the final state, and if the emitted and emitter
c     are both gluons, supply a factor E_em/(E_em+E_rad) * 2
                     if(flst_alr(kn_emitter,alr).eq.0.and.
     1                    flst_alr(alrlen,alr).eq.0) then
                        r0(alr)=r0(alr)*2
     1                       *kn_cmpreal(0,kn_emitter)**par_2gsupp/
     2                       (kn_cmpreal(0,kn_emitter)**par_2gsupp
     3                       +kn_cmpreal(0,alrlen)**par_2gsupp)
                     endif
                  endif
               endif
               r0(alr)=r0(alr)*flst_alrmult(alr)
               filled(alr)=.true.
            else
               if(coef == 0) then
                  r0(alr) = 0
               elseif( .not. filled(jalr)) then
                  write(*,*) ' sigreal_rad: smartsig machinery failure ...'
                  write(*,*) ' exiting ...'
               else
                  r0(alr)=r0(jalr)*coef
               endif
               filled(alr)=.true.
            endif
c supply Born zero damping factor, if required
            if(flg_withdamp) then
               dampfac = 0
               if(em > 2) then
                  if(kn_masses(em) > 0) then
                     dampfac = 1
                  endif
               endif
               if(dampfac == 0) then
                  r=r0(alr)
                  call bornzerodamp(alr,r,rc(alr),rs(alr),rcs(alr),
     1                 dampfac)
                  dampandcuts(alr)=dampandcuts(alr) * dampfac
               endif
            endif
c supply real damping factor, if required
            flst_ireallength = flst_alrlength(alr)            
            call global_suppression('r',dampfac)
            dampandcuts(alr)=dampandcuts(alr) * dampfac
         else
            r0(alr)=0
         endif
      enddo

      if(flg_smartsig) then
         call store_cache_similar(cacheptr,r0,filled)
      endif

      sig=0
      do j=1,rad_alr_nlist
         alr=rad_alr_list(j)
         if(r0(alr).ne.0) then
            r0(alr)=r0(alr) * dampandcuts(alr) * pdf1(flst_alr(1,alr))*pdf2(flst_alr(2,alr))
            sig=sig+r0(alr)
            rad_real_arr(j)=r0(alr)
         else
            rad_real_arr(j)=0
         endif
      enddo
      end


      subroutine sigreal_btl(r0)
      implicit none
      real * 8 r0(*)
      call sigreal_btl0(r0,0)
      end

c Real cross section, required by btilde;
c fills the array r0(alr) with the invariant cross section, multiplied
c by csi^2 (1-y^2) for ISR regions
c    csi^2 (1-y)   for FSR regions
      subroutine sigreal_btl0(r0,imode)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      include 'pwhg_par.h'
      include 'pwhg_pdf.h'
      include 'pwhg_cache.h'
      type(cache_pointer), save :: cacheptr
      integer, save :: cacheind
      real * 8 coef
      logical filled(flst_nalr)
      integer jalr

      integer imode
      real * 8 r0(flst_nalr)
      real * 8 rc(flst_nalr),rs(flst_nalr),rcs(flst_nalr),
     1     dampandcuts(flst_nalr),r
      integer alr,alrpr,iret
      integer j,k
      real * 8 dampfac,weight
      real * 8 pdf1(-pdf_nparton:pdf_nparton),
     1         pdf2(-pdf_nparton:pdf_nparton)
      real * 8 rescfac
      logical ini
      data ini/.true./
      save ini
      integer alrlen
      common/calr/alr
      save/calr/
      if(ini) then
         if(flg_smartsig) then
            call init_cache_similar('sigreal_btl0',flst_nalr)
            call get_cache_pointer('sigreal_btl0',cacheind,cacheptr)
         endif
         ini=.false.
      endif
c End initialization phase; compute graphs
      r0 = 0
      dampandcuts = 1
      if(flg_withdamp) then
         call collbtl(rc)
         call collsoftbtl(rcs)
         call softbtl(rs)
      endif
      filled = .false.
      do alr=1,flst_nalr
c Only R_alpha (namely alr) with the current emitter: 
         if(flst_emitter(alr).eq.kn_emitter
     1    .and. flst_bornresgroup(flst_alr2born(alr)) .eq. flst_ibornresgroup) then
            if(flg_smartsig) then
               call get_cache_value(cacheptr,alr,jalr,coef)
            else
               jalr = - 1
            endif
            if(jalr.lt.0) then
c Not equal to any previous one, compute explicitly.
c First mark as being computed
               filled(alr)=.true.
               if(kn_emitter.eq.0) then
                  kn_resemitter=0
               else
                  kn_resemitter=flst_alrres(flst_alrlength(alr),alr)
               endif
               flst_cur_alr = alr
               call realgr(flst_alrlength(alr),flst_alr(:,alr),
     1              flst_alrres(:,alr),kn_cmpreal,r0(alr))
               call realresweight(alr,weight)
               r0(alr)=r0(alr)*weight
c If the emitter is in the final state, and if the emitted and emitter
c are both gluons, supply a factor E_em/(E_em+E_rad) * 2
               alrlen = flst_alrlength(alr)
               if(kn_emitter.gt.2) then
                  if(flg_doublefsr) then
c    supply a factor E_em/(E_em+E_rad), times 2 if both gluons
                     r0(alr)=r0(alr)
     1                    *kn_cmpreal(0,kn_emitter)**par_2gsupp/
     2                    (kn_cmpreal(0,kn_emitter)**par_2gsupp
     3                    +kn_cmpreal(0,alrlen)**par_2gsupp)
                     if(flst_alr(kn_emitter,alr).eq.0.and.
     1                    flst_alr(alrlen,alr).eq.0) then
                        r0(alr)=r0(alr)*2
                     endif
                  else
c     If the emitter is in the final state, and if the emitted and emitter
c     are both gluons, supply a factor E_em/(E_em+E_rad) * 2
                     if(flst_alr(kn_emitter,alr).eq.0.and.
     1                    flst_alr(alrlen,alr).eq.0) then
                        r0(alr)=r0(alr)*2
     1                       *kn_cmpreal(0,kn_emitter)**par_2gsupp/
     2                       (kn_cmpreal(0,kn_emitter)**par_2gsupp
     3                       +kn_cmpreal(0,alrlen)**par_2gsupp)
                     endif
                  endif
               endif
            else
               if(coef == 0) then
                  r0(alr) = 0
               elseif(.not. filled(jalr) ) then
                  write(*,*) ' error: sigreal_btl flg_smartsig bug'
                  call exit(-1)
               else
                  r0(alr)=r0(jalr)*coef
               endif
               filled(alr)=.true.
            endif
c supply Born zero damping factor, if required
            if(flg_withdamp) then
c
               dampfac = 0
               if(kn_emitter .gt. 2) then
                  if(kn_masses(kn_emitter) .gt. 0) then
c no bornzerodamp with massive emitter
                     dampfac = 1
                  endif
               endif
               if(dampfac == 0) then
                  if(kn_emitter.gt.2) then
                     r=r0(alr)*(1-kn_y)*kn_csi**2
                  else
                     r=r0(alr)*(1-kn_y**2)*kn_csi**2
                  endif
                  r=r*flst_alrmult(alr)
                  call bornzerodamp(alr,r,rc(alr),rs(alr),rcs(alr),
     1                 dampfac)
               endif
               if(imode.eq.0) then
                  dampandcuts(alr) =dampandcuts(alr) * dampfac
               elseif(imode.eq.1) then
                  dampandcuts(alr) =dampandcuts(alr) * (1-dampfac)
               else
                  write(*,*) ' sigreal_btl0: improper call'
               endif
            endif
c supply real damping factor, if required
            flst_ireallength = flst_alrlength(alr)            
            call global_suppression('r',dampfac)
            dampandcuts(alr)=dampandcuts(alr) * dampfac            
         endif
      enddo

      if(flg_smartsig) then
         call store_cache_similar(cacheptr,r0,filled)
      endif

      if(.not.flg_minlo) then
         rescfac = 1
         call pdfcall(1,kn_x1,pdf1)
         call pdfcall(2,kn_x2,pdf2)
      endif
      do alr=1,flst_nalr
         if(flg_minlo) then
            flg_minlo_real=.true.
            call setlocalscales(flst_alr2born(alr),2,rescfac)
            flg_minlo_real=.false.
            call pdfcall(1,kn_x1,pdf1)
            call pdfcall(2,kn_x2,pdf2)
         endif
         r0(alr)=r0(alr)*flst_alrmult(alr)
         if(kn_emitter.gt.2) then
            r0(alr)=r0(alr)*(1-kn_y)*kn_csi**2
         else
            r0(alr)=r0(alr)*(1-kn_y**2)*kn_csi**2
         endif
c include pdf's
         r0(alr)=r0(alr) * dampandcuts(alr) * rescfac *
     1        pdf1(flst_alr(1,alr))*pdf2(flst_alr(2,alr))
      enddo
      end

      subroutine realgr(rlength,rflav,rres,p,res)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer rlength
      integer rflav(nlegreal)
      integer rres(nlegreal)
      real * 8 p(0:3,nlegreal),res
      call real_ampsq(p,rlength,rflav,rres,res)
c flux factor
      res=res/(8*p(0,1)*p(0,2))
      if(res.eq.0) then
c         write(*,*) 'realgr:', rflav
         continue
      endif
      end



      subroutine real_ampsq(p,rlength,rflav,rres,amp2)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_math.h'
      include 'pwhg_st.h'
      real * 8 p(0:3,nlegreal)
      integer rlength
      integer rflav(nlegreal)
      integer rres(nlegreal)
      real * 8 amp2 
      logical pwhg_isfinite
      external pwhg_isfinite      
      real * 8 p0(0:3,flst_numfsb+3)
      integer rflav0(flst_numfsb+3)
      integer is_fs(nlegreal),isfslength
      integer i,j

      call getisfsparticles(rlength,rflav,rres,isfslength,is_fs)

      if(flst_numfsb+3 /= isfslength) then
         write(*,*) ' real_ampsq: length mismatch in arrays'
         call exit(-1)
      endif

      do j=1,isfslength
         rflav0(j)=rflav(is_fs(j))
         p0(:,j)=p(:,is_fs(j))
      enddo      
      call setreal(p0,rflav0,amp2)
c     check if amp2 is finite
      if (.not.pwhg_isfinite(amp2)) amp2=0d0
      amp2 = amp2*st_alpha/(2*pi)
      end
