import cv2
cap = cv2.VideoCapture(3)
while True:
    success, img = cap.read()  
    #Gris
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # Normal
    color_img = img.copy() 
    # BInarizada
    _, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY) 
    # Mostrar las tres imágenes en ventanas separadas
    cv2.imshow("Escala de grises", gray_img)
    cv2.imshow("Color normal", color_img)
    cv2.imshow("Binarizada", binary_img) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()