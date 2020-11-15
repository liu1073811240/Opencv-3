import cv2
import matplotlib.pyplot as plt

# CLAHE(限制对比度的自适应直方图均衡化)
src = cv2.imread("./images/29.jpg", cv2.IMREAD_GRAYSCALE)

# 全局直方图均衡化
img_equalize = cv2.equalizeHist(src)

# CLAHE自适应均衡化
clahe = cv2.createCLAHE(tileGridSize=(7, 7))  # 核为7*7
img_clahe = clahe.apply(src)

# 原直方图
hist_src = cv2.calcHist([src], [0], None, [256], [0, 255])

# 全局均衡化后的直方图
hist_equalize = cv2.calcHist([img_equalize], [0], None, [256], [0, 255])

# CLAHE均衡化后的直方图
hist_clahe = cv2.calcHist([img_clahe], [0], None, [256], [0, 255])

titles = ["Src Image", "Image after equalize", "Image after CLAHE"]
Images = [src, img_equalize, img_clahe]
for i in range(3):
    plt.subplot(2, 3, i+1)
    plt.imshow(Images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

labels = ["Hist Src", "Hist Equalize", "Hist Clahe"]
colors = ["b", "g", "r"]
images = [hist_src, hist_equalize, hist_clahe]
for j in range(3):
    plt.subplot(2, 3, j+4)
    plt.plot(images[j], color=colors[j], label=labels[j])
    plt.legend()

plt.show()




