
[Documentation](https://it.mathworks.com/help/matlab/ref/arguments.html)
[Function Argument Validation](https://it.mathworks.com/help/matlab/matlab_prog/function-argument-validation-1.html#mw_7e4fb227-d0ac-463d-b389-b2d2bb36d689)

---

#### Restrict Size and Type of Input
```matlab
function [m,s] = twoStats(x)
    arguments
        x (1,:) {mustBeNumeric}
    end
    m = mean(x,"all");
    s = std(x,1,"all");
end
```

<br>

#### Define Name-Value Arguments
```matlab
function myRectangle(X,Y,options)
    arguments
       X double
       Y double
       options.LineStyle (1,1) string = "-" 
       options.LineWidth (1,1) {mustBeNumeric} = 1
    end
    % Function code
    ...
end
```

```matlab
% THIS ARE ALL VALID
myRectangle(4,5)
myRectangle(4,5,LineStyle=":",LineWidth=2)
myRectangle(4,5,LineWidth=2,LineStyle=":")
myRectangle(4,5,LineStyle=":")
myRectangle(4,5,LineWidth=2)
```

> Or how i liked to do it:
> ```matlab
> function myRectangle(X,Y,LineStyle,LineWidth)
>    arguments
>       X double
>       Y double
>       LineStyle.LineStyle (1,1) string = "-" 
>       LineWidth.LineWidth (1,1) {mustBeNumeric} = 1
>    end
>    %% simplify name-value arguments:
>    LineStyle = LineStyle.LineStyle
>    LineWidth = LineWidth.LineWidth
>    %% Function code
>    ...
>end
> ```
> NOTE: not too useful, but it works nontheless