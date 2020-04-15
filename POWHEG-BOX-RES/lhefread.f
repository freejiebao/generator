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
      integer i,j,iret
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
         do i=1,nup
            call pwhg_io_read(nlf,string,iret)
            if(iret /=0 ) goto 998
            read(string,*,err=1) idup(i),istup(i),mothup(1,i),
     &           mothup(2,i),icolup(1,i),icolup(2,i),(pup(j,i),j=1,5),
     &           vtimup(i),spinup(i)
         enddo
         call lhefreadextra(nlf,iret)
         if(iret.ne.0) goto 1
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



