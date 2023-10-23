# 调整图像的大小

import cv2

img = cv2.imread('/Users/dai/Pictures/new_file_139.JPG')
print('原始图像大小：', img.shape)     #shape属性返回图像的形状,数组形状： (4032, 3024, 3)

scale_factor = 0.33      #缩放因子是缩放前后的大小比例，大于1.0表示放大图像，小于1.0表示缩小图像
width = int(img.shape[1] * scale_factor)
height = int(img.shape[0] * scale_factor)
dim = (width, height)

resized = cv2.resize(img, dim)          #重新设置图像的大小
print('缩放后的图像大小：', resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(999)                # waitKey(n)函数用于等待用户按任意键n毫秒，如果n=0，则表示一直等待，直到用户按下任意键
cv2.destroyAllWindows()         # 关闭并释放所有窗口