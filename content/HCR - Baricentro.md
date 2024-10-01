---
aliases:
  - baricentro
---
- ***Baricentro, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- Il **baricentro** è il punto di un oggetto o di un sistema di punti in cui si può considerare concentrata l'intera massa del sistema per quanto riguarda l'equilibrio e il movimento.<br>In meccanica, il baricentro è anche chiamato **centro di massa** (specialmente quando si tratta di oggetti con distribuzione di massa non uniforme).
	- ***Definizione di Baricentro***:<br>Il **baricentro** è il punto in cui si può immaginare che tutta la massa di un corpo sia concentrata, così che, se il corpo fosse sostenuto in quel punto, rimarrebbe in equilibrio.<br>In termini matematici, il baricentro è la media ponderata delle posizioni di tutte le parti di un sistema, con i pesi dati dalle rispettive masse.
		- Nel caso di un sistema discreto di punti materiali con masse $m_1, m_2, \dots, m_n$ e posizioni $\mathbf{r_1}, \mathbf{r_2}, \dots, \mathbf{r_n}$, il **baricentro** $\mathbf{r_{CM}}$ è dato dalla formula:$$\mathbf{r_{CM}} = \frac{\sum_{i=1}^{n} m_i \mathbf{r_i}}{\sum_{i=1}^{n} m_i}$$Dove:
		- $\mathbf{r_{CM}}$ è il vettore posizione del baricentro.
		- $m_i$ sono le masse dei punti.
		- $\mathbf{r_i}$ sono le posizioni dei punti.
		- Nel caso di un corpo rigido con distribuzione continua di massa, il baricentro si calcola integrando la distribuzione di massa sull'intero volume del corpo.
	- ***Esempio 1: Baricentro di un Sistema di Punti***:<br>Supponiamo di avere un sistema di tre masse puntiformi:
		- $m_1 = 2 \, \text{kg}$ in $\mathbf{r_1} = (1, 0)$,
		- $m_2 = 3 \, \text{kg}$ in $\mathbf{r_2} = (3, 2)$,
		- $m_3 = 5 \, \text{kg}$ in $\mathbf{r_3} = (6, 1)$.
		- Il baricentro $\mathbf{r_{CM}}$ di questo sistema è:$$\mathbf{r_{CM}} = \frac{2 \cdot (1, 0) + 3 \cdot (3, 2) + 5 \cdot (6, 1)}{2 + 3 + 5}$$Calcoliamo i numeratori per ciascuna coordinata:$$\mathbf{r_{CM}} = \frac{(2 \cdot 1 + 3 \cdot 3 + 5 \cdot 6, 2 \cdot 0 + 3 \cdot 2 + 5 \cdot 1)}{10} = \frac{(2 + 9 + 30, 0 + 6 + 5)}{10} = \frac{(41, 11)}{10}$$Quindi il baricentro è:$$\mathbf{r_{CM}} = (4.1, 1.1)$$
	- ***Esempio 2: Baricentro di un Triangolo***:
		- Nel caso di un **triangolo** di vertici $A(x_1, y_1)$, $B(x_2, y_2)$, e $C(x_3, y_3)$, il baricentro si trova come media aritmetica delle coordinate dei tre vertici:$$\mathbf{r_{CM}} = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)$$Supponiamo di avere un triangolo con vertici in $A(1, 1)$, $B(4, 5)$, e $C(6, 2)$.<br>Il baricentro sarà:$$\mathbf{r_{CM}} = \left( \frac{1 + 4 + 6}{3}, \frac{1 + 5 + 2}{3} \right) = \left( \frac{11}{3}, \frac{8}{3} \right) = \left( 3.67, 2.67 \right)$$
	- ***Baricentro e Centro di Massa***:<br>Il **centro di massa** è una generalizzazione del concetto di baricentro per oggetti con distribuzione continua di massa.<br>Il centro di massa di un oggetto rigido rappresenta il punto dove si può immaginare che l'intera massa del corpo sia concentrata per descriverne il movimento sotto l'azione delle forze.
		- Se la densità di massa non è uniforme, il baricentro e il centro di massa possono non coincidere.<br>Tuttavia, per corpi omogenei (con densità uniforme), il baricentro coincide con il centro geometrico del corpo.
	- ***Esempio 3: Baricentro di un Disco Omogeneo***:
		- Consideriamo un **disco omogeneo**.<br>Poiché la distribuzione di massa è uniforme, il baricentro coincide con il centro geometrico del disco.<br>Se il disco ha il suo centro all'origine del sistema di coordinate, il baricentro è esattamente al centro del disco, cioè in $(0, 0)$.
	- ***Proprietà del Baricentro***:
		1. **Equilibrio**: Il baricentro rappresenta il punto di equilibrio.<br>Se un corpo viene sostenuto nel suo baricentro, rimarrà in equilibrio statico (non si inclinerà in nessuna direzione).
		2. **Invarianza per Traslazioni**: Il baricentro si sposta con il corpo quando il corpo viene traslato nello spazio, ma rimane fisso rispetto al corpo stesso.
		3. **Centro di Massa**: Il baricentro è equivalente al centro di massa se il corpo ha densità uniforme.<br>Se la densità varia, il centro di massa si sposta verso la parte del corpo con maggiore massa.
	- ***Applicazioni del Baricentro***:
		1. **Ingegneria Strutturale**: Il calcolo del baricentro è fondamentale per progettare edifici e ponti, dove è necessario garantire la stabilità delle strutture.
		2. **Robotica**: In robotica, il baricentro viene utilizzato per progettare sistemi di equilibrio, come robot bipedi o quadricotteri, che devono bilanciare il proprio peso per non cadere.
		3. **Fisica dei Corpi Rigidi**: Nella fisica dei corpi rigidi, il baricentro è essenziale per calcolare i movimenti di rotazione e traslazione di un oggetto sotto l'azione di forze esterne.
	- ***Sintesi***:<br>Il **baricentro** rappresenta il punto di un corpo in cui si può immaginare che tutta la sua massa sia concentrata.<br>Esso è determinato dalla distribuzione di massa e posizione delle sue parti e svolge un ruolo chiave nell'equilibrio e nel movimento dei corpi.<br>Nella sua forma più semplice, è il punto medio geometrico di una figura o un oggetto simmetrico e omogeneo, ma in generale può variare a seconda della distribuzione di massa del sistema.
----
