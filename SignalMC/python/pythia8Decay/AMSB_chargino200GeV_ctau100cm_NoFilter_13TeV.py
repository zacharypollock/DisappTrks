COM_ENERGY = 13000.
CROSS_SECTION = 1.0
MCHI = 200  # GeV
CTAU = 1000  # mm
SLHA_TABLE="""
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27843697E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     6.89400000E+04   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     1.26820216E+16   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.11363144E+02   #  h^0
        35     1.95587000E+03   #  H^0
        36     1.94270361E+03   #  A^0
        37     1.95422314E+03   #  H^+
   1000001     2.01900940E+03   #  dnl
   1000002     2.01751855E+03   #  upl
   1000003     2.01900940E+03   #  stl
   1000004     2.01751904E+03   #  chl
   1000005     1.71646375E+03   #  b1
   1000006     1.34441077E+03   #  t1
   1000011     1.47130884E+03   #  el-
   1000012     1.46899902E+03   #  nuel
   1000013     1.47130884E+03   #  mul-
   1000014     1.46899902E+03   #  numl
   1000015     1.46202637E+03   #  tau1
   1000016     1.46698926E+03   #  nutl
   1000021     1.53593469E+03   #  glss
   1000022     1.99839157E+02   #  z1ss
   1000023     6.32158875E+02   #  z2ss
   1000024     2.00113046E+02   #  w1ss !!! IMPORTANT NOTE: 100 MeV has been added to this to get past ResonanceDecays::MSAFETY = 100 MeV
   1000025    -1.22576782E+03   #  z3ss
   1000035     1.23021887E+03   #  z4ss
   1000037     1.23092566E+03   #  w2ss
   2000001     2.03759778E+03   #  dnr
   2000002     2.02848047E+03   #  upr
   2000003     2.03759778E+03   #  str
   2000004     2.02848083E+03   #  chr
   2000005     2.02415881E+03   #  b2
   2000006     1.73585388E+03   #  t2
   2000011     1.46771460E+03   #  er-
   2000013     1.46771460E+03   #  mur-
   2000015     1.47096094E+03   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.98512524E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     1.05499819E-01   # O_{11}
  1  2    -9.94419336E-01   # O_{12}
  2  1     9.94419336E-01   # O_{21}
  2  2     1.05499819E-01   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99964714E-01   # O_{11}
  1  2     8.40252452E-03   # O_{12}
  2  1    -8.40252452E-03   # O_{21}
  2  2     9.99964714E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     4.30086315E-01   # O_{11}
  1  2     9.02787745E-01   # O_{12}
  2  1    -9.02787745E-01   # O_{21}
  2  2     4.30086315E-01   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1    -3.39858839E-03   #
  1  2     9.97539580E-01   #
  1  3    -6.61222860E-02   #
  1  4     2.30493192E-02   #
  2  1     9.98152673E-01   #
  2  2     7.51540344E-03   #
  2  3     5.07033095E-02   #
  2  4    -3.26247998E-02   #
  3  1     1.29647627E-02   #
  3  2    -3.04026231E-02   #
  3  3    -7.05950618E-01   #
  3  4    -7.07489789E-01   #
  4  1     5.92625849E-02   #
  4  2    -6.27231002E-02   #
  4  3    -7.03342974E-01   #
  4  4     7.05594003E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.95677173E-01   # U_{11}
  1  2     9.28812921E-02   # U_{12}
  2  1    -9.28812921E-02   # U_{21}
  2  2    -9.95677173E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.99426425E-01   # V_{11}
  1  2     3.38641442E-02   # V_{12}
  2  1    -3.38641442E-02   # V_{21}
  2  2    -9.99426425E-01   # V_{22}
Block GAUGE Q=  1.46022791E+03   #
     1     3.57492119E-01   # g`
     2     6.52496159E-01   # g_2
     3     1.22099471E+00   # g_3
Block YU Q=  1.46022791E+03   #
  3  3     8.65803540E-01   # y_t
Block YD Q=  1.46022791E+03   #
  3  3     6.84231147E-02   # y_b
Block YE Q=  1.46022791E+03   #
  3  3     5.14152572E-02   # y_tau
Block HMIX Q=  1.46022791E+03   # Higgs mixing parameters
     1     1.21942151E+03   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51206696E+02   # Higgs vev at Q
     4     3.77409725E+06   # m_A^2(Q)
Block MSOFT Q=  1.46022791E+03   # DRbar SUSY breaking parameters
     1     6.36427734E+02   # M_1(Q)
     2     1.90158478E+02   # M_2(Q)
     3    -1.39936938E+03   # M_3(Q)
    31     1.46589587E+03   # MeL(Q)
    32     1.46589587E+03   # MmuL(Q)
    33     1.46393054E+03   # MtauL(Q)
    34     1.46522168E+03   # MeR(Q)
    35     1.46522168E+03   # MmuR(Q)
    36     1.46127014E+03   # MtauR(Q)
    41     1.94845117E+03   # MqL1(Q)
    42     1.94845117E+03   # MqL2(Q)
    43     1.65248535E+03   # MqL3(Q)
    44     1.95919067E+03   # MuR(Q)
    45     1.95919067E+03   # McR(Q)
    46     1.29033850E+03   # MtR(Q)
    47     1.96798145E+03   # MdR(Q)
    48     1.96798145E+03   # MsR(Q)
    49     1.97202722E+03   # MbR(Q)
Block AU Q=  1.46022791E+03   #
  1  1     1.16652148E+03   # A_u
  2  2     1.16652148E+03   # A_c
  3  3     1.16652148E+03   # A_t
Block AD Q=  1.46022791E+03   #
  1  1     2.77925708E+03   # A_d
  2  2     2.77925708E+03   # A_s
  3  3     2.77925708E+03   # A_b
Block AE Q=  1.46022791E+03   #
  1  1     7.27510864E+02   # A_e
  2  2     7.27510864E+02   # A_mu
  3  3     7.27510864E+02   # A_tau
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000024     %.9g # chargino decay
#          BR         NDA      ID1       ID2
           1.0        2        1000022   211
""" % (1.97326979e-13 / CTAU)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(-1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:qqbar2chi+chi- = on',
            'SUSY:qqbar2chi+-chi0 = on',
            '1000024:tau0 = %.1f' % CTAU,
            'ParticleDecays:tau0Max = %.1f' % (CTAU * 10),
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi:
    slhaFile = cms.untracked.string(''),   # value not used
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_add100MeV/AMSBchargino_%sGeV.slha' % MCHI)
)

ProductionFilterSequence = cms.Sequence(generator)
