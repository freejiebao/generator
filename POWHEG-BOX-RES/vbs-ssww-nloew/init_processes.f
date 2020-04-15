      subroutine init_processes
      implicit none
      include 'nlegborn.h'
      include 'pwhg_flst.h'
      include 'pwhg_kn.h'
      include 'pwhg_pdf.h'
      include 'pwhg_par.h'
      include 'pwhg_em.h'
      include 'LesHouches.h'
      include 'pwhg_flg.h'
      include 'pwhg_physpar.h'
      include 'pwhg_st.h'
      include 'pwhg_rad.h'
      include 'pwhg_res.h'
ccc-mauro-mod
      include 'PhysPars.h'
ccc-mauro-mod
      integer i1,i2,i3,i4,i5,k,ii(nlegreal)
      equivalence (i1,ii(1)),(i2,ii(2)),(i3,ii(3)),
     #  (i4,ii(4)),(i5,ii(5))
      logical debug
      parameter (debug=.true.)
      integer j
      integer charge3(-6:6)
      data charge3 /-2,1,-2,1,-2,1,0,-1,2,-1,2,-1,2/
      logical condition
      real * 8 powheginput
      external powheginput
c     vector boson id and decay
      integer idvecbos,vdecaymode
      common/cvecbos/idvecbos,vdecaymode
c     lepton masses
      real *8 lepmass(3)
      common/clepmass/lepmass
      real * 8 cmass, bmass

      integer i,iun,dim_integ
      integer nmaxres_real,nmaxres_born


      flg_samexgridasbtilde = .true.
      if(powheginput("#bornzerodamp").ne.0) then
         flg_bornzerodamp = .true.
         flg_withdamp = .true.
      else
         flg_bornzerodamp = .false.
         flg_withdamp = .false.
      endif

c Must include photon!
      pdf_nparton = 22

      rad_ptsqmin_em = powheginput("#rad_ptsqmin_em")
      if (rad_ptsqmin_em.le.0d0) rad_ptsqmin_em  = 0.001d0**2
c      flg_jacsing = .true.


c     read eventual c and b masses from the input file
      cmass=powheginput("#cmass_lhe")
      if (cmass.gt.0d0) physpar_mq(4)=cmass
      bmass=powheginput("#bmass_lhe")
      if (bmass.gt.0d0) physpar_mq(5)=bmass
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

c*********************************************************     
         
         
      flst_nborn = 0
      flst_nreal = 0
      flst_numfinal=6
      flst_nbornresgroup=5

c     here the reference sign is the one for W+W+,
c     however the correct sign is applied in t_channel_resonance and s_channel_richer_resonance
c     as an overall +/- on the quarks and the W+-
! s~s~->c~c~ 1
      call t_channel_resonance(-3,-3,-4,-4)
! s~d~->c~u~ 2
      call t_channel_resonance(-3,-1,-4,-2)
! s~u->c~d 3
      call t_channel_resonance(-3,2,-4,1)
! s~c->c~s 4
      call t_channel_resonance(-3,4,-4,3)
      call s_channel_richer_resonance(-3,4,-4,3)
! d~s~->u~c~ 5
      call t_channel_resonance(-1,-3,-2,-4)
! d~d~->u~u~ 6
      call t_channel_resonance(-1,-1,-2,-2)
! d~u->u~d 7
      call t_channel_resonance(-1,2,-2,1)
      call s_channel_richer_resonance(-1,2,-2,1)
! d~c->u~s 8
      call t_channel_resonance(-1,4,-2,3)
! us~->dc~ 9
      call t_channel_resonance(2,-3,1,-4)
! ud~->du~ 10
      call t_channel_resonance(2,-1,1,-2)
      call s_channel_richer_resonance(2,-1,1,-2)
! uu->dd 11
      call t_channel_resonance(2,2,1,1)
! uc->ds 12
      call t_channel_resonance(2,4,1,3)
! cs~->sc~ 13
      call t_channel_resonance(4,-3,3,-4)
      call s_channel_richer_resonance(4,-3,3,-4)
! cd~->su~ 14
      call t_channel_resonance(4,-1,3,-2)
! cu->sd 15
      call t_channel_resonance(4,2,3,1)
! cc->ss 16
      call t_channel_resonance(4,4,3,3)
! ud~->c~s 17
      call s_channel_richer_resonance(2,-1,-4,3)
! d~u->c~s 18
      call s_channel_richer_resonance(-1,2,-4,3)
! cs~->u~d 19
      call s_channel_richer_resonance(4,-3,-2,1)
! s~c->u~d 20
      call s_channel_richer_resonance(-3,4,-2,1)
      

      
      
