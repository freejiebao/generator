import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # ggH
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}
bAlgo = "deepcsv"#deepcsv deepflav
bWP = "0.4184" 
# deepjet 0.0494 0.2770 0.7264
# deepcsv 0.1241 0.4184 0.7527

mc = [skey for skey in samples if skey not in ('Fake','DATA')]
# tau veto
aliases['tauVeto_ww'] = {
    'expr': '(Sum$(Tau_pt > 20 && abs(Tau_eta)<2.3 && (Tau_idMVAoldDM2017v2>> 1 & 1) && Tau_idDecayMode &&sqrt( pow(Tau_eta - Lepton_eta[0], 2) + pow(abs(abs(Tau_phi - Lepton_phi[0])-pi)-pi, 2) ) >= 0.4 && sqrt( pow(Tau_eta - Lepton_eta[1], 2) + pow(abs(abs(Tau_phi - Lepton_phi[1])-pi)-pi, 2) ) >= 0.4) == 0)'
}
# muon nuis
aliases['Lepton_newpt'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_newpt.cc+'.format(configurations)],
    'class': 'Mu_Smear',
    'args': (2018),
    'samples': mc+["DATA","Fake"],
}
aliases['Lepton_gept'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_ge.cc+'.format(configurations)],
    'class': 'Mu_GE',
    'args': (2018),
    'samples': mc+["DATA","Fake"],
}
aliases['Lepton_respt'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_res.cc+'.format(configurations)],
    'class': 'Mu_RES',
    'args': (2018),
    'samples': mc+["DATA","Fake"],
}
aliases['sf_up'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_reco_eff.cc+'.format(configurations)],
    'class': 'Mu_RecoSF',
    'args': ("2018","UP",2,"NEWPT"),
    'samples': mc,
}
aliases['sf_nom'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_reco_eff.cc+'.format(configurations)],
    'class': 'Mu_RecoSF',
    'args': ("2018","NOM",2,"NEWPT"),
    'samples': mc,
}
aliases['sf_do'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_reco_eff.cc+'.format(configurations)],
    'class': 'Mu_RecoSF',
    'args': ("2018","DOWN",2,"NEWPT"),
    'samples': mc,
}
aliases['sf_ge'] = {
    #'linesToAdd': ['.L {}/heavyn/macro/muon_reco_eff.cc+'.format(configurations)],
    'class': 'Mu_RecoSF',
    'args': ("2018","NOM",2,"GE"),
    'samples': mc,
}
aliases['sf_res'] = {
    #'linesToAdd': ['.L {}/heavyn/macro/muon_reco_eff.cc+'.format(configurations)],
    'class': 'Mu_RecoSF',
    'args': ("2018","NOM",2,"RES"),
    'samples': mc,
}

aliases['new_metpt'] = {
    'linesToAdd': ['.L {}/heavyn/macro/muon_met_mll.cc+'.format(configurations)],
    'class': 'Mu_MET_MLL',
    'args': (2018,2,"met","NOM"),
    'samples': mc+["DATA","Fake"],
}
aliases['new_mll'] = {
    'class': 'Mu_MET_MLL',
    'args': (2018,2,"mll","NOM"),
    'samples': mc+["DATA","Fake"],
}
aliases['res_metpt'] = {
    'class': 'Mu_MET_MLL',
    'args': (2018,2,"met","RES"),
    'samples': mc+["DATA","Fake"],
}
aliases['res_mll'] = {
    'class': 'Mu_MET_MLL',
    'args': (2018,2,"mll","RES"),
    'samples': mc+["DATA","Fake"],
}
aliases['ge_metpt'] = {
    'class': 'Mu_MET_MLL',
    'args': (2018,2,"met","GE"),
    'samples': mc+["DATA","Fake"],
}
aliases['ge_mll'] = {
    'class': 'Mu_MET_MLL',
    'args': (2018,2,"mll","GE"),
    'samples': mc+["DATA","Fake"],
}

