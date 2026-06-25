import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error al leer frame")
        break

    # Conversión a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rango de color rojo
    rojo_bajo = np.array([0, 100, 100])
    rojo_alto = np.array([10, 255, 255])

    # Crear máscara
    mascara = cv2.inRange(hsv,rojo_bajo,rojo_alto)

    # Mostrar resultados
    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara Roja", mascara)

    # Salir con Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()