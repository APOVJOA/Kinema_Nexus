from landmark import Landmark


class HumanPose:

    def __init__(self):

        self.nose = Landmark()

        self.left_eye = Landmark()
        self.right_eye = Landmark()

        self.left_ear = Landmark()
        self.right_ear = Landmark()

        self.left_shoulder = Landmark()
        self.right_shoulder = Landmark()

        self.left_elbow = Landmark()
        self.right_elbow = Landmark()

        self.left_wrist = Landmark()
        self.right_wrist = Landmark()

        self.left_hip = Landmark()
        self.right_hip = Landmark()

        self.left_knee = Landmark()
        self.right_knee = Landmark()

        self.left_ankle = Landmark()
        self.right_ankle = Landmark()
    def print_pose(self):

        print("LEFT SHOULDER :", self.left_shoulder)
        print("RIGHT SHOULDER:", self.right_shoulder)

        print("LEFT ELBOW :", self.left_elbow)
        print("RIGHT ELBOW:", self.right_elbow)

        print("LEFT WRIST :", self.left_wrist)
        print("RIGHT WRIST:", self.right_wrist)
    def print_all(self):

        for nombre, landmark in self.__dict__.items():
            print(f"{nombre:15} -> {landmark}")