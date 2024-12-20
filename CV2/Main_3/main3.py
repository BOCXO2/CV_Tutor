import cv2
import numpy as np

img = cv2.imread('images/image.jpg')


# img = cv2.flip(img, 1)

def rotate(image, angle):
    height, width = image.shape[:2]
    point = (width / 2, height / 2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)

    return cv2.warpAffine(image, mat, (width, height))


def transform(image, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))


img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
# img = rotate(img, 180)
img = transform(img, 20, 20)
cv2.imshow('FlipImage', img)
cv2.waitKey(0)
