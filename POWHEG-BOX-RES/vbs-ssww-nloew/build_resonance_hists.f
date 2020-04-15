      subroutine build_resonance_histories
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_res.h'
      integer reallength,bornlength
      integer nregions,iregions(2,maxregions)
      integer jreal,jregion,jborn
      call reset_res_histories
      bornlength = flst_numfinal + 2
      do jborn = 1,flst_nborn
         flst_born(2,jborn) = - flst_born(2,jborn) 
         call find_resonance_histories(bornlength,flst_born(:,jborn),flst_bornres(:,jborn),
     1           res_powew,res_powst)
         flst_born(2,jborn) = - flst_born(2,jborn) 
      enddo

      call pwhg_res_histos_born
      call deallocate_res_histories
      call reset_res_histories
      reallength = flst_numfinal + 3
      do jreal=1,flst_nreal
c one more call for no singular regions
         flst_real(2,jreal) = - flst_real(2,jreal)
         ! qcd
!         call find_resonance_histories(reallength,flst_real(:,jreal),flst_realres(:,jreal),
!     1           res_powew,res_powst+1)
         call find_resonance_histories(reallength,flst_real(:,jreal),flst_realres(:,jreal),
     1        res_powew+1,res_powst)
         flst_real(2,jreal) = - flst_real(2,jreal) 
      enddo
c 
      call pwhg_res_histos_real
      call deallocate_res_histories
      end

      recursive subroutine find_resonance_histories(n,flav,resflav,powew,powst)
c     This subroutine finds (recursively) all resonance histories that are compatible with the
c     flavour structure given in <flav>, including some resonances already present. For each found
c     resonance history, a subroutine <store_res_history> is called to deliver the newly found structure.
      implicit none
      integer n,flav(n),resflav(n),powew,powst
      integer nnew,newflav(n+1),newresflav(n+1)
      integer jpart,kpart,kres,nres
c must be dimensioned to the maximum number of resonances that can arise from a given pair.
c In the standard model this is no larger than 3 (q-qbar -> Z,H,g, q W -> 3 cabibbo related quarks)
c Here we exaggerate in safety.
      integer res(10),ordew(10),ordst(10)
      integer jem
      logical not_add
      integer level,iret,j
      data level/0/
      save level
c this keeps track of the nesting level of recursion; it is only used for debugging
      level=level+1
c     not_add will stay false if no pair of particles is found that can come
c     from a resonance
      not_add = .false.
c     We leave the first particle fixed; we loop over all pairs of particles that do not already
c     arise from the splitting or decay of another particle.
      do jpart=2,n-1
         do kpart=jpart+1,n
c see from which resonances jpart and kpart can come from.
c here we include also intermediate gluons, light quarks and light leptons.
c They will be removed at the end
            if(resflav(jpart) == 0 .and. resflav(kpart) == 0) then
               call mother_resonance(flav(jpart),flav(kpart),nres,res,ordew,ordst)
            else
               cycle
            endif
c if no resonances, go to the next group of particles
            if(nres.eq.0) cycle
            do kres=1,nres
c     The power of couplings required for the splitting may be tolarge
               if(ordew(kres).gt.powew.or.ordst(kres).gt.powst) cycle
c     Insert the new mother particle at the end of the flavour list
               call insert_resonance(n,flav,resflav,jpart,kpart,res(kres),
     1              newflav,newresflav)
c     Go on finding new mergings starting with the new list recursively
               call find_resonance_histories(n+1,newflav,newresflav,
     1                 powew-ordew(kres),powst-ordst(kres))
               not_add = .true.
            enddo
         enddo
      enddo
      if(.not.not_add .and. powew == 0 .and. powst == 0
     1     .and. flav(1) == flav(n) ) then
c     If we are here, then
c     1) no pairs were found that can be merged further
c     2) the vertices that were found have exhausted the available strong and weak coupling
c     3) the last merging brought back (consistently) to the particle that was kept fixed
c Check if this structure is acceptable
         nnew = n
         newflav(1:n) = flav
         newresflav(1:n) = resflav
         call clean_resonance_structure(nnew,newflav,newresflav)
         if(nnew.gt.0) then
            iret = 0
            call store_res_history(nnew,newflav,newresflav,iret)
