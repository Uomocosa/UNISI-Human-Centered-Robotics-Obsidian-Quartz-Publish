```matlab
A = [1,2,3]; B = [4,5];
[m,n] = ndgrid(A,B);
Z = [m(:),n(:)]

>> Z =
	1 4
	2 4
	3 4
	1 5
	2 5
	3 5
```