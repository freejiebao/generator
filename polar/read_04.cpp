// c++ -o read_04 `root-config --glibs --cflags` CfgParser.cc LHEF.cc -lm read_04.cpp
/*
apply basic VBS selections
http://govoni.web.cern.ch/govoni/tesi/docs/Alessandro_Tarabini_Tesi.pdf
*/


#include "LHEF.h"
//#include "LHEF_joint.h"
#include <iomanip>
#include <vector>
#include <map>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cassert>
#include <fstream>
#include <algorithm>

#include "TH1.h"
#include "TH2.h"
#include "TFile.h"
#include "TLorentzVector.h"

#include "CfgParser.h"

using namespace std ;


// all histograms of a single sample
struct histos
{
  TString m_name ;  // name of the sample
  double  m_XS ;    // cross-section of the sample (in fb)
  double  m_lumi ;  // integrated luminosity (in /fb)
  map<string, TH1F *> m_histograms ;

  // integral of the events collected, 
  // needed for the histograms normalisation
  double m_norm ;
  
  histos (TString name, double XS, double lumi = 59.74) : 
    m_name (name), 
    m_XS (XS),
    m_lumi (lumi),
    m_norm (0.)
    {
    makeHisto ("m_detajj","#Delta#eta_{jj}[GeV]","Events", 6,2.5,9) ;
    makeHisto ("m_dphijj","#Delta#phi_{jj}[GeV]","Events", 6,0,3.14) ;
    makeHisto ("m_dphijj_2","#Delta#phi_{jj}[GeV]","Events", 12,0,3.14) ;
    makeHisto ("m_dphill","#Delta#phi_{ll}[GeV]","Events", 6,0,3.14) ;
    makeHisto ("m_dphill_2","#Delta#phi_{ll}[GeV]","Events", 12,0,3.14) ;
    float tmp1[]={30,60,90,120,150,180,220,260,300,350,450};
    makeHisto ("m_met","p_{t}^{miss}[GeV]","Events", 10,tmp1) ;
    float tmp2[]={30,90,150,220,300,450};
    makeHisto ("m_met_2","p_{t}^{miss}[GeV]","Events", 5,tmp2) ;
    float tmp3[]={500,1000,1500,2000,2700,3500,5000};
    makeHisto ("m_mjj","m_{jj}[GeV]","Events", 6,tmp3) ;
    float tmp4[]={500,1000,1500,2000,2700,3500};
    makeHisto ("m_mjj_2","m_{jj}[GeV]","Events", 5,tmp4) ;
    float tmp5[]={500,1000,1500,2000,3500};
    makeHisto ("m_mjj_3","m_{jj}[GeV]","Events", 4,tmp5) ;
    float tmp6[]={20,80,140,200,260,320,400,500,800};
    makeHisto ("m_mll","m_{ll}[GeV]","Events", 8,tmp6) ;
    float tmp7[]={20,50,80,110,140,170,200,230,260,290,320,360,400,450,500,650,800};
    makeHisto ("m_mll_2","m_{ll}[GeV]","Events", 16,tmp7) ;
    float tmp8[]={20,80,140,200,260,320,400,500,800};
    makeHisto ("m_mll_3","m_{ll}[GeV]","Events", 8,tmp8) ;
    float tmp9[]={25,50,80,120,160,200,250,300,370,450};
    makeHisto ("m_ptl1","p_{t}^{l1}[GeV]","Events", 9,tmp9) ;
    float tmp10[]={20,35,50,70,90,120,150,180,210,250};
    makeHisto ("m_ptl2","p_{t}^{l2}[GeV]","Events", 9,tmp10) ;
    float tmp11[]={20,35,50,70,90,120,180,250};
    makeHisto ("m_ptl2_2","p_{t}^{l2}[GeV]","Events", 7,tmp11) ;
    float tmp12[]={30,100,180,260,340,420,500,700,900};
    makeHisto ("m_ptj1","p_{t}^{j1}[GeV]","Events", 8,tmp12) ;
    float tmp13[]={30,100,180,260,340,420,500};
    makeHisto ("m_ptj1_2","p_{t}^{j1}[GeV]","Events", 6,tmp13) ;
    float tmp14[]={30,50,80,120,160,200,240,280,380,500};
    makeHisto ("m_ptj2","p_{t}^{j2}[GeV]","Events", 9,tmp14) ;
    float tmp15[]={30,50,80,120,160,200,240,280,380};
    makeHisto ("m_ptj2_2","p_{t}^{j2}[GeV]","Events", 8,tmp15) ;
    makeHisto ("costheta1","cos#theta1","Events", 10,-1,1) ;
    makeHisto ("costheta2","cos#theta2","Events", 10,-1,1) ;
    makeHisto ("costheta11","cos#theta1","Events", 10,-1,1) ;
    makeHisto ("costheta22","cos#theta2","Events", 10,-1,1) ;
    makeHisto ("m_mlvlv","m_{lvlv}[GeV]","Events", 30,100,400) ;
    
    /*
    makeHisto ("m_mjj","m_{jj}[GeV]","Events", 30,500,2000) ;
    makeHisto ("m_mll","m_{ll}[GeV]","Events", 40,20,400) ;
    makeHisto ("m_ptl1","p_{t}^{l1}[GeV]","Events", 33,25,355) ;
    makeHisto ("m_ptl2","p_{t}^{l2}[GeV]","Events", 33,20,350) ;
    makeHisto ("m_ptj1","p_{t}^{j1}[GeV]","Events", 32,30,350) ;
    makeHisto ("m_ptj2","p_{t}^{j2}[GeV]","Events", 32,30,350) ;
    makeHisto ("m_met","p_{t}^{miss}[GeV]","Events", 40,30,400) ;
    makeHisto ("m_detajj","#Delta#eta_{jj}[GeV]","Events", 15,2.5,10) ;
    makeHisto ("m_mlvlv","m_{lvlv}[GeV]","Events", 30,100,400) ;
    makeHisto ("costheta1","cos#theta1","Events", 10,-1,1) ;
    makeHisto ("costheta2","cos#theta2","Events", 10,-1,1) ;
    makeHisto ("costheta11","cos#theta1","Events", 10,-1,1) ;
    makeHisto ("costheta22","cos#theta2","Events", 10,-1,1) ;
    */
    }
  double increaseNorm (double step = 1.) 
    {
      m_norm += step ;
      return m_norm ;
    }

