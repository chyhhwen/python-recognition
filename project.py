import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    # 套用自適應二值化黑白影像
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    img_gray = cv2.medianBlur(img_gray, 5)
    output = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    faceCascade = cv2.CascadeClassifier('face_detect.xml')
    faceRect = faceCascade.detectMultiScale(img_gray, 2, 3)
    for (x, y, w, h) in faceRect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (51, 255, 254), 2)

    #cv2.imshow('oxxostudio', output)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break       # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()