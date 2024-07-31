
[Documentation](https://it.mathworks.com/help/symbolic/symvar.html)

---

> Find symbolic variables in symbolic input

```matlab
syms wa wb yx ya
sum = wa + wb + ya + yx;
symvar(sum)

ans =
	[ wa, wb, ya, yx]
```