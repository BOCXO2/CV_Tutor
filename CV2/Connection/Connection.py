import cv2
import numpy as np

photo = cv2.imread('images/image.jpg')


photo = cv2.resize(photo, (photo.shape[1]//2, photo.shape[0]//2))
img = np.zeros(photo.shape[:2], dtype="uint8")

circle = cv2.circle(img.copy(), (0, 0), 80, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 250), 255, -1)

# img = cv2.bitwise_or(photo, photo, mask=circle)
# img = cv2.bitwise_and(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(photo, photo, mask=circle)

cv2.imshow("Result", photo)
cv2.waitKey(0)