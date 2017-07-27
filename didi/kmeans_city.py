# -*- coding: utf-8 -*-  
import numpy as np  
from sklearn import neighbors    
import pandas as pd
from sklearn.cluster import KMeans ,k_means
from scipy import sparse
from sklearn.externals import joblib

def city_cluster(city_data):
    
    x_p=city_data[:,:4]
    
    clf=KMeans(n_clusters=4)
    xp_pred=clf.fit(x_p)
    
    #print clf.labels_
    #print clf.cluster_centers_
    print("labels:",clf.labels_)  
    print clf.inertia_
    #进行预测
    print clf.predict(x_p)
    #保存模型
    joblib.dump(clf, '/Users/didi/Documents/city_cluster/km0522_03.pkl')
    #载入保存的模型
    #clf = joblib.load('/Users/didi/Documents/city_cluster/')
    
    i = 1  
    label_dict={}
    j=1
    while j <= len(clf.labels_):  
        label_dict[clf.labels_[j-1]]=0
        j = j+1
        
    while i <= len(clf.labels_):  
        label_dict[clf.labels_[i-1]]=label_dict[clf.labels_[i-1]]+1
        print  clf.labels_[i-1]  
        i = i + 1  
    print label_dict
    
def city_pridict(city_data):
    x_p=city_data[:,:4]
    clf = joblib.load('/Users/didi/Documents/city_cluster/km1.pkl')
    clf.predict(x_p)
    
    i = 1  
    label_dict={}
    j=1
    while j <= len(clf.labels_):  
        label_dict[clf.labels_[j-1]]=0
        j = j+1
        
    while i <= len(clf.labels_):  
        label_dict[clf.labels_[i-1]]=label_dict[clf.labels_[i-1]]+1
        print  clf.labels_[i-1]  
        i = i + 1  
    print label_dict
    
if __name__=="__main__":
    city_data=np.loadtxt('/Users/didi/Documents/city_cluster/city_cluster1.txt')
    city_cluster(city_data)
    #city_pridict(city_data)
    