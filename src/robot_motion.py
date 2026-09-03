import json
from pathlib import Path
import math

from pose_math import calculate_angle


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "robot_motion.json"
)


# ==========================================================
# LIMITES PROVISIONALES DEL ROBOT
# ==========================================================

J1_MIN = -180.0
J1_MAX = 180.0

J2_MIN = -180.0
J2_MAX = 180.0

J3_MIN = -180.0
J3_MAX = 180.0


# ==========================================================
# LIMITAR VALOR
# ==========================================================

def clamp(value, minimum, maximum):

    return max(
        minimum,
        min(value, maximum)
    )


# ==========================================================
# CALCULAR MOVIMIENTO DEL ROBOT
# ==========================================================

def calculate_robot_motion(relative_pose):

    # ------------------------------------------------------
    # Obtener vectores del brazo derecho
    # ------------------------------------------------------

    upper_arm = relative_pose["right_arm"]["upper_arm"]
    forearm = relative_pose["right_arm"]["forearm"]

    # ------------------------------------------------------
    # Ángulo del brazo respecto al eje X
    # ------------------------------------------------------

    shoulder_angle = math.degrees(
        math.atan2(
            upper_arm[1],
            upper_arm[0]
        )
    )

    # ------------------------------------------------------
    # Ángulo entre brazo y antebrazo
    # ------------------------------------------------------

    elbow_angle = calculate_angle(
        upper_arm,
        forearm
    )

    # ------------------------------------------------------
    # Conversión provisional a articulaciones del UR
    # ------------------------------------------------------

    j1 = shoulder_angle

    j2 = -shoulder_angle

    j3 = 180.0 - elbow_angle

    # ------------------------------------------------------
    # Aplicar límites
    # ------------------------------------------------------

    j1 = clamp(
        j1,
        J1_MIN,
        J1_MAX
    )

    j2 = clamp(
        j2,
        J2_MIN,
        J2_MAX
    )

    j3 = clamp(
        j3,
        J3_MIN,
        J3_MAX
    )

    # ------------------------------------------------------
    # Crear configuración
    # ------------------------------------------------------

    return {
        "joints": [
            j1,
            j2,
            j3,
            0.0,
            0.0,
            0.0
        ]
    }


# ==========================================================
# GUARDAR JSON
# ==========================================================

def save_robot_motion(robot_motion):

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            robot_motion,
            file,
            indent=4
        )


# ==========================================================
# FUNCIÓN PRINCIPAL
# ==========================================================

def update_robot_motion(relative_pose):

    robot_motion = calculate_robot_motion(
        relative_pose
    )

    save_robot_motion(
        robot_motion
    )

    return robot_motion