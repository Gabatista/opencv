import cv2
import numpy as np

img = cv2.imread("resources/lena.jpg")

#preenchendo o kernel com 1s, dilatando
kernel = np.ones((5,5),np.uint8)


#passando para escala de cinza
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#colocando blur, ksize deve ser impar
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

#detector de beiras, quanto maior, menos beiras
imgCanny = cv2.Canny(img, 150, 300)

#dilatação
imgDialation = cv2.dilate(imgCanny, kernel,iterations=1)

#oposto de dilatação
imgErosiva = cv2.erode(imgDialation, kernel,iterations=1)

cv2.imshow("Cinza", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dialation", imgDialation)
cv2.imshow("Erosiva", imgErosiva)
cv2.waitKey(0)