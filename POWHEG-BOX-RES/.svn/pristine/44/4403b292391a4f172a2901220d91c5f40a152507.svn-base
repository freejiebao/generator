c      implicit none
c      integer ndim
c      character * 20 pwgprefix
c      integer lprefix
c      common/cpwgprefix/pwgprefix,lprefix
c      include 'pwhg_rnd.h'
c      parameter (ndim=19)
c      real * 8 ymax(50,ndim),xint,ymmm,ymin
c      integer k,j
c      lprefix=3
c      pwgprefix='pwg'
c      rnd_cwhichseed='none'
c      xint=8.8d-3
c      call loadmintupb(ndim,'btlupb',xint,ymax)
c      ymmm=0
c      ymin=1d30
c      do k=1,50
c         do j=1,ndim
c            ymmm=max(ymmm,ymax(k,j))
c            ymin=min(ymin,ymax(k,j))
c         enddo
c         write(*,'(19(d8.2,1x))') (ymax(k,j),j=1,ndim)
c      enddo
c      write(*,*) ymmm, ymin, xint**(1d0/ndim)
c      end


c initialize the storage of values for the determination of the
c upper bounding envelope in MINT
      subroutine startstoremintupb(filetag)
      implicit none
      include 'pwhg_rnd.h'
      include 'pwhg_flg.h'
      character * (*) filetag
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      integer iunit
      logical active
      common/storeubc/iunit,active
      save /storeubc/
      data active/.false./
      integer iret
      active=.true.
      if(rnd_cwhichseed.eq.'none') then
         call pwhg_io_open_write(pwgprefix(1:lprefix)//
     1    trim(filetag)//'.dat',iunit,flg_compress_upb,iret)
      else
         call pwhg_io_open_write(pwgprefix(1:lprefix)//
     1    trim(filetag)//'-'//
     1        rnd_cwhichseed//'.dat',iunit,flg_compress_upb,iret)
      endif
      if(iret /= 0) then
         write(*,*) 'startstoremintupb: cannot open output file'
         write(*,*) 'exiting ...'
         call exit(-1)
      endif
      end

      subroutine mintupbformat(ndim,fmt)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer ndim
      character * 30 fmt
      integer nind,ndigits
      nind = flst_nbornresgroup
      if(nind.gt.1) then
         ndigits=int(log10(float(nind)))+1
         fmt='(i    ,   i2,2d11.5)'
         write(fmt(3:6),'(i3)') ndigits
         write(fmt(9:10),'(i2)') ndim
         write(*,*) ' format storemintupb: ['//trim(fmt)//']'
      else
         fmt='(   i2,2d11.5)'
         write(fmt(2:4),'(i2)') ndim
      endif
      end

      subroutine storemintupb(ndim,ncell,ind,imode,f,f0)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer ndim,ncell(ndim),ind,imode
      real * 8 f,f0
      integer iunit,nind
      logical active
      common/storeubc/iunit,active
      character * 30 fmt
c make room for two floats, the index, and ndim 2-digits integers      
      character(len=2*ndim+30) string
      integer k
      logical ini
      data ini/.true./
      save ini,fmt,nind
      if(active) then
         if(ini) then
            call mintupbformat(ndim,fmt)
            nind = flst_nbornresgroup
            ini = .false.
         endif
         if(imode.eq.0) then
            if(nind.gt.1) then
               write(string,fmt) ind,(ncell(k),k=1,ndim),f,f0
               call pwhg_io_write(iunit,trim(string))
            else
               write(string,fmt) (ncell(k),k=1,ndim),f,f0
               call pwhg_io_write(iunit,trim(string))
            endif
         else
            if(nind.gt.1) then
               write(string,fmt) ind,(ncell(k),k=1,ndim),f
               call pwhg_io_write(iunit,trim(string))
            else
               write(string,fmt) (ncell(k),k=1,ndim),f
               call pwhg_io_write(iunit,trim(string))
            endif
         endif
      endif
      end

      subroutine stopstoremintupb
      implicit none
      integer iunit
      logical active
      common/storeubc/iunit,active
      call pwhg_io_close(iunit)
      active=.false.
      end

      subroutine getlinemintupb1(filetag,ndim,cells,ind,f,f0,iret)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      character *(*) filetag
      integer ndim,cells(ndiminteg),ind,iret
      real * 8 f,f0
      character * 1, dimension(:,:), allocatable, save :: allcells
      integer, dimension(:), allocatable, save :: allind
      real , dimension(:), allocatable, save :: allf
      real , dimension(:), allocatable, save :: allf0
      integer nlines,j
      integer status,index
c the internal flag status is
c 0     if the data has not been loaded into memory
c       (typically upon the first invocation)
c 1     if the data s in memory
c the integer index is the data line to be read.
c It is increased after each call, and upon the last
c call (the one returning iret = 1) it is reset to 1
      data status/0/
      save status,index,nlines
c a call with iret=-10 deallocate all arrays and returns ;
      if(iret.eq.-10) then
         write(*,*) ' deallocating mintupb arrays'
         deallocate(allcells,stat=j)
         deallocate(allf,stat=j)
         deallocate(allf0,stat=j)
         if(flst_nbornresgroup .gt. 1) then
            deallocate(allind,stat=j)
         endif
         write(*,*) ' end deallocating '
         status=0
         return
      endif
      if(status.eq.0) then
         write(*,*) ' getlinemintupb1: loading file(s)'
c status=0 is the initial call;
         iret=0
         nlines=0
c in this block count the lines in the file (nlines
 1       continue
         call getlinemintupb(filetag,ndim,cells,ind,f,f0,iret)
         if(iret.eq.0) then
            nlines=nlines+1
            goto 1
         endif
c lines counted
c allocates enough stuff for nlines lines
         deallocate(allcells,stat=iret)
         allocate(allcells(ndim,nlines),stat = iret)
         deallocate(allf,stat=iret)
         allocate(allf(nlines),stat=iret)
         deallocate(allf0,stat=iret)
         allocate(allf0(nlines),stat=iret)
         if(flst_nbornresgroup .gt. 1) then
            allocate(allind(nlines),stat=iret)
         endif
c store file content in allocated array
         do j=1,nlines
            call getlinemintupb(filetag,ndim,cells,ind,f,f0,iret)
            call inttochar(cells,allcells(:,j),ndim)
            if(flst_nbornresgroup .gt. 1) then
               allind(j)=ind
            endif
            allf(j)=f
            allf0(j)=f0
         enddo
c this call should return 1 in iret (no more lines)
         call getlinemintupb(filetag,ndim,cells,ind,f,f0,iret)
c Set status to 1 (cells loaded), index to 1 (initiate reading)
         status=1
         index=1
         write(*,*) 'getlinemintupb1: loaded file(s)'
      endif
      if(index.le.nlines) then
         f=allf(index)
         f0=allf0(index)
         if(flst_nbornresgroup .gt. 1) then
            ind = allind(index)
         endif
         call chartoint(allcells(:,index),cells,ndim)
         index=index+1
         iret=0
      else
c end of data
         iret=1
         index=1
      endif
      end
         
      subroutine getlinemintupb(filetag,ndim,cells,ind,f,f0,iret)
c reads a line from the upper bound file or files.
c iret=-1: failure
c iret=0 : success
c iret=1 : end of stream; next call restart reading
c          from the beginning
      implicit none
      character *(*) filetag
      integer ndim,cells(ndim),ind,iret
      real * 8 f,f0
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rnd.h'
      include 'pwhg_flg.h'
      character * 20 pwgprefix
      character(len=2*ndim+30) string
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      integer ltag
      character * 100 fname
      integer jfile,k,iunit
      character * 30 fmt
      character * 4 chnum
      logical lpresent
      integer status
      data status/0/
      save status,iunit,jfile,fmt
c initial call
      if(status.eq.0) then
         call mintupbformat(ndim,fmt)
         ltag=len(trim(filetag))
c see if there are files to load
         if(rnd_cwhichseed.eq.'none') then
            fname=pwgprefix(1:lprefix)//filetag(1:ltag)//'.dat'
         else
            do jfile=1,9999
               write(chnum,'(i4)') jfile
               if(chnum(1:1).eq.' ') chnum(1:1)='0'
               if(chnum(2:2).eq.' ') chnum(2:2)='0'
               if(chnum(3:3).eq.' ') chnum(3:3)='0'
               fname=pwgprefix(1:lprefix)//filetag(1:ltag)
     1              //'-'//chnum//'.dat'
               inquire(file=fname,exist=lpresent)
               if(lpresent) goto 10
            enddo
            goto 999
         endif
 10      continue
         call pwhg_io_open_read(trim(fname),iunit,iret)
         if(iret /= 0) goto 999
         write(*,*) ' opened ',trim(fname)
c file opened for reading
         status=1
      endif
 12   continue
      call pwhg_io_read(iunit,string,iret)
      if(iret < 0) goto 11
      if(filetag.eq.'btlupb' .and. flg_fastbtlbound) then
         if(flst_nbornresgroup .gt. 1) then
            read(string,fmt=fmt,end=11) ind,(cells(k),k=1,ndim),f,f0
         else
            read(string,fmt=fmt,end=11) (cells(k),k=1,ndim),f,f0
         endif
      else
         if(flst_nbornresgroup .gt. 1) then
            read(string,fmt=fmt,end=11) ind,(cells(k),k=1,ndim),f
         else
            read(string,fmt=fmt,end=11) (cells(k),k=1,ndim),f
         endif
         f0=-1
      endif
      iret=0
      return
 11   continue
      call pwhg_io_close(iunit)
      if(rnd_cwhichseed.ne.'none') then
 13      jfile=jfile+1
         if(jfile.lt.9999) then
            write(chnum,'(i4)') jfile
            if(chnum(1:1).eq.' ') chnum(1:1)='0'
            if(chnum(2:2).eq.' ') chnum(2:2)='0'
            if(chnum(3:3).eq.' ') chnum(3:3)='0'
            fname=pwgprefix(1:lprefix)//filetag//'-'//chnum//'.dat'
            inquire(file=fname,exist=lpresent)
            if(lpresent) then
               call pwhg_io_open_read(trim(fname),iunit,iret)
               if(iret /= 0) goto 999
               write(*,*) ' opened ',trim(fname)
               goto 12
            else
               goto 13
            endif
         endif
      endif
      iret=1
      status=0
      return
 999  iret=-1
      end
         

      subroutine loadmintupb(ndim,filetag,nind,yindmax,yindmaxrat,ymax,ymaxrat)
      implicit none
      include 'pwhg_flg.h'
      include 'pwhg_par.h'      
      integer ndim,nind
      character *(*) filetag
      real * 8 yindmax(nind),yindmaxrat(nind)
      real * 8 ymax(50,ndim),xint,xintrat
      real * 8 ymaxrat(50,ndim)
      integer cells(ndim)
      integer kdim,iret,j,iunit
      real * 8 f,f0,prod,prodrat,xless,xmore,xlessrat,xmorerat
      real * 8 fail,tot,ubtot,failrat,totrat,ubtotrat,ratlim
      integer ipoints,ind,ndiscarded
      integer iterations
      logical ratflg
      iterations=1
      if(filetag.eq.'btlupb' .and. flg_fastbtlbound) then
         ratflg=.true.
      else
         ratflg=.false.
      endif
      ratlim=par_mintupb_ratlim
c First compute total for f and f/f0 (f/b)
      iret=0
      xint=0
      xintrat=0
      ipoints=0
      ndiscarded = 0
      do
         call getlinemintupb1(filetag,ndim,cells,ind,f,f0,iret)
         if(iret.eq.1) exit
         if(iret /= 0) goto 998
         if(f/f0 > ratlim) then
            ndiscarded = ndiscarded + 1
            cycle
         endif
         ipoints=ipoints+1
         xint=xint+f
         if(ratflg) then
            if(f0.gt.0) xintrat=xintrat+f/f0
         endif
      enddo
      write(*,*) 'loadmintupb: num. discarded/total:',
     1     ndiscarded,'/',ipoints
      xint=xint/ipoints
      write(*,*) 'loadmintupb: estimated integral for '
     1    //trim(filetag)//' (pos.+|neg.|)  is ',xint
      xintrat=xintrat/ipoints/10
      xmore=0.01
      xmorerat=xmore/5
      xless=xmore
      xlessrat=xmorerat
c The bound is initially set as if the function was uniform
c with the given integral
      do kdim=1,ndim
         do j=1,50
            ymax(j,kdim)=xint**(1d0/ndim)
            if(ratflg) then
               if(xintrat.gt.0) ymaxrat(j,kdim)=xintrat**(1d0/ndim)
            endif
         enddo
      enddo
      if(nind > 1) then
         do ind=1,nind
            yindmax(ind)=1d0/nind
            yindmaxrat(ind)=1
         enddo
      endif
c     Large loop for finding ymax,ymaxrat, etc. Exit when efficiency is OK
      do
c     loop for reading u-bound data
         do
            call getlinemintupb1(filetag,ndim,cells,ind,f,f0,iret)
            if(iret == 1) exit
            if(iret /= 0) then
               write(*,*) ' error while loading bound files'
               call exit(-1)
            endif
            if(f/f0 > ratlim) then
               ndiscarded = ndiscarded + 1
               cycle
            endif

            call evalprod

            if(f.gt.prod) then
               do kdim=1,ndim
                  ymax(cells(kdim),kdim)=
     1                 ymax(cells(kdim),kdim)*(f/prod+0.1)**(xmore/ndim)
               enddo
               if(nind.gt.1) then
                  yindmax(ind) = yindmax(ind)*(f/prod+0.1)**(xmore/ndim)
               endif
            else
               do kdim=1,ndim
                  ymax(cells(kdim),kdim)=
     1                 ymax(cells(kdim),kdim)/(2d0)**(xless/ndim)
               enddo
               if(nind.gt.1) then
                  yindmax(ind) = yindmax(ind)/(2d0)**(xless/ndim)
               endif
            endif
            if(ratflg) then
               if(f0.gt.0) then
                  if(f/f0.gt.prodrat) then
                     do kdim=1,ndim
                        ymaxrat(cells(kdim),kdim)=
     1                       ymaxrat(cells(kdim),kdim)*
     2                       (f/f0/prodrat+0.1)**(xmorerat/ndim)
                     enddo
                     if(nind.gt.1) then
                        yindmaxrat(ind) = yindmaxrat(ind)*
     1                       (f/f0/prodrat+0.1)**(xmorerat/ndim)
                     endif
                  else
                     do kdim=1,ndim
                        ymaxrat(cells(kdim),kdim)=
     1                       ymaxrat(cells(kdim),kdim)/
     2                       (2d0)**(xlessrat/ndim)
                     enddo
                     if(nind.gt.1) then
                        yindmaxrat(ind) = yindmaxrat(ind)*
     1                       (2d0)**(xlessrat/ndim)
                     endif
                  endif
               endif
            endif
         enddo
c     check if the failure rate is satisfactory
         fail=0
         tot=0
         ubtot=0
         if(ratflg) then
            failrat=0
            totrat=0
            ubtotrat=0
         endif
         do
            call getlinemintupb1(filetag,ndim,cells,ind,f,f0,iret)
            if(iret.eq.1) exit
            if(iret.ne.0) goto 998
            if(f/f0 > ratlim) then
               ndiscarded = ndiscarded + 1
               cycle
            endif

            call evalprod

            if(f.gt.prod) fail=fail+(f-prod)
            tot=tot+f
            ubtot=ubtot+prod
            if(ratflg) then
               if(f0.ne.0) then
                  if(f.gt.f0*prodrat) failrat=failrat+(f-f0*prodrat)
                  totrat=totrat+f
                  ubtotrat=ubtotrat+f0*prodrat
               endif
            endif
         enddo
         if(fail/tot.gt.1d-3.or.(ratflg.and.failrat/totrat.gt.1d-3))then
c     stop updating the rat grid, if satisfactory
            if(ratflg.and.failrat/totrat.lt.1d-3) then
               ratflg=.false.
               write(*,*) ' ratios envelope efficiency',totrat/ubtotrat
               write(*,*) ' ratios failure estimate',failrat/totrat
            endif
            if(iterations.lt.4) then
               write(*,*) ' iterating upper bounding envelope formation'
            elseif(iterations.lt.5) then
               write(*,*) ' more iterations needed'
               write(*,*) ' this can take a moment ...'
            endif
            write(*,*) ' failure estimate, efficiency ',fail/tot,(tot-fail)/ubtot
            if(ratflg) then
               write(*,*) ' ratios failure estimate, efficiency ',
     1              failrat/totrat,(totrat-failrat)/ubtotrat
            endif
            iterations=iterations+1
            xless = xless * 0.9
            xlessrat = xlessrat * 0.9
         else
            exit
         endif
      enddo
      if(filetag.eq.'btlupb' .and. flg_fastbtlbound) then
         ratflg=.true.
      endif
      write(*,*) ' summary of bounds for '//trim(filetag)
      if(ratflg) then
         write(*,*)
     1 ' estimated efficiency without fastbtlbound ',
     2        tot/ubtot
         write(*,*) ' failure estimate ',fail/tot
         write(*,*)
     1 ' estimated efficiency with fastbtlbound ',
     2        totrat/ubtotrat
         write(*,*) ' failure estimate ',failrat/totrat
      else
         write(*,*) ' envelope efficiency ',tot/ubtot
         write(*,*) ' failure estimate ',fail/tot
      endif
      write(*,*) ' processed ',ipoints,' points',iterations,'iterations'
      if(filetag == 'btlupb' .and. flg_fastbtlbound) then
         call newunit(iunit)
         open(unit=iunit,file='mint_upb_'//trim(filetag)//'_rat.top',status='unknown')
         do kdim=1,ndim
            write(iunit,*) 'set limits x 0 50 y 0 5'
            do j=1,50
               write(iunit,*) j, ymaxrat(j,kdim)
            enddo
            write(iunit,*) 'hist'
            write(iunit,*) 'newplot'
         enddo
         if(nind > 1) then
            write(iunit,*) 'set limits x 0', nind,' y 0 5'
            do ind=1,nind
               write(iunit,*) ind, yindmaxrat(ind)
            enddo
            write(iunit,*) 'hist'
            write(iunit,*) 'newplot'
         endif
         close(iunit)
      endif
      call newunit(iunit)
      open(unit=iunit,file='mint_upb_'//trim(filetag)//'.top',status='unknown')
      do kdim=1,ndim
         write(iunit,*) 'set limits x 0 50 y 0 5'
         do j=1,50
            write(iunit,*) j, ymax(j,kdim)
         enddo
         write(iunit,*) 'hist'
         write(iunit,*) 'newplot'
      enddo
      if(nind>1) then
         write(iunit,*) 'set limits x 0', nind,' y 0 5'
         do ind=1,nind
            write(iunit,*) ind, yindmax(ind)
         enddo
         write(iunit,*) 'hist'
         write(iunit,*) 'newplot'
      endif
      close(iunit)
      call getlinemintupb1(filetag,ndim,cells,ind,f,f0,-10)
      return
 998  continue
      write(*,*) ' error while loading bound files'
      call pwhg_exit(-1)
      contains
      subroutine evalprod
      if(nind.gt.1) then
         prod=yindmax(ind)
      else
         prod=1
      endif
      if(ratflg) then
         if(nind.gt.1) then
            prodrat=yindmaxrat(ind)
         else
            prodrat=1
         endif
      endif
      
      do kdim=1,ndim
         prod=prod*ymax(cells(kdim),kdim)
         if(ratflg) prodrat=prodrat*ymaxrat(cells(kdim),kdim)
      enddo
      end subroutine evalprod
      end

      
      subroutine monitorubound(x,icalls)
      implicit none
      real * 8 x
      integer icalls
      include 'pwhg_rnd.h'
      include 'pwhg_flg.h'
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      character * 80 file
      integer iun
      if(flg_monitorubound) then
         if(rnd_cwhichseed.eq.'none') then
            file=pwgprefix(1:lprefix)//'boundviolations.dat'
         else
            file=pwgprefix(1:lprefix)//'boundviolations-'//
     1           rnd_cwhichseed//'.dat'
         endif
         call newunit(iun)
         open(unit=iun,file=file,access='append')
         write(iun,*) 'calls=',icalls,'f/ubound',x
         close(iun)
      endif
      end

      subroutine inttochar(int_arr,ch_arr,ndim)
      integer ndim
      integer int_arr(ndim)
      character * 1 ch_arr(ndim)
      integer k
      do k=1,ndim
         ch_arr(k)=char(int_arr(k))
      enddo
      end

      subroutine chartoint(ch_arr,int_arr,ndim)
      integer ndim
      integer int_arr(ndim)
      character * 1 ch_arr(ndim)
      integer k
      do k=1,ndim
         int_arr(k)=ichar(ch_arr(k))
      enddo
      end

