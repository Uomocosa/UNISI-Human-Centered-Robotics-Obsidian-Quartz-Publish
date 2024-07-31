# 

![[Pasted image 20220404112555.png]]

$$
\left(
\begin{array}{l}
v
\\
w
\end{array}
\right)
= \overline{\overline{J}} \cdot
\left(
\begin{array}{l}
v_{J1}
\\
v_{J2}
\\
v_{J3}
\end{array}
\right)
$$
-> Where:
- $v$ and $w$ : velocity and angular velocity of end-effector
- $v_{Ji}$ : velocity of joint $i$
- $\overline{\overline{J}}$ : Jacobian matrix

$$
v_{Ji} = 
\left\{
\begin{array}{l}
\dot \Theta_i &\text{if joint $i$ is an angular joint}
\\
\dot d_i &\text{if joint $i$ is a prismatic joint}
\end{array}
\right.
$$
-> Where:
- $d_i$: distance of $i$-esim joint from $(i-1)$-esim joint

---
# Chain of joints:
![[Pasted image 20220404113131.png]]

---
# Chains of joints that refers to the same end-effector
![[Pasted image 20220404113202.png]]
![[Pasted image 20220404113214.png]]

The selection of the contact velocities depends on the model of the contact that we used.

-> There are 3 main **contact models**:
1. *Hard finger with friction*
2. *Hard finger without friction*
3. *Soft finger*

We will use the 1-st one (*Hard finger with friction*)

-> To understand the difference between the first and the second model let's consider us holding a pen and wanting to write on a piece of paper:
- If the paper is normal (it has friction) I can easily write on it (1-st case)
- If the paper is oily (it has no friction) I cannot write on it, I can only impose a vertical force, I slip away when I apply tangential forces (2-nd case)
- In case of *Soft fingers* we have reduced control on it, instead of having for its wrench 3 forces and 3 moments we only have 3 forces and 1 moment:
$$
W_{\text{soft finger}} = 
\left[
\begin{array}{l}
\left.\overrightarrow{F} \kern 7px \right|_{[3 \times 1]}
\\[5px]
\left.\overrightarrow{M} \kern 7px \right|_{[1 \times 1]}
\end{array}
\right]_{[4 \times 1]}
$$
---
# Hard Fingers
![[Pasted image 20220404114023.png]]

---
### From single kinematic chain Jacobian (or single finger Jacobian) to Hand Jacobian
![[Pasted image 20220404114141.png]]
-> Where:
- $j_Fi$  : joint Finger $i$
- each joint is angular, so it will have an angular velocity $\dot \Theta_i$

![[Pasted image 20220404114312.png]]
![[Pasted image 20220404114324.png]]

> **NOTE**:
> The energy at the end-effector is the sum of all the energy expended by the joints.
> The joints at each point is calculated by the force times the velocity.

![[Pasted image 20220404114506.png]]

Ideally without dissipation of energy we have:
![[Pasted image 20220404114531.png]]

We also know that:
![[Pasted image 20220404114549.png]]

After a rough estimation of the weight and the barycenter of the object, our brain computes the already seen formula:
![[Pasted image 20220404114630.png]]
-> So our brains has to do a few passages before we move the object at hand:
1. First it calculates the trajectory ($W_c$), how I want the object to behave.
2. Then it calculates the Grasp matrix, where are my finger on the object
3. Lastly it evaluates the forces needed to move the object along the previous thought trajectory

---
# Solution of a linear system
A liner system can have:
- 0 solutions
- 1 solutions
- $\infty$ solutions

-> The forces applied by our brain should belong to the friction cones and if I have only 1 solution  for $F_{C1}, \ F_{C2}, \ \ldots, \ F_{Cn}$ no one guaranties me that one specific solution belongs to the friction cones
- It's much better to have **$\infty$ solutions** to respect the **friction constraints**.

---
# Theorem
$\overrightarrow{W_c} = \overline{\overline{G}} \cdot \overline{\overline{F_c}}$ accepts $1$ or $\infty$ solutions if and only if $\rho(G) = \rho(G \ \vdots \ W_c)$ 
Else it accepts no solutions.

-> $\rho(G)$: **rank** of matrix $G$
-> $\rho(G \ \vdots \ W_c)$: rank of matrix $[G \ \vdots \ W_c]$
-> $\rho(G) = \rho(G \ \vdots \ W_c)$  means that $G$ has to have maximum rank.

---
# Lemma
If $\rho(G) = \rho(G \ \vdots \ W_c)$ and:
- $N(G) = \{0\}$ -> $1$ solution
- $N(G) \neq \{0\}$ -> $\infty$ solutions

-> $N(G)$ : **null space** of $G$
> **NOTE**:
> $\{0\}$ is always in the null space.
> $N(G) \neq \{0\}$ means that the null space contains other vectors other than $\{0\}$

---
# Conclusion
So we desire for a grasp matrix such that:
$$
\left\{
\begin{array}{l}
\rho(G) = \rho(G \ \vdots \ W_c)
\\
N(G) \neq \{0\}
\end{array}
\right.
$$
-> Then we will have $\infty$ solutions for the forces applied at the contact points ($\overline{\overline{F_c}} = F_{C1}, \ F_{C2}, \ \ldots, \ F_{Cn}$).
- Among all the solutions we can find one that satisfies the **friction constraints**.
