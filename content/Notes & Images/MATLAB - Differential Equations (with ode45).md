
[Documentation](https://it.mathworks.com/help/matlab/math/differential-equations.html)

---

#### ~Example:
![[Pasted image 20220111094615.png]]
```matlab
function dydt = vanderpoldemo(t,y,Mu)
	dydt = [y(2); Mu*(1-y(1)^2)*y(2)-y(1)];
end

tspan = [0 20];
% intial conditions y(0) = 2, dy_dt(0) = 0, Mu = 1
y0 = [2; 0];
Mu = 1;
ode = @(t,y) vanderpoldemo(t,y,Mu);
[t,y] = ode45(ode, tspan, y0);

% Plot solution
plot(t,y(:,1))
xlabel('t')
ylabel('solution y')
title('van der Pol Equation, \mu = 1')
```
![[Pasted image 20220111094542.png]]