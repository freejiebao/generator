#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"

#include <vector>

#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4Dfwd.h"
#include "TVector2.h"

#include <iostream>

class CF_wgt : public multidraw::TTreeFunction {
public:
    CF_wgt(char const* yr,char const* var);

    char const* getName() const override {
        return "CF_wgt";
    }
    TTreeFunction* clone() const override {
        return new CF_wgt(_year.c_str(),_variation.c_str());
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
    //FloatArrayReader* Lepton_eta;
    std::string _year{};
    std::string _variation{};
    //UIntValueReader* nGenJet;
    //FloatArrayReader* GenJet_pt;
    //FloatArrayReader* GenJet_eta;
    //FloatArrayReader* GenJet_phi;
    //FloatArrayReader* GenJet_mass;

    //FloatValueReader* GenMET_pt;
    //FloatValueReader* GenMET_phi;
};

CF_wgt::CF_wgt(char const* yr,char const* var):
    TTreeFunction(),
    _year{yr},
    _variation{var}{
}

double
CF_wgt::evaluate(unsigned) {
    unsigned nL{*nLepton->Get()};
    if (nL < 2)
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

    if (iPromptL.size() < 2)
        return 0.;  // false
    //if(Lepton_pdgId->At(iPromptL[0])*Lepton_pdgId->At(iPromptL[1])!=-11*11)
    //  return 0.;
    // 2016 data
    std::vector<double> chargeflip_rate = {2.12423e-06,5.69653e-07,1.02339e-04};
    std::vector<double> chargeflip_rate_err = {4.62571e-07,5.24664e-07,1.04662e-04};
    if(_year=="2017"){
        chargeflip_rate = {2.99592e-06,1.55314e-07,1.35219e-05};
        chargeflip_rate_err = {7.15101e-07,1.54395e-07,1.55985e-05};
    }
    else if (_year=="2018"){
        chargeflip_rate = {1.73537e-06,9.15401e-07,4.27461e-07};
        chargeflip_rate_err = {4.14130e-07,5.12000e-07,4.56917e-07};
    }

    int idx1 = 0;
    int idx2 = 0;
    if (Lepton_pt->At(iPromptL[0]) > 25 && Lepton_pt->At(iPromptL[0]) < 100) {
        idx1 = 0;
    }
    else if (Lepton_pt->At(iPromptL[0]) >= 100 && Lepton_pt->At(iPromptL[0]) < 200) {
        idx1 = 1;
    }
    else if (Lepton_pt->At(iPromptL[0]) >= 200) {
        idx1 = 2;
    }

    if (Lepton_pt->At(iPromptL[1]) > 25 && Lepton_pt->At(iPromptL[1]) < 100) {
        idx1 = 0;
    }
    else if (Lepton_pt->At(iPromptL[1]) >= 100 && Lepton_pt->At(iPromptL[1]) < 200) {
        idx1 = 1;
    }
    else if (Lepton_pt->At(iPromptL[1]) >= 200) {
        idx1 = 2;
    }

    //double _sf1=sf[idx1];
    //double _sf2=sf[idx2];
    double _rate1=0;
    double _rate2=0;
    if (_variation=="nom"){
        _rate1= chargeflip_rate[idx1];
        _rate2= chargeflip_rate[idx2];
    }
    else if (_variation=="up"){
        _rate1= chargeflip_rate[idx1]+chargeflip_rate_err[idx1];
        _rate2= chargeflip_rate[idx2]+chargeflip_rate_err[idx2];
    }
    else if (_variation=="down"){
        _rate1= std::max(0.0,chargeflip_rate[idx1]-chargeflip_rate_err[idx1]);
        _rate2= std::max(0.0,chargeflip_rate[idx2]-chargeflip_rate_err[idx2]);
    }
    if (abs(Lepton_pdgId->At(iPromptL[0])) != 13) {
        _rate1 = 0;
    }
    if (abs(Lepton_pdgId->At(iPromptL[1])) != 13) {
        _rate2 = 0;
    }
    //double mis_id_sf= _rate1*_sf1*(1-_rate2*_sf2)+(1-_rate1*_sf1)*_rate2*_sf2;
    double mis_id_sf = _rate1 * (1 - _rate2) + (1 - _rate1) * _rate2;
    return mis_id_sf;
}

void CF_wgt::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    //_library.bindBranch(Lepton_eta, "Lepton_eta");

    //_library.bindBranch(nGenJet, "nGenJet");
    //_library.bindBranch(GenJet_pt, "GenJet_pt");
    //_library.bindBranch(GenJet_eta, "GenJet_eta");
    //_library.bindBranch(GenJet_phi, "GenJet_phi");
    //_library.bindBranch(GenJet_mass, "GenJet_mass");

    //_library.bindBranch(GenMET_pt, "GenMET_pt");
    //_library.bindBranch(GenMET_phi, "GenMET_phi");
}
