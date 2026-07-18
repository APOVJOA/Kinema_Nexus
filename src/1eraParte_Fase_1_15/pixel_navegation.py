import cv2

# Intentamos conectar con la cámara principal del equipo
cap = cv2.VideoCapture(0)

# Verificamos que la cámara se ha abierto correctamente
if not cap.isOpened():
    print("Error: no se pudo abrir la cámara")
    exit()

# Capturamos un único frame para analizarlo
ret, frame = cap.read()

# Continuamos únicamente si la captura fue correcta
if ret:

    # Miramos pixeles en tres lados diferentes
    print("\nEsquina Superior Izquierda:")
    print(frame[0,0])

    print("\nCentro:")
    print(frame[240,320])

    print("\nEsquina Inferior Derecha:")
    print(frame[479,639])

# Liberamos la cámara al finalizar
cap.release()