#!/usr/bin/env pytheigthon3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:42:52 2020

@autheigthor: maccomputer
"""

import numpy as np
from scipy import ndimage as ndi
import matplotlib.pylab as plt

image = plt.imread('bike.jpg')
width, height, channels = image.shape

im_R = image[...,0]
im_G = image[...,1]
im_B = image[...,2]


angle = np.pi

matrix_identity = np.array([[1,0,0],[0,1,0],[0,0,1]])
# matrix_reflect = np.array([[1,0,0],[0,-1,0],[0,0,1]]) @ np.array([[1,0,0],[0,1,-height],[0,0,1]])

matrix_move = np.array([[1,0,width/2],[0,1,height/2],[0,0,1]]) 
matrix_rotate =  np.array([[np.cos(angle),np.sin(angle),0],[np.sin(angle),-np.cos(angle),0],[0,0,1]])
matrix_move_back =  np.array([[1,0,-width/2],[0,1,-height/2],[0,0,1]])
matrix_flip = matrix_move @ matrix_rotate @ matrix_move_back

#im1 = ndi.affine_transform(image, matrix_identity)
#im2 = np.flip(image,1) # flip horizontally
im1 = ndi.affine_transform(image, matrix_flip)
im_R = ndi.affine_transform(im_R, matrix_flip)
im_G = ndi.affine_transform(im_G, matrix_flip)
im_B = ndi.affine_transform(im_B, matrix_flip)

im1[...,0]=im_R
im1[...,1]=im_G
im1[...,2]=im_B

print(channels)


plt.figure()
plt.subplot(131), plt.imshow(im1), plt.axis('off'), plt.title('original', size=20)
plt.subplot(132), plt.imshow(im_G), plt.axis('off'), plt.title('reflected', size=20)
plt.subplot(133), plt.imshow(im_B), plt.axis('off'), plt.title('flipped', size=20)
plt.show()