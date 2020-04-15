      subroutine bornzerodamp(alr,r0,rc,rs,rcs,dampfac)
c given the R_alpha region (i.e. the alr) and the associated
c real contribution r (without pdf factor),
c returns in dampfac the damping factor to be applied to
c the real contribution to implement Born zero suppression
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_flg.h'
      include 'pwhg_math.h'
      integer alr
      real * 8 r0,rc,rs,rcs,dampfac,h,pwhg_pt2,pt2,powheginput
      integer lalr
      logical ini
      data ini/.true./
      save ini,h
      external pwhg_pt2,powheginput
      if(ini) then
         h=powheginput("#hdamp")
         if(h.lt.0) then
            h=powheginput("#hfact")
            if(h.gt.0) then
               write(*,*)'***************************************'
               write(*,*)' Warning: hfact is here for backward'
               write(*,*)' compatibility with older inplementations'
               write(*,*)' New implementations will use hdamp and'
               write(*,*)' bornzerodamp independently.'
               write(*,*)'***************************************'
            endif
         endif
         if(h.gt.0) then
            write(*,*)'***************************************'
            write(*,*)' Using a damping factor h^2/(pt2+h^2)'
            write(*,*)' to separate real contributions between'
            write(*,*)' Sudakov and remnants    h=',h,' GeV   ' 
            write(*,*)'***************************************'
         endif
         ini=.false.
      endif
c
      dampfac = 1
      if(flst_emitter(alr) < 3) then
c hfact applied only for ISR
         lalr = flst_alrlength(alr)
         if(h.gt.0) then
            pt2 = kn_cmpreal(1,lalr)**2+kn_cmpreal(2,lalr)**2
            dampfac=h**2/(pt2+h**2)
         endif
      endif

      if(flg_bornzerodamp.and.r0.gt.5*abs(rc+rs-rcs)) then
         dampfac=0
      endif

      end


