---
aliases:
  - Jacobiana della mano
---
- ***Come si calcola la "Matrice Jacobiana della Mano", spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- La **matrice Jacobiana della mano** (o più semplicemente **matrice Jacobiana**) in robotica si riferisce alla matrice che descrive la relazione tra le velocità dei giunti di un manipolatore robotico (in questo caso, la "mano" o l'**end-effector**) e la velocità lineare e angolare dell'end-effector stesso.<br>Essa è fondamentale per controllare i movimenti della mano robotica e determinare come le velocità e le forze applicate ai giunti influiscono sulla posizione e l'orientamento della mano.
	- ***Calcolo della Matrice Jacobiana della Mano***:<br>Per calcolare la **matrice Jacobiana** della mano, è necessario conoscere la **cinematica diretta** del manipolatore robotico, cioè le equazioni che descrivono la posizione e l'orientamento della mano in funzione degli angoli dei giunti.
		- Supponiamo che il manipolatore robotico abbia $n$ giunti, dove ogni giunto può ruotare (giunto revoluto) o traslare (giunto prismatico).<br>La Jacobiana è una matrice $6 \times n$, dove:
		- Le prime 3 righe rappresentano la relazione tra le velocità angolari dei giunti e la velocità lineare dell'end-effector.
		- Le ultime 3 righe rappresentano la relazione tra le velocità angolari dei giunti e la velocità angolare dell'end-effector.$$J(\theta) = \begin{bmatrix} \frac{\partial x}{\partial \theta_1} & \frac{\partial x}{\partial \theta_2} & \dots & \frac{\partial x}{\partial \theta_n} \\ \frac{\partial y}{\partial \theta_1} & \frac{\partial y}{\partial \theta_2} & \dots & \frac{\partial y}{\partial \theta_n} \\ \frac{\partial z}{\partial \theta_1} & \frac{\partial z}{\partial \theta_2} & \dots & \frac{\partial z}{\partial \theta_n} \\ \frac{\partial \phi_x}{\partial \theta_1} & \frac{\partial \phi_x}{\partial \theta_2} & \dots & \frac{\partial \phi_x}{\partial \theta_n} \\ \frac{\partial \phi_y}{\partial \theta_1} & \frac{\partial \phi_y}{\partial \theta_2} & \dots & \frac{\partial \phi_y}{\partial \theta_n} \\ \frac{\partial \phi_z}{\partial \theta_1} & \frac{\partial \phi_z}{\partial \theta_2} & \dots & \frac{\partial \phi_z}{\partial \theta_n} \end{bmatrix}$$Dove:
		- $x, y, z$ sono le coordinate della posizione dell'end-effector.
		- $\phi_x, \phi_y, \phi_z$ sono gli angoli di rotazione (orientamento) dell'end-effector.
		- $\theta_1, \theta_2, \dots, \theta_n$ sono le variabili di configurazione (ad esempio, gli angoli di rotazione o traslazione dei giunti).
	- ***Passaggi per il Calcolo della Jacobiana***:
		1. **Cinematica diretta**:
		   - Determina le equazioni che descrivono la posizione $x(\theta)$, $y(\theta)$, e $z(\theta)$ dell'end-effector in funzione degli angoli o traslazioni dei giunti.
		2. **Derivazione parziale**:
		   - Per calcolare ogni elemento della Jacobiana, prendi la **derivata parziale** della posizione o dell'orientamento dell'end-effector rispetto a ciascun angolo o traslazione del giunto.<br>Questo darà la sensibilità della posizione dell'end-effector rispetto ai movimenti di ciascun giunto.
		3. **Costruzione della Jacobiana**:
		   - Organizza le derivate parziali in una matrice $6 \times n$, dove $n$ è il numero di giunti.<br>Le prime 3 righe rappresentano la velocità lineare (posizione), mentre le ultime 3 righe rappresentano la velocità angolare (orientamento).
	- ***Esempio: Braccio Robotico a 2 Giunti***:
		- Consideriamo un semplice braccio robotico con due giunti revoluti, che si muove in un piano 2D.<br>Ogni giunto ha un angolo di rotazione $\theta_1$ e $\theta_2$, e le lunghezze dei segmenti sono $L_1$ e $L_2$.
		- La cinematica diretta (cioè la posizione dell'end-effector) è data da:$$\begin{array}{l}x = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2) \\ y = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)\end{array}$$Ora, calcoliamo le derivate parziali rispetto a $\theta_1$ e $\theta_2$:
		1. **Derivate parziali rispetto a $\theta_1$**:$$\begin{array}{l}\frac{\partial x}{\partial \theta_1} = -L_1 \sin(\theta_1) - L_2 \sin(\theta_1 + \theta_2) \\ \frac{\partial y}{\partial \theta_1} = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)\end{array}$$
		2. **Derivate parziali rispetto a $\theta_2$**:$$\begin{array}{l}\frac{\partial x}{\partial \theta_2} = -L_2 \sin(\theta_1 + \theta_2) \\ \frac{\partial y}{\partial \theta_2} = L_2 \cos(\theta_1 + \theta_2)\end{array}$$La Jacobiana per questo manipolatore $2D$ è quindi:$$J(\theta) = \begin{bmatrix} -L_1 \sin(\theta_1) - L_2 \sin(\theta_1 + \theta_2) & -L_2 \sin(\theta_1 + \theta_2) \\ L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2) & L_2 \cos(\theta_1 + \theta_2) \end{bmatrix}$$Questa Jacobiana descrive la relazione tra le velocità dei giunti ($\dot{\theta_1}, \dot{\theta_2}$) e la velocità dell'end-effector $(\dot{x}, \dot{y})$ nel piano 2D.
	- ***Uso della Matrice Jacobiana***:
		1. **Velocità dell'End-Effector**:
		   - Se conosci le velocità dei giunti $\dot{\theta}$, puoi calcolare la velocità dell'end-effector $\dot{x}$ come:$$\dot{x} = J(\theta) \cdot \dot{\theta}$$
		2. **Forze e Momenti**:
		   - La Jacobiana è anche utilizzata per calcolare come le forze applicate all'end-effector si traducono in **momenti torcenti** sui giunti:$$\tau = J^T(\theta) \cdot F$$Dove $\tau$ è il vettore dei momenti torcenti sui giunti e $F$ è il vettore delle forze applicate sull'end-effector.
		3. **Analisi delle Singolarità**:
		   - Le **singolarità** si verificano quando la Jacobiana perde rango (cioè, quando una o più righe diventano linearmente dipendenti).<br>In questi casi, il robot perde la capacità di muoversi liberamente in alcune direzioni, rendendo difficile il controllo dell'end-effector.
	- ***Esempio Esteso: Manipolatore 3D con 6 Giunti***:
		- Un robot con 6 gradi di libertà (DOF) che lavora nello spazio tridimensionale può essere descritto da una Jacobiana $6 \times 6$.<br>Per esempio, in un braccio robotico con sei giunti (come i bracci robotici industriali), la Jacobiana completa tiene conto delle 3 componenti della velocità lineare $(x, y, z)$ e delle 3 componenti della velocità angolare $(\phi_x, \phi_y, \phi_z)$.
		- Per calcolare la Jacobiana in 3D, si procede come nei casi precedenti, ma con:
		- Derivate parziali rispetto agli angoli dei giunti per le componenti di posizione $(x, y, z)$.
		- Derivate parziali per le componenti di orientamento $(\phi_x, \phi_y, \phi_z)$.
	- ***Sintesi***:
		- La **matrice Jacobiana della mano** in robotica rappresenta il legame tra le velocità dei giunti del manipolatore e la velocità dell'end-effector.<br>Si ottiene calcolando leDove $\tau$ è il vettore dei momenti torcenti sui giunti e $F$ è il vettore delle forze applicate sull'end-effector.
		3. **Analisi delle Singolarità**:
		   - Le **singolarità** si verificano quando la Jacobiana perde rango (cioè, quando una o più righe diventano linearmente dipendenti).<br>In questi casi, il robot perde la capacità di muoversi liberamente in alcune direzioni, rendendo difficile il controllo dell'end-effector.
----
