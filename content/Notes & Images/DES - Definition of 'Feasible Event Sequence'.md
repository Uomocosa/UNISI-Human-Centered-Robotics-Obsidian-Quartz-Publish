### Feasible Event Sequence:
The event sequence $\{e_1,\,e_2,\,e_3,\,...\}$ is **feasible** for the [[DES - Definition of 'State Automata'|state automaton]] ($\mathscr{E}$, $\mathscr{X}$, $\Gamma{}$, $f$, $x_0$) if $e_k\in{}\Gamma{}(x_{k-1})$ for all $k = 1,\:2,\:3,\:...$
- If $e_k\notin{}\Gamma{}(x_{k-1})$ for some index k, the simulation returns an **error**.

---
##### Translation: 
If the sequence of events is not done right, then when simulating it, an event does occur but given the model of the system (which we suppose it is done right) it couldn't.
So the system doesn't know at which state to go.
$\Rightarrow{}$ The sequence of events is defined as **unfeasible**.
$\Rightarrow{}$ And the system is said to be stuck in a **singularity**.

---

###### ~Example: Queuing system (cont'd)
The system it refers to is given [[DES - Definition of 'State Automata'#Example model of a queuing system|here]].

![[Pasted image 20220116203330.png]]