#!/bin/bash

DOPYTHIAPS=0

export LD_LIBRARY_PATH=/PATH_TO_RECOLA2/recola2-collier-XYZ/recola2-XYZ

> Timings.txt

PRG=../pwhg_main
#-nores


# two stages of importance sampling grid calculation
for igrid in {1..2}
do
    
    (echo -n st1 xg$igrid ' ' ; date ) >> Timings.txt
    
    cat powheg.input-save | sed "s/xgriditeration.*/xgriditeration $igrid/ ; s/parallelstage.*/parallelstage 1/" > powheg.input
    
    for i in {1..25}
    do
	echo $i | $PRG > run-st1-xg$igrid-$i.log 2>&1 &
    done
    wait
    
done


# compute NLO and upper bounding envelope for underlying born comfigurations
cat powheg.input-save | sed 's/parallelstage.*/parallelstage 2/ ; s/fakevirt.*/fakevirt 0/' > powheg.input
(echo -n st2 ' ' ; date ) >> Timings.txt
for i in {1..25}
do
    echo $i | $PRG > run-st2-$i.log 2>&1 &
done
wait



#
## compute upper bounding coefficients for radiation
cat powheg.input-save | sed 's/parallelstage.*/parallelstage 3/' > powheg.input
(echo -n st3 ' ' ; date ) >> Timings.txt
for i in {1..25}
do
    echo $i | $PRG > run-st3-$i.log 2>&1 &
done
wait

## generate events 
cat powheg.input-save | sed 's/parallelstage.*/parallelstage 4/ ; s/fakevirt.*/fakevirt 0/' > powheg.input
(echo -n st4 ' ' ; date ) >> Timings.txt
for i in {1..2000}
do
    echo $i | $PRG > run-st4-$i.log 2>&1 &
done
wait
#
# write the ub correction factors needed to run pythia
for file in pwgcounters-st4-????.dat
do
    ../../Scripts/FindReweightFromCounters.py $file > rwgt-$file
done


# run the parton-shower
if [ $DOPYTHIAPS -eq 1 ]
then
    for i in {1..2000}	 
    do
	if [ $i -lt 10 ]
	then
	    suffevt=pwgevents-000
	    suffwgt=rwgt-pwgcounters-st4-000
	elif [ $i -ge 10  ] && [ $i -lt 100  ]
	then
	    suffevt=pwgevents-00
	    suffwgt=rwgt-pwgcounters-st4-00
	elif [ $i -ge 100  ] && [ $i -lt 1000  ]
	then
	    suffevt=pwgevents-0
	    suffwgt=rwgt-pwgcounters-st4-0
	else
	    suffevt=pwgevents-
	    suffwgt=rwgt-pwgcounters-st4-
	fi
	cp powheg.input-save $i-powheg.input
	grep ub_btilde_corr $suffwgt$i.dat >> $i-powheg.input
	grep ub_remn_corr $suffwgt$i.dat >> $i-powheg.input
	echo '    ' >> $i-powheg.input
	
	echo $i > input-$i
	echo $suffevt$i.lhe >> input-$i
	../main-PYTHIA82-lhef < input-$i
    done
fi

(echo -n end ' ' ; date ) >> Timings.txt




