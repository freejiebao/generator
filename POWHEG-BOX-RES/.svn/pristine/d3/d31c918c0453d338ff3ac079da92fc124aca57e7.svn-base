      program write_proc_labels_virtual
      implicit none
      character*1 s1
      character*2 s2
      character*3 s3
      character*60 buff,model
      integer maxproc,maxpart
      parameter (maxproc=999,maxpart=20)
      integer total_proc,i,j,proc_number(maxproc),npart(maxproc),
     &     partid(maxpart,maxproc),lstr(maxproc),l
      character*140 str(maxproc)
      character*2 ls
      logical need_switching
      integer date(3), time(3)
      integer flst_ml5(maxproc),k,alpha,alphas
      
      open(unit=10, file='proc_number',status='old',err=32)
      read (10,*,err=32,end=32) total_proc
      close(10)

      if (total_proc.ge.999) then
         write (*,*) 'ERROR: Too many subprocesses, cannot continue.'
         stop
      endif

      open (unit=11,file='proc_label',status='old',err=33)
      do i=1,total_proc
         read(11,*,err=33,end=33) proc_number(i),npart(i),
     &        (partid(j,i),j=1,npart(i))
         call convert_to_sting(npart(i),partid(1,i),str(i),lstr(i))
      enddo
      close(11)
      
      l=2
