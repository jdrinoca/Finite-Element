# Finite-Element
NOT FINISHED

A 2-D finite element solver and interface.

---

### Table of Contents
1. [Introduction](#Introduction)
2. [How to Download](#How-to-Download)
3. [User's Guide](#Users-Guide)
4. [Why?](#Why)
5. [What's Next?](#Whats-Next)
6. [Final Thoughts](#Final-Thoughts)

---

### Introduction


---

### How to Download


---

### User's Guide


---

### Why?
Good question.

I was taking a course in the [finite element method](https://en.wikipedia.org/wiki/Finite_element_method) right around the same time that I had finally gotten Python working on my desktop, so I decided to combine the two and test my ability to ~~google~~ program.  The script was only intended to be text-based and contained to a single Python file, but I was playing around with the Matplotlib animation function and the project grew from there.

---

### What's Next?
This is still a work-in-progress.

One (major) part that needs updating is the stress calculations for each element.  The stress values are dependant on their order of creation, and a lot of the time do not reflect the actual stresses in the element.  The nodal displacements, however, seem to be correct.

Another big feature I'm missing is a way to save simulation results.  Right now, the only way to analyze the structure is to look at the pretty colors and compare them to the colormap on the right to estimate stress/displacement.  This sucks.  Ideally, I'd like to save the results as a .pdf that would include a screenshot of the full structure (deformed and undeformed) with node and element numbers displayed above each object, and a chart of nodes/element numbers and ther respective displacement/stress.  Once I get the stress calculations dialed in, this is my next step.

I also need to go through each file and finish commenting.  I was pretty good about doing that as I went, but some files (solver, for instance) had so many iterations that I decided to do that when I finished messing with that file (ad infinitum).

This program runs okay(ish).  The more nodes/elements/forces etc. the worse it runs, and it drops off *quickly*.  I dove a little bit into multi-threading the animation loop, since that's the limiting factor for framerate, but I'm not able to swing it yet.  I wanted to get this thing onto Github by the end of August, and I was running out of time (it's 8/24/2020 as I type this).  Multi-threading and other types of code optimization are on my radar, but don't hold your breath.

---

### Final Thoughts
Dear GOD why did I use Matplotlib as the animation platform?!?  Don't get me wrong, the Matplotlib animation function is great, and I'm sure someone who's a better programmer than I would be able to eek out more preformance than me but if they wer smart, they'd probably use something different in the first place.
