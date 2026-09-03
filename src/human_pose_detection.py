import cv2
from ultralytics import YOLO

from pose import HumanPose
from pose_drawer import draw_pose

from relative_pose import calculate_relative_arm_pose
from robot_mapping import load_robot_mapping
from robot_motion import update_robot_motion
robot_mapping = load_robot_mapping()
# -----------------------------
# Cargar modelo
# -----------------------------

model = YOLO("yolo11n-pose.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # Inferencia
    # -----------------------------

    results = model(frame)

    # -----------------------------
    # Crear objeto Pose
    # -----------------------------

    pose = HumanPose()

    keypoints = results[0].keypoints

    if keypoints is not None and len(keypoints.xy) > 0:

        puntos = keypoints.xy[0]
        conf = keypoints.conf[0]

        # Nariz
        pose.nose.x = float(puntos[0][0])
        pose.nose.y = float(puntos[0][1])
        pose.nose.confidence = float(conf[0])

        # Ojos
        pose.left_eye.x = float(puntos[1][0])
        pose.left_eye.y = float(puntos[1][1])
        pose.left_eye.confidence = float(conf[1])

        pose.right_eye.x = float(puntos[2][0])
        pose.right_eye.y = float(puntos[2][1])
        pose.right_eye.confidence = float(conf[2])

        # Orejas
        pose.left_ear.x = float(puntos[3][0])
        pose.left_ear.y = float(puntos[3][1])
        pose.left_ear.confidence = float(conf[3])

        pose.right_ear.x = float(puntos[4][0])
        pose.right_ear.y = float(puntos[4][1])
        pose.right_ear.confidence = float(conf[4])

        # Hombros
        pose.left_shoulder.x = float(puntos[5][0])
        pose.left_shoulder.y = float(puntos[5][1])
        pose.left_shoulder.confidence = float(conf[5])

        pose.right_shoulder.x = float(puntos[6][0])
        pose.right_shoulder.y = float(puntos[6][1])
        pose.right_shoulder.confidence = float(conf[6])

        # Codos
        pose.left_elbow.x = float(puntos[7][0])
        pose.left_elbow.y = float(puntos[7][1])
        pose.left_elbow.confidence = float(conf[7])

        pose.right_elbow.x = float(puntos[8][0])
        pose.right_elbow.y = float(puntos[8][1])
        pose.right_elbow.confidence = float(conf[8])

        # Muñecas
        pose.left_wrist.x = float(puntos[9][0])
        pose.left_wrist.y = float(puntos[9][1])
        pose.left_wrist.confidence = float(conf[9])

        pose.right_wrist.x = float(puntos[10][0])
        pose.right_wrist.y = float(puntos[10][1])
        pose.right_wrist.confidence = float(conf[10])

        # Caderas
        pose.left_hip.x = float(puntos[11][0])
        pose.left_hip.y = float(puntos[11][1])
        pose.left_hip.confidence = float(conf[11])

        pose.right_hip.x = float(puntos[12][0])
        pose.right_hip.y = float(puntos[12][1])
        pose.right_hip.confidence = float(conf[12])

        # Rodillas
        pose.left_knee.x = float(puntos[13][0])
        pose.left_knee.y = float(puntos[13][1])
        pose.left_knee.confidence = float(conf[13])

        pose.right_knee.x = float(puntos[14][0])
        pose.right_knee.y = float(puntos[14][1])
        pose.right_knee.confidence = float(conf[14])

        # Tobillos
        pose.left_ankle.x = float(puntos[15][0])
        pose.left_ankle.y = float(puntos[15][1])
        pose.left_ankle.confidence = float(conf[15])

        pose.right_ankle.x = float(puntos[16][0])
        pose.right_ankle.y = float(puntos[16][1])
        pose.right_ankle.confidence = float(conf[16])

        pose.print_pose()
        relative_pose = calculate_relative_arm_pose(pose)
        print(relative_pose)

        robot_motion = update_robot_motion(relative_pose)

        print(robot_motion)
        draw_pose(frame, pose)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()