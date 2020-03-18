#! /bin/bash

exit_on_error() {
    result=$1
    code=$2
    message=$3

    if [ $1 != 0 ]; then
        echo $3
        exit $2
    fi
}

# Setup CMSSW Base
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# Download sandbox
sandbox_name="VBS_SSWW_$1_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
wget --no-check-certificate --progress=bar "http://stash.osgconnect.net/+jiexiao/eft/${sandbox_name}" || exit_on_error $? 150 "Could not download sandbox."

# Setup framework from sandbox
tar -avxf ${sandbox_name}
date
echo this is the $2-th job
./runcmsgrid.sh 2500 $2 4
date
rm $sandbox_name
