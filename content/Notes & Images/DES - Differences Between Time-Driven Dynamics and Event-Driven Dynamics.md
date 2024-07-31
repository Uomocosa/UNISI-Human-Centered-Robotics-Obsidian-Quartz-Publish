###### Synthesis
A normal physic system (like the suspension system) can be modelled by a differential equation, so it can be derived, and integrated.

A queuing system (like the queue at the post office) cannot be modelled by a differential equation, because the number of elements in the queue belongs to the Natural set ($\mathbb{N}$).

---
### Differences between a Physic system and a Queuing system
![[Pasted image 20220116161842.png]]
![[Pasted image 20220116161856.png]]

- The suspension system will be modelled by a **linear time-invariant [[Differential Equations|differential equation]]**: $m\ddot{x} + c\dot{x} + kx = f$
- So how can we model **event-driven** dynamics?

---

### Objectives of the course:
- Modeling, analysis and simulation of **Discrete Event Systems** (DES)
---

##### Main Contents:
- modeling
- probability
- programming ([[MATLAB - Index|MATLAB]])

##### Which types of models will be considered ? 
- Logical and timed models (**automata**)
- Markov chains

Main application: ***QUEUEING THEORY***

---

###### ~Examples of discrete event systems:
- A manufacturing plant with machines, workers, conveyor belts, buffers, etc.
- A bank with different types of customers and services (desks, ATMs, etc.)
- A computer system with resources and processes needing access to resources