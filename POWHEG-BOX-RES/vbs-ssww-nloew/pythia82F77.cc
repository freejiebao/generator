
// This program is based in the example "main31.cc" from the Pythia8 examples, used to interface Pythia shower with Powheg events

// Copyright (C) 2012 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL version 2, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

#include "Pythia8/Pythia.h"

// uncomment the line below for Pythia 8.223 and comment for Pythia 8.205
#include "Pythia8Plugins/LHAFortran.h"

// comment the line below for Pythia 8.223 and uncomment for Pythia 8.205
//#include "Pythia8/LHAFortran.h"


using namespace Pythia8;

// Only lower case letters allowed for the "interface" structures
extern "C" {

  extern struct
  {
    int    nevhep;
    int    nhep;
    int    isthep[10000];
    int    idhep[10000];
    int    jmohep[10000][2];
    int    jdahep[10000][2];
    double phep[10000][5];
    double vhep[10000][4];
  } ph_hepevt_;

  extern struct {
    int pythiamatching, pytune;
    bool use_photos, vetoqed, py8veto, nohad, savelhe, noQEDqopt;
    int doqcdps;
  } si_data_;

  extern struct {
    double xphcut;    
    double vetoscale_isr;
    double vetoscale_fsr[3];
    int evtnumber;
    int emitter_fsr[3];
    int nfsres;
    double massres[3];
    double vetoscale_isr_qed;
  } si_event_info_;

}



// Use userhooks to veto PYTHIA emissions above the POWHEG scale.
// MyUserHooks is intended to start from scalup the QED radiation from the 
// resonance. It has to be used with SpaceShower:pTmaxMatch = 1 and "TimeShower:pTmaxMatch = 1"

class MyUserHooks : public UserHooks {

public:

  MyUserHooks() {
    cout << "**** SI Setting up custom UserHook" << endl;    
  }

  ~MyUserHooks() {;}

  // Allow process cross section to be modified..

  virtual bool canSetResonanceScale() {
    // If we are vetoing QED emissions, and ptmaxmatch = 1, and we are using PYTHIA8 based veto, set scale for QED radiation from leptons
    //  (the default would be the resonance mass)
    cout << "**** SI: Allow to set scale to veto QED emissions in PYTHIA" << endl;
    if ((si_data_.vetoqed) && (si_data_.py8veto)) return true;
    else return false;
  }

  virtual double scaleResonance( const int iRes, const Event& event) {
    //     Set scale for the emissions from the resonace (FSR), equal to the scale stored in the LHE file
    cout << "SI in scaleResonance. Setting scale: " << si_event_info_.vetoscale_fsr << endl; 
    cout << event[iRes].id();
    cout << "STOP" << endl;
    cout << "\n";
    exit(-1);
    return si_event_info_.vetoscale_fsr[0];
  }    

  virtual double EventList( const Event& event)
  {
    event.list();
    return false;
  }

private:

};

// PowhegHooks is intended to veto QCD radiation (ISR and FSR) 
// and QED radiation from the resonance. So it has to be used with 
// SpaceShower:pTmaxMatch = 2 and "TimeShower:pTmaxMatch = 2"

class PowhegHooks : public UserHooks {

public:  

  // Constructor and destructor.
   PowhegHooks(int nFinalIn, int vetoModeIn, int vetoCountIn,
               int pThardModeIn, int pTemtModeIn, int emittedModeIn,
               int pTdefModeIn, int MPIvetoModeIn) : nFinal(nFinalIn),
               vetoMode(vetoModeIn), vetoCount(vetoCountIn),
               pThardMode(pThardModeIn), pTemtMode(pTemtModeIn),
               emittedMode(emittedModeIn), pTdefMode(pTdefModeIn),
               MPIvetoMode(MPIvetoModeIn) {};
  ~PowhegHooks() {}

//--------------------------------------------------------------------------

  // Routines to calculate the pT (according to pTdefMode) in a splitting:
  //   ISR: i (radiator after)  -> j (emitted after) k (radiator before)
  //   FSR: i (radiator before) -> j (emitted after) k (radiator after)
  // For the Pythia pT definition, a recoiler (after) must be specified.

  // Compute the Pythia pT separation. Based on pTLund function in History.cc
  double pTpythia(const Event &e, int RadAfterBranch, int EmtAfterBranch,
                  int RecAfterBranch, bool FSR) {

    // Convenient shorthands for later
    Vec4 radVec = e[RadAfterBranch].p();
    Vec4 emtVec = e[EmtAfterBranch].p();
    Vec4 recVec = e[RecAfterBranch].p();
    int  radID  = e[RadAfterBranch].id();

    // Calculate virtuality of splitting
    double sign = (FSR) ? 1. : -1.;
    Vec4 Q(radVec + sign * emtVec); 
    double Qsq = sign * Q.m2Calc();

    // Mass term of radiator
    double m2Rad = (abs(radID) >= 4 && abs(radID) < 7) ?
                   pow2(particleDataPtr->m0(radID)) : 0.;

    // z values for FSR and ISR
    double z, pTnow;
    if (FSR) {
      // Construct 2 -> 3 variables
      Vec4 sum = radVec + recVec + emtVec;
      double m2Dip = sum.m2Calc();
      double x1 = 2. * (sum * radVec) / m2Dip;
      double x3 = 2. * (sum * emtVec) / m2Dip;
      z     = x1 / (x1 + x3);
      pTnow = z * (1. - z);

    } else {
      // Construct dipoles before/after splitting
      Vec4 qBR(radVec - emtVec + recVec);
      Vec4 qAR(radVec + recVec);
      z     = qBR.m2Calc() / qAR.m2Calc();
      pTnow = (1. - z);
    }

    // Virtuality with correct sign
    pTnow *= (Qsq - sign * m2Rad);

    // Can get negative pT for massive splittings
    if (pTnow < 0.) {
      cout << "Warning: pTpythia was negative" << endl;
      return -1.;
    }

#ifdef DBGOUTPUT
    cout << "pTpythia: rad = " << RadAfterBranch << ", emt = "
         << EmtAfterBranch << ", rec = " << RecAfterBranch
         << ", pTnow = " << sqrt(pTnow) << endl;
#endif

    // Return pT
    return sqrt(pTnow);
  }

