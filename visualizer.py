'''Docstring for matploitlib Class'''
import matplotlib.pyplot as plt

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