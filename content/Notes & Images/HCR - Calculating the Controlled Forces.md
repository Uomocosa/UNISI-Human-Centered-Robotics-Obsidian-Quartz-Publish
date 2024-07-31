# Calculate the Forces
![[Pasted image 20220404150244.png]]
$$
\overrightarrow{W_c} = 
\overline{\overline{G}} \cdot
\left[
\begin{array}{l}
F_{c1}
\\
F_{c1}
\end{array}
\right]
$$
-> Where:
- $W_c$ is in the columns space of  $\overline{\overline{G}}$
	-> G has max rank so it has $1$ or $\infty$ solutions
	-> ($\infty$ solutions $\Leftrightarrow$ $N(G) \neq \{0\}$)

Then:
$$
\overline{\overline{F_c}} =
\overline{\overline{G}}^{\#} \cdot
\overrightarrow{W_c} +
N_G \cdot \xi
$$
-> Where:
- $\overline{\overline{G}}^{\#}$ : pseudo-inverse
- $N_G$ : free parameter vector ($N_G = N(G)$)
- $\overline{\overline{G}}^{\#} \cdot \overrightarrow{W_c}$ : solution of the linear system

Among all the $\xi$ we chose one such that $\overline{\overline{F_c}} = [F_{c1}, \ F_{c2}]$ belongs to the friction cones.

---
###### ~ Ex.:
Given an object and some contact points:
![[Pasted image 20220404151232.png]]
$$
\overrightarrow{W_c} = 
\overline{\overline{G}} \cdot
\left[
\overrightarrow{F_{c1}}, \
\overrightarrow{F_{c2}}, \
\overrightarrow{F_{c2}}, \
\right]^T
$$
1. Compute $\overline{\overline{G}}$ :
![[Pasted image 20220404151415.png]]

2. Calculate the null space of $G$ : $N_G$
![[Pasted image 20220404151444.png]]

3. Find $\xi$ such that:
![[Pasted image 20220404151517.png]]
