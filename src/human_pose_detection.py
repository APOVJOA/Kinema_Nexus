import cv2
from ultralytics import YOLO

# Cargar modelo de pose
model = YOLO("yolo11n-pose.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Inferencia
    results = model(frame)

    # Dibujar resultados
    annotated = results[0].plot()

    cv2.imshow("YOLO Pose", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()