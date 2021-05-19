import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH206
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

#mcDirectory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/'
mcDirectory = '/eos/user/j/jixiao/HWWnano3/link/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

treeBaseDir = '/eos/user/j/jixiao/HWWnano3/link'#/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'
def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

################################################
############ BASIC MC WEIGHTS ##################
################################################
mcCommonWeightNoMatch = 'SFweight*(Lepton_pt[0]<=200)*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeight = 'SFweight*(Lepton_pt[0]<=200)*PromptGenLepMatch2l*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeightNoMatch_new = 'sfweight*(Lepton_pt[0]>200)*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeight_new = 'sfweight*(Lepton_pt[0]>200)*PromptGenLepMatch2l*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeightNoMatch_ge = 'sfweight_ge*(Lepton_pt[0]>200)*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeight_ge = 'sfweight_ge*(Lepton_pt[0]>200)*PromptGenLepMatch2l*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeightNoMatch_res = 'sfweight_res*(Lepton_pt[0]>200)*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
mcCommonWeight_res = 'sfweight_res*(Lepton_pt[0]>200)*PromptGenLepMatch2l*(Alt$(Lepton_pdgId[0],-9999) * Alt$(Lepton_pdgId[1],9999) > 0)'
############################################
############ MORE MC STAT ##################
############################################

def CombineBaseW(samples, proc, samplelist):
    newbaseW = getBaseWnAOD(mcDirectory, mcProduction, samplelist)
    for s in samplelist:
        addSampleWeight(samples, proc, s, newbaseW+'/baseW')

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
    ['A','Run2018A-02Apr2020-v1'] ,
    ['B','Run2018B-02Apr2020-v1'] ,
    ['C','Run2018C-02Apr2020-v1'] ,
    ['D','Run2018D-02Apr2020-v1'] ,
]
DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
    'MuonEG'         : 'Trigger_ElMu' ,
    'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
    'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
    'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
}
###########################################
############  Reducible Bkg  ##############
###########################################
### Signal
#for i in ['hmn_m50','hmn_m150','hmn_m300','hmn_m450','hmn_m600','hmn_m750','hmn_m900','hmn_m1000','hmn_m1250','hmn_m1500','hmn_m1750','hmn_m2000','hmn_m2500','hmn_m5000','hmn_m7500','hmn_m10000','hmn_m15000','hmn_m20000','sswwjj_dim5']:
for i in ['hmn_m50']:
    files = nanoGetSampleFiles(mcDirectory, i)
    samples['low_'+i] = {
        'name': files,
        'weight': mcCommonWeight,
        'suppressNegative' :['all'],
        'suppressNegativeNuisances' :['all'],
        'FilesPerJob': 4
    }
    samples['high_' + i] = {
        'name': files,
        'weight': mcCommonWeight_new,
        'suppressNegative': ['all'],
        'suppressNegativeNuisances': ['all'],
        'FilesPerJob': 4
    }
    #samples['ge_' + i] = {
    #    'name': files,
    #    'weight': mcCommonWeight_ge,
    #    'suppressNegative': ['all'],
    #    'suppressNegativeNuisances': ['all'],
    #    'FilesPerJob': 4
    #}
    #samples['res_' + i] = {
    #    'name': files,
    #    'weight': mcCommonWeight_res,
    #    'suppressNegative': ['all'],
    #    'suppressNegativeNuisances': ['all'],
    #    'FilesPerJob': 4
    #}
