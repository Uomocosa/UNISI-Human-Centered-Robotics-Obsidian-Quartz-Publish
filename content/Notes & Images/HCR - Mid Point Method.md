---
aliases:
  - Mid Point Method
---
***Formula*** (not the final one, read at the end):$$ x(t_0 + h) = x(t_0) + h \dot x(t_0) + \frac{h^2}{2}\ddot x(t_0) $$Where:
- $\dot x(t_0) = f(x(t),t)$<br>⇒ $x(t_0) = hf(x(t_0),t_0) + \frac{h^2}{2}\dot f(x(t_0),t_0)$ 

==I dont want to compute the derivative over time of $f(x(t_0),t_0)$==;<br>⇒ So we want the result of $\ddot x(t_0)$ using only $x(t_0)$ and $f(x(t),t)$, so we can:
![[Pasted image 20220329103943.png]]
![[Pasted image 20220329104000.png]]
![[Pasted image 20220329104017.png]]

Resulting in: **Mid Point Method**: $$ x(t_0+h) = x(t_0) + hf(x_0 + \frac{h}{2}f(x_0)) $$
