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