// ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonLegacy2016#RECO_efficiency_AN1
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"

#include <vector>

#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4D.h"

#include <iostream>

class Mu_ResScale : public multidraw::TTreeFunction {
public:
    Mu_ResScale(char const* yr,char const* cate,char const* var, int nl);

    char const* getName() const override {
        return "Mu_ResScale";
    }
    TTreeFunction* clone() const override {
        return new Mu_ResScale(_year.c_str(),_category.c_str(),_variation.c_str(),_nlep);
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
    std::string _year{};
    std::string _category{};
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

Mu_ResScale::Mu_ResScale(char const* yr,char const* cate,char const* var, int nl):
    TTreeFunction(),
    _year{yr},
    _category{cate},
    _variation{var},
    _nlep{nl}{
}

double
Mu_ResScale::evaluate(unsigned) {
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
    std::vector<double> diff_scale={0.0155,0.0085,0.0100,0.0239,0.0262,0.0217,0.0324,0.0356,0.1526,0.3481};
    std::vector<double> diff_res = {0.0216,0.0127,0.0087,0.0074,0.0100,0.0022,0.0112,0.0050,0.0207,0.0354};
    if(_year=="2017"){
        diff_scale={0.0155,0.0085,0.0100,0.0239,0.0262,0.0217,0.0324,0.0356,0.1526,0.3481};
        diff_res = {0.0216,0.0127,0.0087,0.0074,0.0100,0.0022,0.0112,0.0050,0.0207,0.0354};
    }
    else if (_year=="2018"){
        diff_scale={0.0155,0.0085,0.0100,0.0239,0.0262,0.0217,0.0324,0.0356,0.1526,0.3481};
        diff_res = {0.0216,0.0127,0.0087,0.0074,0.0100,0.0022,0.0112,0.0050,0.0207,0.0354};
    }
    std::vector<double> pt;
    for (int i=0; i<_nlep;i++){
        pt.push_back(Lepton_pt->At(iPromptL[i]));
    }
    std::vector<int> idx(_nlep,0);
    for (int i=0; i<_nlep;i++){
        if (pt[i] < 200) {//only consider momentum > 200 muons
            idx[i] = -1;
        }
        else if (pt[i] >= 200 && pt[i] < 300) {
            idx[i] = 2;
        }
        else if (pt[i] >= 300 && pt[i] < 400) {
            idx[i] = 3;
        }
        else if (pt[i] >= 400 && pt[i] < 500) {
            idx[i] = 4;
        }
        else if (pt[i] >= 500 && pt[i] < 700) {
            idx[i] = 5;
        }
        else if (pt[i] >= 700 && pt[i] < 900) {
            idx[i] = 6;
        }
        else if (pt[i] >= 900 && pt[i] < 1200) {
            idx[i] = 7;
        }
        else if (pt[i] >= 1200 && pt[i] < 1500) {
            idx[i] = 8;
        }
        else if (pt[i] >= 1500) {
            idx[i] = 9;
        }
    }

    //double _sf1=sf[idx1];
    //double _sf2=sf[idx2];
    std::vector<double> _rate(_nlep,1.);
    for (int i=0; i<_nlep;i++){
        if (idx[i]>=0 && abs(Lepton_pdgId->At(iPromptL[i])) == 13){
            if (_category=="scale"){
                if (_variation=="up"){
                    _rate[i]= 1+diff_scale[idx[i]];
                }
                else if (_variation=="down"){
                    _rate[i]= 1-diff_scale[idx[i]];
                }
            }else{
                if (_variation=="up"){
                    _rate[i]= 1+diff_res[idx[i]];
                }
                else if (_variation=="down"){
                    _rate[i]= 1-diff_res[idx[i]];
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

void Mu_ResScale::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
}