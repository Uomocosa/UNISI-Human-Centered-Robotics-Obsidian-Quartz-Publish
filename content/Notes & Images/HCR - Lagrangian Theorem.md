### Lagrangian Theorem
Given a minimization problem, with constraints such that every constraint is an *equation* (not an inequality):
$$
\begin{array}{l}
\min z = a_o + a_1x_1 + a_2x_2 + \ldots
\\
x_{i1} + x_{k1} + \ldots = h_1
\\
\vdots
\\
x_{im} + x_{km} + \ldots = h_m
%\\
%x_{i(m+1)} + x_{k(m+1)} + \ldots \lt q_1
%\\
%\vdots
%\\
%x_{i(m+n)} + x_{k(m+n)} + \ldots \lt q_n
\end{array}
$$
We can construct a new minimization problem without constraints, such that the solution of the first problem is the same as that of the second problem:
$$
\begin{array}{l}
\min &\bar z =& a_o + a_1x_1 + a_2x_2 + \ldots +
\\
&& + \lambda_1(x_{i1} + x_{k1} + \ldots - h_1) 
\\
&& \vdots
\\
&& +  \lambda_m(x_{im} + x_{km} + \ldots - h_m)
\end{array}
$$
-> So to find the minimum of the $\bar z$ function we can simply resolve the following system:
$$
(\bar x, \bar \lambda): 
\left\{
\begin{array}{l}
\Huge \frac{\partial Q(\bar x,\bar  \lambda)}{\partial x_1} \normalsize = 0
\\[5px]
\Huge \frac{\partial Q(\bar x,\bar  \lambda)}{\partial x_2} \normalsize = 0
\\
\vdots
\\
\Huge \frac{\partial Q(\bar x,\bar  \lambda)}{\partial x_m} \normalsize = 0
\\[5px]
\Huge \frac{\partial Q(\bar x,\bar  \lambda)}{\partial \lambda_1} \normalsize = 0
\\[5px]
\Huge \frac{\partial Q(\bar x,\bar  \lambda)}{\partial \lambda_2} \normalsize = 0
\\
\vdots
\\
\Huge \frac{\partial Q(\bar x,\bar  \lambda)}{\partial \lambda_m} \normalsize = 0
\end{array}
\right.
$$
