import cv2
import imutils
img = cv2.imread('bus.jpg')
resizedImg = imutils.resize(img, width=500)
cv2.imwrite('resizedImage.jpg', resizedImg)
