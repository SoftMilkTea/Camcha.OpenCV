import cv2
import numpy as np
bright_img=cv2.imread('../images/bright_spot.jpg') # 붉은 계열 밝은 사진
dark_img=cv2.imread('../images/dark_spot.jpg') # 붉은 계열 어두운 사진

# bright_img=cv2.imread('../images/bright_spot_white.jpg') # 백색광 밝은 사진
# dark_img=cv2.imread('../images/dark_spot_white.jpg') # 백색광 어두운 사진

subtraction_img = bright_img - dark_img # 픽셀값 뺀 사진

# subtraction_img[:,:,0]=0 # blue 제거
# subtraction_img[:,:,1]=0 # green 제거
# subtraction_img[:,:,2]=0 # red 제거
# subtraction_img=abs(subtraction_img)

cv2.imshow('del_blue_img',subtraction_img[:,:,0]) # blue
cv2.waitKey(0)
cv2.imshow('del_green_img',subtraction_img[:,:,1]) # green
cv2.waitKey(0)
cv2.imshow('del_red_img',subtraction_img[:,:,2]) # red
cv2.waitKey(0)
cv2.imshow('subtraction_img',subtraction_img)
cv2.imwrite('../image/subtarction_image.jpg',subtraction_img) # 이미지 저장
cv2.waitKey(0)