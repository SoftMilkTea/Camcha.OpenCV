import cv2
import os
import numpy as np



dataset_dir = os.path.abspath("/Users/heetop/Desktop/Dataset")
if os.path.isdir(dataset_dir)==False:
    dataset_dir = os.path.abspath("C:/Users/knyup/OneDrive/SW_Mae/Camcha/Dataset")

image_path=os.path.join(dataset_dir,"images/white/bright_white_spot_1.jpg")
white_image=cv2.imread(image_path)
white_image=cv2.resize(white_image,(540,960))

cv2.imshow("Original",white_image)

#1. HSV - Finding Red Color
hsv = cv2.cvtColor(white_image,cv2.COLOR_BGR2HSV)

# lower_red = cv.Scalar(-1, 150, 100)
# upper_red = cv.Scalar(1, 255, 255)
lower_red = np.array([-10,150,150])
upper_red = np.array([10,255,255])

mask_red = cv2.inRange(hsv, lower_red, upper_red)

res = cv2.bitwise_and(white_image, white_image, mask= mask_red)

cv2.imshow("HSV applied",res)



#2. Dilate - make spot be larger 
dilate = cv2.dilate(res,None,iterations=1)



#3. Blob - Finding circle
params = cv2.SimpleBlobDetector_Params()
    # Change thresholds
params.minThreshold = 10
# params.maxThreshold = 200
    # Filter by Area.
params.filterByArea = True
params.minArea = 0.5
params.maxArea = 10
    # Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
    # Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.7
    # Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

    # Filter by Color
params.filterByColor = True
params.blobColor = 255


detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(dilate)
im_wit_keypoints = cv2.drawKeypoints(dilate,keypoints,np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)




# Output Part
cv2.imshow("Dilate applied",dilate)
cv2.imshow("Blob applied",im_wit_keypoints)
cv2.waitKey(0)

