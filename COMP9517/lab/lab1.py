import numpy as np
import cv2



def combineImages(img1, img2, imgOut, axis = 1):
  ## axis = 1 for stacking vertically, 0 for horizontally
  _img1 = cv2.imread(img1, 0)
  _img2 = cv2.imread(img2, 0)
  _imgOut = np.concatenate((_img1, _img2), axis = axis)
  cv2.imwrite(imgOut, _imgOut)

if __name__ == "__main__":
  img1 = 'DataSamples/1.png'
  img2 = 'DataSamples/2.png'
  imgOut = 'out.png'
  
  combineImages(img1, img2, imgOut, axis = 0)
