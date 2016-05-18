import numpy as np
import os
import nibabel as nib
# set data_path -> fix it in a loop
data_path="/Users/pp01sanne/Downloads/"
# load the nifti file
example_ni1 = os.path.join(data_path, 'preproc_2.nii')
n1_img = nib.load(example_ni1)
# change the header [2]
n1_img.header['pixdim']=np.array([ 1.,  1.,  1.,  1.,  2.,  0.,  0.,  0.])
# get the data for the EXPLICIT new image - no over writing
data=n1_img.get_data()
affine=n1_img.get_affine()
# make the new image 
new_img = nib.Nifti1Image(data, affine, header=n1_img.header)
# save the new image
nib.save(new_img, os.path.join(data_path,'test4d.nii.gz'))
print(new_img.header)