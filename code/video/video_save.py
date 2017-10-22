import cv2
import os
import numpy as np

# base dir
dataset_dir = os.path.abspath("/Users/heetop/Desktop/Dataset")
if os.path.isdir(dataset_dir)==False:
    dataset_dir = os.path.abspath("C:/Users/knyup/OneDrive/SW_Mae/Camcha/Dataset")

save_path=os.path.join(dataset_dir,"videos/white/bright_white_spot_5.avi")
# video start

cap = cv2.VideoCapture(0)
# Set parameters

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# We convert the resolutions from float to integer.

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter(save_path,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


while(True):

    ret, white_image = cap.read()

    # image save
    out.write(white_image)

    # Output Part
    cv2.imshow("Original",white_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()

cv2.destroyAllWindows()
