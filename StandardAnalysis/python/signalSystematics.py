#!/usr/bin/env python
import os
import sys
import math
import copy

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText, TObject, TLine

from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.tdrstyle import *
setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

def setStyle(h, color = 1):
    h.SetLineColor(color)
    h.SetLineStyle(1)
    h.SetLineWidth(2)
    h.SetMarkerColor(color)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.5)
    h.SetTitle("")

def setCanvasStyle(canvas):
    canvas.SetHighLightColor(2)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetBorderSize(2)
    canvas.SetTickx(1)
    canvas.SetTicky(1)
    canvas.SetLeftMargin(0.128141)
    canvas.SetRightMargin(0.0414573)
    canvas.SetBottomMargin(0.0971503)
    canvas.SetTopMargin(0.0712435)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)


def setAxisStyle(h, xTitle = "", yTitle = "", xRange = (0, 0), yRange = (0, 0)):
    h.GetXaxis().SetNdivisions(505)
    h.GetXaxis().SetLabelOffset(0.005)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetXaxis().SetTitleOffset(1.0)
    h.GetXaxis().SetTitleSize(0.04)
    if xTitle is not "":
        h.GetXaxis().SetTitle(xTitle)
    if xRange[0] != 0 or xRange[1] != 0:
        h.GetXaxis().SetRangeUser(xRange[0], xRange[1])
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetLabelOffset(0.005)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleSize(0.04)
    if yTitle is not "":
        h.GetYaxis().SetTitle(yTitle)
    if yRange[0] != 0 or yRange[1] != 0:
        h.GetYaxis().SetRangeUser(yRange[0], yRange[1])

class PileupSystematic:

    _integrateHistogram = "Met Plots/metNoMu"
    _masses = []
    _lifetimes = []
    _fout = ""
    _extraSamples = {}

    def addChannel (self, role, name, suffix, condorDir):
        channel = {"name" : name, "suffix" : suffix, "condorDir" : condorDir}
        setattr (self, role, channel)

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addMasses (self, masses):
        self._masses = masses

    def addLifetimes (self, lifetimes):
        self._lifetimes = lifetimes

    def addFout (self, fout):
        self._fout = fout

    def addExtraSamples (self, extraSamples):
        self._extraSamples = extraSamples

    def __init__ (self, masses, lifetimes):
        self.addMasses (masses)
        self.addLifetimes (lifetimes)

    def printPileupSystematic (self, mass, lifetime):
        if hasattr (self, "PileupCentral") and hasattr (self, "PileupDown") and hasattr (self, "PileupUp"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupCentral["suffix"]
            condorDir = self.PileupCentral["condorDir"]
            name = self.PileupCentral["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupDown["suffix"]
            condorDir = self.PileupDown["condorDir"]
            name = self.PileupDown["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            down = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupUp["suffix"]
            condorDir = self.PileupUp["condorDir"]
            name = self.PileupUp["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            up = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(" + sample + ") down: " + str (down) + ", central: " + str (central) + ", up: " + str (up) + ", systematic uncertainty: " + str (relDiffDown * 100.0) + "%/" + str (relDiffUp * 100.0) + "%"
            return (sample, relDiffDown, relDiffUp)
        else:
            print "PileupCentral, PileupDown, and PileupUp not all defined. Not printing pileup systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        systematic = []
        maxSystematic = 0.0
        averageSystematic = 0.0
        n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printPileupSystematic (mass, lifetime)
                systematic.append ([sample, str (1.0 + relDiffDown), str (1.0 + relDiffUp)])

                if abs (relDiffDown) > maxSystematic:
                  maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > maxSystematic:
                  maxSystematic = abs (relDiffUp)

                averageSystematic += abs (relDiffDown)
                averageSystematic += abs (relDiffUp)
                n += 2
        averageSystematic /= n

        print "maximum systematic: " + str (maxSystematic * 100.0) + "%"
        print "average systematic: " + str (averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in systematic for word in row) + 2
            for row in systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class ECaloSystematic:

    _integrateHistogram = "Track Plots/trackCaloTot_RhoCorr"

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "CutFlowPlotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def printECaloSystematic (self, dataOrMC = "Data"):
        if hasattr (self, dataOrMC):
            channel = getattr (self, dataOrMC)
            sample = channel["sample"]
            condorDir = channel["condorDir"]
            name = channel["name"]
            ecalo = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = ecalo.IntegralAndError (0, ecalo.FindBin (10.0) - 1, passesError)
            total = ecalo.IntegralAndError (0, ecalo.GetNbinsX () + 1, totalError)

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)

            print "efficiency of ECalo cut in " + dataOrMC + ": " + str (eff) + " - " + str (effErrorLow) + " + " + str (effErrorHigh)
            return (eff, effErrorLow, effErrorHigh)
        else:
            print dataOrMC + " not defined. Not printing ECalo systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        data, dataErrorLow, dataErrorHigh = self.printECaloSystematic ("Data")
        mc, mcErrorLow, mcErrorHigh = self.printECaloSystematic ("MC")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%"
