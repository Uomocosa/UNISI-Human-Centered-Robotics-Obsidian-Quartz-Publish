
[Documentation](https://it.mathworks.com/help/symbolic/syms.html)

---


# ~Examples:
#### Create 1 or more symbolic variables:
```matlab 
syms a b c
```

#### Create a symbolic Function:
```matlab
syms x(t) t
equation = x(t) == 4*t^2
```

#### Create n variables:
```matlab
syms a [1 n]
```

#### Create a Symbolic Matrix:
```matlab
syms A [2 4] matrix
```

#### Set Assumptions
```matlab
syms a 
assume(a, 'real')
assumeAlso(0 < a < 3)
```

#### Create a derivate:
```matlab
syms x(t) t
equation = diff(x(t),t) == 8*t
```

#### Simplify solution of an equation:
```matlab
syms x(t) t
>> simplify(x^2 + 2*x + 1)
ans =
	(x(t) + 1)^2	
```