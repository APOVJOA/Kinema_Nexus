import cv2

from pose_math import calculate_vector, calculate_angle, calculate_distance


# ==========================================================
# LANDMARKS
# ==========================================================

def draw_landmark(img, landmark, color):

    if landmark.confidence > 0.3:

        cv2.circle(
            img,
            (int(landmark.x), int(landmark.y)),
            6,
            color,
            -1
        )


# ==========================================================
# CONNECTIONS
# ==========================================================

def draw_connection(img, p1, p2, color=(255, 255, 255)):

    if p1.confidence > 0.3 and p2.confidence > 0.3:

        cv2.line(
            img,
            (int(p1.x), int(p1.y)),
            (int(p2.x), int(p2.y)),
            color,
            2
        )


# ==========================================================
# ANGLES
# ==========================================================

def draw_angles(img, pose):

    # -----------------------------
    # Brazo izquierdo
    # -----------------------------

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

    cv2.putText(
        img,
        f"{angulo_izquierdo:.1f}°",
        (
            int(pose.left_elbow.x + 10),
            int(pose.left_elbow.y - 10)
        ),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2
    )

    # -----------------------------
    # Brazo derecho
    # -----------------------------

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

    cv2.putText(
        img,
        f"{angulo_derecho:.1f}°",
        (
            int(pose.right_elbow.x + 10),
            int(pose.right_elbow.y - 10)
        ),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),
        2
    )


# ==========================================================
# DISTANCES
# ==========================================================

def draw_distances(img, pose):

    # -----------------------------
    # Brazo izquierdo
    # -----------------------------

    distancia_brazo_izquierdo = calculate_distance(
        pose.left_shoulder,
        pose.left_elbow
    )

    distancia_antebrazo_izquierdo = calculate_distance(
        pose.left_elbow,
        pose.left_wrist
    )

    # -----------------------------
    # Brazo derecho
    # -----------------------------

    distancia_brazo_derecho = calculate_distance(
        pose.right_shoulder,
        pose.right_elbow
    )

    distancia_antebrazo_derecho = calculate_distance(
        pose.right_elbow,
        pose.right_wrist
    )

    # -----------------------------
    # Mostrar distancias
    # -----------------------------

    cv2.putText(
        img,
        f"Brazo Izquierdo: {distancia_brazo_izquierdo:.1f}px",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        img,
        f"Antebrazp Izquierdo: {distancia_antebrazo_izquierdo:.1f}px",
        (20, 55),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        img,
        f"Brazo Derecho: {distancia_brazo_derecho:.1f}px",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        img,
        f"Antebrazo Derecho: {distancia_antebrazo_derecho:.1f}px",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )


# ==========================================================
# DRAW COMPLETE POSE
# ==========================================================

def draw_pose(frame, pose):

    frame_draw = frame.copy()

    # -----------------------------
    # Hombros
    # -----------------------------

    draw_landmark(
        frame_draw,
        pose.left_shoulder,
        (0, 0, 255)
    )

    draw_landmark(
        frame_draw,
        pose.right_shoulder,
        (0, 0, 255)
    )

    # -----------------------------
    # Codos
    # -----------------------------

    draw_landmark(
        frame_draw,
        pose.left_elbow,
        (0, 255, 0)
    )

    draw_landmark(
        frame_draw,
        pose.right_elbow,
        (0, 255, 0)
    )

    # -----------------------------
    # Muñecas
    # -----------------------------

    draw_landmark(
        frame_draw,
        pose.left_wrist,
        (255, 0, 0)
    )

    draw_landmark(
        frame_draw,
        pose.right_wrist,
        (255, 0, 0)
    )

    # -----------------------------
    # Brazo izquierdo
    # -----------------------------

    draw_connection(
        frame_draw,
        pose.left_shoulder,
        pose.left_elbow
    )

    draw_connection(
        frame_draw,
        pose.left_elbow,
        pose.left_wrist
    )

    # -----------------------------
    # Brazo derecho
    # -----------------------------

    draw_connection(
        frame_draw,
        pose.right_shoulder,
        pose.right_elbow
    )

    draw_connection(
        frame_draw,
        pose.right_elbow,
        pose.right_wrist
    )

    # -----------------------------
    # Ángulos
    # -----------------------------

    draw_angles(
        frame_draw,
        pose
    )

    # -----------------------------
    # Distancias
    # -----------------------------

    draw_distances(
        frame_draw,
        pose
    )

    # -----------------------------
    # Mostrar resultado
    # -----------------------------

    cv2.imshow(
        "KINEMA NEXUS",
        frame_draw
    )