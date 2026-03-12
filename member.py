import math

class Member:

    def __init__(self, name, joint1, joint2):
        self.name = name
        self.joint1 = joint1
        self.joint2 = joint2
        self.force = None

    def length(self):
        dx = self.joint2.x - self.joint1.x
        dy = self.joint2.y - self.joint1.y
        return math.sqrt(dx**2 + dy**2)

    def direction_cosines(self):
        L = self.length()
        dx = self.joint2.x - self.joint1.x
        dy = self.joint2.y - self.joint1.y
        return dx/L, dy/L