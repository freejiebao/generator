c -*- Fortran -*-

c The user must set nlegborn to the appropriate value for his process
c in file nlegborn.h in the user directory
c
c maxprocborn and maxprocreal must be greater or equal to the number of
c independent flavour structures for the born and real process.
c
c flst_nborn and flst_nreal should be set to the  number of
c independent flavour structures for the born and real process.
c
c flst_born and flst_real should be filled with the flavour structure
c of the born and real subprocesses.
c The meaning is: flst_real(j,k) is the flavour of leg j in subprocess k.
c The flavour is taken incoming for the two incoming particles and outgoing
c for the outgoing particles.
c The flavour number is according to PDG conventions, EXCEPT for gluons,
c where we take 0 instead of 21.
c As an example, for p p -> (Z->e+e-)+2 j,
c [1,0,11,-11,1,0] represents d g -> e- e+ d g
c Notice that only one ordering of final state flavour can appear for
c a given final state.
c It is required that legs in the Born and real processes
c should be ordered as follows
c leg 1: incoming parton with positive rapidity
c leg 2: incoming parton with negative rapidity
c from leg 3 onward: final state particles, ordered as follows:
c Colorless particles first, massive coloured particles,
c massless coloured particles.
c The flavour of colored neutral and massive colored particles should
c be the same for all real and born subprocesses.
c This is the case for most QCD NLO calculation.
      integer maxregions
      parameter (maxregions=nlegreal*(nlegreal-1)/2)

      integer flst_nborn, flst_born(nlegborn,maxprocborn),
     1     flst_borntags(nlegborn,maxprocborn),
     2     flst_bornres(nlegborn,maxprocborn), flst_bornmult(maxprocborn),
     3     flst_nreson,flst_reslist(nlegborn),
     4     flst_bornlength(maxprocborn),
     5     flst_bornresgroup(maxprocborn),flst_ibornresgroup,flst_nbornresgroup,
     6     flst_ibornlength,flst_bornrescurr(nlegborn),flst_borncurr(nlegborn)
c The last 3 entries are used to group together born configurations that
c have the same resonance structure from the point of view of the integration.
c Thus, they may differ by particle content, but have resonances in the same
c kinematic configurations.
c flst_bornresgroup(iborn) -> 1 ... flst_nbornresgroup;
c flst_ibornresgroup is the current group when needed
c
c res arrays contain pointers to the mother resonance for
c resonace's decay products, zero for the other particles.
      integer flst_nreal, flst_real(nlegreal,maxprocreal),
     1     flst_realtags(nlegreal,maxprocreal),
     2     flst_realres(nlegreal,maxprocreal),
     4     flst_reallength(maxprocreal),
     5     flst_realresgroup(maxprocreal),flst_nrealresgroup,
     6     flst_ireallength
      integer flst_numfsr,flst_numfsb
      integer flst_nalr,flst_alr(nlegreal,maxalr),
     1     flst_alrtags(nlegreal,maxalr),
     2     flst_alrres(nlegreal,maxalr),
     4     flst_alrlength(maxalr),
     5     flst_numrhreal,
     6     flst_rhreal(nlegreal,maxreshists),
     7     flst_rhrealres(nlegreal,maxreshists),
     7     flst_rhrealtags(nlegreal,maxreshists),
     6     flst_rhreallength(maxreshists),
     7     flst_alrnumrhptrs(maxalr),
     8     flst_alrrhptrs(maxreshists,maxalr),
     9     flst_rhrealnumreg(maxreshists),flst_rhrealreg(2,maxregions,maxreshists)
      integer flst_numrhborn,
     1     flst_rhborn(nlegborn,maxreshists),
     2     flst_rhbornres(nlegborn,maxreshists),
     3     flst_rhborntags(nlegborn,maxreshists),
     4     flst_rhbornlength(maxreshists),
     5     flst_bornnumrhptrs(maxprocborn),
     6     flst_bornrhptrs(maxreshists,maxprocborn)
      integer flst_nregular,flst_regular(nlegreal,maxprocreal),
     1     flst_regulartags(nlegreal,maxprocreal),
     2     flst_regularres(nlegreal,maxprocreal),
     4     flst_regularlength(maxprocreal),flst_regularmult(maxprocreal),
     5     flst_regularnumrhptrs(maxprocreal),flst_regularrhptrs(maxreshists,maxprocreal),
     7     flst_regularresgroup(maxprocreal),flst_iregularresgroup,flst_nregularresgroup
      integer flst_uborn(nlegborn,maxalr),
     1     flst_uborntags(nlegborn,maxalr),
     2     flst_ubornres(nlegborn,maxalr),
     4     flst_ubornlength(maxalr)
      integer flst_alrmult(maxalr), flst_ubmult(maxalr),
     1        flst_emitter(maxalr)
c     list of all regions      
      integer flst_allreg(2,maxregions,maxalr),flst_numallreg(maxalr)
c     pointer from flst_alr to flst_born
      integer flst_alr2born(maxalr)
c     pointer from flst_born to flst_alr
c     born2alr(0,k) = number of alpha_r with underlying born k
c     born2alr(1.. born2alr(0,k),k)= pointer to corresponding alpha_r
      integer flst_born2alr(0:maxalr,maxprocborn)
c This used to be settable by the process. We aim at avoiding this in the
c future, so we make it into a parameter (setting it will generate a compiler error)
      integer,parameter :: flst_lightpart = 3
      logical flst_isres(nlegborn)
      integer flst_cur_iborn,flst_cur_alr
c The following is the list of light particle flavours
c that can undergo collinear splitting
      integer flst_ncollparticles
      integer flst_collparticles(20)
      integer flst_numfinal
      common/pwhg_flst/
     1     flst_nborn, flst_born,flst_borntags,flst_bornres,flst_bornmult,
     2     flst_nreal,flst_real,flst_realtags,flst_realres,
     3     flst_nalr,flst_alr,flst_alrtags,flst_alrres,
     4     flst_nregular,flst_regular,flst_regulartags,flst_regularres,flst_regularmult,
     5     flst_regularnumrhptrs,flst_regularrhptrs,
     6     flst_uborn,flst_uborntags,flst_ubornres,flst_alrmult,
     7     flst_ubmult,flst_emitter,flst_allreg,flst_numallreg,flst_alr2born,
c     8     flst_born2alr,flst_lightpart,  ! flst_lightpart is a parameter now
     8     flst_born2alr,
     9     flst_nreson,flst_reslist,flst_bornlength,flst_reallength,
     1     flst_regularlength,flst_ubornlength,flst_alrlength,
     2     flst_ncollparticles,flst_collparticles,flst_numfsb,flst_numfsr,
     3     flst_numrhreal,flst_rhreal,flst_rhrealres,
     4     flst_rhrealtags,flst_rhreallength,
     3     flst_numrhborn,flst_rhborn,flst_rhbornres,
     4     flst_rhborntags,flst_rhbornlength,
     5     flst_alrnumrhptrs,flst_alrrhptrs,flst_rhrealnumreg,flst_rhrealreg,
     5     flst_bornnumrhptrs,flst_bornrhptrs,
     5     flst_isres,flst_cur_iborn,flst_cur_alr,
     6     flst_bornresgroup,flst_ibornresgroup,flst_nbornresgroup,flst_ibornlength,
     7     flst_bornrescurr,flst_borncurr,flst_realresgroup,flst_nrealresgroup,
     8     flst_regularresgroup,flst_iregularresgroup,flst_nregularresgroup,
     9     flst_ireallength,flst_numfinal
      save /pwhg_flst/
