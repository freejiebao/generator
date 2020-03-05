### To generate restrict_card.dat
```
python3 build_restrict.py
```
### To generate cards
```
START=$PWD
git clone git@github.com:cms-sw/genproductions.git
cd genproductions/bin/MadGraph5_aMCatNLO
sed -i "s/^.*cms-project-generators\/\$model.*$/            wget --no-check-certificate http:\/\/stash.osgconnect.net\/+jiexiao\/\$model/" gridpack_generation.sh
mkdir cards/eft
pushd cards/eft
python $START/build_cards.py
```