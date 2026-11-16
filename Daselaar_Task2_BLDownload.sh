#!/bin/bash

#script modified from https://brainlife.io/docs/cli/download/

#May need to log in to brain life with this command:
# bl login --ttl 7


#Then  you can get the project ID with:
#bl project query -a kirwan@byu.edu

#Which subjects do you want to download? (Sub-054 is has issues with one of its runs on fMRIPrep)
subjects=(002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 052 053 054 055 056 057 058 059 060)

#Variables to be updated for each project:
derDir=/Volumes/Yorick/fMRI_Replication/derivatives
project=07-06-2021

#These may need to be updated depending on what you need to download. These two arrays should be exactly the same length.
datatype=("report/html")
output=(report)
filenames=(html)

#Work:
outputLen=${#output[@]}
subLen=${#subjects[@]}

cd $derDir

#loop over subjects
for (( sub=0; sub<$subLen; sub++ ))
    do
    
    echo "downloading subject: ${subjects[$sub]} --------------"
    mkdir -p $derDir/sub-${subjects[$sub]}
    
    #loop over dataset type within that subject
    for (( i=0; i<$outputLen; i++ ))
        do
        echo "working on datatype: ${output[$i]} ------------"
        
        #cache the list of datasets that we could download
        bl dataset query --datatype ${datatype[$i]} --project $project --json --subject ${subjects[$sub]} >  ${output[$i]}.json

        #loop over the scan IDs
        for id in $(jq -r '.[] | ._id' ${output[$i]}.json)
            do
            tags=$(jq -r '.[] | select(._id=='\"$id\"') | .tags | join(".")' ${output[$i]}.json)
             echo $id $tags
             outdir=$derDir/sub-${subjects[$sub]}/${output[$i]}_$tags
             echo $outdir
             if [ ! -f ${outdir}/${filenames[$i]} ]; then
                bl dataset download --id $id --directory $outdir
             fi
        done        
    done

    #the above is throwing an error when I try to get the "neuro/func/task" datatype list. Try again with the "preprocessed" datatype_tag
    #kludge for func data only

    bl dataset query --datatype_tag "preprocessed" --project $project --json --subject ${subjects[$sub]} >  func.json
    #loop over the scan IDs
    for id in $(jq -r '.[] | ._id' func.json)
        do
        tags=$(jq -r '.[] | select(._id=='\"$id\"') | .tags | join(".")' func.json)
        echo $id $tags
        outdir=$derDir/sub-${subjects[$sub]}/func_$tags
        echo $outdir
        if [ ! -f ${outdir}/bold.nii.gz ]; then
            bl dataset download --id $id --directory $outdir
        fi
    done   
done


