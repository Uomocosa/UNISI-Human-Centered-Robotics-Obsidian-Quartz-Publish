 Documentation
 
 ---
 
 #### ~Example:
 ```matlab
 classdef BasicClass
   properties
      Value {mustBeNumeric}
   end
   methods
      function r = roundOff(obj)
         r = round([obj.Value],2);
      end
      function r = multiplyBy(obj,n)
         r = [obj.Value] * n;
      end
   end
end
 ```
 
 ```matlab
 a = BasicClass
 a.Value = pi/3;
 roundOff(a) == a.roundOff()
 a.multiplyBy(3) == multiplyBy(a,3)
 ```
 
 ---
 
 #### Constructor:
 ```matlab
 classdef BasicClass
   properties
      Value {mustBeNumeric}
   end
   
   methods        
    function obj = BasicClass(val)
        if nargin == 1
            obj.Value = val;
        end
    end
end
 ```
 
 ---
 
 #### Overload Functions
 ```matlab
 method
   function r = plus(o1,o2)
      r = [o1.Value] + [o2.Value];
   end
end
```