
# solved element instance
#
# node1 - 1st connected node (solved node instance)
# node2 - 2nd connected node (solved node instance)
# stress - calculated elemental stress (float)
# color - element color (matplotlib color string)

class solvedElement:
    def __init__(self, node1, node2, stress, color):
        self.node1 = node1
        self.node2 = node2
        self.stress = stress
        self.color = color

    def changeColor(self, color):
        self.color = color