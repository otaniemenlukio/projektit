#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:47:12 2020

@author: maccomputer
"""

import numpy as np
from scipy import ndimage as ndi
from skimage.io import imread
from skimage.color import rgb2gray, gray2rgb
import matplotlib.pylab as plt

image = rgb2gray(imread('bike.jpg'))
width, height = image.shape

matrix_identity = np.array([[1,0,0],[0,1,0],[0,0,1]])
matrix_reflect = np.array([[1,0,0],[0,-1,0],[0,0,1]]) @ np.array([[1,0,0],[0,1,-height],[0,0,1]])

im1 = ndi.affine_transform(image, matrix_identity)
im2 = ndi.affine_transform(image, matrix_reflect)
#im1 = gray2rgb(image)

plt.figure(figsize=(40,20))
plt.subplot(121), plt.imshow(im1), plt.axis('on'), plt.title('original', size=20)
plt.subplot(122), plt.imshow(im2), plt.axis('on'), plt.title('reflected image', size=20)
plt.show()
