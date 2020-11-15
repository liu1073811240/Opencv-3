import cv2

# 图像金字塔

# 高斯金字塔
img = cv2.imread("./images/1.jpg")
for i in range(3):
    cv2.imshow(f"img{i}", img)
    img = cv2.pyrDown(img)
    img = cv2.pyrUp(img)

cv2.waitKey(0)
cv2.destroyAllWindows()





