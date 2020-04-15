      subroutine pwhgevent
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_em.h'
      include 'pwhg_rwl.h'
      include 'LesHouches.h'
      character * 10 id
      integer iret,iun
      real * 8 suppfact
      real * 8 random,powheginput
      external random,powheginput
      integer mcalls,icalls
      data mcalls,icalls/0,0/
      save mcalls,icalls
      real * 8 pwhg_pt2,pt2max_regular
      external pwhg_pt2,pt2max_regular
      real * 8 weight
      integer i,iind
      integer conta
      data conta/0/
      save conta
      integer cconta
      common/ccconta/cconta
      real * 8 seconds,dummy
      integer lh_seed,lh_n1,lh_n2
      common/lhseeds/lh_seed,lh_n1,lh_n2
      logical, save :: ini = .true.
      flg_monitorubound = .true.
c If at the end the event is not generated for some reason (nup=0)
c restart from here
 1    continue
      if(idwtup.eq.3) then
         weight=1
      elseif(idwtup.eq.-4) then
         call computetotgen(rad_totgen)
         weight=rad_totgen * rad_branching
      else
         write(*,*) ' only 3 and -4 are allowed for idwtup'
         call exit(-1)
      endif
c     store current random seeds. To be used to restart at problematic events
      if(ini) then
         ini = .false.
         if(powheginput("#whichpwhgevent") == 1) then
            write(*,*) 'enter random seed, n1, n2'
            read(*,*) lh_seed,lh_n1,lh_n2
            call setrandom(lh_seed,lh_n1,lh_n2)
         endif
      endif

      conta=conta+1
      cconta=conta
      
      call readcurrentrandom(lh_seed,lh_n1,lh_n2)
c     The 1-random() makes it binary compatible with V2, when possible,
c     i.e. when no regulars and no resonances
      call chooseid(1-random(),id)
      if(id.eq.'btilde') then
c     generate underlying Born kinematics
         call reset_timer

         
         call gen_btilde(mcalls,icalls)
         call get_timer(seconds)
         call addtocnt('btilde time (sec)',seconds)
c     generate underlying Born flavour
         call gen_btilde_subp
         iind = rad_ubornsubp
c
         if(powheginput('#testsuda').eq.1) then
            call testsuda
         endif
         if(.not.flg_LOevents) then
c generate radiation
            call reset_timer
            call gen_radiation
            call get_timer(seconds)
            call addtocnt('radiation time (sec)',seconds)
         else
c this call set to zero the number of stored radiations
            call handle_radiations('reset',0,0d0,0d0,0d0,0d0)
         endif
c --- set up les houches interface
         call gen_leshouches('btilde')
c rad_type=1 for btilde events (used only for debugging purposes)
         rad_type=1
         call increasecnt("btilde event")
         rwl_type = rad_type
         rwl_index = rad_ubornsubp
         call mintwrapper_result('btilde',rad_ubornsubp,rwl_weight)
      elseif(id.eq.'remn') then
c     generate remnant n+1 body cross section
         call reset_timer
         call gen_sigremnant
         call get_timer(seconds)
         call addtocnt("remnant time (sec)",seconds)
c     this usless call to random makes it even with V2.
c     In V2 there is an extra call to random() to choose between regulars
c     and remnants, even if regulars are not present.
         dummy = random()
         call gen_remnant_subp
         iind = rad_alrsubp
         if (em_rad_on) then
            rad_pt2max=max(rad_ptsqmin_em,pwhg_pt2())
         else
            rad_pt2max=max(rad_ptsqmin,pwhg_pt2())
         endif
         call set_rad_scales(rad_pt2max)
         call gen_leshouches('remn')
c     rad_type=2 for remnants
         rad_type=2
         call increasecnt("remnant event")
         rwl_type = rad_type
         rwl_index = rad_alrsubp
         call mintwrapper_result('remn',rad_alrsubp,rwl_weight)
      elseif(id.eq.'reg') then
         call reset_timer
         call gen_sigregular(iret)
         call get_timer(seconds)
         call addtocnt("regular time (sec)",seconds)
         call gen_regular_subp
         iind = rad_regularsubp
c     set st_muren2 for scalup value for regular contributions
         if (em_rad_on) then
            rad_pt2max=max(rad_ptsqmin_em,pt2max_regular())
         else
            rad_pt2max=max(rad_ptsqmin,pt2max_regular())
         endif
         call set_rad_scales(rad_pt2max)
         call gen_leshouches_reg
c     rad_type=3 for regular contributions
         rad_type=3
         call increasecnt("regular event")
         rwl_type = rad_type
         rwl_index = rad_regularsubp
         call mintwrapper_result('reg',rad_regularsubp,rwl_weight)
      else
         write(*,*) ' pwhgevent: got id='//trim(id)//', cannot handle'
         write(*,*) ' exiting ...'
      endif

