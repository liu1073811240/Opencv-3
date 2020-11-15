import cv2

# 翻转：flipCode用来控制翻转效果
src = cv2.imread("./images/1.jpg")

dst1 = cv2.flip(src, flipCode=0)  # flipcode=0: 绕x轴翻转，即上下颠倒
# dst2 = cv2.flip(src, flipCode=1)  # flipcode=1: 绕y轴翻转，即左右翻转
# dst3 = cv2.flip(src, flipCode=-1)  # flipcode=-1: 绕x,y轴同时翻转，即上下加左右翻转。

cv2.imshow("src", src)

cv2.imshow("dst1", dst1)
# cv2.imshow("dst2", dst2)
# cv2.imshow("dst3", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()



