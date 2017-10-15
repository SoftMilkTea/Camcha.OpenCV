
import cv2

cap = cv2.VideoCapture(0)


while(True):
 # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blur)
    cv2.circle(frame, maxLoc, 20, (0, 255, 0), 2)



    cv2.imshow("image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