c     add a random azimuthal rotation around beam axis to the Les Hoches momenta
      call add_azimuth_lh

      if(flg_weightedev) then
         if(id.eq.'btilde') then
            call born_suppression(suppfact)
            if(suppfact.eq.0) then
               write(*,*) ' 0 suppression factor in event generation'
               write(*,*) ' aborting'
               call exit(-1)
            endif
            weight=weight/suppfact
         elseif(id.eq.'remn') then
            call rmn_suppression(suppfact)
            if(suppfact.eq.0) then
               write(*,*) ' 0 suppression factor in event generation'
               write(*,*) ' aborting'
               call exit(-1)
            endif
            weight=weight/suppfact
         elseif(id.eq.'reg') then
            call regular_suppression(suppfact)
            if(suppfact.eq.0) then
               write(*,*)
     1              ' 0 suppression factor in regular event generation'
               write(*,*) ' aborting'
               call exit(-1)
            endif
            weight=weight/suppfact
         endif
      endif
c if negative weight, flip the sign of weight
      call mintwrapper_sign_result(id,iind,weight)
c     correct for bound violations
      if(flg_ubexcess_correct) then
         weight = weight * rad_genubexceeded
      endif
c If at the end the event is not generated for some reason (nup=0)
c restart from here
      if(nup.eq.0) goto 1
      xwgtup = weight
      end


      subroutine gen_radiation
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flg.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_em.h'
      real * 8 t,csi,y,azi,sig,born
      real * 8 tmax
      common/ctmax/tmax
      integer kinreg,firstreg,lastreg,fl1,fl2,flemitter
      logical ini,fixed_region
      data ini/.true./
      real * 8 pwhg_pt2,powheginput
      external pwhg_pt2,powheginput
      save ini,fixed_region,firstreg,lastreg
      logical is_charged,is_coloured
      external is_charged,is_coloured

c      integer i1
c      write(*,*)"in gen_radiation",flst_born(:,rad_ubornsubp)
c      do i1=1,flst_bornlength(rad_ubornsubp)
c         write(*,*)kn_pborn(:,i1)
c      enddo
      
      if(ini) then
c when resonances are there, selecting a specific region does
c not make a lot of sense, since the same emission may come
c from different resonances
         firstreg=powheginput("#radregion")
         if(firstreg.le.0) then
            firstreg=1
            lastreg=rad_nkinreg
            fixed_region = .false.
         else
            fixed_region = .true.
            lastreg=firstreg
         endif
         ini=.false.
      endif
      if(.not.fixed_region .and. rad_nkinreg /= lastreg) then
         write(*,*) ' gen_radiation: warning, number of radiation regions'
         write(*,*) ' is not constant!'
         lastreg = rad_nkinreg
      endif
c initialize storing of generated radiation parameters
      call handle_radiations('reset',0,0d0,0d0,0d0,0d0)
c Use highest bid procedure (see appendix B of FNO2006)
      tmax=0
      do rad_kinreg=firstreg,lastreg
         if(rad_kinreg_on(rad_kinreg)) then
            if(rad_kinreg.eq.1) then
c     initial state radiation
c kn_emitter may be 0,1,2 depending upon the flavour
c of the process, which is undefined here.
c Set it to a value less than 2, to avoid problems later.
               kn_emitter = 0
               fl1=flst_born(1,rad_ubornsubp)
               fl2=flst_born(2,rad_ubornsubp)
               if((.not.is_coloured(fl1).and..not.is_coloured(fl2))
     1          .and.(is_charged(fl1).or.is_charged(fl2))) then
c     For processes with partons (colored)  in the initial state, we never enter here. 
c     Only when a lepton is incoming, the following apply
                  write(*,*) 'Initial-state not-coloured charged '//
     $                 'particle'
                  write(*,*) 'ISR upper bound not yet implemented'
                  call pwhg_exit(-1)
c                  em_rad_on = .true.
               else
                  if (flg_QEDonly) then
c     in this case, ONLY real diagrams with photon radiation should be active in the 
c     init_processes.f file.     NO QCD radiation at all
                     em_rad_on = .true.
                  else
                     em_rad_on = .false.
                  endif
               endif
               call gen_rad_isr(t)
            else
c     final state radiation
               kn_emitter=flst_lightpart+rad_kinreg-2
               flemitter=flst_born(kn_emitter,rad_ubornsubp)

               if(.not.is_coloured(flemitter).and.is_charged(flemitter))
     1              then
                  em_rad_on = .true.
               else
                  em_rad_on = .false.
               endif