  // Compute the POWHEG pT separation between i and j
  // ISR: absolute pT of j
  // FSR: pT of j w.r.t. to i
  double pTpowheg(const Event &e, int i, int j, bool FSR) {

    // pT value for FSR and ISR
    double pTnow = 0.;
    if (FSR) {
      // POWHEG d_ij (in CM frame). Note that the incoming beams have not
      // been updated in the parton systems pointer yet (i.e. prior to any
      // potential recoil).
      int iInA = partonSystemsPtr->getInA(0);
      int iInB = partonSystemsPtr->getInB(0);
      double betaZ = - ( e[iInA].pz() + e[iInB].pz() ) /
                       ( e[iInA].e() + e[iInB].e()  );
      Vec4 iVecBst(e[i].p()), jVecBst(e[j].p());
      iVecBst.bst(0., 0., betaZ);
      jVecBst.bst(0., 0., betaZ);

      if ( e[i].id() == 21 && e[j].id() == 21) {
          pTnow = sqrt( (iVecBst + jVecBst).m2Calc() *
                        iVecBst.e() * jVecBst.e() /
                        pow2(iVecBst.e() + jVecBst.e()) );
	  } else {
          pTnow = sqrt( (iVecBst + jVecBst).m2Calc() *
                        jVecBst.e() / iVecBst.e() );
      }
 
    } else {
      // POWHEG pT_ISR is just kinematic pT
      pTnow = e[j].pT();
    }

    // Check result
    if (pTnow < 0.) {
      cout << "Warning: pTpowheg was negative" << endl;
      return -1.;
    }

#ifdef DBGOUTPUT
    cout << "pTpowheg: i = " << i << ", j = " << j
         << ", pTnow = " << pTnow << endl;
#endif

    return pTnow;
  }

  // Calculate pT for a splitting based on pTdefMode.
  // If j is -1, all final-state partons are tried.
  // If i, k, r and xSR are -1, then all incoming and outgoing 
  // partons are tried.
  // xSR set to 0 means ISR, while xSR set to 1 means FSR
  double pTcalc(const Event &e, int i, int j, int k, int r, int xSRin) {

    //    cout << "APPENA ENTRATO IN pTcalc" << endl;

    //cout << "idhep(i)= " << e[i].id() << endl;
    //cout << "idhep(j)= " << e[j].id() << endl;
    //cout << "idhep(k)= " << e[k].id() << endl;


    // Loop over ISR and FSR if necessary
    double pTemt = -1., pTnow;
    int xSR1 = (xSRin == -1) ? 0 : xSRin;
    int xSR2 = (xSRin == -1) ? 2 : xSRin + 1;
    for (int xSR = xSR1; xSR < xSR2; xSR++) {
      // FSR flag
      bool FSR = (xSR == 0) ? false : true;

      // If all necessary arguments have been given, then directly calculate.
      // POWHEG ISR and FSR, need i and j.
      if ((pTdefMode == 0 || pTdefMode == 1) && i > 0 && j > 0) {
        pTemt = pTpowheg(e, i, j, (pTdefMode == 0) ? false : FSR);

      // Pythia ISR, need i, j and r.
      } else if (!FSR && pTdefMode == 2 && i > 0 && j > 0 && r > 0) {
        pTemt = pTpythia(e, i, j, r, FSR);

      // Pythia FSR, need k, j and r.
      } else if (FSR && pTdefMode == 2 && j > 0 && k > 0 && r > 0) {
        pTemt = pTpythia(e, k, j, r, FSR);

      // Otherwise need to try all possible combintations.
      } else {
        // Start by finding incoming legs to the hard system after
        // branching (radiator after branching, i for ISR).
        // Use partonSystemsPtr to find incoming just prior to the
        // branching and track mothers.
        int iInA = partonSystemsPtr->getInA(0);
        int iInB = partonSystemsPtr->getInB(0);
        while (e[iInA].mother1() != 1) { iInA = e[iInA].mother1(); }
        while (e[iInB].mother1() != 2) { iInB = e[iInB].mother1(); }

        // If we do not have j, then try all final-state partons
        int jNow = (j > 0) ? j : 0;
        int jMax = (j > 0) ? j + 1 : e.size();
        for (; jNow < jMax; jNow++) {

          // Final-state jNow only
          if ( !e[jNow].isFinal() ) continue;

          // POWHEG
          if (pTdefMode == 0 || pTdefMode == 1) {

            // ISR - only done once as just kinematical pT
            if (!FSR) {
              pTnow = pTpowheg(e, iInA, jNow, (pTdefMode == 0) ? false : FSR);
              if (pTnow > 0.) pTemt = (pTemt < 0) ? pTnow : min(pTemt, pTnow);
  
              // FSR - try all outgoing partons from system before branching 
              // as i. Note that for the hard system, there is no 
              // "before branching" information.
              } else {

                int outSize = partonSystemsPtr->sizeOut(0);
                for (int iMem = 0; iMem < outSize; iMem++) {
                  int iNow = partonSystemsPtr->getOut(0, iMem);

                  // Coloured only, i != jNow and no carbon copies
                  if (iNow == jNow) continue;
                  if (jNow == e[iNow].daughter1() 
                    && jNow == e[iNow].daughter2()) continue;

                  pTnow = pTpowheg(e, iNow, jNow, (pTdefMode == 0) 
                    ? false : FSR);
                  if (pTnow > 0.) pTemt = (pTemt < 0) 
                    ? pTnow : min(pTemt, pTnow);
                } // for (iMem)

              } // if (!FSR)
  
          // Pythia
          } else if (pTdefMode == 2) {
  
            // ISR - other incoming as recoiler
            if (!FSR) {
              pTnow = pTpythia(e, iInA, jNow, iInB, FSR);
              if (pTnow > 0.) pTemt = (pTemt < 0) ? pTnow : min(pTemt, pTnow);
              pTnow = pTpythia(e, iInB, jNow, iInA, FSR);
              if (pTnow > 0.) pTemt = (pTemt < 0) ? pTnow : min(pTemt, pTnow);
  
            // FSR - try all final-state coloured partons as radiator
            //       after emission (k).
            } else {
              for (int kNow = 0; kNow < e.size(); kNow++) {
                if (kNow == jNow || !e[kNow].isFinal()) continue;
  
                // For this kNow, need to have a recoiler.
                // Try two incoming.
                pTnow = pTpythia(e, kNow, jNow, iInA, FSR);
                if (pTnow > 0.) pTemt = (pTemt < 0) 
                  ? pTnow : min(pTemt, pTnow);
                pTnow = pTpythia(e, kNow, jNow, iInB, FSR);
                if (pTnow > 0.) pTemt = (pTemt < 0) 
                  ? pTnow : min(pTemt, pTnow);

                // Try all other outgoing.
                for (int rNow = 0; rNow < e.size(); rNow++) {
                  if (rNow == kNow || rNow == jNow ||
                      !e[rNow].isFinal()) continue;
                  pTnow = pTpythia(e, kNow, jNow, rNow, FSR);
                  if (pTnow > 0.) pTemt = (pTemt < 0) 
                    ? pTnow : min(pTemt, pTnow);
                } // for (rNow)
  
              } // for (kNow)
            } // if (!FSR)
          } // if (pTdefMode)
        } // for (j)
      }
    } // for (xSR)

#ifdef DBGOUTPUT
    cout << "pTcalc: i = " << i << ", j = " << j << ", k = " << k
         << ", r = " << r << ", xSR = " << xSRin
         << ", pTemt = " << pTemt << endl;
#endif

    return pTemt;
  }

//--------------------------------------------------------------------------

