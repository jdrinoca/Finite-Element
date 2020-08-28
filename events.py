
# handles plot picker events

# Joseph Rudick
# Edited: 8/28/2020

import globals as g

import numpy as np
import sys

# If a node is left-clicked, change its color
# Delete if right-clicked
def nodePick(artist, event):
    if len(g.nodes) > 0 and not g.solved:
        x = event.xdata
        y = event.ydata

        maxD = 0.075/g.zoom     # node 'hitbox', changes relative to zoom value
        d = []      # distances from cursor to node array
        for node in g.nodes:
            d.append(np.sqrt((x-node.u)**2+(y-node.v)**2))
        index = d.index(np.min(d))

        if d[index] < maxD:
            if event.button == 1:   # Change color of closest node if it's within allowable distance
                if g.nodes[index].color == g.defaultNodeColor:
                    g.nodes[index].changeColor(g.selectedColor)
                else:
                    g.nodes[index].changeColor(g.defaultNodeColor)
            elif event.button == 3:     # delete node if right-clicked
                del g.nodes[index], g.nodeX[index], g.nodeY[index], g.nodeColor[index]

    return(False, dict())

# If an element is left-clicked, change its color
# Delete if right-clicked
def elementPick(artist, event):
    if len(g.elements) > 0 and not g.solved:
        x = event.xdata
        y = event.ydata
        xLine = artist.get_xdata()
        yLine = artist.get_ydata()

        maxD = 0.005/g.zoom     # element 'hitbox', changes relative to zoom value
        dArr = np.sqrt((xLine - x)**2 + (yLine - y)**2)
        d = np.sum(dArr)

        index = g.elementsPlot.index(artist)

        if d < np.sqrt((xLine[1]-xLine[0])**2 + (yLine[1]-yLine[0])**2) + maxD:
            if event.button == 1:   # Change color if left-clicked
                if g.elements[index].color == g.defaultElementColor:
                    g.elements[index].changeColor(g.selectedColor)
                else:
                    g.elements[index].changeColor(g.defaultElementColor)
        
            elif event.button == 3:     # Delete if right-clicked
                del g.elements[index], g.elementsPlot[index]
                artist.remove()

    return(False, dict())

# If a constraint is left-clicked, change its color
# Delete if right-clicked
def constraintPick(artist, event):
    if len(g.constraints) > 0 and not g.solved:
        x = event.xdata
        y = event.ydata

        maxD = 0.075/g.zoom     # constraint 'hitbox', changes relative to zoom value
        d = []
        for constraint in g.constraints:
            d.append(np.sqrt((x-constraint.node.u)**2+(y-constraint.node.v+0.075/g.zoom)**2))
        index = d.index(np.min(d))

        if d[index] < maxD:
            if event.button == 1:   # Change color if left-clicked
                if g.constraints[index].color == g.defaultConstraintColor:
                    g.constraints[index].changeColor(g.selectedColor)
                else:
                    g.constraints[index].changeColor(g.defaultConstraintColor)
            elif event.button == 3:     # Delete if right-clicked
                del g.constraints[index], g.constraintX[index], g.constraintY[index], g.constraintColor[index]

    return(False, dict())

# If a force is left-clicked, change its color
# Delete if right-clicked
def forcePick(artist, event):

    if len(g.forces) > 0 and not g.solved:
        x = event.xdata
        y = event.ydata
        coords = artist.get_path()

        index = g.forcesPlot.index(artist)
        if coords.contains_point([x, y], radius=0):     # Check if cursor coordinates are on the force
            if event.button == 1:   # Change color if left-clicked
                if g.forces[index].color == g.defaultForceColor:
                    g.forces[index].changeColor(g.selectedColor)
                else:
                    g.forces[index].changeColor(g.defaultForceColor)
            elif event.button == 3:     # Delete if right-clicked
                del g.forces[index], g.forcesPlot[index]
                artist.remove()

    return(False, dict())

# If a moment is left-clicked, change its color
# Delete if right-clicked
def momentPick(artist, event):

    if len(g.moments) > 0 and not g.solved:
        x = event.xdata
        y = event.ydata
        coords = artist.get_path()

        index = g.momentsPlot.index(artist)
        if coords.contains_point([x, y], radius=0):     # Check if cursor coordinates are on the moment
            if event.button == 1:   # Change color if left-clicked
                if g.moments[index].color == g.defaultMomentColor:
                    g.moments[index].changeColor(g.selectedColor)
                else:
                    g.moments[index].changeColor(g.defaultMomentColor)
            elif event.button == 3:     # Delete if right-clicked
                del g.moments[index], g.momentsPlot[index]
                artist.remove()

    return(False, dict())

# zooms in or out at scroll wheel input
def scrollEvent(event):
    xLim = g.ax.get_xlim()
    yLim = g.ax.get_ylim()
    # mouse location
    x = event.xdata
    y = event.ydata
    # zoom factor
    factor = 1.15

    # zoom in
    if event.button == "down":
        g.ax.set_xlim((xLim[0]-x)/factor+x ,(xLim[1]-x)/factor+x)
        g.ax.set_ylim((yLim[0]-y)/factor+y ,(yLim[1]-y)/factor+y)
    # zoom out
    elif event.button == "up":
        g.ax.set_xlim((xLim[0]-x)*factor+x ,(xLim[1]-x)*factor+x)
        g.ax.set_ylim((yLim[0]-y)*factor+y ,(yLim[1]-y)*factor+y)

# pans on middle mouse click
def middleClick(event):
    # cursor coordinates
    x = event.xdata
    y = event.ydata
    # check for middle mouse click and make sure cursor is inside g.ax
    if event.button == 2 and event.inaxes == g.ax:
        xLim = g.ax.get_xlim()
        yLim = g.ax.get_ylim()

        g.ax.set_xlim(xLim[0]-x+g.coords[0], xLim[1]-x+g.coords[0])
        g.ax.set_ylim(yLim[0]-y+g.coords[1], yLim[1]-y+g.coords[1])
    else:
        # store cursor coordinates when not panning
        g.coords = [x,y]




# close all open windows if main window is closed
def close(event):
    sys.exit()
