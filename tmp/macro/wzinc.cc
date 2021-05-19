#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include <iostream>

class Wzinc : public multidraw::TTreeFunction {
public:
  Wzinc(char const* cat);

  char const* getName() const override { return "Wzinc"; }
  TTreeFunction* clone() const override { return new Wzinc(_category.c_str()); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  std::string _category;
  UIntValueReader* nLepton;
  IntArrayReader* Lepton_pdgId;
  DoubleArrayReader* Lepton_pt;
  FloatArrayReader* Lepton_eta;
  FloatArrayReader* Lepton_phi;
};

Wzinc::Wzinc(char const* cat) :
  TTreeFunction(),
  _category{cat}
{
}

double
Wzinc::evaluate(unsigned)
{
  unsigned nL{*nLepton->Get()};
  if (nL < 3)
    return 0.;

  // more gen lepton selections
  std::vector<unsigned> iPromptL{};
  iPromptL.reserve(nL);

  for (unsigned iL{0}; iL != nL; ++iL) {
    unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId->At(iL)))};
    if (absId != 11 && absId != 13)
      continue;

    iPromptL.push_back(iL);
  }

  if (iPromptL.size() < 3)
    return 0.; // false

  if (iPromptL.size() >= 4 && Lepton_pt->At(iPromptL[3]) >= 10.)
    return 0.;

  for(int i=0; i<3; i++){
      if (!((abs(Lepton_pdgId->At(iPromptL[i])) == 11 && abs(Lepton_eta->At(iPromptL[i])) < 2.4) || (abs(Lepton_pdgId->At(iPromptL[i])) == 13 && abs(Lepton_eta->At(iPromptL[i])) < 2.5))){
        return 0.;
      }
  }

  if ((Lepton_pdgId->At(iPromptL[0])+ Lepton_pdgId->At(iPromptL[1]) != 0)&&(Lepton_pdgId->At(iPromptL[0])+ Lepton_pdgId->At(iPromptL[2]) != 0)&&(Lepton_pdgId->At(iPromptL[1])+ Lepton_pdgId->At(iPromptL[2]) != 0))
    return 0.;

  double lepton_mass0;
  double lepton_mass1;
  double lepton_mass2;

  if (abs(Lepton_pdgId->At(iPromptL[0]))==13){
    lepton_mass0=0.105658;
  }else{
    lepton_mass0=0.000511;
  }

  if (abs(Lepton_pdgId->At(iPromptL[1]))==13){
    lepton_mass1=0.105658;
  }else{
    lepton_mass1=0.000511;
  }

  if (abs(Lepton_pdgId->At(iPromptL[2]))==13){
    lepton_mass2=0.105658;
  }else{
    lepton_mass2=0.000511;
  }

  ROOT::Math::PtEtaPhiMVector pl0(
    Lepton_pt->At(iPromptL[0]),
    Lepton_eta->At(iPromptL[0]),
    Lepton_phi->At(iPromptL[0]),
    lepton_mass0
  );
  ROOT::Math::PtEtaPhiMVector pl1(
    Lepton_pt->At(iPromptL[1]),
    Lepton_eta->At(iPromptL[1]),
    Lepton_phi->At(iPromptL[1]),
    lepton_mass1
  );
  ROOT::Math::PtEtaPhiMVector pl2(
    Lepton_pt->At(iPromptL[2]),
    Lepton_eta->At(iPromptL[2]),
    Lepton_phi->At(iPromptL[2]),
    lepton_mass2
  );
  ROOT::Math::PtEtaPhiMVector plll{pl0 + pl1 + pl2};
  ROOT::Math::PtEtaPhiMVector pl0l1{pl0 + pl1};
  ROOT::Math::PtEtaPhiMVector pl0l2{pl0 + pl2};
  ROOT::Math::PtEtaPhiMVector pl1l2{pl1 + pl2};

  ROOT::Math::PtEtaPhiMVector pl[]={pl0,pl1,pl2};
  int zlepton1_idx=0;
  int zlepton2_idx=1;
  int wlepton_idx=2;
  double zMass_min=-999999;
  for (int i=0; i<2;i++){
    for (int j=i+1; j<3;j++){
        if (Lepton_pdgId->At(iPromptL[i])+Lepton_pdgId->At(iPromptL[j])==0){
            if(abs((pl[i]+pl[j]).M()-91.1876)<abs(zMass_min-91.1876)){
                zMass_min=(pl[i]+pl[j]).M();
                zlepton1_idx=i;
                zlepton2_idx=j;
                wlepton_idx=3-i-j;
            }
        }
    }
  }
  if (!(Lepton_pt->At(iPromptL[zlepton1_idx])>25 && Lepton_pt->At(iPromptL[zlepton2_idx])>10 && Lepton_pt->At(iPromptL[wlepton_idx])>20)){
    return 0;
  }
  if (abs(zMass_min-91.1876)>15){
    return 0;
  }

  if (!((Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1])>0||pl0l1.M()>4) && (Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[2])>0||pl0l2.M()>4) && (Lepton_pdgId->At(iPromptL[1])*Lepton_pdgId->At(iPromptL[2])>0||pl1l2.M()>4)))
    return 0.;

  if (plll.M() <= 100.)
    return 0.;

  return 1.;
}

void
Wzinc::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
    if(_category=="NEWPT"){ // cate: NEWPT, RES, GE
        _library.bindBranch(Lepton_pt, "Lepton_newpt");
    }else if(_category=="RES"){
        _library.bindBranch(Lepton_pt, "Lepton_respt");
    }else if(_category=="GE"){
        _library.bindBranch(Lepton_pt, "Lepton_gept");
    }else{
        _library.bindBranch(Lepton_pt, "Lepton_newpt"); // for Lepton_pt[0]<200, Lepton_newpt is same as Lepton_pt
    }
}
