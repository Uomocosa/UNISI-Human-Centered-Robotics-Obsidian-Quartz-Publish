---
aliases:
  - homogeneous transformation matrix
---
The **entire** [[HCR - Pose of a Rigid Body|pose of an object]], given one [[HCR - Reference Frame|reference frame]] could be represented in another frame, just by multiplying the first one with a matrix called **homogeneous transformation matrix**.

Contrary to the [[HCR - Rotation Matrix|rotation matrix]], where we tackle only the problem of **orientation**, now we want to resolve also the problem of **position**.

After all ==a **pose** is just a collection of *position* and *orientation*==

![[Pasted image 20220303162143.png|300]]
- So, first I resolve the problem of position (**translation**) then the problem of orientation (**rotation**).
	1. Solve the difference of $O$ and $O \kern 1px '$.
	2. Considering the $O$ and $O \kern 1px '$ in the same center i calculate the [[HCR - Rotation Matrix|rotation matrix]].

---
### Definition of 'Transformation Matrix'
The **Transformation Matrix** that change one pose to another is denoted as $T$.
$$ T^O_{O \kern 1px '} =  \left[ \begin{array}{cc} \left[R^O_{O \kern1px '}\right]_{3\times 3} & \kern5px \left[O \kern 1px '\right]_{3\times 1} \\[7px] \begin{array}{l} 0 & 0 & 0
\end{array} & \kern5px 1 \end{array} \right]_{4\times4} $$
Where:
- $R^O_{O \kern 1px '}$ : [[HCR - Rotation Matrix|rotation matrix]].
- $O \kern 1px '$ : distance $\overline{O \kern 2px O \kern 1px '}$

Then we can write the following transformation given a point $p^{O}$ in the reference frame $O$ we can find the point $p^{O \kern 1px '}$ in the reference frame $O \kern 1px '$:$$p^{O \kern 1px '} = T_{O \kern 1px '}^O \cdot p^{O}$$

> **NOTE**:
> The 3 zeros elements in the last row are usually unchanged but sometimes they do change, when they do it's because we want to impose the **concept of prospective**, for example when using a camera some dimensions are forcefully distorted (closer objects appear bigger).

> **NOTE**:
> The last element $(4,4)$ is often $1$, but it can be changed to reference the **scale of my robot or environment** ($0.1$, $0.01$, $0.001$, ... when working with small robots, while we'll change it to $10$, $100$, $1000$, $10000$ for big robots)

----

The **inverse** of a **tranformation matrix** $T$ is also a transformation matrix, and can be computed as:$$\begin{array}{l} T^{-1} &=& \left[\begin{array}{c} R^O_{O \kern1px '} &  O' \kern2px \\[5px] \begin{array}{c} 0 & 0 & 0 \end{array} & 1 \end{array}\right]^{-1} \\[-5px]&\kern3px\downarrow&\\[-5px] &=& \left[\begin{array}{c} \left(R^O_{O \kern1px '}\right)^{\tiny T} &  -\left(R^O_{O \kern1px '}\right)^{\tiny T} \cdot O' \kern2px \\[5px] \begin{array}{c} 0 & 0 & 0 \end{array} & 1 \end{array}\right] \end{array}$$***Source***: [Mecharithm (reading)](https://mecharithm.com/learning/lesson/homogenous-transformation-matrices-configurations-in-robotics-12#:~:text=The%20inverse%20of%20a%20transformation%20matrix%20T%20%E2%88%88%20SE(3)%20is%20also%20a%20transformation%20matrix%20and%20can%20be%20computed%20as) ^inverse-of-a-transformation-matrix
