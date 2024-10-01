---
aliases:
  - collision detection
  - rilevamento delle collisioni
  - algoritmo di collision detection
  - vettore avatar
---
***Ricorda***:

> Dato il piano definito dai coefficienti $(a ,\ b ,\ c)$ e $d$, ovvero:$$ax + by + cz = d$$Definiamo:
> - $\vec x_p$ un punto qualsiasi appartenente allo stesso piano.
> - $D$ è la minima distanza tra $x_p$ ed $x_h$, e si trova dall'equazione:$$D = \min\left(\sqrt{(x_p -x_h)^{\tiny T} \cdot(x_p-x_h)})\right)$$Dove: $x_h$ è la stima della posizione dell'**end-effector**, che per costruzione può trovarsi sotto $\left(d \lt 0\right)$ del piano/triangolo, che identificheremo che un contatto tra il manipolatore ed l'oggetto, oppure può trovarsi sopra il piano  $\left(d \gt 0\right)$ e quindi non è avvenuto contatto tra il manipolatore e l'oggetto.

> Quello che noi vogliamo andare a verificare è il contatto tra $x_p$ ed $x_h$, ovvero andremo a cercare la distanza minima tra i due punti: $\min d$ .
> Dove, $x_h$ è un punto noto, e $x_p$ è un'incognita, non sappiamo quale punto appartenente al piano/triangolo è quello che minimizza la distanza $d$.
> Una volta calcolato $\min d$ , avremo che:
> - $d \lt 0$ : significa che $x_h$ è **sopra il piano** il punto $x_h$ non tocca il piano/triangolo.
> - $d = 0$ Se il risultato è esattamente zero, significa che $x_h$ si trova **sul piano**, tuttavia, la probabilità che il punto esattamente tocchi il piano senza penetrarlo è trascurabile (potrebbe essere visto come un caso limite).
> - $d \lt 0$ : significa che $x_h$ si trova **sotto il piano**, ovvero ha "penetrato" la superficie del piano/triangolo, il che suggerisce un contatto o una deformazione se stiamo considerando un oggetto fisico.

