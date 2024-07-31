# Human Eye
Retina measures about $5 \times 5$ cm$^2$  and contains $10^8$ sampling elements (roots and cones).
- Spectral resolution $\sim 0.01$° over a $150$° field of view (NOT evenly distributed)
- $11$ bit/element, $10$ Hz resolution

-> Resulting in a total of $3$ GB/s (considering both eyes)

# Camera
The cameras of today only archive information up to a rate of $12$MB/s (hundreds of times less than the human eye)

To get a 3d effect we use 2 cameras (one per eye) which project different 2D images, the brain does the rest.

![[Pasted image 20220329100633.png]]

---
# Cinema 3D
![[Pasted image 20220329100700.png]]

Using special lenses one eye sees one screen and the other eye another screen, showing different positions for the same object creates the sense of dept.

Same for virtual reality headsets (instead of special lenses it uses 2 lenses to project 2 different images)

---
# Screen and Lenses
- **Dolby 3D** systems (red and blue lenses) \[Color Filters\]
- **Real D** systems \[Polarizing Filters\]
- **Xpand 3D** systems \[Eclipse Method\] (Expensive but very good performance)

---
# Augmented Reality
Using special cameras (even a phone is sufficient) I can see 3D virtual objects in the real world.

---
# Mathematics
Differential Equations
-> **ODE** (Ordinary Differential Equation)
$$
\dot x = f(x,t)
$$
Need to keep the computation faster as possible, the allowed delays are up to some *milliseconds*, in case of haptic.
- **Euler's Method** (1st order approximation)
- **Mid Point Method** (2nd order approximation)

>**NOTE**:
> 1 diff. eq. of order 2 can be splitted to 2 diff. eq.s of order 1:
> $$
\begin{array}{l}
I \ddot \Theta(t) + \beta \dot \Theta(t) = \tau(t)
\\
\\
\Rightarrow \left(
\begin{array}{l}
x_1
\\
x_2
\end{array}
\right)

= \left(
\begin{array}{l}
\Theta
\\
\dot \Theta 
\end{array}
\right)
\\
\\
\Rightarrow 
\left\{
\begin{array}{l}
\dot x_1(t) = x_2(t)
\\
I\dot x_2(t) + \beta x_2(t) = \tau(t)
\end{array}
\right.

\\
\\
\Rightarrow 
\left[
\begin{array}{l}
\dot x_1
\\
\dot x_2
\end{array}
\right]
=
\left[
\begin{array}{cc}
0 & 1
\\
0 & -\Large\frac{\beta}{I}
\end{array}
\right]
\left[
\begin{array}{l}
x_1
\\
x_2
\end{array}
\right]
+
\left[
\begin{array}{c}
0
\\
\Large\frac{1}{I}
\end{array}
\right]
\tau(t)
\end{array}
$$
> System of 2 differential eq.s of order 1

So given a differential equation of order 2 we can write in Matrix form:
$$
\dot{\overline{x}}(t) = \overline{\overline{A}} \overline x(t) +  \overline{B} \tau(t)
$$

---
# Discrete Time
The computer works step, by step (discrete time)

![[Pasted image 20220329102645.png]]

Mathematical description of the system:
$$
\overline X(t) = f(X(t),t)
$$
(~ex.: eq. to describe the motion of my shoulder)

$\overline X(t_0)$ := **STATE OF THE SYSTEM**

I can find $\overline X(t_0 + h)$ using the mathematical description of the system

> **NOTE**:
> If i have to describe a system that has only to be seen by a human, my speed (frame rate) has to be above 20 Hz
> If you also have to give the sense of touch it has to increase above 1k Hz
> 
> -> **VISION** $> 20$ Hz
> -> **TOUCH** $> 1k$ Hz

---
# Euler's Method
$$
\overline X(t_0 + h) \simeq \overline{X}(t_0) + h \dot {\overline{X}}(t_0)
$$
Good method but a little unstable, if $h$ is too big the system does not behave properly.

###### ~Ex.:
![[Pasted image 20220329103405.png]]

---
# Mid Point Method
$$
x(t_0 + h) = x(t_0) + h \dot x(t_0) + \frac{h^2}{2}\ddot x(t_0)
$$
- $\dot x(t_0) = f(x(t),t)$
-> $x(t_0) = hf(x(t_0),t_0) + \frac{h^2}{2}\dot f(x(t_0),t_0)$ 
- I dont want to compute the derivative of $f(x(t_0),t_0)$

-> So we want the result of $\ddot x(t_0)$ using only $x(t_0)$ and $f(x(t),t)$, so we can:
![[Pasted image 20220329103943.png]]
![[Pasted image 20220329104000.png]]
![[Pasted image 20220329104017.png]]

Resulting in: **Mid Point Method**
$$
x(t_0+h) = x(t_0) + hf(x_0 + \frac{h}{2}f(x_0))
$$
---