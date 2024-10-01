---
aliases:
  - angle and axis
---

![[Pasted image 20220303113439.png]]
Formula:$$ R(\theta, \overline v) = R_z(\alpha) \kern 3px R_y(\beta) \kern 3px R_z(\theta) \kern 3px R_y(-\beta) \kern 3px R_z(-\alpha) $$Where:
- $R_z$: [[HCR - Rotation Matrix|rotation matrix]] along the $z$ axis.
- $\theta$ is the angle of rotation along the $\overline v$ axis (in the figure this axis/vector it's represented by the vector $r$ but i wanted to avoid confusion between this axis of rotation and the elements of the rotation matrix $R$ : $r_{i,j}$, so i called it $\vec v$).<br>The angle of rotation $\theta$ can be found as:$$ \theta = \cos^{-1}\left(\frac{r_{1,1} + r_{2,2} + r_{3,3} - 1}{2}\right) $$And the axis of rotation $\vec v$ as:$$\overline v = \frac{1}{2\sin(\theta)}\left[\begin{array}{c}r_{3,2} - r_{2,3}\\r_{1,3} - r_{3,1}\\r_{2,1} - r_{1,2}\end{array}\right]$$Where:
	- $r_{i,j}$ is the $i,j$ element of the [[HCR - Rotation Matrix|rotation matrix]] $R$

So to find the $R$ rotation matrix we can impose $\theta$ and $\overline v$ as **constraints** and find:
$$
R = 
\left[
\begin{array}{l}
r_{1,1} & r_{1,2} & r_{1,3}
\\
r_{2,1} & r_{2,2} & r_{2,3}
\\
r_{3,1} & r_{3,2} & r_{3,3}
\end{array}
\right]
$$

> **NOTE**: #IMPORTANTE 
> For $r_{1,1} + r_{2,2} + r_{3,3} = 1$ -> $\theta = 0$ (or $\theta = \pi$) -> $\overline v = \infty$ (**Indeterminate**)
> The [[HCR - Rotation Matrix Descriptor 'Quaternion'|Quaternion]] descriptor is more complicated but can avoid this problem.