"""
This function takes a mean of several umatricies calculated with np.mean and recasts it as a unumpy umatrix.

Suppose c1, c2, c3 are all matricies with uncertainties. np.mean([c1,c2,c3],axis=0) will return an array, but the errors and the nominal values cannot be called anymore. This simple function recasts the array as a umatrix so it can be manipulated in the same way.

Copyright 2019 Matthew Heffernan <heffernan@physics.mcgill.ca>

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
"""

import numpy as np
from uncertainties import unumpy

def umatmean(mat):
    
    sizex, sizey = mat.shape
    nom = np.zeros(mat.shape)
    stdvs = np.zeros(mat.shape)
    
    for i in range(sizex):
        for j in range(sizey):
            nom[i][j] = mat[i][j].n
            stdvs[i][j] = mat[i][j].s
    
    umat = unumpy.umatrix(nom,stdvs)
    
    return umat
