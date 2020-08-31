
# controls the load UI

# Joseph Rudick
# Edited: 8/31/2020

import globals as g
from force import force
from moment import moment
from node import node

import numpy as np
import tkinter as tk
from tkinter import ttk

class btn(object):
    def interface(self):
        button = str(self.__getattribute__("button"))
        # Check for left click
        if button == "MouseButton.LEFT":
            # deactivate main buttons
            g.bSolve.set_active(False)
            g.bNode.set_active(False)
            g.bElement.set_active(False)
            g.bConstraint.set_active(False)
            g.bLoad.set_active(False)
            g.bSave.set_active(False)
            g.bImport.set_active(False)
            g.bReset.set_active(False)

            # read values from the interface and create a point force
            def createPointLoad():
                indices = []
                for i in g.nodes:
                    # Check for selected nodes
                    if i.color == 'c':
                        indices.append(g.nodes.index(i))
                # If no nodes are selected, try again
                if len(indices) == 0:
                    tk.messagebox.showerror(title="Node Error", message="Select at Least 1 Node to Continue")
                else:
                    try:
                        # Read interface values and create a force
                        magnitude = float(magEntry.get())
                        angle = float(angleEntry.get()) * np.pi/180

                        for i in indices:
                            g.forces.append(force(g.nodes[i], magnitude, angle, 'darkred'))
                    except ValueError:
                        pass

            # read values from interface and create a distributed load on an element
            def createDistLoad():
                indices = []
                for i in g.elements:
                    # Check for selected elements
                    if i.color == 'c':
                        indices.append(g.elements.index(i))

                # If no elements are selected, try again
                if len(indices) == 0:
                    tk.messagebox.showerror(title="Element Error", message="Select at Least 1 Element to Continue")
                else:
                    try:
                        # read interface values and use them to create equivalent nodal forces (moment and force at each node)
                        for i in indices:

                            distMag = float(distMagEntry.get()) * g.elements[i].L/2
                            b = g.elements[i].node1.u - g.elements[i].node2.u
                            h = g.elements[i].node1.v - g.elements[i].node2.v
                            if b != 0:
                                distAngle = np.arctan(h/b) + np.pi/2
                            else:
                                distAngle = 0

                            g.forces.append(force(g.elements[i].node1, distMag, distAngle, 'darkred'))
                            g.forces.append(force(g.elements[i].node2, distMag, distAngle, 'darkred'))
                            
                            momentMag = float(distMagEntry.get()) * g.elements[i].L**2/12
                            g.moments.append(moment(g.elements[i].node1, 1*momentMag, 'darkred'))
                            g.moments.append(moment(g.elements[i].node2, -1*momentMag, 'darkred'))

                    except ValueError:
                        pass

            # Read values from interface and create a nodal moment (twisting; torque around the node)
            def createMoment():
                indices = []
                for i in g.nodes:
                    if i.color == 'c':
                        # check for selected nodes
                        indices.append(g.nodes.index(i))
                # If no nodes are selected, try again
                if len(indices) == 0:
                    tk.messagebox.showerror(title="Node Error", message="Select at Least 1 Node to Continue")
                else:
                    try:
                        # read interface values and use them to create a moment about each selected node
                        magnitude = float(momentMagEntry.get()) * direction.get()
                        for i in indices:
                            g.moments.append(moment(g.nodes[i], magnitude, 'darkred'))
                    except ValueError:
                        pass

            # Clear selection
            def deselectAll():
                for i in g.nodes:
                    i.changeColor(g.defaultNodeColor)
                for i in g.elements:
                    i.changeColor(g.defaultElementColor)
                for i in g.constraints:
                    i.changeColor(g.defaultConstraintColor)
                for i in g.forces:
                    i.changeColor(g.defaultForceColor)
                for i in g.moments:
                    i.changeColor(g.defaultMomentColor)

            # exit node UI, activate main buttons
            def _quit():

                g.bSolve.set_active(True)
                g.bNode.set_active(True)
                g.bElement.set_active(True)
                g.bConstraint.set_active(True)
                g.bLoad.set_active(True)
                g.bSave.set_active(True)
                g.bImport.set_active(True)
                g.bReset.set_active(True)


                deselectAll()
                root.destroy()

            # Initialize load creation interface
            deselectAll()
            root = tk.Tk()

            if g.solved:
                _quit()
            else:
                root.geometry('+200+100')
                root.title("Enter Load Parameters")
                mainframe = ttk.Frame(root, padding="20 20 20 20")
                mainframe.grid(column=0, row=0)
                root.columnconfigure(0, weight=1)
                root.rowconfigure(0, weight=1)

                ttk.Label(mainframe, text='Point Load', font='Helvetica 10 bold').grid(column=1, row=1)
                ttk.Label(mainframe, text='Magnitude: ').grid(column=1, row=2, sticky = "w")
                magEntry = ttk.Entry(mainframe, width=15)
                magEntry.grid(column=1, row=3)
                ttk.Label(mainframe, text='Direction (deg): ').grid(column=1, row=4, sticky = "w")
                angleEntry = ttk.Entry(mainframe, width=15)
                angleEntry.grid(column=1, row=5)
                ttk.Button(mainframe, text="Create Point Load", command=createPointLoad).grid(column=1, row=7, sticky='s')

                ttk.Label(mainframe, text='      ').grid(column=2, row=1, sticky = "w")
                ttk.Separator(mainframe, orient=tk.VERTICAL).place(x=115, y=0, relheight=1)

                ttk.Label(mainframe, text='Distributed Load', font='Helvetica 10 bold').grid(column=3, row=1)
                ttk.Label(mainframe, text='Magnitude: ').grid(column=3, row=2, sticky = "w")
                distMagEntry = ttk.Entry(mainframe, width=15)
                distMagEntry.grid(column=3, row=3, sticky = "w")
                ttk.Label(mainframe, text='Load Direction is\nNormal to Element').grid(column=3, row=4, sticky = "w")
                ttk.Label(mainframe, text='Converted to\nNodal Equivalents').grid(column=3, row=5, sticky = "w")
                ttk.Label(mainframe, text='    ').grid(column=3, row=6, sticky = "w")
                ttk.Button(mainframe, text="Create Distributed \n           Load", command=createDistLoad).grid(column=3, row=7, stick='s')

                ttk.Label(mainframe, text='      ').grid(column=4, row=1, sticky = "w")
                ttk.Separator(mainframe, orient=tk.VERTICAL).place(x=245, y=0, relheight=1)

                ttk.Label(mainframe, text='Moment', font='Helvetica 10 bold').grid(column=5, row=1)
                ttk.Label(mainframe, text='Magnitude: ').grid(column=5, row=2, sticky = "w")
                momentMagEntry = ttk.Entry(mainframe, width=15)
                momentMagEntry.grid(column=5, row=3, stick='w')
                direction = tk.IntVar(mainframe)
                direction.set(1)
                ttk.Label(mainframe, text='Direction: ').grid(column=5, row=4, sticky = "w")
                b1 = ttk.Radiobutton(mainframe, text='Counter-Clockwise', variable=direction, value=1)
                b1.grid(column=5, row=5, sticky = "w")
                b2 = ttk.Radiobutton(mainframe, text='Clockwise', variable=direction, value=-1)
                b2.grid(column=5, row=6, sticky = "w")
                ttk.Button(mainframe, text="Create Moment", command=createMoment).grid(column=5, row=7, sticky='s')
                
                ttk.Label(mainframe, text='    ').grid(column=6, row=1, sticky = "w")
                ttk.Button(mainframe, text="Clear Selection", command=deselectAll).grid(column=7, row=3, sticky='s')
                ttk.Button(mainframe, text="Cancel", command=_quit).grid(column=7, row=5, sticky='s')
                ttk.Separator(mainframe, orient=tk.VERTICAL).place(x=385, y=0, relheight=1)

                root.protocol("WM_DELETE_WINDOW", _quit)
                root.attributes("-topmost", True)
                root.mainloop()
