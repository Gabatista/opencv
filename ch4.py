#formas e textos
import cv2
import numpy as np

img = np.zeros((512, 512,3), np.uint8)

img[:] = 255, 255, 0

#traçando reta diagonal
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,0),3)

#pontos iniciais e finais, o 2 é a grossura
cv2.rectangle(img,(0,0),(250,350),(0,0,255),5 )
cv2.circle(img,(400,50),30,(255,0,0),5)

#localizao, fonte, escala
cv2.putText(img,"CV",(300,100),cv2.FONT_ITALIC,1,(255,0,0),5)

cv2.imshow("Imagem", img)

cv2.waitKey(0)
