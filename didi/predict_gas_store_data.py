#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np  
from numpy import genfromtxt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.pipeline import Pipeline  
from sklearn.linear_model import LinearRegression
import pandas as pd
import statsmodels.api as sm


# dataPath = "dataDumpy.csv"  
# deleveryData = genfromtxt(dataPath, delimiter=',')  
# X = deleveryData[:, :-1]  
# Y = deleveryData[:, -1]  

data_set = np.loadtxt('/Users/didi/Documents/driver-community-recommend/gas_store_data.txt')
#gd = pd.read_table('/Users/didi/Documents/driver-community-recommend/gas_store_data.txt')

gas_store_data = np.array(data_set)
X = gas_store_data[:,0:-1]
y = gas_store_data[:,-1:]
#print X, y

###########多元一次
print "                                  多元一次回归                                  "
print "=============================================================================="
regr = linear_model.LinearRegression()
regr.fit(X,y)
regr._residues
print regr
#R2
print regr.score(X, y)
print regr.coef_, regr.intercept_, regr._residues

##########多元二次回归
print "                                  多元二次回归                                  "
print "=============================================================================="
clf = Pipeline([('poly', PolynomialFeatures(degree=2,interaction_only=True)),  
                    ('linear', LinearRegression(fit_intercept=False))])
clf.fit(X,y)
print(clf.named_steps['linear'].coef_)
print clf.score(X, y)

###########OLS
est = sm.OLS(y,X).fit()
print est.summary(), est