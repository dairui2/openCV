# 人脸检测

import cv2

img = cv2.imread('./a.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        #图像灰度化

face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")               #创建分类器对象

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2)        #搜索图像中的人脸数据

#给脸部绘制矩形
for x, y, w, h in faces:    #取出人脸矩形左上角的x和y坐标，以及它的高和宽
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Gray", img)
cv2.waitKey(9999)
cv2.destroyAllWindows()