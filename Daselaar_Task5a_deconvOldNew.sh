#!/bin/bash

# Group analysis for old-new
#
# Assumes things are in BIDS format, datasets have been blurred, you've run clustsim
#
# This script was written to run on a local machine (i.e., not on a cluster) with 12 cores available.
# 

	
parDir=/Volumes/Yorick/fMRI_Replication        			# parent directory
derDir=${parDir}/derivatives
refFile=${derDir}/sub-*/deconvOldNew_stats+tlrc			# reference file, for finding dimensions etc
#prefix=
tempDir=/Volumes/Yorick/Templates/vold2_mni    			# desired template
priorDir=${tempDir}/priors_ACT							# location of atropos priors
mask=mask_union
nJobs=12 												# number of cores to devote to this
thr=0.3	
outDir=${derDir}/grp-MVM_OldNew

outputPrefix=MVM_OldNew


if [ ! -d $outDir ]; then
	mkdir -p $outDir
fi

cd $outDir

#should check for mask and create it if it doesn't exist
if [ ! -f ${outDir}/${mask}+tlrc.HEAD ]; then
    3dmask_tool -prefix ${outDir}/${mask} -union -input \
	${derDir}/sub-002/func_mask+tlrc \
	${derDir}/sub-003/func_mask+tlrc \
	${derDir}/sub-004/func_mask+tlrc \
	${derDir}/sub-006/func_mask+tlrc \
	${derDir}/sub-007/func_mask+tlrc \
	${derDir}/sub-008/func_mask+tlrc \
	${derDir}/sub-009/func_mask+tlrc \
	${derDir}/sub-010/func_mask+tlrc \
	${derDir}/sub-011/func_mask+tlrc \
	${derDir}/sub-012/func_mask+tlrc \
	${derDir}/sub-013/func_mask+tlrc \
	${derDir}/sub-014/func_mask+tlrc \
	${derDir}/sub-015/func_mask+tlrc \
	${derDir}/sub-016/func_mask+tlrc \
	${derDir}/sub-017/func_mask+tlrc \
	${derDir}/sub-018/func_mask+tlrc \
	${derDir}/sub-019/func_mask+tlrc \
	${derDir}/sub-020/func_mask+tlrc \
	${derDir}/sub-021/func_mask+tlrc \
	${derDir}/sub-022/func_mask+tlrc \
	${derDir}/sub-023/func_mask+tlrc \
	${derDir}/sub-024/func_mask+tlrc \
	${derDir}/sub-025/func_mask+tlrc \
	${derDir}/sub-027/func_mask+tlrc \
	${derDir}/sub-028/func_mask+tlrc \
	${derDir}/sub-029/func_mask+tlrc \
	${derDir}/sub-030/func_mask+tlrc \
	${derDir}/sub-031/func_mask+tlrc \
	${derDir}/sub-032/func_mask+tlrc \
	${derDir}/sub-033/func_mask+tlrc \
	${derDir}/sub-035/func_mask+tlrc \
	${derDir}/sub-036/func_mask+tlrc \
	${derDir}/sub-037/func_mask+tlrc \
	${derDir}/sub-038/func_mask+tlrc \
	${derDir}/sub-039/func_mask+tlrc \
	${derDir}/sub-040/func_mask+tlrc \
	${derDir}/sub-041/func_mask+tlrc \
	${derDir}/sub-042/func_mask+tlrc \
	${derDir}/sub-043/func_mask+tlrc \
	${derDir}/sub-044/func_mask+tlrc \
	${derDir}/sub-045/func_mask+tlrc \
	${derDir}/sub-046/func_mask+tlrc \
	${derDir}/sub-047/func_mask+tlrc \
	${derDir}/sub-048/func_mask+tlrc \
	${derDir}/sub-049/func_mask+tlrc \
	${derDir}/sub-050/func_mask+tlrc \
	${derDir}/sub-051/func_mask+tlrc \
	${derDir}/sub-053/func_mask+tlrc \
	${derDir}/sub-055/func_mask+tlrc \
	${derDir}/sub-057/func_mask+tlrc \
	${derDir}/sub-058/func_mask+tlrc \
	${derDir}/sub-059/func_mask+tlrc \
	${derDir}/sub-060/func_mask+tlrc 
