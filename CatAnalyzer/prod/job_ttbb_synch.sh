dataset_loc=$CMSSW_BASE/src/CATTools/CatAnalyzer/data/dataset
cfg=$CMSSW_BASE/src/CATTools/CatAnalyzer/prod/ttbbLepJetsAnalyzer_cfg.py
#save_loc=/store/user/san/ntuple/Run2018/V10_2
#save_loc=/store/user/jichoi/ntuple/2018/V10_2_sync
save_loc=/store/user/jichoi/ntuple/2018/V10_2_sync/noisPF_corrected

# 2018 Run2 data
### EG
#create-batch cmsRun --jobName DataSingleEGA --fileList $dataset_loc/dataset_EGamma_Run2018A.txt --cfg $cfg --transferDest $save_loc/DataSingleEGA --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'

create-batch cmsRun --jobName DataSingleEGB --fileList $dataset_loc/dataset_EGamma_Run2018B.txt --cfg $cfg --transferDest $save_loc/DataSingleEGB --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
create-batch cmsRun --jobName DataSingleEGC --fileList $dataset_loc/dataset_EGamma_Run2018C.txt --cfg $cfg --transferDest $save_loc/DataSingleEGC --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
create-batch cmsRun --jobName DataSingleEGD --fileList $dataset_loc/dataset_EGamma_Run2018D.txt --cfg $cfg --transferDest $save_loc/DataSingleEGD --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
#### Mu
#create-batch --jobName DataSingleMuA --fileList $dataset_loc/dataset_SingleMuon_Run2018A.txt --cfg $cfg --transferDest $save_loc/DataSingleMuA --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
#create-batch --jobName DataSingleMuB --fileList $dataset_loc/dataset_SingleMuon_Run2018B.txt --cfg $cfg --transferDest $save_loc/DataSingleMuB --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
#create-batch --jobName DataSingleMuC --fileList $dataset_loc/dataset_SingleMuon_Run2018C.txt --cfg $cfg --transferDest $save_loc/DataSingleMuC --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
#create-batch --jobName DataSingleMuD --fileList $dataset_loc/dataset_SingleMuon_Run2018D.txt --cfg $cfg --transferDest $save_loc/DataSingleMuD --maxFiles 50 --args 'UserJSON=true runOnTTbarMC=0 TTbarCatMC=0'
#
## Signal
#create-batch --jobName TTLJ_PowhegPythia_ttbb_sync --fileList $dataset_loc/dataset_TTLJ_powheg.txt --cfg $cfg --transferDest $save_loc/TTLJ_PowhegPythia_ttbb --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=1 TTbarCatMC=1'
#create-batch --jobName TTLJ_PowhegPythia_ttbj --fileList $dataset_loc/dataset_TTLJ_powheg.txt --cfg $cfg --transferDest $save_loc/TTLJ_PowhegPythia_ttbj --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=1 TTbarCatMC=2'
#create-batch --jobName TTLJ_PowhegPythia_ttcc --fileList $dataset_loc/dataset_TTLJ_powheg.txt --cfg $cfg --transferDest $save_loc/TTLJ_PowhegPythia_ttcc --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=1 TTbarCatMC=3'
#create-batch --jobName TTLJ_PowhegPythia_ttLF --fileList $dataset_loc/dataset_TTLJ_powheg.txt --cfg $cfg --transferDest $save_loc/TTLJ_PowhegPythia_ttLF --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=1 TTbarCatMC=4'
#create-batch --jobName TTLJ_PowhegPythia_ttother --fileList $dataset_loc/dataset_TTLJ_powheg.txt --cfg $cfg --transferDest $save_loc/TTLJ_PowhegPythia_ttother --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=1 TTbarCatMC=5'
#
## Background
#### ttbar background
#create-batch --jobName TTLJ_PowhegPythiaBkg --fileList $dataset_loc/dataset_TTLJ_powheg.txt --cfg $cfg --transferDest $save_loc/TTLJ_PowhegPythiaBkg --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=2 TTbarCatMC=0'
#create-batch --jobName TTLL_PowhegPythiaBkg --fileList $dataset_loc/dataset_TTTo2L2Nu.txt --cfg $cfg --transferDest $save_loc/TTLL_PowhegPythiaBkg --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=2 TTbarCatMC=0'
#create-batch --jobName TTJJ_PowhegPythiaBkg --fileList $dataset_loc/dataset_TTToHadronic.txt --cfg $cfg --transferDest $save_loc/TTJJ_PowhegPythiaBkg --maxFiles 50 --args 'UserJSON=false runOnTTbarMC=2 TTbarCatMC=0'
