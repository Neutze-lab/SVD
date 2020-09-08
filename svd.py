#!/usr/bin/env python3
##################################################
#
# (c) 2020 Adams Vallejos <adams.vallejos@gu.se>
# Version tor  3 sep 2020 16:44:40 CEST
#
##################################################
import shutil
import mrcfile
import sys
import numpy
import os
# USAGE: Type only the names of maps in the input/ folder  below
#       without the '.map' extension, and in time ascending order.
files = [
    'foo_1',
    'foo_2'
]
n = len(files)
mx = mrcfile.open('input/'+str(files[0])+'.map').header.mx
my = mrcfile.open('input/'+str(files[0])+'.map').header.my
mz = mrcfile.open('input/'+str(files[0])+'.map').header.mz
try:
    os.mkdir('output')
    print("Directory " , 'output' ,  " Created ")
except FileExistsError:
    print("Directory " , 'output' ,  " already exists")  
#
shutil.copy('input/'+str(files[0])+'.map','output/'+str('svd_'+str("".join(files))+'.map'))
svd=mrcfile.open('output/'+str('svd_'+str("".join(files))+'.map'),mode='r+')
#
for i in range(n):
    vars()["mrc"+str(i)]= mrcfile.open('input/'+str(files[i]+'.map'),mode='r')
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
svd.set_data(numpy.array(Ar[:,0]).reshape(mrc0.data.shape))
svd.header.mx = mx
svd.header.my = my
svd.header.mz = mz
svd.close()
for i in range(n):
    vars()["mrc"+str(i)].close()
print("SVD on maps performed successfully!")
svd (END)
