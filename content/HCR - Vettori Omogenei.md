---
aliases:
  - vettori omogenei
---
- ***Vettori Omogenei, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- I **vettori omogenei** sono una rappresentazione estesa dei vettori utilizzata in geometria e robotica per semplificare le operazioni di **traslazione** e **rotazione** nello spazio. Sono particolarmente utili quando si lavora con matrici di trasformazione per combinare traslazioni e rotazioni in un'unica operazione.
	- ***Concetto di Vettori Omogenei***:
		- Un vettore normale in uno spazio tridimensionale (3D) è tipicamente rappresentato da tre componenti:$$\mathbf{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$$Questa rappresentazione è sufficiente per operazioni come rotazioni, ma non per le **traslazioni**. Per includere sia le rotazioni che le traslazioni, si utilizza la **rappresentazione omogenea**, che aggiunge una quarta componente al vettore. ==Un vettore omogeneo 3D è scritto come==:$$\mathbf{v_h} = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$L'ultima componente, il **fattore omogeneo** (tipicamente 1), permette di trattare rotazioni e traslazioni all'interno di un unico formalismo matriciale.
	- ***Matrici di Trasformazione Omogenea***:
		- Per comprendere l'utilità dei vettori omogenei, dobbiamo introdurre le **matrici di trasformazione omogenea**, che combinano rotazioni e traslazioni in una singola operazione. ==La matrice di trasformazione omogenea per lo spazio 3D è una matrice 4x4 che ha la forma==:$$T = \begin{bmatrix} R & d \\0 & 1\end{bmatrix}$$Dove:
			- ==$R$ è una matrice 3x3 di rotazione==.
			- ==$d$ è un vettore 3x1 che rappresenta la traslazione==.
			- ==La riga $[0, 0, 0, 1]$ permette di mantenere la struttura omogenea==.
		- Questa matrice viene utilizzata per applicare sia rotazioni che traslazioni a un vettore omogeneo in un'unica operazione.
	- ***Esempio 1: Applicazione di una Traslazione***:
		- Supponiamo di avere un punto $P = (x, y, z)$ nello spazio e vogliamo traslarlo di un vettore di traslazione $d = (dx, dy, dz)$.
		- Il vettore omogeneo per $P$ è:$$P_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$La matrice di trasformazione omogenea che rappresenta solo la traslazione $d$ è:$$T = \begin{bmatrix} 1 & 0 & 0 & dx \\0 & 1 & 0 & dy \\0 & 0 & 1 & dz \\0 & 0 & 0 & 1\end{bmatrix}$$Per ottenere il nuovo punto traslato, moltiplichiamo la matrice di trasformazione per il vettore omogeneo $P_h$:$$P'_h = T \cdot P_h = \begin{bmatrix} 1 & 0 & 0 & dx \\0 & 1 & 0 & dy \\0 & 0 & 1 & dz \\0 & 0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}= \begin{bmatrix} x + dx \\ y + dy \\ z + dz \\ 1 \end{bmatrix}$$Quindi il nuovo punto è traslato di $d$, mantenendo la rappresentazione omogenea.
	- ***Esempio 2: Applicazione di una Rototraslazione***:
		- Supponiamo di avere una combinazione di una rotazione attorno all'asse $z$ di un angolo $\theta$ e una traslazione $d = (dx, dy, dz)$. La matrice di trasformazione omogenea per questa operazioneè:$$T = \begin{bmatrix}\cos\theta & -\sin\theta & 0 & dx \\\sin\theta & \cos\theta & 0 & dy \\0 & 0 & 1 & dz \\0 & 0 & 0 & 1\end{bmatrix}$$Se applichiamo questa trasformazione a un vettore omogeneo$$P_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}$$Il risultato è:$$P'_h = T \cdot P_h = \begin{bmatrix}\cos\theta & -\sin\theta & 0 & dx \\\sin\theta & \cos\theta & 0 & dy \\0 & 0 & 1 & dz \\0 & 0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}= \begin{bmatrix} x' \\ y' \\ z' \\ 1 \end{bmatrix}$$Dove:$$x' = x\cos\theta - y\sin\theta + dx$$$$y' = x\sin\theta + y\cos\theta + dy$$$$z' = z + dz$$Quindi il punto $P_h$ è stato prima ruotato attorno all'asse $z$ e poi traslato di $d$.
	- ***Vantaggi dell'uso di Vettori Omogenei***:
		  1. **Combinazione di rotazioni e traslazioni**: Utilizzando vettori omogenei e matrici di trasformazione omogenea, possiamo combinare rotazioni e traslazioni in un'unica operazione matriciale.
		  2. **Uniformità**: Le operazioni geometriche possono essere eseguite in modo uniforme utilizzando moltiplicazioni di matrici, semplificando i calcoli per sistemi robotici complessi.
		  3. **Generalizzabilità**: I vettori omogenei possono essere utilizzati in spazi di dimensioni superiori, come nello spazio 4D per la grafica computerizzata o in altre applicazioni ingegneristiche.
		- In conclusione, i **vettori omogenei** sono una rappresentazione estesa dei vettori, particolarmente utile in robotica e grafica computazionale per eseguire rotazioni e traslazioni in maniera efficiente e compatta, permettendo di risolvere in modo uniforme problemi di manipolazione spaziale complessi.
