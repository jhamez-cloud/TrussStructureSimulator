import math
import matplotlib.pyplot as plt
import numpy as np

class Joint:
    '''Docstring for joint'''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

        self.fx = 0  # horizontal forces at joint x
        self.fy = 0  # vertical forces at joint y

        # Support type: None, "pinned", "roller"
        self.support = None

    def set_load(self, fx, fy):
        '''Docstring for forces/loads'''
        self.fx = fx #providing forces values for x
        self.fy = fy #providing forces values for y

    def set_support(self, support_type):
        '''Docstring for supports'''
        self.support = support_type

class Member:
    '''Docstring for members or bars connecting joints'''

    def __init__(self, name, joint1, joint2):
        self.name = name
        self.joint1 = joint1
        self.joint2 = joint2
        self.force = None

    def length(self):
        '''Docstring for method used to calculate distances'''
        dx = self.joint2.x - self.joint1.x
        dy = self.joint2.y - self.joint1.y
        return math.sqrt(dx**2 + dy**2)

    def direction_cosines(self):
        '''Docstring for finding the direction of members'''
        L = self.length() #pylint:disable=c0103
        dx = self.joint2.x - self.joint1.x
        dy = self.joint2.y - self.joint1.y
        return dx/L, dy/L

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

class TrussVisualizer:
    '''Docstring For Matploitlib Visual work'''
    def __init__(self, truss):
        self.truss = truss

    def draw(self):
        '''Docstring for plotting points'''

        for member in self.truss.members.values():

            x = [member.joint1.x, member.joint2.x]
            y = [member.joint1.y, member.joint2.y]

            plt.plot(x, y, 'b-o')

            midx = (x[0]+x[1])/2
            midy = (y[0]+y[1])/2

            if member.force is not None:
                plt.text(midx, midy, f"{member.force:.1f}")

        plt.title("Truss Structure")
        plt.axis("equal")
        plt.show()

class TrussSolver:
    '''Docstring for calculating related truss structure calculations'''
    def __init__(self, truss):
        self.truss = truss

    def solve(self):
        '''Docstring for calculations'''
        members = list(self.truss.members.values())
        joints = list(self.truss.joints.values())

        n_members = len(members)
        n_joints = len(joints)

        A = np.zeros((2*n_joints, n_members))
        b = np.zeros(2*n_joints)

        joint_index = {joint.name:i for i,joint in enumerate(joints)}

        for m_index, member in enumerate(members):

            c, s = member.direction_cosines()

            j1 = joint_index[member.joint1.name]
            j2 = joint_index[member.joint2.name]

            A[2*j1][m_index] = c
            A[2*j1+1][m_index] = s

            A[2*j2][m_index] = -c
            A[2*j2+1][m_index] = -s


        for joint in joints:

            j = joint_index[joint.name]

            b[2*j] = -joint.fx
            b[2*j+1] = -joint.fy


        forces = np.linalg.lstsq(A, b, rcond=None)[0]

        for i, member in enumerate(members):
            member.force = forces[i]

        return members

truss = Truss()

number_of_joints = int(input("How many joints has your truss? : "))

joints = []

for i in range(number_of_joints):

    point_name = input("Enter the name of joint: ")
    x, y = map(float, input("Enter x and y coordinates for point: ").split())

    joint = Joint(point_name, x, y)
    joints.append(joint)

    truss.add_joint(joint)



# Apply load
joints[2].set_load(0, -1000)

# Add joints
truss.add_joint(joints[0])
truss.add_joint(joints[1])
truss.add_joint(joints[2])

# Create members
m1 = Member("AB", joints[0], joints[1])
m2 = Member("BC", joints[1], joints[2])
m3 = Member("AC", joints[0], joints[2])

truss.add_member(m1)
truss.add_member(m2)
truss.add_member(m3)

# Solve
solver = TrussSolver(truss)
members = solver.solve()

# Print forces
for m in members:
    print(m.name, m.force)

# Visualize
vis = TrussVisualizer(truss)
vis.draw()

