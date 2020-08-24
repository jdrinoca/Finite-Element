
# node instance
#
# u - x-position (float)
# v - y-position (float)
# color - node color (matplotlib color string)

import globals as g

class node:
    def __init__(self, u, v, color):
        self.u = u
        self.v = v
        self.color = color
    
    def changeColor(self, color):
        g.nodeColor[g.nodes.index(self)] = color
        self.color = color