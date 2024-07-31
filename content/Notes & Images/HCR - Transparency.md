# Transparency
- $Z_E$: impedance of **virtual environment**
- $Z_R$: impedance of the **robot**
![[Pasted image 20220328163959.png]]

I want to simulate an $F_v(s)$ so given the $x_h$ we can have:
$$
F_v(s) = Z_E(s) \cdot \Large \dot{\normalsize X}\normalsize(s)
$$
For this particular robot the only way to give a force feedback is to apply a torque so:
$$
\tau = J^{-1} \cdot F
$$
where $J$ is the Jacobian Matrix.
But there are 2 torques to be summed: the torque of motor $\tau_m$ and that of the human $\tau_h$

![[Pasted image 20220328164321.png]]

Then the torque will be:
$$
\begin{array}{r}
\\
\\
\\
Z_R(s) := Is + B \rightarrow
\\
\\
\end{array}

\begin{array}{l}
\tau(s)&= Is\dot \Theta(s) + B \dot \Theta(s)
\\
& \ |
\\
&= (Is + B)\cdot \dot \Theta(s)
\\
& \ |
\\
&= Z_R(s)\cdot \dot \Theta(s)
\end{array}
$$

Also remember that:
$$
\begin{array}{l}
\tau = J^T \cdot F
\\
\Large \dot{\normalsize X}\normalsize _h (s) = J \cdot \Large \dot{\normalsize X}\normalsize
\end{array}
$$
Then:
$$
\begin{array}{l}
\ \ \ddot x = J \cdot \ddot \Theta
\\
\ \ \ddot \Theta = J^T \cdot \ddot x
\end{array}
$$

What is really felt by the human is the Force of the human itself $F_h$ and the velocity $\Large \dot{\normalsize X}\normalsize(s)$ which is controlled by both $\tau_h$ and $\tau_m$ ->
$$
F = Z_p(s) \cdot \Large \dot{\normalsize X}\normalsize _h \cdot \frac{1}{s}
$$
where $Z_p(s)$ is the impedance **perceived** by the human.
![[Pasted image 20220328165717.png]]

And:
![[Pasted image 20220328165734.png]]