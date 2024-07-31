Simplest Approach:
```matlab
syms x(t) y(t) t a
dynamical_system = [
	diff(x,t) == a*x + 2
	diff(y,t) == -y
];

derivatives = findSymType(dynamical_system, 'diff');

>> derivatives
ans = 
	[diff(x(t),t), diff(y(t),t)]
```

---

My function:
```matlab
function [diff_terms] = find_differential_terms(dynamical_system)
	derivatives = findSymType(dynamical_system, 'diff');
	number_of_derivatives = size(derivatives,2);
	diff_terms = cell(number_of_derivatives,1);
	for i = 1 : number_of_derivatives
		diff_terms{i} = children(derivatives(i));
	end
end
```

Usage:
```matlab
syms x(t) y(t) t a
dynamical_system = [
	diff(x,t) == a*x + 2
	diff(y,t) == -y
];

diff_terms = find_differential_terms(dynamical_system);

>> diff_terms
ans = 
	{
		{x, t}
		{y, t}
	}
```