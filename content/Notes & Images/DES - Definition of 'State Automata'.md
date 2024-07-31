### State Automata:
A **state automaton** is a 1x5 tuple ($\mathcal{E}$, $\mathcal{X}$, $\Gamma{}$, $f$, $x_0$) where:
- $\mathcal{E}\,$ is a discrete set of [[DES - Definition of 'Event'|events]].
- $\mathcal{X}$ is a discrete set of [[DES - Definition of 'State of a System'|states]].
- $\Gamma{}$ is the [[DES - Definition of 'Domain of a Transition Function'|domain]].
	- For each $x\in{}\mathscr{X}$, $\Gamma{}\in{}\mathscr{E}$ is the set of events that are possible in the state $x$.
- $f$ : $\mathcal{X}\times{}\mathcal{E}\to{}\mathcal{X}$ is a [[DES - Definition of 'Transition Function'|transition function]].
	- For each $x\in{}\mathcal{X}$, $e\in{}\Gamma{}$, $x' = f(x,e)$ is the next state when the current state is $x$ and the next event is $e$. 
- $x_0\in{}\mathcal{X}$ is the **initial state**
---

###### ~Example: model of a queuing system

^d29e54

![[03 - State automata(2-4)_211218_152842.pdf]]