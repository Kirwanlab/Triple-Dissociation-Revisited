#!/bin/bash

# scale each voxel time series to have a mean of 100
# (be sure no negatives creep in)
# (subject to a range of [0,200])


derDir=/Volumes/Yorick/fMRI_Replication/derivatives/

cd $derDir
for i in `cat ../subjList.txt`; do
    cd sub-$i
    for run in 1 2 3 4; do 
        if [ ! -f run-${run}_blur8mean+tlrc.HEAD ]; then
            3dTstat -prefix run-${run}_blur8mean -mean run-${run}_blur8+tlrc
        fi
        
        if [ ! -f run-${run}_blur8_scaled+tlrc.HEAD ]; then
            3dcalc -a run-${run}_blur8+tlrc -b run-${run}_blur8mean+tlrc \
               -c mask_run-${run}/mask.nii.gz \
               -expr 'c * min(200, a/b*100)*step(a)*step(b)' \
               -prefix run-${run}_blur8_scaled
        fi
        
    done
    cd $derDir
done
