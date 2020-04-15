c -*- Fortran -*-
      real * 8 physpar_ml(3)
      real * 8 physpar_mq(6)
      integer physpar_npdg
      parameter (physpar_npdg = 50)
      real * 8 physpar_phspmasses(-physpar_npdg:physpar_npdg)
      real * 8 physpar_phspwidths(-physpar_npdg:physpar_npdg)
      real * 8 physpar_pdgmasses(-physpar_npdg:physpar_npdg)
      real * 8 physpar_pdgwidths(-physpar_npdg:physpar_npdg)
      common/pwhg_physpar/physpar_ml,physpar_mq,
     1     physpar_pdgmasses,physpar_pdgwidths,
     1     physpar_phspmasses,physpar_phspwidths
      save /pwhg_physpar/
