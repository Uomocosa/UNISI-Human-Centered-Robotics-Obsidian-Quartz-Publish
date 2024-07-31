# Minimum Distance Point-Surface
![[Pasted image 20220328145142.png]]

It's easy to know if you are "in" or "out" of a single **plane**
- Knowing your position $\bar x_a$ ($a$: avatar) or $\bar x_h$ ($h$: haptic point), and the formula of the plane: $ax + by+ cz +d$ we can calculate:
$$
ax_{ax} + bx_{ay}+ cx_{az} +d
$$
and define as "in" if the result is $\lt 0$ or "out" if the result is $\gt 0$.

![[Pasted image 20220328145201.png]]

---
# Algorithm
Given $x_h$ haptic point (same as $x_a$ just a different name):
$$
x_h = \ <x_{hx}, \ x_{hy}, \ x_{hz}>
$$
the minimum distance from the place $\Sigma$ ($ax + by + cz +d = 0)$ can be computed as the distance of $x_h$ from $x_p$ ($p$: proxy) where $x_p$ is defined as the projection of $x_h$ onto $\Sigma$.

![[Pasted image 20220328150152.png]]

---
### Optimization Problem
We can also see this as an optimization problem:
$$
\begin{array}{l}
\min ||x_p - x_h||
\\
x_p \in \Sigma
\end{array}
$$
Then:
$$
\begin{array}{l}
||x_p - x_h|| = \sqrt{(x_p - x_h)^2}
\\
\\
\begin{array}{l}
\Rightarrow \min ||x_p - x_h|| &= \min(x_p -x_h)^2
\\
&\ |
\\
& = \min(x_p -x_h)^2
\\
&\ |
\\
& = \alpha \cdot \min(x_p -x_h)^2 , \kern 10px \alpha > 0
\end{array}
\end{array}
$$
-> We can reformulate the problem as searching for:
$$
\min \frac{1}{2} (x_p -x_h)^2 
$$
Being vectors $x_p$ and $x_h$ we can write:
$$
\min \frac{1}{2} (x_p -x_h)(x_p -x_h)^T
$$
And also we rewrite the constraint: $x_p \in \Sigma$, ($ax + by + cz +d = 0$) as:
$$
[a, b, c] \cdot x_p + d = 0
$$
Then the problem becomes:
$$
\begin{array}{l}
\min \frac{1}{2} (x_p -x_h)(x_p -x_h)^T
\\
[a, b, c] \cdot x_p + d = 0
\end{array}
$$

### Lagrangian Approach:
Using the [[HCR - Lagrangian Theorem]] we can rewrite the problem as:
$$
Q(x_p, \lambda) = \frac{1}{2}(x_p - x_h)(x_p - x_h)^T + \lambda^T \cdot \left([a,b,c] \cdot x_p + d\right)
$$
and search for its minimum, so:
$$
(x_p, \lambda): 
\left\{
\begin{array}{l}
\Huge \frac{\partial Q(x_p, \lambda)}{\partial x_p} \normalsize = 0
\\[5px]
\Huge \frac{\partial Q(x_p, \lambda)}{\partial \lambda} \normalsize = 0
\end{array}
\right.
$$
Then we have:
$$
(x_p, \lambda): 
\left\{
\begin{array}{l}
(x_p - x_h) + \lambda^T \cdot [a,b,c] = 0
\\[5px]
[a,b,c]\cdot x_p + d = 0
\end{array}
\right.
$$
So, with a bit of substitutions we obtain:
$$
x_p = - \frac{[a,b,c]}{||[a,b,c]||^2}\cdot d
$$
---
# Triangular Meshes
![[Pasted image 20220328152827.png]]

We can create a plane with 3 points (~ex.: $T_1$: triangle 1, formed by $x_1,\  x_2, \ x_3$)
- So given the triangle $T_1$ we can use the previous formula to calculate the minimum distance $x_h$ from $T_1$.

![[Pasted image 20220328153128.png]]

So I can receive an haptic feedback proportional to the distance $\overline{x_h \ x_p}$ 
- For a smooth object there are no problem with this approach.

---
# Spigolar Objects
![[Pasted image 20220328153353.png]]

Notice how for a small displacement of $x_h$ the **direction** of the Force changes drastically.

---
# Proxy Algorithm
- **IDEA**: Remember where you entered from.

1. In case of collision, for the first time @ $t_k = 0$ (-> $x_h(0)$) we compute the normal proxy and we take the tangent circle for the proxy $x_p$ given a small radius $\epsilon$ (in the figure below $C_p(0)$)
![[Pasted image 20220328153658.png]]

2. Then given the haptic point @ $t_k = 1$ -> $x_h(1)$ we find which triangle in my triangular mesh is "**ACTIVE**"
The **ACTIVE** triangle is the one that intersect the segment $\overline{x_h(k)C_p(k-1)}$
![[Pasted image 20220328153926.png]]

Let's see how this proxy algorithm changes things:
![[Pasted image 20220328154125.png]]
- In the new case the proxy cannot change triangle so easily, so it results in a more **smooth** experience.

###### How do we change triangle with the new algorithm?
Let's take for example the following passages:

![[Pasted image 20220328154317.png]]

As we can see there is a small error for $C_p(1)$ but it's accepted.
And for $C_p(2)$ we have indeed changed triangle, now the second triangle is **active**.

---
# Friction Cone
A way to visualize **friction**
![[Pasted image 20220328154550.png]]

The friction cone depends on the $F_D$ (Force Down-ward) and $\mu$ the friction coefficient.

![[Pasted image 20220328154655.png]]

---
# Proxy Algorithm with Friction Cones:
![[Pasted image 20220328154737.png]]

If $x_h(k+1) doesn't escape the friction cone of $C_p(k)$ then:
$$
C_p(k+1) = C_p(k)
$$
- The proxy **does not move**.

---
# Static and Kinematic Friction
Each material interaction has 2 friction coefficients one static ($\mu_s$) and one kinematic ($\mu_d$), the first is to break the stacity and the second to determine the friction force that slows down the motion.

~ Example:
wood on wood: $\mu_s = 0.25 \sim 0.5$,  $\mu_d = 0.2$
glass on glass: $\mu_s = 0.94$,  $\mu_d = 0.4$
sky on dry snow: $\mu_s \simeq 0$,  $\mu_d = 0.04$

When the object is moving and $\mu_s >> \mu_s$ (usually true) we approximate the static friction coefficient $\mu_s$ to 0, so we do not need to calculate it, so $\Omega_d = \tan^{-1}(\mu_d)$

---