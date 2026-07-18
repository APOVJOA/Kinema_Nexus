import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

# Historial de posiciones del objeto
trayectoria = []

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
    kernel = np.ones((5, 5), np.uint8)
    mascara_limpia = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE,kernel)

    # Buscar contornos
    contornos, _ = cv2.findContours(mascara_limpia,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:

        # Contorno más grande
        contorno_principal = max(contornos,key=cv2.contourArea)

        # Dibujar contorno
        cv2.drawContours(frame,[contorno_principal],-1,(0, 255, 0),2)

        # Calcular centro
        M = cv2.moments(contorno_principal)

        if M["m00"] != 0:

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Guardar posición
            trayectoria.append((cx, cy))

            # Mantener únicamente los últimos 100 puntos
            if len(trayectoria) > 100:
                trayectoria.pop(0)

            # Dibujar trayectoria
            for i in range(1, len(trayectoria)):
                cv2.line(frame,trayectoria[i - 1],trayectoria[i],(255, 255, 0),
                    2)

            # Dibujar centro
            cv2.circle(frame,(cx, cy),5,(255, 0, 0),-1)

            # Área del objeto
            area = cv2.contourArea(contorno_principal)

            # Mostrar coordenadas
            cv2.putText(frame,f"X:{cx} Y:{cy}",(cx + 10, cy - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255, 255, 255),2)

            # Mostrar área
            cv2.putText(frame,f"Area:{area:.0f}",(cx + 10, cy + 15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255, 255, 255),2)

    # Mostrar resultados
    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara Roja", mascara)
    cv2.imshow("Mascara Limpia", mascara_limpia)

    # Salir con Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()