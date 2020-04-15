      program versioninclude
      implicit none
      character * 400 string0
      character * 400 string
      character * 1 ench
      integer lchunks
      parameter (lchunks=50)
      integer ios,j,lll,k
      open(unit=11,file='svnversion.txt',iostat=ios,status='old')
      if(ios.ne.0) then
         write(*,*) ' cannot find svnversion.txt'
         call exit(-1)
      endif
      open(unit=13,file='svnversion.tmp',status='unknown')
      write(13,'(a)') 'c -*- Fortran -*-'
      write(13,'(a)')
     1 "      call pwhg_io_write(iun, 'SVN status Begin')"
      do j=1,1000000
         read(unit=11,fmt='(a)',iostat=ios,end=99) string0
         write(13,'(a)') "      call pwhg_io_write(iun,"
 1       k=index(string0,"'")
         if(k==0) then
            string=string0
            string0=""
            ench=""
         else
            string=string0(1:k-1)
            string0=string0(k+1:)
            ench="'"
         endif
         lll = len(trim(string))
         do while(lll.gt.lchunks)
            write(13,'(a)') "     1'"//string(1:lchunks)//"'//"
            string = string(lchunks+1:)
            lll = lll-lchunks
         enddo
         write(13,'(a)') "     1'"//string(1:lll)//"'"//'//"'
     1      //trim(ench)//'"//'
         if(string0 /= "") goto 1
         write(13,'(a)') "     1  '' )"
      enddo
 99   continue
      write(13,'(a)') "      call pwhg_io_write(iun, 'SVN status End')"
      close(11)
      close(13)
      end
