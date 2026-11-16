#!/bin/bash

#script modified from https://brainlife.io/docs/cli/download/

#Variables to be updated for each project:
derDir=/Volumes/Yorick/fMRI_Replication/derivatives
project=5f6d12426bbee324dc9a68f4

#These may need to be updated depending on what you need to download. These two arrays should be exactly the same length.
datatype=("neuro/anat/t1w" "neuro/func/task" "neuro/func/regressors" "neuro/mask" "report/html")
output=(anat func regressors mask report)

#Work:
outputLen=${#output[@]}
cd $derDir

for (( i=0; i<$outputLen; i++ ))
    do
    echo "working on datatype: ${output[$i]} ------------"
        
	#cache the list of datasets that we could download
	if [ ! -f ${output[$i]}.json ]; then
		bl dataset query --limit 10000 --project $project --datatype ${datatype[$i]} --json > ${output[$i]}.json
	fi

	#enumerate subjects
	for subject in $(jq -r '.[].meta.subject' ${output[$i]}.json | sort -u)
	do
		echo "downloading subject:$subject ---------------"
		mkdir -p $derDir/$subject
	
		for id in $(jq -r '.[] | select(.meta.subject == '\"$subject\"') | ._id' ${output[$i]}.json)
	
		do
			tags=$(jq -r '.[] | select(._id=='\"$id\"') | .tags | join(".")' ${output[$i]}.json)
			echo $id $tags
			outdir=$derDir/$subject/${output[$i]}_$tags
			if [ ! -d $outdir ]; then
				bl dataset download $id --directory $outdir
			fi
		done
	done
done