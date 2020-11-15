import cv2
import matplotlib.pyplot as plt

# 绘制直方图
# 一维直方图
img = cv2.imread("./images/30.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转化为灰度图

# 绘制灰度图的直方图
hist_gray = cv2.calcHist(images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0, 255])  # 256表示直方图的个数。

# 绘制单通道B的直方图
hist_B = cv2.calcHist([img], [0], None, [256], [0, 255])

# 绘制单通道G的直方图
hist_G = cv2.calcHist([img], [1], None, [256], [0, 255])

# 绘制单通道R的直方图
hist_R = cv2.calcHist([img], [2], None, [256], [0, 255])

plt.plot(hist_gray, color="gray", label="Gray")
plt.plot(hist_B, color="b", label="B")
plt.plot(hist_G, color='g', label="G")
plt.plot(hist_R, color='r', label="R")
plt.show()

