c          -*- fortran -*-
      integer par_maxseeds,par_maxxgriditerations
      parameter (par_maxxgriditerations=10)
      
      real * 8 par_diexp,par_dijexp,par_2gsupp,
     1     par_fsrtinycsi,par_fsrtinyy,
     2     par_isrtinycsi,par_isrtinyy,
     2     par_mintupb_ratlim
      common/pwhg_par/par_diexp,par_dijexp,par_2gsupp,
     1         par_fsrtinycsi,par_fsrtinyy,
     2         par_isrtinycsi,par_isrtinyy,
     3         par_mintupb_ratlim,
     3         par_maxseeds
      save /pwhg_par/
