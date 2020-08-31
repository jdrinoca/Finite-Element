
# moment instance

# Joseph Rudick
# Edited: 8/31/2020

# node - connected node (node instance)
# vector - moment vector (float, can be negative or positive)
# color - moment color (matplotlib color string)

class moment:
    def __init__(self, node, vector, color):
        self.node = node
        self.vector = vector
        self.color = color

    def changeColor(self, color):
        self.color = color
