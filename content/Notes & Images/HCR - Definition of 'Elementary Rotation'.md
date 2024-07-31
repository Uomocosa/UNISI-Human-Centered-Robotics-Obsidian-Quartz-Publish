### Definition 'Elementary Rotation'
Given 2 [[HCR - Reference Frame|reference frames]] we define the Elementary Rotation of the frame A with respect to frame B as the rotation of **only one axis** of the frames.

The composition of multiple Elementary Rotation Matrix result in a complete [[HCR - Rotation Matrix|Rotation Matrix]]

![[Pasted image 20220303103616.png]]

###### ~ Example: Rotation along the $x$ axis
![[Pasted image 20220303105424.png]]

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
###### ~ Example: Other Elementary Rotations
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
$$
R_{y(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
\cos(\theta) & 0 & \sin(\theta)
\\
0 & 1 & 0
\\
-\sin(\theta) & 0 & \cos(\theta)
\end{array}
\right]
$$
$$
R_{z(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
\cos(\theta) & -\sin(\theta) & 0
\\
\sin(\theta) & \cos(\theta) & 0
\\
0 & 0 & 1
\end{array}
\right]
$$
---