c.....MAURO ADDED
               if (flg_QEDonly) then
c     in this case, ONLY real diagrams with photon radiation should be active in the 
c     init_processes.f file.     NO QCD radiation at all
                  em_rad_on = .true.
               else
                  em_rad_on = .false.
               endif
c.....MAURO ADDED               
               call gen_rad_fsr(t)
            endif
            if(.not.flg_allrad) then
               if(t.lt.tmax) then
                  cycle
               else
c the gen_rad_* routines stop iterating if t goes below tmax, thus
c saving time. This can be used unless allrad is on.
                  tmax = t
               endif
            endif
            if(t.gt.0) then
               call gen_rad_subp
c radiation parameters are stored in an array.
c The corresponding phase space will be rebuilt when the Les Houches event is
c generated.
               call handle_radiations('save',rad_alrsubp,t,kn_csi,kn_y,kn_azi)
            endif
         endif
      enddo
      end



      function pwhg_pt2()
      implicit none
      real * 8 pwhg_pt2
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      real * 8 pres(0:3),q2
      integer em,ires
      if(rad_kinreg.eq.1) then
         pwhg_pt2=(kn_sreal/4)*(1-kn_y**2)*kn_csi**2
      else
         em=flst_lightpart+rad_kinreg-2
         if(kn_masses(em).eq.0) then
            if(flst_bornrescurr(em).ne.0) then
               ires=flst_bornrescurr(em)
               pres=kn_cmpborn(:,ires)
               q2=pres(0)**2-pres(1)**2-pres(2)**2-pres(3)**2
            else
               q2=kn_sreal
            endif
            pwhg_pt2=(q2/2)*(1-kn_y)*kn_csi**2
         else
c comppt2fsrmv takes care of choosing the appropriate frame if the emitter
c (computed acccording to rad_kinreg) is a resonance
            call comppt2fsrmv(kn_y,kn_csi,pwhg_pt2)
         endif
      endif
      end

      function pwhg_upperb_rad()
      implicit none
      real * 8 pwhg_upperb_rad
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_st.h'
      include 'pwhg_em.h'
      real * 8 x,y,csi
      integer em
      csi=kn_csi
      x=1-csi
      y=kn_y
      if(rad_kinreg.eq.1) then
         if (em_rad_on) then
            if(rad_iupperisr.eq.1) then
               pwhg_upperb_rad = 1/((1-x)*(1-y**2))
            endif
         else   
            if(rad_iupperisr.eq.1) then
               pwhg_upperb_rad = 1/((1-x)*(1-y**2))
c     Possible alternatives:
c     rad_iupper=2   pwhg_upperb_rad = 1/(x*(1-x)*(1-y**2))
c     
c     rad_iupper=3:  pwhg_upperb_rad = 1/(x**2*(1-x)*(1-y**2))
            else
               write(*,*) ' rad_iupper=',rad_iupperisr,
     1              'alternative not implemented'
               call pwhg_exit(1)
            endif
         endif   
      else
c     Final state radiation
         em=flst_lightpart+rad_kinreg-2
         if(kn_masses(em).eq.0) then
c     for now use the same
            if (em_rad_on) then
               pwhg_upperb_rad = 1/(csi*(1-y))
            else
               if(rad_iupperfsr.eq.1) then
                  pwhg_upperb_rad = 1/(csi*(1-y))
               elseif(rad_iupperfsr.eq.2) then
                  pwhg_upperb_rad = 1/(csi**2*(1-y)*(1-csi/2*(1-y))**2)
     2                 *csi
               elseif(rad_iupperfsr.eq.3) then
                  pwhg_upperb_rad = 1/(csi*(1-y)*
     2                 (1-csi/2*(1-y)))
               else
                  write(*,*) ' rad_iupper=',rad_iupperfsr,
     1                 'alternative not implemented'
                  call pwhg_exit(1)
               endif
            endif
         else
c     massive emitter
            call compubradmv(y,csi,pwhg_upperb_rad)
         endif
      endif
      if(em_rad_on) then
         pwhg_upperb_rad = pwhg_upperb_rad * em_alpha
      else
         pwhg_upperb_rad = pwhg_upperb_rad * st_alpha
      endif

      end



      function pt2solve(pt2,i)
c Returns  xlr - log(Delta^{(tilde{V})}) , see eq. D14, D15 in ZZ paper
c We use it to find its zero in pt2.
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_em.h'
      include 'pwhg_rad.h'
      include 'pwhg_math.h'
      real * 8 pt2solve,pt2
