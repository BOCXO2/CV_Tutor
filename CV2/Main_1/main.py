import cv2
import numpy as np

img = cv2.imread('images/image.jpg')
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
img = cv2.GaussianBlur(img, (9,9), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 90,90)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('Killua', img)
cv2.waitKey(0)

# video = cv2.VideoCapture('videos/rearview_driving_mounts_1080p.mp4')
# while True:
#     ret, frame = video.read()
#     cv2.imshow('Car', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# video_camera = cv2.VideoCapture(0)
# video_camera.set(5, 500)
# video_camera.set(5, 300)
# while True:
#     ret, frame = video_camera.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame = cv2.Canny(frame, 75, 150)
#     kernel = np.ones((5,5),np.uint8)
#     frame = cv2.dilate(frame, kernel, iterations=1)
#
#     cv2.imshow('Video', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


