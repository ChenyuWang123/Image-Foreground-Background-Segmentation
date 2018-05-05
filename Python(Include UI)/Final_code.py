#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:07:01 2018

@author: Chenyu
"""

import copy
import cv2
import numpy as np
import pylab
from PIL import Image
from sklearn import mixture
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import distance

def getLikelihood(newimg, n1, n2, prob1):
    kmeans = KMeans(init='k-means++', n_clusters=2, n_init=100)
    predict = kmeans.fit_predict(newimg)
    centroids = kmeans.cluster_centers_
    likelihoodList = []
    num = 0
    for i in range(n1):
        for j in range(n2):
            a = distance.euclidean(prob1[i][j],centroids[0])
            b = distance.euclidean(prob1[i][j],centroids[1])
            likelihood1 = a/(a+b)
            likelihood2 = b/(a+b)
            if likelihood1 > likelihood2:
                num+=1
            temp = []
            temp.append(likelihood1)
            temp.append(likelihood2)
            likelihoodList.append(temp)
    return likelihoodList  
class Edge:
    flow = 0
    capacity = 0
    u = 0
    v = 0
    def __init__(self, flow, capacity, u, v):
        self.capacity = capacity
        self.flow = flow
        self.u = u
        self.v = v
        return
    
class Vertex:
    h = 0
    eflow = 0
    def __init__(self, h, eflow):
        self.eflow = eflow
        self.h = h
        return
    
class Graph:
    V = 0
    ver = []
    edge = []

    def __init__(self, m):
        self.V = m
        for i in range(0, m):
            self.ver.append(Vertex(0,0))
        return

    def addEdge(self,u,v,capacity):
        self.edge.append(Edge(0,capacity,u,v))
   
    def preflow(self, s):
        self.ver[s].h = len(self.ver)
        for i in self.edge:
            if i.u == s:
                i.flow = i.capacity
                self.ver[i.v].eflow += i.flow
                self.edge.append(Edge(-i.flow, 0, i.v, s))
            
    def overFlowVertex(self,verr):
        for i in range(1, len(verr)-1):
            if verr[i].eflow>0:
                return i
        return -1
    
    def updateReverseEdgeFlow(self,i,flow):
        u = self.edge[i].v
        v = self.edge[i].u
        for j in self.edge:
            if j.v ==v and j.u ==u:
                j.flow -= flow
                return
        
        self.edge.append(Edge(0,flow,u,v)) 
    def push(self,u):
        for i in range(0, len(self.edge)):
            if self.edge[i].u == u:
                if self.edge[i].flow == self.edge[i].capacity:
                    continue
                if self.ver[u].h > self.ver[self.edge[i].v].h:
                    flow = min(self.edge[i].capacity-self.edge[i].flow, self.ver[u].eflow)
                    self.ver[u].eflow -= flow
                    self.ver[self.edge[i].v].eflow += flow
                    self.edge[i].flow += flow
                    self.updateReverseEdgeFlow(i,flow)
                    return True
        return False
    
    def relabel(self,u):
        mh = float('inf')
        for i in self.edge:
            if i.u == u:
                if i.flow == i.capacity:
                    continue
                if self.ver[i.v].h<mh:
                    mh = self.ver[i.v].h
                    self.ver[u].h = mh+1
                    
    def getMaxFlow(self,s,t):
        self.preflow(s)
        while(self.overFlowVertex(self.ver)!=-1):
            u = self.overFlowVertex(self.ver)
            if not self.push(u):
                self.relabel(u)
        return self.ver[len(self.ver)-1].eflow
    
def GMMcluster(finalmatrix, RPGmatrix, sampleHeight, sampleWidth): # GMM clustering
    GMMclassifier = mixture.GaussianMixture(n_components=3, covariance_type='full', max_iter=500, n_init=5)
    GMMclassifier.fit(finalmatrix)
    GMMpredict = GMMclassifier.predict(RPGmatrix)
    GMMpr = GMMclassifier.predict_proba(RPGmatrix)
    pre = GMMpredict.reshape(-1,1)
    pre = pre.reshape(sampleHeight, sampleWidth).astype('float16')
    return GMMpr  

def readfile(filename):  
    with open(filename,'r') as f:  
        for line in f.readlines(): 
            linestr = line.strip(',')
            linestrlist = linestr.split("\t")
            return linestrlist 

def combo(file, x, y):
    print('Please wait for about two minutes')
    imagefile = plt.imread(file)
    height, width, _ = imagefile.shape
    n1 = int(height/5)
    n2 = int(width/5)
    
    downSample = cv2.resize(imagefile,(n2,n1), interpolation = cv2.INTER_CUBIC)
    sampleHeight, sampleWidth, _ = downSample.shape
    RPGmatrix = np.concatenate((downSample[:,:,0].flatten().reshape(-1,1), downSample[:,:,1].flatten().reshape(-1,1), downSample[:,:,2].flatten().reshape(-1,1)),axis=1)
    
    prob = GMMcluster(RPGmatrix, RPGmatrix, sampleHeight, sampleWidth)
    prob1 = prob.reshape(sampleHeight, sampleWidth, 3).astype('float64')
    
    Gmmpre = getLikelihood(prob, n1, n2, prob1)  
    #Gmmpre = GMMcluster(RPGmatrix)
    
    s=0
    t=len(Gmmpre)+1
    g=Graph(len(Gmmpre)+2)
    for i in range(0, len(Gmmpre)):
        g.addEdge(s,i+1,Gmmpre[i][0])
        g.addEdge(i+1,t,Gmmpre[i][1])
     
    g.getMaxFlow(s,t)
    K = [[0]*n1 for i in range(0,n2)]
    for i in range(0,len(Gmmpre)):
        if g.ver[i+1].h>=g.V:
            K[int(i/n1)][i%n1]=1
        else:
            K[int(i/n1)][i%n1]=0
    
    K = np.array(K, dtype = float)
    list1 = K.reshape(sampleHeight, sampleWidth, 1).astype('float64')
    
    temp = downSample
    one = copy.deepcopy(temp)
    two = copy.deepcopy(temp)
    flag = 1
    x = int(n2/450 * x)
    y = int(n1/350 * y)
    for i in range(n1):
        for j in range(n2):
            if(list1[i][j] == 1):
                one[i][j] = [0,0,0]
                if (x == i and y == j):
                    flag = 2
            else:
                two[i][j] = [0,0,0]
                if (x == i and y == j):
                    flag = 1
                    
    if (flag == 1):
        plt.imshow(one)
        pylab.show()
    if (flag == 2):
        plt.imshow(two)
        pylab.show()
    newone = Image.fromarray(one.astype(np.uint8))
    newone.save('one.bmp')
    newtwo = Image.fromarray(two.astype(np.uint8))
    newtwo.save('two.bmp')
    return one,two

if __name__ == '__main__':
    address = '1.jpg'
    combo(address,2,3)