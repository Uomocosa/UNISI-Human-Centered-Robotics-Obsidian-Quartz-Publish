---
aliases:
  - External Wrench
---
The external wrench $W_{\kern-3px e}$ is so defined:$$
W_{\kern-3px e} := 
\left[
\begin{array}{l}
F_e
\\
M_e
\end{array}
\right]_{6 \times 1}
$$Where:
- $F_e$ : Sum of all external Forces
- $M_e$ : Sum of all external Moments

So if we have an external wrench we can define the system as **In Equilibrium** (or grasping equilibrium) if we apply to it a *Controlled Wrench* $W_{\kern-3px c}$ , such that:
$$
W_{\kern-3px c} = - W_{\kern-3px e}
$$
- $W_{\kern-3px c}$ can be imposed by a human hand (IRL), a robotic hand (Industry) or a virtual hand (VR).
- $W_{\kern-3px c}$ the controlled wrench (3 forces and 3 moments) represents the overall effect in term of forces and moments on the barycenter of the object, given by all the **contact forces** applied by the human/robotic/virtual hand at the contacts established with the object.