c            if(iret > 0) then
c               write(*,*) ' found contribution; original:'
c               write(*,*) (j, j=1,n)
c               write(*,*) flav
c               write(*,*) resflav
c               write(*,*) ' clean:'
c               write(*,*) (j, j=1,nnew )
c               write(*,*) newflav(1:nnew)
c               write(*,*) newresflav(1:nnew)
c            endif
         endif
      endif
      level = level - 1
      end

      subroutine insert_resonance(n,flav,resflav,jpart,kpart,res,
     1     newflav,newresflav)
      implicit none
      integer, parameter:: invalid=-2001
      integer n,mflav(n),flav(n),resflav(n),jpart,kpart,res,
     1     newflav(n+1),newresflav(n+1)
      integer k,respos
      newflav(1:n)    = flav(1:n)
      newresflav(1:n) = resflav(1:n)
      newflav(n+1) = res
      newresflav(n+1) = 0
      newresflav(jpart) = n+1
      newresflav(kpart) = n+1
      end

      subroutine mother_resonance(flj,flk,nres,res,ordew,ordst)
c given flavours flj and flk (with pdg flavour labels except for
c the gluon (label 0)), return in res%i(1:nres) a list of possible resonances
c that give rise to them, with the orders in ew and strong
c g-coupling in ordew(1:nres) and ordst(1:nres).
      implicit none
      integer flj,flk,nres
      integer res(10),ordew(10),ordst(10)
      include 'pwhg_ckm.h'
      integer fla,flb,fl,j
c if flj and flk are different we want them to be order:
c the one with the smallest absolute value first;
c if absolute values are identical, the negative one first.
c This reduces the number of cases to consider.
      if(abs(flj) > abs(flk)) then
         fla = flk
         flb = flj
      elseif(abs(flj) < abs(flk)) then
         fla = flj
         flb = flk
      else
         fla = min(flj,flk)
         flb = max(flj,flk)
      endif
      nres = 0
c QCD couplings
      if(fla == 0) then
         if(flb == 0) then
            call addstres(0)
            return
         elseif(abs(flb) <= 6) then
            call addstres(flb)
            return
         else
c a gluon cannot merge with anything other than gluons and quarks
            return
         endif
      elseif(abs(fla) <= 6 .and. fla+flb == 0) then
         call addstres(0)
c here we don't return; we will find also EW resonances.
      endif

c from now on fla cannot be 0
c EW couplings
      if(abs(flb) <= 16) then
c they are both leptons or quarks
         if(fla+flb == 0) then
c they are opposite leptons or quarks
            call addewres(23)
            call addewres(25)
            return
         else
c they are both leptons (different flavours)
            fl = comesfromw(fla,flb)
            if(fl.ne.0) then
               call  addewres(fl*24)
            endif
         endif
         return
      endif
      if(abs(fla) <= 16) then
c now fla is a lepton or quark, flb is Z, gamma, H or W
         if(flb == 23 .or. flb == 25) then
c We can eliminate H couplings to anything but top.
c Some application may need the Hbb coupling ...
            if(flb == 25 .and. abs(fla) /=6) return
            call addewres(fla)
            return
         elseif(flb == 22) then
            if(abs(fla) <= 6 .or. mod(fla,2) /= 0) then
               call addewres(fla)
               return
            endif
            return
         endif
c     now fla is a lepton or quark, flb is W+ or W-
         if(abs(flb) == 24) then
c     We can eliminate H couplings to anything but top.
c     Some application may need the Hbb coupling ...
            do j=-16,16
               fl = comesfromw(-fla,j)
               if(24*fl == flb) then
                  call addewres(j)
               endif
            enddo
            return
         endif
         return
      endif
