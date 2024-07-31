###### Synthesis
A *State Automata* is a DES where the events are all **deterministic**, this means that we know the sequence of events that will happen, and we can describe how the system will evolve.

>**NOTE**: 
>We do **NOT** know when the events will happen, the State Automata does not have a concept of time.

A state automata is described by the 5-tuple: ($\mathcal{E}, \ \mathcal{X}, \ \Gamma, \ f,  \ x_0$):
- $\mathcal{E}$ : **Event set** : $\{e_1, \ e_2, \ e_3, \ \ldots\}$.
- $\mathcal{X}$ : **State set** : $\{x_0, \ x_1, \ x_2, \ \ldots\}$.
- $\Gamma$ : **Domain** : Given a state $x_i$ what are the possible events from that state?
- $f$ : **Transition Function** : If at state $x_i$, event $e_j$ occurs, at which state will I be then?
- $x_0$ : **Initial State**.

Also if we want to "monitor" one aspect of the system we can use a *State Automata with Outputs*, described by the 7-tuple: ($\mathcal{E}, \ \mathcal{X}, \ \Gamma, \ f,  \ x_0, \ Y, \ g$):
- $Y$ : **Output set** : $\{y_0, \ y_1, \ y_2, \ \ldots\}$.
- $g$ : **Transition Function** : Given a state $x_i$, what will be my output $y_i$?

---
# State Automata 
What do we need for defining the model of a Discrete Event System (DES)?
- Events.
- State.
- [[DES - Definition of 'Transition Function'|Transition Function]].
	- and it's [[DES - Definition of 'Domain of a Transition Function'|domain]].
- Initial State.

With these "ingredients" we are ready to introduce the first model class for [[DES - Definition of an 'Event-Driven System'|discrete-event systems]]:
- [[DES - Definition of 'State Automata'|Definition of 'State Automata']].
- [[DES - Definition of 'State Automata with Output'|Definition of 'State Automata with Output']]. 

---

#### Graphical representation of state automata:
A state automaton ($\mathscr{E}$, $\mathscr{X}$, $\Gamma{}$, $f$, $x_0$) can be represented as a labelled, direct graph where: ^84d27b
- the **nodes** are the states in $\mathscr{X}$.
- there is a direct arc from node $x$ to node $x'$ with label $e$ if and only if $x' = f(x,e)$.
	- ($x$, $x'$, $e$, $f$) as defined [[DES - Definition of 'State Automata'|here]].

![[Pasted image 20220116200240.png]]

The **initial state** $x_0$ is denoted by an arc pointing at the node $x_0$ with no source:
![[Pasted image 20220116200357.png]]

If present, outputs can be represented by labels on the nodes
- there is a label $y$ on node $x$ if and only if $y = g(x)$.

![[Pasted image 20220116200523.png]]

---
###### ~Example: Queuing system (cont'd):
The system it refers to is given [[DES - Definition of 'State Automata'#Example model of a queuing system|here]].

![[Pasted image 20220116200652.png]]

---
#### What can we do with these models?
$\to$ **Simulation**

![[Pasted image 20220116200932.png]]

---
### State Automata with Output:
From the input-output point of view, a state automaton can be seen as:

![[Pasted image 20220116201102.png]]

$\Rightarrow$ A **Purely Logical Model**: given an event sequence, it returns the corresponding state (or output) sequence.
- No information about **when** events (and therefore state transition) occurs
- This is why a state automata are also called **logical** (or **un-timed**) models of discrete event systems.

---
#### Observation:
For the simulation of a state automaton to not get stuck in a "**singularity**", the event sequence provided in input must feasible.
- [[DES - Definition of 'Feasible Event Sequence']]