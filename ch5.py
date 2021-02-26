#perspectiva
import cv2
import numpy as np

img = cv2.imread('resources/dino.jpg')

#'esquina'
altura, largura = 250,350


pts1 = np.float32([[111,210],[210,190],[231,180],[312,450]])
pts2 = np.float32([[0,0],[largura,0],[0,altura],[largura,altura]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgSaida = cv2.warpPerspective(img,matrix,(largura,altura))



cv2.imshow("Dino1", img)
cv2.imshow("Dino", imgSaida)

cv2.waitKey(0)