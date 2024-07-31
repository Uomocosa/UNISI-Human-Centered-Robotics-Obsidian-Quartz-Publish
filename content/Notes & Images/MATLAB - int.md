
[Documentation](https://it.mathworks.com/help/symbolic/sym.int.html)

---

> Symbolic Integration

#### ~Example:
```matlab
syms x
expr = -2*x/(1+x^2)^2;

% Find the indefinite integral of the univariate expression.

F = int(expr)
>> F = 
	1/(x^2 + 1)

```

```matlab
% Find the finite integral of the univariate expression.

syms x
expr = x*log(1+x);
F = int(expr,[0 1])

>> F = 
	1/4
```

```matlab
syms x
f = cos(x)/sqrt(1 + x^2);
Fint = int(f,x,[0 10])
```
![[Pasted image 20220111112250.png]]
```matlab
Fvpa = vpa(Fint)
>> Fvpa = 
	0.37570628299079723478493405557162
```

---

To approximate integrals directly, use [[MATLAB - vpaintegral|vpaintegral]] instead of `vpa`. The `vpaintegral` function is faster and provides control over integration tolerances.
```matlab
Fvpaint = vpaintegral(f,x,[0 10])
>> Fvpaint =
	0.375706
```