import cv2
from ultralytics import YOLO


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

CAMERA_INDEX = 0
WINDOW_NAME = "KINEMA NEXUS - Calibration"


# ==========================================================
# CALIBRATION
# ==========================================================

def start_calibration():
    model = YOLO("yolo11n-pose.pt")
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("Error: no se pudo abrir la cámara.")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Error: no se pudo obtener el frame.")
            break

        # ------------------------------------------------------
        # Inferencia YOLO
        # ------------------------------------------------------

        results = model(frame)

        keypoints = results[0].keypoints
         # ------------------------------------------------------
        # Dibujar detección
        # ------------------------------------------------------

        if keypoints is not None and len(keypoints.xy) > 0:

            # Primera persona detectada
            puntos = keypoints.xy[0]
            conf = keypoints.conf[0]

        # Dibujar puntos detectados
            for i in range(len(puntos)):

                if conf[i] > 0.3:

                    x = int(puntos[i][0])
                    y = int(puntos[i][1])

                    cv2.circle(
                        frame,
                        (x, y),
                        5,
                        (0, 255, 0),
                        -1
                    )   


        # --------------------------------------------------
        # Mensaje de calibración
        # --------------------------------------------------

        cv2.putText(
            frame,
            "CALIBRACION INICIAL",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Colocate dentro del area de la camara",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Adopta la postura indicada",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )
        if keypoints is not None and len(keypoints.xy) > 0:

            if detect_upper_body(keypoints):

                cv2.putText(
            frame,
            "PERSONA DETECTADA",
            (20, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

            else:

                cv2.putText(
            frame,
            "COLOCA LOS BRAZOS DENTRO DE LA CAMARA",
            (20, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

        # --------------------------------------------------
        # Mostrar cámara
        # --------------------------------------------------

        cv2.imshow(WINDOW_NAME, frame)

        # --------------------------------------------------
        # Salir
        # --------------------------------------------------

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def detect_upper_body(keypoints):
    if keypoints is None or len(keypoints.xy) == 0:
        return False

    puntos = keypoints.xy[0]
    conf = keypoints.conf[0]

    # Landmarks necesarios:
    # hombro izquierdo 5
    # hombro derecho 6
    # codo izquierdo 7
    # codo derecho 8
    # muñeca izquierda 9
    # muñeca derecha 10

    required_points = [5, 6, 7, 8, 9, 10]

    for point in required_points:
        if conf[point] < 0.3:
            return False

    return True
# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":
    start_calibration()