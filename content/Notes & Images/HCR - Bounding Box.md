# Bounding Box
Let's define the shape of our triangles with equations:
![[Pasted image 20220404095332.png]]
(Triangles equations are planes equations)

We can define being in an object if we are inside the **bounding box**, then we can say that we are "touching" that object.
![[Pasted image 20220404095414.png]]

-> We are in the bounding box if our current position $<x, \ y, \ z>$ respects all the inequalities:
$$
a_ix+b_iy+c_iz +d \le 0 \kern 25px \forall \kern 2px i
$$
(this is not entirely true, for just touch it should be $=0$, and for penetration $<0$ but having it exactly equal to 0 is impossible).

> The touching simulation and prevision is really good if the mesh has a lot of points (better approximation), but more points also mean more delay.
