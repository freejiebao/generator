### To generate restrict_card.dat
```
python3 build_restrict.py
```
### To generate cards
```
git clone git@github.com:cms-sw/genproductions.git
pushd genproductions/bin/MadGraph5_aMCatNLO
sed -i "s/^.*cms-project-generators\/\$model.*$/            wget --no-check-certificate http:\/\/stash.osgconnect.net\/+jiexiao\/\$model/" gridpack_generation.sh
mkdir cards/eft
cd cards/eft
wget https://raw.githubusercontent.com/freejiebao/generator/master/model/build_cards.py
python build_cards.py
rm build_cards.py
popd
tar zcvf genproductions.tar.gz genproductions
```
### To buile condor scripts
```
mkdir eft
cd eft
mkdir log
wget https://raw.githubusercontent.com/freejiebao/generator/master/model/build_submit.py
python build_submit.py
rm build_submit.py
```
### To submit jobs
```
voms-proxy-init --voms cms --valid 192:00
wget https://raw.githubusercontent.com/freejiebao/generator/master/model/submit_jobs.py
python submit_jobs.py
rm submit_jobs.py
```