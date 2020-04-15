c -*-Fortran-*-
      integer,parameter :: maxflav=30
      integer,parameter :: maxres=20
      integer,parameter :: invalid=-2001
      integer,parameter :: maxstored=20
      integer,parameter :: nlegs = nlegreal
      integer,parameter :: maxhistories = maxprocreal
      integer res_powew,res_powst
      common/pwhg_res/res_powew,res_powst

      integer res_arrflav(nlegs,maxhistories),res_arrresflav(nlegs,maxhistories),
     1          res_arrlength(maxhistories),nfound
      common/arrs/nfound,res_arrflav,res_arrresflav,res_arrlength

c$$$      integer,parameter :: maxflav=30
c$$$      integer,parameter :: maxres=10
c$$$      integer,parameter :: invalid=-2001
c$$$      integer,parameter :: maxstored=20
c$$$      integer,parameter :: nlegs = 20
c$$$      integer,parameter :: maxhistories = 40
