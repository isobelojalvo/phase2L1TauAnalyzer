# define basic process
import FWCore.ParameterSet.Config as cms
import os
process = cms.Process("L1CaloClusters")
 

# import standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.Geometry.GeometryExtended2023D4Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D4_cff')

process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')


# input
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))
Source_Files = cms.untracked.vstring(
    'root://cms-xrd-global.cern.ch//store/mc/PhaseIISpring17D/SinglePion0_FlatPt-8to100/GEN-SIM-DIGI-RAW/NoPU_90X_upgrade2023_realistic_v9-v1/70000/0024CEE8-5829-E711-A2CA-5065F382C231.root'
    #'file:singleE-gen-sim-raw.root'
    #'root://cms-xrd-global.cern.ch//store/mc/PhaseIISpring17D/SingleE_FlatPt-8to100/GEN-SIM-DIGI-RAW/PU200_90X_upgrade2023_realistic_v9-v1/120000/002A4121-132C-E711-87AD-008CFAFBF618.root'
    )
process.source = cms.Source("PoolSource", fileNames = Source_Files)


# L1 Cluster Producer
process.load("L1Trigger.phase2Demonstrator.L1CaloClusterProducer_cff")
process.L1CaloClusterProducer.debug = cms.untracked.bool(True)
process.L1Clusters = cms.Path(process.L1CaloClusterProducer)

# L1 Tau Analyzer
process.load("L1Trigger.phase2L1TauAnalyzer.phase2L1TauAnalyzer_cfi")
process.analyzer = cms.Path(process.L1TauAnalyzer)

# output module
#process.out = cms.OutputModule( "PoolOutputModule",
#                                fileName = cms.untracked.string("CaloClusters.root"),
#                                fastCloning = cms.untracked.bool( False ),
#                                outputCommands = cms.untracked.vstring(#'drop *',
#                                                                       'keep *_*_L1Phase2CaloClusters_*', 
#                                                                       )
#)
#process.FEVToutput_step = cms.EndPath(process.out)

process.TFileService = cms.Service("TFileService", 
   fileName = cms.string("analyzer.root"), 
   closeFileFast = cms.untracked.bool(True)
)


process.schedule = cms.Schedule(process.L1Clusters,process.analyzer)


