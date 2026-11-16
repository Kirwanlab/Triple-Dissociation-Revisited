#!/bin/bash

# 3dClustSim in preparation for group analysis for the replication
#
# Assumes things are in BIDS format, datasets have been blurred
#
# This script was written to run on a local machine (i.e., not on a cluster) with 12 cores available.



parDir=/Volumes/Yorick/fMRI_Replication        				# parent directory
derDir=${parDir}/derivatives
refFile=${derDir}/sub-002/deconvConfidenceCorr_stats+tlrc	# reference file, for finding dimensions etc
tempDir=/Volumes/Yorick/Templates/vold2_mni    				# desired template
priorDir=${tempDir}/priors_ACT								# location of atropos priors
mask=mask_union+tlrc
nJobs=12 													# number of cores to devote to this
thr=0.3	
outDir=${derDir}/grp-MVM_ConfidenceCorr
pref=deconvConfidenceCorr


outputPrefix=MVM_ConfidenceCorr_MC


if [ ! -d $outDir ]; then
	mkdir -p $outDir
fi

cd $outDir


# get template
if [ ! -f vold2_mni_brain+tlrc.HEAD ]; then
	cp ${tempDir}/vold2_mni_brain+tlrc* .
fi
	
### Estimate Blur ###
print=ACF_raw.txt

if [ ! -s $print ]; then
	for k in ${derDir}/sub*; do

		# parameter estimate
		3dFWHMx -mask $mask -input ${k}/${pref}_errts+tlrc -acf >> $print
	done
fi


# simulate noise, determine thresholds
if [ ! -s ACF_MC.txt ]; then

	sed '/ 0  0  0    0/d' $print > tmp

	xA=`awk '{ total += $1 } END { print total/NR }' tmp`
	xB=`awk '{ total += $2 } END { print total/NR }' tmp`
	xC=`awk '{ total += $3 } END { print total/NR }' tmp`

	3dClustSim -mask $mask -pthr .01 .001 .0001 -athr .05 .01 .005 .001 .0005 .0001 -iter 100000 -acf $xA $xB $xC > ACF_MC.txt
	rm tmp
fi
			
			
