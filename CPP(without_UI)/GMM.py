import cv2
import numpy as np
from sklearn import mixture
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial import distance
import time

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
    print(num)
    return likelihoodList 

def GMMcluster(RPGmatrix, sampleHeight, sampleWidth):
    GMMclassifier = mixture.GaussianMixture(n_components=3, covariance_type='full', max_iter=500, n_init=5)
    GMMclassifier.fit(RPGmatrix)
    GMMpredict = GMMclassifier.predict(RPGmatrix)
    GMMpr = GMMclassifier.predict_proba(RPGmatrix)
    pre = GMMpredict.reshape(-1,1)
    pre = pre.reshape(sampleHeight, sampleWidth).astype('float16')
    return GMMpr

def combo(address):
    imagefile = plt.imread(address)
    height, width, _ = imagefile.shape
    n1 = int(height/5)
    n2 = int(width/5)
    
    downSample = cv2.resize(imagefile,(n2,n1), interpolation = cv2.INTER_CUBIC)
    sampleHeight, sampleWidth, _ = downSample.shape
    RPGmatrix = np.concatenate((downSample[:,:,0].flatten().reshape(-1,1), downSample[:,:,1].flatten().reshape(-1,1), downSample[:,:,2].flatten().reshape(-1,1)),axis=1)
    
    prob = GMMcluster(RPGmatrix, sampleHeight, sampleWidth)
    prob1 = prob.reshape(sampleHeight, sampleWidth, 3).astype('float64')
    
    Gmmpre = getLikelihood(prob, n1, n2, prob1)    
    f=open('demo.txt','w')
    for i in Gmmpre:
        k=' '.join([str(j) for j in i])
        f.write(k+"\n")
    f.close()

if __name__ == '__main__':
    address = '2.jpg'
    combo(address)
