```matlab
function [equations] = system_of_equation2array(system_of_equation)
	equations_divided_in_cells = children(system_of_equation);
	number_of_equations = size(equations_divided_in_cells,1);
	equations = sym(zeros(number_of_equations,1));
	for i = 1 : number_of_equations
		lhs_of_equation_i = equations_divided_in_cells{i}{1};
		rhs_of_equation_i = equations_divided_in_cells{i}{2};
		equations(i) = lhs_of_equation_i == rhs_of_equation_i;
	end
end
```

### Usage:
```matlab
syms x(t) y(t) t a
dynamical_system = [
	diff(x,t) == a*x
	diff(y,t) == -y
];

% BEFORE:
>> dynamical_system(1)
ans =
	subs(diff(x(t), t), t, 1) == a*x(1)  
	subs(diff(y(t), t), t, 1) == -y(1)

% AFTER:
dynamical_system = system_of_equation2array(dynamical_system);

>> dynamical_system(1)
ans = 
	diff(x(t), t) == a*x(t)
```
