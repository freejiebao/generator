// ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonLegacy2016#RECO_efficiency_AN1
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"

#include <vector>

#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4D.h"

#include <iostream>

class Mu_IDsf : public multidraw::TTreeFunction {
public:
    Mu_IDsf(char const* yr,char const* var, int nl);

    char const* getName() const override {
        return "Mu_IDsf";
    }
    TTreeFunction* clone() const override {
        return new Mu_IDsf(_year.c_str(),_variation.c_str(), _nlep);
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
    std::string _year{};
    std::string _variation{};
    int _nlep;
    //UIntValueReader* nGenJet;
    //FloatArrayReader* GenJet_pt;
    //FloatArrayReader* GenJet_eta;
    //FloatArrayReader* GenJet_phi;
    //FloatArrayReader* GenJet_mass;

    //FloatValueReader* GenMET_pt;
    //FloatValueReader* GenMET_phi;
};

Mu_IDsf::Mu_IDsf(char const* yr,char const* var,int nl):
    TTreeFunction(),
    _year{yr},
    _variation{var},
    _nlep{nl}{
}

double
Mu_IDsf::evaluate(unsigned) {
    unsigned nL{*nLepton->Get()};
    if (nL < _nlep)
        return 0.;

    // more lepton selections
    std::vector<unsigned> iPromptL{};
    iPromptL.reserve(nL);

    for (unsigned iL{0}; iL != nL; ++iL) {
        unsigned absId{static_cast<unsigned>(std::abs(Lepton_pdgId->At(iL)))};
        if (absId != 13)
            continue;
        iPromptL.push_back(iL);
    }

    if (iPromptL.size() < _nlep)
        return 0.;  // false
    //if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1])!=-11*11)
    //  return 0.;
    // 2016 data
    std::vector<double> sfs_eta0={0.990348,0.990814,0.990373,0.976850};
    std::vector<double> err_eta0={0.000863,0.002369,0.005770,0.040663};
    std::vector<double> sfs_eta1={0.991816,0.994132,0.966091};
    std::vector<double> err_eta1={0.001506,0.004047,0.010599};
    std::vector<double> sfs_eta2={0.992013,0.991341,0.991225,1.017846};
    std::vector<double> err_eta2={0.000787,0.002590,0.006790,0.061889};
    if(_year=="2017"){
        sfs_eta0={0.990348,0.990814,0.990373,0.976850};
        err_eta0={0.000863,0.002369,0.005770,0.040663};
        sfs_eta1={0.991816,0.994132,0.966091};
        err_eta1={0.001506,0.004047,0.010599};
        sfs_eta2={0.992013,0.991341,0.991225,1.017846};
        err_eta2={0.000787,0.002590,0.006790,0.061889};
    }
    else if (_year=="2018"){
        sfs_eta0={0.990348,0.990814,0.990373,0.976850};
        err_eta0={0.000863,0.002369,0.005770,0.040663};
        sfs_eta1={0.991816,0.994132,0.966091};
        err_eta1={0.001506,0.004047,0.010599};
        sfs_eta2={0.992013,0.991341,0.991225,1.017846};
        err_eta2={0.000787,0.002590,0.006790,0.061889};
    }
    std::vector<double> pt(_nlep,0);
    std::vector<double> abseta(_nlep,0);
    for (int i=0; i<_nlep;i++){
        pt[i]=Lepton_pt->At(iPromptL[i]);
        abseta[i]=abs(Lepton_eta->At(iPromptL[i]));
    }
    std::vector<int> idx(_nlep,0);
    for (int i=0; i<_nlep;i++){
        if (abseta[i]>=0.9 && abseta[i]<1.2){
            if (pt[i] < 200) {//only consider momentum > 200 muons
                idx[1] = -1;
            }
            else{
                idx[1] = 2;
            }
        }else{
            if (pt[i] < 200) {//only consider momentum > 200 muons
                idx[1] = -1;
            }
            else if (pt[i] >= 200 && pt[i] < 450) {
                idx[1] = 2;
            }
            else{
                idx[1] = 3;
            }
        }
    }

    //double _sf1=sf[idx1];
    //double _sf2=sf[idx2];
    std::vector<double> _rate(_nlep,1);
    for (int i=0; i<_nlep; i++){
        if (idx[i]>=0){
            if (_variation=="nom"){
                if (abseta[i]<0.9){
                    _rate[i]=sfs_eta0[idx[i]];
                }else if (abseta[i]>=0.9 && abseta[i]<1.2){
                    _rate[i]=sfs_eta1[idx[i]];
                }else{
                    _rate[i]=sfs_eta2[idx[i]];
                }
            }else if (_variation=="up"){
                if (abseta[i]<0.9){
                    _rate[i]=sfs_eta0[idx[i]]+err_eta0[idx[i]];
                }else if (abseta[i]>=0.9 && abseta[i]<1.2){
                    _rate[i]=sfs_eta1[idx[i]]+err_eta1[idx[i]];
                }else{
                    _rate[i]=sfs_eta2[idx[i]]+err_eta2[idx[i]];
                }
            }else if (_variation=="down"){
                if (abseta[i]<0.9){
                    _rate[i]=sfs_eta0[idx[i]]-err_eta0[idx[i]];
                }else if (abseta[i]>=0.9 && abseta[i]<1.2){
                    _rate[i]=sfs_eta1[idx[i]]-err_eta1[idx[i]];
                }else{
                    _rate[i]=sfs_eta2[idx[i]]-err_eta2[idx[i]];
                }
            }
        }
    }
    double multi=1.;
    for (int i=0; i<_nlep;i++){
        multi*=_rate[i];
    }

    return multi;
}

void Mu_IDsf::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
}