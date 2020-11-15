import cv2

img = cv2.imread("./images/1.jpg")
print(img.shape)
rows, cols, channels = img.shape

# 图片缩放：resize()
resize_1 = cv2.resize(img, dsize=(cols*2, rows*2))  # 按尺寸， 图像扩大两倍
resize_2 = cv2.resize(img, dsize=(12, 45), fx=1.2, fy=2)  # 若dsize为负数或零，按比例因子进行缩放，否则就按照dsize所给的尺寸。
# print(resize_1.shape)
print(resize_2.shape)

# cv2.imshow("resize_1", resize_1)
# cv2.imshow("resize_2", resize_2)
cv2.waitKey(0)
cv2.destroyAllWindows()