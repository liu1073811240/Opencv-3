import cv2
import numpy as np
import matplotlib.pyplot as plt

# 梯度操作/高通滤波：找轮廓
src = cv2.imread("./images/6.jpg")  # (201, 200, 3)
gray = cv2.imread("./images/6.jpg", cv2.IMREAD_GRAYSCALE)  # 形状为（201， 200）

# Scharr算子：dx和dy表示的是求导的阶数，0表示这个方向上没有导数， 一般为0,1,2
scharr_x = cv2.Scharr(gray, -1, dx=1, dy=0)  # x轴方向上的一阶导数
scharr_y = cv2.Scharr(gray, -1, dx=0, dy=1)  # y轴方向上的一阶导数

scharr_x_abs = cv2.convertScaleAbs(scharr_x)
scharr_y_abs = cv2.convertScaleAbs(scharr_y)
charr = cv2.addWeighted(scharr_x_abs, 0.5, scharr_y_abs, 0.5, 0)  # 近似有|G|=|Gx|+|Gy|

# Laplacian算子
laplacian = cv2.Laplacian(gray, -1)

title = ['Original image', 'Scharr_x', 'Scharr_y', 'Scharr_x_abs', 'Scharr_y_abs', 'Charr', 'Laplacian']
images = [gray, scharr_x, scharr_y, scharr_x_abs, scharr_y_abs, charr, laplacian]
for i in range(7):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()

