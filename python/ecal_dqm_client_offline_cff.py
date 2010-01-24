import FWCore.ParameterSet.Config as cms

from DQM.EcalBarrelMonitorClient.EcalBarrelMonitorClient_cfi import *
from DQM.EcalEndcapMonitorClient.EcalEndcapMonitorClient_cfi import *

dqmQTestEB = cms.EDFilter("QualityTester",
#    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/EcalBarrelMonitorModule/test/data/EcalBarrelQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True),
    qtestOnEndLumi = cms.untracked.bool(False),
    qtestOnEndRun = cms.untracked.bool(True),
    qtestOnEndJob = cms.untracked.bool(False),
    verboseQT = cms.untracked.bool(False)
)

dqmQTestEE = cms.EDFilter("QualityTester",
#    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/EcalEndcapMonitorModule/test/data/EcalEndcapQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True),
    qtestOnEndLumi = cms.untracked.bool(False),
    qtestOnEndRun = cms.untracked.bool(True),
    qtestOnEndJob = cms.untracked.bool(False),
    verboseQT = cms.untracked.bool(False)
)

eb_dqm_client_offline = cms.Sequence(ecalBarrelMonitorClient*dqmQTestEB)

ee_dqm_client_offline = cms.Sequence(ecalEndcapMonitorClient*dqmQTestEE)

ecal_dqm_client_offline = cms.Sequence(eb_dqm_client_offline*ee_dqm_client_offline)

ecalBarrelMonitorClient.maskFile = ''
ecalBarrelMonitorClient.location = 'P5'
ecalBarrelMonitorClient.verbose = False
ecalBarrelMonitorClient.enabledClients = ['Integrity', 'StatusFlags', 'Occupancy', 'PedestalOnline', 'Cluster', 'TriggerTower', 'Summary']

ecalEndcapMonitorClient.maskFile = ''
ecalEndcapMonitorClient.location = 'P5'
ecalEndcapMonitorClient.verbose = False
ecalEndcapMonitorClient.enabledClients = ['Integrity', 'StatusFlags', 'Occupancy', 'PedestalOnline', 'Cluster', 'TriggerTower', 'Summary']

