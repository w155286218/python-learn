#coding:utf-8  
'''
Created on 2016年4月14日

@author: Charlie
'''

from numpy import *  
  
def loadData():  
    return [[1,1,1,0,0],  
             [2,2,2,0,0],  
             [3,3,3,0,0],  
             [5,5,3,2,2],  
             [0,0,0,3,3],  
             [0,0,0,6,6]]  
  
data=loadData()  
print shape(data)
u,sigma,vt=linalg.svd(data)  
 
'''print u
print sigma  
print vt'''
  
sig3=mat([[sigma[0],0,0],  
      [0,sigma[1],0],  
      [0,0,sigma[2]]])  
  
print u[:,:3]*sig3*vt[:3,:]  