"""Usage: vegas_tests.py [--test_pass=N]

Options:
    --test_pass=N Sets a test passed variable which can be included in a function
"""

#These are test functions which demonstrate different methods of numerical
#    integration in the VEGAS adaptive Monte Carlo framework.
#    
#This is modified from the documentation to include command-line argument passing
#    using docopt

import time
import vegas
import math
from docopt import docopt
import scipy.integrate as si

params = {'scaling':1013.2118364296088}

# Implementing passing of command line arguments
arguments = docopt(__doc__, version='version')

if arguments['--scaling'] != None:
    params['scaling'] = float(arguments['--scaling'])

tol=10

start = time.time()

global count

count = 0

def f(x):
    dx2 = 0
    for d in range(4):
        dx2 += x[d]
    return (dx2)**2

def vf(a,b,c,d):
    g = (a-0.5)**2 +  (b-0.5)**2  + (c-0.5)**2  + (d-0.5)**2 
    func = math.exp(-100*g)*params['scaling']    
    return func

def main():
    integ = vegas.Integrator([-1, 1], [0, 1], [0, 1], [0, 1])  # Passing ranges for multidimensional integration

    result = integ(vf, nitn=10, neval=1000)
    if integ.mpi_rank ==0:    
        print(result.summary())
        print('result = %s    Q = %.2f' % (result, result.Q))
        print('result type = ',type(result.mean))
        print('result mean = ',result.mean)
        end = time.time()
        time_vegas = end-start
        print('Vegas Time (multidimensional) = ',time_vegas,' s')

if __name__ == '__main__':
    main()

# Now, we demonstrate a test of nesting integrations with naive variable passing
# This demonstrates the advantages of VEGAS' multidimensional functionality
    
def vint1(b,c,d):
    flamb = lambda a: vf(a,b,c,d)
    integ = vegas.Integrator([[-1, 1]])
    res = integ(flamb, nitn=10, neval=1000).mean  
    print('int1 done')
    return res
     
def vint2(c,d):
    flamb2 = lambda b: vint1(b,c,d)
    integ = vegas.Integrator([[0, 1]])
    res2 = integ(flamb2, nitn=10, neval=1000).mean      
    print('int2 done')
    return res2
 
def vint3(d):
    flamb3 = lambda c: vint2(c,d)
    integ = vegas.Integrator([[0, 1]])
    res3 = integ(flamb3, nitn=10, neval=1000).mean
    global count
    count = count+1
    print('int3 done ',count)
    return res3
 
def vint4():
    integ = vegas.Integrator([[0, 1]])
    res4 = integ(vint3, nitn=10, neval=1000).mean
    return res4

def sint1(b,c,d):
    flamb = lambda a: vf(a,b,c,d)
    res = si.quad(flamb, -1, 1, epsrel=tol, epsabs=tol)[0]
    print('int1 done')
    return res
     
def sint2(c,d):
    flamb2 = lambda b: sint1(b,c,d)
    res2 = si.quad(flamb2, 0, 1, epsrel=tol, epsabs=tol)[0]   
    print('int2 done')
    return res2
 
def sint3(d):
    flamb3 = lambda c: sint2(c,d)
    res3 = si.quad(flamb3, 0, 1, epsrel=tol, epsabs=tol)[0]
    global count
    count = count+1
    print('int3 done ',count)
    return res3
 
def sint4():
    res4 = si.quad(sint3,0,1)[0]
    return res4
 

def main2():
    start_vegas = time.time()
    result_vegas = vint4()
    end_vegas = time.time()
    time_vegas = end_vegas - start_vegas
    
    start_scipy = time.time()
    result_scipy = sint4()
    end_scipy = time.time()
    time_scipy = end_scipy - start_scipy
    
    
    print('Nested Vegas Result = ',result_vegas)
    print('Nested Vegas Time = ',time_vegas)
    
    print('Nested SciPy Result = ',result_scipy)
    print('Nested Scipy Time = ',time_scipy)
     
if __name__ == '__main__':
    main2()