c now fla and flb are both ew bosons
      if(abs(fla) == 24 .and. fla+flb == 0) then
         call addewres(23)
         call addewres(25)
         return
      endif
      if(abs(fla) == 24 .and. flb == 25) then
         call addewres(fla)
         return
      endif         
      if(abs(flb) == 24 .and. (fla == 23 .or. fla == 22) ) then
         call addewres(flb)
         return
      endif
      if(fla == 23 .and. flb == 23) then
         call addewres(25)
         return
      endif
      if(fla == 23 .and. flb == 25) then
         call addewres(23)
         return
      endif
      if(fla == 25 .and. flb == 25) then
         call addewres(25)
         return
      endif

      contains
         subroutine addewres(fl)
         implicit none
         integer fl
         nres = nres + 1
         res(nres) = fl
         ordew(nres) = 1
         ordst(nres) = 0
         end subroutine addewres

         subroutine addstres(fl)
         implicit none
         integer fl
         nres = nres + 1
         res(nres) = fl
         ordew(nres) = 0
         ordst(nres) = 1
         end subroutine addstres

         integer function comesfromw(fl1,fl2)
         implicit none
         integer fl1,fl2,n1gen,n2gen,ch1,ch2
         if(abs(fl1)<=6.and.abs(fl2)<=6) then
            if(abs(fl1)<=2) then
               n1gen = 1
            elseif(abs(fl1)<=4) then
               n1gen = 2
            else
               n1gen = 3
            endif
            if(abs(fl2)<=2) then
               n2gen = 1
            elseif(abs(fl2)<=4) then
               n2gen = 2
            else
               n2gen = 3
            endif
            if(ckm_diag .and. n1gen /= n2gen) then
               comesfromw = 0
               return
            elseif(ckm_cabibbo .and. n1gen /= n2gen
     1              .and. (n1gen==3 .or. n2gen==3)) then
               comesfromw = 0
               return
            endif
            if(mod(fl1,2) == 0) then
               ch1 = sign(2,fl1)
            else
               ch1 = - sign(1,fl1)
            endif
            if(mod(fl2,2) == 0) then
               ch2 = sign(2,fl2)
            else
               ch2 = - sign(1,fl2)
            endif
            if(abs(ch1+ch2) == 3) then
               comesfromw = (ch1+ch2)/3
               return
            endif
         elseif(abs(fl1) >= 11 .and. abs(fl2) >= 11) then
            if(abs(fl1+fl2) == 1) then
               if(mod(fl1,2) == 0) then
                  ch1 = 0
               else
                  ch1 = - sign(1,fl1)
               endif
               if(mod(fl2,2) == 0) then
                  ch2 = 0
               else
                  ch2 = - sign(1,fl2)
               endif
               if(abs(ch1+ch2) == 1) then
                  comesfromw = ch1+ch2
                  return
               endif
            endif
         endif
         comesfromw = 0
         end function comesfromw
      end

      recursive subroutine store_res_history(n,flav,resflav,iret)
      implicit none
      integer n,flav(n),resflav(n),iret
      integer flav1(n),flav2(n),
     1        resflav1(n),resflav2(n)
      integer j,k,l,res
c before storing the resonance, this subroutine checks if there is a resonance that is son of the
c same resonance. In this case, it looks for a gamma or gluon radiated by the mother resonance,
c and generates two resonance histories, both with the resonance son of a resonance with the same
c flavour removed. In one of the contribution, the gluon/gamma is son of the mother resonance, in the
c second contribution it is son of the granmother.
      iret = 0
      do j=3,n
         res = resflav(j)
         if(res.gt.0) then
            if(flav(j).eq.flav(res)) then
               do k=3,n
                  if((flav(k).eq.0.or.flav(k).eq.22).and.resflav(k).eq.res) then
                     flav1(1:j-1)=flav(1:j-1)
                     flav1(j:n-1)=flav(j+1:n)
                     resflav1(1:j-1)=resflav(1:j-1)
                     resflav1(j:n-1)=resflav(j+1:n)
                     do l=j,n-1
                        if(resflav1(l).gt.j) then
                           resflav1(l)=resflav1(l)-1
                        elseif(resflav1(l).eq.j) then
                           resflav1(l)=res
                        endif
                     enddo
                     flav2 = flav1
                     resflav2 = resflav1
                     resflav2(k-1) = resflav2(res)
                     call store_res_history(n-1,flav1,resflav1,iret)
                     call store_res_history(n-1,flav2,resflav2,iret)
                     return
                  endif
               enddo
            endif
         endif
      enddo
      call store_res_history0(n,flav,resflav,iret)
      end

      subroutine reset_res_histories
      implicit none
      include 'pwhg_dynarrs.h'
