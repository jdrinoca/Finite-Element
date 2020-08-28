
# constraint instance

# Joseph Rudick
# Edited: 8/28/2020

# node - constrained node (node instance)
# x - constrained against X direction (boolean)
# y - constrained against Y direction (boolean)
# theta - constrained against rotation (boolean)
# color - constraint color (matplotlib color string)

import globals as g

class constraint:
    def __init__(self, node, x, y, theta, color):
        self.node = node
        self.x = x
        self.y = y
        self.theta = theta
        self.color = color

    def changeColor(self, color):
        g.constraintColor[g.constraints.index(self)] = color
        self.color = color