# lepton sf
eleWP = 'mvaFall17V1Iso_WP90_SS'
muWP = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': ['low_VgS','high_VgS','ge_VgS','res_VgS']
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': ['low_VgS','high_VgS','ge_VgS','res_VgS']
}
# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}
# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}
aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}
aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/Differential/ngenjet.cc+' % configurations],
    'class': 'CountGenJet',
    'samples': mc
}
##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'getGenZpt',
    'samples': ['DY']
}
handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()

aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2018']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2018']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['Weight2MINLO'] = {
    'linesToAdd': ['.L %s/Differential/weight2MINLO.cc+' % configurations],
    'class': 'Weight2MINLO',
    'args': '%s/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root' % os.getenv('CMSSW_BASE'),
    'samples' : [skey for skey in samples if 'higgs' in skey],
}

#bjet
# https://github.com/latinos/PlotsConfigurations/blob/872c891b67cc9b8e678e6601a2149b9ba354c13d/Configurations/HighMass/v7_Full2018/aliases.py#L189
# B tagging
if bAlgo == "deepcsv": 
  aliases['bVeto'] = {
      'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > {0}) == 0'.format(bWP)
  }

  aliases['bReq'] = {
      'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > {0}) >= 1'.format(bWP)
  }

elif bAlgo == "deepflav":
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] > {0}) == 0'.format(bWP)
    }        
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] > {0}) >= 1'.format(bWP)
    }

aliases['bReq0j'] = {
    'expr': '(Alt$(CleanJet_pt[0], 0) < 30.) && !bVeto'
}

# B tag scale factors
if bAlgo == "deepcsv":
    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log( {0} * Jet_btagSF_deepcsv_shape[CleanJet_jetIdx] + !{0} * 1 )))'.format('(CleanJet_pt>=20 && abs(CleanJet_eta)<2.5)'),
        'samples': mc
    }

    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log( {0} * Jet_btagSF_deepcsv_shape[CleanJet_jetIdx] + !{0} * 1 )))'.format('(CleanJet_pt>=30 && abs(CleanJet_eta)<2.5)'),
        'samples': mc
    }

    aliases['bReq0jSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log( {0} * Jet_btagSF_deepcsv_shape[CleanJet_jetIdx] + !{0} * 1 )))'.format('(CleanJet_pt>=20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)'),
        'samples': mc
    }

    aliases['btagSF'] = {
        'expr': 'bVetoSF*bVeto + bReqSF*bReq + bReq0jSF*bReq0j + (!bVeto && !bReq && !bReq0j)',
        'samples': mc
    }

    for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
        for targ in ['bVeto', 'bReq', 'bReq0j']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_up_%s' % shift)

            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_down_%s' % shift)

        aliases['btagSF%sup' % shift] = {
            'expr': 'bVetoSF{shift}up*bVeto + bReqSF{shift}up*bReq + bReq0jSF{shift}up*bReq0j + (!bVeto && !bReq && !bReq0j)'.format(shift = shift),
            'samples': mc
        }

        aliases['btagSF%sdown' % shift] = {
            'expr': 'bVetoSF{shift}down*bVeto + bReqSF{shift}down*bReq + bReq0jSF{shift}down*bReq0j + (!bVeto && !bReq && !bReq0j)'.format(shift = shift),
            'samples': mc
        }
