import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

cx_anterior = None
cy_anterior = None

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
    mascara = cv2.inRange(hsv, rojo_bajo, rojo_alto)

   # Limpiar máscara
    kernel = np.ones((5,5), np.uint8)

    mascara_limpia = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE,kernel)
    # Buscar contornos
    contornos, _ = cv2.findContours(mascara_limpia,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:

        contorno_principal = max(contornos,key=cv2.contourArea)
# Dibujar contornos
        cv2.drawContours(frame,contorno_principal,-1,(0,255,0), 2)

# Calcular centros
        M = cv2.moments(contorno_principal)

        if M["m00"] != 0:

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print(f"X:{cx} Y:{cy}")
            if cx_anterior is not None:

                cv2.line(frame,(cx_anterior, cy_anterior),(cx, cy),(255, 255, 0),2)

            cv2.circle(frame,(cx, cy),5,(255,0,0),-1)

            area = cv2.contourArea(contorno_principal)
            print(area)
            cv2.putText(frame,f"X:{cx} Y:{cy}",(cx + 10, cy - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255, 255, 255),2)
    # Mostrar resultados
    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara Roja", mascara)
    cv2.imshow("Mascara Limpia", mascara_limpia)
    # Salir con Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cx_anterior = cx
    cy_anterior = cy

cap.release()
cv2.destroyAllWindows()