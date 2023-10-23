# 图像二值化：将图像上像素点的灰度值重新设置为0(黑色)和255(白色)两个极端值，因此需要设置一个阈值T,
# 将大于或等于T的灰度值设置为255，将小于T的灰度值设置为0，图像二值化后只有黑色和白色的视觉效果

import cv2

img = cv2.imread('/Users/dai/Pictures/new_file_139.JPG')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #改变图像的色彩空间，BGR为GRAY，即改为灰度图像

T = 60              # 设置阈值，它的取值范围是0～255
maxval = 255        #设置超过阈值的像素值的最大值，在大于阈值时设置为此最大值

cv2.imshow('img', img)
cv2.imshow('img', gray)

ret, thresh1 =cv2.threshold(gray, T, maxval, cv2.THRESH_BINARY)
cv2.imshow('threshold=60', thresh1)

cv2.waitKey(9999)
cv2.destroyAllWindows()