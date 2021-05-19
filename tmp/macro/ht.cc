#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"

#include <vector>

#include <iostream>

class get_ht : public multidraw::TTreeFunction {
public:
    get_ht();

    char const* getName() const override {
        return "get_ht";
    }
    TTreeFunction* clone() const override {
        return new get_ht();
    }

    unsigned getNdata() override {
        return 1;
    }
    double evaluate(unsigned) override;

protected:
    void bindTree_(multidraw::FunctionLibrary&) override;

    UIntValueReader*  nCleanJet;
    FloatArrayReader* CleanJet_pt;
    FloatArrayReader* CleanJet_eta;
};

get_ht::get_ht()
    : TTreeFunction() {
}

double
get_ht::evaluate(unsigned) {
    unsigned nJ{*nCleanJet->Get()};
    if (nJ < 1)
        return -999.;

    float sum_pt = 0.;
    for (unsigned iJ{0}; iJ != nJ; ++iJ) {
        if (CleanJet_pt->At(iJ) > 30 && abs(CleanJet_eta->At(iJ))<4.7) {
            sum_pt += CleanJet_pt->At(iJ);
        };
    }
    return sum_pt;
}

void get_ht::bindTree_(multidraw::FunctionLibrary& _library) {
    _library.bindBranch(nCleanJet, "nCleanJet");
    _library.bindBranch(CleanJet_pt, "CleanJet_pt");
    _library.bindBranch(CleanJet_eta, "CleanJet_eta");
}