c we keep l=2; yields more flexible code. The *_proc.f routine in this
c case looks for a matching configuration by probing all permutations
c of the incoming flavour list before throwing an error.
c$$$      do i=npart(1),3,-1
c$$$         if (abs(partid(i,1)).gt.9) then
c$$$            l=i
c$$$            exit
c$$$         endif
c$$$      enddo
      write(ls,'(i2)') l

      if (npart(1).gt.l+1) then
         need_switching=.true.
      else
         need_switching=.false.
      endif


      open (unit=12,file='svirt_proc.f',status='unknown')

      write (12,*) '     subroutine svirt_proc(p,legs,wgt)'
      write (12,*) '     implicit none'
      write (12,*) '     include "nexternal.inc"'
      write (12,*) '     include "coupl.inc"'
      write (12,*) '     double precision wgt'
      write (12,*)
     $     '     double precision, allocatable :: virt_wgts(:,:)'
      write (12,*) '     double precision p(0:3,nexternal-1)'
      write (12,*) '     integer legs(nexternal-1),lstr,ans_dim'
      write (12,*) '     character*140 str'
      if (need_switching) then
         write (12,*) '     double precision p1(0:3,nexternal-1)'
         write (12,*) '     integer i,ic(nexternal-1),'
     &        //'legs1(nexternal-1)'
         write (12,*) '     logical mtc,even'
         write (12,*) '     '
         write (12,*) '     do i=1,nexternal-1'
         write (12,*) '        ic(i)=i'
         write (12,*) '     enddo'
         write (12,*) '     mtc=.false.'
         write (12,*) '10   call nexper(nexternal-1-'//ls//
     &        ',ic('//ls//'+1),mtc,even)'
         write (12,*) '     do i='//ls//'+1,nexternal-1'
         write (12,*) '        ic(i)=ic(i)+'//ls
         write (12,*) '     enddo'
         write (12,*) '     CALL SWITCHMOM (P,P1,IC,NEXTERNAL-1)'
         write (12,*) '     CALL SWITCHLEGS(legs,legs1,IC,NEXTERNAL-1)'
         write (12,*) '     '
         write (12,*)
     &        '     call convert_to_string(nexternal-1,legs1,str,lstr)'
      else
         write (12,*) '     '
         write (12,*)
     &        '     call convert_to_string(nexternal-1,legs,str,lstr)'
      endif
      write (12,*) '     '
      do i=1,total_proc
         if (proc_number(i).le.9) then
            s1=char(proc_number(i)+48)
         elseif(proc_number(i).le.99)then
            s2=char(proc_number(i)/10+48)
     &           //char(mod(proc_number(i),10)+48)
         elseif(proc_number(i).le.999) then
            s3=char(proc_number(i)/100+48)
     &           //char((proc_number(i)-(proc_number(i)/100)*100)/10+48)
     &           //char(mod(proc_number(i)-
     &           (proc_number(i)/100)*100,10)+48)
         endif
         if (i.eq.1) then
            write (12,*)
     &           '     if (str.eq."'//str(i)(1:lstr(i))//'") then'
         else
            write (12,*)
     &           '     elseif (str.eq."'//str(i)(1:lstr(i))//'") then'
         endif

         if (proc_number(i).le.9) then
            write (12,*) '        call ml5_'//s1/
     $           /'_get_answer_dimension'//'(ans_dim)'
         elseif (proc_number(i).le.99) then
            write (12,*) '        call ml5_'//s2/
     $           /'_get_answer_dimension'//'(ans_dim)'
         elseif (proc_number(i).le.999) then
            write (12,*) '        call ml5_'//s3/
     $           /'_get_answer_dimension'//'(ans_dim)'
         endif
         write (12,*) '        allocate(virt_wgts(0:3,0:ans_dim))' 

         if (need_switching) then
            if (proc_number(i).le.9) then
               write (12,*) '        call ml5_'//s1//'_sloopmatrix'//
     &              '(p1,virt_wgts)'
            elseif (proc_number(i).le.99) then
               write (12,*) '        call ml5_'//s2//'_sloopmatrix'//
     &              '(p1,virt_wgts)'
            elseif (proc_number(i).le.999) then
               write (12,*) '        call ml5_'//s3//'_sloopmatrix'//
     &              '(p1,virt_wgts)'
            endif
         else
            if (proc_number(i).le.9) then
               write (12,*) '        call ml5_'//s1//'_sloopmatrix'//
     &              '(p,virt_wgts)'
            elseif (proc_number(i).le.99) then
               write (12,*) '        call ml5_'//s2//'_sloopmatrix'//
     &              '(p,virt_wgts)'
            elseif (proc_number(i).le.999) then
               write (12,*) '        call ml5_'//s3//'_sloopmatrix'//
     &              '(p,virt_wgts)'
            endif
         endif
         write (12,*) '        goto 20'
      enddo
      write (12,*) '     endif'
      write (12,*) '     '
      if (need_switching) then
         write (12,*) '     do while(mtc)'
         write (12,*) '        do i='//ls//'+1,nexternal-1'
         write (12,*) '           ic(i)=ic(i)-'//ls
         write (12,*) '        enddo'
         write (12,*) '        goto 10'
         write (12,*) '     enddo'
         write (12,*) '     if (.not.mtc) then'
         write (12,*) '        write (*,*) "Error #1,'//
     &        ' in svirt_proc.f"'
         write (12,*) '        stop'
         write (12,*) '     endif'
         write (12,*) '     '
      endif
      write (12,*) '20   continue'
      write (12,*) '     wgt=virt_wgts(1,0)'
      write (12,*) '     deallocate(virt_wgts)'
      write (12,*) '     return'
      write (12,*) '     end'
      write (12,*) '     '
      write (12,*) '     '
      write (12,*) '     '
      write (12,*) '     '
      write (12,*) '     '


      open(unit=16, file='proc_couplings',status='old',err=36)
      read (16,*,err=36,end=36) alpha
      read (16,*,err=36,end=36) alphas
      close(16)

      open(unit=16,file="../Cards/proc_card.dat",status='old',err=37)
      do 
         read (16,'(a)',err=37,end=37) buff
         if (index(buff,"# Begin MODEL").ne.0) then
            read (16,*,err=37,end=37) model
            exit
         endif
      enddo
      close(16)



      open(unit=18,file='MadLoop.mg5',err=35)
      write(*,*) '************************************************'//
     $     '******'
      write(*,*) 'Writing the orderfile for MadLoop5...'
      
      write(18,*) '# MadLoop.mg5'
      write(18,*) '# Created by POWHEG-BOX'
      write(18,*)
      write(18,*) 'import model loop_'//model
      do j=1,total_proc
         do k=1,npart(1)
            flst_ml5(k)=partid(k,j)
            if (flst_ml5(k).eq.0) flst_ml5(k)=21
         enddo
         write(18,*) 'add process '
     $        ,(flst_ml5(k),k=1,2),' >', (flst_ml5(k),k=3,npart(1))
     $        ,' QED=',alpha,' QCD=',alphas-1,' [virt=QCD] @ ',j
      enddo
      write(18,*) 'output MadLoop5Library'
      write(18,*) 'launch -f'
      close(18)

 1000 format ( ' # Date ', i2.2, '/', i2.2, '/', i4.4, '; time ',
     &     i2.2, ':', i2.2, ':', i2.2 )

      return
 32   write (*,*)
     &     "ERROR: file 'proc_number' not found or not correct format."
      return
 33   write (*,*)
     &     "ERROR: file 'proc_label' not found or not correct format."
 34   write (*,*)
     &  "ERROR: file 'proc_couplings' not found or not correct format."
      return
 35   write(*,*) '******************************************'
      write(*,*) 'Problem in writing the order file'
      write(*,*) 'CANNOT PROCEED. POWHEG execution abort'
      write(*,*) '******************************************'
      return
 36   write (*,*) "ERROR: file 'proc_couplings'"/
     $     /" not found or not correct format."
      return
 37   write (*,*) "ERROR: file '../Cards/proc_card.dat'"/
     $     /" not found or not correct format."
      return
      end


      subroutine convert_to_sting(npart,id,string,lstring)
      implicit none
      integer npart,lstring,i,maxpart
      parameter (maxpart=20)
      integer id(maxpart)
      character*140 string
      character*3 s

      do i=1,140
         string(i:i)=' '
      enddo
      lstring=0
      do i=1,npart
         if (id(i).eq.21) id(i)=0
         if (abs(id(i)).le.9) then
            s=char(abs(id(i))+48)
         elseif(abs(id(i)).le.99)then
            s=char(abs(id(i))/10+48)
     &           //char(mod(abs(id(i)),10)+48)
         elseif(abs(id(i)).le.999) then
            s=char(abs(id(i))/100+48)
     &           //char((abs(id(i))-(abs(id(i))/100)*100)/10+48)
     &           //char(mod(abs(id(i))-(abs(id(i))/100)*100,10)+48)
         else
            write (*,*) 'error, particle ID is too large',abs(id(i))
            stop
         endif
         if (id(i).ge.0) then
            if (id(i).le.9) then
               string(lstring+1:lstring+1)=s
               lstring=lstring+1
            elseif (id(i).le.99) then
               string(lstring+1:lstring+2)=s
               lstring=lstring+2
            elseif (id(i).le.999) then
               string(lstring+1:lstring+3)=s
               lstring=lstring+3
            endif
         else
            if (abs(id(i)).le.9) then
               string(lstring+1:lstring+2)='-'//s
               lstring=lstring+2
            elseif (abs(id(i)).le.99) then
               string(lstring+1:lstring+3)='-'//s
               lstring=lstring+3
            elseif (abs(id(i)).le.999) then
               string(lstring+1:lstring+4)='-'//s
               lstring=lstring+4
            endif
         endif
      enddo
      end
