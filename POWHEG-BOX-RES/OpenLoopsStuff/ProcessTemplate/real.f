      subroutine setreal(p,rflav,amp2)
c Wrapper subroutine to call the OL real emission matrix
      implicit none
      include 'pwhg_math.h'
      include 'pwhg_st.h'
      include 'nlegborn.h'
      real * 8, intent(in)  :: p(0:3,nlegrealexternal)
      integer,  intent(in)  :: rflav(nlegrealexternal)
      real * 8, intent(out) :: amp2

      call openloops_real(p,rflav,amp2)
      end


      subroutine realcolour_lh
c Wrapper subroutine to call the OL code to associate
c a (leading) color structure to an event.
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_cache.h'
      include 'pwhg_flg.h'
      include 'LesHouches.h'
      include 'pwhg_kn.h'
      type(cache_pointer), save :: cacheptr
      integer, save :: cacheind,cachestatus=0
      integer nlegs
      integer rflav(nlegreal),rres(nlegreal)
      integer rflavstrip(nlegrealexternal),outinmap(nlegrealexternal)
      integer nout
      integer color(2,nlegreal)
      integer ireg,icount,iprint,iret,j
      integer ifl, i
      integer is_fs(nlegreal),isfslength,rflav0(flst_numfsb+3)
      real * 8 p0(0:3,flst_numfsb+3)
      real * 8 coef

      call getisfsparticles(flst_ireallength,flst_regular(:,rad_regularsubp),
     &              flst_regularres(:,rad_regularsubp),isfslength,is_fs)
      if(flst_numfsb+3 /= isfslength) then
         write(*,*) ' real_ampsq: length mismatch in arrays'
         call exit(-1)
      endif
      do j=1,isfslength
        rflav0(j)=flst_regular(is_fs(j),rad_regularsubp)
        p0(:,j)=kn_preal(:,is_fs(j))
      enddo

      nlegs = flst_regularlength(ireg)
      rflav(1:nlegs) = flst_regular(1:nlegs,ireg)
      rres(1:nlegs) = flst_regularres(1:nlegs,ireg)

      call stripresonances(nlegs,rflav,rres,nout,rflavstrip,outinmap)

      icount = 0
      iprint = 200

      call allow_all_colors

 1    continue
      icount = icount + 1
      if(icount.gt.1000000) then
        write(*,*) ' realcolour_lh: cannot find colour configuration '
        write(*,*) ' consistent with resonance assignment. Exiting ... '
        call exit(-1)
      elseif(icount.gt.iprint) then
        write(*,*) ' realcolour_lh:',iprint,' tries; keep trying'
        iprint = iprint*10
      endif

      ! call OL color flow
      call openloops_realcolour_ifl(p0,rflav0,color,ifl)

      do j=1,nlegrealexternal
         icolup(:,outinmap(j))=color(:,j)
      enddo

      call complete_resonance_colours(iret)
      if(iret.lt.0) then
         call disallow_color(ifl)
         goto 1
      endif

      end

      subroutine stripresonances(nin,flavin,resin,nout,flavout,outinmap)
      implicit none
      integer nin,nout,flavin(nin),resin(nin),flavout(nin),outinmap(nin)
      logical markfs(nin)
      integer j
      markfs = .true.
      do j=3,nin
         if(resin(j).ne.0) then
            markfs(resin(j)) = .false.
         endif
      enddo
      nout=2
      flavout(1:2) = flavin(1:2)
      outinmap(1:2) = (/ 1,2 /)
      do j = 3,nin
         if(markfs(j)) then
            nout = nout + 1
            flavout(nout) = flavin(j)
            outinmap(nout) = j
         endif
      enddo
      end
