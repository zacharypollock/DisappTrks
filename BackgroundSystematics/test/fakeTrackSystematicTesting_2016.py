#!/usr/bin/env python

import math
from DisappTrks.BackgroundSystematics.bkgdSystematics import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import TCanvas, TFile
import os

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

useJetRequirementForFakes = False

# '' will gives you Dataset_2016.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['BC', 'DEFG', 'DEFGH', 'H', '']

if background == "FAKE" or background == "ALL":

    print "********************************************************************************"
    print "evaluating fake track systematic without MET75_IsoTrk50 (2016)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackSystematicNoMET75_2016.root", "recreate")

    fakeTrackSystematicNoMET75 = FakeTrackSystematic ()
    fakeTrackSystematicNoMET75.addTFile (fout)
    fakeTrackSystematicNoMET75.addTCanvas (canvas)
    fakeTrackSystematicNoMET75.addLuminosityLabel (str (round (lumi["MET_2016"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    fakeTrackSystematicNoMET75.addChannel  ("Basic",                "BasicSelection",         "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_noMET75_new")
    fakeTrackSystematicNoMET75.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_noMET75_new")
    fakeTrackSystematicNoMET75.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_noMET75_new")
    fakeTrackSystematicNoMET75.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_noMET75_new")
    fakeTrackSystematicNoMET75.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_noMET75_new")
    fakeTrackSystematicNoMET75.reweightTo  ("MET_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_noMET75_new",  "BasicSelection",  "Eventvariable Plots/nTracks")
    fakeTrackSystematicNoMET75.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_hist")
    fakeTrackSystematicNoMET75.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_hist")
    fakeTrackSystematicNoMET75.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_hist")
    fakeTrackSystematicNoMET75.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_hist")
    fakeTrackSystematicNoMET75.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_hist")

    print "********************************************************************************"

    fakeTrackSystematicNoMET75.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with lower track pt threshold (2016)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("fakeTrackSystematicTrkPt30_2016.root", "recreate")

    fakeTrackSystematicTrkPt30 = FakeTrackSystematic ()
    fakeTrackSystematicTrkPt30.addTFile (fout)
    fakeTrackSystematicTrkPt30.addTCanvas (canvas)
    fakeTrackSystematicTrkPt30.addLuminosityLabel (str (round (lumi["MET_2016"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    fakeTrackSystematicTrkPt30.addChannel  ("Basic",                "BasicSelection",         "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_hist")
    fakeTrackSystematicTrkPt30.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_trkPt30")
    fakeTrackSystematicTrkPt30.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_trkPt30")
    fakeTrackSystematicTrkPt30.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_trkPt30")
    fakeTrackSystematicTrkPt30.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016",       dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_trkPt30")
    fakeTrackSystematicTrkPt30.reweightTo  ("MET_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_hist",  "BasicSelection",  "Eventvariable Plots/nTracks")
    fakeTrackSystematicTrkPt30.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_hist")
    fakeTrackSystematicTrkPt30.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_trkPt30")
    fakeTrackSystematicTrkPt30.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_trkPt30")
    fakeTrackSystematicTrkPt30.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_trkPt30")
    fakeTrackSystematicTrkPt30.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_trkPt30")

    print "********************************************************************************"

    fakeTrackSystematicTrkPt30.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic in MC with nTracks reweighting"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("mcNTracksReweightedFakeTrackSystematic" + ".root", "recreate")

    mcNTracksReweightedFakeTrackSystematic = FakeTrackSystematic ()
    mcNTracksReweightedFakeTrackSystematic.addTFile (fout)
    mcNTracksReweightedFakeTrackSystematic.addTCanvas (canvas)
    mcNTracksReweightedFakeTrackSystematic.addLuminosityLabel ("13 TeV")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("Basic",         "JustAVertex",        "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "JustADisTrkNHits3",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "JustADisTrkNHits4",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "JustADisTrkNHits5",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "JustADisTrkNHits6",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.reweightTo  ("TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho",  "JustAVertex",  "Eventvariable Plots/nTracks")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("ZtoLL",                "JustAVertex",        "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "JustADisTrkNHits3",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "JustADisTrkNHits4",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "JustADisTrkNHits5",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcNTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "JustADisTrkNHits6",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")

    print "********************************************************************************"

    mcNTracksReweightedFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic in MC with trackRho reweighting"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("mcTrackRhoReweightedFakeTrackSystematic" + ".root", "recreate")

    mcTrackRhoReweightedFakeTrackSystematic = FakeTrackSystematic ()
    mcTrackRhoReweightedFakeTrackSystematic.addTFile (fout)
    mcTrackRhoReweightedFakeTrackSystematic.addTCanvas (canvas)
    mcTrackRhoReweightedFakeTrackSystematic.addLuminosityLabel ("13 TeV")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("Basic",         "JustAVertex",        "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "JustADisTrkNHits3",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "JustADisTrkNHits4",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "JustADisTrkNHits5",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "JustADisTrkNHits6",  "TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.reweightTo  ("TTJets",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho",  "JustAVertex",  "Eventvariable Plots/trackRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("ZtoLL",                "JustAVertex",        "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "JustADisTrkNHits3",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "JustADisTrkNHits4",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "JustADisTrkNHits5",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTrackRhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "JustADisTrkNHits6",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")

    print "********************************************************************************"

    mcTrackRhoReweightedFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic in MC"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("mcFakeTrackSystematic" + ".root", "recreate")

    mcFakeTrackSystematic = FakeTrackSystematic ()
    mcFakeTrackSystematic.addTFile (fout)
    mcFakeTrackSystematic.addTCanvas (canvas)
    mcFakeTrackSystematic.addLuminosityLabel ("13 TeV")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "JustADisTrkNHits3",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "JustADisTrkNHits4",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "JustADisTrkNHits5",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "JustADisTrkNHits6",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "JustADisTrkNHits3",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "JustADisTrkNHits4",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "JustADisTrkNHits5",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "JustADisTrkNHits6",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")

    print "********************************************************************************"

    mcFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic in MC truth"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("mcTruthFakeTrackSystematic" + ".root", "recreate")

    mcTruthFakeTrackSystematic = FakeTrackSystematic ()
    mcTruthFakeTrackSystematic.addTFile (fout)
    mcTruthFakeTrackSystematic.addTCanvas (canvas)
    mcTruthFakeTrackSystematic.addLuminosityLabel ("13 TeV")
    mcTruthFakeTrackSystematic.getTruthFakeRate (True)
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "JustADisTrkNHits3",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "JustADisTrkNHits4",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "JustADisTrkNHits5",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "JustADisTrkNHits6",  "TTJets",         dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "JustADisTrkNHits3",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "JustADisTrkNHits4",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "JustADisTrkNHits5",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")
    mcTruthFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "JustADisTrkNHits6",  "DYJetsToLL_50",  dirs['Andrew']+"2015/fakeTrackProbabilityComparisonWithRho")

    print "********************************************************************************"

    mcTruthFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with nTracks reweighting"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("nTracksReweightedFakeTrackSystematic_2016H" + ".root", "recreate")

    nTracksReweightedFakeTrackSystematic = FakeTrackSystematic ()
    nTracksReweightedFakeTrackSystematic.addTFile (fout)
    nTracksReweightedFakeTrackSystematic.addTCanvas (canvas)
    nTracksReweightedFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    nTracksReweightedFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    nTracksReweightedFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest",  "BasicSelection",  "Eventvariable Plots/nTracks")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    nTracksReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")

    print "********************************************************************************"

    nTracksReweightedFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with trackRho reweighting"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("rhoReweightedFakeTrackSystematic_2016H" + ".root", "recreate")

    rhoReweightedFakeTrackSystematic = FakeTrackSystematic ()
    rhoReweightedFakeTrackSystematic.addTFile (fout)
    rhoReweightedFakeTrackSystematic.addTCanvas (canvas)
    rhoReweightedFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    rhoReweightedFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest")
    rhoReweightedFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTest",  "BasicSelection",  "Eventvariable Plots/trackRho")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")
    rhoReweightedFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTest")

    print "********************************************************************************"

    rhoReweightedFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with nTracks reweighting with lost tracks"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("nTracksReweightedWithLostTracksFakeTrackSystematic_2016H" + ".root", "recreate")

    nTracksReweightedWithLostTracksFakeTrackSystematic = FakeTrackSystematic ()
    nTracksReweightedWithLostTracksFakeTrackSystematic.addTFile (fout)
    nTracksReweightedWithLostTracksFakeTrackSystematic.addTCanvas (canvas)
    nTracksReweightedWithLostTracksFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks",  "BasicSelection",  "Eventvariable Plots/nTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    nTracksReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")

    print "********************************************************************************"

    nTracksReweightedWithLostTracksFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with trackRho reweighting with lost tracks"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("rhoReweightedWithLostTracksFakeTrackSystematic_2016H" + ".root", "recreate")

    rhoReweightedWithLostTracksFakeTrackSystematic = FakeTrackSystematic ()
    rhoReweightedWithLostTracksFakeTrackSystematic.addTFile (fout)
    rhoReweightedWithLostTracksFakeTrackSystematic.addTCanvas (canvas)
    rhoReweightedWithLostTracksFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016H"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("Basic",         "BasicSelection",         "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits3",  "DisTrkSelectionNHits3",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits4",  "DisTrkSelectionNHits4",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits5",  "DisTrkSelectionNHits5",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("DisTrkNHits6",  "DisTrkSelectionNHits6",  "MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.reweightTo  ("MET_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematicTestWithLostTracks",  "BasicSelection",  "Eventvariable Plots/trackRho")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",              "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")
    rhoReweightedWithLostTracksFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",  "SingleMu_2016H",  dirs['Andrew']+"2016_final_prompt/fakeTrackBackgroundTestWithLostTracks")

    print "********************************************************************************"

    rhoReweightedWithLostTracksFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with ZeroBias data (2016D)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("zeroBiasFakeTrackSystematic_2016D" + ".root", "recreate")

    zeroBiasFakeTrackSystematic = FakeTrackSystematic ()
    zeroBiasFakeTrackSystematic.addTFile (fout)
    zeroBiasFakeTrackSystematic.addTCanvas (canvas)
    zeroBiasFakeTrackSystematic.addLuminosityLabel (str (round (lumi["ZeroBias_2016D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    zeroBiasFakeTrackSystematic.addChannel  ("Basic",                "ZeroBiasSelection",        "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBias")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "ZeroBiasSelectionNHits3",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "ZeroBiasSelectionNHits4",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "ZeroBiasSelectionNHits5",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "ZeroBiasSelectionNHits6",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasDisTrk")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                  "SingleMu_2016D",  dirs['Andrew']+"2016/zToMuMu_noSkim")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",      "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")

    print "********************************************************************************"

    zeroBiasFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    print "********************************************************************************"
    print "evaluating fake track systematic with ZeroBias data with jet cut (2016D)"
    print "--------------------------------------------------------------------------------"

    fout = TFile.Open ("zeroBiasJetFakeTrackSystematic_2016D" + ".root", "recreate")

    zeroBiasJetFakeTrackSystematic = FakeTrackSystematic ()
    zeroBiasJetFakeTrackSystematic.addTFile (fout)
    zeroBiasJetFakeTrackSystematic.addTCanvas (canvas)
    zeroBiasJetFakeTrackSystematic.addLuminosityLabel (str (round (lumi["ZeroBias_2016D"] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
    zeroBiasJetFakeTrackSystematic.addChannel  ("Basic",                "ZeroBiasJetSelection",        "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "ZeroBiasJetSelectionNHits3",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "ZeroBiasJetSelectionNHits4",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "ZeroBiasJetSelectionNHits5",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "ZeroBiasJetSelectionNHits6",  "ZeroBias_2016D",  dirs['Andrew']+"2016/zeroBiasJetDisTrk")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                     "SingleMu_2016D",  dirs['Andrew']+"2016/zToMuMu_noSkim")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")
    zeroBiasJetFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",         "SingleMu_2016D",  dirs['Andrew']+"2016/fakeTrackBackground")

    print "********************************************************************************"

    zeroBiasJetFakeTrackSystematic.printSystematic ()

    print "********************************************************************************"

    fout.Close ()

    print "\n\n"

    for runPeriod in runPeriods:

        print "*************************************************************************************"
        print "evaluating fake track systematic in data with D0 cut inverted (2016", runPeriod, ")"
        print "-------------------------------------------------------------------------------------"

        fout = TFile.Open ("invertD0CutFakeTrackSystematic" + runPeriod + ".root", "recreate")

        invertD0CutFakeTrackSystematic = FakeTrackSystematic ()
        invertD0CutFakeTrackSystematic.addTFile (fout)
        invertD0CutFakeTrackSystematic.addTCanvas (canvas)
        invertD0CutFakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        invertD0CutFakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",               "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/basicSelection")
        invertD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionInvertD0CutNHits3", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/fakeBkgd_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionInvertD0CutNHits4", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/fakeBkgd_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionInvertD0CutNHits5", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/fakeBkgd_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionInvertD0CutNHits6", "MET_2016" + runPeriod,       dirs['Brian']+"2016_final/fakeBkgd_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                      "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu")
        invertD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkInvertD0CutNHits3",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeSyst_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkInvertD0CutNHits4",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeSyst_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkInvertD0CutNHits5",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeSyst_d0sideband")
        invertD0CutFakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkInvertD0CutNHits6",   "SingleMu_2016" + runPeriod,  dirs['Brian']+"2016_final/fakeSyst_d0sideband")

        print "********************************************************************************"

        invertD0CutFakeTrackSystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

        print "********************************************************************************"
        print "evaluating fake track systematic with 1 jet, 16 PV (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackSystematicOneJet14to18PV_2016" + runPeriod + ".root", "recreate")

        fakeTrackSystematicOneJet14to18PV = FakeTrackSystematic ()
        fakeTrackSystematicOneJet14to18PV.addTFile (fout)
        fakeTrackSystematicOneJet14to18PV.addTCanvas (canvas)
        fakeTrackSystematicOneJet14to18PV.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("Basic",                "BasicSelection",                   "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits3",         "DisTrkSelectionOneJet14to18PVNHits3",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits4",         "DisTrkSelectionOneJet14to18PVNHits4",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits5",         "DisTrkSelectionOneJet14to18PVNHits5",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("DisTrkNHits6",         "DisTrkSelectionOneJet14to18PVNHits6",  "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final/basicSelectionOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoLL",                "ZtoMuMuOneJet14to18PV",                "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuOneJet14to18PVDisTrkNHits3",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuOneJet14to18PVDisTrkNHits4",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuOneJet14to18PVDisTrkNHits5",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")
        fakeTrackSystematicOneJet14to18PV.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuOneJet14to18PVDisTrkNHits6",    "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final/ZtoMuMuOneJet14to18PV")

        print "********************************************************************************"

        fakeTrackSystematicOneJet14to18PV.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if useJetRequirementForFakes:

        for runPeriod in runPeriods:

            print "********************************************************************************"
            print "evaluating fake track systematic with jet requirement (2016", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open ("fakeTrackSystematicWithJet_2016" + runPeriod + ".root", "recreate")

            fakeTrackSystematicWithJet = FakeTrackSystematic ()
            fakeTrackSystematicWithJet.addTFile (fout)
            fakeTrackSystematicWithJet.addTCanvas (canvas)
            fakeTrackSystematicWithJet.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
            fakeTrackSystematicWithJet.addChannel  ("Basic",                "BasicSelection",          "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final/basicSelection")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",   "MET_2016" + runPeriod,       dirs['Brian']+"2016_rereco/fakeTrackSystematics_v2")
            fakeTrackSystematicWithJet.addChannel  ("ZtoLL",                "ZtoMuMuJet",              "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")
            fakeTrackSystematicWithJet.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6Jet",  "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackgroundWithJet")

            print "********************************************************************************"

            fakeTrackSystematicWithJet.printSystematic ()

            print "********************************************************************************"

            fout.Close ()

            print "\n\n"

    for runPeriod in runPeriods:

        print "********************************************************************************"
        print "evaluating fake track systematic without 3 pixel hits cut (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackSystematic_2016" + runPeriod + ".root", "recreate")

        fakeTrackSystematic = FakeTrackSystematic ()
        fakeTrackSystematic.addTFile (fout)
        fakeTrackSystematic.addTCanvas (canvas)
        fakeTrackSystematic.addLuminosityLabel (str (round (lumi["MET_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        fakeTrackSystematic.addChannel  ("Basic",                "BasicSelection",         "MET_2016" + runPeriod,       dirs['Andrew']+"2016_final_prompt/basicSelection")
        fakeTrackSystematic.addChannel  ("DisTrkNHits3",         "DisTrkSelectionNHits3",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("DisTrkNHits4",         "DisTrkSelectionNHits4",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("DisTrkNHits5",         "DisTrkSelectionNHits5",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("DisTrkNHits6",         "DisTrkSelectionNHits6",  "MET_2016" + runPeriod,       dirs['Andrew']+"2016/fakeTrackSystematics")
        fakeTrackSystematic.addChannel  ("ZtoLL",                "ZtoMuMu",                "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/zToMuMu_noSkim")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits3",  "ZtoMuMuDisTrkNHits3",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits4",  "ZtoMuMuDisTrkNHits4",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits5",  "ZtoMuMuDisTrkNHits5",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")
        fakeTrackSystematic.addChannel  ("ZtoMuMuDisTrkNHits6",  "ZtoMuMuDisTrkNHits6",    "SingleMu_2016" + runPeriod,  dirs['Andrew']+"2016/fakeTrackBackground")

        print "********************************************************************************"

        fakeTrackSystematic.printSystematic ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"