  // Extraction of pThard based on the incoming event.
  // Assume that all the final-state particles are in a continuous block
  // at the end of the event and the final entry is the POWHEG emission.
  // If there is no POWHEG emission, then pThard is set to SCALUP.

  bool canVetoMPIStep()    { return true; }
  int  numberVetoMPIStep() { return 1; }
  bool doVetoMPIStep(int nMPI, const Event &e) {

    if (nMPI > 1) return false;

    // Find if there is a POWHEG emission. Go backwards through the
    // event record until there is a non-final particle. Also sum pT and
    // find pT_1 for possible MPI vetoing
    int    count = 0;
    double pT1 = 0., pTsum = 0.;
    for (int i = e.size() - 1; i > 0; i--) {
      if (e[i].isFinal()) {
        count++;
        pT1    = e[i].pT();
        pTsum += e[i].pT();
      } else break;
    }
    // mauro nfinal used only in this check, skip it
    // Extra check that we have the correct final state
    // if (count != nFinal && count != nFinal + 1) {
    //   cout << "Error: wrong number of final state particles in event" << endl;
    //   exit(1);
    // }
    // Flag if POWHEG radiation present and index
    bool isEmt = (count == nFinal) ? false : true;
    int  iEmt  = (isEmt) ? e.size() - 1 : -1;

    // If there is no radiation or if pThardMode is 0 then set pThard = SCALUP.
    pThard = -1;
    // pThardMode is 0
    if (!isEmt || pThardMode == 0) {
      // This sets the scale to veto emissions in the QCD shower by Pythia
      // This scale is used for all emissions, except if they come from the resonance
      //cout << "SI: in doVetoMPIStep: " << si_event_info_.vetoscale_isr << endl;
      pThard = si_event_info_.vetoscale_isr;
      // Not using directly scalup, because the special file LHE (two scales)
      //      pThard = infoPtr->scalup();
      
    // If pThardMode is 1 then the pT of the POWHEG emission is checked against
    // all other incoming and outgoing partons, with the minimal value taken
    } else if (pThardMode == 1) {
      pThard = pTcalc(e, -1, iEmt, -1, -1, -1);

    // If pThardMode is 2, then the pT of all final-state partons is checked
    // against all other incoming and outgoing partons, with the minimal value
    // taken
    } else if (pThardMode == 2) {
      pThard = pTcalc(e, -1, -1, -1, -1, -1);
    }

    // Find MPI veto pT if necessary
    if (MPIvetoMode == 1) {
      //pTMPI = infoPtr->QFac();
      pTMPI = (isEmt) ? pTsum / 2. : pT1;
    }

#ifdef DBGOUTPUT
    cout << "doVetoMPIStep: Qfac = " << infoPtr->scalup()
         << ", pThard = " << pThard << endl << endl;
#endif

    // Initialise other variables
    accepted   = false;
    nAcceptSeq = nISRveto = nFSRveto = 0;

    if(pThard < 0)
      {
	cout << "something wrong with pThard = " << pThard << endl;
        exit(1);
      }
    //    pThard = infoPtr->QFac();

    // Do not veto the event
    return false;
  }

//--------------------------------------------------------------------------

  // ISR veto

  bool canVetoISREmission() { return (vetoMode == 0) ? false : true; }
  bool doVetoISREmission(int, const Event &e, int iSys) {

    // Must be radiation from the hard system, otherwise return
    if (iSys != 0) return false;

    // If vetocount != 0 and we already have accepted 'vetoCount' emissions in a row,
    // do nothing; if vetocount = 0 check all emissions
    if (vetoCount != 0 && nAcceptSeq >= vetoCount) return false;

    // Pythia radiator after, emitted and recoiler after.
    int iRadAft = -1, iEmt = -1, iRecAft = -1;
    for (int i = e.size() - 1; i > 0; i--) {
      if      (iRadAft == -1 && e[i].status() == -41) iRadAft = i;
      else if (iEmt    == -1 && e[i].status() ==  43) iEmt    = i;
      else if (iRecAft == -1 && e[i].status() == -42) iRecAft = i;
      if (iRadAft != -1 && iEmt != -1 && iRecAft != -1) break;
    }
    if (iRadAft == -1 || iEmt == -1 || iRecAft == -1) {
      e.list();
      cout << "Error: couldn't find Pythia ISR emission" << endl;
      exit(1);
    }

    
    // pTemtMode == 0: pT of emitted w.r.t. radiator
    // pTemtMode == 1: min(pT of emitted w.r.t. all incoming/outgoing)
    // pTemtMode == 2: min(pT of all outgoing w.r.t. all incoming/outgoing)
    int xSR      = (pTemtMode == 0) ? 0       : -1;
    int i        = (pTemtMode == 0) ? iRadAft : -1;
    int j        = (pTemtMode != 2) ? iEmt    : -1;
    int k        = -1;
    int r        = (pTemtMode == 0) ? iRecAft : -1;
    double pTemt = pTcalc(e, i, j, k, r, xSR);

#ifdef DBGOUTPUT
    cout << "doVetoISREmission: pTemt = " << pTemt << endl << endl;
#endif

    // Veto if pTemt > pThard
    //cout << "SI In doVetoISREmission with pThard: " << pThard << endl;

    if(e[iEmt].id() ==  22){
      if (pTemt > si_event_info_.vetoscale_isr_qed) {
	nAcceptSeq = 0;
	nISRveto++;
	return true;
      }      
    }else{
      if (pTemt > pThard) {
	nAcceptSeq = 0;
	nISRveto++;
	return true;
      }
    }
    // Else mark that an emission has been accepted and continue
    nAcceptSeq++;
    accepted = true;

    return false;
  }

//--------------------------------------------------------------------------

  // FSR veto

