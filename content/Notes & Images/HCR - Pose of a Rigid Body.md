# Pose of a Rigid Body
A rigid body is completely described in a reference frame by **position** and **orientation**.
![[Pasted image 20220303100614.png]]
The position of point $O \kern 1px '$ on the rigid body with respect to the coordinate frame $O$ ($x, y, z$) is expressed by a three dimensional vector $<o \kern 1px '_x, \ o \kern 1px '_y, \ o \kern 1px '_z>$.

Where $o \kern 1px '_x, \ o \kern 1px '_y, \ o \kern 1px '_z$ are **versors**. *(??? doesn't make sense that they are versors ???)*

So the position of $O \kern 1px '$ with respect to $O$ is defined as:
$$
O \kern 1px ' = o \kern 1px '_x + o \kern 1px '_y + o \kern 1px '_z
$$
![[Pasted image 20220303101438.png]]

In this case:
- $O$ : is the **World reference frame**
- $O \kern 1px '$ : is the **Object reference frame**

> The idea is:
> I want to know $O \kern 1px '$ in respect to $O$.
> This because in my system $O$ is NOT allowed to change (being the world reference frame) so it's perfect for referencing $O \kern 1px '$ that can change.


While for the **position** of $O \kern 1px '$ with respect to $O$, we can use the position of each vector of the object frame with respect to the [[HCR - Reference Frame|reference frame]]:
![[Pasted image 20220303101837.png]]
We obtain a representation of rotation by the [[HCR - Rotation Matrix|Rotation Matrix]]
