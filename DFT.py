import cv2
import matplotlib.pyplot as plt
import numpy as np

# opencv中的DFT（Discrete Fourier Transform）
img = cv2.imread("./images/1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = gray.shape

# 1.DFT离散傅里叶变换：空域-->频域
dft = cv2.dft(src=np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)  # cv2.DFT_COMPLEX_OUTPUT表示进行傅里叶变化的方法
print(dft.shape)  # (540, 960, 2)  2表示两个通道

# 2.中心化：将低频移动到图像中心
fftshift = np.fft.fftshift(dft)
# 获取振幅谱（展示图片用）：20*np.log()是为了将值限制在[0, 255]
magnitude_spectrum = 20 * np.log(cv2.magnitude(fftshift[:, :, 0], fftshift[:, :, 1]))

# 3.滤波操作之低通滤波（去高频，保低频）
mask = np.zeros((rows, cols, 2), dtype=np.uint8)
mask[(rows//2 - 30):(rows//2+30), (cols//2-30):(cols//2+30)] = 1
fftshift = fftshift * mask

# 4.去中心化：将低频和高频的位置还原
ifftshift = np.fft.ifftshift(fftshift)

# 5.逆傅里叶变换：频域-->空域
idft = cv2.idft(ifftshift)

# 6.二维向量取模（幅值）
img_back = cv2.magnitude(idft[:, :, 0], idft[:, :, 1])

titles = ['Gray', 'magnitude spectrum', 'img_back']
images = [gray, magnitude_spectrum, img_back]
for i in range(3):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.subplot(224), plt.imshow(img_back), plt.title("Result in JET")  # 默认cmap为‘jet’
plt.show()


