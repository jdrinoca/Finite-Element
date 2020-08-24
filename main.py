
import globals as g
import nodeUI, elementUI, constraintUI, loadUI
import solver, saver, importer, reset, slider
import events

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
from matplotlib.widgets import Slider

import numpy as np

# main file
# responsible for plotter initialization and animation
# controls primary interface buttons

# Initialize the plot
fig = plt.figure()
mng = plt.get_current_fig_manager()
# Start zoomed
mng.window.state('zoomed')
# Plot background color
fig.patch.set_facecolor('slategray')

g.ax = fig.add_axes([0, 0, 1, 1], frameon=False, autoscale_on=False)
# Maintain aspect ratio
plt.axis('equal')
# Default plot limits, 16x9 aspect ratio
g.ax.set_xlim(-8,8)
g.ax.set_ylim(-4.5, 4.5)
fig.canvas.set_window_title('STRETCHY')

# draw origin
originSize = 0.075
plt.plot([-originSize,originSize],[0,0], c='k', linewidth = 1)
plt.plot([0,0],[-originSize,originSize], c='k', linewidth = 1)

# button coordinates
axSolve = plt.axes([0.02, 0.9, 0.08, 0.08])
axNode = plt.axes([0.02, 0.7, 0.08, 0.08])
axElement = plt.axes([0.02, 0.6, 0.08, 0.08])
axConstraint = plt.axes([0.02, 0.5, 0.08, 0.08])
axLoad = plt.axes([0.02, 0.4, 0.08, 0.08])

axSave = plt.axes([0.02, 0.2, 0.08, 0.08])
axImport = plt.axes([0.02, 0.1, 0.08, 0.08])

axReset = plt.axes([0.86, 0.1, 0.08, 0.08])
axGain = plt.axes([0.86, 0.2, 0.08, 0.08])

# interface buttons
g.bSolve = Button(axSolve, 'Solve', hovercolor="mediumspringgreen")
g.bSolve.on_clicked(solver.btn.interface)

g.bNode = Button(axNode, 'Add Node', hovercolor="mediumspringgreen")
g.bNode.on_clicked(nodeUI.btn.interface)

g.bElement = Button(axElement, 'Add Element', hovercolor="mediumspringgreen")
g.bElement.on_clicked(elementUI.btn.interface)

g.bConstraint = Button(axConstraint, 'Add constraint', hovercolor="mediumspringgreen")
g.bConstraint.on_clicked(constraintUI.btn.interface)

g.bLoad = Button(axLoad, 'Add Load', hovercolor="mediumspringgreen")
g.bLoad.on_clicked(loadUI.btn.interface)

g.bSave = Button(axSave, 'Save Structure', hovercolor="mediumspringgreen")
g.bSave.on_clicked(saver.btn.interface)

g.bImport = Button(axImport, 'Import Structure', hovercolor="mediumspringgreen")
g.bImport.on_clicked(importer.btn.interface)

g.bReset = Button(axReset, 'Clear Structure', hovercolor="mediumspringgreen")
g.bReset.on_clicked(reset.btn.interface)

g.sGain = Slider(axGain, 'Gain', valmin=1, valmax=10000, valinit=0)
g.sGain.on_changed(slider.btn.interface)
g.sGain.set_active(False)

# array of nodes
g.nodeScat = g.ax.scatter(g.nodeX, g.nodeY, s=75, c=g.nodeColor,\
            edgecolor=g.edgeColor, picker=events.nodePick, zorder=4)
# array of elements
g.elementsPlot = []
# array of constraints
g.constraintScat = g.ax.scatter(g.constraintX, g.constraintY, s=150, c=g.constraintColor,\
                edgecolor=g.edgeColor, marker=6, picker=events.constraintPick, zorder=0)
# arrays of loads, moments
g.forcesPlot = []
g.momentsPlot = []

#solved plots
g.solvedScat = g.ax.scatter(g.solvedX, g.solvedY, s=75, c=g.solvedColor,\
            edgecolor=g.edgeColor, zorder=6)
g.solvedPlot = []

