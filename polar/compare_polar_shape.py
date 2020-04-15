import ROOT
import style

ROOT.TH1.SetDefaultSumw2()
ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(ROOT.kTRUE)
style.GoodStyle().cd()

#samples=['wmwm_ll','wmwm_tl','wmwm_tt','wpwp_ll','wpwp_tl','wpwp_tt']
colorful=[ROOT.kRed,ROOT.kBlue,ROOT.kGreen,ROOT.kCyan]
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
#variables={,'m_mlvlv':'m_{l#nul#nu} [GeV]'}
variables={
    'zepp1':{'name':'Z^{*}_{l1}','rebin':1},
    'zepp2':{'name':'Z^{*}_{l2}','rebin':1},
    'costheta1':{'name':'cos(#theta_{W_{1}})','rebin':1},
    'costheta2':{'name':'cos(#theta_{W_{2}})','rebin':1},
    'costheta11':{'name':'cos(#theta_{W_{1}})','rebin':1},
    'costheta22':{'name':'cos(#theta_{W_{2}})','rebin':1},
    'costheta13':{'name':'cos(#theta_{l1,W2})','rebin':1},
    'costheta23':{'name':'cos(#theta_{l2,W1})','rebin':1},
    'm_detajj':{'name':'#Delta#eta_{jj}','rebin':1},
    'm_dphijj':{'name':'#Delta#phi_{jj}','rebin':1},
    'm_dphijj_2':{'name':'#Delta#phi_{jj}','rebin':1},
    'm_dphill':{'name':'#Delta#phi_{ll}','rebin':1},
    'm_dphill_2':{'name':'#Delta#phi_{ll}','rebin':1},
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
    'etaj1':{'name':'#eta_{j1}','rebin':1},
    'etaj2':{'name':'#eta_{j2}','rebin':1},
    'etal1':{'name':'#eta_{l1}','rebin':1},
    'etal2':{'name':'#eta_{l2}','rebin':1},
    'no_shape':{'name':'count','rebin':1},
}
#variables={'m_ptl1':'p_{t}^{e} [GeV]'}
#variables={'costheta11':'cos(#theta_{e})','costheta22':'cos(#theta_{#mu})','costheta1':'cos(#theta_{e})','costheta2':'cos(#theta_{#mu})','m_detajj':'#Delta#eta_{jj}','m_met':'p_{t}^{miss} [GeV]','m_mjj':'m_{jj} [GeV]','m_mll':'m_{ll} [GeV]','m_mlvlv':'m_{l#nul#nu} [GeV]','m_ptj1':'p_{t}^{j1} [GeV]','m_ptj2':'p_{t}^{j2} [GeV]','m_ptl1':'p_{t}^{e} [GeV]','m_ptl2':'p_{t}^{#mu} [GeV]'}
frame='_dijet_rf'
subdir='dijet_rf'
params = {
    'polar272':{'name':'polar','samples':['VBS_SSWW_TT'+frame,'VBS_SSWW_TL'+frame,'VBS_SSWW_LL'+frame],'scale':[0.9722962041070317,0.9549387370405278,0.953620522749274]},
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

def createPlot(ivar,i,name,samples,scale):
    c1 = ROOT.TCanvas("c1", "c1",5,50,500,500)
    #c1.SetLogy()
    f2=ROOT.TFile.Open('polar.root')
    #h1=f2.Get(ivar+'_SSWW')
    #h1.Sumw2()
    #norm=h1.Integral()
    #h1.Rebin(variables[ivar]['rebin'])

    h2=f2.Get(ivar+'_VBS_SSWW_LL'+frame)
    print(ivar+'_VBS_SSWW_LL'+frame,h2.Integral())
    h2.Sumw2()
    h2.Scale(1/h2.Integral())
    #h2.Rebin(variables[ivar]['rebin'])
    h2.SetLineColor(colorful[0])
    h2.SetMarkerColor(colorful[0])
    h2.SetLineWidth(2)


    h3=f2.Get(ivar+'_VBS_SSWW_TL'+frame)
    h4=f2.Get(ivar+'_VBS_SSWW_TT'+frame)
    h3.Add(h4)
    h3.Scale(1/h3.Integral())
    #h3.Rebin(variables[ivar]['rebin'])
    h3.SetLineColor(colorful[1])
    h3.SetMarkerColor(colorful[1])
    h3.SetLineWidth(2)
    
    if h2.GetMaximum()<h3.GetMaximum():
        h2.SetMaximum(h3.GetMaximum()*1.4)
    else:
        h2.SetMaximum(h2.GetMaximum()*1.4)


    plot_name={'VBS_SSWW_LL'+frame:'EWK W^{#pm}_{L}W^{#pm}_{L}','VBS_SSWW_TL'+frame:'EWK W^{#pm}_{T}W^{#pm}_{X}','VBS_SSWW_TT'+frame:'EWK W^{#pm}_{T}W^{#pm}_{T}'}
    legend_count=0

    h2.SetMinimum(0)
    h2.SetTitle("")
    h2.GetYaxis().SetTitle("A.U.")
    h2.Draw()
    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h2,plot_name['VBS_SSWW_LL'+frame],"l")

    legend_count+=1

    draw_legend(xpositions[legend_count],0.84 - ypositions[legend_count]*yoffset,h3,plot_name['VBS_SSWW_TL'+frame],"l")
    h3.Draw("same e")
    
    c1.SaveAs('polar_plots/'+subdir+'/'+ivar+'_'+i+frame+'_shape.pdf')
    c1.Close()
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
