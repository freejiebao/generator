# plot configuration

# groupPlot = {}
#
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

# groupPlot = {}
#
# Groups of samples to improve the plots (merge different sample during plot).
# If not defined, normal plots is used
#
Red=632; Violet=880; Green=416; Orange=800; Yellow=400; Azure=860
#groupPlot['ZZ']  = dict(nameHR="ZZ", isSignal=0, color=ROOT.kBlue-10, samples=['ZZ4L','ggZZ'])
#groupPlot['VVV']  = dict(nameHR='VVV', isSignal=0, color=ROOT.kBlue-9, samples=['VVV'])
#groupPlot['TTV']  = dict(nameHR='TVX', isSignal=0, color=ROOT.kBlue-7, samples=['ttV','tZq'])
#groupPlot['Vg']  = dict(nameHR="V#gamma", isSignal=0, color=ROOT.kCyan+2, samples=['Vg', 'VgS1_H'])#,'VgS1_L'])
#groupPlot['non-prompt']  = dict(nameHR='Non-prompt', isSignal=0, color=ROOT.kCyan, samples=['Fake'])
#groupPlot['WZ_QCD']  = dict(nameHR="WZ QCD", isSignal=0, color=ROOT.kGreen, samples=['WZ_QCD_powheg'])
#groupPlot['WZ_EWK']  = dict(nameHR="WZ EWK", isSignal=0, color=ROOT.kYellow, samples=['WZ_EWK'])
#groupPlot['DPS']  = dict(nameHR='DPS', isSignal=0, color=ROOT.kYellow-9, samples=['DPS'])
#groupPlot['WpWp_QCD']  = dict(nameHR="QCD W^{#pm}W^{#pm}", isSignal=0, color=ROOT.kOrange+0, samples=['WpWp_QCD'])
#groupPlot['SSWW_EW']  = dict(nameHR='EW W^{#pm}W^{#pm}', isSignal=0, color=ROOT.kMagenta, samples=['SSWW_EW'])

groupPlot['SSWW_EWK']  = dict(nameHR='EW W^{#pm}W^{#pm}', isSignal=0, color=ROOT.kMagenta-10, samples=['SSWW_EW'])
#groupPlot['SSWW_QCD']  = dict(nameHR='QCD W^{#pm}W^{#pm}', isSignal=0, color=ROOT.kMagenta, samples=['WpWp_QCD'])
#groupPlot['chargeflip']  = dict(nameHR="Wrong sign", isSignal=0, color=ROOT.kOrange, samples=['WW','ggWW','DY','top','higgs'])
groupPlot['WZ_QCD']  = dict(nameHR="W^{#pm}Z", isSignal=0, color=ROOT.kYellow, samples=['WZ_QCD_powheg','WZ_EWK'])
#groupPlot['WZ_EWK']  = dict(nameHR="EW W^{#pm}Z", isSignal=0, color=ROOT.kOrange, samples=['WZ_EWK'])
groupPlot['non-prompt']  = dict(nameHR='Non-prompt', isSignal=0, color=ROOT.kCyan, samples=['Fake'])
groupPlot['others']  = dict(nameHR='Other bkgs.', isSignal=0, color=ROOT.kBlue-10, samples=['ZZ4L','ggZZ','VVV','ttV','tZq','Vg', 'VgS_H','VgS_L','DPS','WpWp_QCD'])
groupPlot['hmn_m750']  = dict(nameHR="m_{N}=750GeV", isSignal=2, color=ROOT.kRed+0, samples=['hmn_m750'])
groupPlot['hmn_m1500']  = dict(nameHR="m_{N}=1500GeV", isSignal=2, color=ROOT.kRed+1, samples=['hmn_m1500'])
groupPlot['hmn_m5000']  = dict(nameHR="m_{N}=5000GeV", isSignal=2, color=ROOT.kRed+2, samples=['hmn_m5000'])
groupPlot['sswwjj_dim5']  = dict(nameHR="Dim5#times1000", isSignal=2, color=ROOT.kGreen, samples=['sswwjj_dim5'])
#plot = {}

# keys here must match keys in samples.py
##Fake and prompt substraction
plot['Fake']  = dict(color=Yellow, isSignal=0, isData=0, scale=1.0)
##Signal
plot['SSWW_EW']  = dict(color=Azure + 4, isSignal=0, isData=0, scale=1.0) # WpWpJJ_EWK_powheg WpWp_EWK
plot['hmn_m750']   = dict(color=ROOT.kRed+0, isSignal=2, isData=0, scale=1.0)
plot['hmn_m1500']  = dict(color=ROOT.kRed+1, isSignal=2, isData=0, scale=1.0)
plot['hmn_m5000']  = dict(color=ROOT.kRed+2, isSignal=2, isData=0, scale=1.0)
plot['sswwjj_dim5']  = dict(color=ROOT.kGreen, isSignal=2, isData=0, scale=1000.0)
plot['WpWp_QCD']  = dict(color=Violet, isSignal=0, isData=0, scale=1.0)
#plot['WpWpJJ_QCD']  = dict(color=Violet, isSignal=0, isData=0, scale=1.0)
plot['Vg']  = dict(color=Orange + 10, isSignal=0, isData=0, scale=1.0)
plot['VgS_H']  = dict(color=Orange + 10, isSignal=0, isData=0, scale=1.0) # VgS VgS1 VgS2
plot['VgS_L']  = dict(color=Orange + 10, isSignal=0, isData=0, scale=1.0) # VgS VgS1 VgS2
##Reducible Background
##VV plot
plot['ZZ4L']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
plot['ggZZ']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
plot['WZ_QCD_powheg']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0) # WZ_QCD WZ_QCD_powheg WZ_QCD_AMCNLO
plot['WZ_EWK']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
plot['DPS']  = dict(color=Violet + 10, isSignal=0, isData=0, scale=1.0)
##VVV
plot['VVV']  = dict(color=Green, isSignal=0, isData=0, scale=1.0)
plot['ttV']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
plot['tZq']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
#wrong-sign
plot['WW']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
plot['ggWW']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
plot['top']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
plot['DY']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
plot['higgs']  = dict(color=Green + 10, isSignal=0, isData=0, scale=1.0)
##Data
plot['DATA']  = dict(nameHR='Data', color=1, isSignal=0, isData=1, isBlind=1,scale=1.0)

# additional options
legend['lumi'] = 'L = 59.74/fb'
#legend['lumi'] = 'L = 137.19/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'