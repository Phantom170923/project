import cv2
import numpy as np

img = cv2.imread('color_text.jpg')

new_image = np.zeros(img.shape, dtype='uint8')
top_image = img[0:165, :]
middle_image = img[165:305, :]
bottom_image = img[306:, :]

top_image = cv2.cvtColor(top_image, cv2.COLOR_BGRA2GRAY)
top_image = cv2.GaussianBlur(top_image, (3, 3), 0)

middle_image = cv2.cvtColor(middle_image, cv2.COLOR_BGRA2GRAY)
middle_image = cv2.GaussianBlur(middle_image, (3, 3), 0)

bottom_image = cv2.cvtColor(bottom_image, cv2.COLOR_BGRA2GRAY)
bottom_image = cv2.GaussianBlur(bottom_image, (3, 3), 0)

top_image = cv2.Canny(top_image, 30, 50)
middle_image = cv2.Canny(middle_image, 30, 50)
bottom_image = cv2.Canny(bottom_image, 30, 50)

con1, hir1 = cv2.findContours(top_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
con2, hir2 = cv2.findContours(middle_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
con3, hir3 = cv2.findContours(bottom_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_image, con1, -1, (0, 255, 0), thickness=1)
cv2.drawContours(new_image[165:305, :], con2, -1, (0, 0, 255), thickness=1)
cv2.drawContours(new_image[306:, :], con3, -1, (224, 0, 255), thickness=1)


cv2.imshow('result', new_image)
cv2.waitKey(0)
