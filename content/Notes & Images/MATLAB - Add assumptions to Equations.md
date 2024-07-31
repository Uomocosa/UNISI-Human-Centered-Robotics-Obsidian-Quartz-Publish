### Code:

```matlab
syms y(t) x(t) a
assume([t, a], 'real')
assumeAlso(0 < a < 3)
assumptions
```

### Output:

```matlab
ans =  
[in(a, 'real'), in(t, 'real'), 0 < a, a < 3]
```