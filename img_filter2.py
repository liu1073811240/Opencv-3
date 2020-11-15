import cv2
import numpy as np
import matplotlib.pyplot as plt

# 高通滤波(低通滤波处理背景信息，高通滤波处理轮廓信息)
src = cv2.imread("./images/1.jpg")

# 锐化操作（作用是将轮廓凸显出来）
# 1.自定义锐化核
kernel = np.float32([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
dst1 = cv2.filter2D(src, -1, kernel)

# 2.USM锐化（UnsharpMask）
gaussian = cv2.GaussianBlur(src, (7, 7), 7)
dst2 = cv2.addWeighted(src, 2, gaussian, -1, 0)  # 2*src-gaussian*(-1)

cv2.imshow("src", src)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()



