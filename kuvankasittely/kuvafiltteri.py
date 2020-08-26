#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Created on Wed Aug 26 19:30:39 2020
    
    @author: maccomputer
"""
    
from PIL import Image
    
# Open Image
def open_image(path):
    newImage = Image.open(path)
    return newImage
    
# Save Image
def save_image(image, path):
    image.save(path, 'png')
  
# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), color="white" )
    return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

# Create a Grayscale version of the image
def convert_grayscale(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Transform to grayscale
    for i in range(width):
        for j in range(height):
            # Get Pixel
            pixel = get_pixel(image, i, j)
            red =  pixel[0]
            green = pixel[1]
            blue = pixel[2]
            gray = (red+green+blue)/3
   
            # Transform to grayscale
            #gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            # Set Pixel in new image
            pixels[i, j] = (int(gray), int(gray), int(gray))

    new.show()
    return new

# Main
if __name__ == "__main__":
    # Load Image (JPEG/JPG needs libjpeg to load)
    original = open_image('kuva_matti.png')

    # Example Pixel Color
    print('Color: ' + str(get_pixel(original, 0, 0)))

    # Convert to Grayscale and save
    new = convert_grayscale(original)
    save_image(new, 'kuva_matti_harmaa.png')
