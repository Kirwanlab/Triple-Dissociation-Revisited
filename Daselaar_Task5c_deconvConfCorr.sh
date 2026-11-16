#!/bin/bash

# Group analysis for confidence-correct
#
# Assumes things are in BIDS format, datasets have been blurred, you've run clustsim
#
# This script was written to run on a local machine (i.e., not on a cluster) with 12 cores available.
# 

	
parDir=/Volumes/Yorick/fMRI_Replication        			# parent directory
derDir=${parDir}/derivatives
refFile=${derDir}/sub-*/deconvConfidenceCorr_stats+tlrc	# reference file, for finding dimensions etc
#prefix=
tempDir=/Volumes/Yorick/Templates/vold2_mni    			# desired template
priorDir=${tempDir}/priors_ACT							# location of atropos priors
mask=mask_union
nJobs=12 												# number of cores to devote to this
thr=0.3	
outDir=${derDir}/grp-MVM_ConfidenceCorr

outputPrefix=MVM_ConfidenceCorr


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

#for i in 02 03 04 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 27 28 29 30 31 32 33 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 51 53 54 55 57 58 59 60; do 
#  for ii in 1 2 3 4 5 6; do
#      echo "sub-0$i    memStr$ii    \${derDir}/sub-0${i}/deconvConfidenceCorr_stats+tlrc'[$((ii*2-1))]' \\" 
#  done
#done


