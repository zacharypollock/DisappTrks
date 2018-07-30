from OSUT3Analysis.Configuration.histogramDefinitions import * # import this first so we can overwrite standard histogram definitions if needed
from DisappTrks.StandardAnalysis.HistogramDefinitions import *

def cullHistogram(histoPSet, name):
    histos = histoPSet.histograms
    for i in xrange(len(histos) - 1, -1, -1):
        if histos[i].name == name:
            del histos[i]

def cullHistograms(histoPSet, names):
    for name in names:
        cullHistogram(histoPSet, name)

################################################################################
# Individual histogram changes for pat::IsolatedTrack from CandidateTrack
################################################################################

cullHistograms(TrackHistograms, ['trackd0', 'trackd0Mag']) # 'dxy' (wrt PV) instead of 'd0'
cullHistogram(TrackHistograms, 'trackChi2') # no normalizedChi2

# no track isolation
cullHistograms(TrackExtraHistograms, ['trackIsolation', 
                                      'trackIsolationWithPU', 
                                      'trackIsolationNoPUVsWithPU', 
                                      'trackDRMinJetVsIso'])

# no RecHits for calo energy methods
cullHistograms(TrackExtraHistograms, ['trackFitPlane', 
                                      'trackCaloEMDeltaRp5', 
                                      'trackCaloHadDeltaRp5', 
                                      'trackCaloTot', 
                                      'trackCaloTotByP', 
                                      'trackCaloTot_RhoCorr', 
                                      'trackCaloTot_RhoCorrWide',
                                      'trackCaloTotByP_RhoCorr'])

# the track fit covariance matrix isn't available in pat::IsolatedTrack, so ptError can't be calculated
cullHistograms(TrackExtraHistograms, ['trackPtError', 'trackPtErrorByPt'])

# pat::IsolatedTrack's dxy and dz methods are already with respect to the PV, so we undo the correction
for histo in TrackEventVariableHistograms.histograms:
    for inputVar in histo.inputVariables:
        if trackDZWRTPV in inputVar:
            inputVar = "track.dz"

for histo in TrackEventVarHistograms.histograms:
    for inputVar in histo.inputVariables:
        if trackD0WRTPV in inputVar and "fabs" in inputVar:
            inputVar = "fabs(track.dxy)"
        elif trackD0WRTPV in inputVar:
            inputVar = "track.dxy"
        elif trackDZWRTPV in inputVar and "fabs" in inputVar:
            inputVar = "fabs(track.dz)"
        elif trackDZWRTPV in inputVar:
            inputVar = "track.dz"

# When not producing ntuples, it's likely that electrons/muons/taus will have been selected/skimmed
# So the safest place to get 'dR to closest lepton' is from the pfCandidates -- the name of these methods
# is changed to denote this
cullHistograms(TrackExtraHistograms, ['trackDeltaRToClosestElectron', 
                                      'trackTauDeltaRVsTrackElectronDeltaR', 
                                      'trackTauDeltaRVsTrackMuonDeltaR', 
                                      'trackDeltaRToClosestMuon', 
                                      'trackDeltaRToClosestTau', 
                                      'trackDeltaRToClosestTauHad'])
ExtraDeltaRToClosestLeptonHistograms = cms.VPSet (
    cms.PSet (
        name = cms.string("trackDeltaRToClosestPFElectron"),
        title = cms.string("deltaRMinPFElec;#DeltaR_{min}(track, PF electron)"),
        binsX = cms.untracked.vdouble(100, 0, 1),
        inputVariables = cms.vstring("deltaRToClosestPFElectron"),
    ),
    cms.PSet (
        name = cms.string("trackPFChHadDeltaRVsTrackPFElectronDeltaR"),
        title = cms.string(";#DeltaR_{min}(track, PF electron);#DeltaR_{min}(track, PF charged hadron)"),
        binsX = cms.untracked.vdouble(100, 0, 0.001),
        binsY = cms.untracked.vdouble(100, 0, 0.001),
        inputVariables = cms.vstring("deltaRToClosestPFElectron", "deltaRToClosestPFChHad"),
    ),
    cms.PSet (
        name = cms.string("trackPFChHadDeltaRVsTrackPFMuonDeltaR"),
        title = cms.string(";#DeltaR_{min}(track, PF muon);#DeltaR_{min}(track, PF charged hadron)"),
        binsX = cms.untracked.vdouble(100, 0, 0.001),
        binsY = cms.untracked.vdouble(100, 0, 0.001),
        inputVariables = cms.vstring("deltaRToClosestPFMuon", "deltaRToClosestPFChHad"),
    ),
    cms.PSet (
        name = cms.string("trackDeltaRToClosestPFMuon"),
        title = cms.string("deltaRMinPFMuon;#DeltaR_{min}(track, PF muon)"),
        binsX = cms.untracked.vdouble(100, 0, 1),
        inputVariables = cms.vstring("deltaRToClosestPFMuon"),
    ),
    cms.PSet (
        name = cms.string("trackDeltaRToClosestPFChHad"),
        title = cms.string("deltaRMinPFChHad;#DeltaR_{min}(track, PF charged hadron)"),
        binsX = cms.untracked.vdouble(100, 0, 1),
        inputVariables = cms.vstring("deltaRToClosestPFChHad"),
    ),
)
for histo in ExtraDeltaRToClosestLeptonHistograms:
    TrackExtraHistograms.histograms.append(histo)

