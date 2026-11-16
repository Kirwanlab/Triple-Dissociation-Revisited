#Move behavioral files from Derivatives to Raw Data
# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/anat_run-${run}/t1.nii.gz derivatives/sub-${subj}/anat_run-${run}/sub-${subj}_t1.nii.gz
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/func_run-${run}/bold.nii.gz derivatives/sub-${subj}/func_run-${run}/sub-${subj}_bold.nii.gz
# 	done
# done

# #Start for loop, read and loop through subjList.txt
# for subj in `cat subjList.txt`;
# #remeber to do
# do
# 	#Second for loop, loop through numbers 1-4
# 	for run in 1 2 3 4; 
# 		#do again
# 		do 
# 		#mv (move) - moves but also renames files 
# 		#mv target_file desitnation(or rename)
# 		mv derivatives/sub-${subj}/mask_run-${run}/mask.nii.gz derivatives/sub-${subj}/mask_run-${run}/sub-${subj}_mask.nii.gz
# 	#done for each loop
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/regressors_run-${run}/regressors.tsv derivatives/sub-${subj}/regressors_run-${run}/sub-${subj}_regressors.tsv
# 		mv derivatives/sub-${subj}/regressors_run-${run}/regressors.json derivatives/sub-${subj}/regressors_run-${run}/sub-${subj}_regressors.json
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/10_23_20/anat_10_23_2020.run-${run}/t1.nii.gz derivatives/sub-${subj}/10_23_20/anat_10_23_2020.run-${run}/sub-${subj}_t1.nii.gz
# 		mv derivatives/sub-${subj}/10_23_20/func_10_23_2020.run-${run}/bold.nii.gz derivatives/sub-${subj}/10_23_20/func_10_23_2020.run-${run}/sub-${subj}_bold.nii.gz
# 		mv derivatives/sub-${subj}/10_23_20/func_bold.run-${run}/bold.nii.gz derivatives/sub-${subj}/10_23_20/func_bold.run-${run}/sub-${subj}_bold.nii.gz
# 		mv derivatives/sub-${subj}/10_23_20/mask_10_23_2020.run-${run}/mask.nii.gz derivatives/sub-${subj}/10_23_20/mask_10_23_2020.run-${run}/sub-${subj}_mask.nii.gz
# 		mv derivatives/sub-${subj}/10_23_20/regressors_10_23_2020.run-${run}/regressors.json derivatives/sub-${subj}/10_23_20/regressors_10_23_2020.run-${run}/sub-${subj}_regressors.json
# 		mv derivatives/sub-${subj}/10_23_20/regressors_10_23_2020.run-${run}/regressors.tsv derivatives/sub-${subj}/10_23_20/regressors_10_23_2020.run-${run}/sub-${subj}_regressors.tsv
# 	done
# done

# for subj in `cat subjList.txt`;
# 	do 
# 	rm derivatives/sub-${subj}/*.err 
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/run-${run}_blur8+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_run-${run}_blur8+tlrc.BRIK
# 		mv derivatives/sub-${subj}/run-${run}_blur8_scaled+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_run-${run}_blur8_scaled+tlrc.BRIK
# 		mv derivatives/sub-${subj}/run-${run}_blur8mean+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_run-${run}_blur8mean+tlrc.BRIK
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/run-${run}_blur8+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_run-${run}_blur8+tlrc.HEAD
# 		mv derivatives/sub-${subj}/run-${run}_blur8_scaled+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_run-${run}_blur8_scaled+tlrc.HEAD
# 		mv derivatives/sub-${subj}/run-${run}_blur8mean+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_run-${run}_blur8mean+tlrc.HEAD
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/mask_run-${run}+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_mask_run-${run}+tlrc.HEAD
# 		mv derivatives/sub-${subj}/mask_run-${run}+tlrc.BRIK.gz derivatives/sub-${subj}/sub-${subj}_mask_run-${run}+tlrc.BRIK
# 		mv derivatives/sub-${subj}/mask_run-${run}+tlrc.BRIK.gz derivatives/sub-${subj}/sub-${subj}_mask_run-${run}+tlrc.BRIK.gz
# 	done
# done

