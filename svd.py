#!/usr/bin/env python3
#
# Copyright © 2020 UNIVERSITY OF GOTHENBURG
#                  Department of Chemistry and Molecular Biology
# Copyright © 2020 Adams Vallejos <adams.vallejos@gu.se>
# 
import shutil
import mrcfile
import sys
import numpy
# USAGE: Type only the filenames without the '.map' extension
files = [
    'foo_0',
    'foo_1',
    'foo_2',
    'foo_3',
]
n = len(files)
mx = mrcfile.open(str(files[0])+'.map').header.mx
my = mrcfile.open(str(files[0])+'.map').header.my
mz = mrcfile.open(str(files[0])+'.map').header.mz
for i in range(n):
    shutil.copy(str(files[i])+'.map',str(files[i]+'_svd'+'.map'))
    vars()["mrc"+str(i)]= mrcfile.open(str(files[i]+'_svd'+'.map'),mode='r+')
if mrc0.data.shape == (locals()['mrc'+str(i)]).data.shape :
    m = numpy.prod(mrc0.data.shape)
    A = numpy.zeros((m,n),dtype=numpy.float32)
else :
    sys.exit('Unequal map dimensions')
for i in range(n):
    A[:,i] = (locals()['mrc'+str(i)]).data.reshape(-1)       
cov = A.T @ A 
L,V = numpy.linalg.eig(cov)
S1 = numpy.sqrt(L[0])
U1 = numpy.matmul(A,V[:,0])/S1
Ar = S1*(numpy.matrix(U1).T)*(numpy.matrix(V[:,0]))
for i in range(n):
    vars()["mrc"+str(i)].set_data(numpy.array(Ar[:,i]).reshape(mrc0.data.shape))
for i in range(n):
    vars()["mrc"+str(i)].header.mx = mx
    vars()["mrc"+str(i)].header.my = my
    vars()["mrc"+str(i)].header.mz = mz
    vars()["mrc"+str(i)].close()
print("SVD on maps performed successfully!")
