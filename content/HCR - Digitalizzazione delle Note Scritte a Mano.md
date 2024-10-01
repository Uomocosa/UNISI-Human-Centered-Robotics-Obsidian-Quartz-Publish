###### Basi del Movimento
Il movimento è lo spostamento di un insieme di punti, di materia, secondo un qualche sistema di riferimento di 3 assi.
I movimenti possibili sono:
- **La traslazione**.
- **La rotazione**.

Il problema che affrontiamo è quello di conoscere la posizione e l'orientamento degli oggetti in riferimento ad un sistema (di riferimento) esterno:<br>![[Pasted image 20240828191241.png]]

Se due vettori sono nello stesso sistema di riferimento si possono sommare tramite la regola del parallelogramma per stabilire il vettore risultante.
Per trasporre il vettore in un altro sistema di riferimento si opera la somma tra il vettore, che dal secondo punta al corrente sistema nell'origine, e viene rapprensetato poi secondo il nuovo sistema.
Vediamo degli esempi per capire meglio:<br>![[Pasted image 20240828191527.png]]<br>![[Pasted image 20240828191541.png]]

Secondo Eulero le 3 componenti del vettore possono essere espresse come:$$\begin{array}{l}       a \times x_1 = |a| \cdot |x_1| \cdot \cos \alpha \\ a \times y_1 = |a| \cdot |y_1| \cdot \sin \alpha \end{array}$$Dove:
- $x_1$ and $y_1$ sono **versori**.

Lo si può scrivere anche come:$$\left.\begin{array}{l} a^{*}_{x_1} = a^{\tiny T} \cdot x_1 \\ a^{*}_{y_1} = a^{\tiny T} \cdot y_1 \\ a^{*}_{z_1} = a^{\tiny T} \cdot z_1 \end{array}\right\} = \kern0px \vec a^{*} $$Ovvero:$$\vec a^{*} = \left[\begin{array}{l} a^{\tiny T} \cdot x_1 \\ a^{\tiny T} \cdot y_1 \\ a^{\tiny T} \cdot z_1 \end{array}\right]$$
L'obbietivo ora è determinare la matrice che permette di passare da un sistema di riferimento all'altro:$$\vec a^{*} + \left[?\right]\cdot \vec b^{*}$$Where:
- $\vec a^{*}$ is a $\left[n\times 1\right]$ vector.
- $\left[?\right]$ is a $\left[n\times m\right]$ matrix.
- $\vec b^{*}$ is a $\left[m\times 1\right]$ vector.

Dunque gli assi che definiscono il secondo sistema di riferimento devono essere espressi secondo il primo.
Dato quando stabilito prima per un generico vettore:<br>![[Pasted image 20240831181224.png]]
Dove la matrice trovata è la matrice di rotazione $R_z$. Essa è composta da soli valori $[-1, 1]$, dal momento che tutti gli elementi sono versori.

*~Ex.:*<br>![[Pasted image 20240831181334.png]]

Da questo si può generalizzare che:$$R_z = (R_1)^{\tiny T} \kern10px\Rightarrow\kern10px R^{\tiny T} R = I$$
Inoltre ricordando che:
1. $\det(AB) = \det(A) \cdot \det(B)$
2. $\det(A) = \det(A^{\tiny T})$

**⇒ Se: $\left(\det(R)\right)^2 = \det(I)$, allora: $\det(R) = \det(R^{\tiny T}) = 1$**.

Le operazioni di roto-traslazione sono la combinazione di una traslazione e di una rotazione, vediamo un esempio:<br>![[Pasted image 20240831182042.png]]

Esiste per queste operazioni una tecnica più diretta, ovvero la **funzione di trasformazione omogenea**.

Per applicarla è necessario avere i **vettori omogenei**, i quali hanno un elemento aggiuntivo pari ad $1$ come ultimo elemento rispetto al vettore originale:<br>![[Pasted image 20240831182213.png]]

Esiste anche un'altra forma della matrice di rotazione, la quale ha come riferimento l'angolo tra l'asse delle ascisse di un sistema di riferimento e quello dell'altro sistema:<br>![[Pasted image 20240831182311.png]]

----
###### Cinematica Direttta di un Manipolatore Robotico
(*Direct Kinematics of a Robotic Manipulator*)

