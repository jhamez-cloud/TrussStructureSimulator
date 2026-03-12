from joint import Joint
from member import Member
from truss import Truss
from solver import TrussSolver
from visualizer import TrussVisualizer


# Create truss
truss = Truss()

# Create joints
A = Joint("A", 0, 0)
B = Joint("B", 5, 0)
C = Joint("C", 2.5, 4)

# Apply load
C.set_load(0, -1000)

# Add joints
truss.add_joint(A)
truss.add_joint(B)
truss.add_joint(C)

# Create members
m1 = Member("AB", A, B)
m2 = Member("BC", B, C)
m3 = Member("AC", A, C)

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