### Code:

```matlab
syms y(t) x(t) a

dynamical_system = [
	diff(x,t) == a*x
	diff(y,t) == -y
];

inital_conditions = [
	x(0) == 0.1
	y(0) == 0.2
];

solved_dynamical_system = dsolve(dynamical_system)
solved_complete_systems = dsolve(dynamical_system, inital_conditions)
```

### Output:

```matlab
solved_dynamical_system =
	[struct](matlab:helpPopup struct) with fields:
y: C1*exp(-t)
x: C2*exp(a*t)


solved_complete_systems =
	[struct](matlab:helpPopup struct) with fields:
y: exp(-t)/5
x: exp(a*t)/10
```

> Note:
> The variable "dynamical_system" is not seen as an array but as a single sym variable, so when i refer to dynamical_system(1), i would expect to get in output the first equation of the dynamic_system variable (diff(x,t) == a\*x) insted i get the system with t=1.
> 
> I dont like this matlab approach so i made a function to fix it:
> [[MATLAB - system_of_equation2array.m|system_of_equation2array]]