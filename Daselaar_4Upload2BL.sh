#!/bin/bash

#May need to log in to brain life with this command:
# bl login --ttl 7

#rawDir=/Volumes/Yorick/fMRI_Replication/rawdata			# location of raw dicoms data
workDir=/Volumes/Yorick/fMRI_Replication				# desired working directory
blProjectID=5f6d12426bbee324dc9a68f4

cd /Volumes/Yorick/fMRI_Replication/rawdata

for i in 00{4..9}; do

    #upload structural dataset
    bl dataset upload --project $blProjectID \
		--datatype neuro/anat/t1w \
		--desc "sub-${i} t1 weighted image" \
		--subject ${i}  \
		--session 1 \
		--t1 /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/anat/sub-${i}_T1w.nii.gz \
		--meta /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/anat/sub-${i}_T1w.json \
		--tag "t1" \
		--tag "image"

    #upload functional data
    for run in 1 2 3 4; do 
    bl dataset upload --project $blProjectID \
            --datatype neuro/func/task \
            --desc "sub-${i} task run-${run}" \
    		--subject ${i}  \
    		--session 1 \
	    	--bold /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/func/sub-${i}_task-RecogConf_run-${run}_bold.nii.gz \
         	--meta /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/func/sub-${i}_task-RecogConf_run-${run}_bold.json \
    		--tag "bold" \
	    	--tag "run-${run}"
	done
	
done

for i in 0{10..60}; do

    #upload structural dataset
    bl dataset upload --project $blProjectID \
		--datatype neuro/anat/t1w \
		--desc "sub-${i} t1 weighted image" \
		--subject ${i}  \
		--session 1 \
		--t1 /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/anat/sub-${i}_T1w.nii.gz \
		--meta /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/anat/sub-${i}_T1w.json \
		--tag "t1" \
		--tag "image"

    #upload functional data
    for run in 1 2 3 4; do 
    bl dataset upload --project $blProjectID \
            --datatype neuro/func/task \
            --desc "sub-${i} task run-${run}" \
    		--subject ${i}  \
    		--session 1 \
	    	--bold /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/func/sub-${i}_task-RecogConf_run-${run}_bold.nii.gz \
         	--meta /Volumes/Yorick/fMRI_Replication/rawdata/sub-${i}/func/sub-${i}_task-RecogConf_run-${run}_bold.json \
    		--tag "bold" \
	    	--tag "run-${run}"
	done
	
done

#    #upload blip data
#    bl dataset upload --project $blProjectID \
#        --datatype neuro/fmap \
#        --desc "${i} reverse blip" \
#        --subject ${i}  \
#        --session 1 \
#        --epi1 ${rawDir}/${i}/fmap/${i}_dir-AP_run-1_epi.nii.gz \
#        --epi1_json ${rawDir}/${i}/fmap/${i}_dir-AP_run-1_epi.json \
#        --epi2 ${rawDir}/${i}/fmap/${i}_dir-PA_run-1_epi.nii.gz \
#        --epi2_json ${rawDir}/${i}/fmap/${i}_dir-PA_run-1_epi.json \
#        --tag "blip" \
#        --tag "image"



