
[Documentation](https://it.mathworks.com/help/symbolic/sym.children.html)

---

> Find subexpression of an equation or formula.

#### ~Example:
```maltab
syms x y
subexpr = children(x^2 + x*y + y^2)
>> subexpr =
	1×3 cell array
    	{[x*y]}    {[x^2]}    {[y^2]}

s1 = subexpr{1}
>> s1 = 
	x y
```