c i set by dzero: 1 for first call, 2 for subsequent calls, 3 for last call
c before a normal exit; not used here
      integer i,em
      real * 8 xlr,q2,xlam2c,kt2max,unorm,cunorm,sborn
      integer nlc
      common/cpt2solve/xlr,q2,kt2max,xlam2c,unorm,sborn,nlc
      real * 8 b0,xm,p,tmp
      real * 8 ddilog

      integer conta
      data conta/0/
      save conta
      
      b0=(11*CA-4*TF*nlc)/(12*pi)
      if(em_rad_on) then
         cunorm=unorm*em_alpha
      else
         cunorm=unorm
      endif
      if(rad_kinreg.eq.1) then
         if (em_rad_on) then
            pt2solve=cunorm*pi*(ddilog(-sborn/kt2max)-ddilog(-sborn/pt2)) + xlr
         else         
            if(rad_iupperisr.eq.1) then
c see Notes/upperbounding-isr.pdf
               if(pt2.lt.sborn) then
                  if(sborn.lt.kt2max) then
                     pt2solve=cunorm*pi/b0*(
     $                    (log(2*sborn/xlam2c)*log(log(sborn/xlam2c)/log(pt2/xlam2c))
     $                    - log(sborn/pt2)) +
     $                    log(2d0)*log(log(kt2max/xlam2c)/log(sborn/xlam2c)))
     $                    + xlr
                  else
                     pt2solve=cunorm*pi/b0*(
     $                    (log(2*sborn/xlam2c)*log(log(kt2max/xlam2c)/log(pt2/xlam2c))
     $                    - log(kt2max/pt2)) )
     $                    + xlr
                  endif
               else
                  pt2solve=cunorm*pi/b0*(log(2d0)
     $                 *log(log(kt2max/xlam2c)/log(pt2/xlam2c)))
     $                 + xlr
               endif
            else
               write(*,*) ' rad_iupper=',rad_iupperisr,
     +          ' not implemented'
               call pwhg_exit(1)
c     Alternatives: rad_iupper=2
c     pt2solve=cunorm*pi/b0/2
c     #        *(log(q2/xlam2c)*log(log(kt2max/xlam2c)/log(pt2/xlam2c))
c     #        - log(kt2max/pt2)) + xlr
            endif
         endif
      else
         em = flst_lightpart+rad_kinreg-2
         if(kn_masses(em).ne.0) then
            call compintub(pt2,pt2solve)
c The following lines are used to test the analytic integration
c versus a vegas one; uncomment to test
c            call compintubveg(pt2,tmp)
c            write(*,'(a,3(1x,d10.4))') ' testintub:',pt2,pt2solve,tmp
            pt2solve=cunorm*pt2solve+xlr
         else
            
            if (em_rad_on) then
               if(rad_iupperisr.eq.1) then
                  pt2solve=cunorm*pi/2d0*(log(kt2max/pt2))**2 + xlr
               else
                  write(*,*)
     1    ' rad_iupper=',rad_iupperfsr,' not implemented in photon ISR'
                  call pwhg_exit(1)                  
               endif
            else
               if(rad_iupperfsr.eq.1) then
c final state radiation
                  pt2solve=cunorm*pi/b0*(
     1                 (log(kt2max/xlam2c)*log(log(kt2max/xlam2c)/log(pt2/xlam2c))
     2                 - log(kt2max/pt2)) )
     3                 + xlr
               elseif(rad_iupperfsr.eq.2) then

                  conta=conta+1

                  
                  xm=kn_csimax
                  p=sqrt(pt2/sborn)
                  pt2solve=cunorm*2*pi*2*(
     3                 (log(xm-xm**2)+(2*xm-2)*log(xm)-2*log(1-xm)*xm-2)/xm/2.d+0
     1                 -(p*log(xm-p**2)+(2*p*log(p)-2*log(1-p)*p-2)*xm-2*p*log(p))
     2                 /(p*xm)/2.d+0) + xlr


                  if(kn_csimax.eq.1) stop
                  
               elseif(rad_iupperfsr.eq.3) then
                  xm=kn_csimax
                  p=sqrt(pt2/sborn)
                  pt2solve=cunorm*2*pi*2*(
     3                 (log(xm-xm**2)+(2*xm-2)*log(xm)-2*log(1-xm)*xm-2)/xm/2.d+0
     1                 -(p*log(xm-p**2)+(2*p*log(p)-2*log(1-p)*p-2)*xm-2*p*log(p))
     2                 /(p*xm)/2.d+0) + xlr
               else
                  write(*,*)
     1                 ' rad_iupper=',rad_iupperfsr,' not implemented'
                  call pwhg_exit(1)
               endif            
            endif
         endif
      endif
      end
c'
      subroutine gen_rad_isr(t)
