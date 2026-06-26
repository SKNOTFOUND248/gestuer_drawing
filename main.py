import time

import cv2 
from hand_traker import HandTracker, Detect_Face


cam = cv2.VideoCapture("http://10.151.43.92.:8080/video")

if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()
hand_tracker = HandTracker()
face_detector = Detect_Face()
fps = 0
current_time = 0
prev_time = 0
while True:
    ret, frame = cam.read()
    if not ret:
        break
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    framr = cv2.flip(frame, 1)
    framr = hand_tracker.findHands(framr)
    framr = face_detector.detect_faces(framr)
    lmList = hand_tracker.findPosition(framr) 
    if lmList:
        print(lmList[8])   
    cv2.putText(framr, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Camera Feed", framr)
    
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()    