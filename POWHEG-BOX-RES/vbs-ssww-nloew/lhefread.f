c...lhefheader(nlf)
c...reads initialization information from a les houches events file on unit nlf. 
      subroutine lhefreadhdr(nlf)
      implicit none
      integer nlf
      character * 200 string
      integer ipr,iret,nch
      include 'LesHouches.h'
      logical ini
      data ini/.true./
      save ini
 1    continue
      call pwhg_io_read(nlf,string,iret)
      if(iret == -1) goto 998
      if(adjustl(string(1:10)).eq.'<initrwgt>') then
c     This subroutine is only called by the shower-analysis routines.
c     Here we abandon the old initrwgt handling, and only support the new
c     one. The old handling is only supported by the pwhgreweight.f routines.
         call pwhg_io_backspace(nlf)
         call rwl_readheader(nlf)
         goto 1
      endif
      if(string(1:6).eq.'<init>') then
         call pwhg_io_read(nlf,string,iret)
         if(iret == -1) goto 998
         read(string,*) idbmup(1),idbmup(2),ebmup(1),ebmup(2),
     &        pdfgup(1),pdfgup(2),pdfsup(1),pdfsup(2),idwtup,nprup
         do ipr=1,nprup
            call pwhg_io_read(nlf,string,iret)
            if(iret == -1) goto 998
            read(string,*) xsecup(ipr),xerrup(ipr),xmaxup(ipr),
     &           lprup(ipr)
         enddo
         goto 999
      else
         goto 1
      endif
 998  write(*,*) 'lhefreadhdr: could not find <init> data'
      call exit(1)
 999  end


c...reads event information from a les houches events file on unit nlf. 
      subroutine lhefreadev(nlf)
      implicit none
      integer nlf
      character * 200 string
      include 'LesHouches.h'
      include 'nlegborn.h'
      include 'pwhg_rad.h'
      real*8 mc_isr_scale,mc_fsr_scale
      integer mc_fsr_em
      common/mc_scale_lhe/mc_isr_scale,mc_fsr_scale(3),mc_fsr_em(3)
c      real*8 mc_isr_scale,mc_fsr_scale
c      common/mc_scale_lhe/mc_isr_scale,mc_fsr_scale
      integer i,j,iret
      integer ini
      data ini/0/
      save ini
      real * 8 powheginput
      external powheginput
      logical debug
      save debug
      integer res,oldnup
      integer ngamma,ngammaf
c.....added-vbfscale/b
      real*8 scaluppt
      save    scaluppt
      integer nj
      real*8 ptj(2),cm(1:4)
      logical removeschannel
      save removeschannel
      integer nres
c.....added-vbfscale/e
            
      ngamma=0
      ngammaf=0

      if(ini.eq.0) then
         write(*,*)'in lhefreadev:setting rad_ptsqmin and rad_ptsqmin'
         write(*,*)'AS in init processes. Otherwise not known in lhef'
         write(*,*)'or main pythia                                   '
         ini=1
         rad_ptsqmin_em = powheginput("#rad_ptsqmin_em")
         if (rad_ptsqmin_em.le.0d0) rad_ptsqmin_em  = 0.001d0**2
         rad_ptsqmin=powheginput('#ptsqmin')
         if(rad_ptsqmin.lt.0) rad_ptsqmin=0.8d0
         debug=powheginput('#test_lhe_recomb').gt.0d0

         removeschannel=powheginput('#no-s-channel-evts').gt.0d0
         
         scaluppt=powheginput('#use-scalup-ptj')
         if(scaluppt.lt.0d0) scaluppt=4d0
         write(*,*)'use-scalup-ptj 0 -> scalup=sqrt(s), DEFAULT'
         write(*,*)'use-scalup-ptj 1 -> scalup=ptj_h'
         write(*,*)'use-scalup-ptj 2 -> scalup=ptj_s'
         write(*,*)'use-scalup-ptj 3 -> scalup=(ptj_h+ptj_s)/2'
         write(*,*)'use-scalup-ptj 4 -> scalup=sqrt(ptj_h*ptj_s)'
      endif



 1    continue
      string=' '
      call pwhg_io_read(nlf,string,iret)
      if(iret /=0 ) goto 666
c      read(nlf,fmt='(a)',err=777,end=666) string
      if(string.eq.'</LesHouchesEvents>') then
         goto 998
      endif
      if(string(1:6).eq.'<event') then
c on error try next event. The error may be caused by merging
c truncated event files. Thus we are tolerant about it.
c Only on EOF return with no event found
         call pwhg_io_read(nlf,string,iret)
         if(iret /=0 ) goto 998
         read(string,*,err=1)nup,idprup,xwgtup,scalup,aqedup,aqcdup



