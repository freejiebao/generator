# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>1 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 &&\
    abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 &&\
    tauVeto_ww && zveto_ww && lep0eta && lep1eta &&\
    abs(Alt$(Lepton_pdgId[0],9999))==13 && abs(Alt$(Lepton_pdgId[1],9999))==13'

## Signal regions
# sr_mjj750: 'zlep_ww && mjj > 750 && abs(detajj)>2.5 && mll>20'
cuts['SR'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20'
cuts['SR_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20 && dphill>2'
cuts['SR_met100_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20 && MET_PT<100 && dphill>2'
cuts['SR_met50'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20 && MET_PT<50'
