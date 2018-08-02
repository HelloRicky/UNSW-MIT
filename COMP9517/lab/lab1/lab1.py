import numpy as np
import cv2
from matplotlib import pyplot as plt
import os.path


## helper functions
##------------------------------------------------------------------------

def crop_img_position(x1, x2):
  """
  find out diff value for different dimension
  return 0 if equal
  """
  
  if x1 < x2:
    return 0, (x2-x1)/2 
  return (x1-x2)/2, 0

def combineImages(img1, img2, imgOut, axis = 1):
  """
  axis = 1 for stacking vertically, 0 for horizontally
  imread(arg1, arg2)
  arg2 = [1, 0, -1], where 1 = color, 0 = grayscale, -1 = unchanged
  """

  h1, w1 = img1.shape
  h2, w2 = img2.shape

  c_h1, c_h2 = crop_img_position(h1, h2)
  c_w1, c_w2 = crop_img_position(w1, w2)

  crop_img1 = img1[c_h1:h1-c_h1, c_w1:w1/2]
  crop_img2 = img2[c_h2:h2-c_h2, w2/2:w2-c_w2]

  _imgOut = np.concatenate((crop_img1, crop_img2), axis = axis)
  cv2.imwrite(imgOut, _imgOut)


def quantization(data, imgOut, level):
  b = 2**level - 1
  new_data = np.round(data/255*b)
  new_data = new_data*(255/b)
  return cv2.imwrite(imgOut, new_data)

def image_enhancement(data, imgOut):
  L = np.max(data)
  new_data = L - 1 - data
  return cv2.imwrite(imgOut, new_data)

def contrast_stretching(data, imgOut):
  a = 0
  b = 255
  c = np.min(data)
  d = np.max(data)
  new_data = (data - c)*((b-a)/(d-c)) + a
  return cv2.imwrite(imgOut, new_data)

def histogram_grey_level(data):

  ## plot graph in line
  plt.figure(1)
  plt.subplot(211)
  plt.imshow(data, cmap='gray')
 

  ## convert to 1d array
  plt.subplot(212)
  plt.hist(data.flatten())

  plt.show()


if __name__ == "__main__":
  img_file_1 = 'DataSamples/1.png'
  img_file_2 = 'DataSamples/6.png'
  
  imgOut = 'image3.png'

  img1 = cv2.imread(img_file_1, 0)
  img2 = cv2.imread(img_file_2, 0) 
  
  ## Q2
  #combineImages(img1, img2, imgOut)

  ## Q3
  ## level = [5,3,1]
  quantization(img1, imgOut, level=3)
  
  ## Q4
  #image_enhancement(img1, imgOut)

  ## Q5
  #contrast_stretching(img1, imgOut)

  ## Q6
  img3 = cv2.imread(imgOut, 0) if os.path.exists(imgOut) else img1
  histogram_grey_level(img3)
