// ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonLegacy2016#RECO_efficiency_AN1
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "GEScaleSyst/GEScaleSyst.h"

#include <vector>

#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4D.h"

#include <iostream>

class Mu_GE : public multidraw::TTreeFunction {
public:
    Mu_GE(char const* yr,char const* var, int nl, int il);

    char const* getName() const override {
        return "Mu_GE";
    }
    TTreeFunction* clone() const override {
        return new Mu_GE(_year.c_str(),_variation.c_str(),_nlep,_ilep);
    }

    unsigned getNdata() override {
        return 1;
    }
    double evaluate(unsigned) override;

protected:
    void bindTree_(multidraw::FunctionLibrary&) override;

    UIntValueReader*  nLepton;
    IntArrayReader*   Lepton_pdgId;
    FloatArrayReader* Lepton_pt;
    FloatArrayReader* Lepton_eta;
    FloatArrayReader* Lepton_phi;
    FloatArrayReader* Lepton_rochesterSF;
    FloatValueReader* mll;
    FloatValueReader* MET_pt;
    FloatValueReader* MET_phi;
    std::string _year{};
    std::string _variation{};
    int _nlep;
    int _ilep;
    //UIntValueReader* nGenJet;
    //FloatArrayReader* GenJet_pt;
    //FloatArrayReader* GenJet_eta;
    //FloatArrayReader* GenJet_phi;
    //FloatArrayReader* GenJet_mass;

    //FloatValueReader* GenMET_pt;
    //FloatValueReader* GenMET_phi;
};

Mu_GE::Mu_GE(char const* yr,char const* var,int nl):
    TTreeFunction(),
    _year{yr},
    _variation{var},
    _nlep{nl},
    _ilep{il}{
}

double
Mu_GE::evaluate(unsigned) {
    unsigned nL{*nLepton->Get()};
    if (nL < _ilep+1)
        return -999.;
    if (std::abs(Lepton_pdgId->At(_ilep))!=13)
        return -999.;

    float pf_pt=Lepton_pt->At(_ilep);
    if (pf_pt<=200)
        return pf_pt;
    pf_pt/=(Lepton_rochesterSF->At(_ilep));

    float pf_phi=Lepton_phi->At(_ilep);
    float clip_phi;
    if (pf_phi>M_PI){
        clip_phi = 2*M_PI/3.0; // phi bin edge: https://github.com/khaosmos93/GEScaleSyst/blob/08603f5ac727b3f4e50bb4d801c9fc3991a6230b/GEScaleSyst.h#L32
    }else if(pf_phi < -M_PI){
        clip_phi = -2*M_PI/3.0;
    }

    float pf_eta=Lepton_eta->At(_ilep);


    GEScaleSyst GE=GEScaleSyst();
    GE.SetVerbose(0);
    int start=161000;
    int ncopy=5;
    if(_year=="2017"){
        start=171000;
    }else{
        start=181000;
    }
    float sum_pt=0;
    for(int i=start; i<start+ncopy;i++){
        sum_pt += GE.GEScaleCorrPt( i, pf_pt, pf_eta, clip_phi, Lepton_pdgId->At(_ilep)>0 ? 1:-1 );
    }
    float ge_pt=sum_pt/ncopy;
    return ge_pt;
}

void Mu_GE::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(Lepton_rochesterSF, "Lepton_rochesterSF");
    _library.bindBranch(mll, "mll");
    _library.bindBranch(MET_pt, "MET_pt");
    _library.bindBranch(MET_phi, "MET_phi");
}