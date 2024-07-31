
[Documentation](https://it.mathworks.com/help/symbolic/vpaintegral.html)

---

#### ~Example:

To approximate integrals directly, use `vpaintegral` instead of `vpa`. The `vpaintegral` function is faster and provides control over integration tolerances.

```matlab
Fvpaint = vpaintegral(f,x,[0 10])
>> Fvpaint =
	0.375706
```