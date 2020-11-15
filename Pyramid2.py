import cv2
import numpy as np

# 拉普拉斯金字塔
img = cv2.imread("./images/1.jpg")
img_down = cv2.pyrDown(img)
img_up = cv2.pyrUp(img_down)
# cv2.imshow("img_up", img_up)

img_new = cv2.subtract(img, img_up)  # 结果为轮廓信息
# img_new = cv2.subtract(2*img, np.uint8(img_up))
# cv2.imshow("img_new", img_new)

# 为了更容易看清楚，做了个提高对比度的操作
img_new2 = cv2.convertScaleAbs(img_new, alpha=5, beta=3)
cv2.imshow("img_new2", img_new2)

for i in range(3):
    cv2.imshow(f"img{i}", img_new2)
    img_new2 = cv2.pyrDown(img_new2)
    img_new = cv2.pyrUp(img_new)

cv2.waitKey(0)
cv2.destroyAllWindows()