  // simplify histogram creation
  TH1F * makeHisto (const TString & varname, const TString & x_axis,const TString & y_axis, int nBins, float min, float max)
    {
      TH1F * histo = new TH1F (varname + TString ("_") + m_name, varname + TString ("_")  + m_name+TString(";")+x_axis+TString(";")+y_axis, nBins, min, max) ;
      histo->Sumw2 () ;
      if (m_histograms.find (varname.Data ()) != m_histograms.end ())
        {
          cout << "WARNING histogram " << varname << " defined twice" << endl ;
          return histo ;
        }
      m_histograms[varname.Data ()] = histo ;
      return histo ;
    } 
  TH1F * makeHisto (const TString & varname, const TString & x_axis,const TString & y_axis, int nBins, float *xbins)
    {
      TH1F * histo = new TH1F (varname + TString ("_") + m_name, varname + TString ("_")  + m_name+TString(";")+x_axis+TString(";")+y_axis, nBins, xbins) ;
      histo->Sumw2 () ;
      if (m_histograms.find (varname.Data ()) != m_histograms.end ())
        {
          cout << "WARNING histogram " << varname << " defined twice" << endl ;
          return histo ;
        }
      m_histograms[varname.Data ()] = histo ;
      return histo ;
    } 
  // fill the histograms through the map
  void fill (string varname, double value, double weight = 1.)
    { 
      bool fold_overflow=true;
      if (m_histograms.find (varname) == m_histograms.end ())
        {
          cout << "WARNING histogram " << varname << " does not exist" << endl ;
          return ;
        }
        
      int NbinsX=m_histograms[varname]->GetNbinsX();
      float BinWidth=m_histograms[varname]->GetXaxis()->GetBinWidth(NbinsX);
      float upper_edge=m_histograms[varname]->GetXaxis()->GetBinLowEdge(NbinsX)+BinWidth;
      if(value>=upper_edge && fold_overflow){
        value=m_histograms[varname]->GetXaxis()->GetBinCenter(NbinsX);
      }
      m_histograms[varname]->Fill (value, weight) ;
      return ; 
    }
  
