
[Documentation](https://it.mathworks.com/help/symbolic/sym.symfuntype.html)

---

#### ~Example:
```matlab
syms f(x)
expr = [f(x) sin(x) exp(x) int(f(x)) diff(f(x))]

% Determine the functional type of each array element.
s = symFunType(expr)
>> s = 
	1x5 string
    "f"    "sin"    "exp"    "int"    "diff"
```