'''Docstring for NumPy Calculations'''
import numpy as np

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