  bool canVetoFSREmission() { return (vetoMode == 0) ? false : true; }
  bool doVetoFSREmission(int, const Event &e, int iSys, bool inr) {
    // radiation from the hard system: isys=0
    // radiation from resonances: isys!=0 and inr=1
    // MPI radiation: isys!=0 and inr=0

    // we do not veto MPI radiation
    // if we veto here gamma from resonance (inr==1), 
    // we do not have to use canSetResonanceScale

    // mauro iSys >0 and inr NOT 1 is an error
    //       isysy is the hard process level (e.g. iSys=0 id qq > WW JJ, iSys=1 is WW> lnu lnu, etc)
    //       inr is at most 1
    
    if (iSys != 0 && inr != 1) return false;

    
    // In case of radiation from resonance we veto
    // This is used for ptmaxmatch = 2. 
    // If py8veto = 1, this method is also used to veto photons, otherwise, use external function
    // force the radiation scale, pThard, to be equal to the one set in the LHE file
    if (inr == 1) {
      if ((si_data_.vetoqed == false) || (si_data_.py8veto == false)) {
        //cout << "SI: not using doVetoFSREmission" << endl;
        return false;
      }
      // the pThard assignment to be set after the identification of the resonance
      else {
        // Set scale for FSR from the resonance
        pThard = si_event_info_.vetoscale_fsr[0];
        //cout << "SI: Using PYTHIA8 based veto with ptmaxmatch = 2 for FSR, pthard: " << pThard << endl;
      }
    }


    // If vetocount != 0 and we already have accepted 'vetoCount' emissions in a row,
    // do nothing; if vetocount = 0 check all emissions
    if (vetoCount != 0 && nAcceptSeq >= vetoCount) return false;

    
    // Pythia radiator (before and after), emitted and recoiler (after)
    int iRecAft = e.size() - 1;
    int iEmt    = e.size() - 2;
    int iRadAft = e.size() - 3;
    int iRadBef = e[iEmt].mother1();

    //    cout << "rad bef aft" << e[iEmt].id() << " " << e[iRecAft].id() << " " << e[iRadAft].id() << endl;
    
    if ( (e[iRecAft].status() != 52 && e[iRecAft].status() != -53) ||
         e[iEmt].status() != 51 || e[iRadAft].status() != 51) {
      e.list();
      cout << "Error: couldn't find Pythia FSR emission" << endl;
      exit(1);
    }


    // mauro added: ptHard comes from dovetoISR, but it could change if iSys=0, inr=0 and a 22 is radiated by a 24
    //              it is cleaner to redifine here ptHard everytime to vetoscale_isr (QCD) or vetoscale_isr_qed (22)
    //              If the radiation comes from a 24 (i.e. resonance), set the scale to the corresponding vetoscale (22)
    //              or to vetoscale_isr if it is a QCD radiation

    if(e[iEmt].id() ==  22){
      pThard = si_event_info_.vetoscale_isr_qed;
    }else{
      pThard = si_event_info_.vetoscale_isr;
    }
    

    // if photon splitting from  24 set pthard according to fsr_scale
    
    if(e[iEmt].id() ==  22){
      
      int lep = 0;
      int qqq = 0;
      if(abs(e[iRadBef].id()) == 24 || abs(e[iRadBef].id()) == 11 || abs(e[iRadBef].id()) == 13 ||
	 abs(e[iRadBef].id()) == 15){
	lep=1;
      }
      // this is an approximation in case w->qq if the w radiates, but the resulting photons seem
      // supersoft
      if(abs(e[iRadBef].id()) > 0 && abs(e[iRadBef].id()) <= 5 ){
	qqq=1;
      }
      
      if(lep==qqq){
	cout << "error in dovetofsr"<< endl;
	exit(1);
      }


      if(qqq==1){
	//cout << "GAMMA DA FSR QUARK " << endl;
	//	exit(1);
      }
      
      // isAncestor(int iAncestor)  m2Calc()
      double cut=1e-6;
      double mass2;
      double foundres=0;
      int ifail=0;

      // if(e[iEmt].id()==22 && abs(e[iRadAft].id())==24){
      // 	cout << "gamma da W" << endl;
      // 	 for (int i=0; i < 10 ; i++){
      // 	   cout << i <<" "<< e[i].id()<<" "<<e[i].status()<<" "<<e[i].mother1()<<" "<<e[i].mother2()<< endl;
      // 	 }
      // }
      
      // for (int i=0; i < e.size() ; i++){
      // 	cout << i <<" "<< e[i].id()<<" "<<e[i].status()<<" "<<e[i].mother1()<<" "<<e[i].mother2()<< endl;
      // }
      // cout << "si_event_info_.massres[j]" << si_event_info_.massres[0] <<" "<< si_event_info_.massres[1]<<" " << si_event_info_.massres[2] << endl;
      // cout << "?????????????????????????" << si_event_info_.massres[3] << endl;
      // cout << "e[iEmt].id() " << e[iEmt].id() << " "<< "rad b/a "<< e[iRadBef].id() <<" "<< e[iRadAft].id() << endl;
      // cout << "e[iRadBef/Aft].m2Calc() "<< e[iRadBef].m2Calc() << "  " <<  e[iRadAft].m2Calc() << endl;
      
      //      for (int i=0; i < e.size();i++){
      for (int i=e.size()-1; i > 0 ;i--){

	//cout << "e[i].id()" << e[i].id() << "st" << e[i].status() << "mm" << e[i].p() << endl ;
	
	if(abs(e[i].id())==24 && e[iEmt].isAncestor(i) && foundres==0){

	  //cout << "questo" << endl;
	  
	  //	  if(abs(e[i].status()) >= 21 && abs(e[i].status()) <= 24){
	    foundres++;
	    mass2=e[i].m2Calc();

	    //cout << "mass2" << mass2 << endl ;
	    
	    int cnt=0;
	    double distance[3];
	    for (int j=0; j < si_event_info_.nfsres; j++){
	      if(abs((si_event_info_.massres[j]-mass2)/(si_event_info_.massres[j]+mass2)) < cut) {
		pThard = si_event_info_.vetoscale_fsr[j];
		cnt++;
		distance[cnt]=abs((si_event_info_.massres[j]-mass2)/(si_event_info_.massres[j]+mass2));
	      }
	      //		if()
	      // dovresti mettere (dabs(mass2-massres[j]))/(mass2+massres[j])< 1e-4 -->
	      // pThard = si_event_info_.vetoscale_fsr[j];		  
	    }
	    if(cnt >1 ){
	      cout << "too many matching resonances "<< cnt << endl;
	      cout << std::setprecision(9) << "mass2 "<< mass2 << endl;
	      cout << "e[iEmt].id() "<<e[iEmt].id()<< " "<< e[iRadAft].id() << endl;
	      cout << std::setprecision(9)<<" "<< si_event_info_.massres[0] <<" "<< si_event_info_.massres[1] <<" "<< si_event_info_.massres[2] << endl;
	      cout << std::setprecision(9)<< distance[0] <<" "<< distance[1] <<" "<< distance[2] << endl;
	      
	      int imin=10;
	      double dmin=1e10;
	      for(int i1 =0; i1 < cnt; i1++){
		cout << std::setprecision(9) << i1 << "  " << abs(distance[i1]) << endl;
		if(abs(distance[i1]) < dmin){
		  dmin=abs(distance[i1]);
		  imin=i1;
		}
	      }
	      if(imin > 3){
		cout << "error in dovetofsr" << endl;
		exit(1);
	      }
	      pThard = si_event_info_.vetoscale_fsr[imin];
	      cout << std::setprecision(9) << dmin << " selected "<< imin << " XX "<< si_event_info_.massres[imin] << endl;
	      //  exit(1);
	    }
	    if(cnt==0 && abs(e[iRadAft].id()) == 24) {
	      cout << "gamma from  W, set the scale to 1d-4 "<< endl;
	      pThard = 1e-4;
	    }
	    if(cnt==0 && abs(e[iRadAft].id()) != 24) {
	      ifail =1;
	      cout << "change parameter for res id " << cnt << " with cut "<< cut << endl;
	      cout << "e[iEmt].id() "<<e[iEmt].id()<< " "<< e[iRadAft].id() << endl;
	      cout <<" "<< si_event_info_.massres[0] <<" "<< si_event_info_.massres[1] <<" "<< si_event_info_.massres[2] << endl;
	      cout << mass2 << endl ;
	      //	      exit(1);	
	    }
	  
	  //}
	}
      }
      // added b
      if(ifail==1){
	double cut=1e-2;
	double mass2;
	double foundres=0;
	int ifail=0;
	
	for (int i=e.size()-1; i > 0 ;i--){
	  
	  
	  if(abs(e[i].id())==24 && e[iEmt].isAncestor(i) && foundres==0){
	    
	    foundres++;
	    mass2=e[i].m2Calc();
	    
	    int cnt=0;
	    double distance[3];
	    for (int j=0; j < si_event_info_.nfsres; j++){
	      if(abs((si_event_info_.massres[j]-mass2)/(si_event_info_.massres[j]+mass2)) < cut) {
		pThard = si_event_info_.vetoscale_fsr[j];
		cnt++;
	      }
	      //		if()
	      // dovresti mettere (dabs(mass2-massres[j]))/(mass2+massres[j])< 1e-4 -->
	      // pThard = si_event_info_.vetoscale_fsr[j];		  
	    }
	    if(cnt >1 ){
	      cout << "too many matching resonances V2"<< cnt << endl;
	      cout << "mass2 "<< mass2 << endl;
	      cout << "e[iEmt].id() "<<e[iEmt].id()<< " "<< e[iRadAft].id() << endl;
	      cout <<" "<< si_event_info_.massres[0] <<" "<< si_event_info_.massres[1] <<" "<< si_event_info_.massres[2] << endl;
	      cout << distance[0] <<" "<< distance[1] <<" "<< distance[2] << endl;
	      exit(1);
		}
	    if(cnt==0 && abs(e[iRadAft].id()) == 24) {
	      cout << "gamma from  W, set the scale to 1d-4 "<< endl;
	      pThard = 1e-4;
	    }
	    if(cnt==0 && abs(e[iRadAft].id()) != 24) {
	      ifail =1;
	      cout << "change parameter V2 for res id " << cnt << " with cut "<< cut << endl;
	      cout << "e[iEmt].id() "<<e[iEmt].id()<< " "<< e[iRadAft].id() << endl;
	      cout <<" "<< si_event_info_.massres[0] <<" "<< si_event_info_.massres[1] <<" "<< si_event_info_.massres[2] << endl;
	      cout << mass2 << endl ;
	      exit(1);	
	    }
	    
	    //}
	  }
	}
      }
      // added end
      
    }
    else{ // qcd splitting, we are there only if qcdps is on, and then we do not veto
      pThard=si_event_info_.vetoscale_isr ;
    }


    
    // Behaviour based on pTemtMode:
    //  0 - pT of emitted w.r.t. radiator before
    //  1 - min(pT of emitted w.r.t. all incoming/outgoing)
    //  2 - min(pT of all outgoing w.r.t. all incoming/outgoing)
    int xSR = (pTemtMode == 0) ? 1       : -1;

    int i   = (pTemtMode == 0) ? iRadBef : -1;
    i = (pTdefMode == 1) ? iRadAft : iRadBef;
    // using POWHEG pT definition i should be iRadAft (daugther)
    int k   = (pTemtMode == 0) ? iRadAft : -1;
    int r   = (pTemtMode == 0) ? iRecAft : -1;

    // When pTemtMode is 0 or 1, iEmt has been selected
    double pTemt = 0.;
    if (pTemtMode == 0 || pTemtMode == 1) {
      // Which parton is emitted, based on emittedMode:
      //  0 - Pythia definition of emitted
      //  1 - Pythia definition of radiated after emission
      //  2 - Random selection of emitted or radiated after emission
      //  3 - Try both emitted and radiated after emission

      // j = radiator after

      int j = iRadAft;
      //emittedMode = 0 -> j = iRadAft + 1 = iEmt 
      if (emittedMode == 0 || (emittedMode == 2 && rndmPtr->flat() < 0.5)) j++;

      for (int jLoop = 0; jLoop < 2; jLoop++) {
        if      (jLoop == 0) pTemt = pTcalc(e, i, j, k, r, xSR);
        else if (jLoop == 1) pTemt = min(pTemt, pTcalc(e, i, j, k, r, xSR));
  
        // For emittedMode == 3, have tried iRadAft, now try iEmt
        if (emittedMode != 3) break;
        if (k != -1) swap(j, k); else j = iEmt;
      }

    // If pTemtMode is 2, then try all final-state partons as emitted
    } else if (pTemtMode == 2) {
      pTemt = pTcalc(e, i, -1, k, r, xSR);
    }

#ifdef DBGOUTPUT
    cout << "doVetoFSREmission: pTemt = " << pTemt << endl << endl;
#endif

    // Veto if pTemt > pThard
    //cout << "SI In doVetoFSREmission with pThard: " << pThard << endl;
    if (pTemt > pThard) {
      nAcceptSeq = 0;
      nFSRveto++;
      return true;
    }

    // Else mark that an emission has been accepted and continue
    nAcceptSeq++;
    accepted = true;
    return false;
  }

//--------------------------------------------------------------------------

