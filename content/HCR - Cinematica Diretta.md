---
aliases:
  - cinematica diretta
---

- ***Cinematica Diretta, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- ==La **cinematica diretta** è un concetto fondamentale nella robotica che descrive come determinare la **posizione** e l'**orientamento** dell'end-effector (la "mano" o lo strumento di lavoro) di un robot, dato un insieme di configurazioni o angoli dei giunti del robot stesso==.<br>==In altre parole, con la cinematica diretta, si conoscono le posizioni dei giunti e si vuole calcolare dove si trova l'***end-effector*** nello spazio==.
	- ***Definizione***:
		- La cinematica diretta riguarda il calcolo della **posizione** e **orientazione** dell'end-effector in funzione dei parametri di configurazione del robot, come gli angoli di rotazione (per giunti revoluti) o la distanza di traslazione (per giunti prismatici).
		- Dato un robot con $n$ giunti, ciascun giunto ha un certo valore (ad esempio, un angolo per un giunto revoluto o una distanza per un giunto prismatico), e la cinematica diretta risolve la seguente domanda: **dove si trova l'end-effector, data la configurazione dei giunti?**
	- ***Esempio di Cinematica Diretta: Braccio Robotico a 2 Giunti***:
		- Supponiamo di avere un **braccio robotico a 2 giunti revoluti** in un piano bidimensionale (2D). Ogni giunto può ruotare di un angolo $\theta_1$ e $\theta_2$, e il braccio è costituito da due segmenti rigidi di lunghezze $L_1$ e $L_2$.
	- ***Descrizione del braccio***:
		- Il **primo giunto** ruota attorno all'origine e controlla il primo segmento di lunghezza $L_1$.
		- Il **secondo giunto** è montato all'estremità del primo segmento e controlla il secondo segmento di lunghezza $L_2$.
		- L'end-effector si trova all'estremità del secondo segmento.
	- ***Obiettivo***:
		- Determinare la posizione $(x_{\text{eff}}, y_{\text{eff}})$ dell'end-effector in funzione degli angoli $\theta_1$ e $\theta_2$.
	- ***Equazioni di Cinematica Diretta***:
		- Per trovare la posizione dell'end-effector, possiamo decomporre il problema in due passaggi:
			1. **Posizione del primo giunto** rispetto all'origine (0,0):
				- Il primo segmento ha una lunghezza $L_1$ e ruota di un angolo $\theta_1$.
				- Le coordinate dell'estremità del primo segmento sono:$$     x_1 = L_1 \cos(\theta_1)     $$$$     y_1 = L_1 \sin(\theta_1)     $$
			2. **Posizione dell'end-effector** rispetto al primo giunto:
				- Il secondo segmento ha una lunghezza $L_2$ e ruota di un angolo $\theta_2$ rispetto al primo segmento.
				- Le coordinate dell'end-effector sono date da:$$     x_{\text{eff}} = x_1 + L_2 \cos(\theta_1 + \theta_2) = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)     $$ $$     y_{\text{eff}} = y_1 + L_2 \sin(\theta_1 + \theta_2) = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)     $$Queste equazioni descrivono la **cinematica diretta** del braccio robotico a 2 giunti. Dati i valori di $\theta_1$ e $\theta_2$, puoi determinare la posizione finale dell'end-effector nello spazio 2D.
	- ***Estensione al 3D e Catene Cinematiche***:
		- Per un **robot nello spazio tridimensionale (3D)**, la cinematica diretta diventa più complessa, perché non solo dobbiamo considerare la **posizione** dell'end-effector, ma anche il suo **orientamento** (ossia, la sua rotazione nello spazio 3D). Questo si realizza tipicamente attraverso matrici di trasformazione omogenea, che combinano rotazioni e traslazioni.
	- ***Esempio: Braccio Robotico a 3 Giunti nello Spazio 3D***:
		- Consideriamo un braccio robotico a 3 giunti, con ciascun giunto in grado di ruotare attorno a uno dei tre assi cartesiani $x$, $y$ e $z$.<br>La posizione e orientazione dell'end-effector possono essere determinate usando **matrici di rotazione** e **trasformazioni omogenee**.
		- La posizione finale dell'end-effector in 3D è ottenuta moltiplicando insieme le matrici di trasformazione associate a ciascun giunto, partendo dall'origine fino all'end-effector.
	- ==***Denavit-Hartenberg (DH) Parameters***==:
		- ==Un metodo sistematico per descrivere la cinematica diretta dei robot è l'uso dei **parametri di Denavit-Hartenberg (DH)**==.<br>==Questo metodo descrive la relazione tra i giunti e i link di un robot mediante una serie di parametri standardizzati, come==:
			- ==La distanza tra i giunti==.
			- ==L'angolo tra i link==.
			- ==La lunghezza dei link==.
			- ==L'angolo di torsione tra i giunti==.
		- ==Il metodo DH permette di costruire matrici di trasformazione omogenea per descrivere la posizione e l'orientamento di ogni giunto in funzione degli altri, semplificando notevolmente il calcolo della cinematica diretta per robot complessi==.
	- ***Applicazioni della Cinematica Diretta***:
		  1. **Manipolatori Robotici**: La cinematica diretta è essenziale per determinare dove si troverà l'end-effector di un manipolatore robotico, data una serie di input sui giunti.<br>Ad esempio, in un braccio robotico industriale, è fondamentale sapere esattamente dove si troverà l'utensile in base agli angoli dei giunti per eseguire compiti di precisione.
		  2. **Robot Mobile**: Anche per robot mobili con braccia meccaniche, la cinematica diretta è utilizzata per calcolare la posizione finale dell'end-effector, che può essere utilizzato per compiti di raccolta o manipolazione.
		  3. **Grafica 3D**: Nel campo della grafica 3D, la cinematica diretta viene utilizzata per calcolare il movimento di personaggi o modelli tridimensionali articolati, come il movimento delle articolazioni di un personaggio animato.
	- ***Differenze tra Cinematica Diretta e Cinematica Inversa***:
		- **Cinematica Diretta**: ==Dati gli angoli o le configurazioni dei giunti, calcola la posizione e l'orientamento dell'end-effector==.
		- **Cinematica Inversa**: ==Dato un obiettivo per la posizione e l'orientamento dell'end-effector, calcola gli angoli dei giunti necessari per raggiungere quell'obiettivo==.<br>==Questo è generalmente più complesso e richiede la risoluzione di equazioni non lineari==.
	- ***Riassunto***:
		- La **cinematica diretta** è il processo mediante il quale, a partire dagli angoli e dalle configurazioni dei giunti di un robot, si determina la posizione e l'orientamento finale dell'end-effector.<br>Questo è un concetto centrale nella robotica ed è fondamentale per il controllo dei robot e per la loro interazione con l'ambiente.
