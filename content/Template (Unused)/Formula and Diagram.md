[Wikipedia](https://en.wikipedia.org/wiki/Exponential_distribution)
 
---
# Exponential Distribution:
## PDF
"Probability Density Function"
![[Pasted image 20220121161749.png]]
### Formula:
$$
\Large 
f_x(t) = \left\{
\begin{array}{ccl}
	\lambda e^{-\lambda t} & \text{if} \space t \ge 0
	\\
	0 & otherwise
\end{array}
\right.
$$

---
## CDF
"Cumulative Distribution Function"
![[Pasted image 20220121161809.png]]
### Formula:
$$
\Large 
F_x(t) = \left\{
\begin{array}{ccl}
	1 - \lambda e^{-\lambda t} & \text{if} \space t \ge 0
	\\
	0 & otherwise
\end{array}
\right.
$$

---
### Notes:
- Notation: $\sim Exp(\frac{1}{\lambda})$
- Parameters: $\lambda \gt 0$ 
- Support $x \in [0, \infty)$
- Mean: $\frac{1}{\lambda}$
- Median: $\frac{ln\,2}{\lambda}$
- Variance: $\frac{1}{\lambda ^2}$
- The CDF is the differentiate of the PDF in respect to time:
$$
f_x(t) = \frac{dF_x(t)}{dt}
$$

---
