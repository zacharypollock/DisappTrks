#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.fakeEstimateTest import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import gROOT, TFile, TGraphAsymmErrors

gROOT.SetBatch () # I am Groot.

dirs = getUser()

runPeriods = ['BC', 'DEFGH', '']

stdout = sys.stdout
nullout = open ("/dev/null", "w")
sys.stdout = nullout

N = 5
A = 0.02
B = 0.1
D = (B - A) / N

try:
  os.unlink ("fakeTrackEstimateVsD0.root")
except OSError:
  pass

for runPeriod in runPeriods:

    g0 = TGraphAsymmErrors (N)
    g1 = TGraphAsymmErrors (N)

    maxFluctuationDown = 0.0
    maxFluctuationUp = 0.0

    nominal = 0.0

    for i in range (0, N):
        minD0 = A + i * D

        sys.stdout = stdout
        print "minimum |d0|: " + str (minD0) + " cm"
        sys.stdout = nullout

        fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
        fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        fakeTrackBkgdEstimate.addMinD0 (minD0)
        fakeTrackBkgdEstimate.addChannel  ("Basic3hits",            "DisTrkSelectionNoD0CutNHits3",        "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",        "DisTrkSelectionSidebandD0Cut",        "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits3",  "DisTrkSelectionSidebandD0CutNHits3",  "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits4",  "DisTrkSelectionSidebandD0CutNHits4",  "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits5",  "DisTrkSelectionSidebandD0CutNHits5",  "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0NHits6",  "DisTrkSelectionSidebandD0CutNHits6",  "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("Basic",                 "BasicSelection",                      "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/basicSelection_new")

        nEst = fakeTrackBkgdEstimate.printNest ()

        g0.SetPoint (i, minD0, nEst.centralValue ())
        g0.SetPointError (i, D / 2.0, D / 2.0, min (nEst.maxUncertainty (), nEst.centralValue ()), nEst.maxUncertainty ())

        if i > 0:
          if nEst.centralValue () < nominal:
            maxFluctuationDown = max (maxFluctuationDown, nominal - nEst.centralValue ())
          else:
            maxFluctuationUp = max (maxFluctuationUp, nEst.centralValue () - nominal)

        zToMuMuEstimate = FakeTrackBkgdEstimate ()
        zToMuMuEstimate.addLuminosityInInvPb (lumi["SingleMuon_2016" + runPeriod])
        zToMuMuEstimate.addMinD0 (minD0)
        zToMuMuEstimate.addChannel  ("Basic3hits",            "ZtoMuMuDisTrkNoD0CutNHits3",        "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0",        "ZtoMuMuDisTrkSidebandD0Cut",        "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits3",  "ZtoMuMuDisTrkSidebandD0CutNHits3",  "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits4",  "ZtoMuMuDisTrkSidebandD0CutNHits4",  "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits5",  "ZtoMuMuDisTrkSidebandD0CutNHits5",  "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0NHits6",  "ZtoMuMuDisTrkSidebandD0CutNHits6",  "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("Basic",                 "BasicSelection",                    "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/basicSelection_new")
        zToMuMuEstimate.addChannel  ("ZtoLL",                 "ZtoMuMu",                           "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu_new")

        nEst = zToMuMuEstimate.printNest ()

        g1.SetPoint (i, minD0, nEst.centralValue ())
        g1.SetPointError (i, D / 2.0, D / 2.0, min (nEst.maxUncertainty (), nEst.centralValue ()), nEst.maxUncertainty ())

        if i == 0:
          nominal = nEst.centralValue ()
        else:
          if nEst.centralValue () < nominal:
            maxFluctuationDown = max (maxFluctuationDown, nominal - nEst.centralValue ())
          else:
            maxFluctuationUp = max (maxFluctuationUp, nEst.centralValue () - nominal)

    sys.stdout = stdout
    print "[2016" + runPeriod + "] systematic uncertainty: - " + str (maxFluctuationDown) + " + " + str (maxFluctuationUp) + " (- " + str ((maxFluctuationDown / nominal) * 100.0) + " + " + str ((maxFluctuationUp / nominal) * 100.0) + ")%"
    sys.stdout = nullout

    fout = TFile ("fakeTrackEstimateVsD0.root", "update")
    fout.cd ()
    g0.Write ("est_BasicSelection_2016" + runPeriod)
    g1.Write ("est_ZtoMuMu_2016" + runPeriod)
    fout.Close ()
