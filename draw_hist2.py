import cv2
import matplotlib.pyplot as plt

# 绘制2D直方图
img = cv2.imread("./images/1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 转为HSV图

hist_hsv = cv2.calcHist([hsv], [0, 1], None, [180, 255], [0, 180, 0, 255])

# cv2.namedWindow("hist_hsv", cv2.WINDOW_NORMAL)
cv2.imshow("hist_hsv1", hist_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

