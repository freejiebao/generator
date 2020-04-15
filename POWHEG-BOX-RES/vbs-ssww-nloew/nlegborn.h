c -*- Fortran -*-      
      integer nlegborn,nlegreal
      parameter (nlegborn=    13 )
      parameter (nlegreal=nlegborn+1)
      
      integer ndiminteg
c -(1) because of the 1 resonances
      parameter (ndiminteg=24)!(nlegreal-2)*3-4+2)
      
      integer maxprocborn,maxprocreal
      parameter (maxprocborn=999,maxprocreal=999)
      
      integer maxalr
      parameter (maxalr=maxprocreal*nlegreal*(nlegreal-1)/2)

      integer maxreshists
c      parameter (maxreshists=150)
      parameter (maxreshists=190)

      integer nlegbornexternal
      parameter (nlegbornexternal=8)

c      integer maxresgroups
c      parameter (maxresgroups=2)
