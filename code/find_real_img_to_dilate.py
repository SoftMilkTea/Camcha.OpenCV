# dilate 알고리즘으로 실제 카메라 크기의 이미지 찾아보기
# dilate 알고리즘은 작은 점을 키워주는 알고리즘
# 비디오로 찾기
# 파일 경로는 알아서 주세요


import cv2

cap = cv2.VideoCapture("/Users/heetop/Desktop/Dataset/bright_dot_real_1.mp4")
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
count=0

while(cap.isOpened()):
 # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh= cv2.threshold(gray,170,255,cv2.THRESH_TOZERO)
    # blur = cv2.GaussianBlur(gray,(5,5),0)
    dilate = cv2.dilate(thresh,None,iterations=1)

    # frame = cv2.resize(frame, (540, 960))                    # Resize image
    dilate = cv2.resize(dilate,(540,960))
    cv2.imshow("image", dilate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
