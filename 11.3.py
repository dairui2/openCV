# 图像的聚类分割
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import PIL.Image as Image

# 打开图像并显示
# %matplotlib inline
img = Image.open('./chapter5/lena.tiff')
plt.axis('off')
plt.imshow(img)

# 显示图像的基本信息和图像大小
print(img.info)
row,col = img.size
print('图像的大小：', row, col)

# 显示图像的颜色模式
print('数据类型：',type(img))
print('图像的颜色模式：',img.mode)

# 对图像数据进行聚类并显示每个像素的簇标号
imgData = np.array(img.getdata())
type(imgData)
pixel_vals = imgData.reshape(-1,4)
# pixel_vals
km_cluster = KMeans(n_clusters=3)
label = km_cluster.fit_predict(pixel_vals)
print('每个像素的簇标号：\n', label)

# 显示分割后的图像
label = label.reshape([row, col]).T
pic_new = Image.new('L', (row, col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j), int(int(256/(label[i][j] + 1))))
plt.imshow(pic_new)
plt.waitforbuttonpress(9)