# Finite-Element
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

One (major) part that needs updating is the stress calculations for each element.  The stress values are dependant the order of creation, and a lot of the time do not reflect the actual stresses in the element.  The nodal displacements, however, are correct.

I also need to go through each file and finish commenting.  I was pretty good about doing that as I went, but some files (solver, for instance) had so many iterations that I decided to do that when I finalized that file (as if).

Current files that need commenting are:
  * file1
  * file2
  * file3

This program runs okay(ish).  The more nodes/elements/forces etc. the worse it runs, and this drops off *quickly*.  I dove a little into possibly multi-threading the animation loop since casuses the most noticeable frame issues, but I wasn't able to swing it in the end.  I wanted to get this thing onto Github by the end of August, and I was running out of time (It's 8/23/2020 as I type this).  Multi-threading and other types of code optimization are on my radar but don't hold your breath.

---

### Final Thoughts

