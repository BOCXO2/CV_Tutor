import cv2
import numpy as np

img = cv2.imread('images/image.jpg')
new_img = np.zeros(img.shape, dtype='uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)



cv2.drawContours(new_img, con, -1, (230, 111, 190), 1)
new_img = cv2.resize(new_img, (new_img.shape[1]//2, new_img.shape[0]//2))
cv2.imshow('IMAGE', new_img)
print(con)
cv2.waitKey(0)