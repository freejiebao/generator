      subroutine computetotgen(totabs)
      implicit none
      include 'pwhg_mintw.h'
      real * 8 totabs
      integer j
      totabs=0
      do j=1,mintw_nptrs
         totabs = totabs + mintw_ptrs(j)%totabs
      enddo
      end

      subroutine storeradarray(results)
      implicit none
      include 'pwhg_mintw.h'
      real * 8 results(*)
      real * 8 totabs,totn
      integer iid,k
      do iid = 1,mintw_nptrs
         if(mintw_currid.eq.mintw_ptrs(iid)%id) exit
      enddo
      do k=1,mintw_ptrs(iid)%nchannels
         mintw_ptrs(iid)%results(k) = results(k)
         if(results(k).lt.0) then
            mintw_ptrs(iid)%signs(k) = -1
         else
            mintw_ptrs(iid)%signs(k) = 1
         endif
         if(k.eq.1) then
            mintw_ptrs(iid)%cumulant(k) = abs(results(k))
         else
            mintw_ptrs(iid)%cumulant(k) = mintw_ptrs(iid)%cumulant(k-1) 
     1           + abs(results(k))
         endif
      enddo
c if the sum is zero, no need to normalize, the event will never
c be generated
      if(mintw_ptrs(iid)%cumulant(mintw_ptrs(iid)%nchannels)>0) then
         mintw_ptrs(iid)%cumulant = mintw_ptrs(iid)%cumulant/
     1        mintw_ptrs(iid)%cumulant(mintw_ptrs(iid)%nchannels)
      endif
      end


      subroutine chooseid(r,id)
      implicit none
      include 'pwhg_mintw.h'
      real * 8 r
      character *(*) id
      real * 8 totabs,totn
      integer j
      totabs=0
      do j=1,mintw_nptrs
         totabs = totabs + mintw_ptrs(j)%totabs
      enddo
      totn = 0
      do j=1,mintw_nptrs
         totn = totn + mintw_ptrs(j)%totabs/totabs
         if(totn.gt.r) then
            id = mintw_ptrs(j)%id
            return
         endif
      enddo
      end

      subroutine choosesubproc(id,iproc,isign)
      implicit none
      include 'pwhg_mintw.h'
      character *(*) id
      integer iproc,isign
      real * 8 random,r
      procedure () :: random
      integer iid
      do iid = 1,mintw_nptrs
         if(id.eq.mintw_ptrs(iid)%id) exit
      enddo
      r = random()
      do iproc = 1,mintw_ptrs(iid)%nchannels
         if(r.lt.mintw_ptrs(iid)%cumulant(iproc)) exit
      enddo
c just in case the total cumulant is slightly below 1
      iproc = min(iproc,mintw_ptrs(iid)%nchannels)
      isign = mintw_ptrs(iid)%signs(iproc)
      end


      subroutine loadmintupbwrapper(id)
      implicit none
      character *(*) id
      character * 20 postfix
      integer icurrent
      include 'pwhg_mintw.h'
      call getcurrentptrindex(id,icurrent)
      call getpostfix(id,postfix)
      if(icurrent.lt.0) then
         write(*,*)' loadmintupbwrapper: id ',trim(id),' not found. Exiting ...'
         call exit(-1)
      endif
      call loadmintupb(
     1     mintw_ptrs(icurrent)%ndim,
     2     trim(postfix)//'upb',
     3     mintw_ptrs(icurrent)%nind,
     4     mintw_ptrs(icurrent)%yindmax,
     5     mintw_ptrs(icurrent)%yindmaxrat,
     6     mintw_ptrs(icurrent)%ymax,
     7     mintw_ptrs(icurrent)%ymaxrat)
      end


      subroutine mintwrapper(id,imode,doregrid,iunstat)
      implicit none
      character *(*) id
      integer imode,iunstat
      logical doregrid
c end arg list
      integer ndim,nind,nchannels
      include 'pwhg_mintw.h'
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      integer icurrent,ncall,itmx,j,kdim,kint,ibtilde
      integer parallelstage,xgriditeration
      character * 20 postfix
      real * 8 powheginput
      procedure () :: btilde, sigremnant, sigregular
      procedure (), pointer :: fun => NULL()
      procedure () :: powheginput
      mintw_currid = id
      
      if(id.eq.'btilde'.or.id.eq.'btildeborn') then
         fun => btilde
         nind = flst_nbornresgroup
         ndim = ndiminteg
         if(id.eq.'btildeborn') ndim = ndim - 3
         nchannels = flst_nborn
      elseif(id.eq.'remn') then
         fun => sigremnant
         nind = flst_nbornresgroup
         ndim = ndiminteg
         nchannels = flst_nalr
      elseif(id.eq.'reg') then
         fun => sigregular
         nind = flst_nregularresgroup
         ndim = ndiminteg
         nchannels = flst_nregular
      endif

      if(imode.eq.0) then
         write(*,*) ' mintwrapper: Computing the importance sampling'
         write(*,*) ' grid for '//id
      elseif(imode.eq.1) then
         write(*,*) ' mintwrapper: Computing cross section'
         write(*,*) ' and upper bounding envelopes for '//id         
      endif
         

      call getparallelparms(parallelstage,xgriditeration)

      call getcurrentptrindex(id,icurrent)
      if(icurrent.lt.0) then
         mintw_nptrs = mintw_nptrs + 1
         icurrent = mintw_nptrs
         mintw_ptrs(icurrent)%id = id
         call allocate_mintw(mintw_ptrs(icurrent),ndim,nind,nchannels)
      endif

      call getpostfix(id,postfix)

      do j=1,ndim
         mintw_ptrs(icurrent)%ifold(j)=1
      enddo

      call resettotals(mintw_ptrs(icurrent))

      if(imode.eq.0) then
         if(id.eq.'remn' .and. flg_samexgridasbtilde) then
            call getcurrentptrindex('btilde',ibtilde)
            mintw_ptrs(icurrent)%xint   =  mintw_ptrs(ibtilde)%xint   
            mintw_ptrs(icurrent)%xgrid  =  mintw_ptrs(ibtilde)%xgrid  
            mintw_ptrs(icurrent)%xacc   =  mintw_ptrs(ibtilde)%xacc   
            mintw_ptrs(icurrent)%nhits  =  mintw_ptrs(ibtilde)%nhits  
            mintw_ptrs(icurrent)%wind   =  mintw_ptrs(ibtilde)%wind   
            mintw_ptrs(icurrent)%accind =  mintw_ptrs(ibtilde)%accind 
            mintw_ptrs(icurrent)%indhits=  mintw_ptrs(ibtilde)%indhits
            return
         else
