
[Documentation](https://it.mathworks.com/help/matlab/matlab_oop/example-representing-structured-data.html#:~:text=Objects%20as%20Data%20Structures,-This%20example%20defines&text=A%20MATLAB®%20struct%20with,on%20that%20data%20(methods).)

---

#### ~Example:
```matlab
classdef TensileData
   properties
      Material
      SampleNumber
      Stress
      Strain
      Modulus
   end
end
```

---

#### Add Input Restrictions:
```matlab
classdef TensileData
   properties
      Material string
      SampleNumber (1,1) double
      Stress
      Strain
      Modulus
   end
end
