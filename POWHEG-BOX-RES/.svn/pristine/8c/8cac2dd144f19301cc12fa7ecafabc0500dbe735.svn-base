c -*- Fortran -*-

c external (i.e. not including intermediate resonances) particles in the born process
      integer nlegbornexternal
      parameter (nlegbornexternal=<NLEGBORNEXTERNAL>)
      integer nlegrealexternal
      parameter (nlegrealexternal=nlegbornexternal+1)

c external particles including possible resonances
      integer nlegborn,nlegreal
      parameter (nlegborn=<NLEGBORN> )
      parameter (nlegreal=nlegborn+1)

      integer ndiminteg
c      parameter (ndiminteg=<NDIMINTEG>)
      parameter (ndiminteg=(nlegreal-2-(nlegborn-nlegbornexternal))*3-4+2)


c hard coded arrays. increase size if necessary.
      integer maxprocborn,maxprocreal
      parameter (maxprocborn=999,maxprocreal=999)

      integer maxalr
      parameter (maxalr=maxprocreal*nlegreal*(nlegreal-1)/2)

      integer maxreshists
      parameter (maxreshists=500)


