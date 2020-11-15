import cv2

# 直方图反向投影
# 感兴趣对象ROI (要抠取哪部分图像)
roi = cv2.imread("./images/30.jpg")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # 转化为HSV图

# 目标图像
target = cv2.imread("./images/16.jpg")
hsv_target = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)  # 转化为HSV图

# 统计ROI的直方图
hist_roi = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 179, 0, 255])
'''cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])

images：必须用括号括起来表示，即[image]
chanels：用于计算直方图的通道，使用灰度图计算直方图，所以就直接使用第一个通道；对于彩色可以通过[0]，[1]，[2]分别计算蓝色、绿色或红色通道的直方图
mask：如果计算完整图像的直方图，它将设为None。但是如果想找到图像特定区域的直方图，则必须为它创建一个蒙版图像作为蒙版。
histSize：表示这个直方图分成多少份（即多少个直方柱）。对于满量程，设置为[256]
ranges：表示直方图中各个像素的值，通常设为[0,256]
'''


# ROI的直方图归一化：在调用calBackProject之前，需要对hist_roi进行归一化
cv2.normalize(hist_roi, hist_roi, 0, 255, cv2.NORM_MINMAX)

# 反向投影：calBackProject
backProject = cv2.calcBackProject([hsv_target], [0, 1], hist_roi, [0, 179, 0, 255], 1)

# 圆盘卷积
kernel = cv2.getStructuringElement(shape=cv2.MORPH_ELLIPSE, ksize=(5, 5))
backProject = cv2.filter2D(backProject, -1, kernel)

# 图像二值化
ret, image = cv2.threshold(backProject, 50, 255, cv2.THRESH_BINARY)

# 抠出目标图像中的感兴趣部分
merge_image = cv2.merge((image, image, image))  # 合并图像的三个通道
res = cv2.bitwise_and(target, merge_image)

cv2.imshow("roi", roi)
cv2.imshow("target", target)
cv2.imshow("hist_roi", hist_roi)
cv2.imshow("backProject", backProject)
cv2.imshow("merge image", merge_image)
cv2.imshow("res", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
