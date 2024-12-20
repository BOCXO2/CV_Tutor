import cv2
import numpy as np

img = cv2.imread('images/image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img = cv2.merge([r, g, b])
cv2.imshow('My Image', img)
cv2.waitKey(0)