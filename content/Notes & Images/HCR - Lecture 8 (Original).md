# Grasping vs Manipulation:
- **GRASPING**: Holding an object (it moves with me but is relatively still)
- **MANIPULATION**: Hold an object and control its *trajectory* (specific to the object)

We can see:
- Manipulation -> active motion
- Grasping -> passive motion

-> To manipulate objects humans have specifically developed the thumb
- Really important when talking about manipulation.

There are 2 kinds of manipulation:
- IN-HAND MANIPULATION
- POWER GRASP

---
# IN-HAND MANIPULATION
Move the object with respect to the palm.
Also called "dexteritious manipulation"
~ Ex.: *Writing with a pen*

---
# POWER GRASP
I don't care about the specific motion of the object.
The object moves with respect to the arm (not the palm)
~ Ex.: *Holding air-pods*

---
# Brain prospective
From our brain prospective when we grasp an object (power grasp) it does not cast anything (it doesn't think about the hand receptors).
- For power grasping we do have control over the object in our hand, but it is not accurate, tho it is fast to process (for our brain).
- For in-hand manipulation, like writing with a pen we use 3 contact point (more generally a small number of contact points) and we need to control each of them very well.
(While for power grasping we have many contact point but no need to control them)

---
# Friction Cone
![[Pasted image 20220404102704.png]]

![[Pasted image 20220404102723.png]]
-> Where:
$$
\begin{array}{l}
\Theta = 
\\
\eta: \text{friction coefficent}
\end{array}
$$
(The friction coefficent ($\eta$) is specific for each pair of object interaction)

- A force that want to break the friction is applied as shown:
![[Pasted image 20220404102930.png]]


![[Pasted image 20220404102945.png]]
$F_1$ is too small to break friction (the object doesn't move)
$F_2$ is big enough (the object begins to move)
- Graphically $F_1$ is **inside the friction cone**
- While $F_2$ is **outside the friction cone**

Knowing **where** the friction cone is, and how **big** it is, is extremely crucial, because if i want to apply force to the object without it slipping out (break friction) i need to apply all the forces such that they stay **inside** the friction cones.

###### ~ Ex.: Position of the friction cones
Suppose we have this object:
![[Pasted image 20220404103439.png]]

Let's see how the position of the friction cones is useful.

I apply to the previous object 3 forces: $F_1, F_2, F_3$, resulting in this 3 friction cones:
![[Pasted image 20220404103555.png]]

Take now an opposite force $F$ that tries to break friction.
It is clear that where i apply the previous 3 forces changes the intensity of the Force $F$ needed to break friction:
![[Pasted image 20220404103726.png]]

---
# Representation of the forcer on the Reference Frame
Every force on an object can be represented in the object **RF** (Reference Frame) usually defined as its *barycenter* by another Force plus a Torque.
![[Pasted image 20220404103945.png]]

Also every interaction the object has with the world can be summarized by an external Force and an external Moment (or Torque)

- To compute the Torque $\tau '$
![[Pasted image 20220404104129.png]]
![[Pasted image 20220404104142.png]]

in the RF (reference frame) $0$ ->
$$
\left(
\begin{array}{l}
M_{x_0}
\\
M_{y_0}
\\
M_{z_0}
\end{array}
\right)_0
= 
\overrightarrow{b}_{\ 0} \wedge \overrightarrow{F}_{\ 0}
$$
- The vector product can be computed using the **Skew Matrix**:
![[Pasted image 20220404105207.png]]

---
# Wrench
$$
W := 
\left[
\begin{array}{l}
F
\\
M
\end{array}
\right]_{6 \times 1}
$$
-> Where:
- $F$ : Force vector $[3 \times 1]$
- $M$ : Moment vector $[3 \times 1]$

---
# External Wrench
The external wrench $W_e$ is so defined:
$$
W_e := 
\left[
\begin{array}{l}
F_e
\\
M_e
\end{array}
\right]_{6 \times 1}
$$
-> Where:
- $F_e$ : Sum of all external Forces
- $M_e$ : Sum of all external Moments

-> So if we have an external wrench we can define the system as **In Equilibrium** (or grasping equilibrium) if we apply to it a *Controlled Wrench* $W_c$ , such that:
$$
W_c = - W_e
$$
- $W_c$ can be imposed by a human hand (IRL), a robotic hand (Industry) or a virtual hand (VR).

- $W_c$ the controlled wrench (3 forces and 3 moments) represents the overall effect in term of forces and moments on the barycenter of the object, given by all the **contact forces** applied by the human/robotic/virtual hand at the contacts established with the object.

---
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

---
# Change of the Normal
Suppose we posses an object and we want to find the best possible grasp between this two configurations:
![[Pasted image 20220404111407.png]]

-> We look at the normal of the surface at the contact points:
- Notice how if the contact points in the first case change a little the normal changes a lot.
- While in the second case if we change the contact points a little (or we perturbate them) the normal does not change at all.

![[Pasted image 20220404111625.png]]

-> So we can say:
![[Pasted image 20220404111643.png]]