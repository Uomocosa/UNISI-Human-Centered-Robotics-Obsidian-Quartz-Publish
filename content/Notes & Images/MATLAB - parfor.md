
Original Sources:
- ["parfor" - MATLAB Official Docs'](https://it.mathworks.com/help/parallel-computing/parfor.html)
---

Used in this file:
- 
---

~ Ex.:
```matlab
M = 0;                     % M specifies maximum number of workers
 y = ones(1,100);
 parfor (i = 1:100,M)
      y(i) = i;
 end
```
---
# Parallel For
Use the power of all your PC'cores to do a tedious task