c res_arr common block
      type(intdynarr2):: res_arrflav,res_arrresflav
      type(intdynarr1):: res_arrlength
      integer nfound
      common/res_hists_arrs/res_arrflav,res_arrresflav,res_arrlength,nfound
      allocate(res_arrflav%i(10,10),res_arrresflav%i(10,10),res_arrlength%i(10))
      nfound = 0
      end

      subroutine deallocate_res_histories
      implicit none
      include 'pwhg_dynarrs.h'
c res_arr common block
      type(intdynarr2):: res_arrflav,res_arrresflav
      type(intdynarr1):: res_arrlength
      integer nfound
      common/res_hists_arrs/res_arrflav,res_arrresflav,res_arrlength,nfound

      deallocate(res_arrflav%i)
      deallocate(res_arrresflav%i)
      deallocate(res_arrlength%i)

      end

      subroutine store_res_history0(n,flav,resflav,iret)
      implicit none
      include 'nlegborn.h'
      include 'pwhg_dynarrs.h'
      integer n,flav(n),resflav(n),iret
      logical flavequivr
      integer atags(n),btags(n),j
c res_arr common block
      type(intdynarr2):: res_arrflav,res_arrresflav
      type(intdynarr1):: res_arrlength
      integer nfound
      common/res_hists_arrs/res_arrflav,res_arrresflav,res_arrlength,nfound
      integer newn,newmaxarr
      atags = 0
      btags = 0
      do j=1,nfound
         if(n.eq.res_arrlength%i(j)) then
            if(flavequivr(n,flav,resflav,atags,
     1         res_arrflav%i(1:n,j),res_arrresflav%i(1:n,j),btags)) then
               return
            endif
         endif
      enddo
      nfound = nfound + 1
      if(nfound.gt.size(res_arrresflav%i,2).or.n.gt.size(res_arrresflav%i,1)) then
         if(nfound.gt.size(res_arrresflav%i,2)) then
            newmaxarr = nfound + 10
         else
            newmaxarr = size(res_arrresflav%i,2)
         endif
         if(n.gt.size(res_arrresflav%i,1)) then
            newn = n
         else
            newn = size(res_arrresflav%i,1)
         endif
         call resize_array_int2(res_arrflav,newn,newmaxarr)
         call resize_array_int2(res_arrresflav,newn,newmaxarr)
         call resize_array_int1(res_arrlength,newmaxarr)
      endif
      res_arrlength%i(nfound) = n

      res_arrflav%i(1:n,nfound) = flav
      res_arrresflav%i(1:n,nfound) = resflav

      iret = iret + 1

      end


      subroutine bindigits(m,n,arr)
      implicit none
      integer m,mmm,n,arr(n),k
      if(m.gt.2**n-1) then
         arr(1) = -1
         return
      endif
      mmm = m
      do k=n,1,-1
         arr(k) = mmm/2**(k-1)
         mmm = mod(mmm,2**(k-1))
      enddo
      end


      subroutine pwhg_res_histos_born
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_dynarrs.h' 
c res_arr common block
      type(intdynarr2):: res_arrflav,res_arrresflav
      type(intdynarr1):: res_arrlength
      integer nfound
      common/res_hists_arrs/res_arrflav,res_arrresflav,res_arrlength,nfound
      integer i,n
      logical, parameter :: debug=.false.
      if (debug) then
         write(*,*)  "**** BORN SUMMARY  ****"
         do i=1,nfound
            write(*,*) 'Born flav ',i            
            n=res_arrlength%i(i)         
            write(*,*) res_arrflav%i(1:n,i)
            write(*,*) res_arrresflav%i(1:n,i)
         enddo
      endif
