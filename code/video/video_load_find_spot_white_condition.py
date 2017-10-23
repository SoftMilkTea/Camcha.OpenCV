import cv2
import os
import numpy as np

def filting_red_by_HSV(image):
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    lower_red = np.array([170,200,240])
    upper_red = np.array([180,255,255])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    red_HSV = cv2.bitwise_and(image, image, mask= mask_red)
    return red_HSV

# base dir
dataset_dir = os.path.abspath("/Users/heetop/Desktop/Dataset")
if os.path.isdir(dataset_dir)==False:
    dataset_dir = os.path.abspath("C:/Users/knyup/OneDrive/SW_Mae/Camcha/Dataset")

video_path=os.path.join(dataset_dir,"videos/white/bright_white_spot_9.mp4")


# video load
cap = cv2.VideoCapture(video_path)


# Set parameters
params = cv2.SimpleBlobDetector_Params()
    # Change thresholds
params.minThreshold = 10
params.maxThreshold = 255
# params.maxThreshold = 200
    # Filter by Area.
params.filterByArea = True
params.minArea = 0.5
params.maxArea = 30
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



while(cap.isOpened()):

    ret, white_image = cap.read()
    white_image = cv2.resize(white_image,(960,540))

    #1. HSV - Finding Red Color
    red_HSV = filting_red_by_HSV(white_image)


    #2-Heetop. Dilate - make spot be larger
    dilate = cv2.dilate(red_HSV,None,iterations=1)


    #3. Blob - Finding circle
    keypoints_dilate = detector.detect(dilate)
    for i in range(len(keypoints_dilate)):
        x = int(keypoints_dilate[i].pt[0]) # x axis
        y = int(keypoints_dilate[i].pt[1]) # y axis

        cv2.circle(white_image, (x,y), 10, (0, 255, 0), 2)



    im_wit_keypoints_dilate = cv2.drawKeypoints(white_image,keypoints_dilate,np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)




    # Output Part
    cv2.imshow("dilate",dilate)
    cv2.imshow("im_wit_keypoints_dilate",im_wit_keypoints_dilate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
