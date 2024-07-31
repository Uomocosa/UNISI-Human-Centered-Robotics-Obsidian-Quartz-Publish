
[Documentation](https://it.mathworks.com/help/matlab/matlab_prog/function-argument-validation-1.html)
[[MATLAB - arguments]]

---

#### ~Example:
```matlab
function [] = porva(a,b,opt)
	arguments
		a (1,1) double
		b (2,3) double
		opt.c (1,1) string = "c was passed"
		opt.d (1,1) string = "d was passed"
	end

	%% Actual Function
	disp(class(a))
	disp(class(b))
	disp(class(c))
end
```

```matlab
% All of this will work
porva(1,2)
porva(1,2, "c","JKOJDOIO")
porva(1,2, "d","HOHUO")
porva(1,2, "c","porva","d","poooorva")
```

