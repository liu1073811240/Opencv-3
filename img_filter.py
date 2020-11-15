import cv2
import numpy as np

'''
    图像的时域（分析每个时间点、空间位置的一个点）和频域（分析两个点、线之间的变化：梯度）
    滤波是将信号中特定波段频率滤除的操作，是抑制和防止干扰的一项重要措施。
    图像滤波是图像预处理中不可缺少的操作，其处理效果的好坏将直接影响到后续图像处理和分析的有效性和可靠性。
    图像滤波，即在尽量保留图像细节特征的条件下对目标图像的噪声进行抑制。
    图像滤波的目的：
    1.消除图像中混入的噪声；
    2.为图像识别抽取出图像特征。
    滤波可分为 低通滤波、高通滤波、中通滤波、阻带滤波。都是从频域上区别的。
    低通滤波/平滑滤波：减弱或阻隔高频信号，保留低频信号，只留下变化较小的信号。可使图像变模糊，主要用于去噪。
    高通滤波：减弱或阻隔低频信号，保留高频信号，只留下变化较大的信号。一般用于获取图像边缘、轮廓或梯度。
    中通滤波：获取已知频率范围内的信号，去掉变化较大和较小的信号，留下变化适中的信号。
    阻带滤波：去掉已知频率范围内的信号，去掉变化适中的信号，留下变化较大和较小的信号。
'''

# 卷积滤波
img = cv2.imread("./images/1.jpg")

# 定义一个卷积核
kernel = np.float32([[1, 1, 0], [1, 0, -1], [0, -1, -1]])
# kernel = np.float32([[-1, 1, 0], [1, 0, -1], [0, -1, 1]])
# kernel = np.float32([[1, 0, 0], [0, 0, 0], [0, 0, -1]])

dst = cv2.filter2D(img, -1, kernel)  # -1表示在所有通道做卷积

# cv2.imshow("image", img)
# cv2.imshow("dst", dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img1 = cv2.imread("./images/132.jpg")
img2 = cv2.imread("./images/134.jpg")

# 1.均值滤波：blur(src, ksize, dst=None, anchor=None, borderType=None)
mean = cv2.blur(img1, ksize=(3, 3))

# 2.中值滤波：medianBlur(src, ksize, dst=None), 其中ksize为大于1的奇数
median = cv2.medianBlur(img1, ksize=7)

# 3.高斯滤波：GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
# ksize为奇数，不知道噪声分布的情况下一般使用高斯滤波
# sigmaX是高斯函数在x轴方向上的标准差。若不指定sigmaY，则sigmaY=sigmaX。
gaussian = cv2.GaussianBlur(img1, ksize=(7, 7), sigmaX=3, sigmaY=3)

# 4.双边滤波：bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
# d是每个像素的领域直径，由两个函数组成
# sigmaColor:在颜色空间中的过滤sigma。sigmaSpace:在坐标系空间中的过滤sigma。
# sigma为无穷大时，效果等价于高斯模糊。sigma为0时，与原图一样。
bilateral = cv2.bilateralFilter(img2, 33, 77, 77)
# bilateral = cv2.bilateralFilter(img1, 9, 0, 0)

# 高斯滤波和双边滤波的区别：
# 1）高斯核只考虑了空间分布，没有考虑到像素值的差异，会将图像的边缘模糊掉。
# 2）双边滤波是基于高斯滤波提出的，结合了图像的空间邻近度和像素值相似度的一种折中处理，具有保边特性。

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("mean", mean)
cv2.imshow("median", median)
cv2.imshow("gaussian", gaussian)
cv2.imshow("bilateral", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
