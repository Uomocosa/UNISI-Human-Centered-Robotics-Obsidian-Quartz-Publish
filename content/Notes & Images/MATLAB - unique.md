

```matlab
A = [1,5,2,3,4,1,2]
unique(A) %Will also sort the elements
>> ans = 
	[1,2,3,4,5]
```

#### Unsorted unique
```matlab
unique(A, 'stable')
```