c         write(*,*)"BEFORE",nup

         nres=0
         do i=1,nup
            call pwhg_io_read(nlf,string,iret)
            if(iret /=0 ) goto 998
            read(string,*,err=1) idup(i),istup(i),mothup(1,i),
     &           mothup(2,i),icolup(1,i),icolup(2,i),(pup(j,i),j=1,5),
     &           vtimup(i),spinup(i)
c            write(*,*) idup(i),istup(i),mothup(1,i),
c     &           mothup(2,i),icolup(1,i),icolup(2,i),(pup(j,i),j=1,5),
c     &           vtimup(i),spinup(i)

            if(istup(i).eq.2) nres=nres+1 ! unstable particles have code 2 in LHE
         enddo

         if(removeschannel.and.nres.gt.2)  xwgtup=0d0
         
c.....added-vbfscale/b
c     loop over particles, select jets (avoid W dwcays), reset scalup
c         if(scaluppt.gt.0d0) then
         ptj=0d0
         nj=0
         do i=1,nup
c            write(*,*)'id',idup(i),pup(1:4,i),sqrt(pup(1,i)**2+pup(2,i)**2)
            if(istup(i).eq.1.and.abs(idup(i)).lt.6 ) then
               nj=nj+1
               ptj(nj)=sqrt(pup(1,i)**2+pup(2,i)**2)
            endif
         enddo
         if(nj.ne.2) then
            write(*,*)'not 2 partons at lo, stop',nj
            stop
         endif
         if(scaluppt.eq.0) then
            cm(1:4)=pup(1:4,1)+pup(1:4,2)
            scalup=sqrt(cm(4)**2-cm(1)**2-cm(2)**2-cm(3)**2)
         endif
         if(scaluppt.eq.1) scalup=max(ptj(1),ptj(2))
         if(scaluppt.eq.2) scalup=min(ptj(1),ptj(2))
         if(scaluppt.eq.3) scalup=(ptj(1)+ptj(2))/2d0
         if(scaluppt.eq.4) scalup=sqrt(ptj(1)*ptj(2))
c         write(*,*) 'scalup',scalup
c     endif
c.....added-vbfscale/e         

         
c         write(*,*)'++lhefread+++++++++++++++++++++++++++++++++++++++'
         do i=1,nup
            if(idup(i).eq.22) then
               ngamma=ngamma+1
               if(mothup(1,i).ne.1) ngammaf=ngammaf+1
            endif
            
         enddo
c         write(*,*)'ngamma',ngamma,'ngammaf',ngammaf
         
         call lhefreadextra(nlf,iret)
         if(iret.ne.0) goto 1

c         write(*,*)'mc_isr_scale',mc_isr_scale
c         write(*,*)'mc_fsr_scale',mc_fsr_scale
c         write(*,*)'mc_fsr_em   ',mc_fsr_em

c     mc_fsr_scale(1) hardest one, recombine the other two
c     gammas should be at the end of the event

c         write(*,*)mc_fsr_scale
c         write(*,*)mc_fsr_em
         
         if(debug)then
            oldnup=nup
            do i=2,3
               if(mc_fsr_scale(i).gt.0d0) then
                  res=mothup(1,mc_fsr_em(i))

c                  write(*,*)"res",res
                  
                  do j=1,oldnup
                     if(istup(j).eq.1.and.idup(j).eq.22) then
                        if(mothup(1,j).eq.res) then

c                           write(*,*)"recombined ",j
                           
                           pup(1:4,mc_fsr_em(i))=pup(1:4,mc_fsr_em(i))
     +                          +pup(1:4,j)
                           nup=nup-1
                        endif
                     endif
                  enddo
               endif
            enddo

            if(ngammaf.lt.2.and.nup.ne.oldnup) then
               write(*,*)"error with lhe recomb debug STOP"
               stop
            endif

            if(ngammaf.ge.2.and.nup.eq.oldnup) then
               write(*,*)"error with lhe recomb debug 2 STOP"
               stop
            endif
            
c$$$            write(*,*)"after",nup
c$$$            do i=1,nup
c$$$               write(*,*) idup(i),istup(i),mothup(1,i),
c$$$     &              mothup(2,i),icolup(1,i),icolup(2,i),(pup(j,i),j=1,5),
c$$$     &              vtimup(i),spinup(i)
c$$$            enddo
            
         endif


c here we know both the event type and the scale:
c we have to assign a different meaning to the default 0
         
c the 3rd scale is there only if there is W->qqb, to be fixed once we decide the matching         
         if(mc_fsr_scale(1).eq.0d0) mc_fsr_scale(1)=sqrt(rad_ptsqmin_em)
         if(mc_fsr_scale(2).eq.0d0) mc_fsr_scale(2)=sqrt(rad_ptsqmin_em)
         if(mc_isr_scale.eq.0d0) mc_isr_scale      =sqrt(rad_ptsqmin_em) ! mauro qed only

         
         goto 999
      else
         goto 1
      endif