c Generates hard radiation kinematics according to
c appendix D in ZZ paper.
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_st.h'
      include 'pwhg_em.h'
      real * 8 t
      real * 8 x,y,x1b,x2b
      real * 8 xlr,q2,xlam2c,kt2max,unorm,sborn
      integer nlc
      common/cpt2solve/xlr,q2,kt2max,xlam2c,unorm,sborn,nlc
      real * 8 xmin,rv,xp,xm,chi,tk,uk,ubound,ufct,
     #   value,err,tmp1,tmp2,tmp,rvalue,born,sig
      real * 8 ptsqmin
      common/cdfxmin/xmin
      real * 8 tmax
      common/ctmax/tmax
      real * 8 random,pt2solve,dfxmin,pwhg_alphas0,pwhg_upperb_rad
      external random,pt2solve,dfxmin,pwhg_alphas0,pwhg_upperb_rad
      unorm=rad_norms(rad_kinreg,rad_ubornsubp)
      sborn=kn_sborn
      x1b=kn_xb1
      x2b=kn_xb2
c See Notes/kt2max.pdf
      kt2max = sborn*(1-x2b**2)*(1-x1b**2)/(x1b+x2b)**2

c     in order to uniform the treatment of QCD and QED initial-state radiation, 
c     we introduce the following
      if(em_rad_on) then
c     QED
         ptsqmin=rad_ptsqmin_em
         rad_iupperisr=1
      else
c     QCD
         ptsqmin=rad_ptsqmin
      endif

      if(kt2max.lt.ptsqmin.or.kt2max.lt.tmax) then
         t=-1
         goto 3
      endif
c upper bound is log(q2/t)
      if(rad_iupperisr.eq.1) then
         q2=2*sborn
      else
         write(*,*) ' rad_iupper=',rad_iupperisr,' not implemented'
         call pwhg_exit(1)
c Alternative rad_iupper=2
c         q2=4*sborn/min(x1b,x2b)**2
      endif
c see section 4 in ZZ paper, last paragraph
      xlam2c=rad_lamll**2
      nlc=5
      xlr=0
 1    continue
      xlr=xlr+log(random())
c CERNLIB voodoo:
      call KERSET('C205. ',0,0,101)
c solve for zero of pt2solve
c dzero(xmin,xmax,x,err,eps,maxcalls,function)
c err: on exit if no error occours: |y-y0|<err 
c      error C205.1 function(xmin)*function(xmax)>0,
c                   x=0 and r=-2(ymax-ymin)
c      error C205.2 Number of calls to F exceeds maxcalls,
c                   x=0 and r=-(xmax-xmin)/2
c eps: required accuracy
      call dzero(ptsqmin,kt2max,t,err,1d-8,1000000,pt2solve)
c error conditions
      if(t.eq.0.and.err.lt.0d0 .and. err.gt. ptsqmin-kt2max) then
         write(*,*) 'DZERO fails'
         write(*,*) ' number of calls exceeded'
         call exit(1)
      endif
 3    if(t.lt.ptsqmin.or.t.lt.tmax) then
c below cut (either below absolute minimum, or below previously generated
c radiation in highest bid loop): generate a born event
         t=-1
         kn_csi=0
         return
      endif
c vetoes:
      rv=random()
      xp=(sqrt(1+t/sborn)+sqrt(t/sborn))**2
      xm=(sqrt(1+t/sborn)-sqrt(t/sborn))**2
