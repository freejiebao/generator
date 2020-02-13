import ROOT

f1=ROOT.TFile.Open("wmwm_lt.root")
f2=ROOT.TFile.Open("histograms_phantomv2.root")

#samples=['wmwm_ll','wmwm_tl','wmwm_tt','wpwp_ll','wpwp_tl','wpwp_tt']
samples=['wmwm_lt']
samples2=['wmwm_lt']

variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}

ROOT.gStyle.SetOptStat(0)

for isample in range(0,len(samples)):
    for ivar in variables:
        c1 = ROOT.TCanvas("c1", "c1",5,50,500,500)
        c1.SetLogy()
        tl = ROOT.TLegend(0.65,0.78,0.87,0.90)
        h1=f1.Get(ivar+'_'+samples[isample])
        h2=f2.Get(ivar+'_'+samples2[isample])
        norm = h2.Integral()
        h1.Scale(h2.Integral()/h1.Integral())
        #h1.Rebin(2)
        #h2.Rebin(2)
        if h1.GetMaximum() < h2.GetMaximum():
            h1.SetMaximum(h2.GetMaximum()*1.55)
        else:
            h1.SetMaximum(h1.GetMaximum()*1.55)
        h1.SetLineColor(ROOT.kRed)
        h1.GetXaxis().SetTitle(variables[ivar])
        h1.SetTitle('VBS W^{-}W^{-}:'+variables[ivar])
        h1.SetMarkerColor(ROOT.kRed)
        h2.SetLineColor(ROOT.kBlue)
        h2.SetMarkerColor(ROOT.kBlue)
        h1.Draw("")
        h2.Draw("same E")

        tl.AddEntry(h1,'Process B','l')
        tl.AddEntry(h2,'Phantom LT','l')
        tl.Draw('same')
        c1.SaveAs(ivar+'_'+samples[isample]+".eps")
        c1.Close()