import ROOT
import style

ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
style.GoodStyle().cd()

xoffsetstart = 0.0
yoffsetstart = 0.0
xoffset = 0.20
yoffset = 0.05
#xpositions = [0.68,0.68,0.68,0.68,0.4,0.4,0.4,0.4,0.21,0.21,0.21,0.21]
#ypositions = [0,1,2,3,0,1,2,3,0,1,2,3]
xpositions = [0.68,0.68,0.47,0.47,0.47,0.47,0.21,0.21,0.21,0.21]
ypositions = [0,1,0,1,2,3,0,1,2,3]
def draw_legend(x1,y1,hist,label,options):

    legend = ROOT.TLegend(x1+xoffsetstart,y1+yoffsetstart,x1+xoffsetstart + xoffset,y1+yoffsetstart + yoffset)

    legend.SetBorderSize(     0)
    legend.SetFillColor (     0)
    legend.SetTextAlign (    12)
    legend.SetTextFont  (    42)
    legend.SetTextSize  ( 0.040)

    legend.AddEntry(hist,label,options)

    legend.Draw("same")

    #otherwise the legend goes out of scope and is deleted once the function finishes
    hist.label = legend


f1=ROOT.TFile.Open("mg_total.root")
f2=ROOT.TFile.Open("mg_total.root")

#samples=['wmwm_ll','wmwm_tl','wmwm_tt','wpwp_ll','wpwp_tl','wpwp_tt']
samples=['SSWW']
samples2=['TT','LT','TL','LL']
colorful=[ROOT.kMagenta-10,ROOT.kYellow,ROOT.kGreen,ROOT.kCyan]
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
variables={'costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})'}
#variables2={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
#variables={'m_ptl1':'p_{t}^{e} [GeV]'}

for ivar in variables:
    c1 = ROOT.TCanvas("c1", "c1",5,50,500,500)
    #c1.SetLogy()
    h1=f1.Get(ivar+'_'+samples[0])
    norm=h1.Integral()
    h1.Rebin(2)
    legend_count = 0
    plots=[]
    for idx,isample in enumerate(samples2):
        h2=f2.Get(ivar+'_'+isample)
        h2.Rebin(2)
        h2.SetLineColor(colorful[idx])
        h2.SetMarkerColor(colorful[idx])
        h2.SetLineWidth(2)
        h2.Scale(norm/h2.Integral())
        h2.SetMinimum(0)
        if h1.GetMaximum() < h2.GetMaximum():
            h1.SetMaximum(h2.GetMaximum()*1.15)
        else:
            h1.SetMaximum(h1.GetMaximum()*1.15)
        plots.append(h2)

    h1.SetMinimum(0)

    #h1.SetMarkerStyle(ROOT.kFullCircle)
    h1.SetLineWidth(2)
    h1.SetLineColor(0)
    h1.SetTitle("")
    h1.Draw("hist")

    legend_count=-1
    #draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h1,"EWK W^{#pm}W^{#pm}","lp")
    for idx,iplot in enumerate(plots):
        legend_count+=1
        draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,iplot,samples2[idx],"l")
        iplot.Draw("same hist")
    #h1.Draw("same")
    c1.SaveAs(ivar+'_'+isample+"_shape.pdf")
    c1.Close()

'''
for isample in range(0,len(samples)):
    for ivar in variables:
        c1 = ROOT.TCanvas("c1", "c1",5,50,500,500)
        c1.SetLogy()
        tl = ROOT.TLegend(0.65,0.78,0.87,0.87)
        h1=f1.Get(ivar+'_'+samples[isample])
        h2=f2.Get(ivar+'_'+samples2[isample])
        #h1=f1.Get('m_ptl1_'+samples[isample])
        #h2=f2.Get('m_ptl2_'+samples2[isample])
        norm = h2.Integral()
        #h1.Scale(h2.Integral()/h1.Integral())
        #h1.Rebin(2)
        #h2.Rebin(2)
        if h1.GetMaximum() < h2.GetMaximum():
            h1.SetMaximum(h2.GetMaximum()*1.2)
        else:
            h1.SetMaximum(h1.GetMaximum()*1.2)
        h1.SetLineColor(ROOT.kRed)
        h1.SetMarkerColor(ROOT.kRed)
        h1.GetXaxis().SetTitle('p_{T} [GeV]')#variables[ivar]
        h1.SetTitle('VBS W^{-}W^{-}: pt')#+variables[ivar]
        h2.SetLineColor(ROOT.kBlue)
        h2.SetMarkerColor(ROOT.kBlue)
        h1.Draw("")
        h2.Draw("same E")

        tl.AddEntry(h1,'electron','l')
        tl.AddEntry(h2,'muon','l')
        tl.Draw('same')
        c1.SaveAs(ivar+'_'+samples[isample]+".pdf")
        c1.Close()
'''
