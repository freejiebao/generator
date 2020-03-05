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
wget https://raw.githubusercontent.com/freejiebao/generator/master/model/build_cards.py
python build_cards.py
rm build_cards.py
popd
```