# 필터 적용할때 중앙값 (홀수,홀수) -> 값이 높으면 더 많이 뭉개짐

import cv2

im=cv2.imread("../../images/bright_spot.jpg")
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

cv2.imshow("origin",im)
cv2.waitKey(0)
cv2.imshow("gray",gray)
cv2.waitKey(0)
mul=2
floor=140
for i in range(5):
    blur=cv2.GaussianBlur(gray,(2*i+1,2*i+1),0)

    cv2.imshow(str(i+1)+"blur",blur)
    cv2.waitKey(0)