### Code:

```matlab
>> mystruct
ans = 
	Struct with fields:
		x = 1
		y = 2

>> fn = fieldnames(mystruct);
ans = 
	{x, y}

>> mystruct.(fn{1})
ans = 
	1
```