
Original Sources:
- ["How to sort a structure array based on a specific field" - MATLAB Asnwers](https://it.mathworks.com/matlabcentral/answers/397385-how-to-sort-a-structure-array-based-on-a-specific-field)
---

Used in this file:
- 
---

~ Ex.:
```matlab
% suppose 's' is the struct array. 'DOB' is the field that contains date and time.
T = struct2table(s); % convert the struct array to a table
sortedT = sortrows(T, 'DOB'); % sort the table by 'DOB'
sortedS = table2struct(sortedT) % change it back to struct array if necessary
```
---
