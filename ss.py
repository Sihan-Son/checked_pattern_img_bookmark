# Author: sihan
# Date: 2019-12-24

import cv2
from utils import *

img = cv2.imread(r'./imgs/1.jpg')

a = cut_shuffle_img(img, 50)
cv2.imshow('1', a)
cv2.waitKey(0)
cv2.destroyAllWindows()
type(a)