import cv2
import numpy as np

img = cv2.imread('image.jpg')
blue, green, red = cv2.split(img)


cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)
cv2.waitKey(0)


g = np.zeros_like(green)

new_img = cv2.merge((blue, green * 0, red))
cv2.imshow('New Image', new_img)
cv2.waitKey(0)
merged_img = cv2.merge((blue, green, red))
cv2.imshow('Merged Image', merged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
