---
aliases:
  - rango
  - rango di una matrice
  - matrice a rango massimo
---
- ***Source:*** [Youmath](https://www.youmath.it/forum/algebra-lineare/59683-relazione-tra-rango-nucleo-e-immagine.html)
	- Cos'è il **rango di una matrice**? Il rango di una matrice è il massimo numero di colonne linearmente indipendenti della matrice, e dalla teoria sappiamo che equivale alla dimensione dello spazio generato dalle colonne della matrice.

- ***Rango Massimo, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- ***Definizione***:
		- Il **rango massimo** di una matrice è il massimo numero di righe o colonne linearmente indipendenti in quella matrice.<br>In altre parole, è il massimo numero di vettori che non possono essere scritti come combinazioni lineari degli altri vettori.<br>Il **rango** di una matrice $A$ è il numero di colonne (o righe) indipendenti che costituiscono una base per lo spazio vettoriale generato da $A$.
		- Il **rango massimo** si ottiene quando tutte le righe o tutte le colonne di una matrice sono linearmente indipendenti.<br>In questo caso, il rango della matrice è uguale al numero minore tra il numero di righe e il numero di colonne della matrice.
	- ***Spiegazione***:
		- Per una matrice $A$ di dimensioni $m \times n$ (con $m$ righe e $n$ colonne):
		- Se $A$ ha **rango massimo**, significa che le righe o le colonne sono tutte linearmente indipendenti.<br>Il rango sarà quindi uguale al valore più basso tra $m$ e $n$.$$\text{Rango massimo di } A = \min(m, n)$$
		- Se il rango è inferiore al massimo, significa che alcune righe o colonne sono combinazioni lineari delle altre.
	- ***Esempio di rango massimo***:
		1. **Matrice quadrata non singolare**:
		   - Considera la matrice identità $I$ di dimensioni $3 \times 3$:$$I = \begin{pmatrix}     1 & 0 & 0 \\    0 & 1 & 0 \\    0 & 0 & 1     \end{pmatrix}$$In questa matrice, tutte le righe e tutte le colonne sono indipendenti.<br>Nessuna riga può essere scritta come combinazione lineare delle altre.<br>Quindi, il rango di $I$ è 3, che è il **rango massimo** per una matrice $3 \times 3$.
		2. **Matrice rettangolare di rango massimo**:
		   - Considera una matrice rettangolare $A$ di dimensioni $2 \times 3$:$$A = \begin{pmatrix}     1 & 2 & 3 \\    4 & 5 & 6     \end{pmatrix}$$Il rango massimo per una matrice $2 \times 3$ è il valore minore tra il numero di righe e il numero di colonne, quindi 2.<br>Se le due righe sono linearmente indipendenti, il rango di $A$ sarà 2, cioè il suo rango massimo.
	- ***Esempio di rango non massimo***:
		- Considera la matrice:$$B = \begin{pmatrix}  1 & 2 & 3 \\ 2 & 4 & 6  \end{pmatrix}$$Notiamo che la seconda riga è una combinazione lineare della prima (infatti, è il doppio della prima riga).<br>Quindi, queste due righe non sono indipendenti.<br>Il rango della matrice $B$ è 1, che è inferiore al rango massimo possibile per una matrice $2 \times 3$ (che sarebbe 2).
	- ***Importanza del rango massimo***:<br>Il rango massimo di una matrice è un indicatore della "piena potenza" della matrice nel rappresentare uno spazio vettoriale:
		- **Inversione di matrici**: Solo una matrice quadrata con rango massimo (detto anche **matrice non singolare**) può essere invertita.<br>Se una matrice non ha rango massimo, non è invertibile.
		- **Soluzioni di sistemi lineari**: Se una matrice associata a un sistema lineare ha rango massimo, il sistema ha soluzioni uniche.<br>Se il rango è inferiore, potrebbe avere infinite soluzioni o nessuna.
		- **Robotica e cinematica**: In robotica, il rango della **matrice Jacobiana** determina il numero di gradi di libertà di un manipolatore robotico.<br>Se il rango della Jacobiana è massimo, il robot può muovere il suo end-effector liberamente nello spazio, senza ridondanza o vincoli inutili.
	- ***Esempio in robotica***:
		- Considera un robot con tre giunti che manipola un oggetto in uno spazio tridimensionale.<br>La **matrice Jacobiana** del robot può essere una matrice $3 \times 3$, dove ciascuna riga rappresenta la velocità lineare e angolare dell'end-effector in funzione delle velocità dei giunti.<br>Se il rango della Jacobiana è 3 (rango massimo), il robot ha piena capacità di controllo in tutte e tre le direzioni dello spazio.<br>Se il rango fosse minore di 3, il robot avrebbe dei vincoli e non potrebbe muoversi liberamente in tutte le direzioni.
	- ***Conclusione***:<br>Il **rango massimo** di una matrice si riferisce al numero massimo di righe o colonne linearmente indipendenti che una matrice può avere.<br>Se il rango è massimo, la matrice è pienamente utilizzabile per rappresentare uno spazio vettoriale senza ridondanze o dipendenze lineari.<br>Questo concetto è essenziale in algebra lineare, robotica e molte altre applicazioni ingegneristiche e matematiche.
----
