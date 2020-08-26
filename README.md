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

This is the repository for a program that I developed as a summer project for 2020.  The program is a 2-D finite element solver written entirely in Python 3.  Think West Point Bridge Designer, but more versatile and less polished.  It employs the [finite element method](https://en.wikipedia.org/wiki/Finite_element_method) to calculate the stress and strain for a user-created 2-dimensional structure.  The program was designed for quick engineering analysis where the structure can be approximated as a frame.

---

### Download and Install
To view the source code, just open the file in Github.  If you'd like to download the repository, visit the main repository page and click the green "Code" button above the list of files.  This gives the option to download the master branch as a ZIP.  Once that gets downloaded and unpacked, you now have access to the source code, as well as an executable of the latest version.

To launch the executable, navigate to where the directory was unpacked, and go to the "dist" folder.  From there, click on finite-element and scroll to or search for the file names "stretchy.exe".  This is the executable that allows the program to run without access to Python or the required packages.  Double-click to launch (this may take a while) and have fun!

NOTE:  If you're running either a macOS or a Linux distro, chances are the .exe won't work.  In that case, you have to run from the source code.  Make sure that all the .py files are in the same directory, and run main.py to start.

If you choose to run through the source code, the following packages are required:

* [Matplotlib](https://matplotlib.org/#)
* [NumPy](https://numpy.org/)
* [TkInter](https://docs.python.org/3/library/tkinter.html)
* [pandas](https://pandas.pydata.org/)

---

### User's Guide
#### Background
This program solves for the displacement and stress of frame elements using equations found in chapters 3 and 5 of "A First Course in the Finite Element Method" by Daryl L. Logan.

The displacement calculations account for plane strain in the elements, and require the element materials [modulus of elasticity](https://en.wikipedia.org/wiki/Elastic_modulus) (E) as well as cross sectional area (A) of the element, and it's [area moment of inertia](https://en.wikipedia.org/wiki/List_of_second_moments_of_area) (I).

Stress calculations *do not* account for plane stress, and simply rely on [Hooke's Law](https://en.wikipedia.org/wiki/Hooke's_law).

#### Navigation
All of the navigation is done through the mouse.  Scrolling the mouse wheel will zoom in and out, and holding and dragging middle-mouse will pan the display to where you want.

To select an object, left click on it in the plotter window.  This will highlight it to indicate that it is selected.  Left click the object again to de-select.

#### Creating a Structure
Structures are started with nodes, which can be considered the joints or connections of a frame.  To create a node field, click the "Add Node" button and specify the cartesian coordinates for the node you'd like to place.  Click "Create Node" and repeat, or "Cancel" to exit the node creation interface.  Nodes will serve as the backbone of the structure; They rigidly connect frame elements, and accept initial conditions.

With the node field in place, everything else can be added to the structure.  To create frame elements, select 2 nodes (ONLY 2, no more, no less) and enter the desired member properties.

  A - Area cross-section of the member
  E - Member material modulus of elasticity
  I - Area moment of inertia of the member
  
 

Constraint

Load
  point
  distributed
  moment
  
Solver requirements

#### Solving
With a completed structure, you're free to solve.  Click the "Solve" button in the top left, and you'll see a few things change.  First, the original structure is translucent, and a new deformed structure is visible.  Nodes are now colormapped to their absolute displacement, and elements are colormapped to their stress values.  The colormap is visible to the right, and provides some context values for the colormapping.  In both cases, red indicates the maximum value pink the minimum.

In a lot of cases, the displacement is imperceptible relative to the size of the structure.  For this reason, I have included a "Gain" slider in the bottom right, above the "Reset Solution" button.  In solved mode, the Gain slider can be moved to multiply the displacement of each node.  This allows for better qualitative analysis.  The slider maxes out at 10,000x.

To exit solved mode and return to the structure editor, simply click the "Reset Solution" button in the bottom right.

#### Saving and Importing
Structures are saved as .html documents, which store lists of objects and their properties.  To save, simply click the "Save Structure" button in the bottom left, and navigate to the desired directory.  Similary, a structure can be imported by clicking on the "Import Structure" button.  From there, the file can be opened and imported into the program.

I have included a few different sample structures, located in the folder "Sample Structures".  You can import those to play around with some pre-made structures and to get used to the interface.

---

### Why?
Good question.

I was taking a course in the finite element method right around the same time that I had finally gotten Python working on my desktop, so I decided to combine the two and test my ability to ~~google~~ program.  The script was only intended to be text-based and contained to a single Python file, but I was playing around with the Matplotlib animation function and the project grew from there.

---

### What's Next?
This is still a work-in-progress.

One (major) part that needs updating is the stress calculations for each element.  The stress values are dependant on their order of creation, and a lot of the time do not reflect the actual stresses in the element.  The nodal displacements, however, seem to be correct.

Another big feature I'm missing is a way to save simulation results.  Right now, the only way to analyze the structure is to look at the pretty colors and compare them to the colormap on the right to estimate stress/displacement.  This sucks.  Ideally, I'd like to save the results as a .pdf that would include a screenshot of the full structure (deformed and undeformed) with node and element numbers displayed above each object, and a chart of nodes/element numbers and ther respective displacement/stress.  Once I get the stress calculations dialed in, this is my next step.

I also need to go through each file and finish commenting.  I was pretty good about doing that as I went, but some files (solver, for instance) had so many iterations that I decided to do that when I finished messing with that file (ad infinitum).

This program runs okay(ish).  The more nodes/elements/forces etc. the worse it runs, and it drops off *quickly*.  I dove a little bit into multi-threading the animation loop, since that's the limiting factor for framerate, but I'm not able to swing it yet.  I wanted to get this thing onto Github by the end of August, and I was running out of time (it's 8/24/2020 as I type this).  Multi-threading and other types of code optimization are on my radar, but don't hold your breath.

---

### Final Thoughts
Dear GOD why did I use Matplotlib as the animation platform?!?  Don't get me wrong, the Matplotlib animation function is great, and I'm sure someone who's a better programmer than I would be able to eek out more performance than me.  If they were smart, they'd probably use something different in the first place.  Pygame, for instance, would have been a better choice.  Even skipping over Python entirely and going straight to something like Unity would have helped.  That way, I could even do something in 3-D.  Oh well, live and learn.  At least now I'm *really* familiar with the Matplotlib documentation.

The entire goal of this project was to learn by throwing myself off the deep end, and I believe I did just that.  In my opinion, knowing what *not* to do is just as valuable (if not moreso) than knowing what to do from the start.  I'm not a software engineer by any stretch of the imagination, and I have a lot that I can do to improve (best practices, PEP 8, etc.).  That's not to say that this project was a failure; in fact, I'm very proud of what I was able to accomplish over the long weekend nights spent on making this thing.

Anyway, if you're still reading, congratulations.  I hope you find this project as cool as I have :)
