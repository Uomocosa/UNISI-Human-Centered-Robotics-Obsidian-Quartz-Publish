---
aliases:
  - grasping
  - grasp
  - hand Jacobian
  - Jacobiana della mano
---
***Ricorda***:

> Dati i bracci del manipolatore, costruire le [[HCR - Screw Matrix|screw matrices]], per ogniuno di loro:$$\vec d = \left[\begin{array}{c} d_x \\ d_y \\ d_z \end{array}\right] \kern30px \text{e} \kern30px S(\vec d) = \left[\begin{array}{c} 0 & -d_z & d_y \\ d_z & 0 & -d_x \\ -d_y & d_x & 0 \end{array}\right]$$

> *~Ex.:*<br>![[Pasted image 20240903182148.png]]
> Bracci ([[HCR - Come definire i bracci o joints di un manipolatore|come definire i bracci o joints di un manipolatore]]):$$\vec d_1 = \left[\begin{array}{c} 0 \\ 1 \\ 0 \end{array}\right] \kern30px \text{e} \kern30px \vec d = \left[\begin{array}{c} 1 \\ 0 \\ 0 \end{array}\right] \kern30px \text{e} \kern30px \vec d = \left[\begin{array}{c} 0 \\ 1 \\ 0 \end{array}\right]$$Jacobiana della mano:$$J^{\tiny T} \ = \left[\begin{array}{c} S(d_1) & 0 \\ 0 & S(d_2) \\ 0 & S(d_3) \end{array}\right]$$Se la forza $F$ che vogliamo applicare appartiene al [[HCR - Kernel • Nullspace|kernel]] di questa matrice $J^{\tiny T}$, allora non è possibile per il manipolatore, applicare questa forza all'oggetto.

----
Nello studio del problema del grasping non si modellerà e lavorerà con il braccio ma con la mano dal momento che l'azione del "grasp" non richiede sono di gestire contemporaneamente le dita ma anche di farle collaborare.
Inoltre i bracci robotici non sono di interesse al momento che non è difficile reperirli sul mercato, a differenza delle mani, dove ogni dito può essere pensato come un braccio robotico e l'obbiettivo è quello di muovere oggetti/solidi.

Molte aziende di logistica, come '*Amazon*', investono in questo per poter automatizzare l'intero processo prima del transporto. 
Se il controllo è centralizzato il controllore gestisce tutto ma si parla di collaborazione se si hanno più controllori indipendenti.

==L'azione di manipolazione è divisibile in 3 parti==:
1. Avvicinamento all'oggetto.
2. Instaurazione del contatto ed interazione.
3. Movimento dell'oggetto.

Ci si concentrerà principalmente sulle ultime due e si studieranno tramite metodi e modelli algebrici e non ci si baserà su architetture specifiche.
==Innanzitutto bisogna distinguere tra i due tipi di grasping==:
1. ==***Grasping di potenza***==: dove l'obbiettivo è il **movimento statico** degli oggetti.
2. ==***Grasping di precisione***==: che permette **il movimento relativo tra l'oggetto ed il palmo**, evitando il movimento del braccio.<br>Il controllo è dato dai polpastrelli delle dita in modo che se ne possano sfruttare i gradi di libertà.

L'interazione con un oggetto è data dalle forze esercitate dalle singole dita, infatti posizione e velocità degli oggetti sono conseguenze di queste forze, ma ricordiamo che dipende anche dal modello del contatto.

Si consideri un sistema composto da due dita:<br>![[Pasted image 20240903182148.png]]
- $\tau_1,\ \tau_2,\ \tau_3$: momenti torcenti dei [[HCR - Catena Cinemantica|joints]].
- $F_1,\ F_2$ : forze esercitate dall'end effector, queste forze come si può vedere dalla figura, sono dovute ai momenti torcenti dei **joints**.

==Poiché le due devono collaborare, non si possono usare due [[HCR - Matrice Jacobiana|Jacobiane]] distinte, ma bisogna ricondursi ad'unica matrice==, cioè bisogna pensare al tutto come un unico robot con due catene cinematiche.
In generale data una forza $\vec F$ appicata ad un braccio $\vec d$, il procedimento per il calcolo del movimento torcente $\vec \tau$ può essere "compresso" attraverso la [[HCR - Screw Matrix|screw matrix]]:$$\vec d \times \vec F = S(\vec d) \cdot \vec F $$Dove:$$\vec d = \left[\begin{array}{c} d_x \\ d_y \\ d_z \end{array}\right] \kern30px \text{e} \kern30px S(\vec d) = \left[\begin{array}{c} 0 & -s_z & s_y \\ s_z & 0 & -s_x \\ -s_y & s_x & 0 \end{array}\right]$$Mentre la direzione del vettore $\vec \tau$ è data dalla [[HCR - Regola della Mano destra|regola della mano destra]].
Tale matrice può essere utilizzata per qualsiasi prodotto vettoriale.

