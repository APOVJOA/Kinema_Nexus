import cv2
import json
import time
import subprocess
import numpy as np
import sys
from pathlib import Path

from ultralytics import YOLO

from pose import HumanPose
from pose_math import calculate_vector, calculate_angle, calculate_distance


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

CAMERA_INDEX = 0

WINDOW_NAME = "KINEMA NEXUS - Calibration"

REFERENCE_IMAGE = (
    Path(__file__).resolve().parent.parent
    / "images"
    / "postura_referencia.png"
)

PANEL_WIDTH = 640
PANEL_HEIGHT = 480

MIN_CONFIDENCE = 0.3

MIN_ANGLE = 50
MAX_ANGLE = 170

CALIBRATION_DURATION = 4.0
SAMPLE_INTERVAL = 0.25


# ==========================================================
# IMAGEN DE REFERENCIA
# ==========================================================

def resize_reference_image(image):

    height, width = image.shape[:2]

    # Mantener proporción
    scale = min(
        PANEL_WIDTH / width,
        PANEL_HEIGHT / height
    )

    new_width = int(width * scale)
    new_height = int(height * scale)

    resized = cv2.resize(
        image,
        (new_width, new_height)
    )

    # Crear panel negro
    panel = np.zeros(
        (PANEL_HEIGHT, PANEL_WIDTH, 3),
        dtype=image.dtype
    )

    # Centrar imagen
    x = (PANEL_WIDTH - new_width) // 2
    y = (PANEL_HEIGHT - new_height) // 2

    panel[
        y:y + new_height,
        x:x + new_width
    ] = resized

    return panel
# ==========================================================
# INICIAR HUMAN POSE DETECTION
# ==========================================================

def start_human_pose_detection():

    human_pose_path = (
        Path(__file__).resolve().parent
        / "human_pose_detection.py"
    )

    print("Calibración completada.")
    print("Iniciando Human Pose Detection...")

    subprocess.run(
        [sys.executable, str(human_pose_path)]
    )


# ==========================================================
# DETECTAR CUERPO SUPERIOR
# ==========================================================

def detect_upper_body(keypoints):

    if keypoints is None or len(keypoints.xy) == 0:
        return False

    conf = keypoints.conf[0]

    # Hombros, codos y muñecas
    required_points = [5, 6, 7, 8, 9, 10]

    for point in required_points:

        if conf[point] < MIN_CONFIDENCE:
            return False

    return True


# ==========================================================
# CREAR HUMAN POSE
# ==========================================================

def create_pose(keypoints):

    pose = HumanPose()

    puntos = keypoints.xy[0]
    conf = keypoints.conf[0]

    # ------------------------------------------------------
    # Hombros
    # ------------------------------------------------------

    pose.left_shoulder.x = float(puntos[5][0])
    pose.left_shoulder.y = float(puntos[5][1])
    pose.left_shoulder.confidence = float(conf[5])

    pose.right_shoulder.x = float(puntos[6][0])
    pose.right_shoulder.y = float(puntos[6][1])
    pose.right_shoulder.confidence = float(conf[6])

    # ------------------------------------------------------
    # Codos
    # ------------------------------------------------------

    pose.left_elbow.x = float(puntos[7][0])
    pose.left_elbow.y = float(puntos[7][1])
    pose.left_elbow.confidence = float(conf[7])

    pose.right_elbow.x = float(puntos[8][0])
    pose.right_elbow.y = float(puntos[8][1])
    pose.right_elbow.confidence = float(conf[8])

    # ------------------------------------------------------
    # Muñecas
    # ------------------------------------------------------

    pose.left_wrist.x = float(puntos[9][0])
    pose.left_wrist.y = float(puntos[9][1])
    pose.left_wrist.confidence = float(conf[9])

    pose.right_wrist.x = float(puntos[10][0])
    pose.right_wrist.y = float(puntos[10][1])
    pose.right_wrist.confidence = float(conf[10])

    return pose


# ==========================================================
# COMPROBAR ÁNGULOS
# ==========================================================

