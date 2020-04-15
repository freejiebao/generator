c -*- Fortran -*-

c rad_ubornsubp: current index of underlying born
c rad_alr_list: list of alr's that share the current underlying born
c rad_alr_nlist: length of the above list
c rad_realsubp: index in rad_alr_list of current alr
c rad_realalr: current alr
c rad_realreg: index of regular contribution in the array flst_regular
      integer rad_ubornsubp,rad_alr_list(maxalr),rad_alr_nlist,
     #     rad_alrsubp,rad_regularsubp,rad_sign
c rad_kinreg: index in current kinematic region
c rad_nkinreg: number of kinematic regions
c     kinematic regions are numbered as:
c     1: initial state region
c     2 ... rad_nkinreg: final state regions with increasing
c                        emitter
c     rad_kinreg_on(rad_nkinreg): logical, entry j is true if there is a region
c     with rad_kinreg=j associated with current underlying born.
      integer rad_kinreg,rad_nkinreg
      logical rad_kinreg_on(nlegborn-1)
c rad_ncsiynormsmx: maximum number of csi-y subdivision when computing
c                   the upper bounds
c rad_ncsinorms,rad_nynorms: effective number of csi and y subdivisions
      integer rad_ncsiynormsmx
      parameter (rad_ncsiynormsmx=100)
      integer rad_ncsinorms,rad_nynorms
c 1 for Btilde event, 2 for remnant, 3 for regular
      integer rad_type
c Signed total, absolute value total, positive total and negative total
c obtained in the integration of btilde
      real * 8 rad_tot,rad_etot,rad_totgen
c Grid of the upper bounds of the ratio (R*kn_jacreal/B)/upper_bounding function
c for each given kinematic region and underlying born
      real * 8 rad_csiynorms(rad_ncsiynormsmx,
     #     rad_ncsiynormsmx,nlegborn-1,maxprocborn)
c as above, on the whole grid, for each given underlying born
      real * 8 rad_norms(nlegborn-1,maxprocborn)
c filled with contributions to real cross section after
c a call to sigreal_rad; it is a list of the alr that share the
c same current underlying Born rad_ubornsubp
      real * 8 rad_real_arr(maxalr)
c radiation variables in sigremnant call
      real * 8 rad_xradremn(3)
c user provided factor, to increase the upper bounding ratios
      real * 8 rad_normfact
c minimum pt-squared
      real * 8 rad_ptsqmin,rad_charmthr2,rad_bottomthr2
      real * 8 rad_ptsqmin_em
c LambdaLL for upper bounding coupling (see notes: running_coupling)
      real * 8 rad_lamll
c Hardest radiation kt2
      real * 8 rad_pt2max
c Branching ratio (useful to change xsecup properly when a decay is
c added a posteriori)
      real * 8 rad_branching
c Current event weight, needed when doing reweghting    
      real  * 8 rad_currentweight
      integer rad_iupperfsr,rad_iupperisr
c     These variable store the amount of upper bound violation
c     (ratio of the function value to the upper bound) in gen
c     and in the generation of radiation
      real * 8 rad_genubexceeded
      common/pwhg_rad/
     8     rad_tot,rad_etot,rad_totgen,
     1     rad_csiynorms,rad_norms,rad_real_arr,
     2     rad_normfact,rad_ptsqmin,rad_ptsqmin_em,
     3     rad_charmthr2,rad_bottomthr2,
     4     rad_lamll,rad_xradremn,rad_pt2max,
     5     rad_branching,rad_currentweight,
     5     rad_genubexceeded,
c     integers
     1     rad_ubornsubp,rad_alr_list,rad_alr_nlist,
     2     rad_alrsubp,rad_regularsubp,rad_sign,
     3     rad_kinreg,rad_nkinreg,
     4     rad_ncsinorms,rad_nynorms,rad_type,
     5     rad_iupperfsr,rad_iupperisr,
c     logical
     6     rad_kinreg_on
      save /pwhg_rad/
