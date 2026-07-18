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

    # Información
    print("Shape original:", frame.shape)
    print("Shape ROI:", roi.shape)

    # Mostrar imágenes
    cv2.imshow("Imagen Completa", frame)
    cv2.imshow("ROI", roi)

    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()