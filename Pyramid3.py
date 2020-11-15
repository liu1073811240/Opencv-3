import cv2
import numpy as np

# 图像无缝融合：使用图像金字塔创建一个新的水果，'Orapple'
A = cv2.imread("./images/14.jpg")
B = cv2.imread("./images/15.jpg")
print(A.shape)  # (256, 256, 3)
print(B.shape)  # (256, 256, 3),两个图片大小必须一致

# 高斯金字塔
GA = A.copy()  # 复制一张苹果图片
gpA = [GA]  # 列表里面装有苹果图片数据
# print(gpA)
for i in range(6):
    GA = cv2.pyrDown(GA)
    gpA.append(GA)  # 表示列表里装了一张苹果原图和六张经过下采样的图片

print(np.shape(gpA))  # (7,)

GB = B.copy()  # 复制一张梨的图片
gbB = [GB]  # 列表里面装有苹果图片数据
for i in range(6):
    GB = cv2.pyrDown(GB)
    gbB.append(GB)  # 表示列表里装了一张梨的原图和六张经过下采样的图片

print(np.shape(gbB))


# 拉普拉斯金字塔
lpA = [gpA[6]]
print(np.shape(lpA))  # 苹果列表取最后一张图片，形状为（1， 4， 4， 3）
for i in range(6, 0, -1):
    GE = cv2.pyrUp(gpA[i])  # 从列表中取最后一张图片上采样
    L = cv2.subtract(gpA[i-1], GE)  # 拿列表中的原图片和经过上采样的图片相减，得到轮廓信息
    lpA.append(L)  # 将列表中最后一张图片加上经过处理过的六张图片。

    # cv2.imshow("L", L)
    # cv2.imshow("GE", GE)
    # cv2.imshow("gpA", gpA[i-1])
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
print(np.shape(lpA))  # 一张最小的图片加上六张黑图

lpB = [gbB[6]]  #
for i in range(6, 0, -1):
    GE = cv2.pyrUp(gbB[i])
    L = cv2.subtract(gbB[i-1], GE)
    lpB.append(L)

print(lpB)


# 拼接苹果和橘子
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, channels = la.shape
    ls = np.hstack((la[:, 0:cols//2, :], lb[:, cols//2:, :]))  # 苹果，橘子的宽和高,通道合并。
    # ls = np.vstack((la[:, :cols//2], lb[:, cols//2:]))
    print(ls.shape)  # (4, 4, 3)...
    LS.append(ls)  # 将合并好的图像放在列表中

ls_ = LS[0]  # shape为(4, 4, 3)
print(ls_.shape)  # 列表存放的图片尺寸从小到大排列
for i in range(1, len(LS)):  # (1, 7)
    ls_ = cv2.pyrUp(ls_)  # 进行六次上采样
    ls_ = cv2.add(ls_, LS[i])  # 将上采样的图像和原来的带有轮廓信息的图像进行合并

cv2.imshow(f"pic {i}", ls_)  # 将合并后的最后一张图片展示出来


# 直接合成的图片
rows, cols, channels = A.shape
real = np.hstack((A[:, 0:cols//2, :], B[:, cols//2:, :]))
cv2.imshow("real", real)

cv2.waitKey(0)
cv2.destroyAllWindows()






