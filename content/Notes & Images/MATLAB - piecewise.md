
[Documentation](https://it.mathworks.com/help/symbolic/piecewise.html)

---

#### ~Example:
To define an expression like this:
![[Pasted image 20220111104519.png]]
You can use the `piecewise` command:
```matlab
syms x
y = piecewise(x < 0, 1,  x > 0, -1)
```

<br>
 
 Using otherwise:
![[Pasted image 20220111104717.png]]
```matlab
syms y(x)
y(x) = piecewise(x < -2,-2,(-2 < x) & (x < 0),0,1)
```