COM_ENERGY = 13000.
CROSS_SECTION = 1.0
MCHI = 900  # GeV
CTAU = 100  # mm
SLHA_TABLE="""
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27836258E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     3.20160000E+05   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     9.63624875E+15   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.17885536E+02   #  h^0
        35     5.14209375E+03   #  H^0
        36     5.10833789E+03   #  A^0
        37     5.12604248E+03   #  H^+
   1000001     5.84499561E+03   #  dnl
   1000002     5.84445264E+03   #  upl
   1000003     5.84499561E+03   #  stl
   1000004     5.84445264E+03   #  chl
   1000005     5.11084131E+03   #  b1
   1000006     4.26797754E+03   #  t1
   1000011     8.44497009E+02   #  el-
   1000012     7.82294617E+02   #  nuel
   1000013     8.44497009E+02   #  mul-
   1000014     7.82294617E+02   #  numl
   1000015     4.59390961E+02   #  tau1
   1000016     7.43124634E+02   #  nutl
   1000021     6.02264111E+03   #  glss
   1000022     8.99857849E+02   #  z1ss
   1000023     2.96498828E+03   #  z2ss
   1000024     9.00132288E+02   #  w1ss
   1000025    -4.94443994E+03   #  z3ss
   1000035     4.94548633E+03   #  z4ss
   1000037     4.95200684E+03   #  w2ss
   2000001     5.94409229E+03   #  dnr
   2000002     5.88074072E+03   #  upr
   2000003     5.94409229E+03   #  str
   2000004     5.88074072E+03   #  chr
   2000005     5.89824365E+03   #  b2
   2000006     5.15734326E+03   #  t2
   2000011     4.41901886E+02   #  er-
   2000013     4.41901886E+02   #  mur-
   2000015     7.75092834E+02   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.97571859E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     6.91948459E-02   # O_{11}
  1  2    -9.97603178E-01   # O_{12}
  2  1     9.97603178E-01   # O_{21}
  2  2     6.91948459E-02   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99987841E-01   # O_{11}
  1  2     4.92899446E-03   # O_{12}
  2  1    -4.92899446E-03   # O_{21}
  2  2     9.99987841E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     9.16852951E-02   # O_{11}
  1  2     9.95788038E-01   # O_{12}
  2  1    -9.95788038E-01   # O_{21}
  2  2     9.16852951E-02   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1    -7.91596598E-04   #
  1  2     9.99869168E-01   #
  1  3    -1.56042408E-02   #
  1  4     4.20085900E-03   #
  2  1     9.99881387E-01   #
  2  2     1.02774356E-03   #
  2  3     1.28675103E-02   #
  2  4    -8.40762258E-03   #
  3  1    -3.16098332E-03   #
  3  2     8.06056987E-03   #
  3  3     7.07025349E-01   #
  3  4     7.07135558E-01   #
  4  1     1.50564853E-02   #
  4  2    -1.39906351E-02   #
  4  3    -7.06899285E-01   #
  4  4     7.07015812E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.99734461E-01   # U_{11}
  1  2     2.30428278E-02   # U_{12}
  2  1    -2.30428278E-02   # U_{21}
  2  2    -9.99734461E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.99961317E-01   # V_{11}
  1  2     8.79876781E-03   # V_{12}
  2  1    -8.79876781E-03   # V_{21}
  2  2    -9.99961317E-01   # V_{22}
Block GAUGE Q=  4.47923682E+03   #
     1     3.57524991E-01   # g`
     2     6.52378619E-01   # g_2
     3     1.21928000E+00   # g_3
Block YU Q=  4.47923682E+03   #
  3  3     8.32892656E-01   # y_t
Block YD Q=  4.47923682E+03   #
  3  3     6.45801947E-02   # y_b
Block YE Q=  4.47923682E+03   #
  3  3     5.14558963E-02   # y_tau
Block HMIX Q=  4.47923682E+03   # Higgs mixing parameters
     1     4.95111182E+03   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51892105E+02   # Higgs vev at Q
     4     2.60951160E+07   # m_A^2(Q)
Block MSOFT Q=  4.47923682E+03   # DRbar SUSY breaking parameters
     1     3.00553760E+03   # M_1(Q)
     2     8.59459534E+02   # M_2(Q)
     3    -5.73397852E+03   # M_3(Q)
    31     7.99010315E+02   # MeL(Q)
    32     7.99010315E+02   # MmuL(Q)
    33     7.61961365E+02   # MtauL(Q)
    34     5.51579651E+02   # MeR(Q)
    35     5.51579651E+02   # MmuR(Q)
    36     3.78081726E+02   # MtauR(Q)
    41     5.55658252E+03   # MqL1(Q)
    42     5.55658252E+03   # MqL2(Q)
    43     4.88496289E+03   # MqL3(Q)
    44     5.59192773E+03   # MuR(Q)
    45     5.59192773E+03   # McR(Q)
    46     4.10720898E+03   # MtR(Q)
    47     5.65382471E+03   # MdR(Q)
    48     5.65382471E+03   # MsR(Q)
    49     5.68008496E+03   # MbR(Q)
Block AU Q=  4.47923682E+03   #
  1  1     4.93593066E+03   # A_u
  2  2     4.93593066E+03   # A_c
  3  3     4.93593066E+03   # A_t
Block AD Q=  4.47923682E+03   #
  1  1     1.17858047E+04   # A_d
  2  2     1.17858047E+04   # A_s
  3  3     1.17858047E+04   # A_b
Block AE Q=  4.47923682E+03   #
  1  1     3.34377515E+03   # A_e
  2  2     3.34377515E+03   # A_mu
  3  3     3.34377515E+03   # A_tau
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000024     %.9g # chargino decay
#
#
""" % (1.97326979e-13 / CTAU)

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *


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
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:qqbar2chi+chi- = on',
            'SUSY:qqbar2chi+-chi0 = on',
            '1000024:isResonance = false',
            '1000024:oneChannel = 1 1.0 100 1000022 211',
            '1000024:tau0 = %.1f' % CTAU,
            'ParticleDecays:tau0Max = %.1f' % (CTAU * 10),
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi:
    slhaFile = cms.untracked.string(''),   # value not used
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU/10))
)

ProductionFilterSequence = cms.Sequence(generator)