Siano date le forze di contatto ed i momenti torcenti nei singoli [[HCR - Catena Cinemantica|joints]], si vuole stabilre una relazione che li leghi direttamente:$$ F_{c} = \left[\begin{array}{c} F_{\tiny T} \\ F_{\kern-1px\tiny I} \end{array}\right] \kern30px \text{e} \kern30px \tau = \left[\begin{array}{c} \tau_1 \\ \tau_2 \\ \tau_3  \end{array}\right]  $$Inoltre da ciò che si è visto:$$ V_{\tiny T} = J_{\tiny T} \cdot  \dot \theta_1   \kern30px \text{e} \kern30px V_{\kern-1px\tiny I} = J_{\kern-1px\tiny I} \cdot \left[\begin{array}{c} \dot \theta_2 \\ \dot \theta_3 \end{array}\right]  $$Da cui si ottiene:$$\left[\begin{array}{c} V_{\tiny T} \\ V_{\kern-1px\tiny I} \end{array}\right] = \left[\begin{array}{c} J_{\tiny T} & \mathbf{0} \\ \mathbf{0} & J_{\kern-1px\tiny I} \end{array}\right] \cdot \left[\begin{array}{c} \dot \theta_1 \\ \dot \theta_2 \\ \dot \theta_3 \end{array}\right] $$Dove:
- $\mathbf{0}$ o $\vec 0$ è un vettore o più in generale una sottomatrice composta di soli $0$.
- $V$ è il vettore di velocità dell'end effector.
- $J$ è la [[HCR - Matrice Jacobiana|Jacobiana]], $J_{\tiny T}$ ed $J_I$ distinguono le due **Jacobiane** legate alle due [[HCR - Catena Cinemantica|catena cinematiche]] dell'esempio.
- $\dot \theta$ è la velocità angolare.
- E la matrice:$$\left[\begin{array}{c} J_T \kern5px & \kern5px \vec 0 \\[7px] \vec 0 \kern5px & \kern5px J_I \end{array}\right]$$È la [[HCR - Calcolo della Matrice Jacobiana 'della Mano'|Jacobiana della mano]] (una matrice $\left[9\times 6\right]$), e la sua trasposizione è quella usata per le forze.

La [[HCR - Calcolo della Potenza di Contatto|potenza di contatto]] è data dalla somma delle potenze $M$ joints singoli, infatti la forza sull'**end effector** corrisponde ai momenti torcenti nei joints e la velocità lineare a quelle angolari:$$\begin{array}{l} \tau_1 \kern2px \dot \theta_1 + \tau_2 \kern2px \dot \theta_2 = F_{\kern-1px \tiny I}^{\tiny T} V_{\kern-1px \tiny I}^{\tiny}  \\[5px] \Rightarrow\kern10px \left[\begin{array}{c} \tau_1 & \tau_2 \end{array}\right] \cdot \left[\begin{array}{c} \dot\theta_1 \\ \dot\theta_2 \end{array}\right] = F_{\kern-1px \tiny I}^{\tiny T} \cdot J \cdot\left[\begin{array}{c} \dot\theta_1 \\ \dot\theta_2 \end{array}\right] \\[5px] \Rightarrow\kern10px \left[\begin{array}{c} \tau_1 & \tau_2 \end{array}\right] \cdot = F_{\kern-1px \tiny I}^{\tiny T} \cdot J \\[15px] \Rightarrow\kern10px \vec \tau_{\kern-1px \tiny I}  = F_{\kern-1px \tiny I}^{\tiny T} \cdot J   \end{array}  $$==Quindi in generale==:$$\tau = J^{\tiny T} F_e$$Dove:
- $\tau$ : è la **potenza di contatto**. #NOT_SURE_ABOUT_THIS $\tau$ `è il momento torcente,` $\dot \theta$ `è la velocità angolare, e` $\tau \cdot \dot \theta$ `è la potenza meccanica di un giunto, questo \tau NON è la potenza di contatto, è il vettore che rappresenta i momenti torcenti dei due giunti`
- $F_e$: forza dell'**end effector**.

Nel caso proposto si avrebbe che:$$\left[\begin{array}{c} \tau_1 \\ \tau_2 \\ \tau_3  \end{array}\right] = J^{\tiny T} \left[\begin{array}{c} F_{\tiny T} \\ F_{\kern-1px \tiny I} \end{array}\right] = \left[\begin{array}{c} S(d_1) & 0 \\ 0 & S(d_2) \\ 0 & S(d_3) \end{array}\right] \left[\begin{array}{c} F_{\tiny T} \\ F_{\kern-1px \tiny I} \end{array}\right] $$
#NOT_SURE_ABOUT_THIS `Come è possibile definire la jacobiana in questo modo???`
Dove:
- Le dimensioni della jacobiana sono quindi: #NOT_SURE_ABOUT_THIS  `interpretazione mia`$$(3\cdot n_j) \times (3\cdot n_c)$$Dove:
	- $n_j$ : numero di **joints**.
	- $n_c$ : numero di **contact points**.