c     Born flavor stuff
      if (nfound.gt.maxprocborn) then
         write(*,*) ' pwhg_res_histos_born: maxprocborn too small!'
         write(*,*) ' Increase it up to ',nfound
      endif
      if (maxval(res_arrlength%i(1:nfound)).gt.nlegborn) then
         write(*,*) ' pwhg_res_histos_born: nlegborn too small!'
         write(*,*) ' Increase it to:', maxval(res_arrlength%i(1:nfound))
      endif
      if(nfound.gt.maxprocborn.or.maxval(res_arrlength%i(1:nfound)).gt.nlegborn) then
         write(*,*) ' exiting ...'
         call exit(-1)
      endif    
      flst_nborn=nfound
      do i=1,nfound
         n=res_arrlength%i(i)         
         flst_bornlength(i)=n           
         flst_born(1:n,i)=res_arrflav%i(1:n,i)
        flst_bornres(1:n,i)=res_arrresflav%i(1:n,i)
      enddo

      end

      subroutine pwhg_res_histos_real
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_dynarrs.h'
c res_arr common block
      type(intdynarr2):: res_arrflav,res_arrresflav
      type(intdynarr1):: res_arrlength
      integer nfound
      common/res_hists_arrs/res_arrflav,res_arrresflav,res_arrlength,nfound
      integer i,n
      logical, parameter :: debug=.false.
      if (debug) then
         write(*,*)  "**** REAL SUMMARY  ****"
         do i=1,nfound
            write(*,*) 'Real flav ',i            
            n=res_arrlength%i(i)         
            write(*,*) res_arrflav%i(1:n,i)
            write(*,*) res_arrresflav%i(1:n,i)
         enddo
      endif
c     Real flavor stuff
      if (nfound.gt.maxprocreal) then
         write(*,*) ' pwhg_res_histos_born: maxprocborn too small!'
         write(*,*) ' Increase it up to ',nfound
      endif
      if (maxval(res_arrlength%i(1:nfound)).gt.nlegreal) then
         write(*,*) ' pwhg_res_histos_born: nlegborn too small!'
         write(*,*) ' Increase it to:', maxval(res_arrlength%i(1:nfound))
      endif
      if(nfound.gt.maxprocreal.or.maxval(res_arrlength%i(1:nfound)).gt.nlegreal) then
         write(*,*) ' exiting ...'
         call exit(-1)
      endif    
      flst_nreal=nfound
      do i=1,nfound
         n=res_arrlength%i(i)
         flst_reallength(i)=n           
         flst_real(1:n,i)=res_arrflav%i(1:n,i)
         flst_realres(1:n,i)=res_arrresflav%i(1:n,i)
      enddo

      end
      
      subroutine clean_resonance_structure(n,flav,resarr)
      implicit none
      integer n,flav(n),resarr(n)
      integer j,k,jr,mjr,flr
      logical relocated
      integer lastfs

c     finds the last final state (i.e. not decaying) particle
c     in the list
      lastfs = n
      do j=3,n
         if(resarr(j) > 0) lastfs = min(lastfs,resarr(j))
      enddo
      lastfs = lastfs - 1

c see the comment on the subroutine
      if( .not. examine_t_channel()) then
         n=-1
         return
      endif
c see the comment on the subroutine
      if( .not. examine_s_channel()) then
         n=-1
         return
      endif
c delete all t-channel resonances
      jr = resarr(2)
      do while(jr /= 0)
         mjr = resarr(jr)
         call delete_resonance_entry(jr)
         jr = mjr
      enddo

