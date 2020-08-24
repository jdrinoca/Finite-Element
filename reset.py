
import globals as g
import events
from node import node
from element import element
from constraint import constraint
from force import force
from moment import moment

class btn(object):
    def interface(self):
        button = str(self.__getattribute__("button"))
        if button == "MouseButton.LEFT":

            if(g.solved):
                g.bReset.label.set_text("Clear Structure")
                g.solved = False

                g.solvedNodes = []
                g.solvedX, g.solvedY, g.solvedColor = [], [], []

                g.solvedElements = []

                loops = len(g.solvedPlot)
                for i in range(0, loops):
                    g.solvedPlot.pop(0).remove()

                g.bSolve.set_active(True)
                g.bNode.set_active(True)
                g.bElement.set_active(True)
                g.bConstraint.set_active(True)
                g.bLoad.set_active(True)
                g.bSave.set_active(True)
                g.bImport.set_active(True)

                g.sGain.set_active(False)

                g.sBarDisp.remove()
                g.axBarDisp = None
                g.sBarStress.remove()
                g.axBarStress = None

                g.nodeScat.set_alpha(1)
                for i in g.elementsPlot:
                    i.set_alpha(1)
                g.constraintScat.set_alpha(1)
                for i in g.forcesPlot:
                    i.set_alpha(1)
                for i in g.momentsPlot:
                    i.set_alpha(1)
                
            else:
                g.bReset.label.set_text("Clear Structure")

                g.nodes = []
                g.nodeX, g.nodeY, g.nodeColor = [], [], []

                g.elements = []
                loops = len(g.elementsPlot)
                for i in range(0, loops):
                    g.elementsPlot.pop(0).remove()

                g.constraints = []
                g.constraintX, g.constraintY, g.constraintColor = [], [], []

                g.forces = []
                loops = len(g.forcesPlot)
                for i in range(0, loops):
                    g.forcesPlot.pop(0).remove()

                g.moments = []
                loops = len(g.momentsPlot)
                for i in range(0, loops):
                    g.momentsPlot.pop(0).remove()

                
