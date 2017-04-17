import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.Triggers import *
import os

def customize (process, runPeriod, applyPUReweighting = True, applyTriggerReweighting = True):

    if runPeriod == "2015":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2015")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.string('SingleMu_2015D')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_2015D.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2015D')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2015_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2015_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2015")

    elif runPeriod == "2016BC":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_BC")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.string('SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016BC')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016BC")

    elif runPeriod == "2016DEFGH":
        process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_DEFGH")

        process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.string('SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

        process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFGH')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016DEFGH")

    if not applyPUReweighting:
        process.PUScalingFactorProducer.PU     = cms.string ("")
        process.PUScalingFactorProducer.target = cms.string ("")

    if not applyTriggerReweighting:
        process.TriggerWeightProducer.efficiencyFile  =  cms.string  ("")
        process.TriggerWeightProducer.dataset         =  cms.string  ("")
        process.TriggerWeightProducer.target          =  cms.string  ("")

    moveVariableProducer (process, "TriggerWeightProducer")
    process.schedule.insert (0, process.metFilterPath)

    return process
