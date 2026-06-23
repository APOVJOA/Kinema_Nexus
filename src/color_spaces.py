import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

ret, frame = cap.read()

if ret:

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Dimensiones de la imagen
    alto, ancho, canales = frame.shape

    # Centro dinámico
    centro_y = alto // 2
    centro_x = ancho // 2

   

    print("Pixel BGR:")
    print(frame[centro_y, centro_x])

    print("Pixel HSV:")
    print(hsv[centro_y, centro_x])

    # Información
    

    # Mostrar imágenes
    cv2.imshow("Imagen Completa", frame)
    

    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()