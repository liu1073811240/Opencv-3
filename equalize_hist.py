import cv2
import matplotlib.pyplot as plt

# 直方图均衡化：类似放大方差
# 全局直方图均衡化,将图片变得更亮。
src = cv2.imread("./images/28.jpg", 0)

dst = cv2.equalizeHist(src)

# 原直方图
hist_src = cv2.calcHist([src], [0], None, [256], [0, 255])

# 全局直方图均衡化后的图
hist_dst = cv2.calcHist([dst], [0], None, [256], [0, 255])

plt.subplot(221), plt.imshow(src, cmap="gray"), plt.title("Src Image")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(dst, cmap="gray"), plt.title("Dst Image")
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.plot(hist_src, color="r", label="hist_src"), plt.legend()
plt.subplot(224), plt.plot(hist_dst, color="b", label="hist_dst"), plt.legend()

plt.show()

