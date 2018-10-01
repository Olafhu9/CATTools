import FWCore.ParameterSet.Config as cms
#------------------------------------------------------------------
#------------------------------------------------------------------
## setting up arguements
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
# JSON
options.register('UserJSON', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "UserJSON: Fault  default")
# runOnTTbarMC ==> 0->No ttbar, 1->ttbar Signal, 2->ttbar Background
options.register('runOnTTbarMC', 1, VarParsing.multiplicity.singleton, VarParsing.varType.int, "runOnTTbarMC: 0  default No ttbar sample")
# TTbarCatMC   ==> 0->All ttbar, 1->ttbb, 2->ttbj, 3->ttcc, 4->ttLF, 5->tt, 6->ttjj, 7->ST FCNC
options.register('TTbarCatMC', 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, "TTbarCatMC: 0  default All ttbar events")
# Powheg samples ==> True
options.register('Powheg', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "True for powheg samples")
options.parseArguments()

print "User JSON file: " + str(options.UserJSON)
print "runOnTTbarMC: "   + str(options.runOnTTbarMC)
print "TTbarCatMC: "     + str(options.TTbarCatMC)
#------------------------------------------------------------------
#------------------------------------------------------------------

process = cms.Process("fcncLepJets")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 5000
#process.MessageLogger.cerr.threshold = 'INFO'
#process.MessageLogger.categories.append('fcncLepJets')
#process.MessageLogger.cerr.INFO = cms.untracked.PSet(
#     limit = cms.untracked.int32(-1)
#)
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",

     fileNames = cms.untracked.vstring(
        #'root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/V9_2/SingleElectron/V9_2_Run2017E-31Mar2018-v1/180601_025825/0000/catTuple_1.root'
        'root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/V9_2/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/V9_2_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180603_161622/0000/catTuple_1.root',
        #'root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/V9_2/ST_FCNC-TH_Tleptonic_HTobb_eta_hct-MadGraph5-pythia8/V9_2_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180604_142445/0000/catTuple_1.root'
        #'root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/V9_2/ST_FCNC-TH_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8/V9_2_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180604_142529/0000/catTuple_1.root'
        #'root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/V9_2/TT_FCNC-aTtoHJ_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8/V9_2_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/180907_072143/0000/catTuple_1.root'
        #'root://cms-xrdr.sdfarm.kr:1094///xrd/store/group/CAT/V9_2/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/V9_2_RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180603_161508/0000/catTuple_1.root'
        )
)

# PUReWeight
process.load("CATTools.CatProducer.pileupWeight_cff")
from CATTools.CatProducer.pileupWeight_cff import pileupWeightMap
process.pileupWeight.weightingMethod = "RedoWeight"
process.pileupWeight.pileupMC = pileupWeightMap["2017_25ns_WinterMC_v2"]
process.pileupWeight.pileupRD = pileupWeightMap["Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON"]
process.pileupWeight.pileupUp = pileupWeightMap["Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_Up"]
process.pileupWeight.pileupDn = pileupWeightMap["Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_Dn"]

# json file (Only Data)
if options.UserJSON:
    # /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco
    print "Running data.... Including JSON File."
    import FWCore.PythonUtilities.LumiList as LumiList
    process.source.lumisToProcess = LumiList.LumiList(filename = '../../CatProducer/data/LumiMask/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange()

#Load MET filters for MC
process.load("CATTools.CatAnalyzer.filters_cff")
process.filterRECOMC.doFilter = True
# Lepton Scale Factors
from CATTools.CatAnalyzer.leptonSF_cff import *
# GEN Weights
process.load("CATTools.CatAnalyzer.flatGenWeights_cfi")
# CSV Scale Factors
process.load("CATTools.CatAnalyzer.deepcsvWeights_cfi")
process.deepcsvWeights.minPt = 30   # Same cuts than jet selection
process.deepcsvWeights.maxEta = 2.4

process.fcncLepJets = cms.EDAnalyzer('fcncLepJetsAnalyzer',
                                     TTbarSampleLabel  = cms.untracked.int32(options.runOnTTbarMC),
                                     TTbarCatLabel     = cms.untracked.int32(options.TTbarCatMC),
                                     IsPowheg          = cms.untracked.bool(options.Powheg),
                                     # TriggerNames
                                     triggerNameDataEl = cms.untracked.vstring("HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v",
                                                                               "HLT_Ele32_WPTight_Gsf_L1DoubleEG_v"),
                                     #triggerNameDataEl = cms.untracked.vstring("HLT_Ele32_WPTight_Gsf_v"),
                                     triggerNameDataMu = cms.untracked.vstring("HLT_IsoMu27_v"),
                                     triggerNameMCEl   = cms.untracked.vstring("HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned_v",
                                                                               "HLT_Ele32_WPTight_Gsf_L1DoubleEG_v"),
                                     #triggerNameMCEl   = cms.untracked.vstring("HLT_Ele32_WPTight_Gsf_v"),
                                     triggerNameMCMu   = cms.untracked.vstring("HLT_IsoMu27_v"),
                                     # Input Tags
                                     genWeightLabel    = cms.InputTag("flatGenWeights"),
                                     genLabel          = cms.InputTag("prunedGenParticles"),
                                     genJetLabel       = cms.InputTag("slimmedGenJets"),
                                     deepcsvWeightLabel= cms.InputTag("deepcsvWeights"),
                                     genHiggsCatLabel  = cms.InputTag("GenTtbarCategories:genTtbarId"),
                                     genttbarCatLabel  = cms.InputTag("catGenTops"),
                                     muonLabel         = cms.InputTag("catMuons"),
                                     muonSF            = muonSFTight94X,
                                     electronLabel     = cms.InputTag("catElectrons"),
                                     elecSF            = electronSFMVAWP8094X,
                                     jetLabel          = cms.InputTag("catJets"),
                                     metLabel          = cms.InputTag("catMETs"),
                                     pvLabel           = cms.InputTag("catVertex:nGoodPV"),
                                     puWeightLabel     = cms.InputTag("pileupWeight"),
                                     triggerBits       = cms.InputTag("TriggerResults"), 
                                     triggerObjects    = cms.InputTag("catTrigger"), 
                                     JetMother         = cms.InputTag("genJetHadronFlavour:ancestors"),
                                     nTrueVertLabel    = cms.InputTag("pileupWeight:nTrueInteraction")
                                     )

"""
process.fcncLepJetsQCD = process.fcncLepJets.clone(
    doLooseLepton = cms.untracked.bool(True),
)
"""
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('Tree_fcncLepJets.root')
                                   )

process.p = cms.Path(process.filterRECOMC +
                     process.flatGenWeights +
                     process.deepcsvWeights +
                     process.pileupWeight +
                     process.fcncLepJets) #+ process.fcncLepJetsQCD)
