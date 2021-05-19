// ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonLegacy2016#RECO_efficiency_AN1
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include <random>
#include <vector>

#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include "Math/Vector4D.h"

#include <iostream>

class Mu_RES : public multidraw::TTreeFunction {
public:
    Mu_RES(int yr);

    char const *getName() const override {
        return "Mu_RES";
    }

    TTreeFunction *clone() const override {
        return new Mu_RES(_year);
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
long long Mu_RES::currentEntry{-2};
UIntValueReader *Mu_RES::run{};
UIntValueReader *Mu_RES::nLepton{};
IntArrayReader *Mu_RES::Lepton_pdgId{};
FloatArrayReader *Mu_RES::Lepton_pt{};
FloatArrayReader *Mu_RES::Lepton_eta{};
FloatArrayReader *Mu_RES::Lepton_phi{};
DoubleArrayReader *Mu_RES::Lepton_newpt{};
std::vector<double> Mu_RES::Lepton_respt{};

Mu_RES::Mu_RES(int yr) :
        TTreeFunction(),
        _year{yr} {
}

void Mu_RES::beginEvent(long long _iEntry) {
    setValues(_iEntry);
}

unsigned Mu_RES::getNdata() {
    return Lepton_respt.size();
}

double Mu_RES::evaluate(unsigned iL) {
    return Lepton_respt[iL];
}

void Mu_RES::setValues(long long _iEntry) {
    if (_iEntry == currentEntry)
        return;

    currentEntry = _iEntry;

    Lepton_respt.clear();

    unsigned nL{*nLepton->Get()};
    Lepton_respt.resize(nL);

    if ((*run->Get())!=1){ // it's data, just store pf pt
        for (unsigned iL{0}; iL != nL; ++iL) {
            Lepton_respt[iL] = Lepton_newpt->At(iL);
        }
    }else{
        ROOT::Math::PtEtaPhiMVector part;
        double p;
        double sigma;
        std::default_random_engine generator;
        for (unsigned iL{0}; iL != nL; ++iL) {
            Lepton_respt[iL] = Lepton_newpt->At(iL);
            if (Lepton_pt->At(0) > 200 && std::abs(Lepton_pdgId->At(iL)) == 13) {
                part = ROOT::Math::PtEtaPhiMVector(Lepton_respt[iL], Lepton_eta->At(iL), Lepton_phi->At(iL), 0.1056583745);
                p = part.P();
                // smear sigma
                if (abs(Lepton_eta->At(iL)) < 1.2) {
                    if (_year == 2016) {
                        sigma = 0.0061 + 0.0001 * p - 1.10e-7 * std::pow(p, 2) + 6.10e-11 * std::pow(p, 3) -
                                1.10e-14 * std::pow(p, 4);
                    } else if (_year == 2017) {
                        sigma = 0.0053 + 0.0001 * p - 1.10e-7 * std::pow(p, 2) + 7.10e-11 * std::pow(p, 3) -
                                1.10e-14 * std::pow(p, 4);
                    } else {
                        sigma = 0.0062 + 0.0001 * p - 1.10e-7 * std::pow(p, 2) + 5.10e-11 * std::pow(p, 3) -
                                9.10e-15 * std::pow(p, 4);
                    }
                } else if (abs(Lepton_eta->At(iL)) >= 1.2 && abs(Lepton_eta->At(iL)) < 2.1) {
                    if (_year == 2016) {
                        sigma = 0.0134 + 0.00006 * p - 5.10e-8 * std::pow(p, 2) + 3.10e-11 * std::pow(p, 3) -
                                5.10e-15 * std::pow(p, 4);
                    } else if (_year == 2017) {
                        sigma = 0.0136 + 0.00006 * p - 3.10e-8 * std::pow(p, 2) + 1.10e-12 * std::pow(p, 3) -
                                3.10e-15 * std::pow(p, 4);
                    } else {
                        sigma = 0.0136 + 0.00005 * p - 2.10e-8 * std::pow(p, 2) + 5.10e-12 * std::pow(p, 3);
                    }
                } else {
                    if (_year == 2016) {
                        sigma = 0.0151 + 0.0001 * p - 4.10e-8 * std::pow(p, 2) + 4.10e-12 * std::pow(p, 3) -
                                1.10e-14 * std::pow(p, 4);
                    } else if (_year == 2017) {
                        sigma = 0.0170 + 0.00008 * p - 3.10e-8 * std::pow(p, 2) + 2.10e-11 * std::pow(p, 3) -
                                8.10e-14 * std::pow(p, 4);
                    } else {
                        sigma = 0.0174 + 0.00009 * p - 3.10e-9 * std::pow(p, 2) + 2.10e-11 * std::pow(p, 3) -
                                5.10e-15 * std::pow(p, 4);
                    }
                }
                std::normal_distribution<double> smearing(0, sigma * 0.46);
                //part.SetPt((1+smearing(generator))*pf_pt);
                Lepton_respt[iL] *= (1 + smearing(generator));
            }
        }
    }
}

void Mu_RES::bindTree_(multidraw::FunctionLibrary &_library) {
    if (currentEntry == -2) {
        std::cout << "Let's start Mu_RES." << std::endl;
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
