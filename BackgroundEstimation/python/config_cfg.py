from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################

# Descendents of BasicSelection

# fakeTrackBackground_d0sideband
if False:
    add_channels  (process,  [disTrkSelectionNoD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionNoD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionNoD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionNoD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

if False:
    add_channels  (process,  [disTrkSelectionSidebandD0Cut],        histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionSidebandD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

# Testing: similar to sideband above, but without upper D0 cut
if False:
    add_channels  (process,  [disTrkSelectionInvertD0Cut],        histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits3],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits4],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits5],  histSets,        weights,  [],  collMap,  variableProducers,  False)
    add_channels  (process,  [disTrkSelectionInvertD0CutNHits6],  histSets,        weights,  [],  collMap,  variableProducers,  False)

################################################################################
# SingleElectron channels
################################################################################
# Base skim
#  add_channels  (process,  [ElectronTagSkim],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)

# Tag-and-probe channels for fiducial map
#  add_channels  (process,  [ElectronFiducialCalcBefore],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronFiducialCalcAfter],   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)

# Tag-and-probe channels for electron background estimate
# Tag-and-probe channels for electron background estimate
#  add_channels  (process,  [ZtoEleProbeTrk],                   histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer,  False)
#  add_channels  (process,  [ZtoEleProbeTrkWithFilter],         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer,  True)
#  add_channels  (process,  [ZtoEleProbeTrkWithSSFilter],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronTPProducer,  True)
#  add_channels  (process,  [ZtoEleProbeTrkBeforeArbitration],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                       False)
#  add_channels  (process,  [ZtoEleProbeTrkWithZCuts],          histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                       False)
#  add_channels  (process,  [ZtoEleDisTrk],                     histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                       True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToEleProbeTrk],                       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer,  False)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithFilter],             histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer,  True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithSSFilter],           histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + tauToElectronTPProducer,  True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCuts],              histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                            False)
#  add_channels  (process,  [ZtoTauToEleDisTrk],                         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                            True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsBetterPurity],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                            False)
#  add_channels  (process,  [ZtoTauToEleDisTrkBetterPurity],             histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                            True)


# Single electron control regions
#  add_channels  (process,  [ElectronTagPt55],         histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers + electronMETTriggerProducer,  False)
#  add_channels  (process,  [ElectronTagPt55MetTrig],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,                               False)

# Z->ee control region
#  add_channels  (process,  [ZtoEE],                           histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0Cut],              histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits3],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits4],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits5],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkNoD0CutNHits6],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0Cut],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits3],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits4],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits5],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEEDisTrkSidebandD0CutNHits6],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)

# Channels for doing the lepton background estimates with fewer numbers of hits
#  add_channels  (process,  [ElectronTagPt55NoValidHitsCut],               histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ElectronTagPt55MetTrigNoValidHitsCut],        histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoEleProbeTrkWithZCutsNoValidHitsCut],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)

#  add_channels  (process,  [ZtoEleDisTrkNHits3],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEleDisTrkNHits4],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEleDisTrkNHits5],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEleDisTrkNHits6],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits3],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits4],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits5],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToEleDisTrkNHits6],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  True)

# Tag-and-probe channels without d0 cut on probe track
#  add_channels  (process,  [ZtoEleProbeTrkWithoutD0Cut],       histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToEleProbeTrkWithoutD0Cut],  histSetsElectron,  weightsWithEleSF,  scaleFactorProducersWithElectrons,  collMap,  variableProducers,  False)

################################################################################

################################################################################
# SingleMuon channels
################################################################################
# Base skim and ZtoMuMu
#  add_channels  (process,  [MuonTagSkim],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

# Tag-and-probe channels for fiducial map
#  add_channels  (process,  [MuonFiducialCalcBefore],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [MuonFiducialCalcAfter],   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# Tag-and-probe channels for muon background estimate
#  add_channels  (process,  [ZtoMuDummyTrk],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer,  False)
#  add_channels  (process,  [ZtoMuDummyTrkWithJetFilter],      histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer,  True)
#  add_channels  (process,  [ZtoMuProbeTrk],                   histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer,  False)
#  add_channels  (process,  [ZtoMuProbeTrkWithFilter],         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer,  True)
#  add_channels  (process,  [ZtoMuProbeTrkWithSSFilter],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonTPProducer,  True)
#  add_channels  (process,  [ZtoMuProbeTrkBeforeArbitration],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                   False)
#  add_channels  (process,  [ZtoMuProbeTrkWithZCuts],          histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                   False)
#  add_channels  (process,  [ZtoMuDisTrk],                     histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                   True)

