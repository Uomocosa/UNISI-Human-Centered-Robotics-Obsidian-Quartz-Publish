---
aliases:
  - nullspace
  - kernel
---
***Ricorda***:

> **Nullspace** e **kernel** sono nomi diversi ma significano la stessa cosa.

> Il **nullspace**/**kernel** è l'insieme di vettori $\{\mathbf{x_0} ,\ \mathbf{x_1} ,\ ... \}$ che rispettino la seguente equazione:$$A \mathbf{x_i} = \mathbf{0}$$Dove:
> - $A$ è una matrice di dimensioni $m \times n$.
> - $\mathbf{0}$ è il vettore nullo.

> Se il **nullspace**/**kernel** di una matrice è **vuoto**, ovvero l'unica soluzione dell'equazione $A \mathbf{x_i} = \mathbf{0}$, è $\mathbf{x} = \mathbf{0}$, allora: ==la matrice $\mathbf{A}$ ha [[HCR - Rango Massimo|rango massimo]]==.
> ***N.B.:*** ==Una matrice a rango massimo **non è detto** che abbia **nullspace**/**kernel** nullo==.

----
- ***Kernel di una Matrice, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- Il **kernel di una matrice** (detto anche **nucleo** o **spazio nullo**) è un concetto fondamentale in algebra lineare.<br>Il kernel di una matrice rappresenta l'insieme di tutti i vettori che, moltiplicati per la matrice, producono il vettore nullo.<br>In altre parole, il kernel contiene tutti i vettori che vengono "mandati a zero" dalla trasformazione lineare rappresentata dalla matrice.
	- ***Definizione Formale***:
		- Il **kernel** di una matrice $A$ è l'insieme di tutti i vettori $x$ tali che:$$A \cdot x = 0$$Dove:
		- $A$ è una matrice di dimensioni $m \times n$,
		- $x$ è un vettore $n \times 1$,
		- $0$ è il vettore nullo di dimensioni $m \times 1$.
		- Formalmente, il **kernel** di $A$, denotato come $\text{ker}(A)$, è dato da:$$\text{ker}(A) = \{ x \in \mathbb{R}^n \mid A \cdot x = 0 \}$$Il kernel è uno **spazio vettoriale** e contiene tutti i vettori che, quando moltiplicati per la matrice $A$, danno il vettore nullo.
	- ***Interpretazione Geometrica***:<br>Dal punto di vista geometrico, il kernel di una matrice rappresenta l'insieme di direzioni in cui una trasformazione lineare non ha alcun effetto, cioè, i vettori che vengono "compressi" nel vettore nullo.<br>Se il kernel contiene solo il vettore nullo, significa che la trasformazione lineare è **iniettiva** (cioè ogni vettore diverso viene trasformato in un vettore diverso).<br>Se il kernel contiene più vettori, significa che ci sono vettori che vengono mappati nello stesso risultato, quindi la trasformazione non è iniettiva.
	- ***Esempio 1: Matrice $2 \times 2$***:
		- Consideriamo una matrice $A$ di dimensioni $2 \times 2$:$$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$$Per trovare il kernel di $A$, risolviamo il sistema lineare $A \cdot x = 0$:$$\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$Il sistema di equazioni è:$$\begin{array}{l}1 \cdot x_1 + 2 \cdot x_2 = 0 \\ 2 \cdot x_1 + 4 \cdot x_2 = 0\end{array}$$Entrambe le equazioni sono ridondanti (la seconda è semplicemente il doppio della prima), quindi possiamo semplificare il sistema a:$$x_1 + 2x_2 = 0$$Da qui, possiamo risolvere $x_1 = -2x_2$.<br>Quindi, il kernel è lo spazio vettoriale generato dal vettore $\begin{bmatrix} -2 \\ 1 \end{bmatrix}$, ossia:$$\text{ker}(A) = \left\{ t \begin{bmatrix} -2 \\ 1 \end{bmatrix} \mid t \in \mathbb{R} \right\}$$Il kernel di questa matrice è una retta nello spazio $\mathbb{R}^2$, che contiene tutti i multipli del vettore $\begin{bmatrix} -2 \\ 1 \end{bmatrix}$.
	- ***Esempio 2: Matrice $3 \times 3$***:
		- Consideriamo la matrice $B$:$$B = \begin{bmatrix} 1 & 0 & -1 \\ 2 & 1 & 0 \\ -1 & 1 & 1 \end{bmatrix}$$Per trovare il kernel di $B$, dobbiamo risolvere $B \cdot x = 0$, cioè:$$\begin{bmatrix} 1 & 0 & -1 \\ 2 & 1 & 0 \\ -1 & 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$$Il sistema di equazioni risultante è:
		1. $x_1 - x_3 = 0 \rightarrow x_1 = x_3$
		2. $2x_1 + x_2 = 0 \rightarrow 2x_3 + x_2 = 0 \rightarrow x_2 = -2x_3$
		3. $-x_1 + x_2 + x_3 = 0 \rightarrow -x_3 + (-2x_3) + x_3 = 0$ (quest'ultima equazione è ridondante).
		- La soluzione generale è quindi:$$x_1 = x_3, \quad x_2 = -2x_3$$Quindi il vettore $x$ può essere espresso come:$$x = x_3 \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$$Il kernel di $B$ è quindi generato dal vettore $\begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$, ossia:$$\text{ker}(B) = \left\{ t \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix} \mid t \in \mathbb{R} \right\}$$Anche in questo caso, il kernel è una retta nello spazio $\mathbb{R}^3$.
	- ***Proprietà del Kernel***:
		1. **Spazio Vettoriale**: Il kernel di una matrice è sempre uno spazio vettoriale.<br>Contiene almeno il vettore nullo.
		2. **Dimensione del Kernel (Nullità)**: La dimensione del kernel di una matrice è detta **nullità** della matrice.<br>Se il kernel contiene solo il vettore nullo, la matrice è detta **iniettiva** (ossia la trasformazione associata è iniettiva).
		3. **Teorema del Rango**: Il **Teorema del Rango-Nullità** afferma che per una matrice $A$ di dimensioni $m \times n$, la somma del **rango** di $A$ e della **nullità** di $A$ è uguale a $n$ (il numero di colonne):$$\text{rango}(A) + \text{nullità}(A) = n$$Il rango di $A$ rappresenta il numero di colonne linearmente indipendenti, mentre la nullità rappresenta la dimensione del kernel di $A$.
	- ***Applicazioni del Kernel***:
		1. **Sistemi di Equazioni Lineari**: Il kernel di una matrice è cruciale per capire le soluzioni di un sistema di equazioni lineari.<br>Se il kernel contiene più del solo vettore nullo, allora il sistema ha **infinitamente molte soluzioni**.
		2. **Cinematica Robotica**: In robotica, il kernel della matrice Jacobiana di un manipolatore descrive i **movimenti nulli**, cioè i movimenti dei giunti che non cambiano la posizione dell'end-effector.
		3. **Teoria dei Controlli**: Nella teoria dei controlli, il kernel di una matrice può essere utilizzato per descrivere i **modi non osservabili** o i **modi non controllabili** di un sistema dinamico.
	- ***Sintesi***:
		- Il **kernel di una matrice** rappresenta l'insieme di vettori che vengono mappati nel vettore nullo dalla matrice.<br>Esso è uno spazio vettoriale che può essere utilizzato per analizzare le proprietà delle trasformazioni lineari, la solvibilità dei sistemi di equazioni lineari e i movimenti nulli nei sistemi meccanici.<br>Il kernel è un concetto chiave in algebra lineare e trova molte applicazioni in fisica, robotica e teoria dei controlli.<br>Il rango di $A$ rappresenta il numero di colonne linearmente indipendenti, mentre la nullità rappresenta la dimensione del kernel di $A$.
----
- ***Nullspace, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- ***Definizione***:<br>Il **nullspace** (o **nucleo** di una matrice) è l'insieme di tutti i vettori $\mathbf{x}$ che, moltiplicati per una matrice $A$, danno come risultato il vettore nullo (il vettore con tutti gli elementi pari a zero).<br>In altre parole, il nullspace è l'insieme delle soluzioni dell'equazione:$$A \mathbf{x} = \mathbf{0}$$Dove:
		- $A$ è una matrice di dimensioni $m \times n$.
		- $\mathbf{0}$ è il vettore nullo.
	- ***Spiegazione***:
		- In termini semplici, il nullspace di una matrice $A$ rappresenta tutti i vettori $\mathbf{x}$ che, quando moltiplicati per $A$, producono il vettore nullo.<br>Il nullspace può contenere uno o più vettori, o solo il vettore nullo stesso.<br>L'insieme dei vettori nel nullspace di una matrice forma uno **spazio vettoriale**.
		- Il nullspace è importante in molte applicazioni, inclusa la risoluzione di sistemi di equazioni lineari, l'analisi della cinematica dei robot, e nelle trasformazioni lineari.
		- ***Calcolo del Nullspace***:
		- Per trovare il nullspace di una matrice $A$, dobbiamo risolvere il sistema omogeneo $A \mathbf{x} = \mathbf{0}$.<br>Questo significa:
			1. Impostare l'equazione $A \mathbf{x} = \mathbf{0}$.
			2. Ridurre la matrice $A$ a **forma ridotta a scala** (tramite eliminazione di Gauss o altro metodo).
			3. Trovare le soluzioni del sistema di equazioni risultante.
			- Il **grado di libertà** delle soluzioni dipende dal **rango** della matrice:
			- Se il rango di $A$ è massimo (cioè uguale al numero di colonne della matrice), il nullspace contiene solo il vettore nullo.
			- Se il rango è minore del numero di colonne, ci sono soluzioni non banali nel nullspace.
		- ***Esempi***:
		1. **Matrice quadrata e nullspace banale**:
		   - Considera la matrice identità $A = I$:$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$Per trovare il nullspace di $I$, dobbiamo risolvere:$$I \mathbf{x} = \mathbf{0} \implies \mathbf{x} = \mathbf{0}$$Il nullspace di $I$ contiene solo il vettore nullo $\mathbf{0}$, quindi si dice che ha un **nullspace banale**.
		2. **Matrice con nullspace non banale**:
		   - Consideriamo una matrice $A$:$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$$Per trovare il nullspace di $A$, dobbiamo risolvere l'equazione:$$A \mathbf{x} = \mathbf{0} \implies \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$Questo sistema porta a:$$x_1 + 2x_2 = 0 \implies x_1 = -2x_2$$Quindi, il nullspace di $A$ è l'insieme di tutti i vettori della forma $\mathbf{x} = t \begin{pmatrix} -2 \\ 1 \end{pmatrix}$, dove $t$ è un qualsiasi numero reale.<br>In questo caso, il nullspace non è banale, e tutti i vettori nel nullspace sono multipli del vettore $\begin{pmatrix} -2 \\ 1 \end{pmatrix}$.
		3. **Nullspace in robotica**:
		   - Nella robotica, il nullspace è importante per analizzare la cinematica dei robot.<br>Ad esempio, quando si usa una **matrice Jacobiana** per calcolare le velocità o le forze dei giunti del robot, il nullspace della Jacobiana rappresenta quei movimenti o quelle forze che non influenzano direttamente il movimento dell'end-effector.<br>In altre parole, se il vettore di velocità o di forza si trova nel nullspace della Jacobiana, significa che questi movimenti non alterano la posizione dell'elemento terminale (end-effector) del robot.
		   - **Esempio**: Consideriamo un robot con due bracci che lavorano insieme per afferrare un oggetto.<br>Il nullspace della Jacobiana di questo sistema rappresenta i movimenti che i due bracci possono fare senza influenzare la presa dell'oggetto, cioè movimenti ridondanti o inutili rispetto al compito principale.
	- ***Applicazioni del Nullspace***:
		1. **Risoluzione di sistemi di equazioni**:
		   - Il nullspace è utile per determinare l'esistenza di soluzioni non banali a sistemi di equazioni lineari.<br>Se il nullspace contiene solo il vettore nullo, allora l'unica soluzione è quella banale (il vettore nullo).<br>Se il nullspace contiene altri vettori, esistono soluzioni multiple (o infinite).
		2. **Robotica**:
		   - Nella robotica, il nullspace della matrice Jacobiana è utilizzato per calcolare movimenti ridondanti che non influenzano l'end-effector.<br>Questi movimenti sono spesso utilizzati per ottimizzare la postura del robot o per evitare collisioni.
		3. **Grafica computerizzata e fisica**:
		   - In grafica 3D e simulazioni fisiche, il nullspace è utilizzato per modellare oggetti rigidi e per risolvere problemi di vincoli, come le forze che non causano movimento in un sistema vincolato.
	- ***Conclusione***:<br>Il nullspace è un concetto fondamentale in algebra lineare e ha numerose applicazioni in campi come la robotica, la fisica e l'ingegneria.<br>Esso rappresenta l'insieme di soluzioni di un sistema omogeneo e descrive i vettori che non hanno alcun effetto in determinate trasformazioni lineari o sistemi.
----
- ***Ho trovato un nullspace o kernel, vuoto, ovvero $x = \vec 0$, cosa comporta ciò?***
	- Quando il **kernel** o **nullspace** di una matrice è vuoto, cioè contiene solo il vettore nullo ($\vec{0}$), significa che la mappa lineare associata alla matrice è **iniettiva**.<br>In altre parole, l'unica soluzione dell'equazione omogenea $A \vec{x} = \vec{0}$ è il vettore nullo $\vec{x} = \vec{0}$.
	- Ecco le implicazioni principali:
		1. **Iniettività**: Se il kernel è vuoto, ogni vettore nello spazio di partenza viene mappato su un vettore distinto nello spazio di arrivo.<br>La trasformazione è quindi **iniettiva**.
		2. **Indipendenza lineare delle colonne**: Se il kernel è vuoto, le colonne della matrice sono **linearmente indipendenti**.<br>Non esiste nessuna combinazione lineare non banale delle colonne che dia il vettore nullo.
		3. **Non ci sono soluzioni multiple**: Quando si risolve $A \vec{x} = \vec{b}$, se il kernel è vuoto, ci sarà **al massimo una soluzione** per ogni vettore $\vec{b}$, oppure nessuna soluzione se $\vec{b}$ non è nello spazio immagine della matrice $A$.
		4. **Rango massimo**: Se il kernel è vuoto, il rango della matrice è uguale al numero delle sue colonne (se la matrice è quadrata, il rango sarà uguale alla dimensione della matrice).<br>Questo significa che la matrice è **non singolare** e ha un **determinante diverso da zero** (nel caso di matrici quadrate).
	- In sintesi, trovare un kernel vuoto è un segnale positivo per quanto riguarda la risolubilità e la proprietà della matrice associata a una trasformazione lineare.
----
