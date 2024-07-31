### State Automata with Output:
A state automaton with outputs is a 7-tuple ($\mathcal{E}$, $\mathcal{X}$, $\Gamma{}$, $f$, $x_0$, $Y$, $g$), where:
- ($\mathcal{E}$, $\mathcal{X}$, $\Gamma{}$, $f$, $x_0$) is a [[DES - Definition of 'State Automata'|state automaton]]
- $Y$ is a discrete set of **outputs**
- $g:\mathcal{X}\to{}Y$ is an **output function**
	- For each $x\in{}\mathcal{X}$, $y = g(x)$ is the system output when the current state is $x$
---
### Observation:
State automata are state automata with outputs where:
- $Y = \mathcal{X}$
- $g(x) = x$ for all $x\in{}\mathcal{X}$ (**identity function**)

---
### Observation:
State automata with outputs includes [[Moore Machines]] as a special case (when $\mathscr{X}$ is finite)
- **Moore Machine** are finite state machines used in sequential logic implementation

---
###### ~Example: model of a queuing system (cont'd)
![[03 - State automata(5-6)_211218_152842.pdf]]
 
 ---
 ### Observation:
 In this example the model cannot be completed, its nonsense, so we can say that the model we designed is wrong for the system