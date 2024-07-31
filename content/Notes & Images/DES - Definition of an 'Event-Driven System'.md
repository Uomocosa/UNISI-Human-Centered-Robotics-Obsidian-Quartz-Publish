### Event-Driven System:
An event-driven system is [[DES - Definition of 'Dynamical System'|dynamical]]  or a [[DES - Definition of 'Discrete'|discrete]] system, where the evolution of the system is guided by the events.

 In **event-driven** systems, the [[DES - Definition of 'State of a System'|state]] changes only upon the (typically) asynchronous occurrence of [[DES - Definition of 'Event'|events]].

For these system time $t$ is a **dependent variable** (it depends on the events)

So the state of an **event-driven** system is **NON-DIFFERENTIABLE**, so the system cannot be modeled by [[Differential Equations|differential equations]].

---

###### Example of Event-Driven System: Queuing System
![[Pasted image 20220116173529.png]]
-  Here the **events** are: arrivals, and departures
- The system graph cannot have a continuous function, arrival do not change gradually, the same for departures, so it will result in something like:

![[Pasted image 20220116173709.png]]

---