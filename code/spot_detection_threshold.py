# https://docs.opencv.org/3.2.0/d7/d4d/tutorial_py_thresholding.html
# threshold filter
# cv2.THRESH_TOZERO 임계값 이상이면 실제값
# cv2.THRESH_BINARY 임계값 이상이면 검은색
# cv2.THRESH_OTSU 평균값을 임계값으로 사용
#
import cv2
bright_img=cv2.imread('/Users/heetop/Dropbox/opencv/images/bright_spot.jpg',0) # 밝은 사진
blur = cv2.GaussianBlur(bright_img,(5,5),0) # 필터 처리 안하는게 오히려 더 잘됨
# 노이즈 줄이기 위해서는 필터 처리 하는게 더 나음

ret , thresh = cv2.threshold(blur,150,255,cv2.THRESH_BINARY) # img, 임계값, 변환값(현재 흰색), 방식(현재 임계값 흰색)

edges = cv2.Canny(thresh,150,200) # Canney 알고리즘 -> 구역 찾아줌

cv2.imshow('origin image',bright_img)
cv2.imwrite('../images/spot_origin_image.jpg',bright_img)
cv2.waitKey(0)

# cv2.imshow('blur image',blur)
# cv2.waitKey(0)

cv2.imshow('threshold image',thresh)
cv2.imwrite('../images/spot_threshhold_img.jpg',thresh)
cv2.waitKey(0)

cv2.imshow('canney image',edges)
cv2.imwrite('../images/spot_canney_img.jpg',edges)
cv2.waitKey(0)

