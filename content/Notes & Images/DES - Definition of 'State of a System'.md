###### Synthesis:
For a differentiable system, think of the State as the condition needed to solve the Cauchy problem (~ex.: $f'(0) = 3$, $f(0) = 5$, -> $\left[f'(0), \ f(0)\right]$ is the State of the System).

For a non-differentiable system, and more in **generale** the State is composed by all the conditions needed to calculate the **output** of the system given only the **inputs**.

---
### State of a System:
 The **state** of a system is the set of variables whose value at time $t_0$ is required in order to determine uniquely the output $y(t)$ for all $t\geq{}t_0$, given the input $u(t)$ for all $t\geq{}t_0$
 
 ---
 
 ###### ~Example: state of a capacitor system
 $v(t) = v(0) + \frac{1}{C}\int_{0}^{t} i(\tau{}) \,d\tau{}$

So the state is:
- $x = [v]$ 
- $y = [v]$
---
###### ~Example: determine the space needed to stop the car if one applies a constant breaking force $\vec{F}$
The system is: $s(t) = s(0) + \dot{s}(0)\,t - \frac{F}{M}\frac{t^2}{2}$

So the resulting state is: 
- $x = \begin{bmatrix}	s \\ 	\dot{s} \end{bmatrix}$
- $y = [s]$
--- 
