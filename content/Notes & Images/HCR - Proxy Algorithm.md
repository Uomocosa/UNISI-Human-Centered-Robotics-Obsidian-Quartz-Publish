# Spigolar Objects
![[Pasted image 20220328153353.png]]

Notice how for a small displacement of $x_h$ the **direction** of the Force changes drastically.

---
# Proxy Algorithm
- **IDEA**: Remember where you entered from.

1. In case of collision, for the first time @ $t_k = 0$ (-> $x_h(0)$) we compute the normal proxy and we take the tangent circle for the proxy $x_p$ given a small radius $\epsilon$ (in the figure below $C_p(0)$)
![[Pasted image 20220328153658.png]]

2. Then given the haptic point @ $t_k = 1$ -> $x_h(1)$ we find which triangle in my triangular mesh is "**ACTIVE**"
The **ACTIVE** triangle is the one that intersect the segment $\overline{x_h(k)C_p(k-1)}$
![[Pasted image 20220328153926.png]]

Let's see how this proxy algorithm changes things:
![[Pasted image 20220328154125.png]]
- In the new case the proxy cannot change triangle so easily, so it results in a more **smooth** experience.

###### How do we change triangle with the new algorithm?
Let's take for example the following passages:

![[Pasted image 20220328154317.png]]

As we can see there is a small error for $C_p(1)$ but it's accepted.
And for $C_p(2)$ we have indeed changed triangle, now the second triangle is **active**.
