
# controls the constraint UI

import globals as g
from constraint import constraint
from node import node

import numpy as np
import tkinter as tk
from tkinter import ttk

class btn(object):
    def interface(self):
        # deactivate main buttonsS
        button = str(self.__getattribute__("button"))
        if button == "MouseButton.LEFT":
            g.bSolve.set_active(False)
            g.bNode.set_active(False)
            g.bElement.set_active(False)
            g.bConstraint.set_active(False)
            g.bLoad.set_active(False)
            g.bSave.set_active(False)
            g.bImport.set_active(False)
            g.bReset.set_active(False)

            def createConstraint(indices, u, v, r):
                for i in indices:
                    g.constraints.append(constraint(g.nodes[i], u, v, r, 'y'))

                    g.constraintX.append(g.constraints[len(g.constraints)-1].node.u)
                    g.constraintY.append(g.constraints[len(g.constraints)-1].node.v)
                    g.constraintColor.append(g.constraints[len(g.constraints)-1].color)




            def getNodes():
                indices = []
                for i in g.nodes:
                    if i.color == 'c':
                        indices.append(g.nodes.index(i))
                if len(indices) == 0:
                    tk.messagebox.showerror(title="Node Error", message="Select at Leats 1 Node to Continue")
                else:
                    try:
                        u = uCon.get()
                        v = vCon.get()
                        r = rCon.get()
                        if not u and not v and not r:
                            pass
                        else:
                            createConstraint(indices, u, v, r)
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
            
            def uFlip():
                uCon.set(not uCon.get())
            
            def vFlip():
                vCon.set(not vCon.get())
            
            def rFlip():
                rCon.set(not rCon.get())


            deselectAll()
            root = tk.Tk()

            if g.solved:
                _quit()
            else:
                root.geometry('+200+100')
                root.title("Nodal Constraint Parameters")
                mainframe = ttk.Frame(root, padding="20 20 20 20")
                mainframe.grid(column=0, row=0)
                root.columnconfigure(0, weight=1)
                root.rowconfigure(0, weight=1)

                #ttk.Label(mainframe, text='Element Properties:').grid(column=1, row=1)
                ttk.Label(mainframe, text='Constrain Along:').grid(column=1, row=1, sticky = "w")

                uCon = tk.BooleanVar()
                uCon.set(False)
                vCon = tk.BooleanVar()
                vCon.set(False)
                rCon = tk.BooleanVar()
                rCon.set(False)

                x = tk.Checkbutton(mainframe, text='X Axis', command=uFlip)
                x.grid(column=1, row=2, sticky = "w")
                ttk.Label(mainframe, text='    ').grid(column=2, row=2)
                y = tk.Checkbutton(mainframe, text='Y Axis', command=vFlip)
                y.grid(column=3, row=2, sticky = "w")
                ttk.Label(mainframe, text='    ').grid(column=4, row=2)
                z = tk.Checkbutton(mainframe, text='Rotation', command=rFlip)
                z.grid(column=5, row=2, sticky = "w")

                ttk.Label(mainframe, text='    ').grid(column=1, row=3)

                ttk.Button(mainframe, text="Create Constraint", command=getNodes).grid(column=1, row=4)
                ttk.Label(mainframe, text='    ').grid(column=2, row=4)
                ttk.Button(mainframe, text="Clear Selection", command=deselectAll).grid(column=3, row=4)
                ttk.Label(mainframe, text='    ').grid(column=4, row=4)
                ttk.Button(mainframe, text="Cancel", command=_quit).grid(column=5, row=4)


                root.protocol("WM_DELETE_WINDOW", _quit)
                root.attributes("-topmost", True)
                root.mainloop()