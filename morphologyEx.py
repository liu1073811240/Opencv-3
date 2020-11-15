import cv2
import matplotlib.pyplot as plt

'图像形态学操作'
img1 = cv2.imread("./images/10.jpg", 0)
img2 = cv2.imread("./images/11.jpg", 0)

'''
    1.构造一个特定形状和大小的结构元素(核)，用于形态学操作。
    kernel = getStructuringElement(shape, ksize, anchor=None)
    参数：
    shape: 核的形状。
        MORPH_RECT = 0: 矩形
        MORPH_CROSS = 1: 交叉形
        MORPH_ELLIPSE = 2: 椭圆形
    ksize: 核的结构大小

    2.膨胀: 原图部分区域(A)与核(B)进行卷积，求局部最大值，并将局部最大值赋值给指定像素，从而增长高亮区域。
    dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)

    3.腐蚀: 与膨胀相反，用局部极小值替换当前像素，从而缩短高亮区域。
    erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)

    4.更多形态学操作
    morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
    参数：
    op: 形态学操作类型。
        cv2.MORPH_DILATE: 膨胀。-->增长高亮部分。
        cv2.MORPH_ERODE: 腐蚀。-->缩短高亮部分。
        cv2.MORPH_GRADIENT: 梯度，(膨胀-腐蚀)。-->提取轮廓。
        cv2.MORPH_OPEN: 开，先腐蚀再膨胀。-->去除噪点。
        cv2.MORPH_CLOSE: 闭，先膨胀再腐蚀。-->填补漏洞。
        cv2.MORPH_TOPHAT: 顶帽/礼帽，(原图-开)。-->获取噪点。
        cv2.MORPH_BLACKHAT: 黑帽，(闭-原图)。-->获取漏洞。
'''

# 获取指定形状和大小的结构元素（核）：getStructuringElement(shape, ksize)
# kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3, 3))  # 矩形
# kernel = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(5, 5))  # 交叉形或十字形
kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(5, 5))  # 椭圆形

# 形态学操作：必须是二值化图，膨胀和腐蚀的部分是白颜色。
dilate = cv2.dilate(img1, kernel)  # 膨胀
erode = cv2.erode(img1, kernel)  # 腐蚀

morph_dilate = cv2.morphologyEx(img1, cv2.MORPH_DILATE, kernel)  # 形态学膨胀
morph_erode = cv2.morphologyEx(img1, cv2.MORPH_ERODE, kernel)  # 形态学腐蚀
morph_gradient = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)  # 梯度：膨胀减去腐蚀，用于提取轮廓

morph_open = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)  # 开：先腐蚀后膨胀，用于去噪
morph_close = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)  # 闭：先膨胀后腐蚀，用于填补漏洞
morph_tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)  # 顶帽/礼帽， 原图减去开操作，用于获取噪点。
morph_blackhat = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, kernel)  # 黑帽， 闭操作减去原图， 用于获取漏洞。

# titles = ["IMAGE", "DILATE", "ERODE", "MORPH_DILATE", "MORPH_ERODE", "MORPH_GRADIENT"]
# images = [img1, dilate, erode, morph_dilate, morph_erode, morph_gradient]
# for i in range(6):
#     plt.subplot(2, 3, i+1)
#     plt.imshow(images[i], cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

titles = ["IMAGE", "MORPH_OPEN", "MORPH_CLOSE", "MORPH_TOPHAT", "MORPH_BLACKHAT"]
images = [img2, morph_open, morph_close, morph_tophat, morph_blackhat]
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()



