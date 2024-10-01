- ***Sono arrivato al seguente punto negli appunti che ti ho passato all'inizio***: <br>***La forza esterna che si tratterà principalmente è quella di gravità e con $W_{\text{ext}}$ si indica il vettore***:$$\left[\begin{array}{c} F_{\text{ext}} \\ M_{\text{ext}} \end{array}\right]$$***Il probema può essere formulato come***:$$G \left[\begin{array}{c} F_{c_{1}} \\ F_{c_{2}} \end{array}\right] = - W_{\text{ext}} \kern15px , \kern45px - W_{\text{ext}} = \left[\begin{array}{c} 0 & -mg & 0 & 0 & 0& 0 \end{array}\right]^{\tiny T}$$***Dove le forze di contatto sono le incognite, dunque***:$$F_{\tiny C} = G^{\#} (-W_{\text{ext}}) + N(G) \kern2px \xi$$***Dove l'unica cosa che so per certo è che $G^{\#}$ è la pseudoinversa della grasp matrix $G$, aiutami a capire che cosa vuol dire e che cosa sono i componenti della ultima formula***.<br>(*ChatGPT 4o*)
	- Ottimo, vediamo insieme i componenti della formula per capire cosa sta succedendo in questo contesto, che riguarda il **grasping** robotico.
	- ***Riassunto della situazione***:
		- Sei nel contesto della presa robotica e stai analizzando le **forze di contatto** che agiscono su un oggetto afferrato da un robot.<br>Il problema che stai trattando riguarda principalmente la gestione delle forze esterne, con particolare attenzione alla forza di gravità, indicata come $W_{\text{ext}}$.<br>Le forze di contatto $F_c$ devono bilanciare queste forze esterne per garantire che l'oggetto non scivoli o si muova in maniera indesiderata.
		- Vediamo i vari componenti della formula che hai:
	1. ***Forza esterna $W_{\text{ext}}$***:
		- Il vettore $W_{\text{ext}}$ rappresenta la forza esterna, che in questo caso è principalmente la forza di gravità.<br>È scritto come:$$W_{\text{ext}} = \begin{pmatrix} F_{\text{ext}} \\ M_{\text{ext}} \end{pmatrix}$$
		- $F_{\text{ext}}$: è la forza esterna applicata, ad esempio la gravità $\mathbf{g}$.
		- $M_{\text{ext}}$: è il momento esterno applicato sull'oggetto.
		- Nel tuo caso, $W_{\text{ext}}$ è definito come:$$W_{\text{ext}} = \begin{pmatrix} 0 \\ -mg \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}$$Questo descrive una forza di gravità $-mg$ lungo l'asse $y$ (se assumiamo che l'asse $y$ sia quello verticale), e nessun momento esterno agisce sull'oggetto.
	2. ***La matrice di grasp $G$***:
		- La **grasp matrix** $G$ collega le forze di contatto $F_c$ esercitate dalle dita del robot all'oggetto, con la forza totale e il momento esercitato sull'oggetto.<br>In altre parole, $G$ descrive come le forze applicate in ciascun punto di contatto contribuiscono alla forza e al momento complessivi sull'oggetto.
		- Il sistema di equazioni:$$G \begin{pmatrix} F_{c_1} \\ F_{c_2} \end{pmatrix} = - W_{\text{ext}}$$rappresenta la relazione tra le forze di contatto $F_{c_1}$ e $F_{c_2}$ (cioè le forze applicate dalle dita del robot nei punti di contatto) e la forza esterna $W_{\text{ext}}$, che in questo caso è la gravità.
	3. ***Pseudoinversa della grasp matrix $G^{\#}$***:
		- Come hai già menzionato, $G^{\#}$ è la **pseudoinversa di Moore-Penrose** della grasp matrix $G$.<br>Questa viene usata quando $G$ non è una matrice quadrata o non è invertibile, permettendo comunque di risolvere il sistema di equazioni in un senso approssimato.
		- La formula:$$F_C = G^{\#} (-W_{\text{ext}})$$è una soluzione che minimizza l'errore delle forze di contatto $F_C$, garantendo che la forza esterna $W_{\text{ext}}$ sia bilanciata in modo efficace.<br>Tuttavia, questa soluzione potrebbe non essere unica.
	4. ***Nullspace $N(G)$***:
		- Il termine $N(G) \xi$ rappresenta la **soluzione nel nullspace** di $G$.<br>Il nullspace di una matrice contiene tutti i vettori $\mathbf{x}$ tali che $G \mathbf{x} = 0$.<br>Questo significa che qualsiasi forza aggiuntiva nel nullspace di $G$ non influenzerà la forza totale sull'oggetto, ma può comunque essere applicata.
		- Il parametro $\xi$ è un vettore arbitrario che rappresenta una combinazione lineare dei vettori nel nullspace di $G$.<br>Quindi, la formula completa per $F_C$ diventa:$$F_C = G^{\#} (-W_{\text{ext}}) + N(G) \xi$$Questo significa che:
		- $G^{\#} (-W_{\text{ext}})$ fornisce una soluzione particolare che bilancia le forze esterne.
		- $N(G) \xi$ rappresenta una componente aggiuntiva che può essere regolata senza influenzare la forza totale applicata sull'oggetto.
	- ***Esempio di utilizzo***:
		- Immagina un robot che afferra un oggetto pesante soggetto alla gravità.<br>Le forze di contatto $F_C$ che il robot applica devono bilanciare la forza di gravità.<br>Tuttavia, il robot potrebbe avere **ridondanza** nei gradi di libertà, cioè potrebbe applicare forze aggiuntive nei punti di contatto che non cambiano la presa effettiva sull'oggetto.<br>Queste forze extra sono rappresentate dal termine $N(G) \xi$.
		- In questo modo, puoi usare la soluzione della pseudoinversa per bilanciare la forza esterna, ma allo stesso tempo hai la libertà di aggiungere forze ridondanti nei punti di contatto per ottimizzare la presa (ad esempio, per evitare movimenti o migliorare la stabilità).
	- ***Conclusione***:
		- La formula:$$F_C = G^{\#} (-W_{\text{ext}}) + N(G) \xi$$descrive le forze di contatto necessarie per bilanciare la forza esterna (la gravità), usando la pseudoinversa della grasp matrix.<br>Il termine $N(G) \xi$ rappresenta le forze aggiuntive che possono essere applicate senza influenzare l'equilibrio generale.
----
