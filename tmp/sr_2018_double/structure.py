# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py
#

## Reducible Bkg
for i in ['low_','high_']:
    structure[i+'SSWW_EW']  = {'isSignal' : 0, 'isData' : 0}#, 'removeStatUnc':1}
    #for i in ['50','150','300','450','600','750','900','1000','1250','1500','1750','2000','2500','5000','7500','10000','15000','20000']:
    for j in [i+'hmn_m50']:
        structure[j]  = {'isSignal' : 1, 'isData' : 0}#, 'removeStatUnc':1}
    structure[i+'WZ_EWK']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'WpWp_QCD']  = {'isSignal' : 0, 'isData' : 0}
    #structure['WZ_QCD']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'WZ_QCD_powheg']  = {'isSignal' : 0, 'isData' : 0}
    #structure['WZ_QCD_AMCNLO']  = {'isSignal' : 0, 'isData' : 0}
    #structure['WZ_QCD_mllmin01']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'ZZ4L']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'ggZZ']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'ttV']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'tZq']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'Vg']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'VgS_L']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'VgS_H']  = {'isSignal' : 0, 'isData' : 0}
    #structure[i+'WW']  = {'isSignal' : 0, 'isData' : 0}
    #structure[i+'ggWW']  = {'isSignal' : 0, 'isData' : 0}
    #structure[i+'top']  = {'isSignal' : 0, 'isData' : 0}
    #structure[i+'DY']  = {'isSignal' : 0, 'isData' : 0}
    #structure[i+'higgs']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'DPS']  = {'isSignal' : 0, 'isData' : 0}
    structure[i+'VVV']  = {'isSignal' : 0, 'isData' : 0}
structure['Fake']  = {'isSignal' : 0, 'isData' : 0}
structure['DATA']  = {'isSignal' : 0, 'isData' : 1}