# WWjj EW
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK_madgraph')
samples['low_SSWW_EW'] = {
    'name': files,
    'weight': mcCommonWeight+"*EW_weight",
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_SSWW_EW'] = {
    'name': files,
    'weight': mcCommonWeight_new+"*EW_weight",
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_SSWW_EW'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge+"*EW_weight",
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_SSWW_EW'] = {
#    'name': files,
#    'weight': mcCommonWeight_res+"*EW_weight",
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
### WWjj QCD
files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD')
samples['low_WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_WpWp_QCD'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_WpWp_QCD'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_WpWp_QCD'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
### EW WZ
files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_EWK')
samples['low_WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight+"*EW_weight",
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_WZ_EWK'] = {
    'name': files,
    'weight': mcCommonWeight_new+"*EW_weight",
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_WZ_EWK'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge+"*EW_weight",
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_WZ_EWK'] = {
#    'name': files,
#    'weight': mcCommonWeight_res+"*EW_weight",
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
### WZ QCD
files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_powheg')
samples['low_WZ_QCD_powheg'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_WZ_QCD_powheg'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_WZ_QCD_powheg'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_WZ_QCD_powheg'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}

### Interference
# need:
# WpWpJJ_Interference_TuneCUETP8M1_13TeV-madgraph-pythia8
# WLLJJ_WToLNu_Interference_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8
#files = nanoGetSampleFiles(mcDirectory, 'WpWpJJ_Interference')
#samples['WpWpJJ_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#files = nanoGetSampleFiles(mcDirectory, 'WLLJJ_WToLNu_Interference')
#samples['WLLJJ_WToLNu_Interference'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}

### ZZ
# need:
# ZZJJTo4L_EWK_TuneCP5_13TeV-madgraph-pythia8
# ZZJJTo4L_QCD_TuneCP5_13TeV-madgraph-pythia8
# GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8
#files = nanoGetSampleFiles(mcDirectory, 'ZZJJTo4L_EWK') + \
#        nanoGetSampleFiles(mcDirectory, 'ZZJJTo4L_QCD')
files = nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2')
samples['low_ZZ4L'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_ZZ4L'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_ZZ4L'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_ZZ4L'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}

files = nanoGetSampleFiles(mcDirectory, 'ggZZ2e2m') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2e2t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ2m2t') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4m_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'ggZZ4t')
        #nanoGetSampleFiles(mcDirectory, 'ggZZ4e')
samples['low_ggZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_ggZZ'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_ggZZ'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_ggZZ'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}

### TVX
# need:
# TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8
# TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8
# TTWJetsToQQ_TuneTuneCP5_13TeV-amcatnloFXFX-madspin-pythia8
files = nanoGetSampleFiles(mcDirectory, 'TTZToLLNuNu_M-10') + \
        nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu')
samples['low_ttV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_ttV'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_ttV'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_ttV'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#files = nanoGetSampleFiles(mcDirectory, 'TTZjets') + \
#        nanoGetSampleFiles(mcDirectory, 'TTWjets')
#samples['ttV_inclusive'] = {
#    'name': files,
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
files = nanoGetSampleFiles(mcDirectory, 'tZq_ll')
samples['low_tZq'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_tZq'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_tZq'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_tZq'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
### Vg
# need:
# LLAJJ_EWK_MLL-50_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# LNuAJJ_EWK_MJJ-120_TuneCP5_13TeV-madgraph-pythia8
# old: WGJJ Zg
files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ')
samples['low_Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 6
}
samples['high_Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch_new + '*!(Gen_ZGstar_mass > 0)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 6
}
#samples['ge_Vg'] = {
#    'name': files,
#    'weight': mcCommonWeightNoMatch_ge + '*!(Gen_ZGstar_mass > 0)',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 6
#}
#samples['res_Vg'] = {
#    'name': files,
#    'weight': mcCommonWeightNoMatch_res + '*!(Gen_ZGstar_mass > 0)',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 6
#}
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WGJJ') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
samples['low_VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'low_VgS', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'low_VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'low_VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

samples['high_VgS'] = {
    'name': files,
    'weight': mcCommonWeight_new + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4,
    'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'high_VgS', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'high_VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'high_VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

#samples['ge_VgS'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4,
#    'subsamples': {
#        'L': 'gstarLow',
#        'H': 'gstarHigh'
#    }
#}
#addSampleWeight(samples, 'ge_VgS', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#addSampleWeight(samples, 'ge_VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
#addSampleWeight(samples, 'ge_VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
#
#samples['res_VgS'] = {
#    'name': files,
#    'weight': mcCommonWeight_res + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4,
#    'subsamples': {
#        'L': 'gstarLow',
#        'H': 'gstarHigh'
#    }
#}
#addSampleWeight(samples, 'res_VgS', 'WGJJ', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#addSampleWeight(samples, 'res_VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
#addSampleWeight(samples, 'res_VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
# Others
files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu_DoubleScattering')
samples['low_DPS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_DPS'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_DPS'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_DPS'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW') + \
        nanoGetSampleFiles(mcDirectory, 'WWG')
samples['low_VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
samples['high_VVV'] = {
    'name': files,
    'weight': mcCommonWeight_new,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#samples['ge_VVV'] = {
#    'name': files,
#    'weight': mcCommonWeight_ge,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#samples['res_VVV'] = {
#    'name': files,
#    'weight': mcCommonWeight_res,
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4
#}
#%%%%%%%%%%%%%
### Wrong-sign
#files = nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu')
#samples['WW'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os*nllW',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4,
#}
#files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')
#samples['ggWW'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os*1.53/1.4',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4,
#}
#files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
#        nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1') + \
#        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1')
#samples['top'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 3,
#}
#addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
## MIT:
## DY0JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY1JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY2JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY3JetsToLL_M-50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY0JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY1JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY2JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
## DY3JetsToLL_M-10to50_TuneTuneCP5_13TeV-madgraphMLM-pythia8
#files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-100to200') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-200to400') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-400to600') + \
#        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-600toInf')
#samples['DY'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4,
#}
#CombineBaseW(samples, 'DY', ['DYJetsToLL_M-10to50-LO',                  'DYJetsToLL_M-10to50-LO_ext1'])
#
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_ext2',             'DY_NLO_pTllrw*(LHE_HT < 70)')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-10to50-LO',           'DY_LO_pTllrw*(LHE_HT < 100)')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-10to50-LO_ext1',      'DY_LO_pTllrw*(LHE_HT < 100)')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-70to100',       'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-100to200',      'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-200to400',      'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-400to600',      'DY_LO_pTllrw')
##addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-400to600_ext2', 'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-600to800',      'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-800to1200',     'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-1200to2500',    'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-50_HT-2500toInf',     'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-4to50_HT-100to200',   'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-4to50_HT-200to400',   'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-4to50_HT-400to600',   'DY_LO_pTllrw')
#addSampleWeight(samples,    'DY',   'DYJetsToLL_M-4to50_HT-600toInf',   'DY_LO_pTllrw')
## need:
## GluGluHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
## # not found: VBFHToZZTo4L_M125_13TeV_powheg2_JHUGenV714_pythia8
## VHToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8
#files = nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'HZJ_HToWW_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWW_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125')+nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125')+\
#        nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125') + \
#        nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125')
#samples['higgs'] = {
#    'name': files,
#    'weight': 'mcCommonWeight_os',
#    'suppressNegative' :['all'],
#    'suppressNegativeNuisances' :['all'],
#    'FilesPerJob': 4,
#}
#addSampleWeight(samples, 'higgs', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral
#addSampleWeight(samples, 'higgs', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')

###########################################
################## FAKE ###################
###########################################
#1389 files
samples['Fake'] = {
    'name': [],
    'weight': 'METFilter_DATA*fakeW*(Alt$(Lepton_pdgId[0],-9999)*Alt$(Lepton_pdgId[1],9999)>0)',
    'weights': [],
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'isData': ['all'],
    'FilesPerJob': 47
}
for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__fakeW/', pd + '_' + sd)
        samples['Fake']['name'].extend(files)
        samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))
#samples['Fake']['subsamples'] = {
#    'em': 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 13',
#    'me': 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 11',
#    'ee': 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11',
#    'mm': 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13',
#}
###########################################
################## DATA ###################
samples['DATA'] = {
    'name': [],
    'weight': 'METFilter_DATA*LepWPCut*(Alt$(Lepton_pdgId[0],-9999)*Alt$(Lepton_pdgId[1],9999)>0)',
    'weights': [],
    'isData': ['all'],
    'FilesPerJob': 47
}

for _, sd in DataRun:
    for pd in DataSets:
        files = nanoGetSampleFiles('/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7/', pd + '_' + sd)
        samples['DATA']['name'].extend(files)
        samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
