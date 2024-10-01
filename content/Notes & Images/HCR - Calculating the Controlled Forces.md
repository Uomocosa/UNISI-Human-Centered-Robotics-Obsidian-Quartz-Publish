---
aliases:
  - Calculating the Controlled Forces
---

![[Pasted image 20220404150244.png]]
$$ \vec W_c =  \bar{\bar{G}} \cdot \left[ \begin{array}{l} F_{c1} \\ F_{c1} \end{array} \right] $$Where:
- $W_c$ is in the columns space of  $\bar{\bar{G}}$. #NOT_SURE_ABOUT_THIS `What does it mean?`<br>⇒ G has max rank so it has $1$ or $\infty$ solutions.<br>⇒ ($\infty$ solutions $\Leftrightarrow$ $N(G) \neq \{0\}$)

Then:$$ \bar{\bar{F_c}} = \bar{\bar{G}}^{\#} \cdot \vec W_c + N_G \cdot \xi $$Where:
- $\bar{\bar{G}}^{\#}$ : pseudo-inverse
- $N_G$ : free parameter vector ($N_G = N(G)$)
- $\bar{\bar{G}}^{\#} \cdot \vec W_c$ : solution of the linear system
- ==Among all the $\xi$ we chose one such that $\bar{\bar{F_c}} = [F_{c1}, \ F_{c2}]$ belongs to the friction cones==.

---
- ***~ Ex.:***
	- Given an object and some contact points:<br>![[Pasted image 20220404151232.png|333]]<br>We want to calculate: $$\vec W_c = \bar{\bar{G}} \cdot \left[ \vec F_{c1}, \ \vec F_{c2}, \ \vec F_{c2}  \right]^{\tiny T} $$So:
		1. Compute $\bar{\bar{G}}$ :<br>![[Pasted image 20220404151415.png|444]]
		2. Calculate the [[HCR - Kernel • Nullspace|nullspace]] of $G$ : $N(G)$<br>![[Pasted image 20220404151444.png|444]]
		3. Find $\xi$ such that:<br>![[Pasted image 20220404151517.png|444]]
