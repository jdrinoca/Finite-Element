
# controls the node UI

# Joseph Rudick
# Edited: 8/31/2020

import globals as g
from node import node

import numpy as np
import tkinter as tk
from tkinter import ttk

class btn(object):
    def interface(self):
        button = str(self.__getattribute__("button"))
        # Check for left-click
        if button == "MouseButton.LEFT":
            
            # Read specified X-Y coordinates and create a node if it's unique
            def createNode():
                try:
                    # get X, Y
                    xVal = float(uEntry.get())
                    yVal = float(vEntry.get())

                    # Check if a node already occupies the specified coordinates
                    nodeExists = False
                    for i in g.nodes:
                        if i.u == xVal and i.v == yVal:
                            nodeExists = True
                            tk.messagebox.showerror(title="Node Error", message="Node Already Exists")
                        else:
                            nodeExists = False

                    # Create a node at X, Y
                    if not nodeExists:
                        g.nodes.append(node(xVal, yVal, 'b'))
                        g.nodeX.append(g.nodes[len(g.nodes)-1].u)
                        g.nodeY.append(g.nodes[len(g.nodes)-1].v)
                        g.nodeColor.append(g.nodes[len(g.nodes)-1].color)

                # if nothing is passed in, skip
                except ValueError:
                    pass


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

                root.destroy()

            # deactivate main buttons
            g.bSolve.set_active(False)
            g.bNode.set_active(False)
            g.bElement.set_active(False)
            g.bConstraint.set_active(False)
            g.bLoad.set_active(False)
            g.bSave.set_active(False)
            g.bImport.set_active(False)
            g.bReset.set_active(False)

            # UI layout
            root = tk.Tk()

            if g.solved:
                _quit()
            else:
                root.geometry('+200+100')
                root.title("Enter Node Coordinates")
                mainframe = ttk.Frame(root, padding="20 20 20 20")
                mainframe.grid(column=0, row=0)
                root.columnconfigure(0, weight=1)
                root.rowconfigure(0, weight=1)

                ttk.Label(mainframe, text='X: ').grid(column=1, row=1)
                uEntry = ttk.Entry(mainframe, width=12)
                uEntry.grid(column=2, row=1)
                ttk.Label(mainframe, text='    ').grid(column=3, row=1)

                ttk.Label(mainframe, text='Y: ').grid(column=4, row=1)
                vEntry = ttk.Entry(mainframe, width=12)
                vEntry.grid(column=5, row=1)
                ttk.Label(mainframe, text='    ').grid(column=6, row=1)

                ttk.Button(mainframe, text="Create Node", command=createNode).grid(column=7, row=1)
                ttk.Label(mainframe, text='  ').grid(column=8, row=1)
                ttk.Button(mainframe, text="Cancel", command=_quit).grid(column=9, row=1)

                root.protocol("WM_DELETE_WINDOW", _quit)
                root.attributes("-topmost", True)
                root.mainloop()
