import cv2
import os
from matplotlib import pyplot as plt


dataset_dir = os.path.abspath("/Users/heetop/Desktop/Dataset")
if os.path.isdir(dataset_dir)==False:
    dataset_dir = os.path.abspath("C:/Users/knyup/OneDrive/SW_Mae/Camcha/Dataset")

image_path=os.path.join(dataset_dir,"images/white/bright_white_spot_1.jpg")


white_image=cv2.imread(image_path)
white_image=cv2.resize(white_image,(540,960))
white_image=cv2.GaussianBlur(white_image,(3,3),0)

hsv = cv2.cvtColor(white_image,cv2.COLOR_BGR2HSV)
print(hsv.shape)

figure = plt.figure()
plt.subplot(1,2,1) # 1*2행렬  1번째 이미지
plt.title("ORIGIN")
plt.imshow(white_image)
plt.subplot(1,2,2)
plt.title("GRAY")
plt.imshow(hsv)
plt.show()