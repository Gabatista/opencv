#redimensionar e cortar
#o sentido cartesiano se mantem no x mas inverte no y(apontando para baixo)


import cv2

img = cv2.imread('resources/fusca.jpeg')

#coordenadas da imagem (altura, largura, canais rgb)
print(img.shape)

#altura e largura
imgResize = cv2.resize(img,(720,2480))

#altura e largura
imgRecorte = img[0:200,200:500]

cv2.imshow('Imagem', img)
cv2.imshow("redimensionado", imgResize)
cv2.imshow("Recorte", imgRecorte)

cv2.waitKey(0)