# Capture image from the camera.
# Convert image from RGB to HSV color model.
# Obtain maximum value of value channel and calculate DV threshold.
# Group pixels that fit DV threshold.
# For each group do:
# a. Compute diameter and centroid.
# b. If the proportion of cropped area size and cropped area
# threshold > 0.3 get next group.
# c. Recognize laser spot color and add data to the local list.
# Update the global laser spot list from the local list.
# Go to the step 1.
# 140~170정도가 적당해 보임



import cv2

im=cv2.imread("../../images/bright_spot.jpg")
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)


ret, thresh_gray = cv2.threshold(gray,180,255,cv2.THRESH_BINARY)
# im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)

cv2.imshow("origin",im)
cv2.waitKey(0)
cv2.imshow("gray",gray)
cv2.waitKey(0)
mul=5
floor=140
for i in range(5):
    ret, thresh_gray = cv2.threshold(gray,floor+mul*i,255,cv2.THRESH_BINARY)
    cv2.imshow(str(ret)+"thresh",thresh_gray)
    cv2.waitKey(0)