# Tag-and-probe channels for tau background estimate
#  add_channels  (process,  [ZtoTauToMuProbeTrk],                       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer,  False)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithFilter],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer,  True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithSSFilter],           histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + tauToMuonTPProducer,  True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCuts],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                        False)
#  add_channels  (process,  [ZtoTauToMuDisTrk],                         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                        True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsBetterPurity],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                        False)
#  add_channels  (process,  [ZtoTauToMuDisTrkBetterPurity],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                        True)

# Single muon control regions
#  add_channels  (process,  [MuonTagPt55],         histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers + muonMETTriggerProducer,  False)
#  add_channels  (process,  [MuonTagPt55MetTrig],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,                           False)

# Z->mumu channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMu],                        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
if False:
    add_channels  (process,  [ZtoMuMuCandTrk],                 histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrk],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
    add_channels  (process,  [ZtoMuMuDisTrkNHits3],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkNHits4],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkNHits5],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkNHits6],            histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with no D0 requirement on the isoTrk
if False:
    add_channels  (process,  [ZtoMuMuDisTrkNoD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkNoD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with loosened D0 requirement on the isoTrk
if False:
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkSidebandD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: Z->mumu channels for fake track background estimate with inverted D0 requirement on the isoTrk
if False:
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits3], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits4], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits5], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
    add_channels  (process,  [ZtoMuMuDisTrkInvertD0CutNHits6], histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: Z->mumu+jet channels for fake track background estimate
#  add_channels  (process,  [ZtoMuMuJet],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrkJet],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits3Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits5Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuDisTrkNHits6Jet],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: Z->mumu+jet channels for fake track background estimate with one jet and ==16 PV
#  add_channels  (process,  [ZtoMuMuOneJet14to18PV],             histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers, False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuOneJet14to18PVDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: W->munu for fake track background estimate
#  add_channels  (process,  [WtoMuNu],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: W->munu for fake track background estimate with one jet and ==16 PV
#  add_channels  (process,  [WtoMuNuOneJet14to18PV],              histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrk],        histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [WtoMuNuOneJet14to18PVDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

# TESTING: Z->mumu channels with relaxed missing outer hits requirements
#  add_channels  (process,  [ZtoMuMuDisTrk2],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMuDisTrk1],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

# Channels for doing the lepton background estimates with fewer numbers of hits
#  add_channels  (process,  [MuonTagPt55NoValidHitsCut],                  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [MuonTagPt55MetTrigNoValidHitsCut],           histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuProbeTrkWithZCutsNoValidHitsCut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

#  add_channels  (process,  [ZtoMuDisTrkNHits3],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuDisTrkNHits4],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuDisTrkNHits5],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuDisTrkNHits6],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits3],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits4],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits5],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauToMuDisTrkNHits6],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

# Tag-and-probe channels without d0 cut on probe track
#  add_channels  (process,  [ZtoMuProbeTrkWithoutD0Cut],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoTauToMuProbeTrkWithoutD0Cut],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)

################################################################################

################################################################################
# Tau channels
################################################################################
# Base skim
#  add_channels  (process,  [TauTagSkim],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  True)

# Single tau control regions
#  add_channels  (process,  [TauTagPt55],         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers + tauMETTriggerProducer,  False)
#  add_channels  (process,  [TauTagPt55MetTrig],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,                          False)

# Channels for doing the lepton background estimates with fewer numbers of hits
#  add_channels  (process,  [TauTagPt55NoValidHitsCut],         histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [TauTagPt55MetTrigNoValidHitsCut],  histSetsTau,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# ZeroBias channels
################################################################################
#  add_channels  (process,  [zeroBiasSelection],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  True)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits3],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits4],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits5],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasSelectionDisTrkNHits6],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

#  add_channels  (process,  [zeroBiasJetSelection],              histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits3],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits4],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits5],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [zeroBiasJetSelectionDisTrkNHits6],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# Testing channels to compare pat::IsolatedTracks to CandidateTracks
################################################################################
#  add_channels  (process,  [MinimalMuonTrackSelection],                 cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)
#  add_channels  (process,  [MinimalMuonMatchedCandidateTrackSelection], cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)

#  add_channels  (process,  [MinimalEleTrackSelection],                  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)
#  add_channels  (process,  [MinimalEleMatchedCandidateTrackSelection],  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)

#  add_channels  (process,  [MinimalTauTrackSelection],                  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)
#  add_channels  (process,  [MinimalTauMatchedCandidateTrackSelection],  cms.VPSet(IsolatedTrackCandidateTrackHistograms), weights, scaleFactorProducers, collMap, variableProducers, False)
################################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
