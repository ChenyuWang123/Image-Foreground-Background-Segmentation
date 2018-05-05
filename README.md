Image-Foreground-Background-Segmentation
====
## Introduction
Our target is to design and implement an algorithm to segment any input images into foreground and background. For basic task, we have used cluster classification, combining with Network Flow to achieve this goal. All the input images are down-sampled and compressed firstly to make the processing more efficient. For the second step, we have implement cluster method GMM, K-means and our extension part to get improved cluster result. After that, Network Flow has be accomplished to label and divide pixels into two groups, which represents background and foreground. 

For extension part, we have designed an application to remove certain part of image interactively, and have made attempts and exploration on a more efficient method. The new method developed by ourselves performed a more stable performance than the other two.


## Installation (Windows)
1. Install QT 4.6

     https://www.qt.io/download

2. Install Python 3

     https://www.python.org/downloads/

3. Install `matplotlib`, `pylab`, `numpy`, `sklearn`, `cv2`， `scipy`, `PIL` , `copy` for Python

4. Unzip all project files and open the 'obj' file in QT platform

5. Unfold the folder on the left bar and double click the 'obj' file, entering edit mode

6. 
