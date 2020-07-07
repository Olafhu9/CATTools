from CATTools.CatProducer.catTemplate_cfg import *
    
## setting up arguements
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.register('runOnMC', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "runOnMC: 1  default")
options.register('useMiniAOD', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "useMiniAOD: 1  default")
options.register('globalTag', '', VarParsing.multiplicity.singleton, VarParsing.varType.string, "globalTag: 1  default")
options.register('runGenTop', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "runGenTop: 1  default")
options.register('runParticleTop', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "runParticleTop: 0  default")
options.register('isSignal', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "isSignal: 1 default")

options.parseArguments()
runOnMC = options.runOnMC
useMiniAOD = options.useMiniAOD
globalTag = options.globalTag
if runOnMC: runGenTop = options.runGenTop
else: runGenTop = False
runParticleTop = False
if runOnMC and options.runParticleTop: runParticleTop = True
isMCSignal = (runOnMC and options.isSignal == True)

####################################################################
#### setting up global tag
####################################################################
#from Configuration.AlCa.autoCond_condDBv2 import autoCond
#if runOnMC: process.GlobalTag.globaltag = autoCond['run2_mc']
#else: process.GlobalTag.globaltag = autoCond['run2_data']
if not globalTag:
    if runOnMC: from CATTools.CatProducer.catDefinitions_cfi import globalTag_mc as globalTag
    else: from CATTools.CatProducer.catDefinitions_cfi import globalTag_rd as globalTag
process.GlobalTag.globaltag = globalTag
print "runOnMC =",runOnMC,"and useMiniAOD =",useMiniAOD
print "process.GlobalTag.globaltag =",process.GlobalTag.globaltag    
####################################################################
#### cat tools output
####################################################################
from CATTools.CatProducer.catCandidates_cff import *
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

process = addCatCommonObjects(process)
if runOnMC: process = addCatCommonMCObjects(process)
if runGenTop     : process = addCatGenTopObjects(process)
if runParticleTop: process = addCatParticleTopObjects(process)
if isMCSignal:
    process.genWeight.keepFirstOnly = False
    process.catOut.outputCommands.extend(catEventContentMCSignal)

from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeOutput
miniAOD_customizeOutput(process.catOut)
    
####################################################################
#### setting up cat tools
####################################################################
from CATTools.CatProducer.catTools_cff import *
catTool(process, runOnMC, useMiniAOD)
#### add electron ID
addEgmID(process, runOnMC)
####################################################################
#### setting up pat tools - miniAOD step or correcting miniAOD
####################################################################
from CATTools.CatProducer.patTools.patTools_cff import *
patTool(process, runOnMC, useMiniAOD)
#### Finish Paths and Tasks
process.nEventsFiltered = cms.EDProducer("EventCountProducer")
process.p += process.nEventsFiltered
####################################################################
#### cmsRun options
####################################################################
process.maxEvents.input = options.maxEvents

# Default file here for test purpose
if not options.inputFiles:
    if useMiniAOD:
        process.source.fileNames = cms.untracked.vstring(
        #  'file:/pnfs/knu.ac.kr/data/cms/store/user/jipark/public/cat10x_samples/TTToSemiLeptonic_062A981D-4A57-664A-A583-E803A658594B.root'
          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80001/48303D32-5F5E-4C4E-885D-0DD6CBEA9189.root',
          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FEE9789E-1236-2044-A4D5-68873F7B3F9D.root',
          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FE3FD7FB-8BC6-F04D-8731-F48DC1A286C9.root',
          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FDDE7B05-E3A0-204F-8880-63DD6E7D616E.root',
          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FDA9A83F-0B89-6E45-9B5D-924209D6AEFF.root',
#          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FD64C44F-2D25-6B43-93C3-BF0398713527.root',
#          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FD548FF3-E119-3841-BEC0-23933D82E0B6.root',  
#          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FD230AED-F909-8A45-89DE-BA986A9F26AF.root',
#          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FD13C685-245D-5046-B984-61087060FFCE.root',
#          'root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FCDC90D5-A5BC-4A48-B35C-B665DB8392FC.root',
        )

else:
    process.source.fileNames = options.inputFiles

#pat input files are removed because it would not work if useMiniAOD is on.    
## to suppress the long output at the end of the job

if options.maxEvents < 0:
    process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options.wantSummary = True
#process.MessageLogger.cerr.threshold = 'ERROR'
#process.MessageLogger.suppressWarning = cms.untracked.vstring(["JetPtMismatchAtLowPt", "NullTransverseMomentum"])

## for debugging
#process.source.skipEvents = cms.untracked.uint32(3000)
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",ignoreTotal = cms.untracked.int32(1) )
#print "process.catOut.outputCommands", process.catOut.outputCommands
