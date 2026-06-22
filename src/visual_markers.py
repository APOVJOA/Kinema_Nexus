import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

ret, frame = cap.read()

if ret:

    # Dimensiones de la imagen
    alto, ancho, canales = frame.shape

    # Centro dinámico
    centro_y = alto // 2
    centro_x = ancho // 2

    # Tamaño de la ROI
    mitad_roi = 50

    # Límites de la ROI
    inicio_y = centro_y - mitad_roi
    fin_y = centro_y + mitad_roi

    inicio_x = centro_x - mitad_roi
    fin_x = centro_x + mitad_roi

    # Extraer ROI
    roi = frame[inicio_y:fin_y, inicio_x:fin_x]

    # Color medio de la ROI
    b_medio, g_medio, r_medio = roi.mean(axis=(0, 1))

    # Información
    print("Shape original:", frame.shape)
    print("Shape ROI:", roi.shape)

    print(f"Azul medio: {b_medio:.2f}")
    print(f"Verde medio: {g_medio:.2f}")
    print(f"Rojo medio: {r_medio:.2f}")

    # Dibujar
    cv2.circle(frame, (centro_x, centro_y), 10, (0, 0, 255), -1)

    cv2.line(frame, (0, 0), (centro_x, centro_y), (0, 255, 0), 2)


    cv2.rectangle(frame,(inicio_x, inicio_y),(fin_x, fin_y),(255, 0, 0),2)

    texto = f"({centro_x},{centro_y})"

    cv2.putText(frame,texto,(centro_x + 10, centro_y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255, 255, 255),1)

    # Mostrar imágenes
    cv2.imshow("Imagen Completa", frame)
    cv2.imshow("ROI", roi)
  

    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()