def check_pose_angles(pose):

    # ------------------------------------------------------
    # Brazo izquierdo
    # ------------------------------------------------------

    brazo_izquierdo = calculate_vector(
        pose.left_elbow,
        pose.left_shoulder
    )

    antebrazo_izquierdo = calculate_vector(
        pose.left_elbow,
        pose.left_wrist
    )

    angulo_izquierdo = calculate_angle(
        brazo_izquierdo,
        antebrazo_izquierdo
    )

    # ------------------------------------------------------
    # Brazo derecho
    # ------------------------------------------------------

    brazo_derecho = calculate_vector(
        pose.right_elbow,
        pose.right_shoulder
    )

    antebrazo_derecho = calculate_vector(
        pose.right_elbow,
        pose.right_wrist
    )

    angulo_derecho = calculate_angle(
        brazo_derecho,
        antebrazo_derecho
    )

    # ------------------------------------------------------
    # Comprobar rangos
    # ------------------------------------------------------

    left_valid = (
        MIN_ANGLE <= angulo_izquierdo <= MAX_ANGLE
    )

    right_valid = (
        MIN_ANGLE <= angulo_derecho <= MAX_ANGLE
    )

    return left_valid and right_valid


# ==========================================================
# MEDIR DISTANCIAS
# ==========================================================

def calculate_pose_measurements(pose):

    return {
        "left_arm_length": calculate_distance(
            pose.left_shoulder,
            pose.left_elbow
        ),

        "left_forearm_length": calculate_distance(
            pose.left_elbow,
            pose.left_wrist
        ),

        "right_arm_length": calculate_distance(
            pose.right_shoulder,
            pose.right_elbow
        ),

        "right_forearm_length": calculate_distance(
            pose.right_elbow,
            pose.right_wrist
        )
    }


# ==========================================================
# GUARDAR CALIBRACIÓN
# ==========================================================

def save_calibration(measurements):

    calibration_file = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "calibration.json"
    )

    calibration_file.parent.mkdir(
        exist_ok=True
    )

    with open(
        calibration_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            measurements,
            file,
            indent=4
        )

    print(
        f"Calibración guardada en: {calibration_file}"
    )


# ==========================================================
# DIBUJAR LANDMARKS
# ==========================================================

def draw_landmarks(frame, keypoints):

    puntos = keypoints.xy[0]
    conf = keypoints.conf[0]

    for i in range(len(puntos)):

        if conf[i] > MIN_CONFIDENCE:

            x = int(puntos[i][0])
            y = int(puntos[i][1])

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )


# ==========================================================
# MENSAJES
# ==========================================================

def draw_calibration_messages(frame):

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


# ==========================================================
# CALIBRATION
# ==========================================================

