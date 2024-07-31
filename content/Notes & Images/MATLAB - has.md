
[Documentation](https://it.mathworks.com/help/symbolic/sym.has.html)

---

> Check if expression contains particular subexpression

#### ~Example:
```matlab
syms x y z
has(x + y + z, z)

ans =
  logical
   1

has(x + y, z)

ans =
  logical
   0
```

```matlab
syms x
f = int(tan(x^7), x);
has(f, 'int')

ans =
	logical
		1
```