c no event found:
 777  continue
      print *,"Error in reading"
      print *,string
      nup=0
      return
 666  continue
      print *,"reached EOF"
      print *,string
      nup=0
      return
 998  continue
      print *,"read </LesHouchesEvents>"
      nup=0      
 999  end


      subroutine lhefreadextra(nlf,iret)
      implicit none
      include 'LesHouches.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_st.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      include 'pwhg_weights.h'
      include 'pwhg_rwl.h'
      character * 200 string
      integer nlf,iret
      integer iid,iendid
      integer gen_seed,gen_n1,gen_n2
      real * 8 value
      logical lhweights
c.....mauro
      character*1 tag1,reftag1
      parameter(reftag1='#')
      real *8 kt2minqed
      common/showerqed/kt2minqed
      integer int1,int2,int3,int4,int5
      real*8 re1,re2
      real*8 mc_isr_scale,mc_fsr_scale
      integer mc_fsr_em
      common/mc_scale_lhe/mc_isr_scale,mc_fsr_scale(3),mc_fsr_em(3)
      real*8 mc_tmaxisr,mc_tmaxfsr
      real*8 mc_csiisr,mc_yisr,mc_aziisr
      real*8 mc_csifsr,mc_yfsr,mc_azifsr
      logical mc_dlberad
      common/dblerad/mc_tmaxisr,mc_tmaxfsr,
     +     mc_csiisr,mc_yisr,mc_aziisr,
     +     mc_csifsr,mc_yfsr,mc_azifsr,
     +     mc_dlberad
c.....mauro
      iret = 0
      weights_num = 0
 1    continue
      string=' '
      call pwhg_io_read(nlf,string,iret)
      if(iret /= 0) goto 998
      string = adjustl(string)
      if(string(1:5).eq.'#rwgt') then
         read(string(6:),*) rwl_type,
     $        rwl_index,rwl_weight,rwl_seed,rwl_n1,rwl_n2
c.....mauro-mod
         mc_dlberad=.false.
         if(nup.eq.7) mc_dlberad=.true.
         string=' '
         call pwhg_io_read(nlf,string,iret)
         if(iret /=0 ) goto 998

c         write(*,*)'string',string
         read(string,*)tag1,mc_isr_scale,mc_fsr_em,mc_fsr_scale !sqrt(mc_tmaxfsr)
c.....mauro-mod
      endif
      if(string(1:6).eq.'<rwgt>' .or. string(1:9).eq.'<weights>') then
c     this routine is reached only if flg_rwl_add is true, from the main program,
c     or from the analysis routines. Thus we only enforce the new weight info
c     apparatus. The old apparatus is used only in lhefreadevlhrwgt.
         call pwhg_io_backspace(nlf)
         call rwl_loadweights(nlf,iret)
c on a return with iret != 0 the event will be skipped 
         if(iret.ne.0) return
         goto 1
      endif
      if(string.eq.'</event>') then
         call pwhg_io_backspace(nlf)
         return
      endif
c Look for old new weight format:
      if(string(1:11).eq.'#new weight') then
         if(weights_num.eq.weights_max) then
            write(*,*) ' too many weights!'
            write(*,*) ' increase weights_max'
            call exit(-1)
         endif
         weights_num = weights_num + 1
         read(string(38:),*) weights_val(weights_num),
     1                       weights_renfac(weights_num),
     2                       weights_facfac(weights_num),
     3                       weights_npdf1(weights_num),
     4                       weights_npdf2(weights_num),
     5                       weights_whichpdf(weights_num)
      endif
      if(string(1:5).eq.'#rwgt') then
         string(1:5)=' '
c     do things
c     print*, 'FOUND'
         read(string,*) rad_type
         if(rad_type.eq.1) then
c     btilde
            read(string,*)rad_type,
     $           rad_ubornsubp,rad_currentweight,
     $           gen_seed,gen_n1,gen_n2
         elseif(rad_type.eq.2) then
c     remnant
            read(string,*)rad_type,
     $           rad_alrsubp,rad_currentweight,
     $           gen_seed,gen_n1,gen_n2
         elseif(rad_type.eq.3) then
c     regular
            read(string,*)rad_type,
     $           rad_regularsubp,rad_currentweight,
     $           gen_seed,gen_n1,gen_n2
         else
            write(*,*) 'Invalid rad_type in lhefwriteevrw: ',rad_type
            call exit(-1)
         endif
      endif
      if(string.eq.'# Start extra-info-previous-event') then
         call pwhg_io_read(nlf,string,iret)
         if(iret /= 0) goto 800
         read(string(3:),*) rad_kinreg
         call pwhg_io_read(nlf,string,iret)
 800     if(iret /= 0) then
            write(*,*)
     1           'lhefreadextra:'
            write(*,*)
     1       'found no lines after Start extra-info-previous-event'
            write(*,*) ' exiting ...'
            call exit(-1)
         endif
         read(string(3:),*) rad_type
      endif
      goto 1
      return
 998  continue
      end



