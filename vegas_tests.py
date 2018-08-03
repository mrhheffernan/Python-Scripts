# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:33:41 2017

@author: mheffernan

Sandbox for implementation of vegas
"""
import time
import vegas
import math
#import scipy.integrate as si

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
    func = math.exp(-100*g)* 1013.2118364296088    
    return func

def main():
    integ = vegas.Integrator([-1, 1], [0, 1], [0, 1], [0, 1])   #Okay, so something with the range is critical to passing variables from vegas

    result = integ(vf, nitn=10, neval=1000)
    if integ.mpi_rank ==0:    
        print(result.summary())
        print('result = %s    Q = %.2f' % (result, result.Q))
        print('result type = ',type(result.mean))
        print('result mean = ',result.mean)
        end = time.time()
        time_vegas = end-start
        print('Vegas Time (independent) = ',time_vegas,' s')

if __name__ == '__main__':
    main()

#==============================================================================
# def vf(a,b,c,d):
#     g = (a-0.5)**2 +  (b-0.5)**2  + (c-0.5)**2  + (d-0.5)**2 
#     func = math.exp(-100*g)* 1013.2118364296088    
#     return func
#     
# def vint1(b,c,d):
#     flamb = lambda a: vf(a,b,c,d)
#     integ = vegas.Integrator([[-1, 1]])
#     res = integ(flamb, nitn=10, neval=1000).mean  
#     #res = si.quad(flamb,-1,1,epsrel = tol, epsabs = tol)[0]
#     print('int1 done')
#     return res
#     
# def vint2(c,d):
#     flamb2 = lambda b: vint1(b,c,d)
#     #res2 = si.quad(flamb2,0,1,epsrel = tol, epsabs = tol)[0]
#     integ = vegas.Integrator([[0, 1]])
#     res2 = integ(flamb2, nitn=10, neval=1000).mean      
#     print('int2 done')
#     return res2
# 
# def vint3(d):
#     flamb3 = lambda c: vint2(c,d)
#     res3 = si.quad(flamb3,0,1,epsrel = tol, epsabs = tol)[0]
#     global count
#     count = count+1
#     print('int3 done ',count)
#     return res3
# 
# def vint4():
#     #flamb4 = lambda d: int3(d)
#     res4 = si.quad(vint3,0,1)[0]
#     return res4
# 
# 
# #==============================================================================
# # def main2():
# #     start_siv = time.time()
# #     res_finalv = vint4()
# #     end_siv = time.time()
# #     time_siv = end_siv - start_siv
# #     print('Nested Vegas Result = ',res_finalv)
# #     print('Nested Vegas Time = ',time_siv)
# #     
# # if __name__ == '__main__':
# #     main2()
# #==============================================================================
#     
# def f(a,b,c,d):
#     g = (a+b+c+d)
#     func = g**2
#     return func
#     
# def int1(b,c,d):
#     flamb = lambda a: f(a,b,c,d)    
#     res = si.quad(flamb,-1,1,epsrel = tol, epsabs = tol)[0]
#     #print('int1 done')
#     return res
#     
# def int2(c,d):
#     flamb2 = lambda b: int1(b,c,d)
#     res2 = si.quad(flamb2,0,1,epsrel = tol, epsabs = tol)[0]
#     #print('int2 done')
#     return res2
# 
# def int3(d):
#     flamb3 = lambda c: int2(c,d)
#     res3 = si.quad(flamb3,0,1,epsrel = tol, epsabs = tol)[0]
#     global count
#     count = count+1
#     print('int3 done ',count)
#     return res3
# 
# def int4():
#     #flamb4 = lambda d: int3(d)
#     res4 = si.quad(int3,0,1)[0]
#     return res4
# 
# def main3():    
#     start_si = time.time()
#     res_final = int4()
#     end_si = time.time()
#     time_si = end_si - start_si
#     
#     #time_fac = time_si/time_vegas
#     print('final result scipy = ',res_final)
#     print('time scipy = ',time_si)
# 
# if __name__ == '__main__':
#     main3()
# 
#==============================================================================