c delete all light particles intermediate resonances
      do j=3,n
         jr = resarr(j)
         if(jr.ne.0) then
            flr = flav(jr)
            if(flr == 22 .or. flr == 0 .or. (abs(flr) <= 16 .and. abs(flr) /= 6)) then
               call delete_resonance_entry(jr)
            endif
         endif
      enddo

c move all resonances in 3rd position recursively
      relocated = .true.
      do while(relocated)
c as long as there was a relocation, repeat the procedure
         relocated = .false.
         j=3
         do while(j <= n)
            if(flav(j) /= -2001) then
               jr = resarr(j)
               if(jr > j) then
                  call relocate_res(jr)
                  relocated = .true.
c                  write(*,*) '********** Relocated              *******************'
c                  call printres
                  j=j+1
               endif
            endif
            j=j+1
         enddo
      enddo

      do while(flav(n) == -2001)
         n = n-1
      enddo

      flav(2) = -flav(2)

c      write(*,*) '********* Exiting clean_resonance *******************'
c      call printres

      contains
          subroutine delete_resonance_entry(res)
          implicit none
          integer res
          integer j,mres
          mres = resarr(res)
c store the mother of res; all particles arising from res must become sons of mres
          do j=2,n
             if(flav(j) /= -2001 .and. resarr(j) == res)  resarr(j) = mres
          enddo
          flav(res) = -2001
          end subroutine delete_resonance_entry

          subroutine relocate_res(res)
          implicit none
          integer res,newloc,resfl,resmo,j
          resfl = flav(res)
          resmo = resarr(res)
          flav(3+1:res) = flav(3:res-1)
          resarr(3+1:res) = resarr(3:res-1)
          flav(3) = resfl
          resarr(3) = resmo
c all pointers to res must become 3
c all pointers below res must be increased by 1
          do j=3,n
             if(resarr(j).ne.0.and.flav(j).ne.-2001) then
                if(resarr(j) == res) then
                   resarr(j) = 3
                elseif(resarr(j).lt.res) then
                   resarr(j) = resarr(j) + 1
                endif
             endif
          enddo
          end subroutine relocate_res

          integer function sibling_of(j)
          implicit none
          integer j,k
          if(resarr(j) == 0) then
             sibling_of = 0
          else
             do k=2,n
                if( k /= j .and. resarr(k) == resarr(j)) then
                   sibling_of = k
                   return
                endif
             enddo
             write(*,*) ' sibling_of: no sibling of particle',j
             call printres
             call exit(-1)
          endif
          end function sibling_of

          logical function examine_t_channel()
c Rturns true if the t-channel structure of the event is really needed, false if there is
c an s-channel structure that produces the same event.
c It checks for t channel structure with a t-channel fermionic line emitting
c two EW bosons (W,Z or H). Any emission of gluons or photons may take place between the EW bosons, and
c is ignored.
c A corresponding s-channel structure can always be generated, with a single EW particle emitted from
c the fermion line, splitting into the two EW bosons. All intermediate gluons or photons may be associated
c with the same fermion line before or after the single EW particle. Thus, this structure must be ignored.
          implicit none
          integer jcurr,fljcurr,jr,fljr,flew,kcurr,flkcurr
c flavour of first attatched weak bosons; 0 if none.
          flew = 0
c start from initial state particle 2
          jcurr = 2
          do while(.true.)
             fljcurr = flav(jcurr)
             jr = resarr(jcurr)
             if( jr == 0 ) exit
c If jr is not a fermion, skip. This corresponds to two nearby fermions in the final state.
c They may be paired into a single vector only if flavours match; we prefer to consider them as
c not matched, which is the most general case.
             if(abs(flav(jr)) > 16 ) then
c is an ew particle                
                jcurr = jr
                flew = 0
                cycle
             endif
c Look for the other particle arising from the jr resonance
             kcurr = sibling_of(jcurr)
             flkcurr = flav(kcurr)
             if(flkcurr == 0 .or. flkcurr == 22) then
                jcurr = jr
                cycle
             endif
c Now flkcurr must be W,Z or H
             if( flew /= 0 .and. .not. (flkcurr == flew .and. abs(fljcurr) /= 6)) then
