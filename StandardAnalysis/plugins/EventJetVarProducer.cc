#ifndef EVENT_JET_VAR_PRODUCER
#define EVENT_JET_VAR_PRODUCER

#include "TH2D.h"
#include "TH1D.h"
#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"


class EventJetVarProducer : public EventVariableProducer {
public:
  EventJetVarProducer (const edm::ParameterSet &);
  ~EventJetVarProducer ();

private:
  void AddVariables(const edm::Event &);
  edm::EDGetTokenT<vector<TYPE(jets)> >             tokenJets_;
  edm::EDGetTokenT<vector<TYPE(mets)> >             tokenMets_;
  edm::EDGetTokenT<vector<pat::PackedCandidate> >   tokenPFCands_;
  edm::EDGetTokenT<vector<pat::PackedCandidate> >   tokenLostTracks_;
  edm::EDGetTokenT<vector<pat::PackedGenParticle> >      tokenMcparticles_;

  bool isFirstEvent_;

  bool IsValidJet(const TYPE(jets) & jet);

  unsigned getNTracks (const edm::Handle<vector<pat::PackedCandidate> > &, const edm::Handle<vector<pat::PackedCandidate> > &, double &) const;
  bool hasNeutralino (const edm::Handle<vector<pat::PackedGenParticle> > &) const;
};



EventJetVarProducer::EventJetVarProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  isFirstEvent_ (true)
{
  tokenJets_        =  consumes<vector<TYPE(jets)> >             (collections_.getParameter<edm::InputTag>  ("jets"));
  tokenMets_        =  consumes<vector<TYPE(mets)> >             (collections_.getParameter<edm::InputTag>  ("mets"));
  tokenPFCands_     =  consumes<vector<pat::PackedCandidate> >   (collections_.getParameter<edm::InputTag>  ("pfCandidates"));
  tokenLostTracks_  =  consumes<vector<pat::PackedCandidate> >   (collections_.getParameter<edm::InputTag>  ("lostTracks"));
  tokenMcparticles_ =  consumes<vector<pat::PackedGenParticle> >      (collections_.getParameter<edm::InputTag>  ("mcparticles"));
}

EventJetVarProducer::~EventJetVarProducer() {}

bool
EventJetVarProducer::IsValidJet(const TYPE(jets) & jet){

  if (!(jet.pt() > 30))         return false;
  if (!(fabs(jet.eta()) < 4.5)) return false;
  if (!anatools::jetPassesTightLepVeto (jet)) return false;

  return true;
}


void
EventJetVarProducer::AddVariables (const edm::Event &event) {

  edm::Handle<vector<TYPE(jets)> > jets;
  if (!event.getByToken (tokenJets_, jets)) {
    clog << "ERROR:  Could not find jets collection." << endl;
    return;
  }

  edm::Handle<vector<TYPE(mets)> > mets;
  if (!event.getByToken (tokenMets_, mets)) {
    clog << "ERROR:  Could not find mets collection." << endl;
    return;
  }

  edm::Handle<vector<pat::PackedCandidate> > pfCands;
  if (!event.getByToken (tokenPFCands_, pfCands)) {
    clog << "ERROR:  Could not find pfCandidates collection." << endl;
    return;
  }

  edm::Handle<vector<pat::PackedCandidate> > lostTracks;
  event.getByToken (tokenLostTracks_, lostTracks);

  edm::Handle<vector<pat::PackedGenParticle> > mcParticles;
  event.getByToken (tokenMcparticles_, mcParticles);

  int nJets = 0;
  double dijetMaxDeltaPhi         = -999.;  // default is large negative value
  double deltaPhiMetJetLeading    =  999.;  // default is large positive value
  double deltaPhiMetJetSubleading =  999.;
  double ptJetLeading    = -999;
  double ptJetSubleading = -999;
  double phiJetLeading = -999;
  double phiJetSubleading = -999;
  int idx1 = -1;
  for (const auto &jet1 : *jets) {
    idx1++;
    if (!IsValidJet(jet1)) continue;
    int idx2 = -1;
    if (jet1.pt() > ptJetSubleading) {
      double dPhi = fabs(deltaPhi(jet1, mets->at(0)));
      if (jet1.pt() > ptJetLeading) {
        ptJetSubleading = ptJetLeading;
        phiJetSubleading = phiJetLeading;
        deltaPhiMetJetSubleading = deltaPhiMetJetLeading;
        ptJetLeading = jet1.pt();
        phiJetLeading = jet1.phi();
        deltaPhiMetJetLeading = dPhi;
      } else {
        ptJetSubleading = jet1.pt();
        phiJetSubleading = jet1.phi();
        deltaPhiMetJetSubleading = dPhi;
      }
    }
    for (const auto &jet2 : *jets) {
      idx2++;
      if (idx2 <= idx1)              continue;  // Avoid double-counting.
      if (!IsValidJet(jet2)) continue;
      double dPhi = fabs(deltaPhi(jet1.phi(), jet2.phi()));
      if (dPhi > dijetMaxDeltaPhi) {
        dijetMaxDeltaPhi = dPhi;
      }
    }
    nJets++;
  }

  double trackRho = 0.0;
  unsigned nTracks = getNTracks (pfCands, lostTracks, trackRho);

  bool hasNeutralinoFlag = hasNeutralino (mcParticles);

  (*eventvariables)["nJets"]            = nJets;
  (*eventvariables)["dijetMaxDeltaPhi"] = dijetMaxDeltaPhi;
  (*eventvariables)["phiJetLeading"]     = phiJetLeading;
  (*eventvariables)["phiJetSubleading"]  = phiJetSubleading;
  (*eventvariables)["deltaPhiMetJetLeading"]     = deltaPhiMetJetLeading;
  (*eventvariables)["deltaPhiMetJetSubleading"]  = deltaPhiMetJetSubleading;

  (*eventvariables)["eventUnixTime"]  = event.time ().unixTime ();
  (*eventvariables)["runNumber"]  = event.run ();

  (*eventvariables)["nTracks"]  = nTracks;
  (*eventvariables)["trackRho"]  = trackRho;

  (*eventvariables)["isCharginoChargino"]  = (mcParticles.isValid () ? !hasNeutralinoFlag : false);
  (*eventvariables)["isCharginoNeutralino"]  = (mcParticles.isValid () ? hasNeutralinoFlag : false);

  isFirstEvent_ = false;
}

