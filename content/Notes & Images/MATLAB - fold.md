
[Documentation](https://it.mathworks.com/help/symbolic/fold.html)

---

 MATLAB equivalent of [[Python - reduce]]
 
 #### ~Example:
 ```matlab
syms a b c d e
>> fold(@power, [a b c d e])
ans =
	(((a^b)^c)^d)^e
```