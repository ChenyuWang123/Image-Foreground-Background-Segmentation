# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 18:05:23 2018

@author: Chenyu
"""
from matplotlib import pyplot as plt
import copy
import cv2
import pylab
import os
import numpy as np
from PIL import Image

def readfile(filename):  
    with open(filename,'r') as f:  
        for line in f.readlines(): 
            linestr = line.strip(',')
            linestrlist = linestr.split("\t")
            return linestrlist

def ccombo(address1, address2, x1, x2):       
    imagefile = plt.imread(address1)
    height, width, _ = imagefile.shape
    n1 = int(height/5)
    n2 = int(width/5)
#    n1 = 100
#    n2 = 100
    
    downSample = cv2.resize(imagefile,(n2,n1), interpolation = cv2.INTER_CUBIC)
    sampleHeight, sampleWidth, _ = downSample.shape
          
    linelist = readfile(address2) 
    list1 = []
    for i in linelist[0]:
        if i != ',':
            list1.append(int(i))
    list1 = np.array(list1, dtype = float)
    list1 = list1.reshape(sampleHeight, sampleWidth, 1).astype('float64')
    
    temp = downSample
    one = copy.deepcopy(temp)
    two = copy.deepcopy(temp)
    for i in range(n1):
        for j in range(n2):
            if(list1[i][j] == 1):
                one[i][j] = [0,0,0]
            else:
                two[i][j] = [0,0,0]
    plt.imshow(one)
    pylab.show()
    plt.figure()
    newone = Image.fromarray(one.astype(np.uint8))
    newone.save('one.bmp')
#    np.savetxt("filename.txt",one,fmt="%s",delimiter=",")
#    plt.figure()
    newtwo = Image.fromarray(two.astype(np.uint8))
    newtwo.save('two.bmp')
#    my_file = 'C:/Users/Chenyu/Desktop/EC504/Project/one.bmp'
#    if os.path.exists(my_file):
#        print(1)
#        os.remove(my_file)
    plt.imshow(two)
    pylab.show()

if __name__ == '__main__':
    address1 = '2.jpg'
    address2 = 're.txt'
    ccombo(address1, address2, 1,2)