c Unless the previous electroweak flew and flkcurr are ZZ or HH, and the fermion line is not a top
c (only ttH couplings are considered) the two emitted bosons can come from the same resonance; drop them
                examine_t_channel = .false.
                return
             else
                flew = flkcurr
             endif
             jcurr = jr
          enddo
          examine_t_channel = .true.
          end function examine_t_channel

          logical function examine_s_channel()
          implicit none
          logical tchannel(n),finalstate(n)
          integer j,k1,j1,j2,j3,fl_j1,fl_j2,fl_j3,fl_k1,fl_k2,fl_k3,siblings(n)
c First mark all t-channel nodes
          tchannel = .false.
          j=2
          j2 = resarr(j)
          do while(j2 /= 0)
             tchannel(j2)=.true.
             j2 = resarr(j2)
          enddo
c Now mark all final state particles, and the son of the same resonance
c for each parton that is son of a resonance
          finalstate(1:2) = .false.
          finalstate(3:n) = .true.
          siblings = 0
          do j=3,n
             if(resarr(j) /= 0) then
                finalstate(resarr(j)) = .false.
                siblings(j) = sibling_of(j)
             endif
          enddo
c Now mark all other sons of resonances
          do j=3,n
             if(resarr(j) /= 0) then
                finalstate(resarr(j)) = .false.
             endif
          enddo          
c Now loop over all final state particles that are fermions
          do j=3,n
             if(finalstate(j) .and. abs(flav(j)) <= 16) then
c find the first node that corresponds to radiation of an EW boson
                j1 = j
 1              continue
                j2 = resarr(j1)
                if(j2 == 0 .or. tchannel(j2) .or.abs(flav(j2)) > 16) cycle
                fl_j1 = flav(j1)
                k1 = siblings(j1)
                fl_k1 = flav(k1)
                if(fl_k1 == 0 .or. fl_k1 == 22 .or. abs(flav(j2)) == 6) then
                   j1 = j2
                   goto 1
                endif
c now go on in the same way; stop when the node is an ew resonance
 2              continue
                j3 = resarr(j2)
c                if(j3 == 0 .or. tchannel(j3)) cycl
                if(j3 == 0) cycle
                fl_k2 = flav(siblings(j2))
                if(fl_k2 == 0 .or. fl_k2 == 22) then
                   j2 = j3
                   goto 2
                endif
                if(abs(fl_k2) > 16) then
c This is also an EW resonance. If it can be merged with the first emitted resonance
c abandon this graph
c ***************  add caveat for top
                   if(.not. (fl_k1 == fl_k2 .and. abs(fl_j1) /= 6)) then
                      examine_s_channel = .false.
                      return
                   else
                      j1 = j2
                      fl_j1 = flav(j1)
                      j2 = j3
                      fl_j2 = flav(j2)
                      goto 2
                   endif
                else
c Now j3 must correspond to a boson. If siblings is a b and firstres is a W
c they could have come from a top.
                   if( abs(fl_k2) == 5 .and. abs(fl_k1) == 24 .and.
     1                  fl_k2 * fl_k1 >= 0) then
                      examine_s_channel = .false.
                      return
                   endif
c If j3 is an EW boson, we can always lump j1 and k2 into an EW boson, that forms a
c triple vertex with k1 and j3, unless the new EW boson is a higgs, in which case
c it can only be attatched to a top.
                   if( abs(flav(j3)) > 16 .and. .not. (fl_k2 == 25 .and. abs(fl_j1) == 6) ) then
                      examine_s_channel = .false.
                      return
                   endif                   
                endif
             endif
          enddo                
          examine_s_channel = .true.
          end function examine_s_channel

          subroutine printres
          implicit none
          integer k
          write(*,*) '******************************************************'
          write(*,*) (k,k=1,n)
          write(*,*) flav(1:n)
          write(*,*) resarr(1:n)
          write(*,*) '******************************************************'
          end subroutine printres

      end
