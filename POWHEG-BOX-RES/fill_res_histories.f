c this subroutine looks at each alr configuration, and finds
c all configurations that have the same final state, but differ from it
c because they have an inequivalent resonance history.
c It sets up an array flst_rhreal where all resonance histories are stored.
c

      subroutine fill_res_histories
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_flg.h'
      integer iborn,lborn,alr,lalr,nequivperm,ireg,lreg
      integer numrh,
     1     rh(nlegreal,maxreshists),
     2     rhres(nlegreal,maxreshists),
     3     rhtags(nlegreal,maxreshists),
     4     rhlength(maxreshists)
      integer
     1     brh(nlegborn,maxreshists),
     2     brhres(nlegborn,maxreshists),
     3     brhtags(nlegborn,maxreshists),
     4     brhlength(maxreshists)
      logical ident_isfs,flavequivr,comparethree
c     This subroutines fills the arrays
c     flst_numrhborn,flst_rhbornlength,flst_rhborn,flst_rhbornres,flst_rhborntags
c     flst_numrhreal,flst_rhreallength,flst_rhreal,flst_rhrealres,flst_rhrealtags
c     with all possible resonance histories, including equivalent ones that are
c     competing among each other (as for example the two possible assignments
c     of qq->ZZ-> e+ e- e+ e-). These arrays are needed, since the flst_born and flst_real
c     arrays include only inequivalent configurations.
c     Furthermore, for each flst_born, flst_alr and flst_regular configurations,
c     a list of pointers to competing resonance histories in the arrays flst_rhborn or
c     flst_rhreal is filled (flst_bornrhptrs(:,iborn), flst_alrrhptrs(:,alr), flst_regularrhptrs(:,alr);
c     the number of competing resonance histories (including the given resonance structure) is
c     stored in the arrays  flst_bornnumrhptrs(iborn), flst_alrnumrhptrs(alr), flst_regularnumrhptrs(alr)

c     This needs to be initialized here. The setrhpointers subroutine
c     increments it as it finds new configurations to add.
      flst_numrhborn = 0

      do iborn=1,flst_nborn
         lborn = flst_bornlength(iborn)
c     The br* arrays are filled. The first entry is the current born structure         
         brh(:,1) = flst_born(:,iborn)
         brhres(:,1) = flst_bornres(:,iborn)
         brhtags(:,1) = flst_borntags(:,iborn)
         brhlength(1) = lborn
c     The remaining entries are all competing Born structures with the same
c     final state, but different resonance structure.
c     If the given Born configuration has alternative resonance assignments
c     that lead to a configuration equivalent to the iborn one, then only
c     one configuration is kept, mutliplied by the associated multiplicity (nequivperm)
         if(flg_user_reshists_sep) then
            numrh = 1
            flst_bornmult(iborn) = 1
         else
            call fill_res_histories0(nlegborn,brh,brhres,brhtags,brhlength,
     1           flst_nborn,flst_bornlength,flst_born,flst_bornres,flst_borntags,
     2           numrh,nequivperm)
            flst_bornmult(iborn) = nequivperm
         endif
c     Now there are numrh competing configurations in the br* arrays. These are stored in
c     the arrays flst_rhborn*. However, in order to avoid repetitions, the competing resonance
c     structure are stored only once, and for each Born configuration a set of pointers to the
c     flst_rhborn* arrays is setup in flst_bornrhptrs(:,iborn).
         call setrhpointers(nlegborn,numrh,flst_bornrhptrs(:,iborn),brhlength,brh,brhres,brhtags,
     1        flst_numrhborn,flst_rhbornlength,flst_rhborn,flst_rhbornres,flst_rhborntags)
         flst_bornnumrhptrs(iborn) = numrh
      enddo


c     Same as before for alr's. Notice that we look for inequivalent resonance
c     structures in the flst_real* arrays, not in the flst_alr* ones.
c     At the end, for each of the competing resonance structure we find, we compute
c     again the corresponding singular regions by calling findallsingregrh, that
c     in turn calls find_regions again for each found flst_rh* resonance history.
      flst_numrhreal = 0

      do alr=1,flst_nalr
         lalr = flst_alrlength(alr)
         rh(:,1) = flst_alr(:,alr)
         rhres(:,1) = flst_alrres(:,alr)
         rhtags(:,1) = flst_alrtags(:,alr)
         rhlength(1) = lalr
         if(flg_user_reshists_sep) then
            numrh = 1
         else
            call fill_res_histories0(nlegreal,rh,rhres,rhtags,rhlength,
     1           flst_nreal,flst_reallength,flst_real,flst_realres,flst_realtags,
     2           numrh,nequivperm)
            flst_alrmult(alr) = flst_alrmult(alr) * nequivperm
         endif
         call setrhpointers(nlegreal,numrh,flst_alrrhptrs(:,alr),rhlength,rh,rhres,rhtags,
     1        flst_numrhreal,flst_rhreallength,flst_rhreal,flst_rhrealres,flst_rhrealtags)
         flst_alrnumrhptrs(alr) = numrh
      enddo

c     same as before for regulars. Also here we look for inequivalent resonance
c     structures in the flst_real* arrays.
c     At the end, for each of the competing resonance structure we find, we compute
c     again the corresponding singular regions by calling findallsingregrh, that
c     in turn calls find_regions again for each found flst_rh* resonance history.
c     Competing regular structure will appear as those flst_rh* that have an empty
c     singular region list.
      do ireg=1,flst_nregular
         lreg = flst_regularlength(ireg)
         rh(:,1) = flst_regular(:,ireg)
         rhres(:,1) = flst_regularres(:,ireg)
         rhtags(:,1) = flst_regulartags(:,ireg)
         rhlength(1) = lreg
         if(flg_user_reshists_sep) then
            numrh = 1
         else
            call fill_res_histories0(nlegreal,rh,rhres,rhtags,rhlength,
     1           flst_nreal,flst_reallength,flst_real,flst_realres,flst_realtags,
     2           numrh,nequivperm)
            flst_regularmult(ireg) = flst_regularmult(ireg) * nequivperm
         endif
         call setrhpointers(nlegreal,numrh,flst_regularrhptrs(:,ireg),rhlength,rh,rhres,rhtags,
     1        flst_numrhreal,flst_rhreallength,flst_rhreal,flst_rhrealres,flst_rhrealtags)
         flst_regularnumrhptrs(ireg) = numrh
      enddo

      write(*,*) ' fill_res_histories: found ',flst_numrhreal,' resonance histories'

c     this finds all singular regions in the flst_rhreal* arrays. It fills the flst_rhrealnumreg
c     and flst_rhrealreg array.
      call findallsingregrh
      call pretty_print_flst
      call pretty_print_flst_reg

      end


      subroutine fill_res_histories0(nlegs,rh,rhres,rhtags,rhlength,
     1     ngraphs,graphslength,graphs,graphsres,graphstags,
     2     numrh,nequivperm0)
      implicit none
      include 'nlegborn.h'
      integer nlegs
      integer numrh,nequivperm0,
     1     rh(nlegs,maxreshists),
     2     rhres(nlegs,maxreshists),
     3     rhtags(nlegs,maxreshists),
     4     rhlength(maxreshists)
      integer ngraphs
      integer graphslength(ngraphs),graphs(nlegs,ngraphs),graphsres(nlegs,ngraphs),graphstags(nlegs,ngraphs)
      integer nequivperm,lreal,ireal
      logical ident_isfs,flavequivr
      procedure() :: ident_isfs,flavequivr

c     now find all resonance permutations of the current configuration
      call find_res_perm(rhlength(1),rh(:,1),
     1     rhres(:,1),rhtags(:,1),
     2     maxreshists,nequivperm0,rh(:,2:),
     3     rhres(:,2:),
     4     rhtags(:,2:))
c     also set all lengths:
      nequivperm0 = nequivperm0+1
      rhlength(2:nequivperm0) = rhlength(1)
      numrh = nequivperm0
      do ireal = 1,ngraphs
         lreal = graphslength(ireal)

c     go through the real configurations; find the ones that have the
c     same final state as the current alr, but differ from it (i.e.
c     have different resonance history)
         if(ident_isfs(rhlength(1),rh(:,1),
     1        rhres(:,1),rhtags(:,1),
     2        lreal,
     3        graphs(:,ireal),graphsres(:,ireal),
     4        graphstags(:,ireal))) then
c     Now find if they have inequivalent resonance history
            if(lreal.ne.rhlength(1) .or. .not.
     1           flavequivr(lreal,rh(:,1),
     2           rhres(:,1),rhtags(:,1),
     3           graphs(:,ireal),graphsres(:,ireal),
     4           graphstags(:,ireal))) then
c     OK, ireal is a real configuration with the same fs particles as alr,
c     not equivalent to alr.
c     We begin by copying this configuration to the allreshists array
               numrh = numrh + 1
               rh(:,numrh) =
     1              graphs(:,ireal)
               rhres(:,numrh) =
     1              graphsres(:,ireal)
               rhtags(:,numrh) =
     1              graphstags(:,ireal)
               rhlength(numrh) = lreal
               call reorder_fs(rhlength(1),rh(:,1),
     1              rhres(:,1),rhtags(:,1),
     2              lreal,
     3              rh(:,numrh),
     4              rhres(:,numrh),
     5              rhtags(:,numrh))
c     now find all permutations of the newly added configuration
               call find_res_perm(lreal,rh(:,numrh),
     1              rhres(:,numrh),rhtags(:,numrh),
     2              maxreshists - numrh,nequivperm,rh(:,numrh+1:maxreshists),
     3              rhres(:,numrh+1:maxreshists),
     4              rhtags(:,numrh+1:maxreshists))
c     also set all lengths:
               rhlength(numrh+1:numrh + nequivperm) = lreal
               numrh = numrh + nequivperm
            endif
         endif
      enddo
      end


      subroutine findallsingregrh
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      integer j,nregions,iregions(2,maxregions)
      flst_rhrealnumreg = 0
      do j=1,flst_numrhreal
         call find_regions(flst_rhreallength,flst_rhreal,flst_rhrealres,flst_rhrealtags,
     1     j,nregions,iregions)
         flst_rhrealnumreg(j) = nregions
         flst_rhrealreg(:,1:nregions,j) = iregions(:,1:nregions)
      enddo
      end

      subroutine setrhpointers(nlegs,numrh,arrptrs,rhlength,rh,rhres,rhtags,
     1     numrhgraph,rhgraphlength,rhgraph,rhgraphres,rhgraphtags)
      implicit none
      include 'nlegborn.h'
      integer nlegs
      integer numrh,arrptrs(numrh),
     1     rh(nlegs,maxreshists),
     2     rhres(nlegs,maxreshists),
     3     rhtags(nlegs,maxreshists),
     4     rhlength(maxreshists)
      integer numrhgraph,
     1     rhgraph(nlegs,maxreshists),
     2     rhgraphres(nlegs,maxreshists),
     3     rhgraphtags(nlegs,maxreshists),
     4     rhgraphlength(maxreshists)
      integer j,k
      logical comparethree
      do j=1,numrh
         do k=1,numrhgraph
            if(comparethree(rhlength(j),rh(:,j),rhres(:,j),rhtags(:,j),
     1           rhgraphlength(k),rhgraph(:,k),
     2           rhgraphres(:,k),rhgraphtags(:,k)) ) then
               arrptrs(j) = k
               exit
            endif
         enddo
c if it did not find an already existing rh (k=numrhgraph+1) add a new one;
         if(k.eq.numrhgraph + 1) then
            if(numrhgraph.ge.maxreshists) then
               write(*,*) ' setrhpointers: too many resonance regions, increase maxreshists'
               write(*,*) ' Exiting ...'
               call exit(-1)
            endif
            numrhgraph = numrhgraph + 1
            rhgraphlength(numrhgraph) = rhlength(j)
            rhgraph(:,numrhgraph) = rh(:,j)
            rhgraphres(:,numrhgraph) = rhres(:,j)
            rhgraphtags(:,numrhgraph) = rhtags(:,j)
            arrptrs(j) = numrhgraph
         endif
      enddo
      end


      logical function comparethree(n1,a1,b1,c1,n2,a2,b2,c2)
      implicit none
      integer n1,a1(n1),b1(n1),c1(n1),n2,a2(n2),b2(n2),c2(n2)
      integer j
      comparethree = .false.
      if(n1.eq.n2) then
         if(all(a1.eq.a2).and.all(b1.eq.b2).and.all(c1.eq.c2)) then
            comparethree = .true.
         endif
      endif
      end

      subroutine reorder_fs(na,a,ares,atags,nb,b,bres,btags)
c Reorder final state particles in b, so that they appear in the same sequential
c order as in a.
c It fails if not all fs particles in a have a match in b. However, it will not
c necessarily fail if not all fs particles in b have a match in a.
c Thus one should check before calling us that a and b have equivalent final states.
      implicit none
      integer na,a(na),ares(na),atags(na),nb,b(nb),bres(nb),btags(nb)
      integer ja,jb,kb,lfsb,itmp
      logical isfinalstate

      lfsb = 2

      do ja = 3,na
         if(isfinalstate(ja,na,ares)) then
            do jb = lfsb+1,nb
               if(isfinalstate(jb,nb,bres)) then
                  if(a(ja).eq.b(jb).and.atags(ja).eq.btags(jb)) then
                     lfsb = jb
                     goto 2
                  else
                     do kb = jb+1,nb
                        if(isfinalstate(kb,nb,bres) .and.
     1                       a(ja).eq.b(kb).and.atags(ja).eq.btags(kb)) then
                           itmp = b(jb)
                           b(jb) = b(kb)
                           b(kb) = itmp
                           itmp = bres(jb)
                           bres(jb) = bres(kb)
                           bres(kb) = itmp
                           itmp = btags(jb)
                           btags(jb) = btags(kb)
                           btags(kb) = itmp
                           lfsb = jb
                           goto 2
                        endif
                     enddo
                  endif
               endif
            enddo
c It failed 
            write(*,*) "reorder_fs: shouldn't be here!"
            write(*,*) na
            write(*,*) a
            write(*,*) ares
            write(*,*) atags
            write(*,*) nb
            write(*,*) b
            write(*,*) bres
            write(*,*) btags
            call exit(-1)
         endif
 2       continue
      enddo

      end


      logical function ident_isfs(na,a,ares,atags,nb,b,bres,btags)
c Find if flavour structures a and b have the same initial state and final state
c particles. Resonance histories may be different.
      implicit none
      integer na,a(na),ares(na),atags(na),nb,b(nb),bres(nb),btags(nb)
      integer marker(nb)
      integer ja,ka,jb,kb

      do ja=1,2
         if(a(ja) /= b(ja) .or. atags(ja) /= btags(ja)) then
            ident_isfs = .false.
            return
         endif
      enddo

      marker = 0
c Mark all resonances in b
      do jb = 3,nb
        if (bres(jb) /= 0) then
          marker(bres(jb)) = 2
        endif
      enddo

c loop through fs particles only
      mainloop: do ja=3,na
         do ka=3,na
            if(ka /= ja .and. ares(ka) == ja) then
               cycle mainloop
            endif
         enddo
         secondloop: do jb=3,nb
c If marker = 0 is not a resonance, and was not already associated
c to a fs particle of a.
            if(marker(jb) == 0) then
               if(a(ja) == b(jb) .and. atags(ja) == btags(jb)) then
                  marker(jb) = 1
                  exit secondloop
               endif
            endif
         enddo secondloop

         if(jb.eq.nb+1) then
c match not found!
            ident_isfs = .false.
            return
         endif
      enddo mainloop
c look if there are fs particles in b that are not marked
      do jb = 3,nb
         if(marker(jb) == 0) then
c unmatched fs particle in b!
            ident_isfs = .false.
            return
         endif
      enddo
      ident_isfs = .true.
      end

      subroutine find_res_perm(n,a,ares,atags,m,nb,b,bres,btags)
c     This finds all permutations of final state identical particles that lead to
c     a different resonance history.
c     n: length of flavour list
c     a: flavour
c     ares: resonances
c     atags: tags
c     m: available entries in the arrays b* for storing new permutations
c     nb: number of found equivalent permutations (excluding input configuration)
c     b, bres,btags (:,1:nb) number of found configurations

      implicit none
      include 'nlegborn.h'
      integer m,n,a(n),ares(n),atags(n)
      logical start,mtc,even,arequiv
      integer nb,b(nlegreal,m),bres(nlegreal,m),btags(nlegreal,m)
      integer fs(nlegreal)
      integer aorder(n)
      integer nfs
      integer j,k
      logical resequiv,isfinalstate
      external resequiv,isfinalstate

      nb = 0
      start = .true.

 20   continue

      if(start) then
         nfs = 0
         do j=3,n
            if(.not. isfinalstate(j,n,ares)) cycle
            nfs = nfs+1
            fs(nfs) = j
         enddo
         do j=1,nfs
            aorder(j) = j
         enddo
         mtc = .false.
         start = .false.
      endif
c The first permutation does nothing
      call nexper(nfs,aorder,mtc,even)      
 10   call nexper(nfs,aorder,mtc,even)
      if(mtc) then
c     check if the flavour structure has stayed the same
         do j=1,nfs
            if(a(fs(j)).ne.a(fs(aorder(j)))
     1           .or. atags(fs(j)).ne.atags(fs(aorder(j)))) then
               goto 10
            endif
         enddo
         nb = nb + 1
         if(nb.gt.m) then
            write(*,*) 'find_res_perm: output array too small!',nb,m
            call exit(-1)
         endif
         b(1:n,nb) = a(1:n)
         bres(1:n,nb) = ares(1:n)
         btags(1:n,nb) = atags(1:n)
         do j=1,nfs
            bres(fs(j),nb) = ares(fs(aorder(j)))
         enddo
c     this should also check that the inequivalent resonance structure was not generated earlier
         if(resequiv(n,a,ares,atags,b(:,nb),bres(:,nb),btags(:,nb)))then
            nb = nb-1
            goto 10
         endif
         do j=1,nb-1
            if(resequiv(n,b(:,j),bres(:,j),btags(:,j),
     1           b(:,nb),bres(:,nb),btags(:,nb))) then
               nb = nb-1
               goto 10
            endif
         enddo
         goto 10
      endif

      contains

      subroutine nexper(n,a,mtc,even)
      implicit none
c*******************************************************************************
c     Gives all permutations for a group                                       
c http://www.cs.sunysb.edu/~algorith/implement/wilf/distrib/processed/nexper_2.f
c next permutation of {1,...,n}. Ref NW p 59.                                  
c*******************************************************************************
      integer n,a(n),s,d
      logical mtc,even
      integer i,j,m,i1,ia,l,nm3
      if(mtc)goto 10
      nm3=n-3
      do 1 i=1,n
 1        a(i)=i
      mtc=.true.
 5     even=.true.
      if(n.eq.1)goto 8
 6     if(a(n).ne.1.or.a(1).ne.2+mod(n,2))return
      if(n.le.3)goto 8
      do 7 i=1,nm3
      if(a(i+1).ne.a(i)+1)return
 7     continue
 8      mtc=.false.
      return
 10    if(n.eq.1)goto 27
      if(.not.even)goto 20
      ia=a(1)
      a(1)=a(2)
      a(2)=ia
      even=.false.
      goto 6
 20    s=0
      do 26 i1=2,n
 25       ia=a(i1)
      i=i1-1
      d=0
      do 30 j=1,i
 30       if(a(j).gt.ia) d=d+1
      s=d+s
      if(d.ne.i*mod(s,2)) goto 35
 26    continue
 27     a(1)=0
      goto 8
 35    m=mod(s+1,2)*(n+1)
      do 40 j=1,i
      if(isign(1,a(j)-ia).eq.isign(1,a(j)-m))goto 40
      m=a(j)
      l=j
 40    continue
      a(l)=ia
      a(i1)=m
      even=.true.
      return
      end subroutine nexper

      end
 
      logical function resequiv(n,a,ares,atags,b,bres,btags)
c a,ares,atags and b,bres,btags are the flavour list,
c the resonance list, and the tag list, and 
c returns true if the a and b arrays are
c equivalent up to a permutation of the resonance positions,
c without changing the position of final state particles;
c false otherwise.
      implicit none
      integer n,a(n),ares(n),atags(n),b(n),bres(n),btags(n)
      integer bmarked(n)
      integer j,k
      logical rec_ident_fixfs, isfinalstate
      external rec_ident_fixfs, isfinalstate
c first two entries must be identical
      do j=1,2
         if(a(j) /= b(j) .or. atags(j) /= btags(j)) then
            resequiv = .false.
            return
         endif
      enddo
      bmarked = 0
      do j=3,n
         if(isfinalstate(j,n,ares)) then
c final state particles should match exactly in a and b
            if(.not.isfinalstate(j,n,bres) .or.
     1           a(j).ne.b(j) .or. atags(j).ne.btags(j)) then
               write(*,*)
     1              ' resequiv: called improperly? Should not be here..'
               call exit(-1)
            endif
         else
c Compare only primary particles (i.e., not sons of resonances);
c the recursive comparison takes care of the rest.
            if(ares(j).eq.0) then
               do k=3,n
                  if(bres(k).eq.0) then
                     if(bmarked(k) == 0) then
                        if(rec_ident_fixfs(n,j,k,a,ares,atags,b,bres,
     1                       btags)) then
                           bmarked(k) = 1
                           exit
                        endif
                     endif
                  endif
               enddo
               if(k.eq.n+1) then
                  resequiv = .false.
                  return
               endif
            endif
         endif
      enddo
      resequiv = .true.
      end

     

      logical function isfinalstate(j,n,ares)
      implicit none
      integer j,n,ares(n)
      integer k
      if(j.le.2) then
         isfinalstate = .false.
         return
      else
         do k=3,n
            if( j == ares(k) ) then
               isfinalstate = .false.
               return
            endif
         enddo
      endif
      isfinalstate = .true.
      end
      

      recursive function rec_ident_fixfs(n,ia,ib,a,ares,atags,
     1     b,bres,btags) result(result)
c This recursive function checks if entry ia is equivalent to entry ib in the arrays a and b.
c It properly accounts the fact that identical resonances should also have identical
c decay products recursively. Final state particles should be identical also
c in position, not only in flavour and tag.
      implicit none
      logical result
      integer, intent(in)::
     1     n,ia,ib,a(n),ares(n),atags(n),b(n),bres(n),btags(n)      
c The following variables are local even if -save or -fno-automatic
c is used in compilation, so that recursion works properly.
c Only an explicit save statement could prevent that.
c Notice also that arguments are passed by reference: we always
c pass the same copy of the arrays a,ares,atags and b,bres,btags to the ident
c function.
      integer bmarked(n)
      integer ka,kb
      logical isfinalstate
      if(isfinalstate(ia,n,ares) .or. isfinalstate(ib,n,bres)) then
         if(ia .eq. ib .and. atags(ia) == btags(ib)) then
            result = .true.
         else
            result = .false.
         endif
         return
      endif

      if(a(ia) /= b(ib) .or. atags(ia) /= btags(ib)) then
         result = .false.
         return
      endif
c now ka goes through all elements that come from the decay
c of ia.
      bmarked = 0
      do ka=1,n
         if(ares(ka).eq.ia) then
c For each decay product of ia, see if there is an identical (recursively!)
c decay product of ib. If found, mark it in the array bmarked, so as not to
c usit more than once
            do kb=1,n
               if( bres(kb) == ib .and. bmarked(kb) == 0) then
c see if they are equal
                  if(rec_ident_fixfs(n,ka,kb,a,ares,atags,b,bres,btags))
     1                 then
                     bmarked(kb)=1
                     exit
                  endif
               endif
            enddo
            if(kb == n+1) then
               result = .false.
               return
            endif
         endif
      enddo
      do kb=1,n
         if( bres(kb) == ib ) then
            if(bmarked(kb) == 0) then
               result = .false.
               return
            endif
         endif
      enddo
      result = .true.
      return
      end






      subroutine pretty_print_flst
      implicit none
      include 'nlegborn.h'
      character * 200 string,stringb
      include 'pwhg_flst.h'
      integer alr,k,l,irh,lrh,iun,lstring,lstringb,lastnb,lreal,ptr
      external lastnb
      call newunit(iun)
      open(unit=iun,file='FlavRegList',status='unknown')
      do alr=1,flst_nalr
         lreal = flst_alrlength(alr)
         call from_number_to_madgraph
     1         (lreal,flst_alr(1,alr),flst_emitter(alr),string)
         call from_number_to_madgraph
     1         (lreal-1,flst_uborn(1,alr),-1,stringb)
         lstring=lastnb(string)
         lstringb=lastnb(stringb)
         if(flst_emitter(alr).gt.0) then
            if(flst_alrres(flst_emitter(alr),alr).ne.0) then
               write(string(lstring+1:),'(a,i2)')
     1              ' res. ',flst_alrres(flst_emitter(alr),alr)
            endif
         endif
         lstring=lastnb(string)
         write(iun,'(a,i5,400a)') '*** alr region: ',alr,('*',k=4,lstring)
         write(iun,'(a,i3)') string(1:lstring)//' mult=', flst_alrmult(alr)
         write(iun,'(11x,100i5)') flst_alrres(3:lreal,alr)
          
         write(iun,'(a,i3)') stringb(1:lstringb)//' uborn, mult=',
     1        flst_ubmult(alr)
         write(iun,'(11x,100i5)') flst_ubornres(3:lreal-1,alr)
         write(iun,'(a,2(1x,i2),a,20(1x,2(1x,i2)))')
     1      ' alr region: (',flst_emitter(alr),lreal,');  all regions:',
     2        ((flst_allreg(l,k,alr),l=1,2),k=1,flst_numallreg(alr))
c print competing resonance histories
         write(iun,'(a)') ' Competing resonance histories'
         do irh=1,flst_alrnumrhptrs(alr)
            ptr = flst_alrrhptrs(irh,alr)
            lrh = flst_rhreallength(ptr)
            call from_number_to_madgraph(lrh,
     1           flst_rhreal(:,ptr),-1,string)
            write(iun,'(a,a,i3)') trim(string), '   ptr=',ptr
            write(iun,'(11x,100i5)') flst_rhrealres(3:lrh,ptr)
            if(flst_rhrealnumreg(ptr).gt.0) then
               write(iun,'(a,20(1x,2(1x,i2)))') ' all regions:',
     1              ((flst_rhrealreg(l,k,ptr),l=1,2),k=1,flst_rhrealnumreg(ptr))
            else
               write(iun,*) ' No singular regions'
            endif
         enddo
         write(iun,'(a)') ' End competing resonance histories'
         write(iun,*)
      enddo
      close(iun)
      end




      subroutine pretty_print_flst_reg
      implicit none
      include 'nlegborn.h'
      character * 200 string,stringb
      include 'pwhg_flst.h'
      integer ireg,k,l,irh,lrh,iun,lstring,lstringb,lastnb,lregular,ptr
      external lastnb
      call newunit(iun)
      open(unit=iun,file='FlavRegList',status='unknown',access='append')
      do ireg=1,flst_nregular
         lregular = flst_regularlength(ireg)
         call from_number_to_madgraph
     1         (lregular,flst_regular(:,ireg),-1,string)
         lstring=lastnb(string)
         write(iun,'(a,i5,400a)') '*** regular region: ',ireg,('*',k=4,lstring)
         write(iun,'(a,i3)') string(1:lstring)//' mult=', flst_regularmult(ireg)
         write(iun,'(11x,100i5)') flst_regularres(3:lregular,ireg)
c print competing resonance histories
         write(iun,'(a)') ' Competing resonance histories'
         do irh=1,flst_regularnumrhptrs(ireg)
            ptr = flst_regularrhptrs(irh,ireg)
            lrh = flst_rhreallength(ptr)
            call from_number_to_madgraph(lrh,
     1           flst_rhreal(:,ptr),-1,string)
            write(iun,'(a,a,i3,a,i3)') trim(string),
     2           '   ptr=',ptr,' resgroup=',flst_regularresgroup(ireg)
            write(iun,'(11x,100i5)') flst_rhrealres(3:lrh,ptr)
            if(flst_rhrealnumreg(ptr).gt.0) then
               write(iun,'(a,20(1x,2(1x,i2)))') ' all regions:',
     1              ((flst_rhrealreg(l,k,ptr),l=1,2),k=1,flst_rhrealnumreg(ptr))
            else
               write(iun,*) ' No singular regions'
            endif
         enddo
         write(iun,'(a)') ' End competing resonance histories'
         write(iun,*)
      enddo
      close(iun)
      end

