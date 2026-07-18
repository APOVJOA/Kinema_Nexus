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

    # Analizamos la estructura básica del frame
    print("Tipo de dato:")
    print(type(frame))

    print("\nDimensiones:")
    print(frame.shape)

    print("\nNúmero total de elementos:")
    print(frame.size)

    # Inspeccionamos el píxel situado en la esquina superior izquierda
    print("\nValor del píxel [0,0]:")
    print(frame[0,0])

    # Separamos los canales BGR de ese mismo píxel
    print("\nCanal Azul:")
    print(frame[0,0,0])

    print("\nCanal Verde:")
    print(frame[0,0,1])

    print("\nCanal Rojo:")
    print(frame[0,0,2])

# Liberamos la cámara al finalizar
cap.release()