# for subj in `cat subjList.txt`;
# 	do 
# 	rm derivatives/sub-${subj}/*errts* 
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4
# 		do
# 		mv derivatives/sub-${subj}/motion_censor.1D derivatives/sub-${subj}/sub-${subj}_motion_censor.1D
# 		mv derivatives/sub-${subj}/motion_demean_split.r0${run}.1D derivatives/sub-${subj}/sub-${subj}_motion_demean_split.r0${run}.1D
# 		mv derivatives/sub-${subj}/motion_enorm.1D derivatives/sub-${subj}/sub-${subj}_motion_enorm.1D
# 		mv derivatives/sub-${subj}/motion_demean.txt derivatives/sub-${subj}/sub-${subj}_motion_demean.txt
# 		mv derivatives/sub-${subj}/motion.txt derivatives/sub-${subj}/sub-${subj}_motion.txt
# 		mv derivatives/sub-${subj}/RecogConf_stats+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_RecogConf_stats+tlrc.BRIK
# 		mv derivatives/sub-${subj}/behavioral_summary.txt derivatives/sub-${subj}/sub-${subj}_behavioral_summary.txt
# 		mv derivatives/sub-${subj}/qc_psychopy_behavioral.txt derivatives/sub-${subj}/sub-${subj}_qc_psychopy_behavioral.txt
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	for run in 1 2 3 4; 
# 		do 
# 		mv derivatives/sub-${subj}/motion_CENSORTR.txt derivatives/sub-${subj}/sub-${subj}_motion_CENSORTR.txt
# 		mv derivatives/sub-${subj}/func_mask+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_func_mask+tlrc.HEAD
# 		mv derivatives/sub-${subj}/func_mask+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_func_mask+tlrc.BRIK
# 		mv derivatives/sub-${subj}/deconvOldNew_stats+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_deconvOldNew_stats+tlrc.BRIK
# 		mv derivatives/sub-${subj}/deconvConfidence_stats+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_deconvConfidence_stats+tlrc.BRIK
# 		mv derivatives/sub-${subj}/deconvConfidenceCorr_stats+tlrc.BRIK derivatives/sub-${subj}/sub-${subj}_deconvConfidenceCorr_stats+tlrc.BRIK
# 		mv derivatives/sub-${subj}/deconvOldNew_stats+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_deconvOldNew_stats+tlrc.HEAD
# 		mv derivatives/sub-${subj}/deconvConfidence_stats+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_deconvConfidence_stats+tlrc.HEAD
# 		mv derivatives/sub-${subj}/deconvConfidenceCorr_stats+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_deconvConfidenceCorr_stats+tlrc.HEAD
# 		mv derivatives/sub-${subj}/RecogConf_stats+tlrc.HEAD derivatives/sub-${subj}/sub-${subj}_RecogConf_stats+tlrc.HEAD
# 	done
# done

# for subj in `cat subjList.txt`;
# do
# 	mv derivatives/sub-${subj}/deconvConfidence_stats.REML_cmd derivatives/sub-${subj}/sub-${subj}_deconvConfidence_stats.REML_cmd
# 	mv derivatives/sub-${subj}/deconvConfidenceCorr_stats.REML_cmd derivatives/sub-${subj}/sub-${subj}_deconvConfidenceCorr_stats.REML_cmd
# 	mv derivatives/sub-${subj}/deconvOldNew_stats.REML_cmd derivatives/sub-${subj}/sub-${subj}_deconvOldNew_stats.REML_cmd
# 	mv derivatives/sub-${subj}/RecogConf_stats.REML_cmd derivatives/sub-${subj}/sub-${subj}_RecogConf_stats.REML_cmd
# done

# for subj in `cat subjList.txt`;
# do
# 	cd /Volumes/Yorick/fMRI_Replication/rawdata/sub-${subj}/anat/
# 	for i in $( ls | grep [A-Z] ); do mv $i `echo $i | tr 'A-Z' 'a-z'`; done
# 	cd /Volumes/Yorick/fMRI_Replication/rawdata/sub-${subj}/fmap/
# 	for i in $( ls | grep [A-Z] ); do mv $i `echo $i | tr 'A-Z' 'a-z'`; done
# 	cd /Volumes/Yorick/fMRI_Replication/rawdata/sub-${subj}/func/
# 	for i in $( ls | grep [A-Z] ); do mv $i `echo $i | tr 'A-Z' 'a-z'`; done

