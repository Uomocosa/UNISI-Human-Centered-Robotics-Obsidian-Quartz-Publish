---
aliases:
  - Chain of Joints
---
Let's take a chain of joints:<br>![[Pasted image 20220404112555.png|333]]

The generic formula will be:$$ \left( \begin{array}{l} v \\ w \end{array} \right) =  \bar{\bar{J}} \cdot \left( \begin{array}{l} v_{J1} \\ v_{J2} \\ v_{J3} \end{array} \right) $$Where:
- $v$ and $w$ : **velocity** and **angular velocity** of the **end-effector**.
- $\bar{\bar{J}}$ : [[HCR - Matrice Jacobiana|Jacobian matrix]]
- $v_{Ji}$ : velocity of joint $i$, more specifically:$$ v_{Ji} = \left\{\begin{array}{l}\dot \Theta_i &\text{if joint $i$ is an angular joint}\\\dot d_i &\text{if joint $i$ is a prismatic joint}\end{array}\right.$$Where:
	- $d_i$: distance of $i$-esim joint from $(i-1)$-esim joint.