----
###### Collision Detection
Un oggetto virtuale è rappresentato da una nuvola di punti collegati da forme che ne definiscono e rappresentano approssivatimante la superficie e formano triangoli (`con i punti più vicini` #NOT_SURE_ABOUT_THIS).
==Si è scelta tale forma in quanto non è detto che sia sempre possibile definire figure più complesse ed in quanto rappresentano bene le deformazioni delle superfici==.
Ogni triangolo è identificato dai propi vertici:<br>![[Pasted image 20240904122647.png]]  ![[Pasted image 20240904122701.png]]
**N.B.:** I punti 1, 2, ..., 6, nel nostro caso rappresentaranno coordinate nello spazione, ad esempio:
- ***1***: $\left(x_1, y_1, z_1\right)$
- ***2***: $\left(x_2, y_2, z_2\right)$
- ***6***: $\left(x_6, y_6, z_6\right)$

Il rilevamento della collisione consiste nel determinare se si rientra nella [[HCR - Bounding Box|bounding box]] che contiene parte della superficie dell'oggetto.

> ***Bounding box***: ==*La box più piccola che contiene un triangolo*==:<br>![[Pasted image 20240904123139 - Copia.png]]
> #NOT_SURE_ABOUT_THIS `Non so se la figura è corretta: credo che la box sia troppo piccola.` 

Da ora in poi con $x_h$ si indentifica il "vettore avatar" a $3$ dimensioni.
- Se $x_h$ è fuori la **bounding box**, si è sicuri che la superficie non viene toccata, dunque non si necessata di rispondere con alcuna forza.
- Se $x_h$ è dentro, è necessario un **bounding box** più stringente e si deve calcolare in quale box si trova $x_h$.
- Ciò si ripete fino a che non si ricade nel primo caso (nessun contatto) o fino a quando non si arriva alle box minime:<br>![[Pasted image 20240904123149.png]]

La verifica del tocco si svolge lavorando sul triangolo come piano, descritto dall'equazione:$$(a \ b \ c) \kern2px x_p = d$$Dove:
- $x_p$ è un punto qualsiasi del piano.
- $(a \ b \ c)$ e volendo anche $d$ sono i coefficenti che diniscono il piano su cui il triangolo (della mesh di punti) giace, un piano nello spazio **3D** è definito con la seguente equazione:$$ax + by +cz \pm d = 0$$***NOTE***: *non è veramente importante il segno di $d$, di solito si considera positivo, in questi appunti si considera negativo*.<br>Quindi dati i vertici del triangolo:$$\left[\begin{array}{c} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3  \end{array}\right]$$Possimo descriverlo con un sistema del tipo:$$\left[\begin{array}{c} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3  \end{array}\right] \left[\begin{array}{c} a \\ b \\ c   \end{array}\right]  = \left[\begin{array}{c} d \\ d \\ d    \end{array}\right] $$Che può essere normalizzato, dividendo per $d$.

Quindi, ripeto, preso il piano che comprende il triangolo, che definiamo con il vettore dei suoi coefficienti: $(a \ b \ c)$, avremo che un punto $\bar x$, appartiene a questo piano, se:$$[a \ b \ c]^{\tiny T} \cdot \bar x = d \kern45px \text{oppure:} \kern15px [a \ b \ c]^{\tiny T} \cdot \bar x - d = 0$$In generale dato il vettore avatar $x_h$ : calcolando $(a \ b \ c) \kern2px x_h - d$, avremo che se il risultato è:
1. $> 0$ se l'end-effector ($x_h$) è sopra il piano, cioè non a contatto.
2. $= 0$ se tocca il piano ma ha probilità nulla come evento.
3. $< 0$ se tocca l'oggetto, cioè se deforma la superficie.

Dunque l'algoritmo di collision detection consiste in:
1. **Costruire le bounding boxes**:<br>Nel caso planare un triangolo è un segmento e il piano è una retta, e si ha una nuvola di punti (e maglie triangolari) individuati da coordinate secondo un qualche sistema di riferimento.<br>Per costruinre la box iniziale si considerano i valori minimi e massimi delle coordinate lungo tutti i componenti su tutta la nuvola.
2. **Individuare $x_h(t)$**, ovvero la posizione dell'avatar.
3. **Esprimere il piano** secondo l'equazione vista, calcolando $(a \ b \ c)$ dai vertici del triangolo.
4. **Performare la collision detection**:<br>Ponendo $x_p = x_h$ nell'equazione del piano e studiare il segno del risultato.<br>Se le coordinate di $x_h$ rientrano nel range della box allora può esserci contatto e si verifica in questo modom altrimenti non può e non è necessario alcun calcolo aggiuntivo.
5. **Suddividere la bounding box**: si suddivide la bounding box in ??? (penso 3 #NOT_SURE_ABOUT_THIS ) per ogni dimensione se si è potenzialmente in contatto e si ripete fino ad avere un solo triangolo (o segmento).<br>Si ricalcola tutto al partire dal passo ***3***.

In teoria l'algoritmo viene eseguito sull'oggetto intero ma, consoscendo la posizione iniziale e la velocità del dito, si può restringere l'area, cioè il numero di triangoli su qui svolgere i calcoli.

----
- ***Collision Detection, riguardando gli appunti che ti ho passato, puoi spiegarmi l'algoritmo di Collision Detection e il calcolo della Bounding Box***:<br>(*ChatGPT 4o*)
	- Il **Collision Detection** (rilevamento delle collisioni) è un aspetto fondamentale nella robotica e nella grafica computerizzata, poiché consente a un robot o a un oggetto virtuale di determinare quando entra in contatto con un altro oggetto.<br>Gli algoritmi di collision detection sono usati per evitare collisioni o per risolverle in modo appropriato, ad esempio cambiando la traiettoria del robot.
	- ***Algoritmo di Collision Detection***:<br>L'algoritmo di base per il rilevamento delle collisioni può variare a seconda del contesto, ma una tecnica comune è basata sul concetto di **Bounding Box**.<br>Una Bounding Box è una struttura semplificata che racchiude un oggetto complesso in una forma geometrica più semplice, come un rettangolo (in 2D) o un parallelepipedo (in 3D).
		- ***Passi dell'algoritmo***:
		1. **Bounding Box**: Per ogni oggetto (robot o ostacolo), si calcola una "scatola di delimitazione" (Bounding Box), che rappresenta l'area in cui l'oggetto potrebbe collidere con altri.<br>Ci sono diversi tipi di Bounding Box, come:
			   - **Axis-Aligned Bounding Box (AABB)**: È una scatola rettangolare allineata con gli assi principali del sistema di coordinate.
			   - **Oriented Bounding Box (OBB)**: È simile all'AABB, ma può essere ruotata secondo l'orientamento dell'oggetto.
			2. **Confronto delle Bounding Box**: Una volta calcolate le Bounding Box degli oggetti, si eseguono confronti per vedere se si sovrappongono.<br>Se le Bounding Box non si intersecano, allora sicuramente gli oggetti non collidono.
			3. **Verifica dettagliata**: Se le Bounding Box si sovrappongono, si passa a un controllo più dettagliato per verificare se gli oggetti interni stanno effettivamente collidendo.<br>Questo può coinvolgere tecniche più complesse, come il controllo delle singole geometrie o l’uso di modelli di collisione più accurati.
		- ***Calcolo della Bounding Box***:<br>Il calcolo della Bounding Box può essere semplice o complesso, a seconda della forma e delle dimensioni dell'oggetto.<br>Per un oggetto tridimensionale, come un robot, il calcolo della Bounding Box richiede l'analisi delle coordinate minime e massime degli estremi dell'oggetto.
		- ***Procedura***:
		1. **Individuare i punti estremi**: Per calcolare una **AABB**, è necessario determinare i punti estremi dell'oggetto in tutte le dimensioni (x, y, z).<br>Questi punti rappresentano i vertici più esterni dell'oggetto.
			   - Il punto **min** ha le coordinate più basse su tutti gli assi.
			   - Il punto **max** ha le coordinate più alte su tutti gli assi.
			2. **Definire la Bounding Box**: Una volta trovati i punti min e max, questi definiscono i limiti della Bounding Box.<br>Ad esempio, per una AABB, le facce della scatola saranno parallele agli assi x, y e z, e la dimensione della scatola sarà data dalla differenza tra i punti max e min lungo ciascun asse.
		- ***Esempio***:<br>Considera un oggetto 3D con i seguenti punti estremi:
			- Punto minimo: (1, 2, 3)
			- Punto massimo: (5, 6, 7)
			- La Bounding Box avrà le dimensioni (lunghezza x larghezza x altezza) calcolate come:
			- Lunghezza: 5 - 1 = 4
			- Larghezza: 6 - 2 = 4
			- Altezza: 7 - 3 = 4
		- ***Approfondimento sull'Oriented Bounding Box (OBB)***:<br>Per oggetti che possono avere orientamenti non allineati con gli assi principali, si usa una **OBB**.<br>In questo caso, la Bounding Box è calcolata considerando l'orientamento dell'oggetto, ma il controllo delle collisioni diventa più complesso poiché richiede una rotazione e un confronto tra gli oggetti in spazi tridimensionali.
		- L'uso delle Bounding Box semplifica di molto il processo di rilevamento delle collisioni, poiché riduce il numero di controlli geometrici dettagliati da fare sugli oggetti complessi, accelerando così il calcolo nelle simulazioni o nelle applicazioni in tempo reale.
		- Spero che questa spiegazione ti aiuti a chiarire i concetti di Collision Detection e Bounding Box!
----
- ***Studiando e riguardando gli appunti sono arrivato a questa parte: 'Da ora in poi con $x_h$ si indentifica il "vettore avatar" a $3$ dimensioni ...', mi puoi aiutare a capire cosa si intende per "vettore avatar" e puoi fare degli esempi su questo algoritmo?***:<br>(*ChatGPT 4o*)
	- Il termine **"vettore avatar"** nel contesto dei tuoi appunti sembra fare riferimento alla posizione di un punto o di un oggetto nello spazio tridimensionale, chiamato appunto **$x_h$**.<br>In altre parole, il vettore avatar rappresenta la posizione di un'entità (ad esempio, una parte di un robot o un punto di contatto virtuale) all'interno dello spazio in cui avviene il rilevamento delle collisioni.
	- ***Algoritmo descritto nei tuoi appunti***:
		- L'algoritmo descritto sembra essere una versione iterativa di **collision detection** che utilizza una gerarchia di **Bounding Boxes** di grandezza progressivamente più piccola e precisa.<br>L'idea è quella di verificare se il "vettore avatar" $x_h$ si trova all'interno di una serie di Bounding Boxes sempre più piccole per determinare se c'è contatto con una superficie.
	- ***Passi dell'algoritmo***:
		1. **Controllo iniziale**: Si parte con una **Bounding Box** ampia, che racchiude una regione più grande o un intero oggetto.
		   - Se il vettore $x_h$ si trova **fuori** da questa Bounding Box, si conclude immediatamente che non c'è collisione o contatto, e non è necessario rispondere applicando forze.
		   - Se $x_h$ si trova **dentro** la Bounding Box, si procede con una verifica più dettagliata.
		2. **Bounding Box più stringente**: Se $x_h$ è dentro la Bounding Box iniziale, si restringe ulteriormente la zona di controllo, cercando una **Bounding Box più piccola** che sia contenuta all'interno della precedente.<br>Questo processo continua fino a che non si trova la Bounding Box più stretta o più "localizzata" possibile, che racchiude in modo accurato l'area di possibile contatto.
		3. **Verifica finale**: L'algoritmo prosegue fino a:
		   - Trovare che $x_h$ si trova fuori da una di queste box più piccole, nel qual caso si conclude che non c'è collisione.
		   - O fino a quando si raggiunge una box "minima", oltre la quale non si può più dividere l'area di controllo, confermando che c'è un contatto.
	- ***Esempio***:<br>Immagina di avere un robot umanoide con una mano che si avvicina a una superficie.
		- Il vettore $x_h$ rappresenta la posizione della punta delle dita del robot nello spazio 3D.
		- Si utilizza una **Bounding Box** che racchiude l'intera superficie dell'oggetto che il robot potrebbe toccare.
			- Se $x_h$ è fuori da questa Bounding Box, non c'è contatto, e quindi non serve calcolare forze.
			  - Se $x_h$ è dentro, si restringe la Bounding Box, cercando di capire in quale regione più precisa si trova $x_h$.
		- Si continua a dividere lo spazio in box più piccole, finché non si arriva a una zona molto ristretta che rappresenta una porzione specifica della superficie o l'area di contatto esatta.<br>A quel punto, si può calcolare l'interazione fisica (ad esempio, la forza che la mano del robot esercita sulla superficie).
	- ***Algoritmo "a raffinamento progressivo"***:<br>Questo approccio di raffinare progressivamente le Bounding Boxes è molto efficiente, perché consente di evitare controlli dettagliati inutili su tutta la superficie, concentrandosi solo sulle aree potenzialmente rilevanti.<br>Inoltre, la gerarchia di box permette di risolvere il problema di collisione in modo rapido, riducendo il numero di calcoli necessari.
		- Spero che questo chiarisca meglio l'idea del "vettore avatar" e del processo di raffinare la Bounding Box! Se hai bisogno di ulteriori dettagli, fammi sapere.
----
- ***Andando avanti negli appunti arriviamo alla verifica del tocco e alla definizione del triangolo come piano; non ho capito assolutamente questa parte, cosa sarebbe $d$, e cosa intende per "coefficenti legati ai vertici di un piano" ?***:<br>(*ChatGPT 4o*)
	- In questa parte, stai studiando un approccio geometrico per determinare se un punto, rappresentato dal vettore avatar $x_h$, si trova sopra, tocca o penetra un piano rappresentato da un triangolo.
	- ***L'equazione del piano***:<br>Un piano nello spazio tridimensionale può essere descritto dall'equazione generale:$$(a \ b \ c) \cdot x_p = d$$Dove:
		- $(a, b, c)$ sono i **coefficienti** che rappresentano la **normale** al piano.<br>Questa normale è un vettore perpendicolare al piano.
		- $x_p$ è un punto generico sul piano, con coordinate $(x, y, z)$.
		- $d$ è una costante legata alla distanza del piano dall'origine lungo la normale $(a, b, c)$.
	- ***Il triangolo come piano***:
		- Il triangolo è una figura geometrica che definisce una porzione di un piano nello spazio tridimensionale.<br>I tre vertici del triangolo $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, $(x_3, y_3, z_3)$ definiscono un piano unico.<br>I **coefficienti $(a, b, c)$** sono i componenti della normale a questo piano, che possono essere determinati dai vertici del triangolo.
		- ***Come ottenere la normale $(a, b, c)$***:
		1. **Trova i vettori del triangolo**: Definisci due vettori che si trovano sul piano, ad esempio:
		   - Vettore 1: $v_1 = (x_2 - x_1, y_2 - y_1, z_2 - z_1)$
		   - Vettore 2: $v_2 = (x_3 - x_1, y_3 - y_1, z_3 - z_1)$
		2. **Calcola la normale**: La normale al piano è il prodotto vettoriale tra questi due vettori:$$(a, b, c) = v_1 \times v_2$$Questo ti dà un vettore $(a, b, c)$ perpendicolare al piano, i cui componenti rappresentano i coefficienti dell'equazione del piano.
		3. **Determina $d$**: La costante $d$ si ottiene sostituendo uno dei vertici del triangolo (ad esempio $(x_1, y_1, z_1)$) nell'equazione del piano:$$d = a \cdot x_1 + b \cdot y_1 + c \cdot z_1$$Quindi, l'equazione del piano passante per i vertici del triangolo è:$$a \cdot x_p + b \cdot y_p + c \cdot z_p = d$$
			- ***Interpretazione dei risultati con il vettore avatar $x_h$***:<br>Il tuo punto di interesse, il vettore avatar $x_h$, è inserito nell'equazione del piano per verificare la sua posizione rispetto al triangolo.<br>Il risultato dell'espressione:$$(a \ b \ c) \cdot x_h - d$$Può essere interpretato come segue:
				- **$> 0$**: Se il risultato è positivo, significa che $x_h$ è **sopra il piano** (non tocca il triangolo né il piano).
				- **$= 0$**: Se il risultato è esattamente zero, significa che $x_h$ si trova **sul piano**.<br>Tuttavia, secondo gli appunti, la probabilità che il punto esattamente tocchi il piano senza penetrare è trascurabile (potrebbe essere visto come un caso limite).
				- **$< 0$**: Se il risultato è negativo, significa che $x_h$ si trova **sotto il piano**, ovvero ha "penetrato" la superficie del triangolo, il che suggerisce un contatto o una deformazione se stiamo considerando un oggetto fisico.
	- ***Riassunto di cosa è $d$ e i coefficienti***:
		- **$d$** rappresenta la distanza del piano dall'origine lungo la direzione della normale $(a, b, c)$.
		- I **coefficienti $(a, b, c)$** sono i componenti del vettore normale al piano e sono determinati dai vertici del triangolo.
		- Questo tipo di controllo è usato per verificare se un punto entra in contatto con una superficie triangolare (spesso utilizzata in modelli tridimensionali per rappresentare superfici complesse).
----