  // MPI veto

  bool canVetoMPIEmission() { return (MPIvetoMode == 0) ? false : true; }
  bool doVetoMPIEmission(int, const Event &e) {

    if (MPIvetoMode == 1) {
      if (e[e.size() - 1].pT() > pTMPI) {
#ifdef DBGOUTPUT
        cout << "doVetoMPIEmission: pTnow = " << e[e.size() - 1].pT()
             << ", pTMPI = " << pTMPI << endl << endl;
#endif
        return true;
      }
    }
    return false;
  }

//--------------------------------------------------------------------------

  // Functions to return information

  int    getNISRveto() { return nISRveto; }
  int    getNFSRveto() { return nFSRveto; }

private:
  int    nFinal, vetoMode, vetoCount, pThardMode, pTemtMode,
         emittedMode, pTdefMode, MPIvetoMode;
  double pThard, pTMPI;
  bool   accepted;
  // The number of accepted emissions (in a row)
  int nAcceptSeq;
  // Statistics on vetos
  unsigned long int nISRveto, nFSRveto;

};


// Definition of class derived from LHAupFortran
// (required in newer versions of PYTHIA)
class LHAupFortran_new : public LHAupFortran {

public:
  
  LHAupFortran_new();
  bool fillHepRup();
  bool fillHepEup();
  
};


