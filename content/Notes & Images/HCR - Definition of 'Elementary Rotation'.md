---
aliases:
  - elementary rotation
  - elementary rotation matrix
  - elementary rotation matrices
---
Given 2 [[HCR - Reference Frame|reference frames]] we define the ***elementary rotation*** of the frame $A$ with respect to frame $B$ as the rotation of **only one axis** of the frames.

> The composition of multiple ***Elementary Rotation Matrix*** result in a complete [[HCR - Rotation Matrix|Rotation Matrix]].
> ~Ex.:<br>![[Pasted image 20220303103616.png|444]]

~ Example: Rotation along the $x$ axis:<br>![[Pasted image 20220303105424.png|444]]

We rotate the frame with an angle of $\theta$ along the $x$ axis, as we can see in the second picture we can rewrite the rotation as:
$$
R_{x(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
1 & 0 & 0
\\
0 & \cos(\theta) & -\sin(\theta)
\\
0 & -\sin(\theta) & \cos(\theta)
\end{array}
\right]
$$
---
- ***~Example: Other Elementary Rotations***:$$\begin{array}{l} R_{x(\theta)} \kern 15 px = \kern 15 px \left[ \begin{array}{c} 1 & 0 & 0 \\ 0 & \cos(\theta) & -\sin(\theta) \\ 0 & -\sin(\theta) & \cos(\theta) \end{array} \right] \\[5px] R_{y(\theta)} \kern 15 px = \kern 15 px \left[ \begin{array}{c} \cos(\theta) & 0 & \sin(\theta) \\ 0 & 1 & 0 \\ -\sin(\theta) & 0 & \cos(\theta) \end{array} \right] \\[5px] R_{z(\theta)} \kern 15 px = \kern 15 px \left[ \begin{array}{c} \cos(\theta) & -\sin(\theta) &  0 \\ \sin(\theta) & \cos(\theta) & 0 \\ 0 & 0 & 1 \end{array} \right]  \end{array} $$
