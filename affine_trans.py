import cv2
import numpy as np

# 图像仿射变换
img = cv2.imread("./images/6.jpg")
rows, cols, channels = img.shape  # h, w, c

#  创建仿射变换矩阵M
M0 = np.float32([[1, 0, 0], [0, 1, 0]])
M1 = np.float32([[1, 0, 20], [0, 1, 80]])  # 沿x轴平移+20， 沿y轴平移+80
M2 = np.float32([[0.8, 0, 20], [0, 0.5, 80]])   # 沿x轴变为原来的0.8， y轴变为原来的0.5
# M3 = np.float32([[np.sqrt(3)/2, 0.5, 0], [-0.5, np.sqrt(3)/2, 0]])  # 逆时针旋转30度
M3 = cv2.getRotationMatrix2D((cols//2, rows//2), 45, scale=0.8)  # 按照中心点逆时针旋转45度，图片大小为原来的0.8倍。
M4 = np.float32([[1, 0.5, 0], [0, 1, 0]])  # 沿x轴倾斜0.5倍
M5 = np.float32([[1, 0, 0], [0.5, 1, 0]])  # 沿y轴倾斜0.5倍
# M6 = np.float32([[-1, 0, cols], [0, 1, 0]])  # 绕y轴翻转，沿x轴平移cols个像素单位。
M6 = np.float32([[1, 0, 0], [0, -1, rows]])  # 沿x轴翻转，沿y轴平移rows个像素单位。
M7 = np.float32([[-1, 0, cols], [0, -1, rows]])  # 绕y转翻转、绕x转翻转，最后沿x轴平移cols个像素单位、沿y轴平移rows个像素单位


# 进行仿射变换操作，dsize:指定输出图片的大小
dst0 = cv2.warpAffine(img, M0, dsize=(cols, rows))  # 图形没有变换
dst1 = cv2.warpAffine(img, M1, dsize=(cols, rows))  # 平移
dst2 = cv2.warpAffine(img, M2, dsize=(cols, rows))  # 缩放
dst3 = cv2.warpAffine(img, M3, dsize=(cols, rows))  # 旋转
dst4 = cv2.warpAffine(img, M4, dsize=(cols*2, rows*2))  # 倾斜
dst5 = cv2.warpAffine(img, M5, dsize=(cols*2, rows*2))  # 倾斜
dst6 = cv2.warpAffine(img, M6, dsize=(cols, rows))  # 翻转/镜像
dst7 = cv2.warpAffine(img, M7, dsize=(cols, rows))  # 翻转/镜像


cv2.imshow("img", img)
# cv2.imshow("dst0", dst0)
# cv2.imshow("dst1", dst1)
# cv2.imshow("dst2", dst2)
# cv2.imshow("dst3", dst3)
# cv2.imshow("dst4", dst4)
# cv2.imshow("dst5", dst5)
# cv2.imshow("dst6", dst6)
cv2.imshow("dst7", dst7)
cv2.waitKey(0)
cv2.destroyAllWindows()

