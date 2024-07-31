# Triangular Meshes
Approximate any surface to a mathematical model made of triangles.
Useful for creating simulations and VR-models.

-> How to create a triangular mesh from a real world object
1. Scan the object
2. Obtain from the scan a *cloud of points*
3. Using the points from the cloud of points create the triangular mesh

-> Why is it a **triangular** mesh?
- Because 3 is the minimum number of points needed to create a plane.

-> Each triangle has its own **normal**
- Calculating the normal of a plane is useful for the calculations of the optimal contact point of the robot.


###### ~Ex.: Cloud of points -> Triangular mesh
![[Pasted image 20220404094812.png]]

---
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

---
# Interpolation
For each triangle in our triangular mesh there is only one normal, to solve thins, we can then make an interpolation:
![[Pasted image 20220404094945.png]]
-> So the normal now becomes a smooth function (always depending on the position), before as we can see in the figure we have that the normal is constant for each triangle so we have a non-smooth transition when we pass from one triangle to another.

When we have fewer points then we can take the interpolation:
![[Pasted image 20220404100053.png]]
-> Where:
$$
\begin{array}{l}
\overline{u_p} = \alpha \kern 2px \overline{u_1} + \beta \kern 3px \overline{u_2}
\\[5px]
\rightarrow x_p = x_1 \kern 15px \text{for} \ \alpha = 1, \ \beta = 0
\\
\rightarrow x_p = x_2 \kern 15px \text{for} \ \alpha = 0, \ \beta = 1
\end{array}
$$
Considering:
- Distance between $x_1$ and $x_2$ as: $\overline{x_1 x_2}$
- Distance between $x_1$ and $x_p$ as: $\overline{x_1 x_p}$
- Distance between $x_p$ and $x_2$ as: $\overline{x_p x_2}$

All of them positive (distances cannot be negative)

-> Generally we have:
$$
\begin{array}{l}
\beta = &&\Large\frac{\overline{x_1 x_p}}{\overline{x_1 x_2}}
\\[5px]
\alpha =& 1 - \beta = &\Large\frac{\overline{x_2 x_p}}{\overline{x_1 x_2}}
\end{array}
$$
Considering now 3 points (for a triangle): $x_1, \ x_2, \ x_3$, with their respective normals: $\overline{u_1}, \ \overline{u_2}, \ \overline{u_3}$
![[Pasted image 20220404100912.png]]

-> The interpolated normal of $x_p$ can be calculated as:
![[Pasted image 20220404101120.png]]

---
# How to select a sample triangle?
- OCTATREE method.

Given 8 points create a 3D object (parallelepiped)
![[Pasted image 20220404101233.png]]
-> Creating 6 planes that you can play with.

$<\kern 7px ?  >$ **SEARCH FOR OCTATREE METHOD**
