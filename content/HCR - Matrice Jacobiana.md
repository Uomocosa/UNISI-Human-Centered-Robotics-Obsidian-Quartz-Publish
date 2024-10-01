---
aliases:
  - Jacobiana
  - Jacobian
  - matrice Jacobiana
  - Jacobian matrix
---
- ***References***:
	1. [[HCR - Cinematica Diretta di un Manipolatore Robotico (Lecture)|Jacobiana analitica]] 
	2. [[HCR - Grasping (Lecture)|Jacobiana della mano]] 
	3. [[HCR - Calcolo della Matrice Jacobiana 'della Mano']] 
	4. ***Exams***:
		- [[HCR ~ Exam 2022-01-26]] 
----
- ***Matrice Jacobiana, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- La **matrice Jacobiana** è uno strumento matematico utilizzato in robotica per descrivere la relazione tra le velocità dei giunti di un robot e la velocità (lineare e angolare) dell'end-effector.<br>La Jacobiana è fondamentale per analizzare e controllare i movimenti dei manipolatori robotici, e permette di calcolare anche le forze e i momenti torcenti sui giunti a partire dalle forze applicate all'end-effector.
	- ***Definizione della Matrice Jacobiana***:<br>La **matrice Jacobiana** è una matrice che descrive il tasso di variazione della posizione e dell'orientamento dell'end-effector rispetto ai parametri dei giunti.<br>Essa fornisce una mappatura tra le velocità dei giunti e le velocità dell'end-effector.
		- In un robot con $n$ gradi di libertà, la matrice Jacobiana $J(\theta)$ ha dimensioni $6 \times n$, dove:
		- Le prime 3 righe descrivono la **velocità lineare** dell'end-effector rispetto agli assi $x$, $y$ e $z$.
		- Le ultime 3 righe descrivono la **velocità angolare** dell'end-effector rispetto agli assi $x$, $y$ e $z$.
		- In generale, la matrice Jacobiana si ottiene prendendo le derivate parziali della posizione e dell'orientamento dell'end-effector rispetto agli angoli dei giunti.
	- ***Relazione Cinematica***:
		- Se consideriamo $q = [q_1, q_2, ..., q_n]^T$ come il vettore degli angoli dei giunti e $\dot{q} = [\dot{q}_1, \dot{q}_2, ..., \dot{q}_n]^T$ come il vettore delle velocità dei giunti, la **velocità dell'end-effector** $v_{eff}$ è data da:$$v_{eff} = J(q) \cdot \dot{q}$$Dove:
		- $v_{eff}$ è il vettore di velocità dell'end-effector (che include sia velocità lineare che angolare).
		- $J(q)$ è la matrice Jacobiana che dipende dagli angoli dei giunti.
		- $\dot{q}$ è il vettore delle velocità angolari dei giunti.
	- ***Esempio Semplice: Braccio Robotico a 2 Giunti***:
		- Consideriamo un **braccio robotico a 2 giunti** revoluti (simile al caso del piano 2D) con lunghezze dei segmenti $L_1$ e $L_2$.<br>Gli angoli dei giunti sono $\theta_1$ e $\theta_2$.<br>Vogliamo calcolare la Jacobiana per ottenere la velocità dell'end-effector.
		- La posizione dell'end-effector $(x_{\text{eff}}, y_{\text{eff}})$ è data dalle equazioni di cinematica diretta:$$\begin{array}{l}x_{\text{eff}} = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2) \\ y_{\text{eff}} = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)\end{array}$$La Jacobiana si ottiene derivando la posizione dell'end-effector rispetto agli angoli $\theta_1$ e $\theta_2$:$$J(\theta) = \begin{bmatrix} \frac{\partial x_{\text{eff}}}{\partial \theta_1} & \frac{\partial x_{\text{eff}}}{\partial \theta_2} \\ \frac{\partial y_{\text{eff}}}{\partial \theta_1} & \frac{\partial y_{\text{eff}}}{\partial \theta_2} \end{bmatrix} = \begin{bmatrix} - L_1 \sin(\theta_1) - L_2 \sin(\theta_1 + \theta_2) & -L_2 \sin(\theta_1 + \theta_2) \\ L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2) & L_2 \cos(\theta_1 + \theta_2) \end{bmatrix}$$Questa è la **matrice Jacobiana** del braccio robotico a 2 giunti.<br>La Jacobiana permette di calcolare la velocità dell'end-effector in termini delle velocità angolari dei giunti $\dot{\theta_1}$ e $\dot{\theta_2}$:$$\begin{bmatrix} \dot{x}_{\text{eff}} \\ \dot{y}_{\text{eff}} \end{bmatrix} = J(\theta) \cdot \begin{bmatrix} \dot{\theta_1} \\ \dot{\theta_2} \end{bmatrix}$$Dove $\dot{x}_{\text{eff}}$ e $\dot{y}_{\text{eff}}$ rappresentano le componenti della velocità lineare dell'end-effector.
	- ***Forze e Momenti***:
		- La Jacobiana non è utile solo per calcolare le velocità, ma anche per analizzare le forze e i momenti nei giunti del robot.<br>Conoscendo la forza applicata all'end-effector, è possibile calcolare i momenti torcenti ($\tau$) sui giunti.
		- Dato un vettore di forze applicate all'end-effector $F_{eff}$, i **momenti torcenti** $\tau$ sui giunti sono calcolati come:$$\tau = J^T(q) \cdot F_{eff}$$Dove $J^T(q)$ è la **trasposta** della Jacobiana.
	- ***Singularità della Matrice Jacobiana***:<br>Un concetto importante associato alla Jacobiana è quello delle **singolarità**.<br>Una singolarità si verifica quando la matrice Jacobiana perde rango (il suo determinante diventa zero).<br>In queste condizioni, il robot perde uno o più gradi di libertà nel movimento, e diventa impossibile controllare completamente l'end-effector.
		- **Esempio di Singolarità**: Nel braccio robotico a 2 giunti, una singolarità si verifica quando il braccio è completamente esteso o completamente ripiegato, perché in queste configurazioni il robot non è più in grado di muoversi lungo tutte le direzioni nel piano.
	- ***Esempio: Braccio Robotico a 3 Giunti nello Spazio 3D***:
		- Consideriamo ora un braccio robotico a 3 giunti nello spazio tridimensionale.<br>La posizione dell'end-effector è descritta dalle coordinate $(x, y, z)$ nello spazio 3D, e ogni giunto ruota attorno a un asse diverso.
		- Per un robot a 3 giunti, la Jacobiana sarà una matrice $3 \times 3$ che descrive la velocità lineare dell'end-effector in funzione delle velocità angolari dei giunti $\theta_1$, $\theta_2$, $\theta_3$.$$J(\theta) = \begin{bmatrix} \frac{\partial x}{\partial \theta_1} & \frac{\partial x}{\partial \theta_2} & \frac{\partial x}{\partial \theta_3} \\ \frac{\partial y}{\partial \theta_1} & \frac{\partial y}{\partial \theta_2} & \frac{\partial y}{\partial \theta_3} \\ \frac{\partial z}{\partial \theta_1} & \frac{\partial z}{\partial \theta_2} & \frac{\partial z}{\partial \theta_3} \end{bmatrix}$$Questa Jacobiana consente di calcolare la velocità dell'end-effector e di analizzare le forze e i momenti torcenti sui giunti.
	- ***Applicazioni della Jacobiana in Robotica***:
		1. **Controllo dei Robot**: La Jacobiana viene utilizzata nei controllori robotici per convertire le velocità dei giunti in velocità dell'end-effector e viceversa.
		2. **Analisi delle Forze**: È utilizzata per calcolare i momenti torcenti necessari nei giunti per sostenere le forze applicate all'end-effector.
		3. **Cinematica Inversa**: La Jacobiana è importante per risolvere problemi di cinematica inversa, poiché può essere utilizzata per iterare verso soluzioni che soddisfano i requisiti di posizione e orientamento dell'end-effector.
		4. **Singolarità**: Analizzare la Jacobiana aiuta a identificare configurazioni in cui il robot perde gradi di libertà (singolarità) e quindi a evitare queste configurazioni problematiche.
	- ***Sintesi***:<br>La **matrice Jacobiana** è un concetto chiave in robotica, utilizzato per collegare le velocità dei giunti con le velocità dell'end-effector e per calcolare le forze e i momenti torcenti.<br>La sua importanza si estende alla cinematica, al controllo dei robot e all'analisi delle singolarità.<br>Questa Jacobiana consente di calcolare la velocità dell'end-effector e di analizzare le forze e i momenti torcenti sui giunti.
----
