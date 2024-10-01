---
aliases:
  - trasformazione omogenea
---
- ***Trasformazione Omogenea, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- La **trasformazione omogenea** è una tecnica utilizzata in robotica, grafica 3D e geometria per descrivere e combinare **rotazioni** e **traslazioni** in uno spazio. La trasformazione omogenea estende i vettori e le matrici di rotazione in uno spazio dimensionale superiore, permettendo di rappresentare rotazioni e traslazioni in un'unica operazione.
	- ***Concetto di Trasformazione Omogenea***:
		- ==Una trasformazione omogenea in 3D è rappresentata da una **matrice 4x4**, che include sia la rotazione che la traslazione.<br>È utilizzata per cambiare il sistema di riferimento di un oggetto o per spostare e ruotare punti e vettori nello spazio tridimensionale==.
		- ==La **matrice di trasformazione omogenea** ha la seguente struttura generale==:$$T = \begin{bmatrix}R & d \\0 & 1\end{bmatrix}$$Dove:
			- ==$R$ è una **matrice di rotazione** $3 \times 3$==.
			- ==$d$ è un vettore di **traslazione** $3 \times 1$, che rappresenta lo spostamento dell'origine del sistema di riferimento==.
			- ==La riga $[0 \quad 0 \quad 0 \quad 1]$ permette di mantenere la rappresentazione omogenea==.
		- ==Questa matrice può essere applicata a un **vettore omogeneo**==:$$P_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$Il quale estende il vettore tridimensionale ordinario aggiungendo un'ultima componente uguale a 1.
	- ***Trasformazione Omogenea per Rotazione e Traslazione***:
		- Quando vogliamo ruotare un oggetto e traslarlo contemporaneamente, utilizziamo la matrice di trasformazione omogenea. La trasformazione omogenea consente di combinare le operazioni di **rotazione** e **traslazione** in un'unica matrice, il che è particolarmente utile per applicazioni in cui gli oggetti cambiano posizione e orientamento, come in robotica.
	- ***Matrice di Trasformazione Omogenea:$$T = \begin{bmatrix}R_{3 \times 3} & d_{3 \times 1} \\0_{1 \times 3} & 1\end{bmatrix}$$$R$ è la matrice di rotazione $3 \times 3$.***:
			- $d$ è il vettore di traslazione $3 \times 1$.
			- La riga inferiore $[0 \quad 0 \quad 0 \quad 1]$ permette la rappresentazione omogenea, e garantisce che la trasformazione operi su vettori omogenei.
	- ***Esempio di Trasformazione Omogenea***:
		- Supponiamo di avere un punto $P = (x, y, z)$ e vogliamo:
			- Ruotare il punto attorno all'asse $z$ di un angolo $\theta$.
			- Traslare il punto di $d_x$, $d_y$ e $d_z$.
		- La **matrice di rotazione** attorno all'asse $z$è:$$R_z(\theta) = \begin{bmatrix}\cos\theta & -\sin\theta & 0 \\\sin\theta & \cos\theta & 0 \\0 & 0 & 1\end{bmatrix}$$Il **vettore di traslazione**è:$$d = \begin{bmatrix} d_x \\ d_y \\ d_z \end{bmatrix}$$La matrice di **trasformazione omogenea** è quindi:$$T = \begin{bmatrix}\cos\theta & -\sin\theta & 0 & d_x \\\sin\theta & \cos\theta & 0 & d_y \\0 & 0 & 1 & d_z \\0 & 0 & 0 & 1\end{bmatrix}$$Ora, possiamo applicare questa trasformazione al **vettore omogeneo**:$$P_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$Il quale rappresenta il punto $P$ nello spazio 3D. Il risultato sarà la nuova posizione di $P$ dopo la rotazione e la traslazione.
	- ***Esempio pratico:***:
		- Supponiamo di voler ruotare il punto $P = (1, 0, 0)$ di 90° attorno all'asse $z$ e poi traslarlo di $d_x = 3$, $d_y = 2$, e $d_z = 1$.
		  1. **Matrice di rotazione attorno all'asse $z$ per $\theta = 90^\circ$**:$$   R_z(90^\circ) = \begin{bmatrix}   0 & -1 & 0 \\   1 & 0 & 0 \\   0 & 0 & 1   \end{bmatrix}   $$
		  2. **Vettore di traslazione**:$$   d = \begin{bmatrix} 3 \\ 2 \\ 1 \end{bmatrix}   $$
		  3. **Matrice di trasformazione omogenea**:$$   T = \begin{bmatrix}   0 & -1 & 0 & 3 \\   1 & 0 & 0 & 2 \\   0 & 0 & 1 & 1 \\   0 & 0 & 0 & 1   \end{bmatrix}   $$
		  4. **Applichiamo la trasformazione al vettore omogeneo***$$P_h = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}$$$$   P'_h = T \cdot P_h = \begin{bmatrix}   0 & -1 & 0 & 3 \\   1 & 0 & 0 & 2 \\   0 & 0 & 1 & 1 \\   0 & 0 & 0 & 1   \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \\ 1 \\ 1 \end{bmatrix}   $$Dopo la rotazione e la traslazione, il nuovo punto è $P' = (3, 3, 1)$.
	- ***Uso nelle Catene Cinematiche in Robotica***:
		- Nella robotica, le trasformazioni omogenee vengono utilizzate per rappresentare i movimenti dei giunti e dei link in un manipolatore robotico. ==Ogni giunto può avere una matrice di trasformazione omogenea associata che descrive la sua rotazione e traslazione rispetto al giunto precedente==. Combinando queste matrici, è possibile calcolare la posizione e l'orientamento dell'***end-effector*** (la "mano" del robot).
	- ***Vantaggi delle Trasformazioni Omogenee***:
		  1. **Unificazione delle rotazioni e traslazioni**: ==Le trasformazioni omogenee permettono di combinare rotazioni e traslazioni in un'unica matrice, rendendo più semplice e uniforme la gestione dei movimenti nello spazio 3D==.
		  2. **Composizione di trasformazioni**: Utilizzando le matrici omogenee, è possibile comporre più trasformazioni (come rotazioni e traslazioni consecutive) semplicemente moltiplicando le matrici tra loro.
		  3. **Facilità di implementazione**: Le trasformazioni omogenee possono essere implementate facilmente nei sistemi di robotica e grafica 3D, e forniscono un metodo potente per calcolare movimenti complessi.
	- In sintesi, la **trasformazione omogenea** è uno strumento fondamentale in robotica e geometria computazionale per combinare rotazioni e traslazioni in uno spazio tridimensionale, facilitando la rappresentazione e il calcolo di movimenti complessi.
