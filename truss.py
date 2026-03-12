'''Docstring for truss container class'''
class Truss:
    '''Doctring for creating container class'''
    def __init__(self):
        self.joints = {}
        self.members = {}

    def add_joint(self, joint):
        '''Docstring for adding joints'''
        self.joints[joint.name] = joint #function to add or include joints in the truss container

    def add_member(self, member):
        '''Docstring for adding members'''
        self.members[member.name] = member #function to add or include members in the truss container