# updates the plot
def anim(frame):
    g.zoom = 16/(g.ax.get_xlim()[1]-g.ax.get_xlim()[0])

    # update node position, color
    g.nodeScat.set_facecolors(g.nodeColor)
    g.nodeScat.set_offsets(np.transpose([g.nodeX, g.nodeY]))

    # solved node position, color
    g.solvedScat.set_facecolors(g.solvedColor)
    g.solvedScat.set_offsets(np.transpose([g.solvedX, g.solvedY]))


    # draw new elements
    while len(g.elementsPlot) < len(g.elements):
        index = len(g.elementsPlot)
        tempElem, = g.ax.plot([g.elements[index].node1.u, g.elements[index].node2.u], \
                            [g.elements[index].node1.v, g.elements[index].node2.v], \
                            c=g.elements[index].color, linewidth=2.5, picker=events.elementPick, zorder=1)

        g.elementsPlot.append(tempElem)

    # update elements position, color
    for i in range(0, len(g.elementsPlot)):
        g.elementsPlot[i].set_color(g.elements[i].color)

    #Parallel(n_jobs=2, verbose=10)(delayed(g.elementsPlot[i].set_color)(g.elements[i].color) for i in range(len(g.elementsPlot)))



    # draw solved elements
    while len(g.solvedPlot) < len(g.solvedElements):
        index = len(g.solvedPlot)
        tempElem, = g.ax.plot([g.solvedElements[index].node1.u, g.solvedElements[index].node2.u], \
                            [g.solvedElements[index].node1.v, g.solvedElements[index].node2.v], \
                            c=g.solvedElements[index].color, linewidth=2, zorder=5)

        g.solvedPlot.append(tempElem)

    # update solved element position, color
    for i in range(0, len(g.solvedPlot)):
        g.solvedPlot[i].set_xdata([g.solvedX[g.solvedNodes.index(g.solvedElements[i].node1)], \
                                    g.solvedX[g.solvedNodes.index(g.solvedElements[i].node2)]])
        g.solvedPlot[i].set_ydata([g.solvedY[g.solvedNodes.index(g.solvedElements[i].node1)], \
                                    g.solvedY[g.solvedNodes.index(g.solvedElements[i].node2)]])
        g.solvedPlot[i].set_color(g.solvedElements[i].color)


    # update constraint position, color
    g.constraintScat.set_facecolors(g.constraintColor)
    g.constraintScat.set_offsets(np.transpose([g.constraintX, g.constraintY]))


    # draw new forces
    while len(g.forcesPlot) < len(g.forces):
        index = len(g.forcesPlot)
        tempLoad = patches.FancyArrowPatch((g.forces[index].u1, g.forces[index].v1),\
                            (g.forces[index].u1+g.forces[index].dx*3, g.forces[index].v1+g.forces[index].dy*3),\
                            arrowstyle="Simple,tail_width=2,head_width=8,head_length=8",\
                            facecolor=g.forces[index].color, edgecolor=g.edgeColor, picker=events.forcePick, zorder=2)

        g.ax.add_patch(tempLoad)
        g.forcesPlot.append(tempLoad)

    # update forces position, color
    for i in range(0, len(g.forcesPlot)):
        g.forcesPlot[i].set_facecolor(g.forces[i].color)
        g.forcesPlot[i].set_positions((g.forces[i].u1, g.forces[i].v1),\
                            (g.forces[i].u1+g.forces[i].dx*3/g.zoom, \
                            g.forces[i].v1+g.forces[i].dy*3/g.zoom))
        
    # draw new moments
    while len(g.momentsPlot) < len(g.moments):
        index = len(g.momentsPlot)
        tempMoment = patches.FancyArrowPatch((g.moments[index].node.u, g.moments[index].node.v-.25),\
                            (g.moments[index].node.u, g.moments[index].node.v+.25),\
                            connectionstyle="arc3, rad=%f" % (0.75*np.sign(g.moments[index].vector)),\
                            arrowstyle="Simple,tail_width=2,head_width=8,head_length=8",\
                            facecolor=g.moments[index].color, edgecolor=g.edgeColor, picker=events.momentPick, zorder=3)

        g.ax.add_patch(tempMoment)
        g.momentsPlot.append(tempMoment)

    # update moment position, color
    for i in range(0, len(g.momentsPlot)):
        g.momentsPlot[i].set_facecolor(g.moments[i].color)
        g.momentsPlot[i].set_positions((g.moments[i].node.u, g.moments[i].node.v-.25/g.zoom),\
                            (g.moments[i].node.u, g.moments[i].node.v+.25/g.zoom))


#initialize animation loop
animation = FuncAnimation(fig, anim, interval=1, cache_frame_data=False)
# exit program when the plot is closed
fig.canvas.mpl_connect('close_event', events.close)
# zooms on scroll wheel
fig.canvas.mpl_connect('scroll_event', events.scrollEvent)
# pan on ctrl + left mouse
fig.canvas.mpl_connect('motion_notify_event', events.middleClick)

plt.show()
