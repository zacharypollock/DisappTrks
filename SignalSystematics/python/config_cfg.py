from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon ISR study channels (to get weights)
################################################################################
# Base skim
#  add_channels  (process,  [ZtoMuMu],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  True)

# Channels for zToMuMu for isr weights calculation
#  add_channels  (process,  [ZtoMuMuISRStudy],       histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
#  add_channels  (process,  [ZtoMuMuISRStudyJet30],  histSetsMuon,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# SingleMuon channel for Ecalo systematic
################################################################################
#  add_channels  (process,  [ZtoMuMuDisTrkNHits4NoECaloCut],  histSets,  weightsWithMuonSF,  scaleFactorProducersWithMuons,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# AMSB signal channels (to get systematic fluctuations)
################################################################################
# Central value channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# Pileup systematic channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weightsFluctuatePileup,  scaleFactorProducers,  collMap,  variableProducers,  False)

# MET systematic channels
#  histSets.append(MetShiftHistograms)
#  add_channels  (process,  [disTrkNoMet],             histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoMetSmearedJets],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# JEC systematic channels
#  add_channels  (process,  [disTrkSelectionJECUp,             disTrkSelectionJECDown],             histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJetsJECUp,  disTrkSelectionSmearedJetsJECDown],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# JER systematic channels
#  add_channels  (process,  [disTrkSelectionSmearedJetsUp,  disTrkSelectionSmearedJetsDown],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

# ISR systematic channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weightsFluctuateISR,  scaleFactorProducers,  collMap,  variableProducers,  False)

# Trigger efficiency channels
#  add_channels  (process,  [disTrkSelection],             histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionSmearedJets],  histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)

# Number of missing outer hits channel
#  add_channels  (process,  [disTrkNoNMissOut],  histSets,  weightsFluctuateTrigger,  scaleFactorProducers,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# MET channels for missing inner/middle/outer hits systematics
################################################################################
# Channels used for the missing inner/middle/outer hits systematics
#  add_channels  (process,  [hitsSystematicsCtrlSelection],  histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelection],             histSets,  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)
################################################################################

################################################################################
# MET channels for Checking 2017 Luminosity
################################################################################

#add_channels (process, [metTrigJustMain, metTrigOnlyPerfectNoMain2017, metTrigOnlyPerfectAndMain2017, metTrigAllUnprescaled2017, metTrigAllowDisabledHighPU2017], [histSets,histSetsTrigger],  weights,  scaleFactorProducers,  collMap,  variableProducers,  False)

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
