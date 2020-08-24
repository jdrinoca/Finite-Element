
# controls the element UI

import globals as g
from element import element
from node import node

import numpy as np
import tkinter as tk
from tkinter import ttk

class btn(object):
    def interface(self):

        button = str(self.__getattribute__("button"))
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

            def createElement(indices, A, E, I):
                g.elements.append(element(g.nodes[indices[0]], g.nodes[indices[1]], A, E, I, 'k'))



            def getNodes():
                indices = []
                for i in g.nodes:
                    if i.color == 'c':
                        indices.append(g.nodes.index(i))
                if len(indices) < 2:
                    tk.messagebox.showerror(title="Node Error", message="Select 2 Nodes to Continue")
                elif len(indices) > 2:
                    tk.messagebox.showerror(title="Node Error", message="Select ONLY 2 Nodes to Continue")
                else:
                    for i in g.elements:
                        if (g.nodes[indices[0]]==i.node1 and g.nodes[indices[1]]==i.node2) or\
                            (g.nodes[indices[1]]==i.node1 and g.nodes[indices[0]]==i.node2):
                            tk.messagebox.showerror(title="Element Error", message="Element Already Exists")
                            return
                    try:
                        A = float(aEntry.get())
                        E = float(eEntry.get())
                        I = float(iEntry.get())
                        createElement(indices, A, E, I)
                    except ValueError:
                        pass

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


            deselectAll()
            root = tk.Tk()

            if g.solved:
                _quit()
            else:
                root.geometry('+200+100')
                root.title("Enter Element Properties")
                mainframe = ttk.Frame(root, padding="20 20 20 20")
                mainframe.grid(column=0, row=0)
                root.columnconfigure(0, weight=1)
                root.rowconfigure(0, weight=1)

                #ttk.Label(mainframe, text='Element Properties:').grid(column=1, row=1)
                ttk.Label(mainframe, text='A: ').grid(column=1, row=1, sticky = "e")
                aEntry = ttk.Entry(mainframe, width=15)
                aEntry.grid(column=2, row=1)
                ttk.Label(mainframe, text='    ').grid(column=3, row=1)

                ttk.Label(mainframe, text='E: ').grid(column=4, row=1, sticky = "e")
                eEntry = ttk.Entry(mainframe, width=15)
                eEntry.grid(column=5, row=1)
                ttk.Label(mainframe, text='    ').grid(column=6, row=1)

                ttk.Label(mainframe, text='I: ').grid(column=7, row=1)
                iEntry = ttk.Entry(mainframe, width=15)
                iEntry.grid(column=8, row=1)
                ttk.Label(mainframe, text='    ').grid(column=9, row=1)

                ttk.Button(mainframe, text="Create Element", command=getNodes).grid(column=10, row=1)
                ttk.Label(mainframe, text='    ').grid(column=11, row=1)
                ttk.Button(mainframe, text="Clear Selection", command=deselectAll).grid(column=12, row=1)
                ttk.Label(mainframe, text='    ').grid(column=13, row=1)
                ttk.Button(mainframe, text="Cancel", command=_quit).grid(column=14, row=1)


                root.protocol("WM_DELETE_WINDOW", _quit)
                root.attributes("-topmost", True)
                root.mainloop()