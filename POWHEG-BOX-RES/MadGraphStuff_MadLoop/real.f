      subroutine setreal(p,rflav,amp2)
c Wrapper subroutine to call the MadGraph real emission matrix
c elements and set the event-by-event couplings constant
      implicit none
      include 'pwhg_math.h'
      include 'pwhg_st.h'
      real * 8 p(0:3,*)
      integer rflav(*)
      real * 8 amp2
      call set_ebe_couplings
      call sreal_proc(p,rflav,amp2)
c Cancel as/(2pi) associated with amp2. It will be put back by real_ampsq
      amp2 = amp2/(st_alpha/(2d0*pi))     
      end

      subroutine setreal_colouramps(p,rflav)
c this subroutine should be called to set the colour amplitude
c of the real cross section in madgraph. Should be used before
c choosing the colour configuration, with a call to realcolour_lh
c p and rflav should be the momenta and flavour WITHOUT resonances.
      implicit none
      real * 8 p(0:3,*),amp2
      integer rflav(*)
      call setreal(p,rflav,amp2)
      end

      subroutine realcolour_lh
c Wrapper subroutine to call the MadGraph code to associate
c a (leading) color structure to an event.
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_rad.h'
      include 'pwhg_cache.h'
      include 'pwhg_flg.h'
      include 'LesHouches.h'
      include 'Madlib/nexternal.inc'
      type(cache_pointer), save :: cacheptr
      integer, save :: cacheind,cachestatus=0
      integer nlegs
      integer rflav(nlegreal),rres(nlegreal)
      integer rflavmg(nexternal),outinmap(nexternal)
      integer nout
      integer color(2,nlegreal)
      integer ireg,icount,iprint,iret,j
      integer ifl
      real * 8 coef

c     The following block is to avoid using undefined intermediate
c     MadGraph results when smartsig is active
      if( flg_smartsig .and. cachestatus == 0 ) then
c     will do this until the cache is really used, i.e. until cachestatus=1
         call get_cache_pointer('sigregular',cacheind,cacheptr,cachestatus)
      endif

      if( flg_smartsig .and. cachestatus == 1) then
         call get_cache_value(cacheptr,rad_regularsubp,ireg,coef)
         if(ireg == -1) ireg = rad_regularsubp
      else
         ireg = rad_regularsubp
      endif
c ------------

      nlegs = flst_regularlength(ireg)
      rflav(1:nlegs) = flst_regular(1:nlegs,ireg)
      rres(1:nlegs) = flst_regularres(1:nlegs,ireg)

      call stripresonances(nlegs,rflav,rres,nout,rflavmg,outinmap)

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

      call real_color_ifl(rflavmg,color,ifl)

      do j=1,nexternal
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
