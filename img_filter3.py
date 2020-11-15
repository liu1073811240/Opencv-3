import cv2
import numpy as np
import matplotlib.pyplot as plt

# 梯度操作/高通滤波：找轮廓
src = cv2.imread("./images/6.jpg")  # (201, 200, 3)
gray = cv2.imread("./images/6.jpg", cv2.IMREAD_GRAYSCALE)  # 形状为（201， 200）

# Sobel算子: dx和dy表示的是求导的阶数，0表示这个方向上没有求导，一般为0、1、2。
sobel_x = cv2.Sobel(gray, -1, dx=1, dy=0, ksize=3)  # x轴方向上的一阶导数
sobel_y = cv2.Sobel(gray, -1, dx=0, dy=1, ksize=3)  # y轴方向上的一阶导数

sobel_x_abs = cv2.convertScaleAbs(sobel_x, alpha=2, beta=1)
sobel_y_abs = cv2.convertScaleAbs(sobel_y, alpha=2, beta=1)

sobel_x_abs2 = np.uint8(np.sqrt(sobel_x**2))
sobel_y_abs2 = np.uint8(np.sqrt(sobel_y**2))

sobel = cv2.addWeighted(sobel_x_abs, 0.5, sobel_y_abs, 0.5, 0)

# 结合matplotlib显示多张图片
titles = ['Original Gray', 'Sobel x', 'Sobel y', 'Sobel x abs', 'Sobel y abs', 'Sobel x abs2', 'Sobel y abs2', 'sobel']
images = [gray, sobel_x, sobel_y, sobel_x_abs, sobel_y_abs, sobel_x_abs2, sobel_y_abs2, sobel]
for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


'''
函数cv2.convertScaleAbs(src[,alpha[,beta]])

概述：
先计算数组绝对值，后转化为8位无符号数

参数：
src:输入图像（多维数组）
alpha:比例因子
beta:保存新图像（数组）前可以增加的值

'''



