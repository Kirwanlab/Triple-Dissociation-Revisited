#Move behavioral files from Derivatives to Raw Data
for subj in `cat subjList.txt`; do mv derivatives/sub-${subj}/Sub-${subj}_task-RecogConf_run-* rawdata/sub-${subj}/func; done


# To change directory permissions in Linux, use the following:

# chmod +rwx filename to add permissions.
# chmod -rwx directoryname to remove permissions.
# chmod +x filename to allow executable permissions.
# chmod -wx filename to take out write and executable permissions.
# Note that “r” is for read, “w” is for write, and “x” is for execute. 

