import cv2
import numpy as np

# 图像透视变换
src = cv2.imread("./images/6.jpg")
rows, cols, channel = src.shape  # h, w, c
print(cols, rows)

# 获取透视变换矩阵M：getPerspectiveTransform(src, dst）
# src:源图像中四边形顶点的坐标
# dst:目标图像中对应的四边形顶点的坐标。
pts1 = np.array([[25, 30], [180, 25], [10, 190], [190, 190]], dtype=np.float32)
pts2 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
M = cv2.getPerspectiveTransform(pts1, pts2)

# 进行透视变换：warpPerspective(src, M, dsize)
# M: 透视变换矩阵
# dsize: 指定输出图片的大小
dst2 = cv2.warpPerspective(src, M, dsize=(200, 201))

cv2.imshow("src", src)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