c tmp1: V(t)/tilde{V}(t) in appendix D of ZZ paper;
c (typo: in D.13, log log -> log
      xmin=min(x1b,x2b)/(2*sqrt(1+t/sborn))
      if(em_rad_on) then
         tmp1=log((sqrt(xp-xmin)+sqrt(xm-xmin))
     $        /(sqrt(xp-xmin)-sqrt(xm-xmin)))

         tmp1=tmp1/(log(1+sborn/t)/2)

      else      
         if(rad_iupperisr.eq.1) then
            tmp1=log((sqrt(xp-xmin)+sqrt(xm-xmin))
     $           /(sqrt(xp-xmin)-sqrt(xm-xmin)))
            if(t.lt.sborn) then
               tmp1=tmp1/(log(2*sborn/t)/2)
            else
               tmp1=tmp1/(log(2d0)/2)
            endif
         elseif(rad_iupperisr.eq.2) then
            tmp1=log(2/xmin*(sqrt((xp-xmin)*(xm-xmin))
     $           +1-xmin/2*(xp+xm))/(xp-xm)) /(log(q2/t)/2)
         endif
      endif
c compare with D.11-D.12
c to set xmuren2:
      call set_rad_scales(t)
      if(em_rad_on) then
         tmp2=1d0
      else
         tmp2=st_alpha / pwhg_alphas0(t,rad_lamll,nlc)
      endif
      tmp=tmp1*tmp2
      if(tmp.gt.1) then
         write(*,*)
     +        ' Error: upper bound lower than actual value for ISR',
     #        tmp,tmp1,tmp2,t
         call pwhg_exit(-1)
      endif
      if(rv.gt.tmp) then
         goto 1
      endif
c At this stage: pt generated according to D.2
c generate x proportional to 1/(x sqrt((xp-x)*(xm-x)))
c in the range xmin < x < xm (cf. D.5)
c Generate in d sqrt(xm-x) /sqrt(xp-x)  (rad_iupper=1) or d sqrt(xm-x) /(x sqrt(xp-x)) (rad_iupper=2)
c using       d sqrt(xm-x) /sqrt(xp-xm) (rad_iupper=1) or d sqrt(xm-x) /(xmin sqrt(xp-xm)) (rad_iupper=2) as upper bound using hit and miss
 2    chi=sqrt(xm-xmin)*random()
      x=xm-chi**2
      if(rad_iupperisr.eq.1) then
         if(random().gt.sqrt(xp-xm)/sqrt(xp-x)) goto 2
      elseif(rad_iupperisr.eq.2) then
         if(random().gt.(xmin*sqrt(xp-xm))/(x*sqrt(xp-x))) goto 2
      endif
c get y (abs to avoid tiny negative values)
      y=sqrt(abs(1-4*x/(1-x)**2*t/sborn))
      if(random().gt.0.5d0) y=-y
c At this point an x-y pair is generated according to the
c distribution upper().
c
c Veto if out of range (x1>1 or x2>1)
      tk=-1d0/2*(1-x)*(1-y)
      uk=-1d0/2*(1-x)*(1+y)
      if(   x1b*sqrt((1+tk)/(1+uk)/x) .gt. 1
     # .or. x2b*sqrt((1+uk)/(1+tk)/x) .gt. 1) then
         goto 1
      endif
c extra suppression factor of upper bounding function (may depend upon radiation variables)
      call uboundfct(ufct,1-x,y)
      if(random().gt.ufct) goto 1
c Veto from upper bound to real value. Count how many vetoes,
c since these may be expensive.
      call sigborn_rad(born)
      if(born.lt.0) then
         born=0
      endif
      if(born.eq.0) then
c bizarre situation that may arise when the scale gets so low
c that some pdf vanish (typically heavy flavour pdf's)
         t=-1
         goto 3
      endif
      kn_y=y
      kn_csi=1-x
      kn_azi=2*pi*random()
      ubound=born*pwhg_upperb_rad()*unorm*ufct
c     if(flg_newrad) then
      call gen_real_phsp_isr_rad_g
c     else
c     call gen_real_phsp_isr_rad_old
c     endif
      call sigreal_rad(sig)
      value=sig*kn_jacreal
      if(value.gt.ubound) then
         call increasecnt(
     # 'upper bound failures in generation of radiation')
      endif
      rvalue=random()*ubound
      if(rvalue.gt.value) then
         if (em_rad_on) then
            call increasecnt('ISR vetoed photon radiation')
         else
            call increasecnt('ISR vetoed radiation')
         endif
         goto 1
      endif
      end


      subroutine getkt2maxands(kt2,s)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_mvem.h'
      real * 8 kt2,s
c setupmvemitter fixed to works also in the massless case
      call setupmvemitter
      kt2=kt2max
      s=q**2
      end

      subroutine gen_rad_fsr(t)
c Generates final state hard radiation kinematics according to
c Notes/upperbounding-fsr.pdf
      implicit none
      include 'pwhg_math.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      include 'pwhg_kn.h'
      include 'pwhg_rad.h'
      include 'pwhg_st.h'
      include 'pwhg_em.h'
      real * 8 t
      real * 8 csi,y
      real * 8 xlr,q2,xlam2c,kt2max,unorm,sborn
      integer nlc
      common/cpt2solve/xlr,q2,kt2max,xlam2c,unorm,sborn,nlc
      real * 8 xmin,rv,ubound,ufct,
     #   s,value,err,tmp,rvalue,born,sig
      real * 8 ptsqmin
      common/cdfxmin/xmin
      real * 8 tmax
      common/ctmax/tmax
      real * 8 random,pt2solve,pwhg_alphas0,pwhg_upperb_rad,pwhg_pt2
      external random,pt2solve,pwhg_alphas0,pwhg_upperb_rad,pwhg_pt2
      unorm=rad_norms(rad_kinreg,rad_ubornsubp)
c kn_sborn=kn_sreal:
      call getkt2maxands(kt2max,s)
      sborn=s

c     in order to uniform the treatment of QCD and QED final-state radiation, 
c     we introduce the following
      if(em_rad_on) then
c     QED
         ptsqmin=rad_ptsqmin_em
      else
c     QCD
         ptsqmin=rad_ptsqmin
      endif

      if(kt2max.lt.ptsqmin.or.kt2max.lt.tmax) then
         t=-1
         goto 3
      endif

c see section 4 in ZZ paper, last paragraph
      xlam2c=rad_lamll**2
      nlc=5
      xlr=0
 1    continue
      xlr=xlr+log(random())
c CERNLIB voodoo:
      call KERSET('C205. ',0,0,101)
c solve for zero of pt2solve
c dzero(xmin,xmax,x,err,eps,maxcalls,function)
c err: on exit if no error occours: |y-y0|<err 
c      error C205.1 function(xmin)*function(xmax)>0,
c                   x=0 and r=-2(ymax-ymin)
c      error C205.2 Number of calls to F exceeds maxcalls,
c                   x=0 and r=-(xmax-xmin)/2
c eps: required accuracy

      call dzero(ptsqmin,kt2max,t,err,1d-8,1000000,pt2solve)
c     error conditions
      if(t.eq.0.and.err.lt.0d0 .and. err.gt. ptsqmin-kt2max) then
         write(*,*) 'DZERO fails'
         write(*,*) ' number of calls exceeded'
         call exit(1)
      endif
      

 3    if(t.lt.ptsqmin.or.t.lt.tmax) then
c     below cut (either below absolute minimum, or below previously generated
c     radiation in highest bid loop): generate a born event
         t=-1
         kn_csi=0
         return
      endif

c vetoes:
      rv=random()
      call set_rad_scales(t)
      if(em_rad_on) then
         tmp=1
      else
         if(kn_masses(kn_emitter).eq.0) then
            if(rad_iupperfsr.eq.1) then
               tmp=st_alpha / pwhg_alphas0(t,rad_lamll,nlc)
            elseif(rad_iupperfsr.eq.2) then
               tmp=st_alpha
            elseif(rad_iupperfsr.eq.3) then
               tmp=st_alpha
            endif
         else
            tmp=st_alpha
         endif
      endif
      if(tmp.gt.1.000000001d0) then
         write(*,*) ' Error: upper bound lower than actual value for FSR',
     1        tmp,t
c'
         call exit(1)
      endif
      if(rv.gt.tmp) then
         goto 1
      endif

      if(kn_masses(kn_emitter).eq.0) then         
         if (em_rad_on) then
c     same as with rad_iupperfsr.eq.1 (5 lines below)
            rv=random()
            csi=exp(rv*log(t/s)/2+(1-rv)*log(kn_csimax))
            y=1-2*t/(s*csi**2)
         else
            if(rad_iupperfsr.eq.1) then         
c At this stage: pt generated according to (1) of upperbounding-fsr.pdf;
c generate csi uniformly in 1/csi
c in the range t/s < csi^2 < csimax^2
               rv=random()
               csi=exp(rv*log(t/s)/2+(1-rv)*log(kn_csimax))
c get y
               y=1-2*t/(s*csi**2)
c At this point a csi-y pair is generated according to the
c distribution upper(). It is automatically within range.
            elseif(rad_iupperfsr.eq.2) then
c     csi distributed uniformly in 1/(csi-t/s)
               rv=random()
               csi=1/(rv/(sqrt(t/s)-t/s)+(1-rv)/(kn_csimax-t/s))+t/s
c extra csi dependent factor
               if(random().gt.csi) goto 1
c get y
               y=1-2*t/(s*csi**2)
c At this point a csi-y pair is generated according to the
c distribution upper(). It is automatically within range,
c unless we have a massive emitter
            elseif(rad_iupperfsr.eq.3) then
c     csi distributed uniformly in 1/(csi-t/s)
               rv=random()
               csi=1/(rv/(sqrt(t/s)-t/s)+(1-rv)/(kn_csimax-t/s))+t/s
c get y
               y=1-2*t/(s*csi**2)
               if(random().gt.(csi-t/s)) goto 1
            else
               write(*,*) ' gen_rad_fsr:  rad_iupper=',rad_iupperfsr,
     1              ' invalid'
            endif
         endif
      else
c massive emitter case
         rv=random()
         call gencsiymv(t,rv,csi,y)
c Now veto if we are out of range
         if(csi.gt.1) goto 1
      endif
c
c extra suppression factor of upper bounding function (may depend upon radiation variables)
      call uboundfct(ufct,csi,y)
      if(random().gt.ufct) goto 1
c Veto from upper bound to real value. Count how many vetoes,
c since these may be expensive.
c      write(*,*) ' genrad_fsr: y and csi ',y,csi
      call sigborn_rad(born)
      if(born.lt.0) then
         born=0
      endif
      if(born.eq.0) then
c bizarre situation that may arise when the scale gets so low
c that some pdf vanish (typically heavy flavour pdf's)
         t=-1
         goto 3
      endif
      kn_y=y
      kn_csi=csi
      kn_azi=2*pi*random()
      ubound=born*pwhg_upperb_rad()*unorm*ufct
c      if(flg_newrad) then
      call gen_real_phsp_fsr_rad_g
c      else
c     call gen_real_phsp_fsr_rad_old
c      endif
      call sigreal_rad(sig)
      value=sig*kn_jacreal
      if(value.gt.ubound) then
         call increasecnt(
     # 'upper bound failures in generation of radiation')
      endif
      rvalue=random()*ubound
      if(rvalue.gt.value) then
         if (em_rad_on) then
            call increasecnt('FSR vetoed photon radiation')
         else
            call increasecnt('FSR vetoed radiation')
         endif
         goto 1
      endif
      end


      subroutine add_azimuth_lh
      implicit none
      include 'pwhg_math.h'
      include 'LesHouches.h'
      integer ileg
      real * 8 azi,sazi,cazi
      real * 8 dir(3)
      data dir/0d0,0d0,1d0/
      real * 8 random
      external random
      azi=2d0*pi*random()
      sazi = sin(azi)
      cazi = cos(azi)
      do ileg=1, nup
         call mrotate(dir,sazi,cazi,pup(1:3,ileg))
      enddo
      end
      

      subroutine handle_radiations(mode,alr,t,csi,y,azi)
c Stores the radiation parameters of e newly found radiation
c mode      Action
c 'reset'   Restarts a new event
c 'save'    Saves radiation parameters for a generated radiation (in gen_radiation) 
c 'inquire' Returns in the second parameter (alr) the number of stored radiations
c 'next'    It returns the alr,t,csi,y and azi of the last radiation region.
c           If t=0, no more regions are present.
c           If flg_allrad is false, only one region is returned: the one with the
c           largest t. Otherwise, one region per resonance is returned (the one with
c           the highest t in the given resonance.
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      character * (*) mode
      integer alr
      real * 8 t,csi,y,azi
      integer, parameter :: maxemissions=20
      integer alrs(maxemissions),numemissions
      real * 8 csis(maxemissions),ys(maxemissions),azis(maxemissions),
     1         ts(maxemissions)
      logical valid(maxemissions)
      save numemissions,alrs,ts,csis,ys,azis
      integer jmax,j,resjmax,resj,emitter
      real * 8 tmax
      if(mode.eq.'reset') then
         numemissions = 0
         valid = .true.
      elseif(mode.eq.'save') then
         if(numemissions == maxemissions) then
            write(*,*) ' save_rad_parameters: too many emissions'
            write(*,*) ' increase maxemissions'
            write(*,*) ' exiting ...'
            call exit(-1)
         endif
         numemissions = numemissions + 1
         alrs(numemissions) = alr
         ts(numemissions) = t
         csis(numemissions) = csi
         ys(numemissions) = y
         azis(numemissions) = azi
      elseif(mode.eq.'inquire') then
         alr = numemissions
      elseif(mode.eq.'next') then
c Find hardest radiation
         tmax = -1
         do j=1,numemissions
            if(valid(j).and.ts(j).gt.tmax) then
               tmax = ts(j)
               jmax = j
            endif
         enddo
         if(tmax == -1) then
            t = -1
         else
            alr = alrs(jmax)
            t = ts(jmax)
            csi = csis(jmax)
            y = ys(jmax)
            azi = azis(jmax)
            if(flg_allrad) then
c Invalidate emissions belonging to the same resonance (including the
c pseudo-resonance of production) of the current radiator.
c Find resonance of current radiator:
               if(flst_emitter(alrs(jmax)).le.2) then
                  resjmax = 0
               else
                  resjmax = flst_alrres(flst_emitter(alrs(jmax)),alrs(jmax))
               endif
               do j=1,numemissions
                  if(flst_emitter(alrs(j)).le.2) then
                     resj = 0
                  else
                     resj = flst_alrres(flst_emitter(alrs(j)),alrs(j))
                  endif
                  if(  resj == resjmax ) then
                     valid(j) = .false.
                  endif
               enddo
            else
c Invalidate all emissions;
               valid = .false.
            endif
         endif
      else
         write(*,*) ' save_rad_parameters: unknown mode '//mode
         write(*,*) ' exiting ...'
         call exit(-1)
      endif
      end