elif bAlgo == "deepflav":
    btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepJet_102XSF_V2.csv' % os.getenv('CMSSW_BASE')
    aliases['Jet_btagSF_deepflav_shape'] = {
        'linesToAdd': [
            'gSystem->Load("libCondFormatsBTauObjects.so");',
            'gSystem->Load("libCondToolsBTau.so");',
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L %s/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+' % os.getenv('CMSSW_BASE') 
        ],
        'class': 'BtagSF',
        'args': (btagSFSource,'central','deepjet'),
        'samples': mc
    }

    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log( {0} * Jet_btagSF_deepflav_shape[CleanJet_jetIdx] + !{0} * 1 )))'.format('(CleanJet_pt>=20 && abs(CleanJet_eta)<2.5)'),
        'samples': mc
    }

    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log( {0} * Jet_btagSF_deepflav_shape[CleanJet_jetIdx] + !{0} * 1 )))'.format('(CleanJet_pt>=30 && abs(CleanJet_eta)<2.5)'),
        'samples': mc
    }

    aliases['bReq0jSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log( {0} * Jet_btagSF_deepflav_shape[CleanJet_jetIdx] + !{0} * 1 )))'.format('(CleanJet_pt>=20 && CleanJet_pt<30 && abs(CleanJet_eta)<2.5)'),
        'samples': mc
    }

    aliases['btagSF'] = {
        'expr': 'bVetoSF*bVeto + bReqSF*bReq + bReq0jSF*bReq0j + (!bVeto && !bReq && !bReq0j)',
        'samples': mc
    }
    
    for shift in ['jes', 'lf', 'hf', 'lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
        aliases['Jet_btagSF_deepflav_shape_up_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'up_' + shift,'deepjet'),
            'samples': mc
        }
        aliases['Jet_btagSF_deepflav_shape_down_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'down_' + shift,'deepjet'),
            'samples': mc
        }
    
        for targ in ['bVeto', 'bReq', 'bReq0j']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_up_%s' % shift)
    
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_down_%s' % shift)
    
        aliases['btagSF%sup' % shift] = {
            'expr': 'bVetoSF{shift}up*bVeto + bReqSF{shift}up*bReq + bReq0jSF{shift}up*bReq0j + (!bVeto && !bReq && !bReq0j)'.format(shift = shift),
            'samples': mc
        }

        aliases['btagSF%sdown' % shift] = {
            'expr': 'bVetoSF{shift}down*bVeto + bReqSF{shift}down*bReq + bReq0jSF{shift}down*bReq0j + (!bVeto && !bReq && !bReq0j)'.format(shift = shift),
            'samples': mc
        }

# PU jet Id SF
aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}
aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}
aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}

# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l','LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','XSWeight','METFilter_MC','btagSF','Jet_PUIDSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}
aliases['sfweight'] = {
    'expr': ' * '.join(['SFweight2l','sf_nom', 'LepWPCut','XSWeight','METFilter_MC','btagSF','Jet_PUIDSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}
aliases['sfweight_MuUp'] = {
    'expr': 'sf_up',
    'samples': mc
}
aliases['sfweight_MuDo'] = {
    'expr': 'sf_do',
    'samples': mc
}
aliases['sfweight_ge'] = {
    'expr': ' * '.join(['SFweight2l','sf_ge', 'LepWPCut','XSWeight','METFilter_MC','btagSF','Jet_PUIDSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}
aliases['sfweight_res'] = {
    'expr': ' * '.join(['SFweight2l','sf_res', 'LepWPCut','XSWeight','METFilter_MC','btagSF','Jet_PUIDSF']), #bveto_sf*lep_sf*trig_sf*mu_roc_sf
    #'expr': 'LepWPCut',
    'samples': mc
}
# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}

# variable

aliases['L1_PT']={
    'expr':'Sum$((Lepton_pt[0]<=200)*Lepton_pt[0]+(Lepton_pt[0]>200)*Lepton_newpt[0])',
}
aliases['L2_PT']={
    'expr':'Sum$((Lepton_pt[0]<=200)*Lepton_pt[1]+(Lepton_pt[0]>200)*Lepton_newpt[1])',
}
aliases['MET_PT']={
    'expr':'Sum$((Lepton_pt[0]<=200)*MET_pt+(Lepton_pt[0]>200)*new_metpt)',
}
aliases['MLL']={
    'expr':'Sum$((Lepton_pt[0]<=200)*mll+(Lepton_pt[0]>200)*new_mll)',
}

aliases['L1_PT_GE']={
    'expr':'Sum$((Lepton_pt[0]<=200)*Lepton_pt[0]+(Lepton_pt[0]>200)*Lepton_gept[0])',
}
aliases['L1_PT_GE_2']={
    'expr':'(Lepton_pt[0]<=200)*Lepton_pt[0]+(Lepton_pt[0]>200)*Lepton_gept[0]',
}
aliases['L2_PT_GE']={
    'expr':'Sum$((Lepton_pt[0]<=200)*Lepton_pt[1]+(Lepton_pt[0]>200)*Lepton_gept[1])',
}
aliases['MET_PT_GE']={
    'expr':'Sum$((Lepton_pt[0]<=200)*MET_pt+(Lepton_pt[0]>200)*ge_metpt)',
}
aliases['MLL_GE']={
    'expr':'Sum$((Lepton_pt[0]<=200)*mll+(Lepton_pt[0]>200)*ge_mll)',
}

aliases['L1_PT_RES']={
    'expr':'Sum$((Lepton_pt[0]<=200)*Lepton_pt[0]+(Lepton_pt[0]>200)*Lepton_respt[0])',
}
aliases['L2_PT_RES']={
    'expr':'Sum$((Lepton_pt[0]<=200)*Lepton_pt[1]+(Lepton_pt[0]>200)*Lepton_respt[1])',
}
aliases['MET_PT_RES']={
    'expr':'Sum$((Lepton_pt[0]<=200)*MET_pt+(Lepton_pt[0]>200)*res_metpt)',
}
aliases['MLL_RES']={
    'expr':'Sum$((Lepton_pt[0]<=200)*mll+(Lepton_pt[0]>200)*res_mll)',
}

aliases['ht_sum']={'expr':'Sum$((CleanJet_pt>30)*CleanJet_pt)'}
aliases['ht_ratio']={'expr':'ht_sum/L1_PT'}
aliases['met_ht']={'expr':'MET_PT/ht_sum'}
aliases['met_lep1pt']={'expr':'MET_PT/L1_PT'}
aliases['met_lep2pt']={'expr':'MET_PT/L2_PT'}
aliases['zlep1'] = {'expr' : '(Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj'}
aliases['zlep2'] = {'expr' : '(Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj'}
aliases['ht_ratio_ge']={'expr':'ht_sum/L1_PT_GE'}
aliases['met_ht_ge']={'expr':'MET_PT_GE/ht_sum'}
aliases['met_lep1pt_ge']={'expr':'MET_PT_GE/L1_PT_GE'}
aliases['met_lep2pt_ge']={'expr':'MET_PT_GE/L2_PT_GE'}
aliases['ht_ratio_res']={'expr':'ht_sum/L1_PT_RES'}
aliases['met_ht_res']={'expr':'MET_PT_RES/ht_sum'}
aliases['met_lep1pt_res']={'expr':'MET_PT_RES/L1_PT_RES'}
aliases['met_lep2pt_res']={'expr':'MET_PT_RES/L2_PT_RES'}
# selections
aliases['lep0eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[0],-9999))==11 && abs(Alt$(Lepton_eta[0],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[0],-9999))==13 && abs(Alt$(Lepton_eta[0],-9999.)) <2.4))'
}
aliases['lep1eta']={
    'expr': '((abs(Alt$(Lepton_pdgId[1],-9999))==11 && abs(Alt$(Lepton_eta[1],-9999.)) <2.5) || (abs(Alt$(Lepton_pdgId[1],-9999))==13 && abs(Alt$(Lepton_eta[1],-9999.)) <2.4))'
}
aliases['jetpt30']={
	    'expr': 'Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'
}
aliases['jetpt50']={
	    'expr': 'Alt$(CleanJet_pt[0],-9999.) >50 && Alt$(CleanJet_pt[1],-9999.) >50'
}

aliases['zlep_ww']={
    'expr': 'abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75 && abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/detajj) < 0.75'
}
aliases['zveto_ww']={
    'expr': '(abs(Alt$(Lepton_pdgId[0],-9999)) * abs(Alt$(Lepton_pdgId[1],-9999)) != 11*11 || abs(mll - 91.1876) > 15)'
}

# SR definition
aliases['sr_mjj500'] = {
	'expr': 'zlep_ww && mjj > 500 && abs(detajj)>2.5'
}
aliases['sr_mjj750'] = {
	'expr': 'zlep_ww && mjj > 750 && abs(detajj)>2.5'
}
