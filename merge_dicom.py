import dicom
from numpy import *
import sys 
from lib.dicom_tools import *

# How to use this script:
# 
# The purpose of this script is to merge 2 dicom files, keeping the tags from one while  
# replacing the voxel data with contents from a second file.
#
# Run:
# The script requires three arguments, all of which are unix file paths.  
# The first argument should be a reference to the dicom file we want to use as the template.
# The second argument should be a reference to the dicom file we want to extract voxel data from.
# The third argument should be a file reference to the output file that will be the result 
# of the merge.
#
# Example:
# python original.dcm voxel_data.dcm result.dcm

#Script:

# First, load our 'template' file. We are going to keep the majority of dicom tags 
# from this file while just replacing the voxel data & associated tags.
d = DicomFile(sys.argv[1])

# Next, let's load voxel data from a separate file and replace the voxel data
# in our original file.
d.loadVoxelDataFromFile(sys.argv[2])

# Finally, write the resulting merged dicom file as a new filename.
d.write(sys.argv[3])