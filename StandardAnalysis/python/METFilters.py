import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
import os

# MET filters recommended for Moriond 2017 here:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2017
metFilters = cms.vstring ([
  "Flag_goodVertices",
  "Flag_globalTightHalo2016Filter",
  "Flag_HBHENoiseFilter",
  "Flag_HBHENoiseIsoFilter",
  "Flag_EcalDeadCellTriggerPrimitiveFilter",
])

if osusub.batchMode and types[osusub.datasetLabel] == "data":
  metFilters.append (
    "Flag_eeBadScFilter",
  )