- Inoltre per capire meglio ecco una **Jacobiana** con 3 **contact points** e 5 **joints**: #NOT_SURE_ABOUT_THIS `interpretazione mia`:$$\left[\begin{array}{c} \tau_1 \\ \tau_2 \\ \tau_3 \\ \tau_4 \\ \tau_5  \end{array}\right] = J^{\tiny T} \left[\begin{array}{c} F_{1} \\ F_{2} \\ F_{3} \end{array}\right] = \left[\begin{array}{c} S(d_1) & 0 & 0 \\ S(d_2) & 0 & 0 \\ 0 & S(d_3) & 0 \\ 0 & S(d_4) & 0 \\ 0 & 0 &  S(d_5) \end{array}\right] \left[\begin{array}{c} F_{1} \\ F_{2} \\ F_{3} \end{array}\right] $$***Ricorda*** che 


Ma dal momento che le forze hanno sempre il compoenente $z$ nullo, mentre al più l'ultimo elemento delle prime due righe di $S(d)$ non sono nulli, allora l'unico componenete non nullo di $\tau$ è $z$, come suggerisce la fisica:<br>![[Pasted image 20240903183339.png]]
Dunque il risultato precedente può essere così ridotto:<br>![[Pasted image 20240903183408.png]]

In generale la **Jacobiana** cambia in base alla configurazione del manipolatore (posizione links) e in base agli **end effectors**, i quali a loro volta dipendono da come viene afferrato un oggetto.

*~Ex.:*<br>![[Pasted image 20240903183526 - Copia.png]]
Definiamo i bracci del manipolatore: $$d_1 = \left[\begin{array}{c} 1 \\ 0 \\ 0 \end{array}\right] \kern30px \text{e} \kern30px d_2 = \left[\begin{array}{c} -1 \\ 0 \\ 0 \end{array}\right]$$Quindi, definiamo le rispettive screw matricies:$$S(d_1) = \left[\begin{array}{c} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{array}\right] \kern30px \text{e} \kern30px S(d_2) = \left[\begin{array}{c} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{array}\right]$$Definiamo la Jacobiana:<br> #NOT_SURE_ABOUT_THIS `Come è possibile definire la jacobiana in questo modo???` $$J = \left[\begin{array}{c} 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & -1 & 0 \end{array}\right]$$In questo problema di questa configurazione consiste nell'impossibilità di stringere (*squeeze*) gli oggetti.
- ***N.B.:*** La prima e quarta colonna sono uguali a $0$, queste colonne corrispondono alle componenti $x$ di entrambe le forze $F_1$ ed $F_2$.
- Da questo esempio emerge il concetto di [[HCR - Kernel • Nullspace|kernel di una matrice]], ==in particolare $F$ (la forza) appartiene al kernel di $J$== dal momento che: $$F^{\tiny T} \cdot J = 0$$E ciò vale per le forze direzionate lungo i link (*push/pull*) e lungo $z$.<br>In altre parole i kernel sono tutte le forze che sono resistite non attraverso un momento torcente ma attraverso i vincoli meccanici dei joints.

In conlusione: #NOT_SURE_ABOUT_THIS `Conclusioni pesonali`
- Se la forza che vogliamo imporre all'oggetto tramite il manipolatore, in questo caso per esempio una coppia di forze:$$\left[\begin{array}{c} F_1 \\ F_2 \end{array}\right] = \left[\begin{array}{c} -1 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{array}\right]$$E questo vettore appartiene al [[HCR - Kernel • Nullspace|kernel]] di $J$, allora non esiste nessuna combinazione/valore di $\tau$ che permetta al robot di imporlo, in questo caso il robot non è in grado di tenere fermo l'oggetto applicando due forze uguale e contrarie lungo l'asse $x$ dell'oggetto, basta vedere il disegno per capirlo.

----
- ***Esempio Originale*** (si usa una jacobiana ridotta, mi sembrava non troppo chiaro):  #NOT_SURE_ABOUT_THIS `Inoltre la seguente definizione dei bracci non rispetta quello che è stato detto precedentemente:` [[HCR - Come definire i bracci o joints di un manipolatore|come definire i bracci o joints di un manipolatore]], `ma la screw matrix la rispetta`
	- *~Ex.*:<br>![[Pasted image 20240903183526.png]]<br>In questo problema di questa configurazione consiste nell'impossibilità di stringere (*squeeze*) gli oggetti.
	- Da questo esempio emerge il concetto di [[HCR - Kernel • Nullspace|kernel di una matrice]], in particolare $F$ è kernel di $J$ dal momento che: $$F^{\tiny T} \cdot J = 0$$E ciò vale per le forze direzionate lungo i link (*push/pull*) e lungo $z$.<br>In altre parole i kernel sono tutte le forze che sono resistite non attraverso un momento torcente ma attraverso i vincoli meccanici dei joints.