  // normalise histograms to the integrated cross-section
  void norm (/* double inputIntegral = 0*/)
    {
//      double factor = m_lumi * m_XS / fabs (m_histograms.begin ()->second->Integral ()) ;
//      if (inputIntegral != 0) factor = m_lumi * m_XS / inputIntegral ;

      double factor = m_lumi * 1000. * m_XS / m_norm ;
      for (map<string, TH1F *>::iterator it = m_histograms.begin () ; 
           it != m_histograms.end () ; ++it)
         it->second->Scale (factor) ;
    }
  
  ~histos ()
    {
      // this being empty is not very nice, to be replaced with the unique_ptr or auto_ptr thing 
      // for the histogram pointers, but I need to find a smart way to do it
      // w/o need for implementing it for each histogram I add      
    }  
    
  void save (TFile & outfile) 
    {
      outfile.cd () ;
      for (map<string, TH1F *>::iterator it = m_histograms.begin () ; 
           it != m_histograms.end () ; ++it)
        it->second->Write () ;
    }
  
} ;


// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


TLorentzVector buildLP (LHEF::Reader & reader, int iPart)
{
  TLorentzVector tlv
    (
      reader.hepeup.PUP.at (iPart).at (0), //PG px
      reader.hepeup.PUP.at (iPart).at (1), //PG py
      reader.hepeup.PUP.at (iPart).at (2), //PG pz
      reader.hepeup.PUP.at (iPart).at (3)  //PG E
    ) ;
  return tlv ;
}


// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


inline float zetaStar (float etaq1, float etaq2, float eta)
{
  return (eta - 0.5 * (etaq1 + etaq2)) / fabs (etaq1 - etaq2) ;
}


// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


