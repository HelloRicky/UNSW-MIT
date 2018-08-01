import numpy as np
import cv2



def combineImages(img1, img2, imgOut, axis = 1):
  ## axis = 1 for stacking vertically, 0 for horizontally
  ## imread(arg1, arg2)
  ## arg2 = [1, 0, -1], where 1 = color, 0 = grayscale, -1 = unchanged
  _img1 = cv2.imread(img1, 0)
  _img2 = cv2.imread(img2, 0)
  _imgOut = np.concatenate((_img1, _img2), axis = axis)
  cv2.imwrite(imgOut, _imgOut)

def 

if __name__ == "__main__":
  img1 = 'DataSamples/1.png'
  img2 = 'DataSamples/2.png'
  imgOut = 'image3.png'

  ## Q2
  combineImages(img1, img2, imgOut, axis = 0)

  ## Q3
