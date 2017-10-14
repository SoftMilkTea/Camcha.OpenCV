
import cv2

cap = cv2.VideoCapture("/Users/heetop/Desktop/Dataset/images/bright_dot_2.mp4")
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
count=0

while(cap.isOpened()):
 # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
    cv2.circle(frame, maxLoc, 20, (0, 255, 0), 2)

    frame = cv2.resize(frame, (540, 960))                    # Resize image

    cv2.imshow("image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