fi

			
### MVM ###

3dMVM -prefix $outputPrefix -jobs $nJobs -mask ${mask}+tlrc \
-wsVars "objective*subjective" \
-num_glt 2 \
-gltLabel 1 objective_ttest  -gltCode 1 'objective : 1*repeat -1*novel' \
-gltLabel 2 subjective_ttest -gltCode 2 'subjective : 1*old -1*new' \
-dataTable \
Subj		objective	subjective	InputFile \
sub-002    	repeat		old			${derDir}/sub-002/deconvOldNew_stats+tlrc'[5]' \
sub-002    	repeat		new			${derDir}/sub-002/deconvOldNew_stats+tlrc'[7]' \
sub-002    	novel		old			${derDir}/sub-002/deconvOldNew_stats+tlrc'[3]' \
sub-002    	novel		new			${derDir}/sub-002/deconvOldNew_stats+tlrc'[1]' \
sub-003    	repeat		old			${derDir}/sub-003/deconvOldNew_stats+tlrc'[5]' \
sub-003    	repeat		new			${derDir}/sub-003/deconvOldNew_stats+tlrc'[7]' \
sub-003    	novel		old			${derDir}/sub-003/deconvOldNew_stats+tlrc'[3]' \
sub-003    	novel		new			${derDir}/sub-003/deconvOldNew_stats+tlrc'[1]' \
sub-004    	repeat		old			${derDir}/sub-004/deconvOldNew_stats+tlrc'[5]' \
sub-004    	repeat		new			${derDir}/sub-004/deconvOldNew_stats+tlrc'[7]' \
sub-004    	novel		old			${derDir}/sub-004/deconvOldNew_stats+tlrc'[3]' \
sub-004    	novel		new			${derDir}/sub-004/deconvOldNew_stats+tlrc'[1]' \
sub-006    	repeat		old			${derDir}/sub-006/deconvOldNew_stats+tlrc'[5]' \
sub-006    	repeat		new			${derDir}/sub-006/deconvOldNew_stats+tlrc'[7]' \
sub-006    	novel		old			${derDir}/sub-006/deconvOldNew_stats+tlrc'[3]' \
sub-006    	novel		new			${derDir}/sub-006/deconvOldNew_stats+tlrc'[1]' \
sub-007    	repeat		old			${derDir}/sub-007/deconvOldNew_stats+tlrc'[5]' \
sub-007    	repeat		new			${derDir}/sub-007/deconvOldNew_stats+tlrc'[7]' \
sub-007    	novel		old			${derDir}/sub-007/deconvOldNew_stats+tlrc'[3]' \
sub-007    	novel		new			${derDir}/sub-007/deconvOldNew_stats+tlrc'[1]' \
sub-008    	repeat		old			${derDir}/sub-008/deconvOldNew_stats+tlrc'[5]' \
sub-008    	repeat		new			${derDir}/sub-008/deconvOldNew_stats+tlrc'[7]' \
sub-008    	novel		old			${derDir}/sub-008/deconvOldNew_stats+tlrc'[3]' \
sub-008    	novel		new			${derDir}/sub-008/deconvOldNew_stats+tlrc'[1]' \
sub-009    	repeat		old			${derDir}/sub-009/deconvOldNew_stats+tlrc'[5]' \
sub-009    	repeat		new			${derDir}/sub-009/deconvOldNew_stats+tlrc'[7]' \
sub-009    	novel		old			${derDir}/sub-009/deconvOldNew_stats+tlrc'[3]' \
sub-009    	novel		new			${derDir}/sub-009/deconvOldNew_stats+tlrc'[1]' \
sub-010    	repeat		old			${derDir}/sub-010/deconvOldNew_stats+tlrc'[5]' \
sub-010    	repeat		new			${derDir}/sub-010/deconvOldNew_stats+tlrc'[7]' \
sub-010    	novel		old			${derDir}/sub-010/deconvOldNew_stats+tlrc'[3]' \
sub-010    	novel		new			${derDir}/sub-010/deconvOldNew_stats+tlrc'[1]' \
sub-011    	repeat		old			${derDir}/sub-011/deconvOldNew_stats+tlrc'[5]' \
sub-011    	repeat		new			${derDir}/sub-011/deconvOldNew_stats+tlrc'[7]' \
sub-011    	novel		old			${derDir}/sub-011/deconvOldNew_stats+tlrc'[3]' \
sub-011    	novel		new			${derDir}/sub-011/deconvOldNew_stats+tlrc'[1]' \
sub-012    	repeat		old			${derDir}/sub-012/deconvOldNew_stats+tlrc'[5]' \
sub-012    	repeat		new			${derDir}/sub-012/deconvOldNew_stats+tlrc'[7]' \
sub-012    	novel		old			${derDir}/sub-012/deconvOldNew_stats+tlrc'[3]' \
sub-012    	novel		new			${derDir}/sub-012/deconvOldNew_stats+tlrc'[1]' \
sub-013    	repeat		old			${derDir}/sub-013/deconvOldNew_stats+tlrc'[5]' \
sub-013    	repeat		new			${derDir}/sub-013/deconvOldNew_stats+tlrc'[7]' \
sub-013    	novel		old			${derDir}/sub-013/deconvOldNew_stats+tlrc'[3]' \
sub-013    	novel		new			${derDir}/sub-013/deconvOldNew_stats+tlrc'[1]' \
sub-014    	repeat		old			${derDir}/sub-014/deconvOldNew_stats+tlrc'[5]' \
sub-014    	repeat		new			${derDir}/sub-014/deconvOldNew_stats+tlrc'[7]' \
sub-014    	novel		old			${derDir}/sub-014/deconvOldNew_stats+tlrc'[3]' \
sub-014    	novel		new			${derDir}/sub-014/deconvOldNew_stats+tlrc'[1]' \
sub-015    	repeat		old			${derDir}/sub-015/deconvOldNew_stats+tlrc'[5]' \
sub-015    	repeat		new			${derDir}/sub-015/deconvOldNew_stats+tlrc'[7]' \
sub-015    	novel		old			${derDir}/sub-015/deconvOldNew_stats+tlrc'[3]' \
sub-015    	novel		new			${derDir}/sub-015/deconvOldNew_stats+tlrc'[1]' \
sub-016    	repeat		old			${derDir}/sub-016/deconvOldNew_stats+tlrc'[5]' \
sub-016    	repeat		new			${derDir}/sub-016/deconvOldNew_stats+tlrc'[7]' \
sub-016    	novel		old			${derDir}/sub-016/deconvOldNew_stats+tlrc'[3]' \
sub-016    	novel		new			${derDir}/sub-016/deconvOldNew_stats+tlrc'[1]' \
sub-017    	repeat		old			${derDir}/sub-017/deconvOldNew_stats+tlrc'[5]' \
sub-017    	repeat		new			${derDir}/sub-017/deconvOldNew_stats+tlrc'[7]' \
sub-017    	novel		old			${derDir}/sub-017/deconvOldNew_stats+tlrc'[3]' \
sub-017    	novel		new			${derDir}/sub-017/deconvOldNew_stats+tlrc'[1]' \
sub-018    	repeat		old			${derDir}/sub-018/deconvOldNew_stats+tlrc'[5]' \
sub-018    	repeat		new			${derDir}/sub-018/deconvOldNew_stats+tlrc'[7]' \
sub-018    	novel		old			${derDir}/sub-018/deconvOldNew_stats+tlrc'[3]' \
sub-018    	novel		new			${derDir}/sub-018/deconvOldNew_stats+tlrc'[1]' \
sub-019    	repeat		old			${derDir}/sub-019/deconvOldNew_stats+tlrc'[5]' \
sub-019    	repeat		new			${derDir}/sub-019/deconvOldNew_stats+tlrc'[7]' \
sub-019    	novel		old			${derDir}/sub-019/deconvOldNew_stats+tlrc'[3]' \
sub-019    	novel		new			${derDir}/sub-019/deconvOldNew_stats+tlrc'[1]' \
sub-020    	repeat		old			${derDir}/sub-020/deconvOldNew_stats+tlrc'[5]' \
sub-020    	repeat		new			${derDir}/sub-020/deconvOldNew_stats+tlrc'[7]' \
sub-020    	novel		old			${derDir}/sub-020/deconvOldNew_stats+tlrc'[3]' \
sub-020    	novel		new			${derDir}/sub-020/deconvOldNew_stats+tlrc'[1]' \
sub-021    	repeat		old			${derDir}/sub-021/deconvOldNew_stats+tlrc'[5]' \
sub-021    	repeat		new			${derDir}/sub-021/deconvOldNew_stats+tlrc'[7]' \
sub-021    	novel		old			${derDir}/sub-021/deconvOldNew_stats+tlrc'[3]' \
sub-021    	novel		new			${derDir}/sub-021/deconvOldNew_stats+tlrc'[1]' \
sub-022    	repeat		old			${derDir}/sub-022/deconvOldNew_stats+tlrc'[5]' \
sub-022    	repeat		new			${derDir}/sub-022/deconvOldNew_stats+tlrc'[7]' \
sub-022    	novel		old			${derDir}/sub-022/deconvOldNew_stats+tlrc'[3]' \
sub-022    	novel		new			${derDir}/sub-022/deconvOldNew_stats+tlrc'[1]' \
sub-023    	repeat		old			${derDir}/sub-023/deconvOldNew_stats+tlrc'[5]' \
sub-023    	repeat		new			${derDir}/sub-023/deconvOldNew_stats+tlrc'[7]' \
sub-023    	novel		old			${derDir}/sub-023/deconvOldNew_stats+tlrc'[3]' \
sub-023    	novel		new			${derDir}/sub-023/deconvOldNew_stats+tlrc'[1]' \
sub-024    	repeat		old			${derDir}/sub-024/deconvOldNew_stats+tlrc'[5]' \
sub-024    	repeat		new			${derDir}/sub-024/deconvOldNew_stats+tlrc'[7]' \
sub-024    	novel		old			${derDir}/sub-024/deconvOldNew_stats+tlrc'[3]' \
sub-024    	novel		new			${derDir}/sub-024/deconvOldNew_stats+tlrc'[1]' \
sub-025    	repeat		old			${derDir}/sub-025/deconvOldNew_stats+tlrc'[5]' \
sub-025    	repeat		new			${derDir}/sub-025/deconvOldNew_stats+tlrc'[7]' \
sub-025    	novel		old			${derDir}/sub-025/deconvOldNew_stats+tlrc'[3]' \
sub-025    	novel		new			${derDir}/sub-025/deconvOldNew_stats+tlrc'[1]' \
sub-027    	repeat		old			${derDir}/sub-027/deconvOldNew_stats+tlrc'[5]' \
sub-027    	repeat		new			${derDir}/sub-027/deconvOldNew_stats+tlrc'[7]' \
sub-027    	novel		old			${derDir}/sub-027/deconvOldNew_stats+tlrc'[3]' \
sub-027    	novel		new			${derDir}/sub-027/deconvOldNew_stats+tlrc'[1]' \
sub-028    	repeat		old			${derDir}/sub-028/deconvOldNew_stats+tlrc'[5]' \
sub-028    	repeat		new			${derDir}/sub-028/deconvOldNew_stats+tlrc'[7]' \
sub-028    	novel		old			${derDir}/sub-028/deconvOldNew_stats+tlrc'[3]' \
sub-028    	novel		new			${derDir}/sub-028/deconvOldNew_stats+tlrc'[1]' \
sub-029    	repeat		old			${derDir}/sub-029/deconvOldNew_stats+tlrc'[5]' \
sub-029    	repeat		new			${derDir}/sub-029/deconvOldNew_stats+tlrc'[7]' \
sub-029    	novel		old			${derDir}/sub-029/deconvOldNew_stats+tlrc'[3]' \
sub-029    	novel		new			${derDir}/sub-029/deconvOldNew_stats+tlrc'[1]' \
sub-030    	repeat		old			${derDir}/sub-030/deconvOldNew_stats+tlrc'[5]' \
sub-030    	repeat		new			${derDir}/sub-030/deconvOldNew_stats+tlrc'[7]' \
sub-030    	novel		old			${derDir}/sub-030/deconvOldNew_stats+tlrc'[3]' \
sub-030    	novel		new			${derDir}/sub-030/deconvOldNew_stats+tlrc'[1]' \
sub-031    	repeat		old			${derDir}/sub-031/deconvOldNew_stats+tlrc'[5]' \
sub-031    	repeat		new			${derDir}/sub-031/deconvOldNew_stats+tlrc'[7]' \
sub-031    	novel		old			${derDir}/sub-031/deconvOldNew_stats+tlrc'[3]' \
sub-031    	novel		new			${derDir}/sub-031/deconvOldNew_stats+tlrc'[1]' \
sub-032    	repeat		old			${derDir}/sub-032/deconvOldNew_stats+tlrc'[5]' \
sub-032    	repeat		new			${derDir}/sub-032/deconvOldNew_stats+tlrc'[7]' \
sub-032    	novel		old			${derDir}/sub-032/deconvOldNew_stats+tlrc'[3]' \
sub-032    	novel		new			${derDir}/sub-032/deconvOldNew_stats+tlrc'[1]' \
sub-033    	repeat		old			${derDir}/sub-033/deconvOldNew_stats+tlrc'[5]' \
sub-033    	repeat		new			${derDir}/sub-033/deconvOldNew_stats+tlrc'[7]' \
sub-033    	novel		old			${derDir}/sub-033/deconvOldNew_stats+tlrc'[3]' \
sub-033    	novel		new			${derDir}/sub-033/deconvOldNew_stats+tlrc'[1]' \
sub-035    	repeat		old			${derDir}/sub-035/deconvOldNew_stats+tlrc'[5]' \
sub-035    	repeat		new			${derDir}/sub-035/deconvOldNew_stats+tlrc'[7]' \
sub-035    	novel		old			${derDir}/sub-035/deconvOldNew_stats+tlrc'[3]' \
sub-035    	novel		new			${derDir}/sub-035/deconvOldNew_stats+tlrc'[1]' \
sub-036    	repeat		old			${derDir}/sub-036/deconvOldNew_stats+tlrc'[5]' \
sub-036    	repeat		new			${derDir}/sub-036/deconvOldNew_stats+tlrc'[7]' \
sub-036    	novel		old			${derDir}/sub-036/deconvOldNew_stats+tlrc'[3]' \
sub-036    	novel		new			${derDir}/sub-036/deconvOldNew_stats+tlrc'[1]' \
sub-037    	repeat		old			${derDir}/sub-037/deconvOldNew_stats+tlrc'[5]' \
sub-037    	repeat		new			${derDir}/sub-037/deconvOldNew_stats+tlrc'[7]' \
sub-037    	novel		old			${derDir}/sub-037/deconvOldNew_stats+tlrc'[3]' \
sub-037    	novel		new			${derDir}/sub-037/deconvOldNew_stats+tlrc'[1]' \
sub-038    	repeat		old			${derDir}/sub-038/deconvOldNew_stats+tlrc'[5]' \
sub-038    	repeat		new			${derDir}/sub-038/deconvOldNew_stats+tlrc'[7]' \
sub-038    	novel		old			${derDir}/sub-038/deconvOldNew_stats+tlrc'[3]' \
sub-038    	novel		new			${derDir}/sub-038/deconvOldNew_stats+tlrc'[1]' \
sub-039    	repeat		old			${derDir}/sub-039/deconvOldNew_stats+tlrc'[5]' \
sub-039    	repeat		new			${derDir}/sub-039/deconvOldNew_stats+tlrc'[7]' \
sub-039    	novel		old			${derDir}/sub-039/deconvOldNew_stats+tlrc'[3]' \
sub-039    	novel		new			${derDir}/sub-039/deconvOldNew_stats+tlrc'[1]' \
sub-040    	repeat		old			${derDir}/sub-040/deconvOldNew_stats+tlrc'[5]' \
sub-040    	repeat		new			${derDir}/sub-040/deconvOldNew_stats+tlrc'[7]' \
sub-040    	novel		old			${derDir}/sub-040/deconvOldNew_stats+tlrc'[3]' \
sub-040    	novel		new			${derDir}/sub-040/deconvOldNew_stats+tlrc'[1]' \
sub-041    	repeat		old			${derDir}/sub-041/deconvOldNew_stats+tlrc'[5]' \
sub-041    	repeat		new			${derDir}/sub-041/deconvOldNew_stats+tlrc'[7]' \
sub-041    	novel		old			${derDir}/sub-041/deconvOldNew_stats+tlrc'[3]' \
sub-041    	novel		new			${derDir}/sub-041/deconvOldNew_stats+tlrc'[1]' \
sub-042    	repeat		old			${derDir}/sub-042/deconvOldNew_stats+tlrc'[5]' \
sub-042    	repeat		new			${derDir}/sub-042/deconvOldNew_stats+tlrc'[7]' \
sub-042    	novel		old			${derDir}/sub-042/deconvOldNew_stats+tlrc'[3]' \
sub-042    	novel		new			${derDir}/sub-042/deconvOldNew_stats+tlrc'[1]' \
sub-043    	repeat		old			${derDir}/sub-043/deconvOldNew_stats+tlrc'[5]' \
sub-043    	repeat		new			${derDir}/sub-043/deconvOldNew_stats+tlrc'[7]' \
sub-043    	novel		old			${derDir}/sub-043/deconvOldNew_stats+tlrc'[3]' \
sub-043    	novel		new			${derDir}/sub-043/deconvOldNew_stats+tlrc'[1]' \
sub-044    	repeat		old			${derDir}/sub-044/deconvOldNew_stats+tlrc'[5]' \
sub-044    	repeat		new			${derDir}/sub-044/deconvOldNew_stats+tlrc'[7]' \
sub-044    	novel		old			${derDir}/sub-044/deconvOldNew_stats+tlrc'[3]' \
sub-044    	novel		new			${derDir}/sub-044/deconvOldNew_stats+tlrc'[1]' \
sub-045    	repeat		old			${derDir}/sub-045/deconvOldNew_stats+tlrc'[5]' \
sub-045    	repeat		new			${derDir}/sub-045/deconvOldNew_stats+tlrc'[7]' \
sub-045    	novel		old			${derDir}/sub-045/deconvOldNew_stats+tlrc'[3]' \
sub-045    	novel		new			${derDir}/sub-045/deconvOldNew_stats+tlrc'[1]' \
sub-046    	repeat		old			${derDir}/sub-046/deconvOldNew_stats+tlrc'[5]' \
sub-046    	repeat		new			${derDir}/sub-046/deconvOldNew_stats+tlrc'[7]' \
sub-046    	novel		old			${derDir}/sub-046/deconvOldNew_stats+tlrc'[3]' \
sub-046    	novel		new			${derDir}/sub-046/deconvOldNew_stats+tlrc'[1]' \
sub-047    	repeat		old			${derDir}/sub-047/deconvOldNew_stats+tlrc'[5]' \
sub-047    	repeat		new			${derDir}/sub-047/deconvOldNew_stats+tlrc'[7]' \
sub-047    	novel		old			${derDir}/sub-047/deconvOldNew_stats+tlrc'[3]' \
sub-047    	novel		new			${derDir}/sub-047/deconvOldNew_stats+tlrc'[1]' \
sub-048    	repeat		old			${derDir}/sub-048/deconvOldNew_stats+tlrc'[5]' \
sub-048    	repeat		new			${derDir}/sub-048/deconvOldNew_stats+tlrc'[7]' \
sub-048    	novel		old			${derDir}/sub-048/deconvOldNew_stats+tlrc'[3]' \
sub-048    	novel		new			${derDir}/sub-048/deconvOldNew_stats+tlrc'[1]' \
sub-049    	repeat		old			${derDir}/sub-049/deconvOldNew_stats+tlrc'[5]' \
sub-049    	repeat		new			${derDir}/sub-049/deconvOldNew_stats+tlrc'[7]' \
sub-049    	novel		old			${derDir}/sub-049/deconvOldNew_stats+tlrc'[3]' \
sub-049    	novel		new			${derDir}/sub-049/deconvOldNew_stats+tlrc'[1]' \
sub-051    	repeat		old			${derDir}/sub-051/deconvOldNew_stats+tlrc'[5]' \
sub-051    	repeat		new			${derDir}/sub-051/deconvOldNew_stats+tlrc'[7]' \
sub-051    	novel		old			${derDir}/sub-051/deconvOldNew_stats+tlrc'[3]' \
sub-051    	novel		new			${derDir}/sub-051/deconvOldNew_stats+tlrc'[1]' \
sub-053    	repeat		old			${derDir}/sub-053/deconvOldNew_stats+tlrc'[5]' \
sub-053    	repeat		new			${derDir}/sub-053/deconvOldNew_stats+tlrc'[7]' \
sub-053    	novel		old			${derDir}/sub-053/deconvOldNew_stats+tlrc'[3]' \
sub-053    	novel		new			${derDir}/sub-053/deconvOldNew_stats+tlrc'[1]' \
sub-054    	repeat		old			${derDir}/sub-054/deconvOldNew_stats+tlrc'[5]' \
sub-054    	repeat		new			${derDir}/sub-054/deconvOldNew_stats+tlrc'[7]' \
sub-054    	novel		old			${derDir}/sub-054/deconvOldNew_stats+tlrc'[3]' \
sub-054    	novel		new			${derDir}/sub-054/deconvOldNew_stats+tlrc'[1]' \
sub-055    	repeat		old			${derDir}/sub-055/deconvOldNew_stats+tlrc'[5]' \
sub-055    	repeat		new			${derDir}/sub-055/deconvOldNew_stats+tlrc'[7]' \
sub-055    	novel		old			${derDir}/sub-055/deconvOldNew_stats+tlrc'[3]' \
sub-055    	novel		new			${derDir}/sub-055/deconvOldNew_stats+tlrc'[1]' \
sub-057    	repeat		old			${derDir}/sub-057/deconvOldNew_stats+tlrc'[5]' \
sub-057    	repeat		new			${derDir}/sub-057/deconvOldNew_stats+tlrc'[7]' \
sub-057    	novel		old			${derDir}/sub-057/deconvOldNew_stats+tlrc'[3]' \
sub-057    	novel		new			${derDir}/sub-057/deconvOldNew_stats+tlrc'[1]' \
sub-058    	repeat		old			${derDir}/sub-058/deconvOldNew_stats+tlrc'[5]' \
sub-058    	repeat		new			${derDir}/sub-058/deconvOldNew_stats+tlrc'[7]' \
sub-058    	novel		old			${derDir}/sub-058/deconvOldNew_stats+tlrc'[3]' \
sub-058    	novel		new			${derDir}/sub-058/deconvOldNew_stats+tlrc'[1]' \
sub-059    	repeat		old			${derDir}/sub-059/deconvOldNew_stats+tlrc'[5]' \
sub-059    	repeat		new			${derDir}/sub-059/deconvOldNew_stats+tlrc'[7]' \
sub-059    	novel		old			${derDir}/sub-059/deconvOldNew_stats+tlrc'[3]' \
sub-059    	novel		new			${derDir}/sub-059/deconvOldNew_stats+tlrc'[1]' \
sub-060    	repeat		old			${derDir}/sub-060/deconvOldNew_stats+tlrc'[5]' \
sub-060    	repeat		new			${derDir}/sub-060/deconvOldNew_stats+tlrc'[7]' \
sub-060    	novel		old			${derDir}/sub-060/deconvOldNew_stats+tlrc'[3]' \
sub-060    	novel		new			${derDir}/sub-060/deconvOldNew_stats+tlrc'[1]'


