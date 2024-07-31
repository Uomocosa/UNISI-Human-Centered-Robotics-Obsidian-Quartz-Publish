- ###### Rigid Bodies
- ###### Basics of Kinematics
Represent an object into space using the concept of reference frame

---
# Reference Frame
The reference frame is a 3 axis system that are usually connected by a body, an object or a system that can be used to acquire information or transmit information.
For example a camera can be a reference frame, when you record a video, you are recording from a fixed point of view, the lenses of the camera, which has a **mean direction**.
We can use the object frame (the camera) as reference for a robotic arm that gets information from it, so the camera becomes our **reference frame**.

Main concepts:
- **Reference Frame**.
- **Position**.
- **Orientation**.

---
###### Reference Frames Examples:
1. Camera Reference Frame
2. Multi joint hand fingertips frame
3. Virtual world reference frame
![[Pasted image 20220303095951.png|400]]

Everything has a reference frame in our robotic task.
> **Main task in robotics**: 
> Represent a reference frame of an object into another object's reference frame, that can be the world reference frame, the camera's, sensor's, ...

---
# Pose of a Rigid Body
A rigid body is completely described in a reference frame by **position** and **orientation**.
![[Pasted image 20220303100614.png]]
The position of point $O \kern 1px '$ on the rigid body with respect to the coordinate frame $O$ ($x, y, z$) is expressed by a three dimensional vector $<o \kern 1px '_x, \ o \kern 1px '_y, \ o \kern 1px '_z>$.

Where $o \kern 1px '_x, \ o \kern 1px '_y, \ o \kern 1px '_z$ are **versors**. *(??? doesn't make sense that they are versors ???)*

So the position of $O \kern 1px '$ with respect to $O$ is defined as:
$$
O \kern 1px ' = o \kern 1px '_x + o \kern 1px '_y + o \kern 1px '_z
$$
![[Pasted image 20220303101438.png]]

In this case:
- $O$ : is the **World reference frame**
- $O \kern 1px '$ : is the **Object reference frame**

> The idea is:
> I want to know $O \kern 1px '$ in respect to $O$.
> This because in my system $O$ is NOT allowed to change (being the world reference frame) so it's perfect for referencing $O \kern 1px '$ that can change.


While for the **position** of $O \kern 1px '$ with respect to $O$, we can use the position of each vector of the object frame with respect to the reference frame:
![[Pasted image 20220303101837.png]]
We obtain a representation of rotation by the **Rotation Matrix**

---
# Rotation Matrix
![[Pasted image 20220303101837.png]]

I can try to write something like this:
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
\kern 15 px \to \kern 15 px
\left[
\begin{array}{l}
x'
\\
y'
\\
z'
\end{array}
\right]
\kern 15 px = \kern 15 px
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

---
### Definition 'Elementary Rotation'
Given 2 reference frames we define the Elementary Rotation of the frame A with respect to frame B as the rotation of **only one axis** of the frames.

The composition of multiple Elementary Rotation Matrix result in a complete Rotation Matrix

![[Pasted image 20220303103616.png]]

###### ~ Example: Rotation along the $x$ axis
![[Pasted image 20220303105424.png]]

