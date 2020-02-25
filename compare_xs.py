import ROOT
from array import array

def change(bins,i):
    width=[-0.1,0,0.1]
    xbin=[]
    #print(len(bins))
    for j in range(0,len(bins)):
        #print(bins[j],bins[j+1])
        xbin.append(bins[j]+width[i])
    print(xbin)
    return array('f',xbin)
#without cr

variables = {
    'cross_section':{
        'xbin':array('f',[1, 2, 3, 4]),
        'ex':array('f',[0, 0, 0, 0]),
        'xs_0':array('f',[0.0068,0.0085,0.00898,0.01542]), # cross section for central
        'xs_0_up':array('f',[0.005023,0.0056454,0.002019,0.006811]), # error up 
        'xs_0_down':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error down, here up and down are same
        'xs_1':array('f',[0.0068,0.0085,0.00898,0.01542]), # cross section for cw 0.1 chw 1
        'xs_1_up':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error up
        'xs_1_down':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error down
        'xs_2':array('f',[0.0068,0.0085,0.00898,0.01542]), # cross section for cw 1 chw 0.1
        'xs_2_up':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error up
        'xs_2_down':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error up
        'xs_3':array('f',[0.0068,0.0085,0.00898,0.01542]), # cross section for cw 1 chw 1
        'xs_3_up':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error up
        'xs_3_down':array('f',[0.0005023,0.00056454,0.0002019,0.00006811]), # error up
    },
}
gr=[0,0,0]
reweight_point=['Central','C_{W}=0.1, C_{HW}=1','C_{W}=1, C_{HW}=0.1','C_{W}=1, C_{HW}=1']
#change(variables[ivar]['xbin'],0)
for ivar in variables:
    gr[0]=ROOT.TGraphAsymmErrors(4,change(variables[ivar]['xbin'],0),variables[ivar]['xs_0'],variables[ivar]['ex'],variables[ivar]['ex'],variables[ivar]['xs_0_up'],variables[ivar]['xs_0_down'])
    gr[1]=ROOT.TGraphAsymmErrors(4,change(variables[ivar]['xbin'],1),variables[ivar]['xs_1'],variables[ivar]['ex'],variables[ivar]['ex'],variables[ivar]['xs_1_up'],variables[ivar]['xs_2_down'])
    gr[2]=ROOT.TGraphAsymmErrors(4,change(variables[ivar]['xbin'],2),variables[ivar]['xs_2'],variables[ivar]['ex'],variables[ivar]['ex'],variables[ivar]['xs_2_up'],variables[ivar]['xs_2_down'])
c1 = ROOT.TCanvas("c1","A Simple Graph Example",200,10,500,300)
c1.cd()
c1.SetGridx()
c1.SetLogy()
ROOT.gStyle.SetOptStat(0)

h=ROOT.TH1F("h","",4,0.5,4.5);
h.SetTitle("");
h.GetYaxis().SetTitleOffset(1);
h.GetXaxis().SetTitleOffset(1.);
h.GetYaxis().SetTitle("cross section [pb]")
h.GetXaxis().SetTitle("reweight");
h.GetXaxis().SetNdivisions(-10);
h.SetMaximum(0.1);
h.SetMinimum(0.);
for i in range(0,4):
    h.GetXaxis().SetBinLabel(i+1,reweight_point[i]);
h.Draw("")

gr[0].SetLineColor(ROOT.kBlue)
gr[0].SetMarkerColor(ROOT.kBlue)
gr[0].SetMarkerStyle(20)
#gr[0].GetHistogram().SetMinimum(-1.)
#for i in range(0,4):
#    gr[0].GetXaxis().SetBinLabel(i+1,reweight_point[i]);
gr[0].Draw("PE")

gr[1].SetLineColor(ROOT.kRed)
gr[1].SetMarkerColor(ROOT.kRed)
gr[1].SetMarkerStyle(20)
gr[1].Draw("PE")

gr[2].SetLineColor(ROOT.kGreen)
gr[2].SetMarkerColor(ROOT.kGreen)
gr[2].SetMarkerStyle(20)
gr[2].Draw("PE")


start_point=['C_{W}=0.1, C_{HW}=1','C_{W}=1, C_{HW}=0.1','C_{W}=1, C_{HW}=1']
leg1 = ROOT.TLegend(0.15, 0.83, 0.25, 0.90)
leg1.AddEntry(gr[0], start_point[0])
leg2 = ROOT.TLegend(0.30, 0.83, 0.40, 0.90)
leg2.AddEntry(gr[1], start_point[1])
leg3 = ROOT.TLegend(0.45, 0.83, 0.55, 0.90)
leg3.AddEntry(gr[2], start_point[2])
leg1.SetFillStyle(0)
leg1.SetLineWidth(0)
leg2.SetFillStyle(0)
leg2.SetLineWidth(0)
leg3.SetFillStyle(0)
leg3.SetLineWidth(0)
leg1.Draw('SAME')
leg2.Draw('SAME')
leg3.Draw('SAME')

c1.SaveAs("xs_compare.pdf")