---
aliases:
  - catena cinematica
  - links
  - joints
  - giunti
  - catena cinematica aperta
  - catena cinematica chiusa
---
- ***Catena Cinemantica, spiegazione ed esempi***<br>(*ChatGPT 4o*)
	- ==Una **catena cinematica** è una sequenza di corpi rigidi (chiamati **link**) collegati tra loro tramite **giunti** (o **joints**) che permettono movimenti relativi tra i link==.<br>In robotica, una catena cinematica viene utilizzata per rappresentare la struttura di un robot o di una parte del corpo umano, descrivendo come i movimenti dei giunti influenzano la posizione e l'orientamento dei vari segmenti.
	- ***Definizione di Catena Cinematica***:
		- **Link**: ==I segmenti rigidi che compongono il robot o la struttura==.<br>Ogni link è collegato a un altro link attraverso un giunto.
		- **Giunti**: ==Sono le connessioni tra i link che permettono il movimento relativo==.<br>Esistono due tipi principali di giunti:
			  1. **Giunti revoluti** (o rotativi): ==Consentono la rotazione tra due link attorno a un asse fisso==.
			  2. **Giunti prismatici** (o lineari): ==Consentono una traslazione lineare tra due link lungo un asse==.
		- Una catena cinematica può essere:
			- **Aperta**: Se è una sequenza di link e giunti che **==non== forma un circuito chiuso**.<br>==Esempio tipico è un braccio robotico==.
			- **Chiusa**: Se i link e i giunti **formano un circuito chiuso**.<br>==Un esempio è il parallelogramma articolato==.
	- ***Tipi di Catene Cinematiche***:
		1. **Catena Cinematica Aperta**:<br>Una catena cinematica aperta è una sequenza di link collegati tramite giunti in cui ogni link è connesso al precedente e al successivo, ma l'ultimo link non si collega al primo. Questo tipo di catena si trova spesso nei manipolatori robotici.
			- **Esempio**: Un braccio robotico industriale con più segmenti (link) e giunti. Ogni giunto permette un movimento (rotazione o traslazione), e la posizione finale dell'end-effector (la mano o l'utensile del robot) è determinata dalla configurazione dei giunti.
		2. **Catena Cinematica Chiusa**:<br>In una catena cinematica chiusa, i link formano un circuito chiuso, dove l'ultimo link è collegato al primo. Questo tipo di catena viene utilizzato in meccanismi che richiedono precisione e stabilità.
			- **Esempio**: Il meccanismo di un parallelogramma articolato, utilizzato in alcune strutture robotiche per mantenere una configurazione stabile o per applicare forze con maggiore controllo.
	- ***Esempio di Catena Cinematica Aperta: Braccio Robotico***:<br>Consideriamo un braccio robotico con **3 giunti revoluti** e 3 link. Ogni giunto consente la rotazione attorno a un asse, permettendo al robot di spostare il suo end-effector (ad esempio, una pinza o un utensile) nello spazio.
		- ***Componenti***:
			- **Base**: Il primo link è attaccato alla base del robot.
			- **Giunto 1**: Il primo giunto è revoluto e permette al primo link di ruotare attorno all'asse $z_0$.
			- **Link 1**: Un segmento rigido che si estende dal giunto 1 al giunto 2.
			- **Giunto 2**: Un altro giunto revoluto che permette a link 2 di ruotare attorno a un asse relativo a link 1.
			- **Link 2**: Un altro segmento rigido che si estende dal giunto 2 al giunto 3.
			- **Giunto 3**: Un giunto revoluto alla fine del secondo segmento che permette una rotazione finale.
			- **End-effector**: La parte finale del robot che compie il lavoro (es. pinza o strumento).
		- Ogni giunto nel braccio robotico aggiunge un **grado di libertà** (DOF) al sistema. In questo caso, il robot ha 3 gradi di libertà, corrispondenti alle 3 rotazioni possibili attorno ai giunti.
		- La **cinematica diretta** di questo robot determina la posizione dell'end-effector in base agli angoli dei giunti, mentre la **cinematica inversa** calcola gli angoli dei giunti necessari per raggiungere una specifica posizione dell'end-effector.
	- ***Esempio di Catena Cinematica Chiusa: Meccanismo a Parallelogramma***:<br>Un esempio di catena cinematica chiusa è il **meccanismo a parallelogramma articolato**. Questo tipo di struttura ha quattro link collegati da giunti in modo tale che, quando uno dei giunti si muove, gli altri giunti si muovono in modo coordinato, mantenendo una geometria parallelogrammatica.
		- ***Componenti***:
			- **Link A, B, C, D**: Quattro link connessi da giunti in modo da formare un parallelogramma.
			- **Giunti**: I giunti collegano i link in modo che il movimento di un giunto provoca il movimento sincronizzato degli altri giunti. In questo caso, ogni link rimane parallelo al link opposto durante il movimento.
		- Questo tipo di meccanismo viene utilizzato per mantenere un orientamento fisso o per amplificare il movimento.
		- **Esempio applicativo**: Un meccanismo parallelogramma è usato in alcuni tipi di robot a delta per garantire che l'end-effector rimanga sempre parallelo alla base.
	- ***Utilità delle Catene Cinematiche in Robotica***:
		  1. **Manipolazione Robotica**: Le catene cinematiche aperte, come i bracci robotici, sono ampiamente utilizzate nella robotica per manipolare oggetti, eseguire operazioni di assemblaggio e svolgere compiti che richiedono movimenti precisi.<br>La cinematica di queste catene determina come i giunti devono essere configurati per raggiungere una certa posizione o orientazione.
		  2. **Meccanismi di Precisione**: Le catene cinematiche chiuse vengono spesso utilizzate in meccanismi che richiedono alta precisione e stabilità.<br>Un esempio è il meccanismo parallelogramma utilizzato nei robot delta per ottenere movimenti rapidi e precisi.
		  3. **Progettazione di Sistemi Robotici**: La comprensione delle catene cinematiche è essenziale per progettare robot in grado di svolgere compiti complessi in modo efficiente.<br>Sia le catene aperte che chiuse offrono diverse caratteristiche di movimento, adattabili a varie applicazioni.
	- ***Differenze tra Catene Cinematiche Aperte e Chiuse***:
		- **Catena Aperta**: 
			- ==Più flessibile==.
			- Utilizzata in robot manipolatori.
			- ==Il movimento finale dell'end-effector è determinato dai giunti precedenti, ma ogni giunto ha una libertà di movimento indipendente==.
		- **Catena Chiusa**:
			- ==Più stabile e precisa==.
			- Utilizzata in meccanismi paralleli (come i robot delta).
			- ==Il movimento di un giunto influisce simultaneamente su tutti gli altri giunti, fornendo stabilità e sincronizzazione==.
	- ***Sintesi***:
		- Una **catena cinematica** è una rappresentazione dei movimenti possibili di un sistema di link collegati da giunti, ed è ampiamente utilizzata nella robotica per descrivere bracci manipolatori, meccanismi paralleli, e altre strutture meccaniche. Le catene cinematiche possono essere aperte o chiuse, e ciascun tipo ha applicazioni specifiche in base alle esigenze di flessibilità o precisione del sistema.
