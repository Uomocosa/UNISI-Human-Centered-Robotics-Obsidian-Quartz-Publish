
[Documentation](https://it.mathworks.com/help/symbolic/sym.symtype.html)

---

#### ~Example:
```matlab
a = sym('3/9');
s = symType(a)

>> s = 
	"rational"
```

```matlab
syms f(x)
s = symType(f)

>> s = 
	"symfun"
```

```matlab
f(x) = x^2;
s = symType(f)

>> s = 
	"expression"
```

```matlab
f(x) = x;
s = symType(f)

>> s = 
	"variable"
```