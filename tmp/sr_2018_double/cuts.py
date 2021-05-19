# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>1 && nCleanJet >1 && Alt$(Lepton_pt[2],0.)<10 &&\
    abs(Alt$(CleanJet_eta[0],-9999.)) < 4.7&& abs(Alt$(CleanJet_eta[1],-9999.)) < 4.7 &&\
    tauVeto_ww && zveto_ww && lep0eta && lep1eta &&\
    abs(Alt$(Lepton_pdgId[0],9999))==13 && abs(Alt$(Lepton_pdgId[1],9999))==13'

## Signal regions
cuts['ori'] = 'bVeto && sr_mjj750 && jetpt30 && Lepton_pt[0]>30 && Lepton_pt[1]>30 && mll>20'
# sr_mjj750: 'zlep_ww && mjj > 750 && abs(detajj)>2.5 && mll>20'
#cuts['SR'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20'
#cuts['SR_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20 && dphill>2'
#cuts['SR_met100_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20 && MET_PT<100 && dphill>2'
#cuts['SR_met50'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT>30 && L2_PT>30 && MLL>20 && MET_PT<50'
# ge
#cuts['ge_SR'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_GE>30 && L2_PT_GE>30 && MLL_GE>20'
#cuts['ge_SR_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_GE>30 && L2_PT_GE>30 && MLL_GE>20 && dphill>2'
#cuts['ge_SR_met100_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_GE>30 && L2_PT_GE>30 && MLL_GE>20 && MET_PT_GE<100 && dphill>2'
#cuts['ge_SR_met50'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_GE>30 && L2_PT_GE>30 && MLL_GE>20 && MET_PT_GE<50'
# res
#cuts['res_SR'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_RES>30 && L2_PT_RES>30 && MLL_RES>20'
#cuts['res_SR_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_RES>30 && L2_PT_RES>30 && MLL_RES>20 && dphill>2'
#cuts['res_met100_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_RES>30 && L2_PT_RES>30 && MLL_RES>20 && MET_PT_RES<100 && dphill>2'
#cuts['res_met50'] = 'bVeto && sr_mjj750 && jetpt30 && L1_PT_RES>30 && L2_PT_RES>30 && MLL_RES>20 && MET_PT_RES<50'
#cuts['SR_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && leppt30_30 && dphill>2'

#cuts['SR_met50'] = 'bVeto && sr_mjj750 && jetpt30 && leppt30_30 && MET_pt<50'
#cuts['SR_met100_dphill'] = 'bVeto && sr_mjj750 && jetpt30 && leppt30_30 && MET_pt<100 '
