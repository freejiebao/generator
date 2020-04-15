#!/bin/bash

RUNDIR=${PWD}

svn export ../MadGraphStuff_MadLoop MadTMP
# cp -ra ../MadGraphStuff_MadLoop MadTMP

if [ -e proc_card.dat ]
then
\cp proc_card.dat MadTMP/Cards/
else
echo proc_card.dat missing!
exit -1
fi

cd MadTMP

./NewProcess.sh $*

# commented wrt the original version  26/3/2013
#echo editing DHELAS/Makefile
#sed -i 's/FC[\t ]*=.*// ; s/^DEST[\t ]*=.*/DEST = ..\// ;  s/^LIBRARY[\t ]*=.*/LIBRARY = ..\/libdhelas3.a/'   DHELAS/Makefile
#echo editing MODEL/makefile
#sed -i 's/^F77[\t ]*=.*// ; s/-ffixed-line-length-132// ; s/^LIBDIR[\t ]*=.*/LIBDIR = ..\// ' MODEL/makefile
#echo editing Madlib/makefile
#sed -i 's/^F77[\t ]*=.*// ; s/^LIBDIR[\t ]*=.*/LIBDIR = ..\// ' Madlib/makefile


# -n: do not overwrite existing files

echo > ../MGfiles.list

for i in *
do
# -a : exists, file or directory
if ! [ -a ../$i ]
then
    mv $i ../
    echo $i >> ../MGfiles.list
fi
done

cd $RUNDIR
rm -fr MadTMP


mkdir obj-gfortran
