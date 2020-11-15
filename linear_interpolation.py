import cv2
import time

img = cv2.imread("./images/1.jpg")
rows, cols, channels = img.shape

# 几种插值方式：
# 1.双线性插值（默认）（相较于最邻近插值更加平滑）
linear = cv2.resize(img, dsize=(cols*2, rows*2), interpolation=cv2.INTER_LINEAR)

start_time = time.time()
# 2.最邻近插值（速度最快，但不清晰，有马赛克）
nearest = cv2.resize(img, dsize=(cols*2, rows*2), interpolation=cv2.INTER_NEAREST)
end_time = time.time()

# 3.基于4*4像素三次样条插值
start_time2 = time.time()
cubic = cv2.resize(img, dsize=(cols*2, rows*2), interpolation=cv2.INTER_CUBIC)
end_time2 = time.time()

# 4.基于8*8像素领域内的Lanczos插值 (缺点速度慢，但相较于双线性插值更清晰)
lanczos = cv2.resize(img, dsize=(cols*2, rows*2), interpolation=cv2.INTER_LANCZOS4)

# 5.基于局部像素的重采样：图像放大时，和邻近插值一样，图像缩小时，和线性插值一样。
area = cv2.resize(img, dsize=(cols*2, rows*2), interpolation=cv2.INTER_AREA)

time_use1 = end_time-start_time
time_use2 = end_time2-start_time2
print("最邻近插值所用时间：", time_use1)
print("样条插值所用时间：", time_use2)

cv2.imshow("linear", linear)
cv2.imshow("nearest", nearest)
cv2.imshow("cubic", cubic)
cv2.imshow("lanczos", lanczos)
# cv2.imshow("area", area)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 几种常用方法的效率是：最邻近插值>双线性插值>双立方插值>lanczos插值
# 但是效率和效果成反比，所以根据情况酌情使用。

