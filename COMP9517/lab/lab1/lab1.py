import numpy as np
import cv2


def crop_img_position(x1, x2):
  ## find out diff
  if x1 < x2:
    return 0, (x2-x1)/2 
  return (x1-x2)/2, 0

def combineImages(img1, img2, imgOut, axis = 1):
  ## axis = 1 for stacking vertically, 0 for horizontally
  ## imread(arg1, arg2)
  ## arg2 = [1, 0, -1], where 1 = color, 0 = grayscale, -1 = unchanged
  _img1 = cv2.imread(img1, 0)
  _img2 = cv2.imread(img2, 0)

  h1, w1 = _img1.shape
  h2, w2 = _img2.shape

  c_h1, c_h2 = crop_img_position(h1, h2)
  c_w1, c_w2 = crop_img_position(w1, w2)

  crop_img1 = _img1[c_h1:h1-c_h1, c_w1:w1/2]
  crop_img2 = _img2[c_h2:h2-c_h2, w2/2:w2-c_w2]

  _imgOut = np.concatenate((crop_img1, crop_img2), axis = axis)
  cv2.imwrite(imgOut, _imgOut)


if __name__ == "__main__":
  img1 = 'DataSamples/6.png'
  img2 = 'DataSamples/2.png'
  imgOut = 'image3.png'

  ## Q2
  combineImages(img1, img2, imgOut)

  ## Q3
