// ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonLegacy2016#RECO_efficiency_AN1
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/GEScaleSyst/GEScaleSyst.h"
#include "LatinoAnalysis/GEScaleSyst/GEScaleSyst.cc"
#include <random>
#include <vector>

#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4D.h"

#include <iostream>

class Mu_GE : public multidraw::TTreeFunction {
public:
    Mu_GE(int yr);

    char const *getName() const override {
        return "Mu_GE";
    }

    TTreeFunction *clone() const override {
        return new Mu_GE(_year);
    }

    void beginEvent(long long) override;

    int getMultiplicity() override { return 1; }

    unsigned getNdata() override;

    double evaluate(unsigned) override;

protected:
    void bindTree_(multidraw::FunctionLibrary &) override;

    int _year;

    static long long currentEntry;
    static UIntValueReader *run;
    static UIntValueReader *nLepton;
    static IntArrayReader *Lepton_pdgId;
    static FloatArrayReader *Lepton_pt;
    static FloatArrayReader *Lepton_eta;
    static FloatArrayReader *Lepton_phi;
    static DoubleArrayReader *Lepton_newpt;

    void setValues(long long);

    static std::vector<double> Lepton_respt;
    //UIntValueReader* nGenJet;
    //FloatArrayReader* GenJet_pt;
    //FloatArrayReader* GenJet_eta;
    //FloatArrayReader* GenJet_phi;
    //FloatArrayReader* GenJet_mass;

    //FloatValueReader* GenMET_pt;
    //FloatValueReader* GenMET_phi;
};

/*static*/
long long Mu_GE::currentEntry{-2};
UIntValueReader *Mu_GE::run{};
UIntValueReader *Mu_GE::nLepton{};
IntArrayReader *Mu_GE::Lepton_pdgId{};
FloatArrayReader *Mu_GE::Lepton_pt{};
FloatArrayReader *Mu_GE::Lepton_eta{};
FloatArrayReader *Mu_GE::Lepton_phi{};
DoubleArrayReader *Mu_GE::Lepton_newpt{};
std::vector<double> Mu_GE::Lepton_respt{};

Mu_GE::Mu_GE(int yr) :
        TTreeFunction(),
        _year{yr} {
}

void Mu_GE::beginEvent(long long _iEntry) {
    setValues(_iEntry);
}

unsigned Mu_GE::getNdata() {
    return Lepton_respt.size();
}

double Mu_GE::evaluate(unsigned iL) {
    return Lepton_respt[iL];
}

void Mu_GE::setValues(long long _iEntry) {
    if (_iEntry == currentEntry)
        return;
    if (_iEntry >=10) return;
    currentEntry = _iEntry;

    Lepton_respt.clear();

    unsigned nL{*nLepton->Get()};
    Lepton_respt.resize(nL);
    std::cout<<">>>>>>>>>>>>>>>> ge:"<<_iEntry<<std::endl;
    if ((*run->Get())!=1){ // it's data, just store pf pt
        for (unsigned iL{0}; iL != nL; ++iL) {
            Lepton_respt[iL] = Lepton_newpt->At(iL);
        }
    }else{
        GEScaleSyst GE=GEScaleSyst();
        GE.SetVerbose(0);

        int _1st_copy;
        if(_year==2016){
            _1st_copy=161000;
        }else if (_year==2017){
            _1st_copy=171000;
        }else{
            _1st_copy=181000;
        }
        int ncopy=5;

        for (unsigned iL{0}; iL != nL; ++iL) {
            Lepton_respt[iL] = Lepton_newpt->At(iL);
            if (Lepton_pt->At(0) > 200 && std::abs(Lepton_pdgId->At(iL)) == 13) {
                double tmp_pt=0;
                double clip_phi=Lepton_phi->At(iL);
                if (clip_phi>M_PI){
                    clip_phi = 2*M_PI/3.0; // phi bin edge: https://github.com/khaosmos93/GEScaleSyst/blob/08603f5ac727b3f4e50bb4d801c9fc3991a6230b/GEScaleSyst.h#L32
                }else if(clip_phi < -M_PI){
                    clip_phi = -2*M_PI/3.0;
                }
                for(int i=0;i<ncopy;i++){
                    tmp_pt+=GE.GEScaleCorrPt( _1st_copy+i, Lepton_respt[iL], Lepton_eta->At(iL), clip_phi,Lepton_pdgId->At(iL)>0 ? 1:-1);
                }
                Lepton_respt[iL]=tmp_pt/ncopy;
            }
            std::cout<<"\t Lepton_pt:"<<Lepton_pt->At(iL)<<"\t Lepton_newpt:"<<Lepton_newpt->At(iL)<<"\t Lepton_gept:"<<Lepton_respt[iL]<<std::endl;
        }
    }
}

void Mu_GE::bindTree_(multidraw::FunctionLibrary &_library) {
    if (currentEntry == -2) {
        std::cout << "Let's start Mu_GE." << std::endl;
        currentEntry = -1;
        _library.bindBranch(run, "run");
        _library.bindBranch(nLepton, "nLepton");
        _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
        _library.bindBranch(Lepton_pt, "Lepton_pt");
        _library.bindBranch(Lepton_eta, "Lepton_eta");
        _library.bindBranch(Lepton_phi, "Lepton_phi");
        _library.bindBranch(Lepton_newpt, "Lepton_newpt");
        _library.addDestructorCallback([]() {
            currentEntry = -2;
            run = nullptr;
            nLepton = nullptr;
            Lepton_pdgId = nullptr;
            Lepton_pt = nullptr;
            Lepton_eta = nullptr;
            Lepton_phi = nullptr;
            Lepton_newpt = nullptr;
        });
    }
}
