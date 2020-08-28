
# element instance

# Joseph Rudick
# Edited: 8/28/2020

# node1 - 1st connected node (node instance)
# node2 - 2nd connected node (node instance)
# A - element cross-section area (float)
# E - element modulus of elasticity (float)
# I - element area moment of inertia (float)
# color - element color (matplotlib color string)

import numpy as np

class element:
    def __init__(self, node1, node2, A, E, I, color):
        self.node1 = node1
        self.node2 = node2
        self.A = A
        self.E = E
        self.I = I
        self.L = np.sqrt((node1.u-node2.u)**2+(node1.v-node2.v)**2)
        if node2.u-node1.u != 0:
            self.angle = (node2.v-node1.v)/(node2.u-node1.u)
        else:
            self.angle = (np.pi/2)
        self.color = color

    def changeColor(self, color):
        self.color = color
