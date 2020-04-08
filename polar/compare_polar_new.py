import ROOT
import style

ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
style.GoodStyle().cd()

#samples=['wmwm_ll','wmwm_tl','wmwm_tt','wpwp_ll','wpwp_tl','wpwp_tt']
colorful=[ROOT.kMagenta-10,ROOT.kYellow,ROOT.kGreen,ROOT.kCyan]
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
#variables={,'m_mlvlv':'m_{l#nul#nu} [GeV]'}
variables={
    'costheta1':{'name':'cos(#theta_{W_{1}})','rebin':1},
    'costheta2':{'name':'cos(#theta_{W_{2}})','rebin':1},
    'costheta11':{'name':'cos(#theta_{W_{1}})','rebin':1},
    'costheta22':{'name':'cos(#theta_{W_{2}})','rebin':1},
    'm_detajj':{'name':'#Delta#eta_{jj}','rebin':1},
    'm_dphijj':{'name':'#Delta#phi_{jj}','rebin':1},
    'm_met':{'name':'p_{T}^{miss} [GeV]','rebin':1},
    'm_met_2':{'name':'p_{T}^{miss} [GeV]','rebin':1},
    'm_mjj':{'name':'m_{jj} [GeV]','rebin':1},
    'm_mjj_2':{'name':'m_{jj} [GeV]','rebin':1},
    'm_mjj_3':{'name':'m_{jj} [GeV]','rebin':1},
    'm_mll':{'name':'m_{ll} [GeV]','rebin':1},
    'm_mll_2':{'name':'m_{ll} [GeV]','rebin':1},
    'm_mll_3':{'name':'m_{ll} [GeV]','rebin':1},
    'm_mlvlv':{'name':'m_{l#nul#nu}','rebin':1},
    'm_ptj1':{'name':'p_{T}^{j1} [GeV]','rebin':1},
    'm_ptj1_2':{'name':'p_{T}^{j1} [GeV]','rebin':1},
    'm_ptj2':{'name':'p_{T}^{j2} [GeV]','rebin':1},
    'm_ptj2_2':{'name':'p_{T}^{j2} [GeV]','rebin':1},
    'm_ptl1':{'name':'p_{T}^{l1} [GeV]','rebin':1},
    'm_ptl2':{'name':'p_{T}^{l2} [GeV]','rebin':1},
    'm_ptl2_2':{'name':'p_{T}^{l2} [GeV]','rebin':1},
}
#variables={'m_ptl1':'p_{t}^{e} [GeV]'}
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}

params = {
    'polar272':{'name':'polar','samples':['SSWW_TT','SSWW_TL','SSWW_LL'],'scale':[0.9722962041070317,0.9549387370405278,0.953620522749274]},
}

xoffsetstart = 0.0
yoffsetstart = 0.0
xoffset = 0.15
yoffset = 0.05
#xpositions = [0.68,0.68,0.68,0.68,0.4,0.4,0.4,0.4,0.21,0.21,0.21,0.21]
#ypositions = [0,1,2,3,0,1,2,3,0,1,2,3]
xpositions = [0.68,0.68,0.68,0.47,0.47,0.47,0.47,0.21,0.21,0.21,0.21]
ypositions = [0,1,2,0,1,2,3,0,1,2,3]
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

def createCanvasPads():
    c = ROOT.TCanvas("c", "canvas", 400, 400)
    # Upper histogram plot is pad1
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.018)  # joins upper and lower plot
    #pad1.SetGridx()
    pad1.Draw()
    # Lower ratio plot is pad2
    c.cd()  # returns to main canvas before defining pad2
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.08, 1, 0.3)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetBottomMargin(0.3)
    #pad2.SetGridx()
    pad2.Draw()

    return c, pad1, pad2

