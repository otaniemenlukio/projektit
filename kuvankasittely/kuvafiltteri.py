#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Aug 26 19:30:39 2020
    
    @author: maccomputer
    Documentation of PILLOW: https://pillow.readthedocs.io/en/5.1.x/index.html
    
    tutorial: 
    https://pillow.readthedocs.io/en/3.0.0/handbook/tutorial.html#geometrical-transforms
    
    examples:
    https://www.codementor.io/@isaib.cicourel/image-manipulation-in-python-du1089j1u
"""
    
from PIL import Image, ImageFilter
    

def open_image(path):
    newImage = Image.open(path)
    return newImage

def save_image(image, path):
    image.save(path, 'png')
  

def create_image(i, j):
    image = Image.new("RGB", (i, j), color="white" )
    return image

def get_pixel(image, i, j):
    
    width, height = image.size
    if i > width or j > height:
        return None

    
    pixel = image.getpixel((i, j))
    return pixel


def convert_to_gray(image):
    width, height = image.size
    new = create_image(width, height)
    pixels = new.load()

    
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)
            red =  pixel[0]
            green = pixel[1]
            blue = pixel[2]
            gray = int((red+green+blue)/3)
   
            pixels[i, j] = (gray, gray, gray)

    #new.show()
    return new

def invert_colors(image):
    width, height = image.size
    new = create_image(width, height)
    pixels = new.load()

    
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)
            red =  255 - pixel[0]
            green = 255 - pixel[1]
            blue = 255 - pixel[2]
   
            pixels[i, j] = (red, green, blue)

    #new.show()
    return new


def main():
    original = open_image('bike.jpg')
    
       
    print('Color: ' + str(get_pixel(original, 0, 0)))
    
    
    im1 = convert_to_gray(original)
    im1.show()
    #save_image(im1, 'imgage_gray.jpg')
   
    im2 = invert_colors(original)
    im2.show()
    #save_image(im2, 'image_inverted.jpg')
    
    '''
    FILTERS: 
        BLUR, 
        CONTOUR
        DETAIL
        EDGE_ENHANCE
        EDGE_ENHANCE_MORE
        EMBOSS
        FIND_EDGES
        SHARPEN
        SMOOTH
        SMOOTH_MORE
    '''
    im3 = original.filter(ImageFilter.CONTOUR)
    im3.show()
    
    im4 = original.filter(ImageFilter.FIND_EDGES)
    im4.show()
    
    im5 = original.filter(ImageFilter.EMBOSS)
    im5.show()
    
    im6 = original.filter(ImageFilter.EDGE_ENHANCE)
    im6.show()
    
    '''
    Transposing of image:
    transpose(Image.FLIP_LEFT_RIGHT)
    FLIP_TOP_BOTTOM    
    FLIP_LEFT_RIGHT
    ROTATE_90, ROTATE_180
    
    img.rotate(90)
    img.resize((256, 256))
    
    
    Crop:
    borders = (200, 200, 800, 800)
    crop = img.crop(borders)
    '''
    
    im6 = original.transpose(Image.FLIP_LEFT_RIGHT)
    im6.show()
    
    
    

main()