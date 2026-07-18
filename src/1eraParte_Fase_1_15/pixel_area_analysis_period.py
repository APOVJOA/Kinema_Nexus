import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error al leer frame")
        break

    alto, ancho, _ = frame.shape

    centro_y = alto // 2
    centro_x = ancho // 2

    mitad_roi = 50

    inicio_y = max(0, centro_y - mitad_roi)
    fin_y = min(alto, centro_y + mitad_roi)

    inicio_x = max(0, centro_x - mitad_roi)
    fin_x = min(ancho, centro_x + mitad_roi)

    roi = frame[inicio_y:fin_y, inicio_x:fin_x]

    if roi.size != 0:
        b_medio, g_medio, r_medio = roi.mean(axis=(0, 1))
        print(f"R:{r_medio:.0f} G:{g_medio:.0f} B:{b_medio:.0f}")

    cv2.imshow("Imagen Completa", frame)
    cv2.imshow("ROI", roi)

    # espera 3 segundos
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(3)

cap.release()
cv2.destroyAllWindows()