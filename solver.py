
# solves for nodal displacement and elemental stress
# puts plotter in post-processing mode

# Joseph Rudick
# Edited: 8/31/2020

import globals as g
from node import node
from element import element
from constraint import constraint
from force import force
from moment import moment

from solvedNode import solvedNode
from solvedElement import solvedElement

import tkinter as tk
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class btn(object):
    def interface(self):
        button = str(self.__getattribute__("button"))
        if button == "MouseButton.LEFT":
            try:
                # make sure structure containts at least one of each element, constraint, and load
                if len(g.elements)==0 or len(g.constraints)==0 or (len(g.forces)==0 and len(g.moments)==0):
                    tk.messagebox.showerror(title="Structure Error", message="Solving requires at least one element, constraint, and load")
                    return

                # check for elements without a node
                nodeList = []
                for i in g.elements:
                    if i.node1 in g.nodes and i.node2 in g.nodes:
                        if i.node1 not in nodeList: nodeList.append(i.node1)
                        if i.node2 not in nodeList: nodeList.append(i.node2)
                    else:
                        tk.messagebox.showerror(title="Element Error", message="At least 1 element is missing a node")
                        return
                
                # check for nodes not connected to elements
                for i in g.nodes:
                    if i not in nodeList:
                        tk.messagebox.showerror(title="Node Error", message="At least 1 node is not connected to an element")
                        return

                # check for constraints without a node
                for i in g.constraints:
                    if i.node not in nodeList:
                        tk.messagebox.showerror(title="Constraint Error", message="At least 1 constraint is missing a node")
                        return

                # check for loads without a node
                for i in g.forces:
                    if i.node not in nodeList:
                        tk.messagebox.showerror(title="Force Error", message="At least 1 force is missing a node")
                        return
                for i in g.moments:
                    if i.node not in nodeList:
                        tk.messagebox.showerror(title="Moment Error", message="At least 1 moment is missing a node")
                        return

                # compute global stiffness matrix
                K = np.float64(np.matrix([[0 for i in range(len(g.nodes)*3)] for j in range(len(g.nodes)*3)]))

                # Add local stiffness matrix of each element to the global stiffness matrix
                for elem in g.elements:
                    L = elem.L
                    coef = elem.E/L
                    A = elem.A
                    I = elem.I
                    S = (elem.node2.v-elem.node1.v)/L
                    C = (elem.node2.u-elem.node1.u)/L
                    n1 = g.nodes.index(elem.node1)*3
                    n2 = g.nodes.index(elem.node2)*3

                    K[n1,n1] += coef*(A*C**2+12*I*S**2/L**2)
                    K[n1,n1+1] += coef*(C*S*(A-12*I/L**2))
                    K[n1,n1+2] += coef*(-6*S*I/L)
                    K[n1,n2] += coef*(-1*(A*C**2+12*I*S**2/L**2))
                    K[n1,n2+1] += coef*(-1*C*S*(A-12*I/L**2))
                    K[n1,n2+2] += coef*(-6*I*S/L)

                    K[n1+1,n1] += coef*(C*S*(A-12*I/L**2))
                    K[n1+1,n1+1] += coef*(A*S**2+12*I*C**2/L**2)
                    K[n1+1,n1+2] += coef*(6*I*C/L)
                    K[n1+1,n2] += coef*(-1*C*S*(A-12*I/L**2))
                    K[n1+1,n2+1] += coef*(-1*(A*S**2+12*I*C**2/L**2))
                    K[n1+1,n2+2] += coef*(6*I*C/L)

                    K[n1+2,n1] += coef*(-6*S*I/L)
                    K[n1+2,n1+1] += coef*(6*I*C/L)
                    K[n1+2,n1+2] += coef*(4*I)
                    K[n1+2,n2] += coef*(6*I*S/L)
                    K[n1+2,n2+1] += coef*(-6*I*C/L)
                    K[n1+2,n2+2] += coef*(2*I)

                    K[n2,n1] += coef*(-1*(A*C**2+12*I*S**2/L**2))
                    K[n2,n1+1] += coef*(-1*C*S*(A-12*I/L**2))
                    K[n2,n1+2] += coef*(6*I*S/L)
                    K[n2,n2] += coef*(A*C**2+12*I*S**2/L**2)
                    K[n2,n2+1] += coef*(C*S*(A-12*I/L**2))
                    K[n2,n2+2] += coef*(6*I*S/L)

                    K[n2+1,n1] += coef*(-1*C*S*(A-12*I/L**2))
                    K[n2+1,n1+1] += coef*(-1*(A*S**2+12*I*C**2/L**2))
                    K[n2+1,n1+2] += coef*(-6*I*C/L)
                    K[n2+1,n2] += coef*(C*S*(A-12*I/L**2))
                    K[n2+1,n2+1] += coef*(A*S**2+12*I*C**2/L**2)
                    K[n2+1,n2+2] += coef*(-6*I*C/L)

                    K[n2+2,n1] += coef*(-6*I*S/L)
                    K[n2+2,n1+1] += coef*(6*I*C/L)
                    K[n2+2,n1+2] += coef*(2*I)
                    K[n2+2,n2] += coef*(6*I*S/L)
                    K[n2+2,n2+1] += coef*(-6*I*C/L)
                    K[n2+2,n2+2] += coef*(4*I)


                # create initial global displacement vector
                d = np.transpose(np.float64(np.matrix([1 for i in range(len(g.nodes)*3)])))
                    
                for constraint in g.constraints:
                    n = g.nodes.index(constraint.node)*3
                    if constraint.x:
                        d[n] = 0
                    if constraint.y:
                        d[n+1] = 0
                    if constraint.theta:
                        d[n+2] = 0
                    

                # create global force vector
                F = np.transpose(np.float64(np.matrix([0 for i in range(len(g.nodes)*3)])))

                for force in g.forces:
                    n = g.nodes.index(force.node)*3
                    F[n] = force.magnitude*np.cos(force.angle)
                    F[n+1] = force.magnitude*np.sin(force.angle)
                for moment in g.moments:
                    n = g.nodes.index(moment.node)*3
                    F[n+2] = moment.vector

                    
                # solve for global displacement
                ind = 0
                for i in K:
                    if d[ind] == 0:
                        K[ind] = K[ind]*0
                        K[ind,ind] = 1
                        F[ind] = 0
                    ind += 1

                d = np.linalg.solve(K,F)
                g.displacement = d

                # Solve for elemental stress
                stress = []
                for i in g.elements:
                    elementAngle = [-1*np.cos(i.angle), -1*np.sin(i.angle), np.cos(i.angle), np.sin(i.angle)]
                    elementDisp = np.transpose([np.float(d[g.nodes.index(i.node1)*3]), np.float(d[g.nodes.index(i.node1)*3+1]), \
                                                np.float(d[g.nodes.index(i.node2)*3]), np.float(d[g.nodes.index(i.node2)*3])])
                    stress.append(i.E/i.L*np.dot(elementAngle, elementDisp))

                # Convert displacement vector to absolute displacements for each node
                disp = []
                for i in range(0, np.int(len(d)/3)):
                    disp.append(np.float(np.sqrt(d[i*3]**2+d[i*3+1]**2)))

                # Create and normalize a colormap for displacement and stress
                normalizedDisp = mpl.colors.Normalize(vmin=np.min(disp), vmax=np.max(disp))
                normalizedStress = mpl.colors.Normalize(vmin=np.min(stress), vmax=np.max(stress))
                cmap = mpl.pyplot.get_cmap(g.colormap)

                # Create the colormap legends
                g.axBarDisp = plt.axes([0.90, 0.4, 0.04, 0.5])
                g.sBarDisp = mpl.colorbar.ColorbarBase(g.axBarDisp, orientation='vertical', cmap=cmap, norm=normalizedDisp)
                g.axBarDisp.yaxis.set_ticks_position('right')
                g.axBarDisp.set_ylabel("Displacement")
                g.axBarDisp.yaxis.set_label_position('right')
                g.axBarStress = plt.axes([0.86, 0.4, 0.04, 0.5])
                g.sBarStress = mpl.colorbar.ColorbarBase(g.axBarStress, orientation='vertical', cmap=cmap, norm=normalizedStress)
                g.axBarStress.yaxis.set_ticks_position('left')
                g.axBarStress.set_ylabel("Stress")
                g.axBarStress.yaxis.set_label_position('left')


                # Create the solved structure with scaled displacements
                # Node colors correspond to total nodal displacements
                # Element colors correspond to elemental stress
                nodeInd = 0
                for i in g.nodes:
                    g.solvedNodes.append(solvedNode(i.u+np.float(d[nodeInd*3]), i.v+np.float(d[nodeInd*3+1]), \
                                            i, cmap(normalizedDisp(disp[nodeInd]))))
                    g.solvedX.append(g.solvedNodes[len(g.solvedNodes)-1].u)
                    g.solvedY.append(g.solvedNodes[len(g.solvedNodes)-1].v)
                    g.solvedColor.append(g.solvedNodes[len(g.solvedNodes)-1].color)


                    nodeInd += 1

                elementInd = 0
                for i in g.elements:
                    g.solvedElements.append(solvedElement(g.solvedNodes[g.nodes.index(i.node1)], \
                        g.solvedNodes[g.nodes.index(i.node2)], 1, cmap(normalizedStress(stress[elementInd]))))

                    elementInd += 1


                g.solved = True

                # De-activate main buttons
                g.bSolve.set_active(False)
                g.bNode.set_active(False)
                g.bElement.set_active(False)
                g.bConstraint.set_active(False)
                g.bLoad.set_active(False)
                g.bSave.set_active(False)
                g.bImport.set_active(False)

                g.sGain.set_active(True)
                g.sGain.set_val(1)

                g.bReset.label.set_text("Reset Solution")

                g.nodeScat.set_alpha(0.2)
                for i in g.elementsPlot:
                    i.set_alpha(0.2)
                g.constraintScat.set_alpha(0.2)
                for i in g.forcesPlot:
                    i.set_alpha(0.2)
                for i in g.momentsPlot:
                    i.set_alpha(0.2)

                                
            # If an error is thrown, abort solution process and send an error box
            except Exception as e:
                tk.messagebox.showerror(title="Solver Error", message="Something went wrong :(\nCheck your initial conditions")