// Fill the histograms for a single sample
// histograms will not get normalised, since the same sample
// could be split in several LHE files and this function
// may get called several times, one for each LHE file.
// Therefore, the normalisation will have to be called afterwards
double 
fillHistos (LHEF::Reader & reader, histos & Histos, int max = -1)
{
  int events = 0 ;
   
  //PG loop over input events
  while (reader.readEvent ()) 
    {
//      if ( reader.outsideBlock.length() ) std::cout << reader.outsideBlock;

      if (events++ % 10000 == 0) cout << "        reading event in file: " << events << endl ;
          
      vector<TLorentzVector> v_f_Ws ;
      vector<TLorentzVector> v_f_quarks ;
      vector<TLorentzVector> v_f_leptons ;
      vector<TLorentzVector> v_f_neutrinos ;

      // loop over particles in the event
      for (int iPart = 0 ; iPart < reader.hepeup.IDUP.size (); ++iPart) 
        {
          // outgoing particles          
          if (reader.hepeup.ISTUP.at (iPart) == 1)
            {
              TLorentzVector dummy = buildLP (reader, iPart) ;
              // quarks
              if (abs (reader.hepeup.IDUP.at (iPart)) < 7) 
                {
                  v_f_quarks.push_back (dummy) ;        
                } // quarks
              else if (abs (reader.hepeup.IDUP.at (iPart)) == 11 ||
                       abs (reader.hepeup.IDUP.at (iPart)) == 13 ||
                       abs (reader.hepeup.IDUP.at (iPart)) == 15)
                {
                  v_f_leptons.push_back (dummy) ;
                }
              else if (abs (reader.hepeup.IDUP.at (iPart)) == 12 ||
                       abs (reader.hepeup.IDUP.at (iPart)) == 14 ||
                       abs (reader.hepeup.IDUP.at (iPart)) == 16)
                {
                  v_f_neutrinos.push_back (dummy) ;        
                }
            } // outgoing particles
        } // loop over particles in the event

      int warnNum = 0 ;
      if (v_f_quarks.size () < 2)
        {
          cout << "warning, not enough quarks" << endl ;
          ++warnNum ;
        }
      if (v_f_leptons.size () < 2)
        {
          cout << "warning, not enough leptons" << endl ;
          ++warnNum ;
        }
      if (v_f_neutrinos.size () < 2)
        {
          cout << "warning, not enough neutrinos" << endl ;
          ++warnNum ;
        }
      if (warnNum > 0) continue ;

      //PG apply basic selections
      //PG ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 

      auto l1=v_f_leptons.at(0);
      auto l2=v_f_leptons.at(1);
      auto n1=v_f_neutrinos.at(0);
      auto n2=v_f_neutrinos.at(1);
      auto j1=v_f_quarks.at(0);
      auto j2=v_f_quarks.at(1);

      float weight = reader.hepeup.XWGTUP ;
      Histos.increaseNorm (weight) ;

      if (v_f_quarks.at (0).Pt () < 30) continue ;
      if (v_f_quarks.at (1).Pt () < 30) continue ;

      if (v_f_leptons.at (0).Pt () < 25) continue ;
      if (v_f_leptons.at (1).Pt () < 20) continue ;

      TLorentzVector ME = v_f_neutrinos.at (0) + v_f_neutrinos.at (1) ;
      if (ME.Pt () < 30) continue ;

      TLorentzVector v_jj = v_f_quarks.at (0) + v_f_quarks.at (1) ;
      if (fabs (v_f_quarks.at (0).Eta ()>5)) continue;
      if (fabs (v_f_quarks.at (1).Eta ()>5)) continue;
      if (fabs (v_f_quarks.at (0).Eta () - v_f_quarks.at (1).Eta ()) < 2.5 ) continue ;
      if (v_jj.M () < 500) continue ;

      TLorentzVector v_ll = v_f_leptons.at (0) + v_f_leptons.at (1) ;
      if (v_ll.M () < 20) continue ;
      if (fabs (zetaStar (v_f_quarks.at (0).Eta (), v_f_quarks.at (1).Eta (), v_f_leptons.at (0).Eta ())) > 0.75) continue ;
      if (fabs (zetaStar (v_f_quarks.at (0).Eta (), v_f_quarks.at (1).Eta (), v_f_leptons.at (1).Eta ())) > 0.75) continue ;
      
      //PG fill histograms
      //PG ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
      
//      Histos.m_mjj->Fill (v_jj.M (), reader.hepeup.XWGTUP) ;
//      Histos.m_mll->Fill (v_ll.M (), reader.hepeup.XWGTUP) ;
      Histos.fill ("m_mjj", v_jj.M (), weight) ;
      Histos.fill ("m_mjj_2", v_jj.M (), weight) ;
      Histos.fill ("m_mjj_3", v_jj.M (), weight) ;
      Histos.fill ("m_mll", v_ll.M (), weight) ;
      Histos.fill ("m_mll_2", v_ll.M (), weight) ;
      Histos.fill ("m_mll_3", v_ll.M (), weight) ;
      Histos.fill ("m_dphijj", j1.DeltaPhi(j2), weight) ;
      Histos.fill ("m_dphijj_2", j1.DeltaPhi(j2), weight) ;
      Histos.fill ("m_dphill", l1.DeltaPhi(l2), weight) ;
      Histos.fill ("m_dphill_2", l1.DeltaPhi(l2), weight) ;

      float ptl1 = v_f_leptons.at (0).Pt () ;
      float ptl2 = v_f_leptons.at (1).Pt () ;

      if (ptl1 < ptl2) swap (ptl1, ptl2) ;

      Histos.fill ("m_ptl1", ptl1, weight) ;
      Histos.fill ("m_ptl2", ptl2, weight) ;
      Histos.fill ("m_ptl2_2", ptl2, weight) ;
      
      TLorentzVector v_lvlv = l1+n1+l2+n2;
      Histos.fill ("m_mlvlv", v_lvlv.M(), weight) ;

      Histos.fill ("m_met", ME.Pt (), weight) ;
      Histos.fill ("m_met_2", ME.Pt (), weight) ;
      
      float ptj1 = j1.Pt () ;
      float ptj2 = j2.Pt () ;
      //if (ptj1 < ptj2) swap (ptj1, ptj2) ;
      Histos.fill ("m_ptj1", ptj1, weight) ;
      Histos.fill ("m_ptj1_2", ptj1, weight) ;
      Histos.fill ("m_ptj2", ptj2, weight) ;
      Histos.fill ("m_ptj2_2", ptj2, weight) ;
      Histos.fill ("m_detajj", abs(j1.Eta()-j2.Eta()), weight) ;

      auto l1_1=l1;
      auto l2_1=l2;
      auto l1_2=l1;
      auto l2_2=l2;
      auto w1_1=l1+n1;
      auto w2_1=l2+n2;  
      auto w1_2=l1+n1;
      auto w2_2=l2+n2;
      auto wboost1_1=w1_1.BoostVector(); 
      auto wboost2_1=w2_1.BoostVector(); 
      auto wboost1_2=w1_2.BoostVector(); 
      auto wboost2_2=w2_2.BoostVector(); 
      l1_1.Boost(-wboost1_1);
      w1_1.Boost(-wboost1_1);
      w2_1.Boost(-wboost1_1);
      l2_2.Boost(-wboost2_2);
      w2_2.Boost(-wboost2_2);
      w1_2.Boost(-wboost2_2);
      Histos.fill ("costheta1", TMath::Cos(l1_1.Vect().Angle(w1_1.Vect())), weight) ;
      Histos.fill ("costheta2", TMath::Cos(l2_2.Vect().Angle(w2_2.Vect())), weight) ;      
      Histos.fill ("costheta11", cos(l1_1.Angle(-w2_1.Vect())), weight) ;
      Histos.fill ("costheta22", cos(l2_2.Angle(-w1_2.Vect())), weight) ;
      if (max > 0 && max < events) 
        {
          cout << max << " events reached, exiting" << endl ;
          break ;
        }

    } //PG loop over input events

  return events ;
  
}


// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


struct inputInfo
{
  double mass ;
  string mg_file ;
  double mg_xs ;
  string ph_file ;
  double ph_xs ;
  void print ()
    {
      cout << "----------------------------\n" ;
      cout << "mass    : " << mass << "\n" ;
      cout << "mg_file : " << mg_file << "\n" ;
      cout << "mg_xs   : " << mg_xs << "\n" ;
      cout << "ph_file : " << ph_file << "\n" ;
      cout << "ph_xs   : " << ph_xs << "\n" ;
      cout << "----------------------------\n" ;
    }
} ;


// ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


int main (int argc, char ** argv) 
{

  if (argc < 2)
    {
      cerr << "Forgot to put the cfg file --> exit " << endl ;
      return 1 ;
    }

  int maxEventsPerSample = -1 ;
  if (argc >= 3)
    {
      maxEventsPerSample = atoi (argv[2]) ;
    }
  cout << "reading " << maxEventsPerSample << " events per sample" << endl ;

  CfgParser * gConfigParser = new CfgParser (argv[1]) ;

  //PG get the samples to be analised, 
  //PG including collection of LHE files and the relative XS

  vector<string> collections = gConfigParser->readStringListOpt ("general::samples") ;
  map<string, pair<float, vector<string> > > samples ;
  // loop over samples
  for (int i = 0 ; i < collections.size () ; ++i)
    {
      float XS = gConfigParser->readFloatOpt (collections.at (i) + "::XS") ;
      vector<string> inputfiles = gConfigParser->readStringListOpt (collections.at (i) + "::files") ;
      samples[collections.at (i)] = pair<float, vector<string> > (XS, inputfiles) ;
    } // loop over samples

  //PG prepare the histogram structs to be filled,
  //PG fill the histograms looping on LHE events

  // loop over samples
  map<string, pair<float, vector<string> > >::iterator it ;
  vector<histos> Histos ;
  for (it = samples.begin () ; it != samples.end () ; ++it)
    {
      cout << "sample: " << it->first << endl ;
      Histos.push_back (histos (it->first, it->second.first)) ;
      // loop over files
      int events = 0 ;
      for (int ifile = 0 ; ifile < it->second.second.size () ; ++ifile)
        {
          cout << "    reading: " << it->second.second.at (ifile) << endl ;
          std::ifstream ifs (it->second.second.at (ifile).c_str ()) ;
          LHEF::Reader reader (ifs) ;
          events += fillHistos (reader, Histos.back (), maxEventsPerSample) ;
          if (maxEventsPerSample > 0 && events >= maxEventsPerSample) break ;
          cout << "    read: " << events << " events" << endl ;

        } // loop over files
      Histos.back ().norm () ;
    } // loop over samples

  //PG save histograms
  string outfilename = gConfigParser->readStringOpt ("general::outputFile") ;
  TFile outFile (outfilename.c_str (), "recreate") ;
  for (int i = 0 ; i < Histos.size () ; ++i) Histos.at (i).save (outFile) ;
  outFile.Close () ;

  return 0 ;
}