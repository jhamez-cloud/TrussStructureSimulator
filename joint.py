'''Docstring for Truss Joints Object'''
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
