# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step1 --filein file:EXO-RunIIFall15DR76-02578.root --fileout file:AMSB_chargino_step4.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 76X_mcRun2_asymptotic_v12 --step PAT --era Run2_25ns --python_filename AMSB_chargino_step4.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring,DisappTrks/SignalMC/genParticlePlusGeant.customizeKeep,DisappTrks/SignalMC/recoCollectionsToKeep.customize -n 1786
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

import OSUT3Analysis.DBTools.osusub_cfg as osusub
import re
import os

def addSecondaryFileFromSkim (fileName):
    parents = []
    fileName = fileName.rstrip ('\n')
    fileName = re.sub (r'^file:', r'', fileName)
    if not os.path.isfile (fileName):
      return parents

    jobNumber = re.sub (r'.*/[^/]*_([^/_]*)\.root$', r'\1', fileName)
    parentDir = re.sub (r'(.*)/[^/]*\.root$', r'\1/', fileName)
    condorErr = open (parentDir + "condor_" + jobNumber + ".err")
    for line in condorErr:
        if re.search (r'Successfully opened file', line) and not re.search (r'MinBias', line):
            p = re.sub (r'.* Successfully opened file (.*)', r'\1', line)
            p = p.rstrip ('\n')
            if not p in parents:
                parents.append (p)

    return sorted (list (set (parents)))

def addSecondaryFile (fileName):
    parents = []
    fileName = fileName.rstrip ('\n')
    skimParents = addSecondaryFileFromSkim (fileName)
    for p in skimParents:
      if re.search (r'_step1_', p):
        parents.append (p)
      else:
        parents += addSecondaryFile (p)

    return parents

def addSecondaryFiles (source):
    parents = []
    fileNames = source.fileNames
    if osusub.batchMode:
        fileNames = osusub.runList
    for fileName in fileNames:
        parents += addSecondaryFile (fileName)

    source.secondaryFileNames = cms.untracked.vstring (parents)

process = cms.Process('PAT',eras.Run2_25ns)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1786)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:EXO-RunIIFall15DR76-02578.root'),
    secondaryFileNames = cms.untracked.vstring()
)
addSecondaryFiles (process.source)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1786'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:AMSB_chargino_step4.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_v12', '')

process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
process.candidateTracks = cms.Path(process.candidateTrackProducer)
from DisappTrks.CandidateTrackProducer.customize import disappTrksOutputCommands
process.MINIAODSIMoutput.outputCommands.extend(disappTrksOutputCommands)

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.candidateTracks,process.endjob_step,process.MINIAODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from DisappTrks.SignalMC.genParticlePlusGeant
from DisappTrks.SignalMC.genParticlePlusGeant import customizeKeep

#call to customisation function customizeKeep imported from DisappTrks.SignalMC.genParticlePlusGeant
process = customizeKeep(process)

# Automatic addition of the customisation function from DisappTrks.SignalMC.recoCollectionsToKeep
from DisappTrks.SignalMC.recoCollectionsToKeep import customize

#call to customisation function customize imported from DisappTrks.SignalMC.recoCollectionsToKeep
process = customize(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# Automatic addition of the customisation function from DisappTrks.SignalMC.genParticlePlusGeant
from DisappTrks.SignalMC.genParticlePlusGeant import customizeMiniAOD

#call to customisation function customizeKeep imported from DisappTrks.SignalMC.genParticlePlusGeant
process = customizeMiniAOD(process)

# End of customisation functions