We rotate the frame with an angle of $\theta$ along the $x$ axis, as we can see in the second picture we can rewrite the rotation as:
$$
R_{x(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
1 & 0 & 0
\\
0 & \cos(\theta) & -\sin(\theta)
\\
0 & -\sin(\theta) & \cos(\theta)
\end{array}
\right]
$$
###### ~ Example: Other Elementary Rotations
$$
R_{x(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
1 & 0 & 0
\\
0 & \cos(\theta) & -\sin(\theta)
\\
0 & -\sin(\theta) & \cos(\theta)
\end{array}
\right]
$$
$$
R_{y(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
\cos(\theta) & 0 & \sin(\theta)
\\
0 & 1 & 0
\\
-\sin(\theta) & 0 & \cos(\theta)
\end{array}
\right]
$$
$$
R_{z(\theta)}
\kern 15 px = \kern 15 px
\left[
\begin{array}{c}
\cos(\theta) & -\sin(\theta) & 0
\\
\sin(\theta) & \cos(\theta) & 0
\\
0 & 0 & 1
\end{array}
\right]
$$
---
# Composition of Elementary Rotation
Each orientation could be composed by elementary rotations of the object frame with respect to the reference frame.

Successive rotations of an object about the **object frame** is obtained by **Premultiplication** of rotation matrices.

Successive rotations of an object about the **reference frame** is obtained by **Postmultiplication** of rotation matrices.

Where Premultiplication and Postmultiplication only mean when the Elementary Rotation Matrix is multiplied (if at the beginning or at the end).

> Remember:
> The object frame is referenced to the reference frame

---
# Rotation Matrices Descriptors
Rotation Matrices give a redundant description of frame orientation.

We can use other descriptors:
- **Euler Angles**.
- **RPY Angles**.
- **Angle and Axis**.
- **Quaternion**.

---
# Euler Angles
I have to specify beforehand in which axis i will rotate: ~ex.: **ZXZ**
Also all Euler Angles will do 3 elementary rotations: $[\varphi, \ \theta, \ \psi]$

Where for formality:
- "**ROLL**" : always means a rotation along the $z$ axis
- "**PITCH**" : always means a rotation along the $y$ axis
- "**YAW**" : always means a rotation along the $x$ axis
> This are names that sailor uses for rotating the ships

###### ~ Examples of Euler Angles Rotations:
- **ZXZ** (Most used for the Euler Angles, *Standard for Euler Angles*): 
$$
R^O_{O \kern 1px '} = R_z(\varphi) \kern 1px R_x(\theta) \kern 1px R_z(\psi)
$$
- **ZYX** (Roll Pitch and Yaw):
$$
R^O_{O \kern 1px '} = R_z(\varphi) \kern 1px R_y(\theta) \kern 1px R_x(\psi)
$$
---
# RPY Angles
Specific Euler Angeles:
**ZYX** (Roll Pitch and Yaw):
$$
R^O_{O \kern 1px '} 
\kern 15px = \kern 15px 
R_{RPY}
\kern 15px \triangleq  \kern 15px 
R_z(\varphi) \kern 1px R_y(\theta) \kern 1px R_x(\psi)
$$
---
# Angle and Axis
![[Pasted image 20220303113439.png]]

$$
R(\theta, r) = R_z(\alpha) \kern 3px R_y(\beta) \kern 3px R_z(\theta) \kern 3px R_y(-\beta) \kern 3px R_z(-\alpha)
$$
Where:
$$
\theta = \cos^{-1}\left(\frac{r_{1,1} + r_{2,2} + r_{3,3} - 1}{2}\right)
$$
And:
$$
r = \frac{1}{2\sin(\theta)}
\left[
\begin{array}{c}
r_{3,2} - r_{2,3}
\\
r_{1,3} - r_{3,1}
\\
r_{2,1} - r_{1,2}
\end{array}
\right]
$$
- Where $r_{i,j}$ is the $i,j$ element of the Rotation Matrix $R$

So for $r_{1,1} + r_{2,2} + r_{3,3} = 1$ -> $\theta = 0$ -> $r = \infty$ (Indeterminate).
The Quaternion descriptor is more complicated but can avoid this problem

---
# Quaternion
There is **no** possibility that 2 different quaternions give the same final rotation.

Let's take an example: in the Angle and Axis descriptor formulas, we find that $\theta = \cos^{-1}\left(\frac{r_{1,1} + r_{2,2} + r_{3,3} - 1}{2}\right)$
Now if $r_{1,1} + r_{2,2} + r_{3,3} = 1$ then $\theta$ can be both equal to $0$ or $\pi$.

Let's now define $\eta$ and $\epsilon$ with respect to $\theta$ and $r$ as:
$$
\begin{align}
&\eta = \cos\left(\frac{\theta}{2}\right)
\\
&\epsilon = \sin\left(\frac{\theta}{2}\right)\cdot r
\end{align}
$$
Where $r$ is a vector ($3 \times 1$) so is $\epsilon$, while $\eta$ is a scalar ($1 \times 1$)

Notice that:
$$
\eta^2 + \epsilon_x^2 + \epsilon_y^2 + \epsilon_z^2 = 1
$$
And:
$$
\eta = \frac{1}{2} \sqrt{r_{1,1} + r_{2,2} + r_{3,3}}
$$
$$
\epsilon = 
\left[
\begin{array}{l}
sgn(r_{3,2}-r_{2,3}) \sqrt{1 + r_{1,1}- r_{2,2} -r_{3,3}}
\\
sgn(r_{1,3}-r_{3,1}) \sqrt{1 + r_{2,2}- r_{1,1} -r_{3,3}}
\\
sgn(r_{2,1}-r_{1,2}) \sqrt{1 + r_{3,3}- r_{1,1} -r_{2,2}}
\end{array}
\right]
$$
---
# Homogeneous Transformation Matrix
The pose of an object, then a frame could be represented in another one by one only matrix called **homogeneous transformation matrix**:

![[Pasted image 20220303162143.png|300]]

First I resolve the problem of position then the problem of orientation.
1. Solve the difference of $O$ and $O \kern 1px '$
2. Considering the $O$ and $O \kern 1px '$ in the same center i calculate the Rotation Matrix

So a **Pose** is just a collection of *Translation* and *Rotation*.

The Transformation Matrix that change one pose to another is denoted as $T$.
$$
T^O_{O \kern 1px '} = 
\left[
\begin{array}{cc}
\left[R^O_{O \kern 1px '}\right]_{3\times 3}
& 
\left[O \kern 1px '\right]_{3\times 1}
\\
\begin{array}{l}
0 & 0 & 0
\end{array} & 1
\end{array}
\right]_{4\times4}
$$
$$
p^{O \kern 1px '} = T_{O \kern 1px '}^O \cdot p^{O}
$$
The 3 zeros elements in the last row are usually unchanged but sometimes they do change, when they do it's because we want to impose the concept of prospective, for example when using a camera some dimensions are forcefully distorted (closer objects appear bigger).

 The last element $(4,4)$ is often $1$, but it can be changed to reference the scale of my robot or environment ($0.1$, $0.01$, $0.001$, ... when working with small robots, $10$, $100$, $1000$, $10000$ for big robots)