################################################################################
# New histograms comparing pat::IsolatedTrack to dR-matched CandidateTrack
################################################################################

IsolatedTrackCandidateTrackHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("isoTrackIsMatchedToCandidateTrack"),
            title = cms.string(";has CandidateTrack"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("matchedCandidateTrack.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("isoTrackDRToMatchedCandidateTrack"),
            title = cms.string(";#Delta R to matched CandidateTrack"),
            binsX = cms.untracked.vdouble(300, 0.0, 0.3),
            inputVariables = cms.vstring("dRToMatchedCandidateTrack"),
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackPt"),
            title = cms.string(";IsolatedTrack Pt [GeV];Matched CandidateTrack Pt [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt", "matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackEta"),
            title = cms.string(";IsolatedTrack Eta;Matched CandidateTrack Eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta", "matchedCandidateTrack.eta")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackPhi"),
            title = cms.string(";IsolatedTrack Phi;Matched CandidateTrack Phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi", "matchedCandidateTrack.phi")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackNumValidPixelHits"),
            title = cms.string(";IsolatedTrack NumValidPixelHits;Matched CandidateTrack NumValidPixelHits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            binsY = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidPixelHits", "matchedCandidateTrack.hitPattern_.numberOfValidPixelHits")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackNumValidHits"),
            title = cms.string(";IsolatedTrack NumValidHits;Matched CandidateTrack NumValidHits"),
            binsX = cms.untracked.vdouble(100, -0.5, 99.5),
            binsY = cms.untracked.vdouble(100, -0.5, 99.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidHits", "matchedCandidateTrack.numberOfValidHits")
        ),
        cms.PSet (
            name = cms.string("matchedCandidateTrackNormalizedChi2"),
            title = cms.string(";Matched CandidateTrack #chi^{2}/ndf"),
            binsX = cms.untracked.vdouble(50, 0, 10),
            inputVariables = cms.vstring("matchedCandidateTrack.normalizedChi2")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackNHitsMissingOuterNotBest"),
            title = cms.string(";IsolatedTrack Missing Outer Hits;Matched CandidateTrack Missing Outer Hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingOuterHits", "matchedCandidateTrack.missingOuterHits_")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackNHitsMissingMiddleNotBest"),
            title = cms.string(";IsolatedTrack Missing Middle Hits;Matched CandidateTrack Missing Middle Hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingMiddleHits", "matchedCandidateTrack.missingMiddleHits_")
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackNHitsMissingInnerNotBest"),
            title = cms.string(";IsolatedTrack Missing Inner Hits;Matched CandidateTrack Missing Inner Hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingInnerHits", "matchedCandidateTrack.missingInnerHits_")
        ),
        #####################################################
        # Candidate Track vs Isolated Track Calo Histograms
        #####################################################
        #cand calo em VS iso calo em
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloJustEMVsIsoMatchedCaloJetEmEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetEmEnergy [GeV];CandidateTrack caloNewNoPUDRp5CentralCaloJustEM [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            binsY = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetEmEnergy", "matchedCandidateTrack.caloNewNoPUDRp5CentralCaloJustEm")
        ),
        #cand calo sum VS iso calo em
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloVsIsoMatchedCaloJetEmEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetEmEnergy [GeV];CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            binsY = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetEmEnergy", "matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        #cand calo had VS iso calo had
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloJustHadVsIsoMatchedCaloJetHadEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetHadEnergy [GeV];CandidateTrack caloNewNoPUDRp5CentralCaloJustHad [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            binsY = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetHadEnergy", "matchedCandidateTrack.caloNewNoPUDRp5CentralCaloJustHad")
        ),
        #cand calo sum VS iso calo had
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloVsIsoMatchedCaloJetHadEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetHadEnergy [GeV];CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            binsY = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetHadEnergy", "matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        #cand calo sum VS iso calo sum
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloVsIsoMatchedCaloJetEmPlusHadEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetEmPlusHadEnergy [GeV];CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            binsY = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetEmEnergy + matchedCaloJetHadEnergy", "matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        #single variable calo plots
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCalo"),
            title = cms.string(";CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloJustEm"),
            title = cms.string(";CandidateTrack caloNewNoPUDRp5CentralCaloJustEm [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCandidateTrack.caloNewNoPUDRp5CentralCaloJustEm")
        ),
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloJustHad"),
            title = cms.string(";CandidateTrack caloNewNoPUDRp5CentralCaloJustHad [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCandidateTrack.caloNewNoPUDRp5CentralCaloJustHad")
        ),
        cms.PSet (
            name = cms.string("IsoMatchedCaloJetEmPlusHadEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetEmPlusHadEnergy [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetEmEnergy + matchedCaloJetHadEnergy")
        ),
        cms.PSet (
            name = cms.string("IsoMatchedCaloJetEmEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetEmEnergy [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetEmEnergy")
        ),
        cms.PSet (
            name = cms.string("IsoMatchedCaloJetHadEnergy"),
            title = cms.string(";IsolatedTrack matchedCaloJetHadEnergy [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 40),
            inputVariables = cms.vstring("matchedCaloJetHadEnergy")
        ),

        #######################################################
        # Candidate Track Calo vs Isolated Track PF isolation
        #######################################################

        #cand hadron calo vs isoTrk PF neutral hadron isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloJustHadVsIsoTrkMatchedNeutralHadIso"),
            title = cms.string(";IsolatedTrack neutralHadIso [GeV];CandidateTrack caloNewNoPUDRp5CentralCaloJustHad [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.caloNewNoPUDRp5CentralCaloJustHad")
        ),
        #cand hadron+EM calo vs isoTrk PF neutral hadron isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloVsIsoTrkMatchedNeutralHadIso"),
            title = cms.string(";IsolatedTrack neutralHadIso [GeV];CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        #cand EM calo vs isoTrk PF photon isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloJustEMVsIsoTrkMatchedPhotonIso"),
            title = cms.string(";IsolatedTrack photonIso [GeV];CandidateTrack caloNewNoPUDRp5CentralCaloJustEM [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso", "matchedCandidateTrack.caloNewNoPUDRp5CentralCaloJustEm")
        ),
        #cand hadron+EM calo vs isoTrk PF photon isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloVsIsoTrkMatchedPhotonIso"),
            title = cms.string(";IsolatedTrack photonIso [GeV];CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso", "matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        #cand hadron+EM calo vs isoTrk PF photon + neutral had isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp5CentralCaloVsIsoTrkMatchedPhotonAndNeutralHadIso"),
            title = cms.string(";IsolatedTrack photonIso + neutralHadronIso [GeV];CandidateTrack caloNewNoPUDRp5CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso + pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.caloNewNoPUDRp5CentralCalo")
        ),
        
        #cone size of 0.3

        #cand hadron calo vs isoTrk PF neutral hadron isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp3CentralCaloJustHadVsIsoTrkMatchedNeutralHadIso"),
            title = cms.string(";IsolatedTrack neutralHadIso [GeV];CandidateTrack caloNewNoPUDRp3CentralCaloJustHad [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.caloNewNoPUDRp3CentralCaloJustHad")
        ),
        #cand hadron+EM calo vs isoTrk PF neutral hadron isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp3CentralCaloVsIsoTrkMatchedNeutralHadIso"),
            title = cms.string(";IsolatedTrack neutralHadIso [GeV];CandidateTrack caloNewNoPUDRp3CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.caloNewNoPUDRp3CentralCalo")
        ),
        #cand EM calo vs isoTrk PF photon isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp3CentralCaloJustEMVsIsoTrkMatchedPhotonIso"),
            title = cms.string(";IsolatedTrack photonIso [GeV];CandidateTrack caloNewNoPUDRp3CentralCaloJustEM [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso", "matchedCandidateTrack.caloNewNoPUDRp3CentralCaloJustEm")
        ),
        #cand hadron+EM calo vs isoTrk PF photon isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp3CentralCaloVsIsoTrkMatchedPhotonIso"),
            title = cms.string(";IsolatedTrack photonIso [GeV];CandidateTrack caloNewNoPUDRp3CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso", "matchedCandidateTrack.caloNewNoPUDRp3CentralCalo")
        ),
        #cand hadron+EM calo vs isoTrk PF photon + neutral had isolation
        cms.PSet (
            name = cms.string("candCaloNewNoPUDRp3CentralCaloVsIsoTrkMatchedPhotonAndNeutralHadIso"),
            title = cms.string(";IsolatedTrack photonIso + neutralHadronIso [GeV];CandidateTrack caloNewNoPUDRp3CentralCalo [GeV]"),
            binsX = cms.untracked.vdouble(400, 0, 16),
            binsY = cms.untracked.vdouble(400, 0, 16),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso + pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.caloNewNoPUDRp3CentralCalo")
        ),

        #####################################################
        # Candidate Track vs Isolated Track Isolation Histograms
        #####################################################
        cms.PSet (
            name = cms.string("candTrackIsoNoPUDRp3VsIsoPFChHadIso"),
            title = cms.string(";Isolated Track chargedHadronIso;CandidateTrack trackIso"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfIsolationDR03_.chargedHadronIso", "matchedCandidateTrack.trackIsoNoPUDRp3")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFChHadIso"),
            title = cms.string(";Isolated Track chargedHadronIso / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("pfIsolationDR03_.chargedHadronIso / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candTrackIsoNoPUDRp3VsIsoPFpuChHadIso"),
            title = cms.string(";Isolated Track puChargedHadronIso;CandidateTrack trackIso"),
            binsX = cms.untracked.vdouble(200, 0, 100),
            binsY = cms.untracked.vdouble(200, 0, 100),
            inputVariables = cms.vstring("pfIsolationDR03_.puChargedHadronIso", "matchedCandidateTrack.trackIsoNoPUDRp3")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFpuChHadIso"),
            title = cms.string(";Isolated Track puChargedHadronIso / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("pfIsolationDR03_.puChargedHadronIso / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candTrackIsoNoPUDRp3VsIsoPFSumChHadIso"),
            title = cms.string(";Isolated Track chargedHadronIso + puChargedHadronIso;CandidateTrack trackIso"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfIsolationDR03_.chargedHadronIso + pfIsolationDR03_.puChargedHadronIso", "matchedCandidateTrack.trackIsoNoPUDRp3")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFSumChHadIso"),
            title = cms.string(";Isolated Track (chargedHadronIso + puChargedHadronIso) / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("(pfIsolationDR03_.chargedHadronIso + pfIsolationDR03_.puChargedHadronIso) / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candTrackIsoNoPUDRp3VsIsoPFNeutChHadIso"),
            title = cms.string(";Isolated Track neutralHadronIso;CandidateTrack trackIso"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfIsolationDR03_.neutralHadronIso", "matchedCandidateTrack.trackIsoNoPUDRp3")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFNeutChHadIso"),
            title = cms.string(";Isolated Track (neutralHadronIso) / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("(pfIsolationDR03_.neutralHadronIso) / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candTrackIsoNoPUDRp3VsIsoPFPhotonIso"),
            title = cms.string(";Isolated Track photonIso;CandidateTrack trackIso"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfIsolationDR03_.photonIso", "matchedCandidateTrack.trackIsoNoPUDRp3")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFPhotonIso"),
            title = cms.string(";Isolated Track (photonIso) / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("(pfIsolationDR03_.photonIso) / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFTTotalIso"),
            title = cms.string(";Isolated Track (chargedHadronIso + puChargedHadronIso + neutralHadronIso + photonIso ) / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("(pfIsolationDR03_.chargedHadronIso + pfIsolationDR03_.puChargedHadronIso + pfIsolationDR03_.neutralHadronIso + pfIsolationDR03_.photonIso) / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("candTrackRelIsoNoPUDRp3VsIsoRelPFchHadneuHadPUIso"),
            title = cms.string(";Isolated Track (chargedHadronIso + puChargedHadronIso + neutralHadronIso ) / pt;CandidateTrack trackIso / pt"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("(pfIsolationDR03_.chargedHadronIso + pfIsolationDR03_.puChargedHadronIso + pfIsolationDR03_.neutralHadronIso) / pt", "matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt")
        ),
        cms.PSet (
            name = cms.string("isoTrackDRMinJet"),
            title = cms.string(";IsolatedTrack dRMinJet [GeV];"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("dRMinJet")           
        ),
        cms.PSet (
            name = cms.string("candTrackDeltaRToClosestElectronVsIsoTrackDeltaRToClosestPFElectron"),
            title = cms.string(";#DeltaR_{min}(track, PF muon);#DeltaR_{min}(track, PF charged hadron)"),
            binsX = cms.untracked.vdouble(1000, 0, 1),
            binsY = cms.untracked.vdouble(1000, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestPFElectron", "matchedCandidateTrack.deltaRToClosestElectron"),
        ),
    )
)

IsoTrackCandTrackEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("candVsIsoTrackD0WRTPV"),
            title = cms.string(";IsolatedTrack d_{0} (PV);Matched CandidateTrack d_{0} (PV)"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            binsY = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("track.dxy", trackD0WRTPV.replace("track.", "track.matchedCandidateTrack."))
        ),
        cms.PSet (
            name = cms.string("candVsIsoTrackDZWRTPV"),
            title = cms.string(";IsolatedTrack d_{z} (PV);Matched CandidateTrack d_{z} (PV)"),
            binsX = cms.untracked.vdouble(60, -30, 30),
            binsY = cms.untracked.vdouble(60, -30, 30),
            inputVariables = cms.vstring("track.dz", trackDZWRTPV.replace("track.", "track.matchedCandidateTrack.")),
        ),
    )
)