In genere un manipolatore robotico è un braccio robotico, ed in genere si rappresenta così:<br>![[Pasted image 20240910193537.png]]
Esso è generalmentee composto da **linkers**, i quali sono copri rigidi, e da **joints**, i quali contengono meccanismi che permettono il moviemetno relativo tra i linkers.
Esistono due categorie di joints:
1. **Joints Prismatici**: i quali permettono una **traslazione**.
2. **Joints Revoluti**: i quali permettono una **rotazione**.

Entrambi i tipi di joints conferiscono **1 grado di libertà** al manipolatore.
L'insieme di linkers a di joints formano una **catena cinemantica** che in questo caso è **aperta**, mentre, se il manipolatre operasse un oggetto si diretta **connessa**.

L'interesse principale della **cinematica diretta** è quello di stabilire a priori la posizione dell'**end effector**, data una sequenza di comandi espressi sotto forma di angoli (si considerano solo **joints revoluti**).
Più utile è la **cinenamtica inversa** per cui, a partire dalla posizione che si vuole raggiungere, si determina la sequenza di comandi necessari ma è molto più complessa e non verra trattata.

In generale, secondo tale configurazione, la posizione dell'end effector può essere espressa come:<br>![[Pasted image 20240831183047.png]]

In questo caso si poteva arrivare al risultato anche attraverso la trigonometria, ma nel caso tridimensionale, si pò procedere solo in questo modo e si fa uso della **convenzione delle tavole di Denavit-Hartenberg** ([Wikipedia: 'Convenzione di Denavit-Hartenberg](https://it.wikipedia.org/wiki/Convenzione_di_Denavit-Hartenberg))

Oltre alla posizione e all'orientamento dell'end effector, spesso si controlla anche la sua velocità, espressa in funzione della velocita dei joints, come:<br>![[Pasted image 20240831183420.png]]

A partire da ciò si può stabilire la forza esercitata sull'end effector, conoscendo i **momenti torcenti** dei joints e la loro potenza:<br>![[Pasted image 20240831183535.png]]<br>![[Pasted image 20240831183546.png]]

----
###### Grasping
Nello studio del problema del grasping non si modellerà e lavorerà con il braccio ma con la mano dal momento che l'azione del "grasp" non richiede sono di gestire contemporaneamente le dita ma anche di farle collaborare.
Inoltre i bracci robotici non sono di interesse al momento che non è difficile reperirli sul mercato, a differenza delle mani.
Ogni dito può essere pensato come un braccio robotico e l'obbiettivo è quello di muovere oggetti/solidi.

Molte aziende di logistica, come '*Amazon*', investono in questo per poter automatizzare l'intero processo prima del transporto. 
Se il controllo è centralizzato il controllore gestisce tutto ma si parla di collaborazione se si hanno più controllori indipendenti.

L'azione di manipolazione è divisibile in 3 parti:
1. Avvicinamento all'oggetto.
2. Instaurazione del contatto ed interazione.
3. Movimento dell'oggetto.

Ci si concentrerà principalmente sulle ultime due e si studieranno tramite metodi e modelli algebrici e non ci si baserà su architetture specifiche.
Innanzitutto bisogna distinguere tra i due tipi di grasping:
1. **Grasping di potenza**: dove l'obbiettivo è il movimento statico degli oggetti.
2. **Grasping di precisione**: che permette il movimento relativo tra l'oggetto ed il palmo, evitando il movimento del braccio.<br>Il controllo è dato dai polpastrelli delle dita in modo che se ne possano sfruttare i gradi di libertà.

L'interazione con un oggetto è resa attraverso le forze esercitate dalle singole dita, infatti posizione e velocità degli oggetti sono conseguenze delle forze, ma ciò dipende anche dal modello del contatto.

Si consideri un sistema composto da due dita:<br>![[Pasted image 20240903182148.png]]
Poiché le due devono collaborare, non si possono usare due **Jacobiane** distinte, ma bisogna ricondursi ad'unica matrice, cioè bisogna pensare al tutto come un unico robot con due catene cinematiche.
In generale data una forze $\vec F$ appicata ad un braccio $\vec d$, il procedimento per il calcolo del movimento torcente $\vec \tau$ può essere "compresso" attraverso la **screw matrix**:<br>![[Pasted image 20240903182405.png]]

Mentre la direzione del vettore $\vec \tau$ è data dalla **regola della mano destra**.
Tale matrice può essere utilizzata per qualsiasi prodotto vettoriale.
Siano date le forze di contatto ed i momenti torcenti nei singoli "**joints**", si vuole stabilre una relazione che li leghi direttamente:<br>![[Pasted image 20240903182607.png]]
Dove la matrice è la **Jacobiana della mano** (una matrice $\left[9\times 6\right]$) e la trasposizione è quella usata per le forze.

La **potenza di contatto** è data dalla somma delle potenze $M$ joints singoli, infatti la forza sull'**end effector** corrisponde ai momenti torcenti nei joints e la velocità lineare a quelle angolari:<br>![[Pasted image 20240903183108 1.png]]
Quindi in generale:$$\tau = J^{\tiny T} F_e$$Dove:
- $\tau$ : è la **potenza di contatto**.

Nel caso proposto si avrebbe che:<br>![[Pasted image 20240903183217.png]]
Ma dal momento che le forze hanno sempre il compoenente $z$ nullo, mentre al più l'ultimo elemento delle prime due righe di $S(d)$ non sono nulli, allora l'unico componenete non nullo di $\tau$ è $z$, come suggerisce la fisica:<br>![[Pasted image 20240903183339.png]]
Dunque il risultato precedente può essere così ridotto:<br>![[Pasted image 20240903183408.png]]

In generale la **Jacobiana** cambia in base alla configurazione del manipolatore (posizione links) e in base agli **end effectors**, i quali a loro volta dipendono da come viene afferrato un oggetto.

*~Ex.*:<br>![[Pasted image 20240903183526.png]]
In questo problema di questa configurazione consiste nell'impossibilità di stringere (*squeeze*) gli oggetti.
Da questo esempio emerge il concetto di **kernel di una matrice**, in particolare $F$ è kernel di $J$ dal momento che: $$F^{\tiny T} \cdot J = 0$$E ciò vale per le forze direzionate lungo i link (*push/pull*) e lungo $z$.
In altre parole i kernel sono tutte le forze che sono resistite non attraverso un momento torcente ma attraverso i vincoli meccanici dei joints.

----
###### Grasp Matrix
Come si è visto nel grasping alle forze applicate all'oggetto si contrappongono le forze vingolari di esso.
Si studia ora il provlema dal punto di vista dell'oggetto.
La **matrice di grasp**, permette di stabilire, a partire dalle forze di contatto, l'egfetto complessivo in termini di movimento.
Si considera da ora come sistema di riferimento o quello fissato nel baricentro dell'oggetto.
Lo spostamento in termini di traslazione e di rotazione può essere stabilito attraverso:<br>![[Pasted image 20240903184008.png]]
Le quali definiscono la dinamica dell'oggetto.
Si consideri la prima equazione, innanzitutto esistono 3 tipi di forze:
1. **Forze di contatto**.
2. **Forze di gravità**.
3. **Forze ambientali**.<br>(*Quest'ultimo non verrà considerato.)

Si consideri il seguente esempio:<br>![[Pasted image 20240903184206.png]]
Per quanto riguarda la seconda equazione, è possible generare una rotazione (planare) sia tramite due o più forze, sia tramite l'applicazione di un momento torcente ma per trasmettere questo è necessario che l'**end effector** sia una superficie piatta, dunque si considerano solo le forze.

Si consideri il seguente esempio:<br>![[Pasted image 20240903184411.png]]
Unendo i due risultati si ottiene che:<br>![[Pasted image 20240903184440.png]]
Dove la matrice di grasp contiene tante colonne:$$\left[\begin{array}{c} I \\ S(d_i)    \end{array}\right]$$Quanti sono i punti di conttatto diversi ($i$).

*~Ex.*:<br>![[Pasted image 20240903184627.png]]
Si vogliono trovare ora i kernel di $G$, nel caso di applicazione di due foze su un oggetto quadrato di lato $A$:<br>![[Pasted image 20240903184710.png]]
In questo caso non c'è alcun movimento dell'oggeto am ciò è preceduto al **grasp**, cioè le forze applicate devono avere modulo e direzione tali che l'oggetto non scivoli e che ci sia sufficente **attrito statico** da mantenere la presa, anche in caso di forze esterne.
In termini vettoriali si deve far in modo che le risultanti delle forze ai punti di contatto rientrino sempre nel **cono d'attrito**:<br>![[Pasted image 20240903184915.png]]
Se una forza esterna tenta di portare via l'oggetto e se le forze della presa non aumentano, la presa viene persa.
In generale per risolvere questo problema è necessario conoscere la direzione normale nei punti di contatto ed il **coefficiente di attrito**.
La forza esterna che si tratterà principalmente è quella di gravità e con $W_{\text{ext}}$ si indica il vettore:$$\left[\begin{array}{c}  F_{\text{ext}} \\ M_{\text{ext}}     \end{array}\right]$$Il probema può essere formulato come:<br>![[Pasted image 20240903185616.png]]
Dove le forze al contatto sono le incognite, dunque:<br>![[Pasted image 20240903185623.png]]
In questo caso:$$F_C = \left[\begin{array}{l} 0 & {mg\over \tau} &0 & 0 & {mg\over \tau} & 0\end{array}\right]^{\tiny T}$$Ma le forze non possono essere dirette parallelamente a quella di gravità perché non si avrebbe attrito con l'oggetto e scivolerebbe.
Dunque a queste vanno sommate forze dirette verso l'interno in modo che: $F_c = F_p + F_{c_i}$ rientri nel cono di attrito, per questo $F_{c_i}$ e $N(G)$:$$G\cdot F_{c_i} = 0$$Per ottenere questo è necessario applicare il giusto momento torcente, con le due equazioni:
1. $-W = G \cdot F$ : che invertita permette di stabilire la forza al contatto da applicare per il **grasp**.
2. $\tau = J^{\tiny T} \cdot F$ : che permette di stabilire il momento torcente necesarrio per applicare $F$.

Nel grasping, però è importatnte avere misure in feedback delle forze applicate, conoscendo il momento torcente applicato.
Per avere queste informazione, dato il seguente sistema:<br>![[Pasted image 20240904121151.png]]
Dove:
- $n$ : è il numero di joints.
- $n_c$ : è in numero di contact points.

È necessario che ci siano più equazioni che variabili, cioè:$$n + E \geq 3 \kern2px n_c$$Nel caso raffigurato di **enveloping grasping** è importante valutare le forze, infatti si hanno $10$ equazioni e $12$ variabili, ma non è rivelante che esse siano nel **cono d'attrito**, dal momento che l'oggetto è bloccato dalla presa.

Se il sistema non ha un **nullspace**, allora esso ha una sola soluzione ele forze devpno trovarsi necessariamente nel cono d'attrito per fare presa, ma se non lo fossero, non si potrebbe intervenire artificalmente.
Dunque è necessario che ci siano infinite soluzioni, cioè:$$N(G) \neq 0$$Se $G$ è a **rango massimo**, si ha un grasp che può muoveere l'oggetto in ogni direzione.

----
###### Haptics
La tecnologia aptica è l'ultima frontiera della robotica del **grasping** e concerne la restituzione all'utente o l'adattamento della presa in funzione delle forze percepite.
In altre parole "*haptics*" significa interazione tattile.

I componenti necessari per tale interazione sono:
1. **Misura del movimento**, specificatamente misura del movimento di una certa parte del corpo, tramite una tecnologia appropiata.
2. **Rilevamento delle collisioni** tramite un'elaborazione della misura, ripsetto ad una rappresentazione dell'oggtto.
3. **Rendering aptico** tramite un attuatore per permetter "l'*acknowledgment*" all'effettività dell'azione svolta, restituendo una sensazione reale o simulata o un display aptico.

In termini matematici si traduce come:<br>![[Pasted image 20240904122054.png]]
Dove $\Delta x$ è relativo ad una superficie.

In generale la quantità di energia scambiata nell'interazione aptica è molto più alta rispetto agli altri tipi di interazione per questo non è un sistema efficiente per comunicare.
Il tocco è essenzialmente uno scambio di forze e per questo la robotica è il campo giusto da cui sviluppare interfaccie aptiche.
Il processo può essere così schematizzato:<br>![[Pasted image 20240904122251.png]]
Il "*simulation engine*" è quello che svolge i calcoli, così che si possa rivelare la collisione, restituire un **feedback**, e mostrare a schermo l'ambiente virtuale.

----
###### Collision Detection
Un oggetto virtuale è rappresentato da una nuvola di punti collegati da forme che ne definiscono e rappresentano approssivatimante la superficie e che sono triangoli.
Si è scelta tale forma in quanto non è detto che sia sempre possibile definire figure più complesse ed in quanto rappresentano bene le deformazioni delle superfici.
Ogni triangolo è identificato dai propi vertici:<br>![[Pasted image 20240904122647.png]]  ![[Pasted image 20240904122701.png]]

Il rilevamento della collisione consiste nel determinare se si rientra nella **bounding box** che contiene parte della superficie dell'oggetto.
La box più piccola che contiene un triangolo.
Da ora in poi con $x_h$ si indentifica il vettore avatar a $3$ dimensioni.
Se $x_h$ è fuori la **bounding box**, si è sicuri che la superficie non viene toccata, dunque non si necessata di rispondere con alcuna forza.
Se $x_h$ è dentro, è necessario un **bounding box** più stringente e si deve calcolare in quale box si trova $x_h$.
Ciò si ripete fino a che non si ricade nel caso precedente o fino a qunado non si arriva alle box minime:<br>![[Pasted image 20240904123149.png]]
La verifica del tocco si svolge lavorando sul triangolo come piano, descritto dall'equazione:$$(a \ b \ c) \kern2px x_p = d$$Dove:
- $x_p$ è un punto qualsiasi del piano.
- $(a \ b \ c)$ sono coefficienti legati ai vertici del triangolo:<br>![[Pasted image 20240904123139.png]]

Un triangolo è dunque descritto da un sistema del tipo:<br>![[Pasted image 20240904123224.png]]
Che può essere normalizzato, dividendo per $d$.

In generale se $x_h$ è nell'equazione del piano, $(a \ b \ c) \kern2px x_h - d$, si ottiene:
1. $> 0$ se è sopra il piano, cioè non a contatto.
2. $= 0$ se tocca il piano ma ha probilità nulla come evento.
3. $< 0$ se tocca l'oggetto, cioè se deforma la superficie.

Dunque l'argoritmo di collision detection consiste in:
1. **Costruire le bounding boxes**:<br>Nel caso planare un triangolo è un segmento e il piano una retta e si ha una nuvola di punti (e maglie triangolari) indiviruati da coordinate secondo un qualche sistema di riferimento.<br>Per costruinre la box iniziale si considerano i valori minimi e massimi delle coordinate lungo tutti i componenti su tutta la nuvola.
2. **Individuare $x_h(t)$**, ovvero la posizione dell'avatar.
3. **Esprimere il piano** secondo l'equazione vista, calcolando $(a \ b \ c)$ dai vertici del triangolo.
4. **Performare la collision detection**:<br>Ponendo $x_p = x_h$ nell'equazione del piano e studiare il segno del risultato.<br>Se le coordinate di $x_h$ rientrano nel range della box allora può esserci contatto e si verifica in questo modom altrimenti non può e non è necessario alcun calcolo aggiuntivo.
5. **Suddividere la bounding box**: si suddivide la bounding box in ??? (`penso 3` #NOT_SURE_ABOUT_THIS ) per ogni dimensione se si è potenzialmente in contatto e si ripete fino ad avere un solo triangolo (o segmento).<br>Si ricalcola tutto al partire dal passo ***3***.

In teoria l'algoritmo viene eseguito sull'oggetto intero ma, consoscendo la posizione iniziale e la velocità del dito, si può restringere l'area, cioè il numero di triangoli su qui svolgere i calcoli.

----
###### Rendering Aptico
Se $x_h$ si trova all'interno della superficie si può rispondere con una forza normale alla superficie:<br>![[Pasted image 20240904191833.png]]
È necessario ininnazitutto trovare $x_p$ il punto a distanza minore a $x_h$ sulla superficie in quanto:$$F=k(x_h-x_p)$$Trovare $x_p$ è un problema di minimizzazione sulla distanza, dunque:$$d = \sqrt{(x_p -x_h)^{\tiny T} \cdot(x_p-x_h)}$$Ovvero:<br>![[Pasted image 20240904191943.png]]
L'ottimo si trova risolvendo:<br>![[Pasted image 20240904192007.png]]
Per quanto riguarda $k$, deve essere alto in modo che la forza sia sufficiente a non permettere deformazioni eccessive.
Bisogna però distinguere tra il $k$ del materiale reale e quello assunto dalla simulazione il quale sarà sempre minore per le limitazioni nella rappresentazione.
$k$ deve essere suffecentemente alto da evitare l'incocio in quanto si hanno più punti di contatto.
Si una un ulteriore $k$ diverso se la superficie è deformabile, e se viene deformata.

Si consideri un oggetto curvo, come una sfera.
In generale la differenza temporale tra un'azione ed il feedback non può superare la frazione di seconod, in quanto si avrebbe la dissociazione dei due eventi.
La computazione però potrebbe impiegare molto tempo dunque si deve cercare di usare meno dati possibili.
Si ipotizzi, per esempio, di voler approssimare la sfera con un cubo: le forze non possono essere dirette secondo normali a questo in quanto risulterebbe irrealistico:<br>![[Pasted image 20240904192433.png]]
Si potrebbe aumentare il numero di vertici, migliorando l'approssimazione, o si potrebbe utilizzare l'**interpolazione**: si consideri un punto sulla superficie reale e si calcolino i piani, considerando i punti adiacenti.
Per ognuno di essi si detrmina la normale secondo $x,\ y,\ z$ la funzione del piano oppure:$${1 \over (a^2 + b^2 + c^2)}\cdot \left<a \kern10px b \kern10px c  \right>$$Dove:
- $\left<a \kern10px b \kern10px c  \right>$ è un modo più carino di chiamare $(a \ b \ c)$. #NOT_SURE_ABOUT_THIS (non so se sono la stessa cosa, e se effettivamente questa formula è corretta, [[HCR - Handwritten Notes (Not Mine)|pagina 15 delle note scritte a mano]])

E facendo la media di queste si ottiene la normale al punto iniziale cioè:<br>![[Pasted image 20240904192930.png]]
Equivalente a risolvere il seguente sistema:<br>![[Pasted image 20240904192957.png]]
Dove:
- $(a \ b \ c)^{\tiny T}$ è l'ingognita e consiste nella normale al piano definito da tutti i punti.

Tenendo allora conto della costruzione fatta, se si penetra nella superficie, bisogna stabilire la normale della forza da applicare.
Si consideri inizialmente il caso bidimensionale rappresentato:<br>L'interpolazione permette di stabilire che:<br>![[Pasted image 20240904193146.png]]
In particolare, che:
1. Se $d_1 = 0$, $N = N_1$.
2. Se $d_2 = 0$, $N = N_2$.

Per il caso tridimensionale non si fa altro che applicare questo due volte.
Inannzitutto va scelto un vertice e va proiettato sul lato opposto passando per $x_p$, il quale è conosciuto dalla **collision detection**.
Si calcola poi la normale in $x_{pp}$ tramite l'interpolazione sul lato in cui si trova:<br>![[Pasted image 20240904193535.png]]
Infine si interpola sulla proiezione per calcolare la normale ad $x_p$:<br>![[Pasted image 20240904193603.png]]

Si consideri ora un oggetto fino (sottile): se $x_h$ è troppo in profondità l'algoritmo di collision detection riconoscerebbe dove più vicina la superficie inferiore e si avrebbe una forza diretta nel senso opposto:<br>![[Pasted image 20240904193732.png]]
Perciò va tenuta in memoria dello stato passato.
Per risolvere il problema, invece di prendere $x_p$ sulla superficie, si considera come centro di una sfera di raggio trascurabile, si traccia il segmento:$$\overline{x_h(k+1)\kern3px x_h(k)}$$Ed il piano intersecato è quello su cui unicamente va svolto l'algoritmo di collision detection:<br>![[Pasted image 20240904194056.png]]
Questa tecnica è detta **algoritmo di possibilità virtuale**.

----
###### Force Feedback
Finora si è trascurato l'attrito in quanto la forza applicata si assumeva perpendicolare alla superficie dunque la forza tangente è nulla.
Tenendo conto dell'attrito, data una forza non diretta lungo la normale, la forza reattiva, la quale è esattametne uguale e opposta, deve ricadere nel cono d'attrito.
Essa dunque è esprimibile come la somma dei componenti normale e tangente alla superficie:$$F_{\tiny N} = N^{\tiny T} F N = N N^{\tiny T} F$$Dove:
- $N^{\tiny N} F$ è il modulo della componente normale e $N$ il vettore normale.

Da $F = F_{\tiny N} + F_{\tiny T}$ : <br>![[Pasted image 20240904194348.png]]
Secondo l'**agoritmo di rendering**:
- $F = k_h\left[x_p(k) - x_h(k)\right]$ : è la forza reattiva esercitata dagli attuatori sulle dita.
- $F = k_h\left[x_p(k) - x_h(h)\right]$ : è la forza esercitata per muovere l'oggetto virtuale.

Un esempio sono: $J^{\tiny T} F = \tau$ e $F = M \ddot x$ .

Si consideri un oggetto rigido e si rappresenti il punto di contatto come una sfera di raggio nullo:<br>![[Pasted image 20240904194659.png]]
Cioè:$$x_o(k) = x_p(k)$$Allora $x_o(k+1) = x_p(k)$ e non dipende da $x_h$ in quanto la superficie è non deformabile e l'oggetto è statico.
Si consideri ora un oggetto deformabile:$$x_o(k+1) = F(x_h(k))$$Il modello più semplice per gli oggetti deformabile è la molla:<br>![[Pasted image 20240904194853.png]]
Per la quale: $\Delta x = {F \over k_0}$ dove $k_0$ nella simulazione può essere fissato stimando quello reale della deformazione ma è diverso da quello dell'interfaccia aptica:<br>![[Pasted image 20240904195008.png]]
Dunque la forza necessaria per ottenere tale deformazione è:<br>![[Pasted image 20240904195031.png]]
Dove:
- Per ***corpi rigidi***, $k_h \neq 0$ e $k_0 = 0$ .
- Per ***corpi morbidi***, $k_h \neq 0$ e $k_0 \neq 0$, e $k_h = k_0$, allora avremmo lo **stesso spostamento per entrambe**.

Si consideri l'implementazione di questi risultati per creare un simulatore: è necessario costruire un sistema a controreazione che sia asintoticamente stabile<br>![[Pasted image 20240904195247.png]]<br>![[Pasted image 20240904195256.png]]
Si ha un polo in $- {k_h \over k_0}$ che deve essere stabile, dunque:<br>![[Pasted image 20240904195346.png]]
Per stabilità si intende che al tocco di un oggetto virtuale, la parte di superficie coinvolta si stabilizza ad un certo valore.
In realtà il sistema non ha dinamica ma la assume in simulazione, dal momento che i calcolatori campionano e aggiornano il sistema secondo diversi valori della forza.

----
###### Oggetti Dinamici
La dinamica in generale degli oggetti è descrivibile attraverso **ode** e il problema più grande in simulazione è trocare risolutori di equazioni differenziali al fine di avere il **real-time**.
Si fa dunque uso di semplificazioni.
Un esempio di oggetto dinamico è:<br>![[Pasted image 20240905120929.png]]<br>![[Pasted image 20240905120935.png]]
La quale è un ode di 2° ordine e dipende dal tempo.
Si approssima ad un sistema di due equazioni differenziali di 1° ordine:<br>![[Pasted image 20240905121028.png]]
La dimensione del vettore è pari all'ordine dell'equazione (quindi: $2$).
Risolvendolo:<br>![[Pasted image 20240905121101.png]]
Dunque riconducendo il tutto alla forma $\dot x = Ax + Bu$ dove $u = F$ :<br>![[Pasted image 20240905121137.png]]

Si consideri ora lo spostamento di un oggetto in uno spazio 3D (esempio caso multivariable):<br>![[Pasted image 20240905121220.png]]
Si definisce lo stato:$$\lambda = \left(x ,\ y ,\ z ,\ \dot x ,\ \dot y ,\ \dot z\right)^{\tiny T} = \left(\lambda_1 ,\ \ldots ,\ \lambda_6 \right)^{\tiny T}$$Per passare a $6$ equazioni differenziali di grado $1$:<br>![[Pasted image 20240905121429.png]]
Dove: le componenti $m$ della massa sono uguali, ma quelle dell'inerzia sono diverse.
![[Pasted image 20240905121508.png]]
In generale:$$\dot x(t) = F(x(t) ,\ u(t))$$Ma i calcolatori lavorano nel discreto, per cui $\dot x(t)$ non esiste propriamente e:<br>![[Pasted image 20240905121622.png]]
Dove:
- $h$ è l'intervallo.
- $k \in \mathbb{N}$ .

Per determinare $\dot x$ si utilizza il **metodo di Eulero**, il quale consiste nell'approssimare $F$ alla sua **espansione di Taylor** al primo oridne:<br>![[Pasted image 20240905121744.png]]
***N.B.***: Se si conoscessro tutte le derivate di $F$ in un punto si potrebbe prevederla in un futuro qualsiasi.

Tale approssimazione ha però forti limitazioni, si prenda ad esempio una molla:<br>![[Pasted image 20240905121857.png]]
Secondo l'**equazione di Eulero**:<br>![[Pasted image 20240905121922.png]]
Per la stabiltà sin impone che $\left|1 - Keh\right|\lt 1$ :<br>![[Pasted image 20240905122033.png]]
Dunque più che $K e$ è alto, più $h$ diventa piccolo e peggiore è il *real-time*.
Il fatto che si ha un problema numerico fa capire che l'approssimazione è piuttosto grossolana.

Si utilizza dunque il **metodo del mid-point**, il quale considera il secondo termine derivato dell'espansione.

Si supponga di avere un sistema ad evoluzione libera:<br>![[Pasted image 20240905122233.png]]
La derivata secondo è stabilita sempre tramite l'**espansione di Taylor** svolta su $F$ :<br>![[Pasted image 20240905122317.png]]
Ma non si conosce $\Delta x$, secondo il metodo:$$\Delta x = {h \over 2} F(x_0)$$In modo da semplificare questa espressione.
Dunque sostituendo tutto nell'equazione iniziale:<br>![[Pasted image 20240905122441.png]]
Il termine aggiuntivo permette $h$ maggiori.

----
###### Transparency
La transparenza è un concetto legato alla dinamica dell'ambiente composto da un robot, che funge da interfaccia utente, e in questo caso, in simulatore virtuale dell'oggetto e della sua dinamica.
Si definisce:<br>![[Pasted image 20240905122606.png]]<br>![[Pasted image 20240905122802.png]]
La dinamica nel simulatore è descrivibile attraverso:<br>![[Pasted image 20240905122625.png]]

Il problema viene affrontato utilizzando la **Trasformata di Laplace**, la quale permette di transformare equazioni differenziali in algebriche.
Per condizioni iniziali nulle:<br>![[Pasted image 20240905122736.png]]

Si definisce **impedenza** il rapporto tra forza e velocità dell'oggetto:<br>![[Pasted image 20240905122858.png]]
Il problema è che esistono due dinamiche:
1. **La dinamica del robot**, la quale deve essere impercettibile.
2. **La dinamica del simulatore**, che è quella interessante.

Un sistema si definisce trasparente se l'unica dinamica è quella dell'oggetto virtuale.
La dinamica è data da:<br>![[Pasted image 20240905123035.png]]
Dove:
- $I_R \kern3px \ddot \theta$ è il momento torcente complessivo dell'interfaccia.
- $\tau$ quello applicato dal robot
- $J^{\tiny T} \kern2px F$ quello dell'utente.
- $B_R \kern3px \dot \theta$ è l'attrito viscoso dei **joints**.

Applicando **Laplace** a questa equazione:<br>![[Pasted image 20240905123302.png]]
Se si assume $K h$ molto alto, allora: $K h(t) = K_p (t)$ e $\dot x h(t) = \dot x_p(t) = \dot x_0(t)$ .
In quanto più rigido:<br>![[Pasted image 20240905123433.png]]
In realtà la forza percepita è:$$F(s) = Z_{\tiny \text{MF}}(s) \leq xh(s)$$Si riprende lo studio dell'effetto complessivo:<br>![[Pasted image 20240905123548.png]]
Per ottenere $F_{\tiny \text{M}}$ si deve portare$$-J^{\tiny T} \kern1px Z_{\tiny \text{J}} \kern2px J^{-1}=0$$E ciò è possobile riducendo l'ineriza, quindi il peso del braccio e l'attrito dei **joints**.
