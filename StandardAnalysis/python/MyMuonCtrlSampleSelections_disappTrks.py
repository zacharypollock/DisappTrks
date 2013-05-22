
import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####   
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters
#triggersSingleMU = cms.vstring()
# Selection of control samples
triggersDoubleMu = cms.vstring(
    "HLT_DoubleMu11_Acoplanarity03_v",
    "HLT_DoubleMu14_Mass8_PFMET40_v",
    "HLT_DoubleMu14_Mass8_PFMET50_v",
    "HLT_DoubleMu3_4_Dimuon5_Bs_Central_v",
    "HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v",
    "HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v",
    "HLT_DoubleMu3p5_LowMass_Displaced_v",
    "HLT_DoubleMu4_Acoplanarity03_v",
    "HLT_DoubleMu4_Dimuon7_Bs_Forward_v",
    "HLT_DoubleMu4_JpsiTk_Displaced_v",
    "HLT_DoubleMu4_Jpsi_Displaced_v",
    "HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v",
    "HLT_DoubleMu5_IsoMu5_v",
    "HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v",
    )

triggersSingleMu = cms.vstring(
    "HLT_IsoMu24_v",
    )

triggersJetMet = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "HLT_MET120_HBHENoiseCleaned_v"
    )


WToMu = cms.PSet(
    name = cms.string("WToMu"),
    triggers = copy.deepcopy(triggersSingleMu),
#    triggers = copy.deepcopy(triggersJetMet),
    cuts = cms.VPSet(
    cms.PSet (
        inputCollection = cms.string("mets"),
        cutString = cms.string("pt > 220"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("pt > 110"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("fabs(eta) < 2.5"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightID > 0"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("detIso < 0.05"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 0.02"),
        numberRequired = cms.string(">= 1"),
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("<= 1"),  
        ),
    cms.PSet (
        inputCollection = cms.string("mets"),
        cutString = cms.string("pt > 40"),
        numberRequired = cms.string("== 1"),  
        ),
)
)

ZtoMuMu = cms.PSet(
    # Get this example from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/OSUT3Analysis/AnaTools/python/MyEventSelections.py?revision=1.2&view=markup  
    name = cms.string("ZtoMuMu"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.1"),
        numberRequired = cms.string(">= 2"),
        #alias = cms.string("|eta| < 2.1")
      ),    
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 2"),
        #alias = cms.string("pT > 20 GeV") 
      ),
      cms.PSet (
          inputCollection = cms.string("muons"),
          cutString = cms.string("tightID > 0"),
          numberRequired = cms.string(">= 2")
#          #alias = cms.string("MuonTightID")
          ),
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 2"),
        #alias = cms.string("Muon Iso < 0.12")
      ),

      cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
        numberRequired = cms.string(">= 2"),
        #alias =cms.string("|d0| < 0.01 cm")
        ),
      cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedDZ) < 0.01"),
        numberRequired = cms.string(">= 2"),
        #alias =cms.string("|dZ| < 0.01 cm")
        ),
      cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("tkNumValidHits > 4"),
        numberRequired = cms.string(">= 2"),
        #alias =cms.string("Valid Hits > 4")
        ),
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("= 0"),
        #alias = cms.string("Electrons = 0")
        ),
      cms.PSet (
          inputCollection = cms.string("muon-muon pairs"),
          cutString = cms.string("chargeProduct == -1"),
          numberRequired = cms.string(">= 1"),
          
                    ),
      cms.PSet (
        inputCollection = cms.string("muon-muon pairs"),
        cutString = cms.string("invMass > 40 & invMass < 160"),
        numberRequired = cms.string(">= 1"),
        ),
      cms.PSet (
          inputCollection = cms.string("muon-track pairs"),
          cutString = cms.string("deltaR < 0.15"),
          numberRequired = cms.string(">= 1"),
          ),
      )
   )   


ZtoMuTrack = cms.PSet(
    name = cms.string("ZtoMuTrack"),
    cuts = cms.VPSet(
    cms.PSet(
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("(m) pT > 20 GeV")
        ),
    
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) |eta| < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightID > 0"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("MuonTightID")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("Muon Iso < 0.12")
        ),
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) |d0| < 0.01 cm")
        ),
    
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedDZ) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) |dZ| < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("tkNumValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) Valid Hits > 4")
        ),
    cms.PSet(
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("(t) pT > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(t) |eta| < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(t) |d0| < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(t) |dZ| < 0.01 cm")
        ),
    cms.PSet(
         inputCollection= cms.string("tracks"),
         cutString = cms.string("numValidHits > 4"),
         numberRequired = cms.string(">= 1"),
         #alias =cms.string("(t) Valid Hits > 4")
         ),
 ##    cms.PSet (
