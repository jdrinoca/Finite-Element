
# imports a previously-saved structure
# clears the plotter first, so save your work!

# Joseph Rudick
# Edited: 8/31/2020

import globals as g
from node import node
from element import element
from constraint import constraint
from force import force
from moment import moment

import tkinter as tk
from tkinter import filedialog
import pandas as pd

class btn(object):
    def interface(self):
        button = str(self.__getattribute__("button"))
        # check for left click
        if button == "MouseButton.LEFT":

            # Initialize file dialogue interface
            root = tk.Tk()
            root.withdraw()
            
            filepath = filedialog.askopenfilename()
            if filepath == "":
                return
            try:

                # convert file contents to a dataframe
                dfs = pd.read_html(filepath)

                # Clear existing structure
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

                    
                # Loop through the dataframe and create the structure
                table = 0
                for i in dfs:
                    if table == 0:
                        for j in i.values:
                            g.nodes.append(node(j[1], j[2], 'b'))
                            g.nodeX.append(g.nodes[len(g.nodes)-1].u)
                            g.nodeY.append(g.nodes[len(g.nodes)-1].v)
                            g.nodeColor.append(g.nodes[len(g.nodes)-1].color)
                    elif table == 1:
                        for j in i.values:
                            g.elements.append(element(g.nodes[int(j[1])], g.nodes[int(j[2])], j[3], j[4], j[5], 'k'))
                    elif table == 2:
                        for j in i.values:
                            g.constraints.append(constraint(g.nodes[int(j[1])], bool(j[2]), bool(j[3]), bool(j[4]), 'y'))
                            g.constraintX.append(g.constraints[len(g.constraints)-1].node.u)
                            g.constraintY.append(g.constraints[len(g.constraints)-1].node.v)
                            g.constraintColor.append(g.constraints[len(g.constraints)-1].color)
                    elif table == 3:
                        for j in i.values:
                            g.forces.append(force(g.nodes[int(j[1])], j[2], j[3], 'darkred'))
                    elif table == 4:
                        for j in i.values:
                            g.moments.append(moment(g.nodes[int(j[1])], j[2], 'darkred'))
                    table += 1
            except ValueError:  # If the file chosen is not .html or has invalid contents
                tk.messagebox.showerror(title="File Error", message="Invalid Structure File")

            # Clear the dataframe
            dfs = 0


