# 计算机视觉技术包括：图像和视频访问，图像显示，图像缩放，图像旋转，图像灰度化、归一化和图像分割
# OpenCV是一个开源的用于处理计算机视觉问题的库
# 读取和显示图像.

import cv2      # cv表示底层采用C语言实现，cv2表示底层采用C++语言实现

img = cv2.imread('/Users/dai/Pictures/new_file_139.JPG')        #imread()函数用于读取images目录下的图像文件，返回图像对象

print('img对象类型：',type(img))     # type()返回图像对象的数据类型，即NumPy数组(ndarray)类型
print('数组形状：',img.shape)        # shape属性返回图像的形状,数组形状： (4032, 3024, 3)

h = img.shape[0]        #高度
w = img.shape[1]        #宽度

msg = '''
图像高度：{0}
图像宽度：{1}
图像总像素：{2}
'''
print(msg.format(h, w, img.size))

cv2.imshow('fangdong', img)
cv2.waitKey(999)                # waitKey(n)函数用于等待用户按任意键n毫秒，如果n=0，则表示一直等待，直到用户按下任意键
cv2.destroyAllWindows()         # 关闭并释放所有窗口
