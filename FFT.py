import numpy as np
import cv2
import matplotlib.pyplot as plt

# numpy中的FFT（Fast Fourier Transform） 快速傅里叶变换
# FFT：时域是对每个像素值的统计，频域是对像素之间的差异值进行统计
img = cv2.imread("./images/1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape  # h, w
# print(gray.shape)

# 1.FFT快速傅里叶变换：空域-->频域
fft = np.fft.fft2(gray)  # 傅里叶变换，参数为灰度图
print(fft.shape)  # (h, w)

# 2.中心化：将低频信号移动到图像中心
fftshift = np.fft.fftshift(fft)
# print(fftshift.shape)
# 获取振幅谱（展示图片用）；20*np.log()是为了将值限制在[0, 255]
magnitude_spectrum = 20 * np.log(np.abs(fftshift))

# 3.滤波操作之高通滤波（去低频，保高频）
fftshift[rows//2-10:rows//2+10, cols//2-10:cols//2+10] = 0
print(fftshift.shape)  # (540, 960)

# 4.去中心化：将剩余的低频和高频的位置还原
ifftshift = np.fft.ifftshift(fftshift)

# 5.逆傅里叶变换：频域-->空域
ifft = np.fft.ifft2(ifftshift)

# 6.二维向量取模（幅值）
img_back = np.abs(ifft)

titles = ['Input Gray Image', 'Magnitude_Spectrum', 'Img_back']
images = [gray, magnitude_spectrum, img_back]
for i in range(3):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.subplot(224), plt.imshow(img_back), plt.title("Result in JET")
plt.show()




