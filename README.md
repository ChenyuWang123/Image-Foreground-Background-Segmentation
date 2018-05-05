Image-Foreground-Background-Segmentation
====
## Introduction
Our target is to design and implement an algorithm to segment any input images into foreground and background. For basic task, we have used cluster classification, combining with Network Flow to achieve this goal. All the input images are down-sampled and compressed firstly to make the processing more efficient. For the second step, we have implement cluster method GMM, K-means and our extension part to get improved cluster result. After that, Network Flow has be accomplished to label and divide pixels into two groups, which represents background and foreground. 

<div align=center><img width="150" height="80" src="https://github.com/ChenyuWang123/Image-Foreground-Background-Segmentation/blob/master/down3.png"/></div> 
<div align=center><img width="150" height="80" src="https://github.com/ChenyuWang123/Image-Foreground-Background-Segmentation/blob/master/down4.png"/></div>

For extension part, we have designed an application to remove certain part of image interactively, and have made attempts and exploration on a more efficient method. The new method developed by ourselves performed a more stable performance than the other two.

<div align=center><img width="200" height="200" src="https://i1.kknews.cc/SIG=t0eajp/288r00028791qn583976.jpg"/></div> 

## C++ Version Installation Guide (Windows)
1. Install QT 4.6

     https://www.qt.io/download

2. Install Python 3

     https://www.python.org/downloads/

3. Install `matplotlib`, `pylab`, `numpy`, `sklearn`, `cv2`，`scipy`, `PIL` , `copy` for Python

4. Unzip all project files and open the `*.pro` file in QT platform

5. Unfold the folder on the left bar and double click the `*.pro` file, entering edit mode

6. Add these two lines to the file (different PC varies):

     `INCLUDEPATH +=C:/Python36/include/`

     `LIBS += C:/Python36/libs/python36.lib`
     
7. Open `pyconfig.h` and modify as follows

     `#ifdef _DEBUG` 
     
     `//# define Py_DEBUG` 
     
     `#endif`
     
8. Open `object.h` and modify as follows

     `#if defined(Py_DEBUG) && !defined(Py_TRACE_REFS)`
     
     `// #define Py_TRACE_REFS`
     
     `#endif`
     
9. Make sure the compiler runs in `MSVC 2017 64 bits` and `debug` mode, start!
     
## Python Version Installation Guide

1. Download the file from our GitHub

2. Install `matplotlib`, `pylab`, `numpy`, `sklearn`, `cv2`，`scipy`, `PIL` , `copy` for Python(Using pip install 'libraray name' in the command line)

3. Drag any picutes you need to the file

4. Using "Python UI_python.py" command in the command line to run the UI

5. Upload the image form your computer, click any point you care about in the picture, and click "Sever Image" button to run the program. It will takes about 2-8 minutes to finish the process(It depends on the size of your input picture)

6. You could see the forground or background picture in the window and both pictures will be saved in the file called "one.bmp" and "two.bmp".