3dMVM  -prefix $outputPrefix -jobs $nJobs -mask ${mask}+tlrc \
-wsVars "memStr" \
-num_glt 4 \
-gltLabel 1 familiarity -gltCode 1 'memStr : -5*memStr1 -3*memStr2 -1*memStr3 +1*memStr4 +3*memStr5 +5*memStr6' \
-gltLabel 2 novelty		-gltCode 2 'memStr : +5*memStr1 +3*memStr2 +1*memStr3 -1*memStr4 -3*memStr5 -5*memStr6' \
-gltLabel 3 recollect   -gltCode 3 'memStr : -1*memStr1 -1*memStr2 -1*memStr3 -1*memStr4 -1*memStr5 +5*memStr6' \
-gltLabel 4 nonlinearnovel   -gltCode 4 'memStr : +5*memStr1 -1*memStr2 -1*memStr3 -1*memStr4 -1*memStr5 -1*memStr6' \
-dataTable  \
Subj       memStr     InputFile \
sub-002    memStr1    ${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-002    memStr2    ${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-002    memStr3    ${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-002    memStr4    ${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-002    memStr5    ${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-002    memStr6    ${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-003    memStr1    ${derDir}/sub-003/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-003    memStr2    ${derDir}/sub-003/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-003    memStr3    ${derDir}/sub-003/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-003    memStr4    ${derDir}/sub-003/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-003    memStr5    ${derDir}/sub-003/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-003    memStr6    ${derDir}/sub-003/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-004    memStr1    ${derDir}/sub-004/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-004    memStr2    ${derDir}/sub-004/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-004    memStr3    ${derDir}/sub-004/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-004    memStr4    ${derDir}/sub-004/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-004    memStr5    ${derDir}/sub-004/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-004    memStr6    ${derDir}/sub-004/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-006    memStr1    ${derDir}/sub-006/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-006    memStr2    ${derDir}/sub-006/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-006    memStr3    ${derDir}/sub-006/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-006    memStr4    ${derDir}/sub-006/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-006    memStr5    ${derDir}/sub-006/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-006    memStr6    ${derDir}/sub-006/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-007    memStr1    ${derDir}/sub-007/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-007    memStr2    ${derDir}/sub-007/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-007    memStr3    ${derDir}/sub-007/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-007    memStr4    ${derDir}/sub-007/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-007    memStr5    ${derDir}/sub-007/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-007    memStr6    ${derDir}/sub-007/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-008    memStr1    ${derDir}/sub-008/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-008    memStr2    ${derDir}/sub-008/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-008    memStr3    ${derDir}/sub-008/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-008    memStr4    ${derDir}/sub-008/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-008    memStr5    ${derDir}/sub-008/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-008    memStr6    ${derDir}/sub-008/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-009    memStr1    ${derDir}/sub-009/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-009    memStr2    ${derDir}/sub-009/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-009    memStr3    ${derDir}/sub-009/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-009    memStr4    ${derDir}/sub-009/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-009    memStr5    ${derDir}/sub-009/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-009    memStr6    ${derDir}/sub-009/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-010    memStr1    ${derDir}/sub-010/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-010    memStr2    ${derDir}/sub-010/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-010    memStr3    ${derDir}/sub-010/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-010    memStr4    ${derDir}/sub-010/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-010    memStr5    ${derDir}/sub-010/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-010    memStr6    ${derDir}/sub-010/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-011    memStr1    ${derDir}/sub-011/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-011    memStr2    ${derDir}/sub-011/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-011    memStr3    ${derDir}/sub-011/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-011    memStr4    ${derDir}/sub-011/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-011    memStr5    ${derDir}/sub-011/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-011    memStr6    ${derDir}/sub-011/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-012    memStr1    ${derDir}/sub-012/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-012    memStr2    ${derDir}/sub-012/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-012    memStr3    ${derDir}/sub-012/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-012    memStr4    ${derDir}/sub-012/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-012    memStr5    ${derDir}/sub-012/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-012    memStr6    ${derDir}/sub-012/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-013    memStr1    ${derDir}/sub-013/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-013    memStr2    ${derDir}/sub-013/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-013    memStr3    ${derDir}/sub-013/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-013    memStr4    ${derDir}/sub-013/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-013    memStr5    ${derDir}/sub-013/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-013    memStr6    ${derDir}/sub-013/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-014    memStr1    ${derDir}/sub-014/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-014    memStr2    ${derDir}/sub-014/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-014    memStr3    ${derDir}/sub-014/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-014    memStr4    ${derDir}/sub-014/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-014    memStr5    ${derDir}/sub-014/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-014    memStr6    ${derDir}/sub-014/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-015    memStr1    ${derDir}/sub-015/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-015    memStr2    ${derDir}/sub-015/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-015    memStr3    ${derDir}/sub-015/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-015    memStr4    ${derDir}/sub-015/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-015    memStr5    ${derDir}/sub-015/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-015    memStr6    ${derDir}/sub-015/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-016    memStr1    ${derDir}/sub-016/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-016    memStr2    ${derDir}/sub-016/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-016    memStr3    ${derDir}/sub-016/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-016    memStr4    ${derDir}/sub-016/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-016    memStr5    ${derDir}/sub-016/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-016    memStr6    ${derDir}/sub-016/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-017    memStr1    ${derDir}/sub-017/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-017    memStr2    ${derDir}/sub-017/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-017    memStr3    ${derDir}/sub-017/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-017    memStr4    ${derDir}/sub-017/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-017    memStr5    ${derDir}/sub-017/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-017    memStr6    ${derDir}/sub-017/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-018    memStr1    ${derDir}/sub-018/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-018    memStr2    ${derDir}/sub-018/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-018    memStr3    ${derDir}/sub-018/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-018    memStr4    ${derDir}/sub-018/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-018    memStr5    ${derDir}/sub-018/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-018    memStr6    ${derDir}/sub-018/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-019    memStr1    ${derDir}/sub-019/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-019    memStr2    ${derDir}/sub-019/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-019    memStr3    ${derDir}/sub-019/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-019    memStr4    ${derDir}/sub-019/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-019    memStr5    ${derDir}/sub-019/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-019    memStr6    ${derDir}/sub-019/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-020    memStr1    ${derDir}/sub-020/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-020    memStr2    ${derDir}/sub-020/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-020    memStr3    ${derDir}/sub-020/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-020    memStr4    ${derDir}/sub-020/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-020    memStr5    ${derDir}/sub-020/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-020    memStr6    ${derDir}/sub-020/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-021    memStr1    ${derDir}/sub-021/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-021    memStr2    ${derDir}/sub-021/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-021    memStr3    ${derDir}/sub-021/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-021    memStr4    ${derDir}/sub-021/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-021    memStr5    ${derDir}/sub-021/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-021    memStr6    ${derDir}/sub-021/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-022    memStr1    ${derDir}/sub-022/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-022    memStr2    ${derDir}/sub-022/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-022    memStr3    ${derDir}/sub-022/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-022    memStr4    ${derDir}/sub-022/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-022    memStr5    ${derDir}/sub-022/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-022    memStr6    ${derDir}/sub-022/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-023    memStr1    ${derDir}/sub-023/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-023    memStr2    ${derDir}/sub-023/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-023    memStr3    ${derDir}/sub-023/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-023    memStr4    ${derDir}/sub-023/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-023    memStr5    ${derDir}/sub-023/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-023    memStr6    ${derDir}/sub-023/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-024    memStr1    ${derDir}/sub-024/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-024    memStr2    ${derDir}/sub-024/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-024    memStr3    ${derDir}/sub-024/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-024    memStr4    ${derDir}/sub-024/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-024    memStr5    ${derDir}/sub-024/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-024    memStr6    ${derDir}/sub-024/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-025    memStr1    ${derDir}/sub-025/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-025    memStr2    ${derDir}/sub-025/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-025    memStr3    ${derDir}/sub-025/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-025    memStr4    ${derDir}/sub-025/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-025    memStr5    ${derDir}/sub-025/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-025    memStr6    ${derDir}/sub-025/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-027    memStr1    ${derDir}/sub-027/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-027    memStr2    ${derDir}/sub-027/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-027    memStr3    ${derDir}/sub-027/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-027    memStr4    ${derDir}/sub-027/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-027    memStr5    ${derDir}/sub-027/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-027    memStr6    ${derDir}/sub-027/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-028    memStr1    ${derDir}/sub-028/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-028    memStr2    ${derDir}/sub-028/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-028    memStr3    ${derDir}/sub-028/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-028    memStr4    ${derDir}/sub-028/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-028    memStr5    ${derDir}/sub-028/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-028    memStr6    ${derDir}/sub-028/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-029    memStr1    ${derDir}/sub-029/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-029    memStr2    ${derDir}/sub-029/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-029    memStr3    ${derDir}/sub-029/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-029    memStr4    ${derDir}/sub-029/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-029    memStr5    ${derDir}/sub-029/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-029    memStr6    ${derDir}/sub-029/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-030    memStr1    ${derDir}/sub-030/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-030    memStr2    ${derDir}/sub-030/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-030    memStr3    ${derDir}/sub-030/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-030    memStr4    ${derDir}/sub-030/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-030    memStr5    ${derDir}/sub-030/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-030    memStr6    ${derDir}/sub-030/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-031    memStr1    ${derDir}/sub-031/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-031    memStr2    ${derDir}/sub-031/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-031    memStr3    ${derDir}/sub-031/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-031    memStr4    ${derDir}/sub-031/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-031    memStr5    ${derDir}/sub-031/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-031    memStr6    ${derDir}/sub-031/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-032    memStr1    ${derDir}/sub-032/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-032    memStr2    ${derDir}/sub-032/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-032    memStr3    ${derDir}/sub-032/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-032    memStr4    ${derDir}/sub-032/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-032    memStr5    ${derDir}/sub-032/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-032    memStr6    ${derDir}/sub-032/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-033    memStr1    ${derDir}/sub-033/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-033    memStr2    ${derDir}/sub-033/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-033    memStr3    ${derDir}/sub-033/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-033    memStr4    ${derDir}/sub-033/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-033    memStr5    ${derDir}/sub-033/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-033    memStr6    ${derDir}/sub-033/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-035    memStr1    ${derDir}/sub-035/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-035    memStr2    ${derDir}/sub-035/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-035    memStr3    ${derDir}/sub-035/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-035    memStr4    ${derDir}/sub-035/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-035    memStr5    ${derDir}/sub-035/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-035    memStr6    ${derDir}/sub-035/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-036    memStr1    ${derDir}/sub-036/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-036    memStr2    ${derDir}/sub-036/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-036    memStr3    ${derDir}/sub-036/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-036    memStr4    ${derDir}/sub-036/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-036    memStr5    ${derDir}/sub-036/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-036    memStr6    ${derDir}/sub-036/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-037    memStr1    ${derDir}/sub-037/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-037    memStr2    ${derDir}/sub-037/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-037    memStr3    ${derDir}/sub-037/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-037    memStr4    ${derDir}/sub-037/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-037    memStr5    ${derDir}/sub-037/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-037    memStr6    ${derDir}/sub-037/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-038    memStr1    ${derDir}/sub-038/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-038    memStr2    ${derDir}/sub-038/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-038    memStr3    ${derDir}/sub-038/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-038    memStr4    ${derDir}/sub-038/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-038    memStr5    ${derDir}/sub-038/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-038    memStr6    ${derDir}/sub-038/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-039    memStr1    ${derDir}/sub-039/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-039    memStr2    ${derDir}/sub-039/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-039    memStr3    ${derDir}/sub-039/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-039    memStr4    ${derDir}/sub-039/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-039    memStr5    ${derDir}/sub-039/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-039    memStr6    ${derDir}/sub-039/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-040    memStr1    ${derDir}/sub-040/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-040    memStr2    ${derDir}/sub-040/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-040    memStr3    ${derDir}/sub-040/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-040    memStr4    ${derDir}/sub-040/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-040    memStr5    ${derDir}/sub-040/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-040    memStr6    ${derDir}/sub-040/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-041    memStr1    ${derDir}/sub-041/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-041    memStr2    ${derDir}/sub-041/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-041    memStr3    ${derDir}/sub-041/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-041    memStr4    ${derDir}/sub-041/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-041    memStr5    ${derDir}/sub-041/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-041    memStr6    ${derDir}/sub-041/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-042    memStr1    ${derDir}/sub-042/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-042    memStr2    ${derDir}/sub-042/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-042    memStr3    ${derDir}/sub-042/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-042    memStr4    ${derDir}/sub-042/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-042    memStr5    ${derDir}/sub-042/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-042    memStr6    ${derDir}/sub-042/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-043    memStr1    ${derDir}/sub-043/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-043    memStr2    ${derDir}/sub-043/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-043    memStr3    ${derDir}/sub-043/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-043    memStr4    ${derDir}/sub-043/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-043    memStr5    ${derDir}/sub-043/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-043    memStr6    ${derDir}/sub-043/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-044    memStr1    ${derDir}/sub-044/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-044    memStr2    ${derDir}/sub-044/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-044    memStr3    ${derDir}/sub-044/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-044    memStr4    ${derDir}/sub-044/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-044    memStr5    ${derDir}/sub-044/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-044    memStr6    ${derDir}/sub-044/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-045    memStr1    ${derDir}/sub-045/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-045    memStr2    ${derDir}/sub-045/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-045    memStr3    ${derDir}/sub-045/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-045    memStr4    ${derDir}/sub-045/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-045    memStr5    ${derDir}/sub-045/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-045    memStr6    ${derDir}/sub-045/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-046    memStr1    ${derDir}/sub-046/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-046    memStr2    ${derDir}/sub-046/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-046    memStr3    ${derDir}/sub-046/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-046    memStr4    ${derDir}/sub-046/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-046    memStr5    ${derDir}/sub-046/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-046    memStr6    ${derDir}/sub-046/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-047    memStr1    ${derDir}/sub-047/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-047    memStr2    ${derDir}/sub-047/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-047    memStr3    ${derDir}/sub-047/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-047    memStr4    ${derDir}/sub-047/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-047    memStr5    ${derDir}/sub-047/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-047    memStr6    ${derDir}/sub-047/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-048    memStr1    ${derDir}/sub-048/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-048    memStr2    ${derDir}/sub-048/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-048    memStr3    ${derDir}/sub-048/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-048    memStr4    ${derDir}/sub-048/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-048    memStr5    ${derDir}/sub-048/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-048    memStr6    ${derDir}/sub-048/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-049    memStr1    ${derDir}/sub-049/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-049    memStr2    ${derDir}/sub-049/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-049    memStr3    ${derDir}/sub-049/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-049    memStr4    ${derDir}/sub-049/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-049    memStr5    ${derDir}/sub-049/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-049    memStr6    ${derDir}/sub-049/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-051    memStr1    ${derDir}/sub-051/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-051    memStr2    ${derDir}/sub-051/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-051    memStr3    ${derDir}/sub-051/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-051    memStr4    ${derDir}/sub-051/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-051    memStr5    ${derDir}/sub-051/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-051    memStr6    ${derDir}/sub-051/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-053    memStr1    ${derDir}/sub-053/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-053    memStr2    ${derDir}/sub-053/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-053    memStr3    ${derDir}/sub-053/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-053    memStr4    ${derDir}/sub-053/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-053    memStr5    ${derDir}/sub-053/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-053    memStr6    ${derDir}/sub-053/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-054    memStr1    ${derDir}/sub-054/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-054    memStr2    ${derDir}/sub-054/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-054    memStr3    ${derDir}/sub-054/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-054    memStr4    ${derDir}/sub-054/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-054    memStr5    ${derDir}/sub-054/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-054    memStr6    ${derDir}/sub-054/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-055    memStr1    ${derDir}/sub-055/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-055    memStr2    ${derDir}/sub-055/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-055    memStr3    ${derDir}/sub-055/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-055    memStr4    ${derDir}/sub-055/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-055    memStr5    ${derDir}/sub-055/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-055    memStr6    ${derDir}/sub-055/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-057    memStr1    ${derDir}/sub-057/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-057    memStr2    ${derDir}/sub-057/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-057    memStr3    ${derDir}/sub-057/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-057    memStr4    ${derDir}/sub-057/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-057    memStr5    ${derDir}/sub-057/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-057    memStr6    ${derDir}/sub-057/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-058    memStr1    ${derDir}/sub-058/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-058    memStr2    ${derDir}/sub-058/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-058    memStr3    ${derDir}/sub-058/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-058    memStr4    ${derDir}/sub-058/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-058    memStr5    ${derDir}/sub-058/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-058    memStr6    ${derDir}/sub-058/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-059    memStr1    ${derDir}/sub-059/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-059    memStr2    ${derDir}/sub-059/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-059    memStr3    ${derDir}/sub-059/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-059    memStr4    ${derDir}/sub-059/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-059    memStr5    ${derDir}/sub-059/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-059    memStr6    ${derDir}/sub-059/deconvConfidenceCorr_stats+tlrc'[11]' \
sub-060    memStr1    ${derDir}/sub-060/deconvConfidenceCorr_stats+tlrc'[1]' \
sub-060    memStr2    ${derDir}/sub-060/deconvConfidenceCorr_stats+tlrc'[3]' \
sub-060    memStr3    ${derDir}/sub-060/deconvConfidenceCorr_stats+tlrc'[5]' \
sub-060    memStr4    ${derDir}/sub-060/deconvConfidenceCorr_stats+tlrc'[7]' \
sub-060    memStr5    ${derDir}/sub-060/deconvConfidenceCorr_stats+tlrc'[9]' \
sub-060    memStr6    ${derDir}/sub-060/deconvConfidenceCorr_stats+tlrc'[11]'
