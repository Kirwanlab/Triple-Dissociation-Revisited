#!/bin/bash

# Blur the functional datasets

derDir=/Volumes/Yorick/fMRI_Replication/derivatives/

cd $derDir
# for i in `cat ../subjList.txt`; do
#     cd sub-$i
#     3dmerge -prefix run-4_blur8 -1blur_fwhm 8 -doall func_10_23_2020.run-4/bold.nii.gz
#     cd $derDir
# done


#Kirwan's Code
for i in `cat ../subjList.txt`; do 
    cd sub-$i 
    for ii in 1 2 3 4; do 
#       if [ ! -f run-${ii}_blur8+tlrc.HEAD ]; then 
        3dmerge -prefix run-${ii}_blur8 -1blur_fwhm 8 -doall func_run-${ii}/bold.nii.gz 
#       fi 
    done 
    cd $derDir
done

for ii in 1 2 3 4; do 
#       if [ ! -f run-${ii}_blur8+tlrc.HEAD ]; then 
    3dmerge -prefix run-${ii}_blur8 -1blur_fwhm 8 -doall func_run-${ii}/bold.nii.gz 
#       fi 
done