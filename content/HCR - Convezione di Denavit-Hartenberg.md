---
aliases:
  - convezione di Denavit-Hartenberg
  - tavole di Denavit-Hartenberg
---
- ***Convezione di Denavit-Hartenberg, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- ==La **Convenzione di Denavit-Hartenberg (DH)** è un metodo standardizzato utilizzato in robotica per descrivere la **cinematica dei manipolatori robotici**==.<br>Questo metodo semplifica il processo di calcolo delle trasformazioni di coordinate tra i giunti di un robot, che sono necessari per determinare la posizione e l'orientamento dell'end-effector (cioè l'utensile o la mano del robot) nello spazio.<br>==Grazie alla convenzione DH, possiamo descrivere in modo sistematico la struttura di un robot e le trasformazioni tra i suoi giunti==.
	- ***Obiettivo della Convenzione DH***:
		- ==La convenzione DH ha lo scopo di facilitare il calcolo delle **trasformazioni omogenee** che descrivono la posizione e l'orientamento di ogni giunto rispetto a quello precedente, utilizzando quattro parametri noti come **parametri di Denavit-Hartenberg**==.<br>==Questi parametri permettono di rappresentare la posizione e l'orientamento relativi tra due sistemi di riferimento adiacenti==.
	- ***Parametri DH***:
		- ==Per ogni coppia di giunti consecutivi, la convenzione DH definisce 4 parametri che descrivono le loro relazioni geometriche==:
			1. **$\theta_i$**: Angolo di rotazione attorno all'asse $z_{i-1}$, che orienta l'asse $x_i$ rispetto a $x_{i-1}$.<br>==Questo parametro è variabile per un giunto **revoluto** (giunto rotante) e fisso per un giunto **prismatico**==.
			2. **$d_i$**: Distanza lungo l'asse $z_{i-1}$ tra l'origine del sistema di riferimento $i-1$ e l'origine del sistema di riferimento $i$.<br>==Questo parametro è variabile per un giunto **prismatico** (giunto traslante) e fisso per un giunto **revoluto**==.
			3. **$\alpha_i$**: Angolo di rotazione attorno all'asse $x_i$ che descrive l'inclinazione tra l'asse $z_{i-1}$ e l'asse $z_i$.<br>==Questo parametro è sempre fisso e descrive l'angolo tra i due assi==.
			4. **$a_i$**: Distanza lungo l'asse $x_i$ tra l'asse $z_{i-1}$ e l'asse $z_i$.<br>==Anche questo parametro è fisso e rappresenta la distanza tra i giunti lungo l'asse $x_i$.==
	- ***Matrice di Trasformazione DH***:
		- ==Utilizzando questi quattro parametri, si costruisce una **matrice di trasformazione omogenea** $T_i^{i-1}$ per ogni giunto del robot, che permette di passare dal sistema di riferimento $i-1$ al sistema $i$==:$$T_i^{i-1} = \begin{bmatrix}\cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\\sin\theta_i & \cos\theta_i \cos\alpha_i & -\cos\theta_i \sin\alpha_i & a_i \sin\theta_i \\0 & \sin\alpha_i & \cos\alpha_i & d_i \\0 & 0 & 0 & 1\end{bmatrix}$$Questa matrice include le informazioni di rotazione e traslazione tra i giunti e descrive come passare da un sistema di riferimento all'altro.
	- ***Esempio di Applicazione: Braccio Robotico a 2 Giunti***:
		- Supponiamo di avere un braccio robotico a **2 giunti revoluti** con lunghezze dei segmenti $L_1$ e $L_2$.<br>Vogliamo utilizzare la convenzione DH per descrivere la relazione tra i due giunti e calcolare la posizione dell'end-effector:
			- **Giunto 1 (base del braccio)**:
				- $\theta_1$: Angolo di rotazione attorno all'asse $z_0$ (variabile).
				- $d_1 = 0$: Il primo giunto non ha traslazione lungo l'asse $z_0$.
				- $\alpha_1 = 0$: Gli assi $z_0$ e $z_1$ sono paralleli (nessun angolo tra loro).
				- $a_1 = L_1$: La lunghezza del primo segmento del braccio.
			- **Giunto 2 (alla fine del primo segmento)**:
				- $\theta_2$: Angolo di rotazione attorno all'asse $z_1$ (variabile).
				- $d_2 = 0$: Non c'è traslazione lungo l'asse $z_1$.
				- $\alpha_2 = 0$: Gli assi $z_1$ e $z_2$ sono paralleli.
				- $a_2 = L_2$: La lunghezza del secondo segmento del braccio.
	- ***Matrici di Trasformazione***:
		- Per il giunto 1, la matrice di trasformazione omogenea $T_1^0$ sarà:$$T_1^0 = \begin{bmatrix}\cos\theta_1 & -\sin\theta_1 & 0 & L_1 \cos\theta_1 \\\sin\theta_1 & \cos\theta_1 & 0 & L_1 \sin\theta_1 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1\end{bmatrix}$$Per il giunto 2, la matrice di trasformazione omogenea $T_2^1$ sarà:$$T_2^1 = \begin{bmatrix}\cos\theta_2 & -\sin\theta_2 & 0 & L_2 \cos\theta_2 \\\sin\theta_2 & \cos\theta_2 & 0 & L_2 \sin\theta_2 \\0 & 0 & 1 & 0 \\0 & 0 & 0 & 1\end{bmatrix}$$==La posizione finale dell'end-effector nel sistema di riferimento del giunto 0 è data moltiplicando le matrici di trasformazione==:$$T_2^0 = T_1^0 \cdot T_2^1$$Calcolando questa moltiplicazione si ottiene una nuova matrice che rappresenta la posizione e l'orientamento dell'end-effector rispetto al sistema di riferimento base.
	- ***Vantaggi della Convenzione DH***:
		  1. **Sistematicità**: La convenzione DH fornisce un metodo sistematico e standard per descrivere i robot.<br>Questo facilita l'analisi e la modellazione di robot con strutture complesse.
		  2. **Facilità di Calcolo**: Utilizzando i parametri DH, è possibile calcolare facilmente le matrici di trasformazione omogenea, che possono essere moltiplicate insieme per ottenere la posizione finale dell'end-effector rispetto alla base.
		  3. **Scalabilità**: Il metodo DH può essere facilmente esteso a robot con più giunti, poiché si possono costruire matrici di trasformazione per ogni giunto e moltiplicarle insieme per ottenere la cinematica completa del robot.
	- ***Limiti della Convenzione DH***:
		- Sebbene la convenzione di Denavit-Hartenberg sia molto utilizzata, ha alcuni limiti:
			- ==Non sempre è immediato scegliere i sistemi di riferimento locali per ciascun giunto, specialmente in robot con geometrie complesse o con giunti particolari==.
			- ==La convenzione DH standard può risultare complicata quando ci sono angoli particolari o giunti con configurazioni inusuali==.
		- Per superare alcune di queste difficoltà, sono state proposte delle varianti della convenzione DH, come la **Convenzione DH Modificata**.
	- ***Sintesi***:
		- La **convenzione di Denavit-Hartenberg** è uno dei metodi più comuni per descrivere la cinematica dei manipolatori robotici.<br>Essa permette di rappresentare in modo compatto e sistematico la relazione tra i giunti di un robot e di calcolare facilmente la posizione e l'orientamento dell'end-effector.<br>Grazie a questo metodo, è possibile trattare robot con strutture complesse e analizzare i loro movimenti in modo efficiente.
