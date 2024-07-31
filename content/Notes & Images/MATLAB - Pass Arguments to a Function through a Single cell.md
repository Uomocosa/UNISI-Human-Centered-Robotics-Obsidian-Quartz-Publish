```matlab
function myfun(arg1, arg2)
	disp(arg1);
	disp(arg2);
end

% Merged function call using a cell array.
mergedVariable = {1 'test'};
>> fun(mergedVariable{:})
ans = 
	1
	'Test'
```