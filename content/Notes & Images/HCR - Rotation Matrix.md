---
aliases:
  - rotation matrix
  - rotation matrices
---
Given two [[HCR - Reference Frame|reference frames]] like so:
![[Pasted image 20220303101837.png]]

We can write:
$$
\left\{
\begin{array}{l}
x'  = x'_x \cdot x + x'_y \cdot y + x'_z \cdot z
\\
y'  = y'_x \cdot x + y'_y \cdot y + y'_z \cdot z
\\
z'  = z'_x \cdot x + z'_y \cdot y + z'_z \cdot z
\end{array}
\right. 
\kern 30 px \to \kern 30 px
\left[
\begin{array}{l}
x'
\\
y'
\\
z'
\end{array}
\right]
= 
\bar{\bar{R}}
\left[
\begin{array}{l}
x
\\
y
\\
z
\end{array}
\right]
$$
Where for example $z'_x, \ z'_y, \ z'_z$ is defined as:
![[Pasted image 20220303102512.png]]

So, $R$ is defined as:
$$
R
\kern 15 px = \kern 15 px
\left[
\begin{array}{l}
x'_x & x'_y & x'_z
\\
y'_x & y'_y & y'_z
\\
z'_x & z'_y & z'_z
\end{array}
\right]
\kern 15 px \triangleq \kern 15 px
R_{O\kern1px'}^{O}

$$
$R_{O\kern1px'}^{O}$ $\triangleq$ Rotation Matrix from reference frame $O$ to $O \kern 1px '$
