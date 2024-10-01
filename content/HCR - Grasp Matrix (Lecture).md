***Ricorda***:

> Definiamo la **grasp matrix** come:$$\left[\begin{array}{c} F_{\tiny \text{NET}} \\ M_{\tiny \text{NET}} \end{array}\right] = \underbrace{\left[\begin{array}{c} I & I \\ S(d_1) & S(d_2) \end{array}\right]}_{\text{grasp matrix}} \left[\begin{array}{c} F_{c_1} \\ F_{c_2} \end{array}\right]$$Dove la [[HCR - Grasp Matrix • Matrice di Grasp|matrice di grasp]] contiene tante colonne, quanti sono i punti di contatto diversi ($i$):$$\left[\begin{array}{c} I \\ S(d_i)    \end{array}\right]$$Dove:
> - $d_i$ è un punto di contatto sull'oggetto.
> - $S(d_i)$ è la sua [[HCR - Screw Matrix|screw matrix]].

> *~Esempio:*
> ![[Pasted image 20240903184627 - Copy.png]]
> Definiamo:$$d_{1} = \left[\begin{array}{c} -2 \\ 0 \\ 0 \end{array}\right] \kern50px d_{2} = \left[\begin{array}{c} 2 \\ -1 \\ 0 \end{array}\right] \kern50px d_{3} = \left[\begin{array}{c} 2 \\ 1 \\ 0 \end{array}\right]$$Calcoliamo la grasp matrix:$$G = \left[\begin{array}{c} I & I & I \\ \begin{array}{c}  0 & 0 & 0 \\ 0 & 0 & 2 \\  0 & -2 & 0   \end{array} \kern3px & \kern3px \begin{array}{c}  0 & 0 & -1 \\ 0 & 0 & -2 \\  1 & 2 & 0   \end{array}  \kern3px & \kern3px  \begin{array}{c}  0 & 0 & 1 \\ 0 & 0 & -2 \\  -1 & 2 & 0   \end{array} \end{array} \right]$$

> Data la **grasp matrix** di un oggetto, e le forze che imponiamo ai contact points, avremo che, il [[HCR - Definition of 'Wrench'|wrench]] che otterremo è dato da:$$W = G F$$Dove:
> - $W = \left[F \kern10px \tau \right]^{\tiny T}$ di solito viene definito come $W = \left[F \kern10px M \right]^{\tiny T}$.<br>Questo per non confondere il momento torcente dell'oggetto (di solito chiamato $M$), con i momenti torcenti dei **joints** (di solito chiamati $\tau$).<br>Size: $[6 \times 1]$.
> - $G$ : **matrice di grasp** definita precedentemente.<br>Size: $[6 \times (3n_c)]$. ($n_c$ : *numero di contact points*)
> - $F = [F_{c_1} ,\ \ldots ,\ F_{c_n}]$ chiamato anche $F_{\tiny C}$: vettore di forze di ogni contact point o vettore di forze di contatto.<br>Size: $[(3n_c) \times 1]$. ($n_c$ : *numero di contact points*)

> Definiamo adesso $N(G)$ ovvero il [[HCR - Kernel • Nullspace|nullspace]] della **matrice di grasp** $G$, avremo che $N(G)$ sarà una matrice $[ ? \times (3n_c)]$, che contiene tutti i vettori $x$, tale per cui:$$x\in N(G) \kern10px : \kern10px Gx = 0$$Ovvero, tutti i vettori appartenti a $N(G)$ corrispondono a forze $F$ che non apportano modifiche al wrench dell'oggetto, ovvero applicata una forza$$F \in N(G) \kern15px\Rightarrow\kern15px G\cdot F = W = 0$$Essendo $N(G)$ una matrice, questo vale anche per tutti i vettori che sono **combinazioni lineari** delle righe della matrice, ovvero, dato un qualsiasi vettore $\xi$, scelto arbitrariamente avermo che:$$G \cdot [N(G) \kern2px \xi] = 0$$Dove: 
> - $N(G) \cdot \xi$ : ha le stesse dimensioni di $F$, ovvero: $[(3n_c) \times 1]$.
> - Il fatto che queste forze $\left(F = N(G)\cdot \xi \right)$ comportino un [[HCR - Definition of 'Wrench'|wrench]] nullo, non vuol dire che non hanno utilità, in quanto possano aiutare ad umentare la presa, l'attrito, per esempio stringendo più forte l'oggetto possiamo aumentare il [[HCR - Cono d'Attrito|cono d'attrito]].

