
# force instance

# Joseph Rudick
# Edited: 8/28/2020

# node - connected node (node instance)
# magnitude - magnitude of the force (float)
# angle - force vector direction from positive X (float)
# color - force color (matplotlib color string)

import numpy as np

class force:
    def __init__(self, node, magnitude, angle, color):
        self.node = node
        self.magnitude = magnitude
        self.angle = angle
        self.color = color
        self.u1 = node.u
        self.v1 = node.v
        self.dx = np.sign(magnitude) * np.cos(angle) * 0.25
        self.dy = np.sign(magnitude) * np.sin(angle) * 0.25

    def changeColor(self, color):
        self.color = color
