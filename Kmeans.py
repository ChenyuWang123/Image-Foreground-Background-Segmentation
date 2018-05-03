# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:09:47 2018

@author: Chenyu
"""
import cv2
#import sys
import numpy as np
#from sklearn import mixture
from matplotlib import pyplot as plt
#from numba import jit
from sklearn.cluster import KMeans
#from scipy.spatial import distance

#def getLikelihood(newimg):
#    kmeans = KMeans(init='k-means++', n_clusters=2, n_init=100)
#    predict = kmeans.fit_predict(newimg)
##    error = kmeans.inertia_
#    centroids = kmeans.cluster_centers_
##    labels = kmeans.labels_
#    likelihoodList = []
##     segmentedimage = np.zeros(img.shape)
#    num = 0
#    for i in range(n1):
#        for j in range(n2):
#            a = distance.euclidean(prob1[i][j],centroids[0])
#            b = distance.euclidean(prob1[i][j],centroids[1])
#            likelihood1 = a/(a+b)
#            likelihood2 = b/(a+b)
#            if likelihood1 > likelihood2:
#                num+=1
##         if (likelihood > 0.5):
##             segmentedimage[i][j]=1;
#            temp = []
#            temp.append(likelihood1)
#            temp.append(likelihood2)
#            likelihoodList.append(temp)
#    print(num)
#    return likelihoodList 
#
#def GMMcluster(finalmatrix):
#    GMMclassifier = mixture.GaussianMixture(n_components=3, covariance_type='full', max_iter=500, n_init=5)
#    GMMclassifier.fit(finalmatrix)
#    GMMpredict = GMMclassifier.predict(RPGmatrix)
#    GMMpr = GMMclassifier.predict_proba(RPGmatrix)
#    pre = GMMpredict.reshape(-1,1)
#    pre = pre.reshape(sampleHeight, sampleWidth).astype('float16')
#    return GMMpr

if __name__ == '__main__':
    imagefile = plt.imread('C:/Users/Chenyu/Desktop/EC504/Project/2.jpg')
    height, width, _ = imagefile.shape
    n1 = int(height/5)
    n2 = int(width/5)
    
    downSample = cv2.resize(imagefile,(n2,n1), interpolation = cv2.INTER_CUBIC)
    sampleHeight, sampleWidth, _ = downSample.shape
    RPGmatrix = np.concatenate((downSample[:,:,0].flatten().reshape(-1,1), downSample[:,:,1].flatten().reshape(-1,1), downSample[:,:,2].flatten().reshape(-1,1)),axis=1)
    
    kmeans = KMeans(init='k-means++', n_clusters=2, n_init=100)
    predict = kmeans.fit_predict(RPGmatrix)
#    prob = GMMcluster(RPGmatrix)
    prob1 = predict.reshape(sampleHeight, sampleWidth, 1).astype('float64')
    
#    Gmmpre = getLikelihood(prob)
    print(len(predict))
    result = []
    for i in range(len(predict)):
        temp = []
        if (predict[i] == 0):
            temp.append(1)
            temp.append(0)
        else:
            temp.append(0)
            temp.append(1)
        result.append(temp)
    f=open('demoooooo.txt','w')
    for i in result:
        k=' '.join([str(j) for j in i])
        f.write(k+"\n")
    f.close()
