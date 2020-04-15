c -*- Fortran -*-


      integer, parameter :: maxptrs=10
      integer, parameter :: nintervals=50
      character * 20 :: mintw_currid
      type mintw_pointer
         sequence
         character * 20 :: id
         real * 8, pointer :: wind(:),accind(:),yindmax(:),yindmaxrat(:),
     1        xgrid(:,:),xacc(:,:),ymax(:,:),ymaxrat(:,:),xmmm(:,:),xindmmm(:),
     2        totj(:),totabsj(:),totposj(:),totnegj(:),etotj(:),etotabsj(:),
     3        etotposj(:),etotnegj(:),results(:),cumulant(:)
         integer, pointer :: ifold(:),indhits(:),nhits(:,:),signs(:)
         real * 8 :: xint,ans,err,gen_sigma,gen_sigma2,gen_isigma,gen_totev
         real * 8, pointer :: tot,totabs,totpos,totneg,etot,etotabs,etotpos,etotneg
         integer :: ncall,itmx,ndim,nind
         integer, pointer :: nchannels,nentries
      end type mintw_pointer

      type(mintw_pointer) :: mintw_ptrs(maxptrs)

      integer mintw_nptrs
      common/pwhg_mintw/mintw_ptrs,mintw_nptrs,mintw_currid

      
