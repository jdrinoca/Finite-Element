
# solved node instance
#
# u - x-position (float)
# v - y-position (float)
# node - original node (node instance)
# color - node color (matplotlib color string)

import globals as g

class solvedNode:
    def __init__(self, u, v, node, color):
        self.u = u
        self.v = v
        self.color = color
        self.disp = [u-node.u, v-node.v]
    
    def changeColor(self, color):
        g.solvedColor[g.solvedNodes.index(self)] = color
        self.color = color
