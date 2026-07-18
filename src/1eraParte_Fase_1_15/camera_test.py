import cv2

# Abrir la cámara principal
cap = cv2.VideoCapture(0)

# Comprobar que se ha abierto correctamente
if not cap.isOpened():
    print("Error: no se pudo abrir la cámara.")
    exit()

while True:

    # Capturar un frame
    ret, frame = cap.read()

    # Comprobar que el frame existe
    if not ret:
        print("Error al capturar el frame.")
        break

    # Mostrar el frame
    cv2.imshow("Kinema Nexus - Camera Test", frame)

    # Salir al pulsar Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()