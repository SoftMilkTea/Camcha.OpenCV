import cv2
import os
import numpy as np

dataset_dir = os.path.abspath("/Users/heetop/Desktop/Dataset")

image_path=os.path.join(dataset_dir,"images/white/bright_white_spot_3.jpg")

white_image=cv2.imread(image_path)
white_image=cv2.resize(white_image,(540,960))

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 0.5
params.maxArea = 1

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
detector = cv2.SimpleBlobDetector_create(params)


hsv = cv2.cvtColor(white_image,cv2.COLOR_BGR2HSV)

# lower_red = cv.Scalar(-1, 150, 100)
# upper_red = cv.Scalar(1, 255, 255)
lower_red = np.array([-10,100,100])
upper_red = np.array([10,255,255])

mask_red = cv2.inRange(hsv, lower_red, upper_red)

res = cv2.bitwise_and(white_image, white_image, mask= mask_red)

dilate = cv2.dilate(res,None,iterations=1)
keypoints = detector.detect(res)
im_wit_keypoints = cv2.drawKeypoints(res,keypoints,np.array([]),(255,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



cv2.imshow("white",res)
cv2.imshow("hsv",im_wit_keypoints)
cv2.waitKey(0)




# import cv2
# import numpy as np
# import os

# dataset_dir = os.path.abspath("/Users/heetop/Desktop/Dataset")

# image_path=os.path.join(dataset_dir,"images/white/bright_white_spot_3.jpg")
# # Read image
# im = cv2.imread("blob.jpg")

# # Setup SimpleBlobDetector parameters.
# params = cv2.SimpleBlobDetector_Params()

# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200


# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500

# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1

# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87

# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

# # Create a detector with the parameters
# detector = cv2.SimpleBlobDetector(params)


# # Detect blobs.
# keypoints = detector.detect(im)

# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# # the size of the circle corresponds to the size of blob

# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Show blobs
# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)