c end true one
      
      
      if (debug) then
         write(*,*) ' born processes',flst_nborn
         do j=1,flst_nborn
            write(*,*) (flst_born(k,j),k=1,flst_bornlength(j))
            write(*,*) (flst_bornres(k,j),k=1,flst_bornlength(j))
         enddo
      endif
     
     
      if (debug) then
         write(*,*) ' real processes',flst_nreal
         do j=1,flst_nreal
            write(*,*) (flst_real(k,j),k=1,flst_reallength(j))
            write(*,*) (flst_realres(k,j),k=1,flst_reallength(j))
         enddo
      endif
      
      call newunit(iun)
      open(unit=iun, file='DetailedFlavList.txt', status='unknown')
      write(iun,*) ' ***********   FINAL POWHEG    ***************'
      write(iun,*) ' ***********     BORN          ***************'
      do i=1,flst_nborn
!     write(iun,'(a,100i4)')'                  ',int(1:flst_bornlength(i))
         write(iun,'(a,i3,a,100i4)')'flst_born(',i,')   =',flst_born(1:flst_bornlength(i),i)
         write(iun,'(a,i3,a,100i4)')'flst_bornres(',i,')=',flst_bornres(1:flst_bornlength(i),i)
         write(iun,*)
      enddo   
      write(iun,*) 'max flst_bornlength: ',maxval(flst_bornlength(1:flst_nborn))
      
      
      
      write(iun,*) ' ***********     REAL          ***************'
      do i=1,flst_nreal
!     write(iun,'(a,100i4)')'                  ',int(1:flst_reallength(i))
         write(iun,'(a,i3,a,100i4)')'flst_real(',i,')   =',flst_real(1:flst_reallength(i),i)
         write(iun,'(a,i3,a,100i4)')'flst_realres(',i,')=',flst_realres(1:flst_reallength(i),i)
         write(iun,*)
      enddo   
      write(iun,*) 'max flst_reallength: ',maxval(flst_reallength(1:flst_nreal))
      

      
      call buildresgroups(flst_nborn,nlegborn,flst_bornlength,
     1     flst_born,flst_bornres,flst_bornresgroup,flst_nbornresgroup)
      write(iun,*)'FLST_NBORNRESGROUP',flst_nbornresgroup
      

      write(iun,*) ' ***********     BORN   RR     ***************',flst_nborn
      do i=1,flst_nborn
         write(iun,'(a,i3,a,100i4)')'flst_born(',i,')   =',flst_born(1:flst_bornlength(i),i)
         write(iun,'(a,i3,a,100i4)')'flst_bornres(',i,')=',flst_bornres(1:flst_bornlength(i),i)
         write(iun,*)'ibornresgroup',flst_bornresgroup(i)
c         write(iun,*)
      enddo   
      
      call buildresgroups(flst_nreal,nlegreal,flst_reallength,
     1     flst_real,flst_realres,flst_realresgroup,flst_nrealresgroup)


      write(iun,*) ' ***********     REAL  RR      ***************'
      do i=1,flst_nreal
         write(iun,*)'irealresgroup', flst_realresgroup(i)
         write(iun,*)
      enddo   

      
      write(iun,*) 
      write(iun,*) '*********   SUMMARY  *********'
      write(iun,*) 'set nlegborn to: ',maxval(flst_bornlength(1:flst_nborn))
      write(iun,*) 'set nlegreal to: ',maxval(flst_reallength(1:flst_nreal))
      
      nmaxres_real = maxval(flst_realres(1:flst_reallength(flst_nreal),1:flst_nreal)) - 2
      nmaxres_born = maxval(flst_bornres(1:flst_bornlength(flst_nborn),1:flst_nborn)) - 2
      write(iun,*) 'max number of resonances: ',max(nmaxres_real,nmaxres_born)
      
c     add (-1) for overall azimuthal rotation of the event around the beam axis
      dim_integ = (flst_numfinal+1)*3 - 4 + 2 + max(nmaxres_real,nmaxres_born)
      write(iun,*) 'set ndiminteg to: ',dim_integ 


      write(iun,*) 'flst_nbornresgroup ',flst_nbornresgroup 
      write(iun,*) 'flst_nrealresgroup ',flst_nrealresgroup

      write(iun,*) '*********   END SUMMARY  *********'
      write(iun,*)

      close(iun)


      
      return
 998  write(*,*) 'init_processes: increase maxprocreal'
      stop
 999  write(*,*) 'init_processes: increase maxprocborn'
      end
      
      block data lepmass_data 
      real *8 lepmass(3)
      common/clepmass/lepmass
!      data lepmass /0.51099892d-3,0.105658369d0,1.77699d0/
      data lepmass /0d0,0d0,1.77699d0/
      end
