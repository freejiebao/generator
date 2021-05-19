#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"

#include "Math/Vector4D.h"
#include "TFile.h"
#include "TGraph.h"
#include "TH1F.h"
#include "TLorentzVector.h"
#include "TMath.h"
#include "TSystem.h"
#include "TVector2.h"

#include <cmath>
#include <iostream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>

class HEMissue : public multidraw::TTreeFunction {
public:
    HEMissue(char const* _type);
    HEMissue(unsigned type);

    char const* getName() const override {
        return "HEMissue";
    }
    TTreeFunction* clone() const override {
        return new HEMissue(returnVar_);
    }

    unsigned getNdata() override {
        return 1;
    }
    double evaluate(unsigned) override;

protected:
    enum ReturnType {
        _mjj,
        _jet1_pt,
        _jet2_pt,
        _MET_pt,
        _MET_phi,
        nVarTypes
    };

    ~HEMissue(){};

    void bindTree_(multidraw::FunctionLibrary&) override;

    unsigned returnVar_{nVarTypes};

    UIntValueReader*    run{};
    UIntValueReader*    luminosityBlock{};
    ULong64ValueReader* event{};

    static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;

    static UIntValueReader*  nJet;
    static FloatArrayReader* Jet_pt;
    static FloatArrayReader* Jet_eta;
    static FloatArrayReader* Jet_phi;
    static IntArrayReader*   Jet_idx;
    static FloatArrayReader* Jet_mass;
    static FloatValueReader* MET_pt;
    static FloatValueReader* MET_phi;

    static std::array<double, nVarTypes> returnValues;

    static void setValues(UInt_t, UInt_t, ULong64_t);
};

std::tuple<UInt_t, UInt_t, ULong64_t> HEMissue::currentEvent{};
UIntValueReader*                      HEMissue::nJet;
FloatArrayReader*                     HEMissue::Jet_pt{};
FloatArrayReader*                     HEMissue::Jet_eta{};
FloatArrayReader*                     HEMissue::Jet_phi{};
FloatArrayReader*                     HEMissue::Jet_mass{};
IntArrayReader*                       HEMissue::Jet_idx{};
FloatValueReader*                     HEMissue::MET_pt;
FloatValueReader*                     HEMissue::MET_phi;

std::array<double, HEMissue::nVarTypes> HEMissue::returnValues{};

HEMissue::HEMissue(char const* _type)
    : TTreeFunction() {
    std::string type(_type);
    if (type == "_mjj")
        returnVar_ = _mjj;
    else if (type == "_jet1_pt")
        returnVar_ = _jet1_pt;
    else if (type == "_jet2_pt")
        returnVar_ = _jet2_pt;
    else if (type == "_MET_pt")
        returnVar_ = _MET_pt;
    else if (type == "_MET_phi")
        returnVar_ = _MET_phi;
    else
        throw std::runtime_error("unknown return type " + type);
}

HEMissue::HEMissue(unsigned type)
    : TTreeFunction(), returnVar_(type) {
}

double
HEMissue::evaluate(unsigned) {
    setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
    return returnValues[returnVar_];
}

void HEMissue::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(run, "run");
    _library.bindBranch(luminosityBlock, "luminosityBlock");
    _library.bindBranch(event, "event");

    _library.bindBranch(nJet, "nCleanJet");
    _library.bindBranch(Jet_pt, "CleanJet_pt");
    _library.bindBranch(Jet_eta, "CleanJet_eta");
    _library.bindBranch(Jet_phi, "CleanJet_phi");
    _library.bindBranch(Jet_mass, "Jet_mass");
    _library.bindBranch(Jet_idx, "CleanJet_jetIdx");
    _library.bindBranch(MET_pt, "MET_pt");
    _library.bindBranch(MET_phi, "MET_phi");

    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {
        nJet     = nullptr;
        Jet_pt   = nullptr;
        Jet_eta  = nullptr;
        Jet_phi  = nullptr;
        Jet_mass = nullptr;
        Jet_idx  = nullptr;
        MET_phi  = nullptr;
        MET_pt   = nullptr;
    });
}

/*static*/
void HEMissue::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event) {

    if (std::get<0>(currentEvent) == _run && std::get<1>(currentEvent) == _luminosityBlock && std::get<2>(currentEvent) == _event)
        return;

    currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

    //cout << "VBS category "<< vbs_cat <<  endl;
    //resolved category
    // To apply JER we have to change the 4-momenta

    vector<ROOT::Math::PtEtaPhiMVector> jets;
    if (*nJet->Get() < 2) {
        cout << ">>> Jets' size less than 2... Skipping " << endl;
        return;
    }

    int njet = *nJet->Get();
    for (int i = 0; i < njet; i++) {
        jets.emplace_back(Jet_pt->At(i),
                          Jet_eta->At(i),
                          Jet_phi->At(i),
                          Jet_mass->At(Jet_idx->At(i)));
    }
    // the correction is not for data, it's for mc
    //if(_run<319077){
    //    returnValues[_mjj]   = *mjj->Get();
    //    returnValues[_jet1_pt]  = jets[0].Pt();
    //    returnValues[_jet2_pt]  = jets[1].Pt();
    //    returnValues[_MET_pt]  = *MET_pt->Get();
    //    returnValues[_MET_phi] = *MET_phi->Get();
    //    return;
    //}

    //Correct the jets
    vector<ROOT::Math::PtEtaPhiMVector> corr_jets;
    ROOT::Math::PtEtaPhiMVector         tmp_jets;
    ROOT::Math::PtEtaPhiMVector         delta_p4;
    for (auto j : jets) {
        float new_pt = j.Pt();
        //cout << new_pt << " " << j.Eta() << " " << j.Phi() << endl;
        if ((j.Eta() > -2.5 && j.Eta() < -1.3) && (j.Phi() > -1.57 && j.Phi() < -0.87)) {
            new_pt *= 0.8;
        }
        else if ((j.Eta() > -3. && j.Eta() < -2.5) && (j.Phi() > -1.57 && j.Phi() < -0.87)) {
            new_pt *= 0.65;
        }
        tmp_jets = ROOT::Math::PtEtaPhiMVector(new_pt, j.Eta(), j.Phi(), j.M());
        corr_jets.emplace_back(tmp_jets);
        if (j.Pt() > 15) {  //(all jets with pt>15 GeV passing the tight ID -in order to reject muons/electrons-, and propagate this to the MET as well)
            delta_p4 += (tmp_jets - j);
        }
    }

    //met correction
    ROOT::Math::PtEtaPhiMVector met{*MET_pt->Get(), 0, *MET_phi->Get(), 0};

    returnValues[_mjj]     = (corr_jets[0] + corr_jets[1]).M();
    returnValues[_jet1_pt] = corr_jets[0].Pt();
    returnValues[_jet2_pt] = corr_jets[1].Pt();

    returnValues[_MET_pt]  = (met - delta_p4).Pt();
    returnValues[_MET_phi] = (met - delta_p4).Phi();

    //cout << "vbs_1_pt" << vbs_jets[1].Pt() << "- "<< vbs_jets[1].Pt() << endl;
}