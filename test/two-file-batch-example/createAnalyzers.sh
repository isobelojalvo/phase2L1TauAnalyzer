jobName="2019_Jul23-dyll-try5"
#
j=0
for i in {0..1}
do
    cat test-Analyzer.py > SUB-Analyzer-${i}.py
    #echo "process.source.skipEvents = cms.untracked.uint32(${j})" >> SUB-Analyzer-${i}.py
    j=$(( $j + 100))
    cat submit.py >> SUB-Analyzer-${i}.py
    cat submit-$i.py >> SUB-Analyzer-${i}.py

    mkdir -p /nfs_scratch/ojalvo/${jobName}/SUB-DYLL-200PU-SUBPhase-$i/dags/daginputs

    farmoutAnalysisJobs --vsize-limit=7000 --assume-input-files-exist  --input-file-list=inputFileList-dummy.txt --output-dir=/hdfs/store/user/ojalvo/${jobName} --submit-dir=/nfs_scratch/ojalvo/${jobName}/SUB-DYLL-200PU-SUBPhase-$i/submit --output-dag-file=/nfs_scratch/ojalvo/${jobName}/SUB-DYLL-200PU-SUBPhase-$i/dags/dag  ${jobName}-DYLL-200PU  $CMSSW_BASE  $CMSSW_BASE/src/L1Trigger/phase2L1TauAnalyzer/test/two-file-batch-example/SUB-Analyzer-$i.py     &
    
    if [ "$i" -eq "15" ]; then
	wait;
    fi

    if [ "$i" -eq "30" ]; then
	wait;
    fi

    if [ "$i" -eq "45" ]; then
	wait;
    fi

    if [ "$i" -eq "60" ]; then
	wait;
    fi


done



