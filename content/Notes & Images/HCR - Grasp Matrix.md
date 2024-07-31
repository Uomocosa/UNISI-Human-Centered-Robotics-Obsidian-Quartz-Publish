# Grasp Matrix
![[Pasted image 20220404105945.png]]

- For each contact point we have a wrench $\overrightarrow{W_i}$ of dimensions $[6 \times 1]$
- We define the **Grasp Matrix** $\overline{\overline G}$ as:
$$
\overrightarrow{W_i} = \overline{\overline G} \cdot
%\left.
\left[
\overrightarrow{F_1}, \
\overrightarrow{F_2}, \
\ldots, \
\overrightarrow{F_n}, \
\right]^T
%\right|_{3n \times 1}
$$
-> Where:
- $W_c$ has dimensions: $[6 \times 1]$
- $\left[\overrightarrow{F_1}, \ \overrightarrow{F_2}, \ \ldots, \ \overrightarrow{F_n}, \ \right]^T$ has dimensions: $[3n \times 1]$
- So $\overline{\overline G}$ has dimensions: $[6 \times 3n]$

-> Instead of using the Moment of each contact point, we use the arm $\overrightarrow{b}$  to calculate it using the grasp matrix:
![[Pasted image 20220404110729.png]]
-> Where:
- $\overline{\overline I}$ : Identity matrix $[3 \times 3]$
- $\overline{\overline{S(b)}}$ : Skew matrix $[3 \times 3]$
- $\overrightarrow{b}$ : arm (distance of the contact point $C_i$ from the RF $O$ : $\overline{O \kern 3px C_i}$) $[3 \times 1]$

> **NOTE**:
> The Grasp Matrix depend on the reference frame, so we can write:
> ![[Pasted image 20220404111148.png]] 
> Or $\overline{\overline G}_0$
> Meaning the Grasp matrix is associated to the $0$-th reference frame
