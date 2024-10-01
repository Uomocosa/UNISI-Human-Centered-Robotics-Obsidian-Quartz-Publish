---
aliases:
  - matrice di rotazione
---
- ***Matrice di Rotazione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- La **matrice di rotazione** è una matrice che descrive la rotazione di un oggetto nello spazio attorno a uno o più assi cartesiani. In robotica, informatica grafica e fisica, le matrici di rotazione vengono utilizzate per trasformare le coordinate di un punto o di un vettore da un sistema di riferimento a un altro dopo una rotazione.
	- ***Matrice di Rotazione 2D***:
		- ==Nel caso di una rotazione nel piano 2D, la matrice di rotazione è una matrice $2 \times 2$ che ruota un vettore attorno all'origine di un angolo $\theta$==. ==La matrice di rotazione per una rotazione antioraria attorno all'origine è==:$$R(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta \\\sin\theta & \cos\theta\end{bmatrix}$$
	- ==***Esempio di rotazione in 2D***==:
		- ==Supponiamo di voler ruotare il punto $P(1, 0)$ di 90 gradi ($\theta = 90^\circ$) in senso antiorario attorno all'origine==.
		- ==La matrice di rotazione per $\theta = 90^\circ$ è==:$$R(90^\circ) = \begin{bmatrix}\cos(90^\circ) & -\sin(90^\circ) \\\sin(90^\circ) & \cos(90^\circ)\end{bmatrix}= \begin{bmatrix}0 & -1 \\1 & 0\end{bmatrix}$$Se applichiamo questa matrice al vettore $P = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, otteniamo:$$P' = R(90^\circ) \cdot P = \begin{bmatrix}0 & -1 \\1 & 0\end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$Il nuovo punto dopo la rotazione è $P'(0, 1)$, che corrisponde a una rotazione di 90 gradi antioraria attorno all'origine.
	- ***Matrice di Rotazione 3D***:
		- Nel caso di una rotazione nello spazio tridimensionale (3D), la rotazione può avvenire attorno a uno dei tre assi cartesiani $x$, $y$ o $z$. La matrice di rotazione sarà una matrice $3 \times 3$.
	- ***1. Rotazione attorno all'asse $x$***:
		- La matrice di rotazione per un angolo $\theta$ attorno all'asse $x$è:$$R_x(\theta) = \begin{bmatrix}1 & 0 & 0 \\0 & \cos\theta & -\sin\theta \\0 & \sin\theta & \cos\theta\end{bmatrix}$$Questa matrice lascia invariata la coordinata $x$, mentre ruota le componenti $y$ e $z$ del vettore.
	- ***2. Rotazione attorno all'asse $y$***:
		- La matrice di rotazione per un angolo $\theta$ attorno all'asse $y$è:$$R_y(\theta) = \begin{bmatrix}\cos\theta & 0 & \sin\theta \\0 & 1 & 0 \\-\sin\theta & 0 & \cos\theta\end{bmatrix}$$Questa matrice lascia invariata la coordinata $y$, mentre ruota le componenti $x$ e $z$ del vettore.
	- ***3. Rotazione attorno all'asse $z$***:
		- La matrice di rotazione per un angolo $\theta$ attorno all'asse $z$è:$$R_z(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta & 0 \\\sin\theta & \cos\theta & 0 \\0 & 0 & 1\end{bmatrix}$$Questa matrice lascia invariata la coordinata $z$, mentre ruota le componenti $x$ e $y$ del vettore.
	- ***Esempio di rotazione in 3D***:
		- Supponiamo di voler ruotare il punto $P = (1, 0, 0)$ attorno all'asse $z$ di 90 gradi.
		- La matrice di rotazione attorno all'asse $z$ per $\theta = 90^\circ$è:$$R_z(90^\circ) = \begin{bmatrix}0 & -1 & 0 \\1 & 0 & 0 \\0 & 0 & 1\end{bmatrix}$$Applicando questa matrice al vettore $P = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$, otteniamo:$$P' = R_z(90^\circ) \cdot P = \begin{bmatrix}0 & -1 & 0 \\1 & 0 & 0 \\0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$$Quindi, dopo una rotazione di 90 gradi attorno all'asse $z$, il punto $P(1, 0, 0)$ diventa $P'(0, 1, 0)$.
	- ==***Proprietà delle Matrici di Rotazione***==:
		  1. **Ortogonalità**: ==Una matrice di rotazione è una **matrice ortogonale**, il che significa che la sua **trasposta** è uguale alla sua inversa==:$$   R^T = R^{-1}   $$   
		  2. **Determinante**: ==Il determinante di una matrice di rotazione è sempre uguale a 1==:$$   \text{det}(R) = 1   $$
		  3. **Composizione di rotazioni**: ==Se vuoi combinare più rotazioni, puoi moltiplicare tra loro le matrici di rotazione corrispondenti==.<br>Ad esempio, se vuoi ruotare prima attorno all'asse $x$ e poi attorno all'asse $y$, puoi calcolare la matrice di rotazione totale come:$$   R_{\text{totale}} = R_y(\theta_y) \cdot R_x(\theta_x)   $$
		  4. **Invarianza della lunghezza**: ==Le matrici di rotazione non alterano la lunghezza dei vettori==.<br>Se $v$ è un vettore, la sua lunghezza rimane invariata dopo una rotazione:$$   \| R \cdot v \| = \| v \|   $$
	- ***Applicazioni delle Matrici di Rotazione***
		- Le matrici di rotazione sono utilizzate in una vasta gamma di applicazioni, tra cui:
			- **Robotica**: Per calcolare la posizione e l'orientamento dei giunti e degli end-effector nei manipolatori robotici.
			- **Grafica computazionale**: Per ruotare oggetti nello spazio tridimensionale.
			- **Simulazioni fisiche**: Per modellare il movimento e l'orientamento di corpi rigidi.
			- **Visione artificiale**: Per trasformare immagini o punti nello spazio in base alla posizione e all'orientamento di una telecamera.
		- In sintesi, le **matrici di rotazione** forniscono un modo compatto e sistematico per descrivere le rotazioni nello spazio, e sono uno strumento essenziale in molte aree della matematica applicata e dell'ingegneria.
