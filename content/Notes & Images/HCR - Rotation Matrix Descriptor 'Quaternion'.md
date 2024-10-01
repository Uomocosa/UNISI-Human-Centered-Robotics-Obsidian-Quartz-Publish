---
aliases:
  - quaternion
---
> ***NOTE***: #IMPORTANTE 
> ==There is **no** possibility that 2 different quaternions give the same final rotation.==

Let's take an example: in the [[HCR - Rotation Matrix Descriptor 'Angle and Axis'|angle and axis]] descriptor formulas, we find that:
$$
\theta = \cos^{-1}\left(\frac{r_{1,1} + r_{2,2} + r_{3,3} - 1}{2}\right)
$$
Now if we consider $r_{1,1} + r_{2,2} + r_{3,3} = 1$ then $\theta$ can be both equal to $0$ or $\pi$, so we have and *indetermination* on the angle.

Let's now define $\eta$ and $\epsilon$ with respect to $\theta$ and $\vec v$ as:$$\begin{align} &\eta = \cos\left(\frac{\theta}{2}\right) \\[7px] &\varepsilon = \sin\left(\frac{\theta}{2}\right)\cdot \vec v \end{align} $$Where:
- $\vec v$ is a vector ($3 \times 1$) and so is $\varepsilon$.
- While $\eta$ is a scalar ($1 \times 1$).

Notice that:$$\eta^2 + \varepsilon_x^2 + \varepsilon_y^2 + \varepsilon_z^2 = 1$$And:$$ \begin{array}{c} \eta = \frac{1}{2} \sqrt{r_{1,1} + r_{2,2} + r_{3,3}} \\[10px] \varepsilon =  \left[ \begin{array}{l} \operatorname{sign}(r_{3,2}-r_{2,3}) \sqrt{1 + r_{1,1}- r_{2,2} -r_{3,3}} \\ \operatorname{sign}(r_{1,3}-r_{3,1}) \sqrt{1 + r_{2,2}- r_{1,1} -r_{3,3}}
\\ \operatorname{sign}(r_{2,1}-r_{1,2}) \sqrt{1 + r_{3,3}- r_{1,1} -r_{2,2}} \end{array} \right] \end{array}$$So by using $\eta$ and $\varepsilon$ as **constraints** we can then find the rotation matrix $R$ :
$$
R = 
\left[
\begin{array}{l}
r_{1,1} & r_{1,2} & r_{1,3}
\\
r_{2,1} & r_{2,2} & r_{2,3}
\\
r_{3,1} & r_{3,2} & r_{3,3}
\end{array}
\right]
$$
---
# Quaternions re-explained
(As everyone knows them)
- [Youtube - 'Quaternions and 3d rotation, explained interactively' by '3Blue1Brown'](https://www.youtube.com/watch?v=zjMuIxRvygQ)

Given a point $\overline p$ an axis of rotation $\overline v$ and the 2 angles of rotation $\theta$ and $\varphi$ we can define:
$$
q = \left(
	\cos\left(
		\theta \over 2
	\right) +
	\sin\left(
		\varphi \over 2
	\right)
\right)  \ \cdot \ 
\Large(
	\normalsize
	\overline v \cdot [i, \ j, \ k]
\Large)
$$
Where:
- $i^2 = j^2 = k^2 = ijk = -1$

So once we have defined $q$ the new point $\overline{p}'$ location after the rotation is given by:
$$
\overline p ' = q \cdot p \cdot q^{-1}
$$
Where:
$$
\begin{array}{l}
\text{if:} \kern 10px & q &= w_0 + x_0i + y_0j + z_0k
\\
\text{then:} \kern 10px & q^{-1} &= w_0 - x_0i - y_0j - z_0k
\end{array}
$$
