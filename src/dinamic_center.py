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

    alto, ancho, canales = frame.shape

    centro_y = int(alto / 2)
    centro_x = int(ancho / 2)

    print("Alto:", alto)
    print("Ancho:", ancho)

    print("Centro Y:", centro_y)
    print("Centro X:", centro_x)

    print("\nPixel central:")
    print(frame[centro_y, centro_x])

# Liberamos la cámara al finalizar
cap.release()