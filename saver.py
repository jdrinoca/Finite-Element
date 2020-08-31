
# saves the current structure
# If solved, saves only the initial structure
# results are saved automatically

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
        # Check for left click
        if button == "MouseButton.LEFT":

            # Initialize file dialog interface
            root = tk.Tk()
            root.withdraw()
            
            filepath = filedialog.asksaveasfilename()
            # Do nothing if no file name is specified
            if filepath == "":
                return
            # Add '.html' extension if not already there
            if ".html" not in filepath:
                filepath += ".html"

            # Create the specified .html file and save the structure as a series of .html tables
            with open(filepath, "w") as html:

                df = []
                count = 0
                for i in g.nodes:
                    df.append([count, i.u, i.v])
                    count += 1
                df = pd.DataFrame(df, columns=["Node","x","y"])
                df = df.to_html(index=False)
                html.write(df)

                df = []
                count = 0
                for i in g.elements:
                    df.append([count, g.nodes.index(i.node1), g.nodes.index(i.node2), i.A, i.E, i.I])
                    count += 1
                df = pd.DataFrame(df, columns=["Element","node1","node2","A","E","I"])
                df = df.to_html(index=False)
                html.write(df)

                df = []
                count = 0
                for i in g.constraints:
                    df.append([count, g.nodes.index(i.node), i.x, i.y, i.theta])
                    count += 1
                df = pd.DataFrame(df, columns=["Constraint","node","x","y","r"])
                df = df.to_html(index=False)
                html.write(df)

                df = []
                count = 0
                for i in g.forces:
                    df.append([count, g.nodes.index(i.node), i.magnitude, i.angle])
                    count += 1
                df = pd.DataFrame(df, columns=["Force","node","magnitude","direction"])
                df = df.to_html(index=False)
                html.write(df)

                df = []
                count = 0
                for i in g.moments:
                    df.append([count, g.nodes.index(i.node), i.vector])
                    count += 1
                df = pd.DataFrame(df, columns=["Moment","node","magnitude"])
                df = df.to_html(index=False)
                html.write(df)


            
