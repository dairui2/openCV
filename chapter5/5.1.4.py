# 图像旋转

import cv2

img = cv2.imread('/Users/dai/Pictures/new_file_139.JPG')

h = img.shape[0]        #高度
w = img.shape[1]        #宽度

center = (w // 2, h // 2)   #计算旋转中心点，整除计算

# 获取二维旋转的仿射矩阵
M = cv2.getRotationMatrix2D(center, -45, 0.33)      #设置 center旋转中心点，-45旋转的角度，0.33缩放因子
rotated = cv2.warpAffine(img, M, (w, h))            #(w, h)设置输出图像的大小

cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(999)                # waitKey(n)函数用于等待用户按任意键n毫秒，如果n=0，则表示一直等待，直到用户按下任意键
cv2.destroyAllWindows()         # 关闭并释放所有窗口

