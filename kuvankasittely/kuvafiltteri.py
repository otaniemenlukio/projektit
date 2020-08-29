#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Aug 26 19:30:39 2020
    
    @author: maccomputer
    based on
    https://www.codementor.io/@isaib.cicourel/image-manipulation-in-python-du1089j1u
"""
    
from PIL import Image
    

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

    new.show()
    return new

def invert_colors(image):
    width, height = image.size
    new = create_image(width, height)
    pixels = new.load()

    
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)
            red =  abs(255-pixel[0])
            green = abs(255-pixel[1])
            blue = abs(255-pixel[2])
   
            pixels[i, j] = (red, green, blue)

    new.show()
    return new

def main():
    original = open_image('mtb_ruunaa.jpeg')
    
       
    print('Color: ' + str(get_pixel(original, 0, 0)))
    
    
    new_gray = convert_to_gray(original)
    save_image(new_gray, 'mtb_ruunaa_harmaa.jpeg')
   
    new_inverted = invert_colors(original)
    save_image(new_inverted, 'mtb_ruunaa_inverted.jpeg')

main()