unsigned
EventJetVarProducer::getNTracks (const edm::Handle<vector<pat::PackedCandidate> > &pfCands, const edm::Handle<vector<pat::PackedCandidate> > &lostTracks, double &trackRho) const
{
  unsigned nTracks = 0.0;
  TH2D *etaPhi = new TH2D ("etaPhi", ";#phi;#eta", 20, -3.142, 3.142, 20, -2.5, 2.5);
  for (const auto &pfCand : *pfCands)
    {
      if (pfCand.charge () && pfCand.numberOfHits () > 0)
        {
          nTracks++;
          etaPhi->Fill (pfCand.phi (), pfCand.eta ());
        }
    }
  if (lostTracks.isValid ())
    {
      if (isFirstEvent_)
        clog << "[EventJetVarProducer] using lost tracks collection..." << endl;
      nTracks += lostTracks->size ();
      for (const auto &lostTrack : *lostTracks)
        etaPhi->Fill (lostTrack.phi (), lostTrack.eta ());
    }
  else
    if (isFirstEvent_)
      clog << "[EventJetVarProducer] NOT using lost tracks collection..." << endl;

  set<double> trackNumberDensity;
  for (int iPhi = 1; iPhi <= etaPhi->GetXaxis ()->GetNbins (); iPhi++)
    {
      for (int iEta = 1; iEta <= etaPhi->GetYaxis ()->GetNbins (); iEta++)
        {
          double phiWidth = etaPhi->GetXaxis ()->GetBinWidth (iPhi),
                 etaWidth = etaPhi->GetYaxis ()->GetBinWidth (iEta),
                 area = phiWidth * etaWidth,
                 number = etaPhi->GetBinContent (iPhi, iEta);

          trackNumberDensity.insert (number / area);
        }
    }
  delete etaPhi;

  unsigned i = 0, n = trackNumberDensity.size ();
  trackRho = 0.0;
  for (set<double>::const_iterator numberDensity = trackNumberDensity.cbegin (); i <= n / 2.0 && numberDensity != trackNumberDensity.cend (); numberDensity++, i++)
    {
      if (n % 2 && i == (n - 1) / 2)
        trackRho = *numberDensity;
      if (!(n % 2) && (i == (n / 2) - 1 || i == n / 2))
        trackRho += *numberDensity;
    }
  if (!(n % 2))
    trackRho /= 2.0;

  return nTracks;
}

bool
EventJetVarProducer::hasNeutralino (const edm::Handle<vector<pat::PackedGenParticle> > &mcParticles) const
{
  if (mcParticles.isValid ())
    {
      unsigned i = 0;
      for (const auto &mcParticle : *mcParticles)
        {
          if (abs (mcParticle.pdgId ()) == 1000022)
            return true;
          if ((++i) >= 10)
            break;
        }
    }
  else
    if (isFirstEvent_)
      clog << "[EventJetVarProducer] NOT determining generated signal event type..." << endl;
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventJetVarProducer);


#endif
