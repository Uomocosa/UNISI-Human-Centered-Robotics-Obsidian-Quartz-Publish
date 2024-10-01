- ***Pseudoinversa di una Matrice, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- ***Definizione***:
		- La **pseudoinversa di una matrice** (o **pseudoinversa di Moore-Penrose**) è una generalizzazione dell'inversa di una matrice quadrata a matrici che non sono necessariamente quadrate o invertibili.<br>È una matrice denotata $A^+$ che fornisce una soluzione approssimata ai sistemi di equazioni lineari, specialmente quando non esiste una soluzione unica.
	- ***Spiegazione***:
		- Per una matrice quadrata $A$, l'inversa $A^{-1}$ è una matrice che soddisfa:$$A A^{-1} = A^{-1} A = I$$dove $I$ è la matrice identità.<br>Tuttavia, non tutte le matrici sono quadrate o invertibili, ma possiamo comunque definire una **pseudoinversa** $A^+$ che approssima l'inversa e soddisfa condizioni simili.<br>La pseudoinversa è utilizzata quando:
		- La matrice non è quadrata (ad esempio una matrice $m \times n$ con $m \neq n$).
		- La matrice è **singolare** (ha determinante pari a zero) e quindi non invertibile nel senso tradizionale.
		- La pseudoinversa di una matrice $A$ soddisfa le seguenti proprietà:
		1. $A A^+ A = A$
		2. $A^+ A A^+ = A^+$
		3. $(A A^+)^T = A A^+$
		4. $(A^+ A)^T = A^+ A$
	- ***Costruzione della pseudoinversa***:<br>La pseudoinversa può essere calcolata utilizzando la **decomposizione ai valori singolari** (SVD):
		1. Dato $A$, troviamo la sua decomposizione $A = U \Sigma V^T$, dove:
		   - $U$ e $V$ sono matrici ortogonali.
		   - $\Sigma$ è una matrice diagonale contenente i valori singolari di $A$.
		2. La pseudoinversa $A^+$ si calcola come:$$A^+ = V \Sigma^+ U^T$$Dove $\Sigma^+$ è ottenuta invertendo i valori singolari non nulli di $\Sigma$ (per i valori nulli, si lascia zero).
	- ***Esempi***:
		1. **Matrice quadrata non invertibile**:
		   - Consideriamo la matrice:$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$$Questa matrice è **singolare** perché le righe non sono linearmente indipendenti (la seconda riga è il doppio della prima).<br>Non esiste un'inversa nel senso tradizionale, ma possiamo calcolare la sua pseudoinversa $A^+$.<br>Utilizzando la decomposizione ai valori singolari, otteniamo una soluzione approssimata per il sistema lineare associato.
		2. **Matrice rettangolare**:
		   - Supponiamo di avere una matrice $A$ rettangolare di dimensioni $3 \times 2$:$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$$Poiché $A$ non è quadrata, non possiamo calcolare la sua inversa nel senso tradizionale.<br>Tuttavia, possiamo calcolare la pseudoinversa $A^+$, che avrà dimensioni $2 \times 3$ e potrà essere utilizzata per risolvere il sistema di equazioni $A \mathbf{x} = \mathbf{b}$ nel modo dei **minimi quadrati**, minimizzando l'errore della soluzione.
	- ***Applicazioni della pseudoinversa***:
		1. **Risoluzione di sistemi lineari**:
		   - La pseudoinversa è utilizzata per risolvere sistemi lineari che non hanno una soluzione unica o che non possono essere risolti con i metodi tradizionali.<br>In particolare, per un sistema sovradeterminato (cioè con più equazioni che incognite), la pseudoinversa fornisce la soluzione dei **minimi quadrati**, che minimizza l'errore tra la soluzione stimata e i dati osservati.
		   - Se abbiamo un sistema $A \mathbf{x} = \mathbf{b}$, dove $A$ è una matrice rettangolare, la pseudoinversa $A^+$ fornisce la soluzione:$$\mathbf{x} = A^+ \mathbf{b}$$Questa soluzione minimizza la norma $|| A \mathbf{x} - \mathbf{b} ||$, riducendo l'errore tra i dati $\mathbf{b}$ e la soluzione approssimata.
		2. **Robotica e cinematica inversa**:
		   - Nella robotica, la pseudoinversa della **matrice Jacobiana** è spesso utilizzata per calcolare la **cinematica inversa**.<br>La matrice Jacobiana $J$ mappa le velocità dei giunti del robot alle velocità dell'end-effector.<br>Se il robot ha ridondanza (più gradi di libertà rispetto ai movimenti richiesti), la Jacobiana potrebbe non essere invertibile.<br>La pseudoinversa consente di trovare una soluzione approssimata che minimizza l'errore e fornisce una soluzione ai movimenti dei giunti.
		   - Esempio: Se $J$ è la Jacobiana e $\mathbf{v}$ è la velocità desiderata per l'end-effector, possiamo calcolare la velocità dei giunti come $\mathbf{\dot{q}} = J^+ \mathbf{v}$, dove $J^+$ è la pseudoinversa della Jacobiana.
		3. **Apprendimento automatico**:
		   - La pseudoinversa viene anche utilizzata in alcune tecniche di **regressione lineare** per trovare i coefficienti che minimizzano l'errore tra le previsioni del modello e i dati osservati.
	- ***Esempio numerico***:
		- Consideriamo una matrice semplice:$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$$Per trovare la pseudoinversa $A^+$, possiamo usare la decomposizione ai valori singolari (SVD).<br>Il risultato è:$$A^+ = \begin{pmatrix} -16.6667 & -1.6667 & 13.3333 \\ 13.3333 & 1.6667 & -10.0000 \end{pmatrix}$$Questa pseudoinversa minimizza l'errore nel risolvere sistemi lineari sovradeterminati associati alla matrice $A$.
	- ***Conclusione***:<br>La **pseudoinversa** è uno strumento potente per gestire matrici che non sono invertibili o quadrate.<br>Essa fornisce una soluzione approssimata in molti contesti, inclusa la risoluzione di sistemi di equazioni lineari, la robotica e la minimizzazione dell'errore nei modelli di regressione.
----
