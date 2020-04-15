      function btilde(iresgroup,xx,www0,ifirst,imode,
     1     retval,retval0)
      implicit none
      include 'nlegborn.h'
      real * 8 xx(ndiminteg),www0,retval,retval0
      integer btilde,iresgroup,ifirst,imode
      real * 8, save :: tot(2)
      btilde=0
      tot=0
      if(iresgroup == 1) then
         tot(1) =  www0
      elseif(iresgroup == 2) then
         tot(2) =  www0
      endif
      retval0 = tot(1)+tot(2)
      if(imode == 1) then
         if(iresgroup == 1) then
            tot(1) = xx(1)**2 * www0
         elseif(iresgroup == 2) then
            tot(2) = xx(1)**3 * www0
         endif
         retval = tot(1)+tot(2)
      endif
      if(ifirst == 2) then
         call adduptotals(tot,2)
      endif
      end


      
