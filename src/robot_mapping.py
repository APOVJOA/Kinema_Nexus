import json
from pathlib import Path


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

CALIBRATION_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "calibration.json"
)


# ==========================================================
# MEDIDAS PROVISIONALES DEL ROBOT
# ==========================================================

# Estos valores son únicamente para pruebas.
# Se sustituirán cuando se defina el robot definitivo.

ROBOT_LEFT_ARM_LENGTH = 300.0
ROBOT_RIGHT_ARM_LENGTH = 300.0

ROBOT_LEFT_FOREARM_LENGTH = 280.0
ROBOT_RIGHT_FOREARM_LENGTH = 280.0


# ==========================================================
# CARGAR CALIBRACIÓN
# ==========================================================

def load_calibration():

    if not CALIBRATION_FILE.exists():

        raise FileNotFoundError(
            f"No se encontró el archivo de calibración: "
            f"{CALIBRATION_FILE}"
        )

    with open(
        CALIBRATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ==========================================================
# CALCULAR ESCALA
# ==========================================================

def calculate_scale(
    robot_length,
    human_length
):

    if human_length <= 0:

        raise ValueError(
            "La longitud humana debe ser mayor que cero."
        )

    return robot_length / human_length


# ==========================================================
# CREAR MAPEO HUMANO - ROBOT
# ==========================================================

def create_robot_mapping(calibration):

    # ------------------------------------------------------
    # Medidas del operador
    # ------------------------------------------------------

    human_left_arm = calibration["left_arm_length"]
    human_right_arm = calibration["right_arm_length"]

    human_left_forearm = calibration["left_forearm_length"]
    human_right_forearm = calibration["right_forearm_length"]

    # ------------------------------------------------------
    # Calcular relaciones
    # ------------------------------------------------------

    left_arm_scale = calculate_scale(
        ROBOT_LEFT_ARM_LENGTH,
        human_left_arm
    )

    right_arm_scale = calculate_scale(
        ROBOT_RIGHT_ARM_LENGTH,
        human_right_arm
    )

    left_forearm_scale = calculate_scale(
        ROBOT_LEFT_FOREARM_LENGTH,
        human_left_forearm
    )

    right_forearm_scale = calculate_scale(
        ROBOT_RIGHT_FOREARM_LENGTH,
        human_right_forearm
    )

    # ------------------------------------------------------
    # Devolver configuración de mapeo
    # ------------------------------------------------------

    return {
        "left_arm_scale": left_arm_scale,
        "right_arm_scale": right_arm_scale,
        "left_forearm_scale": left_forearm_scale,
        "right_forearm_scale": right_forearm_scale
    }


# ==========================================================
# CARGAR Y CREAR MAPEO
# ==========================================================

def load_robot_mapping():

    calibration = load_calibration()

    mapping = create_robot_mapping(
        calibration
    )

    return mapping