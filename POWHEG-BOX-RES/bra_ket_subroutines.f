      function dotp(p1,p2)
      implicit none
      real * 8 dotp,p1(0:3),p2(0:3)
      dotp = (p1(0)*p2(0) - p1(3)*p2(3)) - p1(1)*p2(1) - p1(2)*p2(2)
      end

      function momsq03(p)
      implicit none
      real * 8 momsq03,p(0:3)
      momsq03 = p(0)**2-p(1)**2-p(2)**2-p(3)**2
      end

      function cdotp(p1,cp2)
      implicit none      
      complex * 16 cdotp,cp2(0:3)
      real * 8 p1(0:3)
      cdotp = (p1(0)*cp2(0) - p1(3)*cp2(3))
     #      - p1(1)*cp2(1) - p1(2)*cp2(2)
      end
      
      function ccdotp(cp1,cp2)
      implicit none      
      complex * 16 ccdotp,cp1(0:3),cp2(0:3)
      ccdotp = (cp1(0)*cp2(0) - cp1(3)*cp2(3))
     #     - cp1(1)*cp2(1) - cp1(2)*cp2(2)
      end

