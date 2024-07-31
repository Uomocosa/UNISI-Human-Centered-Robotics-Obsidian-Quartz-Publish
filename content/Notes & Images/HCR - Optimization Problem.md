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