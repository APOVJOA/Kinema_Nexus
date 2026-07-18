import cv2
import numpy as np
import json

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

# Historial de posiciones del objeto
trayectoria = []

distancia_total = 0
direccion = "Sin movimiento"
velocidad = 0
velocidad_media = 0

ancho_robot = 600      # mm
alto_robot = 500       # mm

# Zona de trabajo activa
zona_x_min = -150
zona_x_max = 150

zona_y_min = -100
zona_y_max = 100

ancho_imagen = 640     # px
alto_imagen = 480      # px

centro_imagen_x = ancho_imagen // 2
centro_imagen_y = alto_imagen// 2

escala_x = ancho_robot / ancho_imagen
escala_y = alto_robot / alto_imagen

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
            if len(trayectoria) >= 2:

                x1, y1 = trayectoria[-2]
                x2, y2 = trayectoria[-1]
                #Comparacion movimientos
                dx = x2 - x1
                dy = y2 - y1
                # Calculo velocidad
                velocidad = np.sqrt(dx**2 + dy**2)

                distancia_total += velocidad

                velocidad_media = distancia_total / (len(trayectoria) - 1)
                #Comprobacion de dirección
                if abs(dx) < 3 and abs(dy) < 3:

                    if dx > 0:
                        direccion = "Derecha"
                    else:
                        direccion = "Izquierda"

                else:

                    if dy > 0:
                        direccion = "Abajo"
                    else:
                        direccion = "Arriba"
                
                cv2.putText(frame,f"Direccion: {direccion}",(10, 30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 255, 255),2)
                cv2.putText(frame,f"dX:{dx}  dY:{dy}",(10, 60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
                cv2.putText(frame,f"Velocidad: {velocidad:.2f} px/frame",(10, 90),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0, 255, 255),2)
                cv2.putText(frame,f"Distancia: {distancia_total:.1f} px",(10, 120),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
                cv2.putText(frame,f"Velocidad media: {velocidad_media:.2f}",(10,150),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)            
                cv2.putText(frame,f"Puntos: {len(trayectoria)}",(10,180),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)

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

            x_mm = (cx - centro_imagen_x) * escala_x
            y_mm = (centro_imagen_y - cy) * escala_y

            cv2.putText(frame,f"Robot X:{x_mm:.1f} mm",(10, 210),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
            
            #Identificacion espacio de trabajo
            cv2.putText(frame,f"Robot Y:{y_mm:.1f} mm",(10,240),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
            if (-300 <= x_mm <= 300) and (-250 <= y_mm <= 250):
                estado = "Dentro del espacio"
            else:
                estado = "Fuera del espacio"
            cv2.putText(frame,estado,(10, 270),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0) if estado == "Dentro del espacio" else (0,0,255),2)
            datos_robot = {
                "x": x_mm,
                "y": y_mm,
                "area": area,
                "direccion": direccion,
                "velocidad": velocidad,
                "velocidad_media": velocidad_media,
                "distancia": distancia_total,
                "estado": estado
                }
            with open("data/robot_data.json", "w") as archivo:
                json.dump(datos_robot, archivo, indent=4)


    # Mostrar resultados
    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara Roja", mascara)
    cv2.imshow("Mascara Limpia", mascara_limpia)

    # Salir con Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()