> Per trovare le forze necessarie ad ottenere un certo [[HCR - Definition of 'Wrench'|wrench]] $W_0$, possiamo applicare la seguente formula inversa:$$F_{\tiny C} = G^{\#} (W_{0}) + N(G) \kern2px \xi$$Dove:
> - $G^{\#}$ : è la [[HCR - Pseudoinversa di una Matrice|pseudoinversa]] della **matrice di grasp**.
> - Consiglio: #NOT_SURE_ABOUT_THIS `Conclusioni personali`
> 	1. Prima di tutto trovare la soluzione $F'_{\tiny C} = G^{\#} (W_{0})$.
> 	2. Dopodichè trovare un vettore $\xi$ tale per cui le forze $F'_{\tiny C}$ rientrino nei rispettivi [[HCR - Cono d'Attrito|coni d'attrito]] di ogni contact point.
> 	3. Le formula finale sarà la stessa, ma almeno non dobbiamo tirare del tutto a caso la definizione del vettore $\xi$.

> ==Se il sistema non ha un [[HCR - Kernel • Nullspace|nullspace]], allora esso ha una sola soluzione, e le forze devono trovarsi necessariamente nel cono d'attrito per fare presa==, se non lo fossero, non si potrebbe intervenire artificalmente.
> Dunque per esseri sicuri di poter afferrare un oggetto, è necessario che ci siano infinite soluzioni, cioè:$$N(G) \neq 0$$Inoltre, se $G$ è a [[HCR - Rango Massimo|rango massimo]] (ed il rango massimo è uguale a $6$), si ha un [[HCR - Grasping (Lecture)|grasp]] che può muovere l'oggetto in ogni direzione.
> - #IMPORTANTE Una matrice con [[HCR - Kernel • Nullspace|nullspace]] nullo, ha rango massimo.
> - #IMPORTANTE Un [[HCR - Kernel • Nullspace|nullspace]] nullo, non comporta però una matrice a rango massimo

> Dopo aver trovato le forze dei contatti necessarie da applicare $(F_{\tiny C}$) tale per cui si abbia un certo [[HCR - Definition of 'Wrench'|wrench]] $(W)$, dobbiamo assicurarci che il manipolatore possa applicare queste forze, per verificarlo andremo a controllare la [[HCR - Grasping (Lecture)|Jacobiana della mano]] $(J)$, dopo averla calcolata calcoleremo i momenti torcenti dei **joints**, utilizzando la seguente formula:$$\tau = J^{\tiny T} \cdot F_{\tiny C}$$Possiamo racchiudere wrench, momenti torcenti, matrice di grasp, Jacobiana della mano e forze di contatto in un unico sistema:$$\begin{array}{c}\left[\begin{array}{c} W \\ \tau \end{array}\right] \\ {\tiny (n+6) \times 1} \end{array} \begin{array}{c} = \\ {\left.\right.} \end{array} \begin{array}{c}\left[\begin{array}{c} G \\ J^{\tiny T} \end{array}\right] \\ {\left.\right.} \end{array} \begin{array}{c}\left[\begin{array}{c} F_{c_{1}} \\ F_{c_{2}} \end{array}\right] \\ {\tiny (3n_c) \times 1} \end{array}$$Dove:
> - $n$ : è il numero di [[HCR - Catena Cinemantica|joints]] (riferimento a $(n+6) \times 1$).
> - $n_c$ : è in numero di **contact points** (riferimento a $(3 n_c) \times 1$).
> - $J$ : è la [[HCR - Grasping (Lecture)|Jacobiana della mano]].
> - Inoltre ricordiamo che per far avere una soluzione a questo sistema, ==è necessario che ci siano più equazioni che variabili==, cioè:$$n + 6 \geq 3 \kern2px n_c$$

----
Come si è visto nel [[HCR - Grasping (Lecture)|grasping]] alle forze applicate all'oggetto si contrappongono le forze vincolari di esso.
==Si studia ora il problema dal punto di vista dell'oggetto==.
La [[HCR - Grasp Matrix • Matrice di Grasp|matrice di grasp]], permette di stabilire, a partire dalle forze di contatto, l'effetto complessivo in termini di movimento.
==Si considera da ora come sistema di riferimento o quello fissato nel [[HCR - Baricentro|baricentro]] dell'oggetto==.
Lo spostamento in termini di traslazione e di rotazione può essere stabilito attraverso:$$\begin{array}{l} m\left[\begin{array}{c} \ddot x_0 \\ \ddot y_0 \\ \ddot z_0   \end{array}\right] = \sum \kern2px (\text{tutte le forze applicate all'oggetto}) \\[5px] \kern0px \kern6.5pxI\left[\begin{array}{c} \ddot \theta_0 \\ \ddot \theta_0 \\ \ddot \theta_0  \end{array}\right] = \sum \kern2px (\text{tutte i momenti torcenti applicati all'oggetto}) \end{array} $$Le quali definiscono la dinamica dell'oggetto.
Si consideri la prima equazione, innanzitutto esistono 3 tipi di forze:
1. **Forze di contatto**.
2. **Forze di gravità**.
3. **Forze ambientali**.<br>(*Quest'ultimo non verrà considerato.)

Si consideri il seguente esempio:<br>[[HCR - Grasp Matrix (Example I) • Python Script|Codice python per questo esempio]]<br>![[Pasted image 20240903184206 - Copy.png]]
Dove:$$F_{c_1} = \left[\begin{array}{c} F_{c{_1}x} \\ F_{c{_1}x} \\ F_{c{_1}x} \end{array}\right] \kern50px F_{c_2} = \left[\begin{array}{c} F_{c{_2}x} \\ F_{c{_1}x} \\ F_{c{_1}x} \end{array}\right]$$La forza totale:$$m\left[\begin{array}{c} \ddot x_0 \\ \ddot y_0 \\ \ddot z_0   \end{array}\right] = F_{\tiny\text{NET}}$$Ed in questo caso:$$F_{\tiny\text{NET}} = F_{c_{1}} + F_{c_{2}} = \underbrace{\left[\begin{array}{c}  I & I \end{array}\right]}_{G_{\tiny F}} \left[\begin{array}{c}  F_{c_1} \\ F_{c_2} \end{array}\right] \left.\begin{array}{c} {\tiny \leftarrow 3 \times 1} \\ {\tiny \leftarrow 3 \times 1} \end{array}\right.$$Per quanto riguarda la seconda equazione, è possible generare una rotazione (planare) sia tramite due o più forze, sia tramite l'applicazione di un [[HCR - Momento Torcente|momento torcente]], ma per trasmettere questo è necessario che l'**end effector** sia una superficie piatta, dunque si considerano solo le forze.

Si consideri il seguente esempio:<br>![[Pasted image 20240903184411.png]]
Unendo i due risultati si ottiene che:$$\left[\begin{array}{c} F_{\tiny \text{NET}} \\ M_{\tiny \text{NET}} \end{array}\right] = \underbrace{\left[\begin{array}{c} I & I \\ S(d_1) & S(d_2) \end{array}\right]}_{\text{grasp matrix}} \left[\begin{array}{c} F_{c_1} \\ F_{c_2} \end{array}\right]$$Dove la [[HCR - Grasp Matrix • Matrice di Grasp|matrice di grasp]] contiene tante colonne, quanti sono i punti di contatto diversi ($i$):$$\left[\begin{array}{c} I \\ S(d_i)    \end{array}\right]$$

----
Seguendo il seguente esempio:<br>[[HCR - Grasp Matrix (Example II) • Python Script|Codice python per questo esempio]]<br>![[Pasted image 20240903184627 - Copy.png]]
Definiamo:$$d_{1} = \left[\begin{array}{c} -2 \\ 0 \\ 0 \end{array}\right] \kern50px d_{2} = \left[\begin{array}{c} 2 \\ -1 \\ 0 \end{array}\right] \kern50px d_{3} = \left[\begin{array}{c} 2 \\ 1 \\ 0 \end{array}\right]$$
Calcoliamo la grasp matrix:$$G = \left[\begin{array}{c} I & I & I \\ \begin{array}{c}  0 & 0 & 0 \\ 0 & 0 & 2 \\  0 & -2 & 0   \end{array} \kern3px & \kern3px \begin{array}{c}  0 & 0 & -1 \\ 0 & 0 & -2 \\  1 & 2 & 0   \end{array}  \kern3px & \kern3px  \begin{array}{c}  0 & 0 & 1 \\ 0 & 0 & -2 \\  -1 & 2 & 0   \end{array} \end{array} \right]$$In generale la dinamica dell'oggetto è descritta come:$$\left[\begin{array}{c} F_{\tiny \text{NET}} \\ M_{\tiny \text{NET}} \end{array}\right] = G \left[\begin{array}{c} F_{c_{1}} \\ F_{c_{2}} \end{array}\right] = \left[\begin{array}{c}m & 0 \\ 0 & I \end{array}\right] \left[\begin{array}{c} \ddot x_0 & \ddot y_0 & \ddot z_0 & \ddot \theta_x & \ddot \theta_y & \ddot \theta_z \end{array}\right]^{\tiny T}$$Dove:$$m = \left[\begin{array}{c} m_x & 0 & 0 \\ 0 & m_y & 0 \\ 0 & 0 &  m_z \end{array}\right] \kern45px \text{e} \kern45px I = \left[\begin{array}{c} I_x & 0 & 0 \\ 0 & I_y & 0 \\ 0 & 0 &  I_z \end{array}\right]$$E specificatamente: #NOT_SURE_ABOUT_THIS `conclusioni personali`
- $m$ rappresenta la massa dell'oggetto: $m_x = m_y = m_z$.
- $I$ è la matrice di inerzia.

Tornando alla definizione della grasp matrix del primo esempio, si vogliono trovare ora i [[HCR - Kernel • Nullspace|kernel]] di $G$, nel caso di applicazione di due forze su un oggetto quadrato di lato $A$:$$\left[\begin{array}{c} F_{\tiny \text{NET}} \\ M_{\tiny \text{NET}} \end{array}\right] = \left[\begin{array}{c} 1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\0 & 0 & 1 & 0 & 0 & 1 \\0 & 0 & 0 & 0 & 0 & 0 \\0 & 0 & 2 & 0 & 0 & -2 \\0& -2 & 0 & 0 & 2 & 0 \end{array}\right] \left[\begin{array}{c} F_{c_{1}x} \\ F_{c_{1}y} \\ 0 \\ F_{c_{2}x} \\ F_{c_{2}y} \\ 0 \end{array}\right]$$In forma di sistema:$$\left\{\begin{array}{l} F_{c_{1}x} + F_{c_{2}x} = 0 \\ F_{c_{1}y} + F_{c_{2}y} = 0 \\ -2 F_{c_{1}x} + 2 F_{c_{2}x} = 0 \end{array}\right. \kern30px \Rightarrow \left\{\begin{array}{l} F_{c_{1}x} = - F_{c_{2}x} \\ F_{c_{1}y} = F_{c_{2}y} = 0 \end{array}\right. $$I [[HCR - Kernel • Nullspace|kernel]] (del primo esempio con soli due punti di ccontatto) hanno forma:$$\left[\begin{array}{c} F_{c_{1}x} \\ 0 \\ 0 \\ - F_{c_{2}x} \\ 0 \\ 0 \end{array}\right]$$In questo caso, non c'è alcun movimento dell'oggeto, ma ciò è preceduto al **grasp**, cioè le forze applicate devono avere modulo e direzione tali che l'oggetto **non scivoli** e che ci sia sufficente [[HCR - Attrito Statico|attrito statico]] da mantenere la presa, anche in caso di forze esterne.
In termini vettoriali si deve far in modo che le risultanti delle forze ai punti di contatto rientrino sempre nel [[HCR - Cono d'Attrito|cono d'attrito]]:<br>![[Pasted image 20240903184915.png]]
Se una forza esterna tenta di portare via l'oggetto e se le forze della presa non aumentano, la presa viene persa.
In generale per risolvere questo problema è necessario conoscere la [[HCR - Direzione Normale|direzione normale]] nei punti di contatto ed il [[HCR - Coefficiente d'Attrito|coefficiente di attrito]].
La forza esterna che si tratterà principalmente è quella di gravità e con $W_{\text{ext}}$ si indica il vettore:$$\left[\begin{array}{c}  F_{\text{ext}} \\ M_{\text{ext}}     \end{array}\right]$$Il probema può essere formulato come:$$G \left[\begin{array}{c}  F_{c_{1}} \\ F_{c_{2}} \end{array}\right]  = - W_{\text{ext}} \kern15px , \kern45px - W_{\text{ext}} =  \left[\begin{array}{c} 0 & -mg & 0 & 0 & 0& 0 \end{array}\right]^{\tiny T}$$Dove le forze di contatto sono le incognite, dunque:$$F_{\tiny C} = G^{\#} (-W_{\text{ext}}) + N(G) \kern2px \xi$$Dove: 
- $G^{\#}(-\omega)$ : sono i **componenti tangenti della forza/wrench esterno $\left( W_{\text{ext}}\right)$**.
	- $^{\#}$ indica la [[HCR - Pseudoinversa di una Matrice|pseudoinversa]].
-  $N(G)\cdot \xi$ : sono i **componenti normali della forza/wrench esterno $\left( W_{\text{ext}}\right)$**. #NOT_SURE_ABOUT_THIS `queste due definizioni di compononenti normali e tangenti l'ho trovate nelle soluzioni dell'`[[HCR ~ Exam 2017-04-04 (with Solutions)|esame del 04/04/2017]] `non so sono corrette`
	- $N(G)$ : [[HCR - Kernel • Nullspace|Nullspace]] di $G$. #NOT_SURE_ABOUT_THIS 
	- $\xi$ : è un vettore arbitrario che rappresenta una combinazione lineare dei vettori nel nullspace di $G$. #NOT_SURE_ABOUT_THIS `Definizione data da ChatGPT`
- [[HCR - Spiegazione Formula per il Bilanciamento delle Forze Esterne (ChatGPT)]]
	- $G^{\#}(-\omega)$ fornisce una soluzione particolare che bilancia le forze esterne.
	- $N(G) \xi$ rappresenta una componente aggiuntiva che può essere regolata senza influenzare la forza totale applicata sull'oggetto.
- #NOT_SURE_ABOUT_THIS $\xi$ `potrebbe essere il coefficiente di attrito, od un vettore che lo rappresenta.` `MOOOLTO probabile che sia una cazzata`

Se continuiamo con il caso del primo esmpio con 2 soli punti di contatto, applicando la formula precendente con $\xi = \bar{\bar{0}}$ ( #NOT_SURE_ABOUT_THIS `Non ho idea di cosa` $\xi$ `potrebbe essere` ), troveremo:$$F_C = \left[\begin{array}{l} 0 & {mg\over 2} &0 & 0 & {mg\over 2} & 0\end{array}\right]^{\tiny T}$$==Ma le forze non possono essere dirette parallelamente a quella di gravità perché non si avrebbe attrito con l'oggetto e scivolerebbe==.
Dunque a queste forze ($F_{C}$ o $F_{c_p}$), vanno sommate forze dirette verso l'interno ($F_{c_i}$) in modo che: $$F_{c_{\tiny\text{TOT}}} = F_{c_p} + F_{c_i}$$Dove, ripeto per chiarezza: #NOT_SURE_ABOUT_THIS `conclusioni personali`
- $F_{c_p}$ forze dei contact points trovate con la formula: $F_{\tiny C} = G^{\#} (-W_{\text{ext}})$, quindi, se guardiamo il risultato dell'esempio: $F_{c_p} = F_C = \left[\begin{array}{l} 0 & {mg\over 2} &0 & 0 & {mg\over 2} & 0\end{array}\right]^{\tiny T}$
- $F_{c_i}$ forze dirette internamente all'oggetto, o anche forze normali rispetto al piano/triangolo su cui si posano le dita, quindi se usiamo come esempio lo stesso (esempio dei due contact points avremo): $F_{c_i} = \left[\begin{array}{l} F_{\tiny\text{attrito}_1x} & 0 &0 & -F_{\tiny\text{attrito}_2x} & 0 & 0\end{array}\right]^{\tiny T}$. Ovvero due forze direzionate lungo l'asse $x$.

Le forze "verso l'interno" $\left(F_{c_{i}} \right)$, sono forze che devono essere aggiunte solo se il kernel della matrice non è nullo, ovvero se $G$ non è di rango massimo:
#NOT_SURE_ABOUT_THIS `rielaborazione/conclusione personale`$$F_{c_i} \in N(G) \kern15px\Rightarrow\kern15pxG\cdot F_{c_i} = 0$$
Vogliamo inoltre che le forze applicate rientrino nel cono di attrito, per ottenere questo è necessario applicare il giusto momento torcente, con le due equazioni:
1. $-W = G \cdot F$ : che invertita permette di stabilire la forza al contatto da applicare per il **grasp**.
2. $\tau = J^{\tiny T} \cdot F$ : che permette di stabilire il momento torcente necesarrio per applicare $F$.

Nel grasping, però è importatnte avere misure in feedback delle forze applicate, conoscendo il momento torcente applicato.
Per avere queste informazione, dato il seguente sistema:$$\begin{array}{c}\left[\begin{array}{c} -W \\ \tau \end{array}\right] \\ {\tiny (n+6) \times 1} \end{array} \begin{array}{c} = \\ {\left.\right.} \end{array} \begin{array}{c}\left[\begin{array}{c} G \\ J^{\tiny T} \end{array}\right] \\ {\left.\right.} \end{array} \begin{array}{c}\left[\begin{array}{c} F_{c_{1}} \\ F_{c_{2}} \end{array}\right] \\ {\tiny (3n_c) \times 1} \end{array}$$Dove:
- $n$ : è il numero di [[HCR - Catena Cinemantica|joints]] (riferimento a $(n+6) \times 1$).
- $n_c$ : è in numero di **contact points** (riferimento a $(3 n_c) \times 1$).
- $J$ : è la [[HCR - Grasping (Lecture)|Jacobiana della mano]].

==È necessario che ci siano più equazioni che variabili==, cioè:$$n + 6 \geq 3 \kern2px n_c$$Nel caso raffigurato di [[HCR - Enveloping Grasping|enveloping grasping]]:<br>![[Pasted image 20240921095329.png]]<br>È importante valutare le forze, infatti si hanno $10$ equazioni e $12$ variabili, ma non è rivelante che esse siano nel **cono d'attrito**, dal momento che l'oggetto è bloccato dalla presa.

==Se il sistema non ha un [[HCR - Kernel • Nullspace|nullspace]], allora esso ha una sola soluzione, e le forze devono trovarsi necessariamente nel cono d'attrito per fare presa==, se non lo fossero, non si potrebbe intervenire artificalmente.
Dunque è necessario che ci siano infinite soluzioni, cioè:$$N(G) \neq 0$$Inoltre, se $G$ è a [[HCR - Rango Massimo|rango massimo]] (ed il rango massimo è uguale a $6$), si ha un [[HCR - Grasping (Lecture)|grasp]] che può muovere l'oggetto in ogni direzione.
#IMPORTANTE Una matrice con [[HCR - Kernel • Nullspace|nullspace]] nullo, ha rango massimo.
#IMPORTANTE Un [[HCR - Kernel • Nullspace|nullspace]] nullo, non comporta però una matrice a rango massimo.

- ***N.B.:*** Riprendendo i due esempi con 2 punti di contatto e 3 punti di contatto, abbiamo che:
	- Per il problema dei 2 punti di contatto, la matrice di grasp $G$ **non** ha rango massimo.
	- Per il problema dei 3 punti di contatto, la matrice di grasp $G$ **ha** rango massimo.
	- Entrambe le matrici di grasp dei due problemi hanno un nullspace non nullo.
- Infatti se prendiamo un cubo con due dita (per esempio due dita di mani diverse), avremo che possiamo spostare il cubo in tutte e 3 le dimensioni, ma possiamo rotarlo solo in 2.<br>Mentre se lo prendiamo con 3 dita, come nel problema relativo (quindi $G$ ha rango massimo) possiamo spostare e rotare lo stesso cubo in tutte le direzioni.