def start_calibration():

    # ------------------------------------------------------
    # Cargar modelo
    # ------------------------------------------------------

    model = YOLO("yolo11n-pose.pt")

    # ------------------------------------------------------
    # Cargar imagen de referencia
    # ------------------------------------------------------

    reference = cv2.imread(
        str(REFERENCE_IMAGE)
    )

    if reference is None:

        print(
            "Error: no se pudo cargar "
            "la imagen de referencia."
        )

        print(REFERENCE_IMAGE)

        return

    reference_panel = resize_reference_image(
        reference
    )

    # ------------------------------------------------------
    # Abrir cámara
    # ------------------------------------------------------

    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():

        print(
            "Error: no se pudo abrir la cámara."
        )

        return

    # ------------------------------------------------------
    # Variables de calibración
    # ------------------------------------------------------

    calibrating = False

    calibration_start_time = None

    last_sample_time = None

    measurements = {
        "left_arm_length": [],
        "left_forearm_length": [],
        "right_arm_length": [],
        "right_forearm_length": []
    }

    # ======================================================
    # BUCLE PRINCIPAL
    # ======================================================

    while True:

        ret, frame = cap.read()

        if not ret:

            print(
                "Error: no se pudo obtener el frame."
            )

            break

        # --------------------------------------------------
        # Inferencia YOLO
        # --------------------------------------------------

        results = model(frame)

        keypoints = results[0].keypoints

        # --------------------------------------------------
        # Dibujar detección
        # --------------------------------------------------

        if (
            keypoints is not None
            and len(keypoints.xy) > 0
        ):

            draw_landmarks(
                frame,
                keypoints
            )

        # --------------------------------------------------
        # Mensajes generales
        # --------------------------------------------------

        draw_calibration_messages(frame)

        # ==================================================
        # DETECCIÓN DE PERSONA
        # ==================================================

        pose_valid = False
        pose = None

        if (
            keypoints is not None
            and len(keypoints.xy) > 0
        ):

            if detect_upper_body(keypoints):

                # Crear HumanPose
                pose = create_pose(
                    keypoints
                )

                # Comprobar postura
                pose_valid = check_pose_angles(
                    pose
                )

        # ==================================================
        # POSTURA CORRECTA
        # ==================================================

        if pose_valid:

            cv2.putText(
                frame,
                "POSTURA CORRECTA",
                (20, 135),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

            # --------------------------------------------------
            # INICIAR CALIBRACIÓN
            # --------------------------------------------------

            if not calibrating:

                calibrating = True

                calibration_start_time = time.time()

                last_sample_time = calibration_start_time

                measurements = {
                    "left_arm_length": [],
                    "left_forearm_length": [],
                    "right_arm_length": [],
                    "right_forearm_length": []
                }

            # --------------------------------------------------
            # TIEMPO DE CALIBRACIÓN
            # --------------------------------------------------

            current_time = time.time()

            calibration_elapsed = (
                current_time
                - calibration_start_time
            )

            # --------------------------------------------------
            # TOMAR MUESTRA
            # --------------------------------------------------

            if (
                current_time - last_sample_time
                >= SAMPLE_INTERVAL
            ):

                sample = calculate_pose_measurements(
                    pose
                )

                measurements[
                    "left_arm_length"
                ].append(
                    sample["left_arm_length"]
                )

                measurements[
                    "left_forearm_length"
                ].append(
                    sample["left_forearm_length"]
                )

                measurements[
                    "right_arm_length"
                ].append(
                    sample["right_arm_length"]
                )

                measurements[
                    "right_forearm_length"
                ].append(
                    sample["right_forearm_length"]
                )

                last_sample_time = current_time

            # --------------------------------------------------
            # MOSTRAR PROGRESO
            # --------------------------------------------------

            remaining_time = max(
                0,
                CALIBRATION_DURATION
                - calibration_elapsed
            )

            if calibrating:

                cv2.putText(
                    frame,
                    f"CALIBRANDO: {remaining_time:.1f}s",
                    (20, 165),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 255),
                    2
                )

            # --------------------------------------------------
            # FINALIZAR CALIBRACIÓN
            # --------------------------------------------------

            if (
                calibrating
                and calibration_elapsed >= CALIBRATION_DURATION
            ):

                if len(
                    measurements["left_arm_length"]
                ) > 0:

                    calibrated_measurements = {

                        "left_arm_length": float(
                            np.mean(
                                measurements[
                                    "left_arm_length"
                                ]
                            )
                        ),

                        "left_forearm_length": float(
                            np.mean(
                                measurements[
                                    "left_forearm_length"
                                ]
                            )
                        ),

                        "right_arm_length": float(
                            np.mean(
                                measurements[
                                    "right_arm_length"
                                ]
                            )
                        ),

                        "right_forearm_length": float(
                            np.mean(
                                measurements[
                                    "right_forearm_length"
                                ]
                            )
                        )
                    }

                    save_calibration(
                        calibrated_measurements
                    )

                    print(
                        "================================"
                    )

                    print(
                        "CALIBRACION COMPLETADA"
                    )

                    print(
                        calibrated_measurements
                    )

                    print(
                        "================================"
                    )

                    calibrating = False

                    calibration_start_time = None

                    last_sample_time = None
                   
                    cap.release()
                    cv2.destroyAllWindows()

                    start_human_pose_detection()


                    return

        # ==================================================
        # POSTURA INCORRECTA / PERSONA NO DETECTADA
        # ==================================================

        else:

            if (
                keypoints is not None
                and len(keypoints.xy) > 0
            ):

                if detect_upper_body(keypoints):

                    cv2.putText(
                        frame,
                        "AJUSTA LA POSTURA",
                        (20, 135),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 255),
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

            else:

                cv2.putText(
                    frame,
                    "NO SE DETECTA NINGUNA PERSONA",
                    (20, 135),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 255),
                    2
                )

        # ==================================================
        # PREPARAR CÁMARA
        # ==================================================

        camera_panel = cv2.resize(
            frame,
            (PANEL_WIDTH, PANEL_HEIGHT)
        )

        # ==================================================
        # MOSTRAR REFERENCIA + CÁMARA
        # ==================================================

        combined = cv2.hconcat(
            [
                reference_panel,
                camera_panel
            ]
        )

        cv2.imshow(
            WINDOW_NAME,
            combined
        )

        # ==================================================
        # SALIR
        # ==================================================

        if cv2.waitKey(1) & 0xFF == ord("q"):

            break

    # ======================================================
    # LIBERAR RECURSOS
    # ======================================================

    cap.release()

    cv2.destroyAllWindows()


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    start_calibration()