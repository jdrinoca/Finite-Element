# Finite-Element
A 2-D finite element solver and interface.

By Joseph Rudick

Uploaded on 8/24/2020

---

### Table of Contents
1. [Introduction](#Introduction)
2. [Download and Install](#download-and-install)
3. [User's Guide](#users-guide)
4. [Why?](#why)
5. [What's Next?](#whats-next)
6. [Final Thoughts](#final-thoughts)

---

### Introduction
Welcome!

This is the repository for a program that I developed as a summer project for 2020.  The program is a 2-D finite element solver written entirely in Python 3.  Think West Point Bridge Designer, but more versatile and less polished.  It employs the [finite element method](https://en.wikipedia.org/wiki/Finite_element_method) to calculate the stress and strain for a user-created 2-dimensional structure.  The program was designed for quick engineering analysis where the structure can be approximated as a 2-D frame.

---

### Download and Install
To view the source code, just open the file here in Github.  If you'd like to download the repository, visit the main repository page and click the green "Code" button above the list of files.  This gives the option to download the master branch as a ZIP.  Once that gets downloaded and unpacked, you now have access to the source code, as well as an executable of the latest version.

To launch the executable, navigate to where the directory was unpacked, and go to the "dist" folder.  From there, click on finite-element and scroll to or search for the file named "stretchy.exe".  This is the executable that allows the program to run without access to Python or the required packages.  Double-click to launch (this may take a while) and have fun!

NOTE:  If you're running either a macOS or a Linux distro, chances are the .exe won't work.  In that case, you have to run from the source code.  Make sure that all the .py files are in the same directory, and run main.py to start.

If you choose to run from the source code, the following packages are required:

* [Matplotlib](https://matplotlib.org/#)
* [NumPy](https://numpy.org/)
* [TkInter](https://docs.python.org/3/library/tkinter.html)
* [pandas](https://pandas.pydata.org/)

---

### User's Guide
#### Background
This program solves for the displacement and stress of frame elements using equations found in chapters 3 and 5 of "A First Course in the Finite Element Method" by Daryl L. Logan.

The displacement calculations account for plane strain in the elements, and require the element materials [modulus of elasticity](https://en.wikipedia.org/wiki/Elastic_modulus) (E) as well as cross sectional area (A) of the element, and its [area moment of inertia](https://en.wikipedia.org/wiki/List_of_second_moments_of_area) (I).

Stress calculations *do not* account for plane stress, and simply rely on [Hooke's Law](https://en.wikipedia.org/wiki/Hooke's_law).

#### Navigation
All navigation is done through the mouse.  Scrolling the mouse wheel will zoom in and out, and holding and dragging middle-mouse will pan the display to where you want.

To select an object, left click on it in the plotter window.  This will highlight it to indicate that it is selected.  Left click the object again to de-select.

#### Creating a Structure
Structures are started with nodes, which can be considered the joints or connections of a frame.  To create a node field, click the "Add Node" button and specify the cartesian coordinates for the node you'd like to place.  Click "Create Node" and repeat with new coordinates, or click "Cancel" to exit the node creation interface.  Nodes will serve as the backbone of the structure; They rigidly connect frame elements, and accept initial conditions.

With the node field in place, everything else can be added to the structure.  To create frame elements, select 2 nodes (ONLY 2, no more, no less) and enter the desired member properties.

  * A - Area cross-section of the member
  * E - Member material modulus of elasticity
  * I - Area moment of inertia of the member
  
Click "Create Element" to create the element.  To create another element, select the desired 2 nodes and enter the element properties.  Click "Cancel" to exit the element creation interface.

Constraints are part of the initial conditions required to create a solveable structure.  They either fix a node in place, or reduce its degrees of freedom.  To constrain a node, click the button "Add Constraint" and select the nodes you'd like to constrain.  To fully fix a node (prevent it from moving in the X and Y direction, and stop rotation), check all 3 boxes in the menu.  The check boxes are how the degrees of freedom are controlled.  Click on "create Constraint" and either repeat with different nodes, or click "Cancel" to exit the constraint creation interface.

The other initial conditions are the loads that the structure experiences.  If there's no loading, there's nothing to solve.  In this program, loads are divided into 3 categories.

  * **Point Loads:** Forces that act on nodes.  To create a point load, select a node, specify the desired magnitude and direction of the load, and click "Create Point Load". (ex. 4000, 90 deg will create a 4000 unit force pulling directly up on the node)
  * **Moment Loads:** Torques that act on nodes.  To create a moment, select a node, specify a magnitude and direction (clockwise/counter-clockwise), and click "Create Moment".
  * **Distributed Loads:** USE AT YOUR OWN RISK.  The distributed load function is kind of buggy, so avoid if possible.  I'm currently trying to find a better way to do it, but I didn't want to bother to re-do the TkInter interface.  It will work for some applications, so feel free to try it.  If you notice somehting off about your solution, retry but approximate the distributed load as point loads and moments.  That's what the program is suppossed to do, anyways.

#### Solving
With a completed structure, you're free to solve.  Click the "Solve" button in the top left, and you'll see a few things change.  First, the original structure is translucent, and a new deformed structure is visible.  Nodes are now colormapped to their absolute displacement, and elements are colormapped to their stress values.  The colormap is visible to the right, and provides some context values for the colormapping.  In both cases, red indicates the maximum value, and pink the minimum.

In a lot of cases, the displacement is imperceptible relative to the size of the structure.  For this reason, I have included a "Gain" slider in the bottom right, above the "Reset Solution" button.  In solved mode, the Gain slider can be moved to magnify the displacement of each node.  This allows for better qualitative analysis.  The slider maxes out at 10,000x.

To exit solved mode and return to the structure editor, simply click the "Reset Solution" button in the bottom right.

#### Saving and Importing
Structures are saved as .html documents, which store lists of objects and their properties.  To save, simply click the "Save Structure" button in the bottom left, and navigate to the desired directory.  Similary, a structure can be imported by clicking on the "Import Structure" button.  From there, the file can be opened and imported into the program.

I have included a few different sample structures, located in the folder "Sample Structures".  You can import those to play around with some pre-made structures and to get used to the interface.

---

### Why?
Good question.

I was taking a course in the finite element method right around the same time that I had finally gotten Python working on my desktop, so I decided to combine the two and test my ability to ~~google~~ program.  The script was only intended to be text-based and contained to a single Python file, but I was playing around with the Matplotlib animation function and next thing I know, it's 3am and I'm trying to programatically pan a Matplotlib plot using the mouse.

---

### What's Next?
This is still a work-in-progress.

One (major) part that needs updating is the stress calculations for each element.  The stress values are dependant on their order of creation, and a lot of the sometimes do not reflect the actual stresses in the element.  The nodal displacements, however, seem to be correct.

Another big feature I'm missing is a way to save simulation results.  Right now, the only way to analyze the structure is to look at the pretty colors and compare them to the colormap on the right to estimate stress/displacement.  Ideally, I'd like to save the results as a .pdf that would include a screenshot of the full structure (deformed and undeformed) with node and element numbers displayed above each object, and a chart of nodes/element numbers and ther respective displacement/stress.  Once I get the stress calculations dialed in, this is my next step.

I also need to go through each file and finish commenting.  I was pretty good about doing that as I went, but some files (solver, for instance) had so many iterations that I decided to do that when I finished messing with that file (ad infinitum).

This program runs okay(ish).  The more nodes/elements/forces etc. the worse it runs, and it drops off *quickly*.  I dove a little bit into multi-threading the animation loop, since that's the limiting factor for framerate, but I'm not able to swing it yet.  I wanted to get this thing onto Github by the end of August, and I was running out of time (it's 8/24/2020 as I type this).  Multi-threading and other types of code optimization are on my radar, but don't hold your breath.

---

### Final Thoughts
WHY did I use Matplotlib as the animation platform?!  Don't get me wrong, the Matplotlib animation function is great, and I'm sure someone who's a better programmer than I would be able to eek out more performance.  If they were smart, they'd probably use something different in the first place.  Pygame, for instance, would have been a better choice.  Even skipping over Python entirely and going straight to something like Unity would have helped.  That way, I could even do something in 3-D.  Oh well, live and learn.  At least now I'm *really* familiar with the Matplotlib documentation.

The entire goal of this project was to learn by throwing myself off the deep end, and I believe I did just that.  In my opinion, knowing what *not* to do is just as valuable (if not moreso) than knowing what to do from the very beginning.  I'm not a software engineer by any stretch of the imagination, and I have a lot that I can do to improve (best practices, PEP 8, etc.).  That's not to say that this project was a failure; in fact, I'm very proud of what I was able to accomplish over the long weekend nights spent making this thing.

Anyway, if you're still reading, I hope you find this project as cool as I have :)
