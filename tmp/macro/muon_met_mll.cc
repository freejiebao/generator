// ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonLegacy2016#RECO_efficiency_AN1
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"

#include <vector>
#include <math.h>
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4D.h"

#include <iostream>

class Mu_MET_MLL : public multidraw::TTreeFunction {
public:
    // var: mll met
    // cat: NOM GE RES
    Mu_MET_MLL(int yr, int nl,char const* var,char const* cat);

    char const* getName() const override {
        return "Mu_MET_MLL";
    }
    TTreeFunction* clone() const override {
        return new Mu_MET_MLL(_year,_nlep,_variable.c_str(),_category.c_str());
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
    DoubleArrayReader* Lepton_syspt;
    FloatValueReader* MET_pt;
    FloatValueReader* MET_phi;
    FloatValueReader* mll;
    int _year;
    int _nlep;
    std::string _variable{};
    std::string _category{};
};

Mu_MET_MLL::Mu_MET_MLL(int yr,int nl, char const* var,char const* cat):
    TTreeFunction(),
    _year{yr},
    _nlep{nl},
    _variable{var},
    _category{cat}{
}

double
Mu_MET_MLL::evaluate(unsigned) {
    unsigned nL{*nLepton->Get()};
    float _mll = *mll->Get();
    float _MET_pt = *MET_pt->Get();
    float _MET_phi = *MET_phi->Get();
    if ((nL < _nlep) || (Lepton_pt->At(0)<=200)){
        if(_variable=="mll"){
            return _mll;
        }else{
            return _MET_pt;
        }
    }
    // check all the leptons are muons
    for (int i = 0; i < _nlep; ++i) {
        if(abs(Lepton_pdgId->At(i))!=13){
            if(_variable=="mll"){
                return _mll;
            }else{
                return _MET_pt;
            }
        }
    }
    std::vector<ROOT::Math::PtEtaPhiMVector> part_pf(_nlep);
    std::vector<ROOT::Math::PtEtaPhiMVector> part_sys(_nlep);
    ROOT::Math::PtEtaPhiMVector part_tot_pf;
    ROOT::Math::PtEtaPhiMVector part_tot_sys;
    for(int i=0; i<_nlep; i++){
        part_pf[i]=ROOT::Math::PtEtaPhiMVector(Lepton_pt->At(i),Lepton_eta->At(i),Lepton_phi->At(i),0.1056583745);
        part_tot_pf+=part_pf[i];
        part_sys[i]=ROOT::Math::PtEtaPhiMVector(Lepton_syspt->At(i),Lepton_eta->At(i),Lepton_phi->At(i),0.1056583745);
        part_tot_sys+=part_sys[i];
    }
    if (_variable=="mll"){
        return (part_sys[0]+part_sys[1]).mass();
    }
    // met
    double px_pf = part_tot_pf.px();
    double py_pf = part_tot_pf.py();

    double px_sys = part_tot_sys.px();
    double py_sys = part_tot_sys.py();

    double met_px = _MET_pt*std::cos(_MET_phi);
    double met_py = _MET_pt*std::sin(_MET_phi);

    float corr_met_pt = std::sqrt(std::pow(met_px-(px_sys-px_pf),2)+std::pow(met_py-(py_sys-py_pf),2));
    return corr_met_pt;
}

void Mu_MET_MLL::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");
    _library.bindBranch(Lepton_rochesterSF, "Lepton_rochesterSF");
    if(_category=="NOM"){ // NOM: nominal
        _library.bindBranch(Lepton_syspt, "Lepton_newpt");
    }else if (_category=="GE"){
        _library.bindBranch(Lepton_syspt, "Lepton_gept");//GE: ge scale
    }else{
        _library.bindBranch(Lepton_syspt, "Lepton_respt");//RES: resolution
    }
    if(_year==2017){
        _library.bindBranch(MET_pt, "METFixEE2017_pt");
        _library.bindBranch(MET_phi, "METFixEE2017_phi");
    }else{
        _library.bindBranch(MET_pt, "MET_pt");
        _library.bindBranch(MET_phi, "MET_phi");
    }
    _library.bindBranch(mll, "mll");
}
