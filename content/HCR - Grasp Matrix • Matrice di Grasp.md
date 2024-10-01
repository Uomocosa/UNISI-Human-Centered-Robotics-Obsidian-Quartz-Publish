---
aliases:
  - grasp matrix
  - matrice di grasp
---
- ***References***:
	1. [[HCR - Grasp Matrix (Lecture)]] 
	2. [[HCR - Grasp Matrix]] 
	3. [[HCR - Calculating the Controlled Forces]] 
	4. [[HCR - Grasp Matrix (Example I) • Python Script]] 
	5. [[HCR - Grasp Matrix (Example II) • Python Script]] 
	6. ***Exams***:
		- [[HCR ~ Exam 2022-01-26]] 
		- [[HCR ~ Exam 2017-04-04 (with Solutions)]] 
		- [[HCR ~ Exam 2017-02-27 (with Solutions)]] 
		- [[HCR ~ Exam 2017-01-25 (with Solutions)]] 
----
- ***Grasp Matrix, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- La **Grasp Matrix** (o **matrice di presa**) è uno strumento matematico utilizzato in robotica e meccanica per analizzare le forze e i momenti trasferiti tra un oggetto e un sistema di presa (ad esempio, una mano robotica o una pinza) durante la manipolazione.<br>Questa matrice descrive come le forze applicate dalle dita o dalle pinze sul punto di contatto si traducono in una forza risultante e un momento applicato sull'oggetto afferrato.
	- ***Definizione della Grasp Matrix***:
		- La **Grasp Matrix**, denotata spesso come $G$, mappa le forze applicate nei punti di contatto tra il sistema di presa (ad esempio le dita) e l'oggetto, convertendole in una forza e un momento applicati al **centro di massa** dell'oggetto.<br>La matrice $G$ permette di descrivere la relazione tra le **forze di contatto** $f$ nei punti di contatto e le **forze e momenti risultanti** $w$ sull'oggetto intero.
		- La relazione è data da:$$w = G \cdot f$$Dove:
		- $w$ è il vettore delle forze e momenti applicati all'oggetto (tipicamente un vettore $6 \times 1$ che include 3 componenti di forza e 3 componenti di momento).
		- $G$ è la Grasp Matrix (una matrice $6 \times 3n$, dove $n$ è il numero di punti di contatto, che mappa le forze di contatto sulle forze risultanti).
		- $f$ è il vettore delle forze di contatto applicate dalle dita (un vettore $3n \times 1$, dove $n$ è il numero di punti di contatto, e ogni contatto ha 3 componenti di forza).
	- ***Struttura della Grasp Matrix***:
		- Se ci sono $n$ punti di contatto tra il sistema di presa (ad esempio, le dita di una mano robotica) e l'oggetto, la Grasp Matrix $G$ avrà dimensioni $6 \times 3n$, dove:
		- **6** è il numero totale di gradi di libertà per descrivere le forze e i momenti applicati all'oggetto (3 per le forze lineari e 3 per i momenti angolari).
		- **3n** è il numero totale di componenti di forza che possono essere applicate da ciascun punto di contatto, dove ogni punto di contatto ha 3 componenti di forza (lungo gli assi $x$, $y$ e $z$).
	- ***Composizione della Grasp Matrix***:
		- Per ogni punto di contatto $i$ tra l'oggetto e il sistema di presa, la Grasp Matrix ha una sottosezione che include:
		1. **Identità 3x3**: Questa parte della matrice rappresenta come le forze di contatto si traducono direttamente nelle forze sull'oggetto.
		2. **Termine del momento (cross product matrix)**: Questo termine rappresenta come la posizione del punto di contatto rispetto al centro di massa dell'oggetto genera un momento.<br>È la matrice del prodotto vettoriale che trasforma le forze di contatto nei momenti applicati sull'oggetto.
		- Se $r_i$ è il vettore posizione del punto di contatto $i$ rispetto al centro di massa dell'oggetto, il contributo alla Grasp Matrix è:$$G_i = \begin{bmatrix} I & 0 \\ \hat{r_i} & I \end{bmatrix}$$Dove:
		- $I$ è la matrice identità $3 \times 3$.
		- $\hat{r_i}$ è la matrice antisimmmetrica del vettore $r_i$, utilizzata per il prodotto vettoriale con le forze, generando il momento attorno al centro di massa.
	- ***Esempio 1: Due Dita che Afferano un Oggetto***:
		- Consideriamo un esempio semplice in cui due dita di una mano robotica afferrano un oggetto.<br>Supponiamo che i punti di contatto siano $r_1 = (x_1, y_1, z_1)$ e $r_2 = (x_2, y_2, z_2)$, i vettori posizione dei punti di contatto rispetto al centro di massa dell'oggetto.
		- La Grasp Matrix sarà composta da due blocchi $G_1$ e $G_2$, uno per ciascun punto di contatto:$$G = \begin{bmatrix} I & 0 & I & 0 \\ \hat{r_1} & I & \hat{r_2} & I \end{bmatrix}$$Questa matrice descrive come le forze di contatto $f_1$ e $f_2$ generate dalle due dita si combinano per produrre le forze e i momenti applicati sull'oggetto.
		- Se le forze applicate ai punti di contatto sono $f_1$ e $f_2$, la forza e il momento risultante applicati all'oggetto intero saranno:$$w = G \cdot \begin{bmatrix} f_1 \\ f_2 \end{bmatrix}$$
	- ***Esempio 2: Mano Robotica con 3 Dita***:<br>Immaginiamo una mano robotica con 3 dita che afferra un oggetto.<br>Ogni dito ha un punto di contatto con l'oggetto, e vogliamo calcolare la Grasp Matrix per descrivere come le forze esercitate dalle dita influenzano l'oggetto.
		- Per ciascun punto di contatto, abbiamo una sottomatrice composta da:
		1. Una **matrice identità** $3 \times 3$ che rappresenta il contributo delle forze applicate alla forza complessiva sull'oggetto.
		2. Una **matrice antisimmmetrica** $3 \times 3$ che descrive come le forze in un punto di contatto generano un momento sull'oggetto rispetto al centro di massa.
		- Supponiamo che i vettori posizione dei punti di contatto siano $r_1$, $r_2$, e $r_3$, con le relative forze di contatto $f_1$, $f_2$, e $f_3$.<br>La Grasp Matrix sarà:$$G = \begin{bmatrix} I & 0 & 0 & I & 0 & 0 \\ \hat{r_1} & I  & \hat{r_2} & I & \hat{r_3} & I \end{bmatrix}$$Dove $I$ è la matrice identità $3 \times 3$ e $\hat{r_i}$ è la matrice antisimmmetrica che rappresenta il momento generato dalla forza applicata nel punto $r_i$.
		- La forza e il momento risultante sull'oggetto saranno dati da:$$w = G \cdot \begin{bmatrix} f_1 \\ f_2 \\ f_3 \end{bmatrix}$$
	- ***Forze di Contatto e Grasp Matrix***:<br>Una volta costruita la Grasp Matrix, è possibile usarla per diversi scopi:
		- **Controllo della presa**: Determinare come devono essere distribuite le forze di contatto per mantenere un oggetto in equilibrio.
		- **Forze interne**: La Grasp Matrix può essere utilizzata per analizzare le forze interne che non alterano il movimento dell'oggetto ma sono necessarie per stabilizzare la presa.
		- **Analisi di stabilità**: La Grasp Matrix può essere usata per verificare se un insieme di forze di contatto è in grado di mantenere l'oggetto in equilibrio statico.
	- ***Sintesi***:<br>La **Grasp Matrix** è uno strumento fondamentale per descrivere la relazione tra le forze di contatto applicate da un sistema di presa (come una mano robotica) e le forze e i momenti risultanti sull'oggetto afferrato.<br>La matrice permette di calcolare come le forze delle dita si traducono in una forza e un momento complessivo sull'oggetto e può essere utilizzata per analizzare la stabilità della presa e per determinare le forze necessarie per manipolare un oggetto in modo sicuro ed efficiente.
----
