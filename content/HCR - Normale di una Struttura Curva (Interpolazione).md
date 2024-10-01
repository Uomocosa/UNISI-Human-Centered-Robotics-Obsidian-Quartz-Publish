---
aliases:
  - normale di una struttura curva
  - interpolazione
---
***Ricorda***:

>

>

----
###### Normale di una Struttura Curva (Interpolazione)
Si consideri un oggetto curvo, come una sfera. In generale la differenza temporale tra un'azione ed il feedback non può superare la frazione di secondo, in quanto si avrebbe la dissociazione dei due eventi.
La computazione però potrebbe impiegare molto tempo dunque si deve cercare di usare meno dati possibili.

Si ipotizzi, per esempio, di voler approssimare la sfera con un cubo: le forze non possono essere dirette secondo normali a questo in quanto risulterebbe irrealistico:<br>![[Pasted image 20240904192433.png]]

Si potrebbe aumentare il numero di vertici, migliorando l'approssimazione, o si potrebbe utilizzare l'**interpolazione**:
1. Si consideri un punto sulla superficie reale e si calcolino i piani, considerando i punti adiacenti.<br>Per ognuno di essi si detrmina la normale secondo $x,\ y,\ z$ la funzione del piano oppure:$${1 \over (a^2 + b^2 + c^2)}\cdot \left<a \kern10px b \kern10px c  \right>$$Dove:
	- $\left<a \kern10px b \kern10px c  \right>$ è un modo più carino di chiamare $(a \ b \ c)$. #NOT_SURE_ABOUT_THIS `non so se sono la stessa cosa, e se effettivamente questa formula è corretta, ref:` [[HCR - Handwritten Notes (Not Mine)|pagina 15 delle note scritte a mano]]
2. E facendo la media di queste si ottiene la normale al punto iniziale cioè:<br>![[Pasted image 20240904192930.png]]<br>Equivalente a risolvere il seguente sistema:$$\begin{array}{c} \left[\begin{array}{l} \vec x_{p_{1}}^{\tiny T} \\ \vec x_{p_{2}}^{\tiny T} \\ \vec x_{p_{3}}^{\tiny T} \\ \vec x_{p_{4}}^{\tiny T} \\ \vec x_{p_{5}}^{\tiny T} \end{array}\right] \\[5px] {\tiny 5 \times 3} \end{array} \kern0px  \begin{array}{c} \left[\begin{array}{l} a \\[2px] b \\ c \end{array}\right] \\[5px] {\tiny 3 \times 1} \end{array} = \begin{array}{c} \left[\begin{array}{l} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{array}\right] \\[5px] {\tiny 5 \times 1}\end{array}$$Dove:
	- $(a \ b \ c)^{\tiny T}$ è l'incognita e consiste nella normale al piano definito da tutti i punti.
	- $x_{p_i}$ è **la normale** di uno dei piano/triangoli.
----
