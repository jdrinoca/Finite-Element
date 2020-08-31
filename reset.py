
# If solved, returns the structure to an unsolved state.
# If unsolved, clears the plotter and deletes the structure

# Joseph Rudick
# Edited: 8/31/2020

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
        # Check for left click
        if button == "MouseButton.LEFT":

            # Return to editing mode if the structure is in a sovled state
            if(g.solved):
                g.bReset.label.set_text("Clear Structure")
                g.solved = False

                # Delete solution
                g.solvedNodes = []
                g.solvedX, g.solvedY, g.solvedColor = [], [], []

                g.solvedElements = []

                loops = len(g.solvedPlot)
                for i in range(0, loops):
                    g.solvedPlot.pop(0).remove()

                # Activate main buttons, clear the gain slider
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
                
            # Clear plotter and delete structure if not in solved mode
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

                
