exit_on_error() {
    result=$1
    code=$2
    message=$3

    if [ $1 != 0 ]; then
        echo $3
        exit $2
    fi
}

#### FRAMEWORK SANDBOX SETUP ####
# Load cmssw_setup function
source cmssw_setup.sh

# Setup CMSSW Base
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/SMP-RunIISummer15wmLHEGS-00006_1_cfg.py .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/SMP-RunIISummer16DR80Premix-00098_1_cfg.py .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/SMP-RunIISummer16DR80Premix-00098_2_cfg.py .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/SMP-RunIISummer16MiniAODv3-00004_1_cfg.py .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/SMP-RunIISummer16NanoAODv5-00095_1_cfg.py .


# Download sandbox, replace it when you have different sandbox_name
sandbox_name1="sandbox-CMSSW_7_1_21_patch2-6f38682.tar.bz2"
sandbox_name2="sandbox-CMSSW_8_0_21-278a0a7.tar.bz2"
sandbox_name3="sandbox-CMSSW_9_4_9-0ddecda.tar.bz2"
sandbox_name4="sandbox-CMSSW_10_2_15-6be322f.tar.bz2"
# Change to your own http
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/$sandbox_name1 .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/$sandbox_name2 .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/$sandbox_name3 .
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/2016reco/$sandbox_name4 .
pushd .
# Setup framework from sandbox
cmssw_setup $sandbox_name1 || exit_on_error $? 151 "Could not unpack sandbox"
popd
sandbox_name="VBS_SSWW_$1_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
xrdcp root://eosuser.cern.ch//eos/user/j/jixiao/eft/gridpack/2016/$sandbox_name .
sed -i "s/^.*tarball.tar.xz.*$/     args = cms.vstring(\'..\/$sandbox_name\')/" -i SMP-RunIISummer15wmLHEGS-00006_1_cfg.py

cmsRun SMP-RunIISummer15wmLHEGS-00006_1_cfg.py
rm $sandbox_name
rm -rf cmssw-tmp

pushd .
cmssw_setup $sandbox_name2 
popd
cmsRun SMP-RunIISummer16DR80Premix-00098_1_cfg.py
rm *_inLHE.root *wmLHEGS*.root
cmsRun SMP-RunIISummer16DR80Premix-00098_2_cfg.py
rm *DRPremix*step1.root
rm -rf cmssw-tmp


pushd .
cmssw_setup $sandbox_name3 
popd
cmsRun SMP-RunIISummer16MiniAODv3-00004_1_cfg.py
rm *DRPremix*.root
rm -rf cmssw-tmp

# Setup framework from sandbox
pushd .
cmssw_setup $sandbox_name4 || exit_on_error $? 151 "Could not unpack sandbox"
popd
cmsRun SMP-RunIISummer16NanoAODv5-00095_1_cfg.py
rm *MiniAOD*.root
# clean
rm -rf cmssw-tmp

rm *py
rm *pyc
rm $sandbox_name1
rm $sandbox_name2
rm $sandbox_name3
rm $sandbox_name4
