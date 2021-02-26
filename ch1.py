import cv2

"""
ler imagem
img = cv2.imread('resources/lena.jpg')

cv2.imshow("Saída",img)
cv2.waitKey(0)

"""

"""
ler video
capt = cv2.VideoCapture('resources/test.mp4')

while True:
    success, img = capt.read()
    cv2.imshow("Vídeo",img)
    #'q' para sair do loop
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

"""

#usar webcam
capt = cv2.VideoCapture(0)
capt.set(3,640) #largura
capt.set(4,480) #altura
capt.set(10,100)#ajustando brilho

while True:
    success, img = capt.read()
    cv2.imshow("Vídeo",img)
    #'q' para sair do loop
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break