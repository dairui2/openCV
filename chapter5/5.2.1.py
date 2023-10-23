# 图像灰度化:将3个颜色通道变为1个颜色通道

import cv2

img = cv2.imread('/Users/dai/Pictures/new_file_139.JPG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #改变图像的色彩空间，BGR为GRAY，即改为灰度图像

cv2.imshow('img', img)
cv2.imshow('img', gray)

cv2.waitKey(999)
cv2.destroyAllWindows()