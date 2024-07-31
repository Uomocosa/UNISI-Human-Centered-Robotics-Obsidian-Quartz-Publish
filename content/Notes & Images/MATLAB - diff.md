
[Documentation](https://it.mathworks.com/help/symbolic/diff.html)

---

> Symbolic Derivative

#### ~Example:
```matlab
syms f(x)
f(x) = sin(x^2);
Df = diff(f,x)

>> Df 
ans = 
	2*cos(x^2)
	
>> Df(2)
ans = 
	4*cos(4)

>> double(Df(2))
ans = 
	-2.6146
```

<br>

#### ~Derivates above the first:
```matlab
syms f(x)
f(x) = sin(x^2);
>> diff(f,x,x)
ans = 
	-4*sin(x^2)
```