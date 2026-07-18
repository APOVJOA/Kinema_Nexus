class Landmark:

    def __init__(self, x=0, y=0, confidence=0):
        self.x = x
        self.y = y
        self.confidence = confidence

    def __repr__(self):
        return f"({self.x:.1f}, {self.y:.1f}) conf={self.confidence:.2f}"