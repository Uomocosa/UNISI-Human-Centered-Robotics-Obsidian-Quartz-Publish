### From single kinematic chain Jacobian (or single finger Jacobian) to Hand Jacobian
![[Pasted image 20220404114141.png]]
-> Where:
- $j_Fi$  : joint Finger $i$
- each joint is angular, so it will have an angular velocity $\dot \Theta_i$

![[Pasted image 20220404114312.png]]
![[Pasted image 20220404114324.png]]

> **NOTE**:
> The energy at the end-effector is the sum of all the energy expended by the joints.
> The joints at each point is calculated by the force times the velocity.

![[Pasted image 20220404114506.png]]

Ideally without dissipation of energy we have:
![[Pasted image 20220404114531.png]]

We also know that:
![[Pasted image 20220404114549.png]]

After a rough estimation of the weight and the barycenter of the object, our brain computes the already seen formula:
![[Pasted image 20220404114630.png]]
-> So our brains has to do a few passages before we move the object at hand:
1. First it calculates the trajectory ($W_c$), how I want the object to behave.
2. Then it calculates the Grasp matrix, where are my finger on the object
3. Lastly it evaluates the forces needed to move the object along the previous thought trajectory