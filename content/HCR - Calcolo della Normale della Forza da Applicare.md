---
aliases:
  - normale della forza da applicare
---
***Ricorda***:

> ***Caso bidimensionale***:<br>![[Pasted image 20240924170627.png|222]]
> Vettore normale della forza da applicare, trovato tramite interpolazione:$$N = {d_2 \over d_1 + d_2}\kern2px N_1 + {d_1 \over d_1 + d_2}\kern2px N_2$$

> ***Caso tridimensionale***:<br>![[Pasted image 20240924170815.png|222]]
> Il vettore normale $\left(N_{x_{p}}\right)$, si trova facendo:$$\begin{array}{l} 1.&& N_{x_{pp}} = {\large{d_{3_{pp}} \over d_{2_{pp}} + d_{3_{pp}}}}\kern2px N_2 + {\large{d_{2_{pp}} \over d_{2_{pp}} + d_{3_{pp}}}}\kern2px N_3  \\[5px]   2.&& N_{x_{p}} = {\large{d_2 \over d_1 + d_2}}\kern2px N_1 + {\large{d_2 \over d_1 + d_2}}\kern2px N_{x_{pp}} \end{array}$$

----
###### Calcolo della Normale della Forza da Applicare
Tenendo allora conto della costruzione fatta, se si penetra nella superficie, bisogna stabilire **la normale della forza da applicare**.
Si consideri inizialmente il caso bidimensionale rappresentato:<br>![[Pasted image 20240924170627.png|333]]
L'interpolazione permette di stabilire che:$$N = {d_2 \over d_1 + d_2}\kern2px N_1 + {d_1 \over d_1 + d_2}\kern2px N_2$$Dove:
- $d_1 = \overline{x_p \kern5px P_1}$
- $d_2 = \overline{x_p \kern5px P_2}$
- E $P_1$, $P_2$, sono i punti/estremi del triangolo, o in questo caso del segmento (siamo nel caso **bidimensionale**)
- Inoltre:
	1. Se $d_1 = 0$, $N = N_1$.
	2. Se $d_2 = 0$, $N = N_2$.

Per il caso **tridimensionale** non si fa altro che applicare questo due volte:<br>![[Pasted image 20240924170815.png|333]]
- Come si può vedere meglio nel caso tridimensioale, le diverse forze normali ai vertici, quindi $N_1$, $N_2$, $N_3$, sono tutte diverse, nel caso bidimensionale questo non era chiarissimo.<br>Possiamo quindi considerare $N$ o $N_{x_p}$ come un vettore pesato tra $N_1$, $N_2$ ed $N_3$

Inannzitutto va scelto un vertice e va proiettato sul lato opposto passando per $x_p$, il quale è conosciuto dalla **collision detection**.
Si calcola poi la normale in $x_{pp}$ tramite l'interpolazione sul lato in cui si trova:$$N_{x_{pp}} = {d_{3_{pp}} \over d_{2_{pp}} + d_{3_{pp}}}\kern2px N_2 + {d_{2_{pp}} \over d_{2_{pp}} + d_{3_{pp}}}\kern2px N_3$$Infine si interpola sulla proiezione per calcolare la normale ad $x_p$:$$N_{x_{p}} = {d_2 \over d_1 + d_2}\kern2px N_1 + {d_2 \over d_1 + d_2}\kern2px N_{x_{pp}}$$

----