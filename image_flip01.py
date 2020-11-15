import cv2

# 图像翻转
src = cv2.imread("./images/1.jpg")
dst = cv2.transpose(src)  # h, w, c --> w, h, c

cv2.imshow("", src)
cv2.imshow("", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()




