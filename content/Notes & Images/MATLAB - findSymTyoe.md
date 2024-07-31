
[Documentation](https://it.mathworks.com/help/symbolic/sym.findsymtype.html)

---

#### ~Example:
```matlab
syms y(t) k
eq = diff(y) + k*y == sin(y);
X = findSymType(eq,'variable');

>> X
ans = 
	{k t}
	
X = findSymType(eq,'symfun')

>> X
ans = 
	{y(t)}
	
X = findSymType(eq,'diff')

>> X
ans = 
	{diff(y(t),t)}
```