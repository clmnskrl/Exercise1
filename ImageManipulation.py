import cv2
import numpy as np
import Utilities

# Example for basic pixel based image manipulation:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

# Task 1:   Implement some kind of noticeable image manipulation in this function
#           e.g. channel manipulation, filter you already know, drawings on the image etc.
def myFirstImageManipulation(img):
    #cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return 0



# Task 2:   Print the basic image properties to the console:
#           width, height, number of channels, number of pixels, pixel type,
#           the color of the first pixel of the image,
#           Color of the first pixel in the second row
#           Color of the first pixel in the second column
#           This function should work for color and for grayscale images
def printImageDetails(img):    
    image_metadata = {
        'width': img.shape[1],
        'height': img.shape[0],
        'channels': img.shape[2] if img.ndim == 3 else 1,
        'pixels': img.shape[0]*img.shape[1],
        'pixel_type': "rgb" if img.ndim == 3 else "grayscale"
    }

    print('image properties:\n'
          f' image width: {image_metadata["width"]}\n'
          f' image height: {image_metadata["height"]}\n'
          f' number of channels: {image_metadata["channels"]}\n'
          f' number of pixels: {image_metadata["pixels"]}\n'
          f' pixel type: {image_metadata["pixel_type"]}\n'
          f' color of first pixel in first row: {Utilities.color_name(img[0,0])}\n'
          f' color of first pixel in second row: {Utilities.color_name(img[1,0])}\n'
          f' color of first pixel in second column: {Utilities.color_name(img[0,1])}\n'
          )
    return 0



# Task 3:   Seperate the three channels of a colour image in this function and return them as separate images
#           
def separateChannels(img):

    return 0
