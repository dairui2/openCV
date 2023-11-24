# 验证码识别，核心内容是图像识别
# OCR(Optical Character Recognition，光学字符识别)引擎Tesseract，可以识别多种格式的图像文件并将其转换成文本，目前支持60多种语言(含中文)；pytesseract库调用OCR引擎Tesseract
# PIL中所涉及的基本概念有如下几个：通道(bands)、尺寸(size)、坐标系统(coordinate system)。

import cv2
import pytesseract as tess
from PIL import Image

maxval = 255

# 读取图片
src_image = cv2.imread('./lake.png')
# print(src_image)

# 转为灰度图像
gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

# 转为二值化图像
th_image = cv2.adaptiveThreshold(gray_image, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 1)

# 将OpenCV图像转为PIL图像
pil_image = Image.fromarray(th_image)

# 转为文本显示
text = tess.image_to_string(pil_image, lang='chi_sim+eng')

# 删除文本中的空格
text = text.replace(' ', '')
# 删除文本前后的空白
text = text.strip()
print(text)