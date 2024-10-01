---
aliases:
  - System of Ordinary Differential Equations
---
Differential Equations
-> **ODE** (Ordinary Differential Equation)
$$
\dot x = f(x,t)
$$
Need to keep the computation faster as possible, the allowed delays are up to some *milliseconds*, in case of haptic.
- **Euler's Method** (1st order approximation)
- **Mid Point Method** (2nd order approximation)

---
**NOTE**:
1 diff. eq. of order 2 can be splitted to 2 diff. eq.s of order 1:
$$
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
System of 2 differential eq.s of order 1

---
So given a differential equation of order 2 we can write in Matrix form:
$$
\dot{\overline{x}}(t) = \overline{\overline{A}} \overline x(t) +  \overline{B} \tau(t)
$$
