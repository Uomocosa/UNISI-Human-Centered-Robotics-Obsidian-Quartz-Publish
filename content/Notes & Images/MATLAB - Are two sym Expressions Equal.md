
[Original Source](https://it.mathworks.com/matlabcentral/answers/524675-test-equality-of-two-symbolic-expressions)

---

#### ~Example:
```matlab
eq1 = x(t) == -4*t
eq2 = y(t) == -4*t
isequal(rhs(eq1), rhs(eq2))
>> ans = 
	logical
	1


x = sin(a + b);
y = sin(a)*cos(b) + sin(b)*cos(a);

isequal(x, y)
>> ans = 
	logical
	0
	
isAlways(x==y)
>> ans =
	logical
	1
```