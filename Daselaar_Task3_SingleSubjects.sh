#!/bin/bash

#Variables to be updated for each project:
derDir=/Volumes/Yorick/fMRI_Replication/derivatives
#bl_tag=10_23_2020

#These may need to be updated depending on what you've called your runs:
scanRuns=(run-1 run-2 run-3 run-4)

#Work:
scanRunLen=${#scanRuns[@]}
cd $derDir


# Loop through subjects
for sub in sub-*;
    do
    echo "working on subject: $sub ----------"
    cd ${sub}
    
    #clear out old copies of the motion* files
    if [ -f motion.txt ]; then
        rm motion*
    fi

    # Do the motion detection stuff
    for (( i=0; i<$scanRunLen; i++ ))
        do
        echo "working on run: ${scanRuns[$i]} ------------"

        # Create motion regressors from the BL regressor files
        # Use variable $bl_tag to avoid hard-coding something like the "_2_17_2021" tag into the file name. 
        1dcat regressors_${scanRuns[$i]}/regressors.tsv'[trans_x,trans_y,trans_z,rot_x,rot_y,rot_z]' >> motion.txt
            
    done #scan runs loop
    
    
    # Create a single mask per participant from the functional masks from BL for each task specifically
#     if [ ! -f func_mask+tlrc.HEAD ]; then
#         3dmask_tool -union -input mask_${bl_tag}.run-1/mask.nii.gz \
#         -input mask_${bl_tag}.run-2/mask.nii.gz \
#         -input mask_${bl_tag}.run-3/mask.nii.gz \
#         -input mask_${bl_tag}.run-4/mask.nii.gz \
#         -prefix func_mask
#         
#         #make it reflect that it's in MNI space
#         3drefit -view tlrc -space MNI func_mask+orig
#         
#         #resample mask to functional resolution
#         3dresample -master run-1_blur8_scaled+tlrc -prefix func_mask_resamp -input func_mask+tlrc
#         
#     fi

    if [ ! -f func_mask+tlrc.HEAD ]; then
        for run in 1 2 3 4; do
            3dAutomask -clfrac .1 -prefix mask_run-${run} run-${run}_blur8_scaled+tlrc
        done
        3dmask_tool -union -input mask_run-1+tlrc \
        -input mask_run-2+tlrc \
        -input mask_run-3+tlrc \
        -input mask_run-4+tlrc \
        -prefix func_mask
    fi
    
    # Look for large motion events to censor, create censor files

    # deal with any uneven numbers of TRs across blocks
    unset nTRs
    for i in 1 2 3 4; do
        nTRs+=`3dinfo -nt run-${i}_blur8+tlrc`
        nTRs+=" "
    done

    1d_tool.py -infile motion.txt -set_run_lengths $nTRs -overwrite -demean -write motion_demean.txt
    1d_tool.py -infile motion_demean.txt -set_run_lengths $nTRs -overwrite -show_censor_count -censor_prev_TR -censor_motion 0.3 motion
    1d_tool.py -infile motion_demean.txt -set_run_lengths $nTRs -overwrite -split_into_pad_runs motion_demean_split
        
    #display the motion parameters and TRs to be censored
    1dplot -ynames x-trans y-trans z-trans x-rot y-rot z-rot -censor motion_censor.1D -xlabel "TR#" -title "$sub $i" motion.txt &


     #single-subject regression
     if [ ! -f RecogConf_stats+tlrc.HEAD ]; then

        3dDeconvolve -input run-1_blur8_scaled+tlrc run-2_blur8_scaled+tlrc run-3_blur8_scaled+tlrc run-4_blur8_scaled+tlrc\
         -censor motion_censor.1D \
         -mask func_mask+tlrc \
         -polort A \
         -num_stimts 41 \
         -local_times \
         -stim_file 1 motion_demean_split.r01.1D'[0]' -stim_base 1 -stim_label 1 trans_x.r1 \
         -stim_file 2 motion_demean_split.r01.1D'[1]' -stim_base 2 -stim_label 2 trans_y.r1 \
         -stim_file 3 motion_demean_split.r01.1D'[2]' -stim_base 3 -stim_label 3 trans_z.r1 \
         -stim_file 4 motion_demean_split.r01.1D'[3]' -stim_base 4 -stim_label 4 rot_x.r1 \
         -stim_file 5 motion_demean_split.r01.1D'[4]' -stim_base 5 -stim_label 5 rot_y.r1 \
         -stim_file 6 motion_demean_split.r01.1D'[5]' -stim_base 6 -stim_label 6 rot_z.r1 \
         -stim_file 7 motion_demean_split.r02.1D'[0]' -stim_base 7 -stim_label 7 trans_x.r2 \
         -stim_file 8 motion_demean_split.r02.1D'[1]' -stim_base 8 -stim_label 8 trans_y.r2 \
         -stim_file 9 motion_demean_split.r02.1D'[2]' -stim_base 9 -stim_label 9 trans_z.r2 \
         -stim_file 10 motion_demean_split.r02.1D'[3]' -stim_base 10 -stim_label 10 rot_x.r2 \
         -stim_file 11 motion_demean_split.r02.1D'[4]' -stim_base 11 -stim_label 11 rot_y.r2 \
         -stim_file 12 motion_demean_split.r02.1D'[5]' -stim_base 12 -stim_label 12 rot_z.r2 \
         -stim_file 13 motion_demean_split.r03.1D'[0]' -stim_base 13 -stim_label 13 trans_x.r3 \
         -stim_file 14 motion_demean_split.r03.1D'[1]' -stim_base 14 -stim_label 14 trans_y.r3 \
         -stim_file 15 motion_demean_split.r03.1D'[2]' -stim_base 15 -stim_label 15 trans_z.r3 \
         -stim_file 16 motion_demean_split.r03.1D'[3]' -stim_base 16 -stim_label 16 rot_x.r3 \
         -stim_file 17 motion_demean_split.r03.1D'[4]' -stim_base 17 -stim_label 17 rot_y.r3 \
         -stim_file 18 motion_demean_split.r03.1D'[5]' -stim_base 18 -stim_label 18 rot_z.r3 \
         -stim_file 19 motion_demean_split.r04.1D'[0]' -stim_base 19 -stim_label 19 trans_x.r4 \
         -stim_file 20 motion_demean_split.r04.1D'[1]' -stim_base 20 -stim_label 20 trans_y.r4 \
         -stim_file 21 motion_demean_split.r04.1D'[2]' -stim_base 21 -stim_label 21 trans_z.r4 \
         -stim_file 22 motion_demean_split.r04.1D'[3]' -stim_base 22 -stim_label 22 rot_x.r4 \
         -stim_file 23 motion_demean_split.r04.1D'[4]' -stim_base 23 -stim_label 23 rot_y.r4 \
         -stim_file 24 motion_demean_split.r04.1D'[5]' -stim_base 24 -stim_label 24 rot_z.r4 \
         -stim_times 25 timing/cr-1.txt 'BLOCK(3.4,1)'    -stim_label 25 CR1 \
         -stim_times 26 timing/cr-2.txt 'BLOCK(3.4,1)'    -stim_label 26 CR2 \
         -stim_times 27 timing/cr-3.txt 'BLOCK(3.4,1)'    -stim_label 27 CR3 \
         -stim_times 28 timing/cr-4.txt 'BLOCK(3.4,1)'    -stim_label 28 CR4 \
         -stim_times 29 timing/fa-1.txt 'BLOCK(3.4,1)'    -stim_label 29 FA1 \
         -stim_times 30 timing/fa-2.txt 'BLOCK(3.4,1)'    -stim_label 30 FA2 \
         -stim_times 31 timing/fa-3.txt 'BLOCK(3.4,1)'    -stim_label 31 FA3 \
         -stim_times 32 timing/fa-4.txt 'BLOCK(3.4,1)'    -stim_label 32 FA4 \
         -stim_times 33 timing/hit-1.txt 'BLOCK(3.4,1)'   -stim_label 33 HIT1 \
         -stim_times 34 timing/hit-2.txt 'BLOCK(3.4,1)'   -stim_label 34 HIT2 \
         -stim_times 35 timing/hit-3.txt 'BLOCK(3.4,1)'   -stim_label 35 HIT3 \
         -stim_times 36 timing/hit-4.txt 'BLOCK(3.4,1)'   -stim_label 36 HIT4 \
         -stim_times 37 timing/miss-1.txt 'BLOCK(3.4,1)'  -stim_label 37 MISS1 \
         -stim_times 38 timing/miss-2.txt 'BLOCK(3.4,1)'  -stim_label 38 MISS2 \
         -stim_times 39 timing/miss-3.txt 'BLOCK(3.4,1)'  -stim_label 39 MISS3 \
         -stim_times 40 timing/miss-4.txt 'BLOCK(3.4,1)'  -stim_label 40 MISS4 \
         -stim_times 41 timing/other.txt 'BLOCK(3.4,1)'   -stim_label 41 other \
         -gltsym 'SYM: HIT1 HIT2 HIT3 HIT4 MISS1 MISS2 MISS3 MISS4 -CR1 -CR2 -CR3 -CR4 -FA1 -FA2 -FA3 -FA4' -glt_label 1 Obj_OldNew \
         -gltsym 'SYM: HIT1 HIT2 HIT3 HIT4 -MISS1 -MISS2 -MISS3 -MISS4 -CR1 -CR2 -CR3 -CR4 FA1 FA2 FA3 FA4' -glt_label 2 Sub_OldNew \
         -gltsym 'SYM: 1*CR4 1*MISS4 2*CR3 2*MISS3 3*CR2 3*MISS2 4*FA2 4*HIT2 5*FA3 5*HIT3 6*FA4 6*HIT4'    -glt_label 3 Familiarity \
         -gltsym 'SYM: 6*CR4 6*MISS4 5*CR3 5*MISS3 4*CR2 4*MISS2 3*FA2 3*HIT2 2*FA3 2*HIT3 1*FA4 1*HIT4'    -glt_label 4 Novelty \
         -gltsym 'SYM: 1*CR4 1*MISS4 1*CR3 1*MISS3 1*CR2 1*MISS2 1*FA2 1*HIT2 1*FA3 1*HIT3 6*FA4 6*HIT4'    -glt_label 5 Recollection \
         -gltsym 'SYM: 1*CR4 2*CR3 3*CR2 4*HIT2 5*HIT3 6*HIT4'    -glt_label 6 Corr_Familiarity \
         -gltsym 'SYM: 1*CR4 1*CR3 1*CR2 1*HIT2 1*HIT3 6*HIT4'    -glt_label 7 Corr_Recollection \
         -tout \
         -x1D X.xmat.1D \
         -xjpeg X.jpg \
         -errts RecogConf_errts \
         -bucket RecogConf_stats \
         -GOFORIT 30 \
         -jobs 12
    fi
    
    cd $derDir
done
