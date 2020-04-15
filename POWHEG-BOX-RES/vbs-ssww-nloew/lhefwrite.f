c...lhefheader(nlf)
c...writes initialization information to a les houches events file on unit nlf. 
      subroutine lhefwritehdr(nlf)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_flg.h'
      integer nlf
      real * 8 version
      common/cversion/version
      data version/1.0/
      integer ipr,iran,n1ran,n2ran,iun,iret
      character * 3 whichpdfpk
      external whichpdfpk
      character(100) buffer
      include 'LesHouches.h'
      call  pwhg_io_write(nlf,'<LesHouchesEvents version="3.0">')
      call  pwhg_io_write(nlf,'<!--')
      call  pwhg_io_write(nlf,'file generated with POWHEG-BOX-V2')
      iun = nlf
      include 'svn.version'
      call  pwhg_io_write(nlf,'Input file powheg.input contained:')
      call wrtpowheginput(nlf)
      call  pwhg_io_write(nlf,'End of powheg.input content')
      write(buffer,'(a)') 'PDF package: '//whichpdfpk()
      call  pwhg_io_write(nlf,trim(buffer))
      call rm48ut(iran,n1ran,n2ran)
      write(buffer,*) 'Random number generator initialized with: ',
     1     iran,' ',n1ran,' ',n2ran
      call  pwhg_io_write(nlf,trim(buffer))
      call  pwhg_io_write(nlf,'-->')
      if(flg_rwl) then
         call pwhg_io_write(nlf,'<header>')
         call rwl_write_rwgt_info(nlf)
         call pwhg_io_write(nlf,'</header>')
      endif
      call  pwhg_io_write(nlf,'<init>')
      write(buffer,110) idbmup(1),idbmup(2),ebmup(1),ebmup(2),
     1     pdfgup(1),pdfgup(2),pdfsup(1),pdfsup(2),idwtup,nprup
      call  pwhg_io_write(nlf,trim(buffer))
      do 100 ipr=1,nprup
         write(buffer,120) xsecup(ipr),xerrup(ipr),xmaxup(ipr),
     &        lprup(ipr)
         call  pwhg_io_write(nlf,trim(buffer))
 100  continue
      call  pwhg_io_write(nlf,'</init>')
 110  format(1p,2(1x,i8),2(1x,e12.5),6(1x,i6))
 120  format(1p,3(1x,e12.5),1x,i6)
      end


      subroutine printleshouches
c useful for debugging
      call lhefwritev(6)
      end

c...lhefeader(nlf)
c...writes event information to a les houches events file on unit nlf. 
      subroutine lhefwritev(nlf)
      implicit none
      integer nlf
      include 'LesHouches.h'
      include 'pwhg_flg.h'
      integer i,j,iret
      integer, save :: counter=0
      character(200) buffer
c.....mauro
      integer i1,i2
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
      
      if(flg_noevents) then
c do not write events, write only the event count
         counter = counter + 1
         if((counter/1000)*1000.eq.counter) then
            write(nlf,*) counter
         endif
         return
      endif
      call  pwhg_io_write(nlf,'<event>')
      write(buffer,210) nup,idprup,xwgtup,scalup,aqedup,aqcdup
      call  pwhg_io_write(nlf,trim(buffer))
      do 200 i=1,nup
         write(buffer,220) idup(i),istup(i),mothup(1,i),
     & mothup(2,i),icolup(1,i),icolup(2,i),(pup(j,i),j=1,5),
     & vtimup(i),spinup(i)
         call  pwhg_io_write(nlf,trim(buffer))
 200  continue
      if(flg_reweight) then
         call lhefwriteevrw(nlf)
         if(flg_rwl) then
            call rwl_write_weights(nlf)
         endif
      endif
      if(flg_pdfreweight) call lhefwritepdfrw(nlf)
      if(flg_debug) call lhefwritextra(nlf)
c.....mauro ! noe moved to io_write
      write(buffer,230)'#', mc_isr_scale,mc_fsr_em,mc_fsr_scale !sqrt(mc_tmaxfsr)
      call  pwhg_io_write(nlf,trim(buffer))
c.....mauro
      call  pwhg_io_write(nlf,'</event>')
 210  format(1p,2(1x,i6),4(1x,e12.5))
 220  format(1p,i8,5(1x,i5),5(1x,e16.9),1x,e12.5,1x,e10.3)
c 230  format(A1,e16.9,e16.9)
 230  format(A1,e16.9,3(i8),e16.9,1x,e16.9,1x,e16.9)
      end

c...lheftrailer(nlf)
c...writes trailer to a les houches events file on unit nlf. 
      subroutine lhefwritetrailer(nlf)
      implicit none
      integer nlf,iran,n1ran,n2ran,iret
      character(100) buffer
      call pwhg_io_write(nlf,'</LesHouchesEvents>')
c     save last random number
      call rm48ut(iran,n1ran,n2ran)
      write(buffer,*) '#Random number generator exit values: ',
     # iran,' ',n1ran,' ',n2ran
      call  pwhg_io_write(nlf,trim(buffer))
      end

      subroutine lhefwritextra(nlf)
      implicit none
      include 'LesHouches.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_st.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      integer nlf
      integer lh_seed,lh_n1,lh_n2,iret
      common/lhseeds/lh_seed,lh_n1,lh_n2
      character(100) buffer
      call pwhg_io_write(nlf,'# Start extra-info-previous-event')
      write(buffer,*) '# ',rad_kinreg,'       rad_kinreg'
      call pwhg_io_write(nlf,trim(buffer))
      write(buffer,*) '# ',rad_type,'         rad_type'
      call pwhg_io_write(nlf,trim(buffer))
      write(buffer,*) '# ', lh_seed,' ',lh_n1,' ',lh_n2,
     #     "    previous event's random seeds "
      call pwhg_io_write(nlf,trim(buffer))
      call pwhg_io_write(nlf,'# End extra-info-previous-event')
      end

      subroutine lhefwritepdfrw(nlf)
      implicit none
      integer nlf
      integer id1,id2,iret
      real * 8 x1,x2,xf1,xf2,xmufact
      character(100) buffer
      call pdfreweightinfo(id1,id2,x1,x2,xmufact,xf1,xf2)
      write(buffer,111)'#pdf ',id1,id2,x1,x2,xmufact,xf1,xf2
      call pwhg_io_write(nlf,trim(buffer))
 111  format(a,2(1x,i2),5(1x,e14.8))
      end

      subroutine lhefwriteevrw(nlf)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_rwl.h'
      integer nlf
      character * 132 string
      write(string,*)'#rwgt ',rwl_type,
     $        rwl_index,rwl_weight,rwl_seed,rwl_n1,rwl_n2
      call pwhg_io_write(nlf,trim(adjustl(string)))
      end