def createPlot(ivar,i,name,samples,scale):
    c1, pad1, pad2 = createCanvasPads()#c1 = ROOT.TCanvas("c1", "c1",5,50,400,400)
    #c1.SetLogy()
    #f1=ROOT.TFile.Open('eft_samples/eft_SSWW.root')
    f2=ROOT.TFile.Open('polar_samples/polar.root')
    h1=f2.Get(ivar+'_SSWW')
    h1.Sumw2()
    #h1.Scale(0.984729304924904)
    h1.Rebin(variables[ivar]['rebin'])
    hs=ROOT.THStack("hs","")
    htotal=h1.Clone()
    htotal.Scale(0)
    legend_count = 0
    plots=[]
    print(">>>>>>>>>>>> h2:")
    print(ivar+'_SSWW',h1.Integral())
    for idx,isample in enumerate(samples):
        h2=f2.Get(ivar+'_'+isample)
        print(ivar+'_'+isample,h2.Integral())
        h2.Sumw2()
        #h2.Scale(scale[idx])
        #h2.Rebin(variables[ivar]['rebin'])
        h2.SetFillColor(colorful[idx+1])
        h2.SetLineWidth(0)
        hs.Add(h2)
        htotal.Add(h2)
        plots.append(h2)

    if h1.GetMaximum() < htotal.GetMaximum():
        h1.SetMaximum(htotal.GetMaximum()*1.4)
    else:
        h1.SetMaximum(h1.GetMaximum()*1.4)

    h1.SetMinimum(0.001)
    hs.SetMinimum(0.001)
    htotal.SetMinimum(0.001)

    h1.SetMarkerStyle(9)
    h1.SetMarkerSize(0.7)
    h1.SetLineWidth(3)
    h1.SetLineColor(ROOT.kBlack)
    h1.SetTitle('')
    h1.GetXaxis().SetLabelSize(0)
    #h1.SetFillColor(colorful[0])
    pad1.cd()
    h1.Draw()
    #htotal.SetLineColor(ROOT.kRed)
    #htotal.SetLineWidth(2)
    #htotal.SetTitle('')
    #htotal.GetXaxis().SetLabelSize(0.0)
    #htotal.GetXaxis().SetTitle(variables[ivar]['name'])
    #htotal.GetYaxis().SetTitle('Events')
    #htotal.GetYaxis().SetTitleSize(0.05)
    #htotal.Draw('HIST ][')
    hs.Draw("hist SAME")

    legend_count=0
    plot_name={'SSWW_LL':'EWK W^{#pm}_{L}W^{#pm}_{L}','SSWW_TL':'EWK W^{#pm}_{T}W^{#pm}_{L}','SSWW_TT':'EWK W^{#pm}_{T}W^{#pm}_{T}'}
    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h1,'EWK W^{#pm}W^{#pm}:'+'{0}'.format(int(h1.Integral())),"lp")
    for idx,iplot in enumerate(plots):
        legend_count+=1
        draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,iplot,plot_name[samples[idx]]+':{0}'.format(int(iplot.Integral())),"f")

    gstat = ROOT.TGraphAsymmErrors(htotal)

    for j in range(0,gstat.GetN()):
        gstat.SetPointEYlow (j, htotal.GetBinError(j+1))
        gstat.SetPointEYhigh(j, htotal.GetBinError(j+1))

    gstat.SetFillColor(ROOT.kGray+2)
    gstat.SetFillStyle(3345)
    ROOT.gStyle.SetHatchesSpacing(0.5)
    ROOT.gStyle.SetHatchesLineWidth(1)
    gstat.SetMarkerSize(0)
    gstat.SetLineWidth(2)
    gstat.SetLineColor(0)
    gstat.Draw("E2same")

    #htotal.Draw("HIST SAME ][")
    legend_count+=1
    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,gstat,'stat.',"f")
    
    h1.Draw("SAME E")

    
    r_central=htotal.Clone()
    r_central.Divide(htotal)
    r_combine=h1.Clone()
    r_combine.Divide(htotal)
    r_combine.SetTitle('')

    r_central.SetMaximum(1.49)
    r_central.SetMinimum(0.51)
    r_central.SetTitle('')
    y = r_central.GetYaxis()
    y.SetNdivisions(505)
    y.SetTitle("SM/EFT")
    y.SetTitleSize(10)
    y.SetTitleFont(43)
    y.SetTitleOffset(1.55)
    y.SetLabelFont(43)
    y.SetLabelSize(8.5)
    x = r_central.GetXaxis()
    x.SetTitleSize(10)
    x.SetTitleFont(43)
    x.SetTitleOffset(4.0)
    x.SetLabelFont(43)
    x.SetLabelSize(8.5)

    pad2.cd()
    r_combine.SetMarkerStyle(0)
    r_central.SetFillColor(ROOT.kGray)
    r_central.SetMarkerSize(0)
    r_central.Draw('E2')

    l1=ROOT.TLine(x.GetXmin(),1.0,x.GetXmax(),1.0)
    l1.SetLineColor(ROOT.kRed)
    l1.SetLineStyle(1)
    l1.SetLineWidth(2)
    l1.Draw('SAME')
    r_combine.SetMarkerStyle(9)
    r_combine.SetMarkerSize(0.7)
    r_combine.SetLineWidth(3)
    r_combine.SetLineColor(ROOT.kBlack)
    r_combine.Draw('SAME X0E')

    c1.SaveAs('polar_plots/'+ivar+'_'+i+'.pdf')
    c1.Close()
    #f1.Close()
    f2.Close()

for ivar in variables:
    for i in params:
        createPlot(ivar,i,params[i]['name'],params[i]['samples'],params[i]['scale'])
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