c     It is computing the importance sampling grids. The grids must be initialized
c     to constant spacing in the first iteration. In parallel mode, each iteration
c     is invoked separately; so, only the first parallel mode iteration should be
c     initialized. It enters here only if imode=0, that means either parallestage
c     equal 1 or 3 (when building a born envelope). If parallelstage is 1, should
c     only do it for xgriditeration 1, thus the following logic
            if(parallelstage.ne.1.or.xgriditeration.eq.1) then
               do kdim=1,ndim
                  do kint=0,nintervals
                     mintw_ptrs(icurrent)%xgrid(kint,kdim)=dble(kint)/nintervals
                  enddo
               enddo
               do j=1,nind
                  mintw_ptrs(icurrent)%wind(j) = dble(j-1) / nind
               enddo
               mintw_ptrs(icurrent)%wind(nind+1) = 1
            endif

            ncall = powheginput("#ncall1"//trim(postfix))
            if(ncall.lt.0) then
               ncall = powheginput("#ncall1")
            endif
            mintw_ptrs(icurrent)%ncall = ncall
         
            itmx = powheginput("#itmx1"//trim(postfix))
            if(itmx.lt.0) then
               itmx = powheginput("itmx1")
            endif
            mintw_ptrs(icurrent)%itmx = itmx
         endif
      elseif(imode.eq.1) then
         if(flg_storemintupb) call startstoremintupb(trim(postfix)//'upb')
c basically reset random number generator, if optionally required
         call setstage2init
         if(id.eq.'btilde') then
            mintw_ptrs(icurrent)%ifold(ndim-2) = powheginput("foldcsi")
            mintw_ptrs(icurrent)%ifold(ndim-1) = powheginput("foldy")
            mintw_ptrs(icurrent)%ifold(ndim)   = powheginput("foldphi")
         endif
c     reset accumulated values in btilde function

         ncall = powheginput("#ncall2"//trim(postfix))
         if(ncall.lt.0) then
            ncall = powheginput("#ncall2")
         endif
         mintw_ptrs(icurrent)%ncall = ncall
         
         itmx = powheginput("#itmx2"//trim(postfix))
         if(itmx.lt.0) then
            itmx = powheginput("itmx2")
         endif
         mintw_ptrs(icurrent)%itmx = itmx
      endif
      
      call mint(fun,
     1     mintw_ptrs(icurrent)%ndim,
     2     mintw_ptrs(icurrent)%ncall,
     3     mintw_ptrs(icurrent)%itmx,
     4     mintw_ptrs(icurrent)%ifold,
     5     imode,doregrid,
     6     mintw_ptrs(icurrent)%nind,
     7     mintw_ptrs(icurrent)%wind,
     7     mintw_ptrs(icurrent)%accind,
     8     mintw_ptrs(icurrent)%indhits,
     9     mintw_ptrs(icurrent)%yindmax,
     1     mintw_ptrs(icurrent)%yindmaxrat,
     2     mintw_ptrs(icurrent)%xgrid,
     3     mintw_ptrs(icurrent)%xint,
     4     mintw_ptrs(icurrent)%xacc,
     5     mintw_ptrs(icurrent)%nhits,
     6     mintw_ptrs(icurrent)%ymax,
     7     mintw_ptrs(icurrent)%ymaxrat,
     8     mintw_ptrs(icurrent)%ans,
     9     mintw_ptrs(icurrent)%err)

      if(imode == 0) then
c     In imode=0 we don't call writestat(iunstat), because tot* and etot* variables
c     are still undefined. Write instead the estimate for the absolute total
         write(*,*) trim(id)//': estimated absolute value cross section:',
     1        mintw_ptrs(icurrent)%ans,'+-',mintw_ptrs(icurrent)%err
         write(iunstat,*) trim(id)//': estimated absolute value cross section:',
     1        mintw_ptrs(icurrent)%ans,'+-',mintw_ptrs(icurrent)%err
      elseif(imode == 1) then
         if(flg_storemintupb) call stopstoremintupb
         call finaltotals(id)
c     The following will be written to iunstat by writestat(iunstat). No need to repeat it here.
         write(*,*) id//' pos.   weights:', mintw_ptrs(icurrent)%totpos,' +- ',
     1                                      mintw_ptrs(icurrent)%etotpos
         write(*,*) id//' |neg.| weights:', mintw_ptrs(icurrent)%totneg,' +- ',
     1                                      mintw_ptrs(icurrent)%etotneg
         write(*,*) id//' total (pos.-|neg.|):', mintw_ptrs(icurrent)%tot,' +- ',
     1                                           mintw_ptrs(icurrent)%etot
      endif

      end

      subroutine mintwrapper_sign_result(id,iind,w)
      implicit none
      character *(*) id
      integer iind
      real * 8 res,w
      call mintwrapper_result0(id,iind,res,w)
      end
      subroutine mintwrapper_result(id,iind,res)
      implicit none
      character *(*) id
      integer iind
      real * 8 res,w
      call mintwrapper_result0(id,iind,res,w)
      end
      subroutine mintwrapper_result0(id,iind,res,w)
      implicit none
      character *(*) id
      integer iind
      real * 8 res,w
      include 'pwhg_mintw.h'
      integer icurrent
      call getcurrentptrindex(id,icurrent)
      if(icurrent.lt.0) then
         write(*,*)' mintwrapper_result: arrays for ',id,' are not there!'
         write(*,*)' exiting ...'
         call exit(-1)
      endif
      if(iind > mintw_ptrs(icurrent)%nchannels) then
         write(*,*)' mintwrapper_result: index ',iind,' out of bounds'
         write(*,*)' exiting ...'
         call exit(-1)
      endif
      res = mintw_ptrs(icurrent)%results(iind)
      w = w * mintw_ptrs(icurrent)%signs(iind)
      end

      subroutine genwrapper(id,imode,mcalls,icalls,x,ind)
      implicit none
      character *(*) id
      integer imode,mcalls,icalls,ind
      real * 8 x(*)
      include 'nlegborn.h'
      include 'pwhg_mintw.h'
      include 'pwhg_flg.h'
      include 'pwhg_rad.h'
      logical save_nlotest
      integer icurrent
      real * 8 gen_sigma,gen_sigma2,gen_isigma,gen_totev
c     Feedback from the integrator, used to provide an estimate of
c     the cross section while generating an event
      real * 8 sigma, sigma2
      integer isigma
      common/gencommon/sigma,sigma2,isigma
      procedure () :: btilde, sigremnant, sigregular
      procedure (), pointer :: fun => NULL()
      mintw_currid = id
      if(id.eq.'btilde' .or.id.eq.'btildeborn' ) then
         fun => btilde
      elseif(id.eq.'remn') then
         fun => sigremnant
      elseif(id.eq.'reg') then
         fun => sigregular
      endif

      flg_ingen = .true.
      call getcurrentptrindex(id,icurrent)
      if(icurrent.lt.0) then
         write(*,*)' genwrapper: arrays for ',id,' are not there!'
         write(*,*)' exiting ...'
         call exit(-1)
      endif
      save_nlotest = flg_nlotest
      flg_nlotest = .false.
      call gen(
     1   fun,
     2   mintw_ptrs(icurrent)%ndim,
     3   mintw_ptrs(icurrent)%xgrid,
     4   mintw_ptrs(icurrent)%ymax,
     5   mintw_ptrs(icurrent)%ymaxrat,
     6   mintw_ptrs(icurrent)%nind,
     7   mintw_ptrs(icurrent)%wind,
     8   mintw_ptrs(icurrent)%yindmax,
     9   mintw_ptrs(icurrent)%yindmaxrat,
     1   mintw_ptrs(icurrent)%xmmm,
     2   mintw_ptrs(icurrent)%xindmmm,
     3   mintw_ptrs(icurrent)%ifold,
     4   imode,mcalls,icalls,x,ind )

      if (imode == 1) then
        mintw_ptrs(icurrent)%gen_sigma  =
     1       mintw_ptrs(icurrent)%gen_sigma  + sigma
        mintw_ptrs(icurrent)%gen_sigma2 =
     2       mintw_ptrs(icurrent)%gen_sigma2 + sigma2
        mintw_ptrs(icurrent)%gen_isigma =
     3       mintw_ptrs(icurrent)%gen_isigma + isigma
        mintw_ptrs(icurrent)%gen_totev  =
     4       mintw_ptrs(icurrent)%gen_totev  + rad_genubexceeded

        gen_sigma  = mintw_ptrs(icurrent)%gen_sigma
        gen_isigma = mintw_ptrs(icurrent)%gen_isigma
        gen_sigma2 = mintw_ptrs(icurrent)%gen_sigma2
        gen_totev  = mintw_ptrs(icurrent)%gen_totev

        call setcnt(trim(id)//" cross section used:",
     1        mintw_ptrs(icurrent)%totabs)
c     prevent division by zero if gen_isigma=0 
        if (gen_isigma.ne.0) then
           call setcnt(trim(id)//" cross section estimate:",
     2         gen_sigma/gen_isigma)
           call setcnt(trim(id)//" cross section estimate"//
     3          " num. points:", dble(gen_isigma))
           call setcnt(trim(id)//
     1          " cross section error estimate:",
     2          sqrt(((gen_sigma2/gen_isigma)-(gen_sigma/gen_isigma)**2)/
     3          gen_isigma))
        endif
        if(flg_ubexcess_correct) then
           call setcnt(trim(id)//
     1          " bound violation correction factor:",
     1          gen_totev/mcalls)
        endif
      endif
      flg_nlotest = save_nlotest
      flg_ingen = .false.
      end

      subroutine getpostfix(id,postfix)
      character *(*) id,postfix
      if(id.eq.'btilde') then
         postfix='btl'
      elseif(id.eq.'btildeborn') then
         postfix='btlbrn'
      elseif(id.eq.'remn') then
         postfix='rm'
      elseif(id.eq.'reg') then
         postfix='reg'
      endif
      end

      subroutine allocate_mintw(ptr,ndim,nind,nchannels)
      implicit none
      include 'pwhg_mintw.h'
      type(mintw_pointer) :: ptr
      integer ndim,nind,nchannels
      integer istat
      ptr%ndim = ndim
      ptr%nind = nind
      allocate(ptr%wind(nind+1),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%accind(nind),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%yindmax(nind),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%yindmaxrat(nind),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%xgrid(0:nintervals,ndim),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%xacc(0:nintervals,ndim),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%ymax(nintervals,ndim),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%ymaxrat(nintervals,ndim),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%xmmm(nintervals,ndim),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%xindmmm(nind),stat=istat)
      if(istat.ne.0) goto 999


      allocate(ptr%nchannels,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%nentries,stat=istat)
      if(istat.ne.0) goto 999

      allocate(ptr%totj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%totabsj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%totposj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%totnegj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotabsj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotposj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotnegj(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%results(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%cumulant(nchannels),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%signs(nchannels),stat=istat)
      if(istat.ne.0) goto 999


      allocate(ptr%tot,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%totabs,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%totpos,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%totneg,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etot,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotabs,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotpos,stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%etotneg,stat=istat)
      if(istat.ne.0) goto 999


      allocate(ptr%ifold(ndim),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%indhits(nind),stat=istat)
      if(istat.ne.0) goto 999
      allocate(ptr%nhits(nintervals,ndim),stat=istat)
      if(istat.ne.0) goto 999

      ptr%nchannels = nchannels

      ptr%gen_sigma  = 0
      ptr%gen_sigma2 = 0
      ptr%gen_isigma = 0
      ptr%gen_totev  = 0
      
      return
 999  continue
      
      write(*,*) 'mintwrapper: allocation failed, status=',istat
      call exit(-1)
      end

      subroutine deallocate_mintw(ptr)
      implicit none
      include 'pwhg_mintw.h'
      type(mintw_pointer) :: ptr
      integer istat
      deallocate(ptr%wind,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%accind,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%yindmax,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%yindmaxrat,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%xgrid,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%xacc,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%ymax,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%ymaxrat,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%xmmm,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%xindmmm,stat=istat)
      if(istat.ne.0) goto 999

      deallocate(ptr%nchannels,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%nentries,stat=istat)
      if(istat.ne.0) goto 999


      deallocate(ptr%totj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%totabsj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%totposj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%totnegj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotabsj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotposj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotnegj,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%results,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%cumulant,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%signs,stat=istat)
      if(istat.ne.0) goto 999

      deallocate(ptr%tot,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%totabs,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%totpos,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%totneg,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etot,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotabs,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotpos,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%etotneg,stat=istat)
      if(istat.ne.0) goto 999

      deallocate(ptr%ifold,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%indhits,stat=istat)
      if(istat.ne.0) goto 999
      deallocate(ptr%nhits,stat=istat)
      if(istat.ne.0) goto 999
      return
 999  continue
      write(*,*) 'mintwrapper: deallocation failed, status=',istat
      call exit(-1)
      end

      subroutine getcurrentptrindex(id,icurrent)
      implicit none
      character *(*) id
      integer icurrent
      include 'pwhg_mintw.h'
      integer j
      do j=1,mintw_nptrs
         if(id.eq.mintw_ptrs(j)%id) exit
      enddo
      if(j.le.mintw_nptrs) then
         icurrent = j
      else
         icurrent = -1
      endif
      end



      
      subroutine storexgrids(id,xgriditeration)
      implicit none
      include 'pwhg_mintw.h'
      include 'pwhg_rnd.h'
      character *(*) id
      integer xgriditeration
      integer iun,icu,ndim
      character * 20 postfix
      character * 40 mergelabels
      character * 8 chnum
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      call newunit(iun)
      call getpostfix(id,postfix)
      call getcurrentptrindex(id,icu)
      ndim = mintw_ptrs(icu)%ndim
      if(xgriditeration.gt.0) then
         write(chnum,'(i4)') xgriditeration
         chnum = '-xg'//trim(adjustl(chnum))//'-'
         open(unit=iun,
     1        file=mergelabels(pwgprefix(1:lprefix)//trim(chnum)//'xgrid',
     2        postfix,rnd_cwhichseed,'.dat'),
     3        form='unformatted',status='unknown')
      else
         open(unit=iun,
     1        file=mergelabels(pwgprefix(1:lprefix)//'xgrid',
     2        postfix,rnd_cwhichseed,'.dat'),
     3        form='unformatted',status='unknown')
      endif
      write(iun) mintw_ptrs(icu)%ndim,mintw_ptrs(icu)%nind
      write(iun) mintw_ptrs(icu)%xint
      write(iun) mintw_ptrs(icu)%xgrid
      write(iun) mintw_ptrs(icu)%xacc
      write(iun) mintw_ptrs(icu)%nhits
      write(iun) mintw_ptrs(icu)%wind
      write(iun) mintw_ptrs(icu)%accind
      write(iun) mintw_ptrs(icu)%indhits
c     write also the error on xint. Needed if check_bad_st1 is on
      write(iun) mintw_ptrs(icu)%err
      close(iun)
      end
      
      subroutine loadxgridsn(id,level,iret)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_mintw.h'
      include 'pwhg_rnd.h'
      include 'pwhg_par.h'
      character *(*) id
      integer level,iret
      integer iun,icu,ndim,nind,nchannels
      character * 20 postfix
      integer nfiles,jfile,jdim,jind,jfound,k,kdim
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      character * 100 file
      character * 40 mergelabels
      character * 4 chseed
      character * 8 chnum
      logical lpresent0,lpresent
      integer ilevel,l
      integer parallelstages,xgriditeration
      character * 10 parlabel
      real * 8 powheginput
      double precision, allocatable :: totarr(:,:)
      logical, allocatable :: goodentries(:)
      type(mintw_pointer) :: ptr
      logical check_bad_st1
      integer kcheck_bad,ios

      check_bad_st1 = powheginput("#check_bad_st1") == 1
      if(powheginput('use-old-grid').eq.0) then
         iret=1
         return
      endif

      if(id.eq.'btilde'.or.id.eq.'btildeborn') then
         nchannels = flst_nborn
      elseif(id.eq.'remn') then
         nchannels = flst_nalr
      elseif(id.eq.'reg') then
         nchannels = flst_nregular
      endif

      call newunit(iun)
      call getpostfix(id,postfix)
      call getcurrentptrindex(id,icu)
      if(icu.gt.0) then
         write(*,*) ' loadxgrids: grid with id=',trim(id),' already allocated!'
         write(*,*) ' exiting ...'
         call pwhg_exit(-1)
      endif

c first probe if there are files to load
      nfiles=par_maxseeds

      if(level.le.0) then
         file = mergelabels(pwgprefix(1:lprefix)//'xgrid',
     1        postfix,'none','.dat')
         inquire(file= file,exist=lpresent0)
      else
         lpresent0 = .false.
      endif
      ilevel = 0
      do jfile=1,nfiles
         write(chseed,'(i4)') jfile
         call blanktozero(chseed)
         do l=1,par_maxxgriditerations
c with this statement, it will always exit with ilevel = level,
c or ilevel = 0 if none is found.
            if(level.gt.0.and.l.ne.level) cycle
            write(chnum,'(i4)') l
            chnum = '-xg'//trim(adjustl(chnum))//'-'
            file = mergelabels(pwgprefix(1:lprefix)//trim(chnum)//'xgrid',
     1           postfix,chseed,'.dat')
            inquire(file= file,exist=lpresent)
            if(lpresent) ilevel = max(ilevel,l)
         enddo
      enddo

      if(ilevel.gt.0.and.lpresent0) then
         write(*,*) ' loadxgrids: there are parallel and single-run '//
     1     ' xgrid files ... exiting '
         call pwhg_exit(-1)
      endif

      if(ilevel.eq.0.and..not.lpresent0) then
         iret = -1
         return
      endif

      mintw_nptrs = mintw_nptrs + 1
      icu = mintw_nptrs
      mintw_ptrs(icu)%id = id

      if(ilevel.eq.0) then
         file = mergelabels(pwgprefix(1:lprefix)//'xgrid',
     1        postfix,'none','.dat')
         open(unit=iun,file=file,form='unformatted',status='unknown')
         read(iun) ndim,nind
         call allocate_mintw(mintw_ptrs(icu),ndim,nind,nchannels)

         write(*,*) ' loadxgrids: loading ',file

         read(iun) mintw_ptrs(icu)%xint
         read(iun) mintw_ptrs(icu)%xgrid
         read(iun) mintw_ptrs(icu)%xacc
         read(iun) mintw_ptrs(icu)%nhits
         read(iun) mintw_ptrs(icu)%wind
         read(iun) mintw_ptrs(icu)%accind
         read(iun) mintw_ptrs(icu)%indhits
         close(iun)
         iret = 0
      else
         write(chnum,'(i4)') ilevel
         chnum = '-xg'//trim(adjustl(chnum))//'-'
         if(check_bad_st1) then
            allocate(totarr(2,nfiles),goodentries(nfiles))
            goodentries = .true.
            totarr = 0
         endif
c     this loop is executed only once if check_bad_st1 is false
c     twice otherwise
         do kcheck_bad = 1,2
            ndim = -1
            nind = -1
            jfound = 0
            do jfile=1,nfiles
               if(check_bad_st1) then
                  if(.not. goodentries(jfile)) then
                     cycle
                  endif
               endif
               write(chseed,'(i4)') jfile
               call blanktozero(chseed)
               file = mergelabels(pwgprefix(1:lprefix)//trim(chnum)//'xgrid',
     1              postfix,chseed,'.dat')
               inquire(file= file,exist=lpresent)
               if(lpresent) then
                  jfound = jfound + 1
                  open(unit=iun,file=file,form='unformatted',status='unknown')
                  write(*,*) ' loadxgrids: loading ',file
                  read(iun) jdim,jind
                  if(ndim.lt.0) then
                     ndim = jdim
                     nind = jind
c     At this point we know that there are files to load;
c     but we are carefull not to allocate twice
                     if(kcheck_bad == 1) then
                        call allocate_mintw(ptr,ndim,nind,0)
                        call allocate_mintw(mintw_ptrs(icu),ndim,nind,nchannels)
                     endif
                     mintw_ptrs(icu)%xint    = 0
                     mintw_ptrs(icu)%xacc    = 0
                     mintw_ptrs(icu)%nhits   = 0
                     mintw_ptrs(icu)%accind  = 0
                     mintw_ptrs(icu)%indhits = 0
                  elseif(ndim.ne.jdim.or.nind.ne.jind) then
                     write(*,*) ' loadxgrids: inconsistent grid in'
                     write(*,*) file
                     write(*,*) ' exiting ...'
                     call exit(-1)
                  endif
                  read(iun) ptr%xint
                  read(iun) ptr%xgrid
                  read(iun) ptr%xacc
                  read(iun) ptr%nhits
                  read(iun) ptr%wind
                  read(iun) ptr%accind
                  read(iun) ptr%indhits
                  if(check_bad_st1 .and. kcheck_bad == 1) then
                     read(iun,iostat=ios) ptr%err
                     if(ios /= 0) then
                        write(*,*) ' loadxgridsn: error when reading file ',file
                        write(*,*)
     1                       ' presumably this file was generated before svn version r3598'
                        write(*,*) ' and cannot be used with "check_bad_st1 1"'
                        write(*,*) ' you must generate one further step of xgriditeration'
                        write(*,*) ' without check_bad_st1 before continuing'
                        write(*,*) ' exiting ...'
                        call pwhg_exit(-1)
                     endif
                     totarr(1,jfile) = ptr%xint
                     totarr(2,jfile) = ptr%err
                  endif
                  mintw_ptrs(icu)%xint    = mintw_ptrs(icu)%xint  + ptr%xint
                  mintw_ptrs(icu)%xacc    = mintw_ptrs(icu)%xacc  + ptr%xacc
                  mintw_ptrs(icu)%nhits   = mintw_ptrs(icu)%nhits + ptr%nhits
                  mintw_ptrs(icu)%accind  = mintw_ptrs(icu)%accind  + ptr%accind
                  mintw_ptrs(icu)%indhits = mintw_ptrs(icu)%indhits + ptr%indhits
                  if(jfound.eq.1) then
                     mintw_ptrs(icu)%xgrid = ptr%xgrid
                     mintw_ptrs(icu)%wind = ptr%wind
                  endif
                  close(iun)
               endif
            enddo
            if(jfound == 0) then
               write(*,*) ' loadxgrids: did not find any file for loading'
               write(*,*) ' exiting ...'
               call pwhg_exit(-1)
            else
               iret = 0
            endif
            if(jfound > 1 .and. check_bad_st1 .and. kcheck_bad == 1) then
               call check_stat_consistency(nfiles,totarr,goodentries,iret)
               if(iret == 0) then
                  exit
               endif
            endif
         enddo
         mintw_ptrs(icu)%xint  = mintw_ptrs(icu)%xint/jfound
         call deallocate_mintw(ptr)
         if(check_bad_st1) then
            deallocate(goodentries,totarr)
         endif
      endif

      call getparallelparms(parallelstages,xgriditeration)
      call setparallellabel(parallelstages,xgriditeration,parlabel)

      if(parallelstages.lt.0) then
         file=mergelabels(pwgprefix(1:lprefix),'xgrid-'//trim(postfix),
     1        rnd_cwhichseed,'.top')
      else
         file=mergelabels(pwgprefix(1:lprefix),trim(parlabel)//'-xgrid-'//trim(postfix),
     1        rnd_cwhichseed,'.top')
      endif

      call regridplotopen(file)

      do kdim=1,ndiminteg
         call regrid(mintw_ptrs(icu)%xacc(:,kdim),mintw_ptrs(icu)%xgrid(:,kdim),
     1        mintw_ptrs(icu)%nhits(:,kdim),kdim,nintervals)
      enddo
      if(nind.gt.1) then
         call regridind(nind,mintw_ptrs(icu)%accind,mintw_ptrs(icu)%indhits,
     1        mintw_ptrs(icu)%wind)
         iret = 0
      endif

      call regridplotclose

      end


      subroutine  check_stat_consistency(nentries,res,goodentries,iret)
      implicit none
      integer nentries,iret
      integer indices(nentries)
      double precision res(2,nentries)
      logical goodentries(nentries)
      double precision average,weight,tmpav,tmpweight
      double precision tmp,tmp2(2),ow,oav
      double precision, parameter :: maxdev=10
      integer nonz,j,k,itmp,ij,ijp1
      logical :: ex
      logical :: pwhg_isfinite
      double precision powheginput
      
      do j=1,nentries
         indices(j)=j
      enddo
c     bubblesort
      ex = .true.
      do while(ex)
         ex = .false.
         do j=1,nentries-1 
c     swap in growing order, but put zeros and NaN's at the end.
c     when to swap
            ij = indices(j)
            ijp1 = indices(j+1)
            if(.not. goodentries(ijp1)) cycle
            if(res(2,ijp1) == 0) cycle
            if(.not. goodentries(ij) .or. res(2,ij) == 0 .or. res(2,ij)>res(2,ijp1) ) then
               indices(j) = ijp1
               indices(j+1) = ij
               ex = .true.
            endif
         enddo
      enddo
      do j=1,nentries
         ij = indices(j)
         tmp = res(2,ij)
         if(.not. goodentries(ij) .or. tmp == 0 .or. .not. pwhg_isfinite(tmp) ) then
            nonz = j - 1
            exit
         endif
      enddo
c     Compute the average. Neglect zero, NaNs, infs, etc.
      write(*,*) '************ sorted, unsorted ************'
      do j=1,nonz
         ij = indices(j)
         write(*,*) res(2,ij), res(2,j)
      enddo
      write(*,*) '******** end sorted, unsorted ************'
 
      average = 0
      weight = 0
      do j=1,nonz
         ij = indices(j)
         if(res(1,ij).ne.0) then
            oav = average
            ow = weight
            average = (average*(j-1) + res(1,ij))/j
            weight = sqrt((weight*(j-1))**2 + res(2,ij)**2)/j
            if(j.gt.1) then
               write(*,*) ' old,new av.',oav,average
               write(*,*) ' old,new err.',ow,weight
               write(*,*) ' deviation:',abs(oav-average)/ow
c     after half of the runs
               if(abs(oav-average)/ow.gt.maxdev) then
                  write(*,*) ' check_stat_consistency:'
                  write(*,*)
     1                 ' The program has detected inconsistent results'
                  write(*,*) ' among different runs. The runs:'
                  write(*,*) (indices(k),k=j,nonz)
                  write(*,*) ' look suspicious. '
                  write(*,*) ' Inspect your runs at stage 2 '
                  if(nonz-j+1.gt. nonz/10) then
                     write(*,*)
     1                    ' The fraction of inconsistent runs is too large'
                     write(*,*) ' exiting ...'
                     call pwhg_exit(-1)
                  else
                     write(*,*)
     1                    ' The fraction of inconsistent file is < 10%'
                     write(*,*) ' We discard the following files:'
                     write(*,*) (indices(k),k=j,nonz)
                     write(*,*) ' and reload the others'                     
                     do k=j,nonz
                        goodentries(indices(k)) = .false.
                     enddo
                     iret = -1
                     goto 999
                  endif
               endif
            endif
         endif
      enddo
      iret = 0
 999  continue
      write(*,'(a)') '********** Check_stat_consistency ******'
      do  j=1,nentries
         write(*,*) j, res(1,j),res(2,j),goodentries(j)
      enddo
      write(*,'(a)') '********** end Check_stat_consistency ******'
      end


      subroutine storegrids(id,label)
      implicit none
      include 'pwhg_mintw.h'
      include 'pwhg_rnd.h'
      character *(*) id,label
      integer xgriditeration
      integer iun,icu,ndim
      character * 20 postfix
      character * 40 mergelabels
      character * 20 pwgprefix
      character * 8 chnum
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      call newunit(iun)
      call getpostfix(id,postfix)
      call getcurrentptrindex(id,icu)
      ndim = mintw_ptrs(icu)%ndim
      open(unit=iun,
     1     file=mergelabels(pwgprefix(1:lprefix)//trim(label),
     2     postfix,rnd_cwhichseed,'.dat'),
     3     form='unformatted',status='unknown')

      write(iun) mintw_ptrs(icu)%ndim,mintw_ptrs(icu)%nind,mintw_ptrs(icu)%nchannels
      write(iun) mintw_ptrs(icu)%ifold
      write(iun) mintw_ptrs(icu)%xgrid
      write(iun) mintw_ptrs(icu)%wind
      write(iun) mintw_ptrs(icu)%yindmax
      write(iun) mintw_ptrs(icu)%yindmaxrat
      write(iun) mintw_ptrs(icu)%ymax
      write(iun) mintw_ptrs(icu)%ymaxrat

      write(iun) mintw_ptrs(icu)%nentries
      write(iun) mintw_ptrs(icu)%tot
      write(iun) mintw_ptrs(icu)%totabs
      write(iun) mintw_ptrs(icu)%totpos
      write(iun) mintw_ptrs(icu)%totneg
      write(iun) mintw_ptrs(icu)%etot
      write(iun) mintw_ptrs(icu)%etotabs
      write(iun) mintw_ptrs(icu)%etotpos
      write(iun) mintw_ptrs(icu)%etotneg

      close(iun)
      end

      subroutine loadgrids(id,label,iret)
      implicit none
      character *(*) id,label
      integer iret
      include 'pwhg_rnd.h'
      include 'pwhg_mintw.h'
      include 'pwhg_par.h'
      type(mintw_pointer) :: ptr

      integer ndim,nind,nchannels,jfound,icu,iun
      integer ios
      character * 20 pwgprefix,postfix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      character * 4 chseed, firstfound
      integer j,k,jfile,nfiles
      logical lpresent,manyfiles,filefound
      character * 40 mergelabels
      real * 8 powheginput
      external powheginput
      double precision, allocatable :: totarr(:,:)
      logical, allocatable :: goodentries(:)
      logical firsttime
      logical, save :: check_bad_st2
      integer kcheck_bad, iretcheck
      if(powheginput('use-old-grid').eq.0) then
         iret=1
         return
      endif
      iret=0
      call getpostfix(id,postfix)
      call newunit(iun)

      open(unit=iun,file=mergelabels(pwgprefix(1:lprefix)//trim(label),
     1     postfix,'none','.dat'),
     2     form='unformatted',status='old',iostat=ios)

      write(*,*) ' entering loadgrids('//trim(id)//', '//trim(label)//'),'

      if(ios.eq.0) then
         nfiles=1
         manyfiles=.false.
         write(*,*) ' Opened file '//
     1     mergelabels(pwgprefix(1:lprefix)//trim(label),
     1        postfix,'none','.dat')
         check_bad_st2 = .false.
      else
         nfiles=par_maxseeds
         manyfiles=.true.
         check_bad_st2 =
     1        powheginput("#check_bad_st2") == 1
         if(check_bad_st2) then
            allocate(totarr(2,nfiles),goodentries(nfiles))
            goodentries = .true.
            totarr = 0
         endif
      endif
c Try to open and merge a set of grid files, generated with different
c     random seeds
c     if check_bad_st2 == 1 we go through the loop twice, the first
c     time to find bad runs to be discarded
      do kcheck_bad = 1,2
         filefound=.false.
         jfound=0
         do jfile=1,nfiles
            if(manyfiles) then
               if(check_bad_st2) then
                  if(.not.goodentries(jfile)) cycle
               endif
               write(chseed,'(i4)') jfile
               call blanktozero(chseed)
               inquire(file=mergelabels(pwgprefix(1:lprefix)//trim(label),postfix,
     1              chseed,'.dat'),exist=lpresent)
               if(.not.lpresent) cycle
               open(unit=iun,file=mergelabels(pwgprefix(1:lprefix)//trim(label),postfix,
     1              chseed,'.dat'),
     2              form='unformatted',status='old',iostat=ios)
               if(ios.ne.0) then
                  iret=-1
                  return
               else
                  write(*,*)
     1                 ' Opened ',mergelabels(pwgprefix(1:lprefix)//trim(label),postfix,
     2                 chseed,'.dat')
               endif
            endif

            filefound=.true.

            jfound = jfound + 1

            read(iun,iostat=ios) ndim,nind,nchannels
            if(ios.ne.0) goto 999

            if(jfound.eq.1) then
               call allocate_mintw(ptr,ndim,nind,nchannels)
            endif

            read(iun,iostat=ios) ptr%ifold
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%xgrid
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%wind
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%yindmax
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%yindmaxrat
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%ymax
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%ymaxrat
            if(ios.ne.0) goto 998

            read(iun,iostat=ios) ptr%nentries
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%tot
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%totabs
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%totpos
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%totneg
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%etot
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%etotabs
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%etotpos
            if(ios.ne.0) goto 998
            read(iun,iostat=ios) ptr%etotneg
            if(ios.ne.0) goto 998

            if(check_bad_st2) then
               totarr(1,jfile) = ptr%totabs
               totarr(2,jfile) = ptr%etotabs
            endif
            
            if(jfound.eq.1) then
               if(kcheck_bad == 1) then
                  call getcurrentptrindex(id,icu)
                  if(icu.gt.0) then
                     write(*,*) ' loadgrids: id '//trim(id)//' already there!'
                     write(*,*) ' exiting ...'
                     call exit(-1)
                  else
                     mintw_nptrs = mintw_nptrs + 1
                     icu= mintw_nptrs
                     mintw_ptrs(icu)%id = id
                  endif
                  call allocate_mintw(mintw_ptrs(icu),ndim,nind,nchannels)
               endif
               firstfound = chseed
               mintw_ptrs(icu)%ifold = ptr%ifold 
               mintw_ptrs(icu)%xgrid = ptr%xgrid 
               mintw_ptrs(icu)%wind = ptr%wind
               mintw_ptrs(icu)%yindmax = ptr%yindmax
               mintw_ptrs(icu)%yindmaxrat = ptr%yindmaxrat
               mintw_ptrs(icu)%ymax = ptr%ymax
               mintw_ptrs(icu)%ymaxrat = ptr%ymaxrat
               mintw_ptrs(icu)%nentries = ptr%nentries
               mintw_ptrs(icu)%tot = ptr%tot
               mintw_ptrs(icu)%totabs = ptr%totabs
               mintw_ptrs(icu)%totpos = ptr%totpos
               mintw_ptrs(icu)%totneg = ptr%totneg
               mintw_ptrs(icu)%etot = ptr%etot
               mintw_ptrs(icu)%etotabs = ptr%etotabs
               mintw_ptrs(icu)%etotpos = ptr%etotpos
               mintw_ptrs(icu)%etotneg = ptr%etotneg
            else
               if(.not.all(ptr%xgrid.eq.mintw_ptrs(icu)%xgrid)) then
                  write(*,*) ' error loading grids: '
                  write(*,*)  pwgprefix(1:lprefix)//label//'-'//
     1                 rnd_cwhichseed//'.dat does not have the same importance'
                  write(*,*) 'sampling grid as ',pwgprefix(1:lprefix)
     1                 //label//'-'//firstfound//'.dat'
                  write(*,*) ' exiting ...'
                  call exit(-1)
               endif
               if(.not.all(ptr%ifold.eq.mintw_ptrs(icu)%ifold)) then
                  write(*,*) ' error loading grids: '
                  write(*,*)  pwgprefix(1:lprefix)//label//'-'//
     1                 rnd_cwhichseed//'.dat does not have the same folding as'
                  write(*,*) pwgprefix(1:lprefix)
     1                 //label//'-'//firstfound//'.dat'
                  write(*,*) ' exiting ...'
                  call exit(-1)
               endif
               mintw_ptrs(icu)%ymax = max(mintw_ptrs(icu)%ymax,ptr%ymax)
               mintw_ptrs(icu)%ymaxrat = max(mintw_ptrs(icu)%ymaxrat,ptr%ymaxrat)
               mintw_ptrs(icu)%yindmax = max(mintw_ptrs(icu)%yindmax,ptr%yindmax)
               mintw_ptrs(icu)%yindmaxrat = max(mintw_ptrs(icu)%yindmaxrat,ptr%yindmaxrat)

               call combineerrors(mintw_ptrs(icu)%tot,mintw_ptrs(icu)%etot,ptr%tot,ptr%etot)
               call combineerrors(mintw_ptrs(icu)%totabs,mintw_ptrs(icu)%etotabs,ptr%totabs,ptr%etotabs)
               call combineerrors(mintw_ptrs(icu)%totpos,mintw_ptrs(icu)%etotpos,ptr%totpos,ptr%etotpos)
               call combineerrors(mintw_ptrs(icu)%totneg,mintw_ptrs(icu)%etotneg,ptr%totneg,ptr%etotneg)

            endif
            close(iun)
         enddo
         if(filefound) then
            if(manyfiles .and. check_bad_st2) then
c     check that the different runs are more or less consistent
               if(kcheck_bad == 1) then
                  call check_stat_consistency(nfiles,totarr,
     1                 goodentries,iretcheck)
                  if(iretcheck.eq.-1) then
                     cycle
                  endif
               endif
            endif
            call deallocate_mintw(ptr)
            iret = 0
         else
            iret = -1
         endif
         exit
      enddo
      if(check_bad_st2) then
         deallocate(totarr,goodentries)
      endif
      return
 998  continue
      call deallocate_mintw(ptr)
 999  continue
      iret=-1
      
      contains
         subroutine combineerrors(tot,etot,t,e)
         implicit none
         real *  8 tot,etot,t,e,rjfound,rnentries
         rjfound = jfound
         rnentries = ptr%nentries
         etot = sqrt( (etot**2*(rjfound-1)**2+e**2)/rjfound**2
     1        + (rjfound-1)*(tot-t)**2/(rjfound**3*rnentries) )
         tot = (tot*(rjfound-1)+t)/rjfound
         end subroutine
      end
      
        

      subroutine getparallelparms(parallelstage,xgriditeration)
      implicit none
      include 'pwhg_par.h' 
      include 'pwhg_rnd.h' 
      integer parallelstage,xgriditeration
      logical ini
      integer pstage,xiteration
      data ini/.true./
      save ini,pstage,xiteration
      real * 8 powheginput
      external powheginput
      if(ini) then
         pstage = powheginput('#parallelstage')
         xiteration = powheginput('#xgriditeration')
         if(pstage.gt.0) then
            if(xiteration.gt.par_maxxgriditerations) then
               write(*,*) ' getparallelparms:'
               write(*,*) ' POWHEG is compiled with a maximum'
               write(*,*) ' number of x-grid iterations=',
     1              par_maxxgriditerations
               write(*,*) ' increase the par_maxxgriditerations parameter'
               write(*,*) ' in the pwhg_par.h file to use more.'
               write(*,*) ' (BUT YOU SHOULD NOT NEED MORE THAN 3 or 4!'
               write(*,*) ' increase ncall1 instead)'
               write(*,*) ' exiting ...'
               call pwhg_exit(-1)
            endif
            if(xiteration.lt.1) then
               write(*,*) ' getparallelparms:'
               write(*,*) ' xgriditeration=',xiteration,' not allowed,'
               write(*,*) ' exiting ...'
               call pwhg_exit(-1)
            endif
            if(rnd_cwhichseed.eq.'none') then
               write(*,*) ' getparallelparms:'
               write(*,*) ' with parallelstage also manyseeds '
               write(*,*) ' must be set'
               write(*,*) ' exiting ...'
               call pwhg_exit(-1)
            endif
         endif
         ini = .false.
      endif
      parallelstage = pstage
      xgriditeration = xiteration
      end

               
         
      subroutine blanktozero(string)
      character *(*) string
      integer l,k
      l=len(string)
      do k=1,l
         if(string(k:k).eq.' ') string(k:k)='0'
      enddo
      end


      subroutine doregrid(ptr)
      implicit none
      include 'pwhg_mintw.h'
      type(mintw_pointer) :: ptr
      integer kdim
      do kdim=1,ptr%ndim
         call regrid(ptr%xacc(:,kdim),ptr%xgrid(:,kdim),
     1        ptr%nhits(:,kdim),kdim,nintervals)
      enddo
      if(ptr%nind.gt.1) then
         call regridind(ptr%nind,ptr%accind,ptr%indhits,ptr%wind)
      endif
      end

      
      subroutine resettotals(ptr)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_mintw.h'
      include 'pwhg_flst.h'
      type (mintw_pointer) :: ptr
      real * 8, pointer :: tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg
      real * 8, pointer :: totj(:),totabsj(:),totposj(:),totnegj(:),
     1     etotj(:),etotabsj(:),etotposj(:),etotnegj(:)
      integer,  pointer ::  nentries
      integer, pointer ::  nchannels
      common/cmintotals/totj,totabsj,totposj,totnegj,etotj,etotabsj,etotposj,etotnegj,
     1     tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg,nentries,nchannels
      integer j
      totj => ptr%totj
      totabsj => ptr%totabsj
      totposj => ptr%totposj
      totnegj => ptr%totnegj
      etotj    => ptr%etotj
      etotabsj => ptr%etotabsj
      etotposj => ptr%etotposj
      etotnegj => ptr%etotnegj

      tot => ptr%tot
      totabs => ptr%totabs
      totpos => ptr%totpos
      totneg => ptr%totneg
      etot    => ptr%etot
      etotabs => ptr%etotabs
      etotpos => ptr%etotpos
      etotneg => ptr%etotneg

      nchannels => ptr%nchannels
      nentries => ptr%nentries
      
      nentries=0
      tot=0
      etot=0
      totabs=0
      etotabs=0
      totpos=0
      etotpos=0
      totneg=0
      etotneg=0
      do j=1,nchannels
         totj(j)=0
         etotj(j)=0
         totabsj(j)=0
         etotabsj(j)=0
         totposj(j)=0
         etotposj(j)=0
         totnegj(j)=0
         etotnegj(j)=0
      enddo
      end

      subroutine adduptotals(results,n)
      implicit none
      include 'nlegborn.h'
      integer n
      real * 8 results(n)
      real * 8, pointer :: tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg
      real * 8, pointer :: totj(:),totabsj(:),totposj(:),totnegj(:),
     1     etotj(:),etotabsj(:),etotposj(:),etotnegj(:)
      integer,  pointer ::  nentries
      integer, pointer ::  nchannels
      common/cmintotals/totj,totabsj,totposj,totnegj,etotj,etotabsj,etotposj,etotnegj,
     1     tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg,nentries,nchannels
      real * 8 dtot,dtotabs,dtotpos,dtotneg
      integer j
      nentries=nentries+1
      dtot=0
      dtotabs=0
      dtotpos=0
      dtotneg=0
      do j=1,n
         dtot=dtot+results(j)
         dtotabs=dtotabs+abs(results(j))
         if(results(j).gt.0) then
            dtotpos=dtotpos+results(j)
         else
            dtotneg=dtotneg-results(j)
         endif
      enddo
      tot=tot+dtot
      totabs=totabs+dtotabs
      totpos=totpos+dtotpos
      totneg=totneg+dtotneg      
      etot=etot+dtot**2
      etotabs=etotabs+dtotabs**2
      etotpos=etotpos+dtotpos**2
      etotneg=etotneg+dtotneg**2
c j contributions
      do j=1,n
         dtot=results(j)
         dtotabs=abs(results(j))
         if(results(j).gt.0) then
            dtotpos=results(j)
         else
            dtotneg=-results(j)
         endif
         totj(j)=totj(j)+dtot
         totabsj(j)=totabsj(j)+dtotabs
         totposj(j)=totposj(j)+dtotpos
         totnegj(j)=totnegj(j)+dtotneg     
         etotj(j)=etotj(j)+dtot**2
         etotabsj(j)=etotabsj(j)+dtotabs**2
         etotposj(j)=etotposj(j)+dtotpos**2
         etotnegj(j)=etotnegj(j)+dtotneg**2
      enddo
      end

      subroutine finaltotals(id)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      character *(*) id
      real * 8, pointer :: tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg
      real * 8, pointer :: totj(:),totabsj(:),totposj(:),totnegj(:),
     1     etotj(:),etotabsj(:),etotposj(:),etotnegj(:)
      integer,  pointer ::  nentries
      integer, pointer ::  nchannels
      common/cmintotals/totj,totabsj,totposj,totnegj,etotj,etotabsj,etotposj,etotnegj,
     1     tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg,nentries,nchannels
      integer n,j,k
      character * 80 format
      real * 8 tmp_totj,tmp_etotj,tmp_totabsj,
     1     tmp_etotabsj,tmp_totposj,tmp_etotposj,
     2     tmp_totnegj,tmp_etotnegj
      real * 8 tmp
      integer iun
      character * 20 pwgprefix
      integer lprefix
      common/cpwgprefix/pwgprefix,lprefix
      real * 8 powheginput
      external powheginput
      n=nentries

      etot=sqrt((etot/n-(tot/n)**2)/n)
      etotabs=sqrt((etotabs/n-(totabs/n)**2)/n)
      etotpos=sqrt((etotpos/n-(totpos/n)**2)/n)
      etotneg=sqrt((etotneg/n-(totneg/n)**2)/n)

      tot=tot/n
      totabs=totabs/n
      totpos=totpos/n
      totneg=totneg/n
c
      if(powheginput('#ubsigmadetails').eq.1) then
         call newunit(iun)
         open(iun,file=pwgprefix(1:lprefix)//'sigma-details-'//trim(id)//'.dat')
         format='(      (i8,1x),4(a,1x,d10.4,a,d7.1))'
         write(format(2:4),'(i3)') nlegborn
         tmp=0
         do j=1,flst_nborn
            tmp_totj=totj(j)/n
            tmp_etotj=sqrt((etotj(j)/n-(totj(j)/n)**2)/n)
            tmp_totabsj=totabsj(j)/n
            tmp_etotabsj=sqrt((etotabsj(j)/n-(totabsj(j)/n)**2)/n)
            tmp_totposj=totposj(j)/n
            tmp_etotposj=sqrt((etotposj(j)/n-(totposj(j)/n)**2)/n)
            tmp_totnegj=totnegj(j)/n
            tmp_etotnegj=sqrt((etotnegj(j)/n-(totnegj(j)/n)**2)/n)
            write(iun,format) (flst_born(k,j),k=1,nlegborn),
     1           'tot:',tmp_totj,' +- ',tmp_etotj,
     2           '; abs:',tmp_totabsj,' +- ',tmp_etotabsj,
     3           '; pos:',tmp_totposj,' +- ',tmp_etotposj,
     4           '; neg:',tmp_totnegj,' +- ',tmp_etotnegj
            tmp=tmp+tmp_totj
         enddo
         write(iun,*) tmp
         close(iun)
      endif
      end



      subroutine writestat(iunstat)
      implicit none
      integer iunstat
      include 'pwhg_mintw.h'
      integer icurrent
      real * 8 totpos,totneg,tot,etotpos,etotneg,etot
      totpos = 0
      totneg = 0
      tot = 0
      etotpos = 0
      etotneg = 0
      etot = 0
      
      do icurrent=1,mintw_nptrs
         write(*,*) mintw_ptrs(icurrent)%id
     1   //' pos.   weights:', mintw_ptrs(icurrent)%totpos,' +- ',
     2        mintw_ptrs(icurrent)%etotpos
         totpos = totpos + mintw_ptrs(icurrent)%totpos
         etotpos = sqrt(etotpos**2 + mintw_ptrs(icurrent)%etotpos**2 )
         write(*,*) mintw_ptrs(icurrent)%id
     1   //' |neg.| weights:', mintw_ptrs(icurrent)%totneg,' +- ',
     2        mintw_ptrs(icurrent)%etotneg
         totneg = totneg + mintw_ptrs(icurrent)%totneg
         etotneg = sqrt(etotneg**2 + mintw_ptrs(icurrent)%etotneg**2 )
         write(*,*) mintw_ptrs(icurrent)%id
     1   //' total (pos.-|neg.|):', mintw_ptrs(icurrent)%tot,' +- ',
     2        mintw_ptrs(icurrent)%etot
         tot = tot + mintw_ptrs(icurrent)%tot
         etot = sqrt(etot**2 + mintw_ptrs(icurrent)%etot**2 )

         write(iunstat,*) mintw_ptrs(icurrent)%id
     1   //' pos.   weights:', mintw_ptrs(icurrent)%totpos,' +- ',
     2        mintw_ptrs(icurrent)%etotpos
         write(iunstat,*) mintw_ptrs(icurrent)%id
     1   //' |neg.| weights:', mintw_ptrs(icurrent)%totneg,' +- ',
     2        mintw_ptrs(icurrent)%etotneg
         write(iunstat,*) mintw_ptrs(icurrent)%id
     1   //' total (pos.-|neg.|):', mintw_ptrs(icurrent)%tot,' +- ',
     2        mintw_ptrs(icurrent)%etot
      enddo

      write(*,*) 'grand total'
     1     //' pos.   weights:', totpos,' +- ',
     2     etotpos
      write(*,*) 'grand total'
     1     //' |neg.| weights:', totneg,' +- ',
     2     etotneg
      write(*,*) 'grand total'
     1     //' total (pos.-|neg.|):', tot,' +- ',
     2     etot
      
      write(iunstat,*) 'grand total'
     1     //' pos.   weights:', totpos,' +- ',
     2     etotpos
      write(iunstat,*) 'grand total'
     1     //' |neg.| weights:', totneg,' +- ',
     2     etotneg
      write(iunstat,*) 'grand total'
     1     //' total (pos.-|neg.|):', tot,' +- ',
     2     etot
      
      end
