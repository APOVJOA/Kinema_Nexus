from pose_math import calculate_vector


# ==========================================================
# POSICIONES RELATIVAS DEL BRAZO
# ==========================================================

def calculate_relative_arm_pose(pose):
    """
    Calcula los vectores relativos de los segmentos
    de ambos brazos del operador.

    Brazo:
        Hombro → Codo

    Antebrazo:
        Codo → Muñeca
    """

    # ------------------------------------------------------
    # Brazo izquierdo
    # ------------------------------------------------------

    left_arm = calculate_vector(
        pose.left_shoulder,
        pose.left_elbow
    )

    left_forearm = calculate_vector(
        pose.left_elbow,
        pose.left_wrist
    )

    # ------------------------------------------------------
    # Brazo derecho
    # ------------------------------------------------------

    right_arm = calculate_vector(
        pose.right_shoulder,
        pose.right_elbow
    )

    right_forearm = calculate_vector(
        pose.right_elbow,
        pose.right_wrist
    )

    # ------------------------------------------------------
    # Devolver vectores relativos
    # ------------------------------------------------------

    return {
        "left_arm": {
            "upper_arm": left_arm,
            "forearm": left_forearm
        },

        "right_arm": {
            "upper_arm": right_arm,
            "forearm": right_forearm
        }
    }