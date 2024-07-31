
Original Sources:
- ["Function Argument Validation" - MATLAB Official Docs](https://it.mathworks.com/help/matlab/matlab_prog/function-argument-validation-1.html)
---

Used in this file:
- 
---

~ Ex.:
```matlab
function myInterp(x,v,method)
    arguments
        x (1,:) {mustBeNumeric,mustBeReal}
        v (1,:) {mustBeNumeric,mustBeReal,mustBeEqualSize(x)}
        method (1,:) char {mustBeMember(method,{'linear','cubic','spline'})} = 'linear'
    end
    % Function code
    ....
end

% Custom validation function
function mustBeEqualSize(a,b)
    % Test for equal size
    if ~isequal(size(a),size(b))
        eid = 'Size:notEqual';
        msg = 'Size of first input must equal size of second input.';
        throwAsCaller(MException(eid,msg))
    end
end
```
---
# mustRespectTheFuckISay
MATLAB has a pretty way of declareing what an argument can and **can't** be, {mustBeText} {mustBeNumeric} ecc.

If you want to create a new mustBeSomething function above is the way to do it.