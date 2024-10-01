---
aliases:
  - triangular meshes
---
Approximate any surface to a mathematical model made of triangles.
Useful for creating simulations and VR-models.

----
- ***How to create a triangular mesh from a real world object***:
	1. Scan the object.
	2. Obtain from the scan a *cloud of points*.
	3. Using the points from the cloud of points create the triangular mesh.
----
- ***Why is it a triangular mesh***?
	- Because 3 is the minimum number of points needed to create a plane.
----
- ***Each triangle has its own normal***
	- Calculating the normal of a plane is useful for the calculations of the optimal contact point of the robot.
----
- ***~Ex.: Cloud of points -> Triangular mesh***:<br>![[Pasted image 20220404094812.png]]