// Implementation of required functions of the derived class
extern "C" {

  LHAupFortran_new::LHAupFortran_new() {}
  
  bool LHAupFortran_new::fillHepRup() {
    return true;
  }

  bool LHAupFortran_new::fillHepEup() {
    return true;
  }

}


extern "C" {
  
  // Main object
  Pythia* pythia_p;

  // LHA input Fortran interface (using derived class)
  LHAupFortran_new LHAinstance;

  // LHA output (to be used if .LHE events are requested)
  LHAupFromPYTHIA8* myLHA;

  void pythia_init_() {

    cout << "**** SI: Initializing PYTHIA (interface to 8.2xx versions)" << endl;
    
    // Create instance of Pythia generator and load parameters from path in variable PYTHIA8DATA
    pythia_p = new Pythia();

//     cout << "SI: pythiamatching: " << si_data_.pythiamatching << endl;
//     cout << "SI: pytune: " << si_data_.pytune << endl;
//     cout << "SI: use_photos: " << si_data_.use_photos << endl;
//     cout << "SI: vetoqed: " << si_data_.vetoqed << endl;
//     cout << "SI: py8veto: " << si_data_.py8veto << endl;
//     cout << "SI: nohad: " << si_data_.nohad << endl;
//     cout << "SI: savelhe: " << si_data_.savelhe << endl;
    
    
    // Add settings that can be set explicitly here, (or in external configuration file)
    pythia_p->settings.addMode("POWHEG:nFinal",    1, true, false, 1, 0);
    pythia_p->settings.addMode("POWHEG:veto",      1, true, true,  0, 1);
    // maximum POWHEG:veto=2 not documented
    pythia_p->settings.addMode("POWHEG:vetoCount", 0, true, false, 0, 0);
    pythia_p->settings.addMode("POWHEG:pThard",    0, true, true,  0, 2);
    pythia_p->settings.addMode("POWHEG:pTemt",     0, true, true,  0, 2);
    pythia_p->settings.addMode("POWHEG:emitted",   0, true, true,  0, 3);
    pythia_p->settings.addMode("POWHEG:pTdef",     1, true, true,  0, 2);
    pythia_p->settings.addMode("POWHEG:MPIveto",   0, true, true,  0, 1);

    // Load external configuration file
    //pythia_p->readFile("main31.cmnd");    
    // or set values for settings (hardcoded!)
    
    // Number of outgoing particles of POWHEG Born level process (not counting daughters of resonance)
    // (i.e. not counting additional POWHEG radiation)
    pythia_p->readString("POWHEG:nFinal = 1");
//    pythia_p->readString("POWHEG:nFinal = 2");

    // How vetoing is performed:
    // 0 - No vetoing is performed
    // 1 - Showers are started at the kinematical limit (pTmaxMatch = 2)
    //     and emissions are vetoed if pTemt > pThard = scalup
    pythia_p->readString("POWHEG:veto = 1");

    // After 'vetoCount' accepted emissions in a row, no more emissions
    // are checked. 'vetoCount = 0' means all emissions are checked.
    pythia_p->readString("POWHEG:vetoCount = 0");

    // Selection of pThard 
    // 0 - pThard = scalup
    // 1 - the pT of the POWHEG emission is tested against all other
    //     incoming and outgoing partons, with the minimal value chosen
    // 2 - the pT of all final-state partons is tested against all other
    //     incoming and outgoing partons, with the minimal value chosen
    pythia_p->readString("POWHEG:pThard = 0");

    // Selection of pTemt:
    //  0 - pTemt is pT of the emitted parton w.r.t. radiating parton
    //  1 - pT of the emission is checked against all incoming and outgoing
    //      partons. pTemt is set to the minimum of these values
    //  2 - the pT of all final-state partons is tested against all other
    //      incoming and outgoing partons, with the minimal value chosen
    pythia_p->readString("POWHEG:pTemt = 0");

    // Selection of emitted parton for FSR
    //  0 - Pythia definition of emitted
    //  1 - Pythia definition of radiator
    //  2 - Random selection of emitted or radiator
    //  3 - Both emitted and radiator are tried
    pythia_p->readString("POWHEG:emitted = 0");

    // pT definitions
    //  0 - POWHEG ISR pT definition is used for both ISR and FSR
    //  1 - POWHEG ISR pT and FSR d_ij definitions
    //  2 - Pythia definitions
    pythia_p->readString("POWHEG:pTdef = 1");

    // MPI vetoing
    //  0 - No MPI vetoing is done
    //  1 - When there is no radiation, MPIs with a scale above pT_1 are vetoed,
    //      else MPIs with a scale above (pT_1 + pT_2 + pT_3) / 2 are vetoed
    // according to the PYTHIA8 manual, 1 is intended specifically 
    // for POWHEG simulations of 2 -> 2 + 2 -> 3 QCD processes
    pythia_p->readString("POWHEG:MPIveto = 0"); 

    // Read in settings
//     int nEvent      = pythia_p->settings.mode("Main:numberOfEvents");
//     int nError      = pythia_p->settings.mode("Main:timesAllowErrors");

    // Read in POWHEG settings
    int nFinal      = pythia_p->settings.mode("POWHEG:nFinal");
    int vetoMode    = pythia_p->settings.mode("POWHEG:veto");
    int vetoCount   = pythia_p->settings.mode("POWHEG:vetoCount");
    int pThardMode  = pythia_p->settings.mode("POWHEG:pThard");
    int pTemtMode   = pythia_p->settings.mode("POWHEG:pTemt");
    int emittedMode = pythia_p->settings.mode("POWHEG:emitted");
    int pTdefMode   = pythia_p->settings.mode("POWHEG:pTdef");
    int MPIvetoMode = pythia_p->settings.mode("POWHEG:MPIveto");

    // Add in user hooks for shower vetoing
    MyUserHooks *PWGHook1 = NULL;
    PowhegHooks *PWGHook2 = NULL;

    // Shower matching settings
    // vetoMode is 1
    if (si_data_.pythiamatching == 2) {
      cout << "**** SI: Setting PYTHIA matching strategy to 2" << endl;
      pythia_p->readString("SpaceShower:pTmaxMatch = 2");
      pythia_p->readString("TimeShower:pTmaxMatch = 2");      
    }
    else if (si_data_.pythiamatching == 1) {
      cout << "**** SI: Setting PYTHIA matching strategy to 1" << endl;
      pythia_p->readString("SpaceShower:pTmaxMatch = 1");
      pythia_p->readString("TimeShower:pTmaxMatch = 1");      
    }
    
    // QED shower flags in PYTHIA    
    pythia_p->readString("TimeShower:QEDshowerByL  = on");
    pythia_p->readString("TimeShower:QEDshowerByQ  = on");
    pythia_p->readString("SpaceShower:QEDshowerByQ  = on");
    pythia_p->readString("TimeShower:QEDshowerByGamma = on");
    if (si_data_.noQEDqopt) {
      cout << "**** SI: noQEDqopt was on" << endl;
      pythia_p->readString("TimeShower:QEDshowerByQ  = off");
      pythia_p->readString("SpaceShower:QEDshowerByQ  = off");
      exit(1);
    }


    // pythia_p->readString("TimeShower:QEDshowerByL  = off");
    // pythia_p->readString("TimeShower:QEDshowerByQ  = off");
    // pythia_p->readString("SpaceShower:QEDshowerByQ  = off");
    // pythia_p->readString("TimeShower:QEDshowerByGamma = off");
    // pythia_p->readString("TimeShower:QEDshowerByOther = off");

    
    pythia_p->readString("TimeShower:alphaEMorder = 0"); //alpha(0) for QED shower
    pythia_p->readString("SpaceShower:alphaEMorder = 0"); //alpha(0) for QED shower
    
    // If photon radiation from leptons is performed by PHOTOS, turn off in pythia
    //if (optionphotos_.use_photos) {
    if (si_data_.use_photos) {
      cout << "**** SI: QED radiation from leptons is off in PYTHIA (because PHOTOS is on)" << endl;
      pythia_p->readString("TimeShower:QEDshowerByL  = off");
      pythia_p->readString("TimeShower:QEDshowerByGamma  = off");
      cout << "photos not implemented " << endl;
      exit(1);
    }


    cout << "QCD PS in  pythia "<< si_data_.doqcdps << endl;
    if(si_data_.doqcdps == 0){
      cout << "**** SI: QCD shower turned off "<< endl;
      pythia_p->readString("TimeShower:QCDshower = off");
      pythia_p->readString("SpaceShower:QCDshower = off");
    }
    //    exit(1);
    // lower QED shower cutoff     
    pythia_p->readString("TimeShower:pTminChgL=1.0e-6");
    pythia_p->readString("TimeShower:pTminChgQ=0.8944e0"); // QED to comply with PowHeg//
    pythia_p->readString("SpaceShower:pTminChgQ=0.8944e0"); // QED to comply with PowHeg//

    // MPI
    pythia_p->readString("PartonLevel:MPI = off");
    pythia_p->readString("MultipartonInteractions:pTmaxMatch = 0"); //default

    // hadronization on by default
    pythia_p->readString("HadronLevel:Hadronize = on");

    if(si_data_.nohad) {
      cout << "**** SI: Setting off all hadronization and decays" << endl;
      pythia_p->readString("HadronLevel:All = off");
    }

    if ((si_data_.pytune >= -1) && (si_data_.pytune <= 50)) {
      cout << "**** SI: Setting PYTHIA tune to: " << si_data_.pytune << endl;
      stringstream ss1;
      ss1 << "Tune:pp = " << si_data_.pytune;
      cout << "SI: " << ss1.str() << endl;
      pythia_p->readString(ss1.str());
//       pythia_p->readString("Tune:pp = 14"); // Monash2013 tune
    }
    else {
      cout << "**** SI: PYTHIA will use default pp tune" << endl;
    }

    
    // setting stable hadrons
    pythia_p->readString("111:mayDecay = off"); // pi0 stable//
    pythia_p->readString("211:mayDecay = off"); // pi+ stable//
    pythia_p->readString("221:mayDecay = off"); // eta stable//
    pythia_p->readString("223:mayDecay = off"); // omega stable//
    pythia_p->readString("313:mayDecay = off"); // K*0 stable//
    pythia_p->readString("331:mayDecay = off"); // eta' stable//
    pythia_p->readString("333:mayDecay = off"); // Phi stable//
    pythia_p->readString("423:mayDecay = off"); // D*0 stable//
    pythia_p->readString("413:mayDecay = off"); // D*+ stable//
    pythia_p->readString("433:mayDecay = off"); // D*+_s stable//
    pythia_p->readString("521:mayDecay = off");  // B+ stable//
    pythia_p->readString("-521:mayDecay = off"); // B- stable//
    pythia_p->readString("511:mayDecay = off"); // B0 stable//
    pythia_p->readString("-511:mayDecay = off"); // B0bar stable//
    pythia_p->readString("531:mayDecay = off"); // B0_s stable//
    pythia_p->readString("-531:mayDecay = off"); // B0_s bar stable//
    pythia_p->readString("5222:mayDecay = off"); // Sigma_b+ stable//
    pythia_p->readString("5112:mayDecay = off"); // Sigma_b- stable//
    pythia_p->readString("5232:mayDecay = off"); // Csi0_b stable//
    pythia_p->readString("-5132:mayDecay = off"); // Csi_b+ stable//
    pythia_p->readString("5132:mayDecay = off"); // Csi_b- stable//
    pythia_p->readString("541:mayDecay = off"); // B_c+ stable//
    pythia_p->readString("-541:mayDecay = off"); // B_c- stable//
    pythia_p->readString("553:mayDecay = off"); // Y(1S) stable//
    pythia_p->readString("2114:mayDecay = off"); // Delta0 stable//
    pythia_p->readString("3212:mayDecay = off"); // Sigma0 stable//
    pythia_p->readString("-5112:mayDecay = off"); // Sigma_b+ stable//
    pythia_p->readString("-5222:mayDecay = off"); // Sigma_b- stable//
    pythia_p->readString("-5122:mayDecay = off"); // Lambda0_b bar stable//
    pythia_p->readString("5332:mayDecay = off"); // Omega_b- stable//
    pythia_p->readString("-5232:mayDecay = off"); // Csi_b 0 bar stable//
    pythia_p->readString("-5332:mayDecay = off"); // Omega_b+ stable//
    pythia_p->readString("5122:mayDecay = off"); // Lambda0_b stable//

    // Choice of UserHooks defined above: 
    if(si_data_.pythiamatching == 2) {
      cout << "**** SI: Defining PowhegHook to perform the matching (ptmaxmatch = 2)" << endl;
      // POWHEG matching implemented originally in main31.cc
      PWGHook2=new PowhegHooks(nFinal, vetoMode, vetoCount, pThardMode, pTemtMode, emittedMode, pTdefMode, MPIvetoMode);
      pythia_p->setUserHooksPtr((UserHooks *) PWGHook2); 
    } 
    else if (si_data_.pythiamatching == 1) {
      // Matching based on the scale of the resonance
      // Need custom "User Hook" to be able to veto QED emissions
      cout << "**** SI: Defining custom UserHook needed to veto QED radiation (ptmaxmatch = 1)" << endl;
      PWGHook1=new MyUserHooks();
      pythia_p->setUserHooksPtr((UserHooks *) PWGHook1); 
    }
    
    // Do not print particle data table
    pythia_p->readString("Init:showChangedParticleData = off");
    
    // Possibility to set the random seed 
    cout << "**** SI: Setting random seed for PYTHIA" << endl;
    pythia_p->readString("Random:setSeed = on");
    
    // Setting of the random seed
    // A negative value gives the default seed,
    // a value 0 gives a random seed based on the time, and
    // a value between 1 and 900,000,000 a unique different random number sequence.

    // mauro for debug constant seed
    pythia_p->readString("Random:seed = 0");
    //pythia_p->readString("Random:seed = -1");

    // Set pointer to LHA interface    
    pythia_p->setLHAupPtr(&LHAinstance);

    // Set process (read LHE events from pointer)
    pythia_p->readString("Beams:frameType = 5");
    
    // Do the actual initialization 
    bool pythiaok = pythia_p->init();
    if (!pythiaok) {
      cout << "**** SI: PYTHIA could not be initialized, aborting" << endl;
      exit(1);
    }
    
    // Checking pythia random seed
    double x1 = pythia_p->rndm.flat();
    double x2 = pythia_p->rndm.flat();
    cout << "**** SI: Random values by PYTHIA random generator (for check): x = " << x1 << ", " << x2 << endl;

    // Initialize and open LHEF file for output, if requested
    if (si_data_.savelhe) {
      cout << "**** SI: Storing showered events in LHE file" << endl;
      myLHA = new LHAupFromPYTHIA8(&(pythia_p->event), &(pythia_p->info));
      // Open a file on which LHEF events should be stored, and write header.
      myLHA->openLHEF("output_shower_events.lhe");
      // Store initialization info in the LHAup object.
      myLHA->setInit();
      // Write out this initialization info on the file.
      myLHA->initLHEF();
    }
    
    
  }

  void pythia_next_(int & iret)
  {

    //cout << "SI: Processing event with Pythia, info: " << si_event_info_.evtnumber << " " << si_event_info_.xphcut << " " << si_event_info_.vetoscale_isr << " " << si_event_info_.vetoscale_fsr << endl;
    // Process event with Pythia
    iret = pythia_p->next();
    
    // Here, some C++ based analysis can be done. 

    // For example:
    // Read event weight:
    // double weight = pythia_p->info.weight();

    // Access LHE input block (input to PYTHIA):
//     for (int i = 0; i < pythia_p->process.size(); i++) {
//       cout << i << " " << pythia_p->process[i].id() << endl;
//     }

    // Access particles after the PYTHIA shower:
//     for (int i = 0; i < pythia_p->event.size(); i++) {
//       cout << i << " " << pythia_p->event[i].id() << endl;
//     }

    

    if (si_data_.savelhe) {
      // Store event info in the LHAup object.
      myLHA->setEvent();
      // Write out this event info on the file.
      // With optional argument (verbose =) false the file is smaller.
      myLHA->eventLHEF();
    }

  }

  void pythia_to_hepevt_(const int &nmxhep, int & nhep, int * isthep,
                         int * idhep,
                         int  (*jmohep)[2], int (*jdahep)[2],
                         double (*phep)[5], double (*vhep)[4])
  {
    nhep = pythia_p->event.size();
    if(nhep>nmxhep)
      {
	cout << "too many particles!" ;
	exit(-1);
    }
    for (int i = 0; i < pythia_p->event.size(); ++i)
    {
      //*(isthep+i) = pythia_p->event.statusHepMC(i);
      *(isthep+i) = pythia_p->event[i].statusHepMC();
      *(idhep+i) = pythia_p->event[i].id();
      // All pointers should be increased by 1, since here we follow
      // the c/c++ convention of indeces from 0 to n-1, but i fortran
      // they are from 1 to n.
      (*(jmohep+i))[0] = pythia_p->event[i].mother1() + 1;
      (*(jmohep+i))[1] = pythia_p->event[i].mother2() + 1;
      (*(jdahep+i))[0] = pythia_p->event[i].daughter1() + 1;
      (*(jdahep+i))[1] = pythia_p->event[i].daughter2() + 1;
      (*(phep+i))[0] = pythia_p->event[i].px();
      (*(phep+i))[1] = pythia_p->event[i].py();
      (*(phep+i))[2] = pythia_p->event[i].pz();
      (*(phep+i))[3] = pythia_p->event[i].e();
      (*(phep+i))[4] = pythia_p->event[i].m();
    }
    // override mother of very first event, set to 0
    *(jmohep)[0] = 0 ;
    *(jmohep)[1] = 0 ;
  }

  void pythia_close_() {
    //cout << "SI in pythia_close" << endl;
    if (si_data_.savelhe) {
      cout << "**** SI: Closing and saving output LHE file" << endl;
      myLHA->closeLHEF();
      delete myLHA;
    }
    delete pythia_p;
  }


}


// comment the defs for Pythia 8.223 and uncomment for Pythia 8.205

// User-written routine that does the event generation and fills hepeup.
// We do nothing here; we fill the common block on the fortran side
// before we start pythia and before we call each event.
// bool LHAupFortran::fillHepRup()
// {
//   return true;
// }

// bool LHAupFortran::fillHepEup()
// {
//   return true;
// }
