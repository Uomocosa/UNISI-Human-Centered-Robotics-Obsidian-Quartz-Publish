- t
	- I **gradi di libertà (DOF, Degrees of Freedom)** si riferiscono al numero di parametri indipendenti che definiscono la configurazione o lo stato di un sistema meccanico.<br>In robotica e biomeccanica, i gradi di libertà descrivono il numero di movimenti indipendenti che un robot o una parte del corpo può compiere nello spazio tridimensionale.
	- ***Definizione Generale***:<br>Per un sistema meccanico, ogni **grado di libertà** rappresenta una direzione o un asse lungo il quale il sistema può muoversi o ruotare.<br>Un oggetto libero nello spazio tridimensionale ha 6 gradi di libertà:
		- **3 gradi di libertà di traslazione**: Movimento lungo gli assi $x$, $y$, $z$.
		- **3 gradi di libertà di rotazione**: Rotazione attorno agli assi $x$, $y$, $z$.
		- Questi gradi di libertà sono importanti perché determinano la capacità di un sistema di raggiungere una determinata posizione e orientamento nello spazio.
	- ***Tipi di Gradi di Libertà***:
		1. **Gradi di Libertà di Traslazione**:
		   - Descrivono lo spostamento lineare di un oggetto lungo gli assi cartesiani $x$, $y$ e $z$.
		   - Ogni asse di traslazione aggiunge un grado di libertà.
		   - Un esempio di traslazione lungo un asse è il movimento di un'ascensore, che si sposta verticalmente lungo l'asse $z$.
		2. **Gradi di Libertà di Rotazione**:
		   - Descrivono la capacità di un oggetto di ruotare attorno agli assi $x$, $y$ e $z$.
		   - Ogni asse di rotazione aggiunge un grado di libertà.
		   - Ad esempio, la rotazione della testa attorno al collo rappresenta un grado di libertà di rotazione attorno a un asse verticale.
	- ***Esempio: Movimento in 2D e 3D***:
		- **Punto nel piano 2D**: Un punto su un piano bidimensionale ha **2 gradi di libertà** (può muoversi lungo l'asse $x$ e l'asse $y$).
		  - Esempio: Una formica che cammina su un foglio di carta può spostarsi lungo due direzioni indipendenti (orizzontale e verticale), quindi ha 2 gradi di libertà.
		- **Oggetto nello spazio 3D**: Un oggetto rigido libero nello spazio tridimensionale ha **6 gradi di libertà**: 3 di traslazione (lungo $x$, $y$, $z$) e 3 di rotazione (attorno a $x$, $y$, $z$).
		  - Esempio: Un aereo in volo può muoversi in avanti/indietro (traslazione lungo $x$), salire/scendere (traslazione lungo $z$), virare a sinistra/destra (rotazione attorno a $z$, chiamata **yaw**), inclinarsi lateralmente (rotazione attorno a $x$, chiamata **roll**), e inclinarsi verso l'alto o il basso (rotazione attorno a $y$, chiamata **pitch**).
	- ***Esempio di un Braccio Robotico***:<br>Un **braccio robotico** è spesso modellato come una **catena cinematica** formata da segmenti rigidi connessi da giunti.<br>Ogni giunto aggiunge gradi di libertà al sistema.<br>In un braccio robotico, i gradi di libertà sono solitamente definiti dai giunti **revoluti** (che permettono la rotazione) o **prismatici** (che permettono la traslazione).
		- **Braccio robotico a 6 DOF**: Un braccio robotico con 6 gradi di libertà è uno dei modelli più comuni.<br>I suoi 6 gradi di libertà gli permettono di raggiungere qualsiasi posizione e orientamento nello spazio tridimensionale.<br>Un tipico braccio robotico industriale ha:
		  - 3 gradi di libertà per spostare la "mano" (end-effector) in qualsiasi punto dello spazio tridimensionale.
		  - 3 gradi di libertà per orientare la mano in qualsiasi direzione.
		- Ecco come i 6 gradi di libertà potrebbero essere distribuiti in un braccio robotico:
		- **3 DOF di rotazione** nei primi giunti, per consentire movimenti del braccio attorno all'origine.
		- **3 DOF di rotazione** negli ultimi giunti, per consentire la manipolazione e orientamento dell'end-effector.
	- ***Esempi Pratici***:
		1. **Mano Umana**: 
		   - La mano ha molti gradi di libertà.<br>Ad esempio, il polso ha 3 gradi di libertà: flessione/estensione (su/giù), deviazione radiale/ulnare (sinistra/destra), e pronazione/supinazione (rotazione del polso).<br>Ogni dito ha diversi gradi di libertà nei giunti che permettono la flessione e l'estensione delle falangi.
		2. **Veicolo**:
		   - Un'auto su strada ha **3 gradi di libertà**: traslazione lungo l'asse $x$ (avanti e indietro), traslazione lungo l'asse $y$ (sinistra e destra quando sterza), e rotazione attorno all'asse $z$ (virata in curva, cioè "yaw").
		3. **Manipolatore robotico**: 
		   - Un manipolatore robotico con **7 gradi di libertà** ha maggiore flessibilità, in quanto può risolvere problemi di cinematica ridondante, cioè può raggiungere la stessa posizione in modi diversi, fornendo maggiore precisione o evitando ostacoli.
	- ***Gradi di Libertà in Sistemi Ridotti***:
		- **Catene cinematiche chiuse**: Se un sistema ha vincoli che limitano i movimenti (come in una catena cinematica chiusa), i gradi di libertà del sistema si riducono.<br>Per esempio, un braccio robotico che opera all'interno di una struttura chiusa potrebbe avere limitazioni di movimento, riducendo il numero di gradi di libertà effettivi.
		- **Robot a base mobile**: Se un robot è montato su una base mobile (come un robot su ruote), la base stessa potrebbe avere 2 o 3 gradi di libertà aggiuntivi, aumentando la capacità del sistema di muoversi.
	- ***Sintesi***:<br>In sintesi, i **gradi di libertà** descrivono le possibilità di movimento di un sistema meccanico.<br>In robotica, ogni giunto aggiunge un grado di libertà al robot, e la somma totale dei gradi di libertà determina quanto liberamente un robot può muoversi o manipolare oggetti nello spazio.
----