##         inputCollection = cms.string("tracks"),
##         cutString = cms.string("nHitsMissingMiddle == 0"),
##         numberRequired = cms.string(">= 1"),
##         #alias = cms.string("Missing Middle Hits = 0")
##         ),
##     cms.PSet (
##         inputCollection = cms.string("tracks"),
##         cutString = cms.string("nHitsMissingInner == 0"),
##         numberRequired = cms.string(">= 1"),
##         #alias = cms.string("Missing Inner Hits = 0")
##        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("Track Isolation")
        ),
    )
    )

ZtoMuTrackPreSel = cms.PSet(
    name = cms.string("ZtoMuTrackPreSel"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = copy.deepcopy(ZtoMuTrack.cuts)
    )
cutMuTrackInvMass = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < invMass(m+t) < 160")
    )
ElectronVetoAll =   cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("= 0"),  # Require no electron in event.
        #alias = cms.string("Electrons = 0")
        )
ZtoMuTrackPreSel.cuts.append(cutMuTrackInvMass)


ZtoMuTrackFullPreSel = cms.PSet(
    name = cms.string("ZtoMuTrackFullPreSel"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = copy.deepcopy(ZtoMuTrack.cuts)
    )

deadEcalVeto =  cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 0"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deadEcal Veto")
    )

crackVeto =    cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Crack Veto")
    )

ZtoMuTrackFullPreSel.cuts.append(ElectronVetoAll)
ZtoMuTrackFullPreSel.cuts.append(deadEcalVeto)
ZtoMuTrackFullPreSel.cuts.append(crackVeto)
MuonVetoOneMax =   cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("<= 1"),  # Require no more than one muon in event (since one mu is already selected).
            #alias = cms.string("Muons = 1")
            )
ZtoMuTrackFullPreSel.cuts.append(MuonVetoOneMax)
ZtoMuTrackFullPreSel.cuts.append(cutMuTrackInvMass)




WtoMuNuTrackFullPreSel = cms.PSet(
    name = cms.string("WtoMuNuTrackFullPreSel"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
    cms.PSet(
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("(m) pT > 20 GeV")
        ),
    
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) |eta| < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightID > 0"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("MuonTightID")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("Muon Iso < 0.12")
        ),
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) |d0| < 0.01 cm")
        ),
    
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedDZ) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) |dZ| < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("tkNumValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(m) Valid Hits > 4")
        ),
    cms.PSet(
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("(t) pT > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(t) |eta| < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(t) |d0| < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #alias =cms.string("(t) |dZ| < 0.01 cm")
        ),
    cms.PSet(
         inputCollection= cms.string("tracks"),
         cutString = cms.string("numValidHits > 4"),
         numberRequired = cms.string(">= 1"),
         #alias =cms.string("(t) Valid Hits > 4")
         ),
    cms.PSet (
         inputCollection = cms.string("tracks"),
         cutString = cms.string("nHitsMissingMiddle == 0"),
         numberRequired = cms.string(">= 1"),
         #alias = cms.string("Missing Middle Hits = 0")
         ),
     cms.PSet (
         inputCollection = cms.string("tracks"),
         cutString = cms.string("nHitsMissingInner == 0"),
         numberRequired = cms.string(">= 1"),
         #alias = cms.string("Missing Inner Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        #alias = cms.string("Track Isolation")
        ),
    )
    )

WtoMuNuTrackFullPreSel.cuts.append(ElectronVetoAll)
WtoMuNuTrackFullPreSel.cuts.append(deadEcalVeto)
WtoMuNuTrackFullPreSel.cuts.append(crackVeto)
WtoMuNuTrackFullPreSel.cuts.append(MuonVetoOneMax)


deltaRMuTrack = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deltaRMuTrack > 0.15")
    )
muonInvMassWtoMuNu = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT > 50"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("muonMETMT > 50 GeV")
    )


WtoMuNuTrackFullPreSel.cuts.append(deltaRMuTrack)
WtoMuNuTrackFullPreSel.cuts.append(muonInvMassWtoMuNu)



