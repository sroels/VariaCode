#!/usr/bin/python
import sys
import numpy as np
import os
import nibabel as nib

#HOW TO USE this file
# it takes 4 arguments sys.argv[0] is the command itself
old_path=sys.argv[1]
new_path=sys.argv[2]
old_file=sys.argv[3]
new_file=sys.argv[4]

#"/Users/pp01sanne/Downloads/"
#'preproc_2.nii'
#
#
#"/Users/pp01sanne/Downloads/"
print(old_path)
print(new_path)
print(old_file)
print(new_file)

# load the nifti file
example_ni1 = os.path.join(old_path, old_file)
n1_img = nib.load(example_ni1)
# change the header [2]
n1_img.header['pixdim']=np.array([ 1.,  1.,  1.,  1.,  2.,  0.,  0.,  0.])
# get the data for the EXPLICIT new image - no over writing
data=n1_img.get_data()
affine=n1_img.get_affine()
# make the new image 
new_img = nib.Nifti1Image(data, affine, header=n1_img.header)
# save the new image
nib.save(new_img, os.path.join(new_path, new_file))
#print(new_img.header)