# done

# for subj in `cat subjList.txt`;
# do
# 	for i in 1 2 3 4;
# 	do	
# 		tr A-Z a-z < rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-${i}_events.tsv > rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-${i}_events2.tsv
# 		rm rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-${i}_events.tsv
# 		mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-${i}_events2.tsv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-${i}_events.tsv
# 	done

# done

# To change directory permissions in Linux, use the following:

# chmod +rwx filename to add permissions.
# chmod -rwx directoryname to remove permissions.
# chmod +x filename to allow executable permissions.
# chmod -wx filename to take out write and executable permissions.
# Note that “r” is for read, “w” is for write, and “x” is for execute. 

# for subj in `cat subjList.txt`;
# do
# 	mv rawdata/sub-${subj}/fmap/sub-${subj}_dir-ap_run-1_epi.json   rawdata/sub-${subj}/fmap/dir-ap_run-1_epi.json
# 	mv rawdata/sub-${subj}/fmap/sub-${subj}_dir-ap_run-1_epi.nii.gz rawdata/sub-${subj}/fmap/dir-ap_run-1_epi.nii.gz
# 	mv rawdata/sub-${subj}/fmap/sub-${subj}_dir-pa_run-1_epi.json   rawdata/sub-${subj}/fmap/dir-pa_run-1_epi.json
# 	mv rawdata/sub-${subj}/fmap/sub-${subj}_dir-pa_run-1_epi.nii.gz rawdata/sub-${subj}/fmap/dir-pa_run-1_epi.nii.gz

# done

# for subj in `cat subjList.txt`;
# do
# 	mv derivatives/sub-${subj}/RecogConf_stats.REML_cmd derivatives/sub-${subj}/sub-${subj}_RecogConf_stats.REML_cmd
# done

# for subj in `cat subjList.txt`;
# do
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-1_bold.nii.gz   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-1_bold.nii.gz
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-2_bold.nii.gz   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-2_bold.nii.gz
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-3_bold.nii.gz   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-3_bold.nii.gz
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-4_bold.nii.gz   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-4_bold.nii.gz
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-1_bold.json   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-1_bold.json
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-2_bold.json   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-2_bold.json
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-3_bold.json   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-3_bold.json
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-4_bold.json   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-4_bold.json
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-1_events.tsv   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-1_events.tsv
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-2_events.tsv   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-2_events.tsv
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-3_events.tsv   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-3_events.tsv
# 	mv rawdata/sub-${subj}/func/sub-${subj}_task-recogconf_run-4_events.tsv   rawdata/sub-${subj}/func/sub-${subj}_task-RecogConf_run-4_events.tsv

# done
# sed -e 's#"func/sub-060_task-RecogConf_run-4_bold.nii.gz",#"func/sub-060_task-RecogConf_run-4_bold.nii.gz"#g' -i .backup sub-060/fmap/sub-060_dir-ap_run-1_epi.json
# sed -e 's#"func/sub-060_task-RecogConf_run-5_bold.nii.gz",##g' -i .backup sub-060/fmap/sub-060_dir-ap_run-1_epi.json
# sed -e 's#"func/sub-060_task-RecogConf_run-6_bold.nii.gz",##g' -i .backup sub-060/fmap/sub-060_dir-ap_run-1_epi.json
# sed -e 's#"func/sub-060_task-RecogConf_run-7_bold.nii.gz",##g' -i .backup sub-060/fmap/sub-060_dir-ap_run-1_epi.json
# sed -e 's#"func/sub-060_task-RecogConf_run-8_bold.nii.gz"##g' -i .backup sub-060/fmap/sub-060_dir-ap_run-1_epi.json
for subj in {22..60};
do
	rm sub-0${subj}/fmap/sub-0${subj}_dir-ap_run-1_epi.json.backup
done