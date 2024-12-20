import cv2
import numpy as np

# BGR - в OpenCV
# RGB - стандарт

photo = np.zeros((450, 450, 3), dtype='uint8')
# photo[100:150, 200:280] = 70, 100, 30

cv2.rectangle(photo, (20, 20), (100, 100), (70, 100, 30), thickness=cv2.FILLED)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[1] // 2),  (70, 100, 30), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (70, 100, 30), thickness=cv2.FILLED)

cv2.putText(photo, 'AIProgrammer', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=4)

cv2.imshow('My_Photo', photo)
cv2.waitKey(0)

