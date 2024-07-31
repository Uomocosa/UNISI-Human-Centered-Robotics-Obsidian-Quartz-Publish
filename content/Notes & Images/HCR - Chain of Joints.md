# Chain of joints
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