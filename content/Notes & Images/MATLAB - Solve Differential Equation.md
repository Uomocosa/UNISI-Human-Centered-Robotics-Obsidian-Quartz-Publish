### Code:

```matlab
syms x(t) a
differential_equation = diff(x,t) == a*x
initial_condition = x(0) == 1
complete_systems = [differential_equation, initial_condition]
solved_dynamical_system = dsolve(differential_equation)
solved_complete_systems = dsolve(complete_systems)
```

### Output:

```matlab
solved_dynamical_system =  
C1*exp(a*t)  

solved_complete_systems =  
exp(a*t)
```
