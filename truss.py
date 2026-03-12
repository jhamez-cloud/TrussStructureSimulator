class Truss:

    def __init__(self):
        self.joints = {}
        self.members = {}

    def add_joint(self, joint):
        self.joints[joint.name] = joint

    def add_member(self, member):
        self.members[member.name] = member