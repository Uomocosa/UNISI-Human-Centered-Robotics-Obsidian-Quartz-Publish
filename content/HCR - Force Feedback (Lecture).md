***Ricorda***:
#NOT_SURE_ABOUT_THIS `Tutto quello che dirò in questo segmento è basato su idee e conclusioni personali, niente di tutto ciò è stato revisionato dal professore`

> ***Componente Normale della Forza***:$$F_{\tiny N} = N^{\tiny T} F N = N N^{\tiny T} F$$Dove:
> - $N^{\tiny T} F$ è il modulo della componente normale e $N$ il vettore normale alla superficie.<br> #NOT_SURE_ABOUT_THIS Probabilmente $N$ è il **versore** normale alla superficie.

> ***Componente Tangente o Trasverso della Forza***:$$\begin{array}{l} F_T &=& F-F_N \\[-5px] & \kern3px \downarrow & \\[-5px] &=&  F-NN^{\tiny T} F \\[-5px] & \kern3px \downarrow & \\[-5px] &=& \left(I - NN^{\tiny T} \right) \kern2px F  \end{array}$$

> Partendo dalla formula trovata [[HCR - Rendering Aptico (Lecture)|in precedenza]]:$$F = k(x_h - x_p)$$Definiamo $k_h$ il "coefficente elastico dell'interfaccia aptica" ($_h$ : *haptic*), e cambiamo leggermente la precedente formula in:$$F = k_h\left[x_h(k) - x_p(h)\right]$$Che rappresenta ***la forza esercitata per muovere l'oggetto virtuale*** e di conseguenza ***la forza reattiva esercitata dagli attuatori sulle dita*** sarà:$$F = k_h\left[x_p(k) - x_h(k)\right]$$(*Ovvero l'opposto*)

> Algoritmo di ***Force Feedback***:
> - ***Setup***
> 	1. Partiamo sapendo la posizione $x_h$, e il triangolo/piano che stiamo toccando.
> 	2. Troviamo $x_p$ come abbiamo visto [[HCR - Calcoli per la Minimizzazione di una Distanza|precedentemente]].
> 	3. Troviamo $F$ : *la forza reattiva esercitata sull'**end-effector***, usando la seguente formula:$$F = k_h\left[x_p(k) - x_h(k)\right]$$Dove: $k_h$ è un coefficente elastico stiamato dell'oggetto, se l'oggetto è rigido sarà più alto, se l'oggetto è morbido sarà più basso.
> - *Vediamo ora come possiamo descrivere l'evoluzione della posizione dell'**end-effector** nel discreto*:
> 	1. Se l'oggetto è rigido, ovvero non è deformabile, avremo che $\forall k$, possiamo dire:$$x_o(k) = x_p(k)$$Mentre se l'oggetto è deformabile, averemo che la posizione dell'**end-effector** nel mondo virtuale $(x_0)$ cambierà in base alla posizione che assume nel mondo reale $(x_h)$, maggiori spiegazioni su queste variabili di seguito:$$x_o(k+1) = f(x_h(k))$$Dove, prendiamo l'esempio di un gioco in realtà virtuale:
> 		- $x_0$ : rappresenta la posizione che vediamo nello schermo/**mondo virtuale** della mano/end-effector.
> 		- $x_h$ : la posizione nel **mondo reale** della mano/end-effector.
> 		- $x_p$ : il punto a distanza minima del triangolo/piano dell'oggetto con cui stiamo interagendo ed $x_h$ (definizione data [[HCR - Calcoli per la Minimizzazione di una Distanza|precedentemente]]).
> 		- $k_h$ : è il coefficiente elastico dato per restituire un **force feedback** all'utente, sulla base di $x_p$ ed $x_h$.
> 		- $k_0$ : è il coefficiente elastico che viene definito per deformare l'oggetto virtuale, data $F$ (il **force feedback**).
> 	2. Definiamo $\Delta x = x_0(k+1) - x_0(k)$ e definiamo inoltre un $k_0$ tale per cui: $$\Delta x = {F \over k_0}$$Dove, $k_0$ nella simulazione può essere fissato stimando quello reale, ma è diverso da quello dell'interfaccia aptica ($k_h$), quindi possiamo dire che:$$\begin{array}{l}   x_0(k+1)   &=&   x_0(k) + \Delta x   \\[-5px] & \kern3px \downarrow & \\[-5px] &=&    x_0(k) + {1 \over k_0}F   \\[-5px] & \kern3px \downarrow & \\[-5px] &=&   x_0(k) + {k_h \over k_0}\left[x_h(k) - x_p(k)\right]    \end{array}$$Dunque avremo che:<br>• La forza necessaria per ottenere una deformazione $\Delta x$ è:$$F = k_o \cdot \left|x_o(k) -x_o(k+1)\right|$$• Mentre la forza che resituiremo in feedback all'utente è pari a:$$F = k_h \cdot \left|x_h(k) -x_p(k)\right|$$Dove:
> 		- Per ***corpi rigidi***, $k_h \neq 0$ e $k_0 = 0$ in quanto non si deve avere una deformazione, ovvero per $k_0 = 0 \Rightarrow F = \infty$, per deformare un corpo rigido sarebbe necessaria una forza infinita, ma ovviamente per non far male all'utente, (non possiamo rispondere con una forza troppo alta) quindi  è necessario rispondere con una forza finita (ricorda che la forza reattiva è $F = k_h\left[x_p(k) - x_h(k)\right]$).
> 		- Per ***corpi morbidi***, $k_h \neq 0$ e $k_0 \neq 0$, e $k_h = k_0$, allora avremmo lo **stesso spostamento per entrambe**.

> Si consideri l'***implementazione di questi risultati*** per creare un simulatore, innanzitutto è necessario costruire un sistema a controreazione che sia asintoticamente stabile:<br>![[Pasted image 20240904195247.png]]
> Ovvero:$$\begin{array}{l}   Z[x_0(k+1)]   &=&   {\huge{k_h \over k_0}} {\huge{1 \over 1 + {{\huge k_{\normalsize h}} \over {\huge k_{\normalsize 0}}}z }} \cdot Z[x_0(k)]   \\[-5px] & \kern3px \downarrow & \\[-5px] &=&  {\huge{k_{\normalsize h} \kern1px z \over k_{\normalsize 0} \kern1px z + k_{\normalsize h}}} \cdot Z[x_h(k)] \end{array}$$Si ha un polo in $- {k_h \over k_0}$ che deve essere stabile, dunque:$$\left|{{k_h \over k_0}}\right| < 1 \kern25px \Rightarrow \kern25px k_h < k_0 $$Per stabilità si intende che: ==*al tocco di un oggetto virtuale, la parte di superficie coinvolta si stabilizza ad un certo valore*==.
> In realtà il sistema non ha dinamica ma la assume in simulazione, dal momento che i calcolatori campionano e aggiornano il sistema secondo diversi valori della forza
> Come si può vedere in oltre se il corpo è rigido, ergo per $k_0 = 0$ avremo che $x_0(k+1) = x_0(k)$ ovvero non penetremo la superficie iniziale (in quanto non deformabile)

----
Finora si è trascurato l'attrito in quanto la forza applicata si assumeva perpendicolare alla superficie dunque la forza tangente è nulla.
Tenendo conto dell'attrito, data una forza non diretta lungo la normale, la forza reattiva, la quale è esattametne uguale e opposta, deve ricadere nel cono d'attrito.
Essa dunque è esprimibile come la somma dei componenti normale e tangente alla superficie:$$F_{\tiny N} = N^{\tiny T} F N = N N^{\tiny T} F$$Dove:
- $N^{\tiny T} F$ è il modulo della componente normale e $N$ il vettore normale:<br>![[Pasted image 20240918124534.png|150]]
	- Come possiamo vedere $F$ o $-F$ deve ricadere nel cono di attrito, altrimenti l'oggetto scivolerebbe dalla presa, nel caso in cui $F$ non ha componenti tangenti, avremo che ricadrà per forza nel cono di attrito.<br>In questo caso invece con $F_{\tiny T} \neq 0$ non è detto.

Da $F = F_{\tiny N} + F_{\tiny T}$ (forza normale + forza tangente):$$\begin{array}{l} F_T &=& F-F_N \\[-5px] & \kern3px \downarrow & \\[-5px] &=&  F-NN^{\tiny T} F \\[-5px] & \kern3px \downarrow & \\[-5px] &=& \left(I - NN^{\tiny T} \right) \kern2px F  \end{array}$$

Secondo l'[[HCR - Rendering Aptico (Lecture)|algoritmo di rendering]] $\left(F = k(x_h - x_p)\right)$ avremo che:
- $F = k_h\left[x_p(k) - x_h(k)\right]$ : è la forza reattiva esercitata dagli attuatori sulle dita.
- $F = k_h\left[x_h(k) - x_p(h)\right]$ : è la forza esercitata per muovere l'oggetto virtuale.
	- $k_0$ : stima del coefficente elastico reale.
	- $k_h$ : coefficente elastico dell'interfaccia aptica ($_h$ : *haptic*)
- Un esempio sono: $J^{\tiny T} F = \tau$ e $F = M \ddot x$, forze uguali e contrarie.

![[Pasted image 20240918124600.png|200]]
- #NOT_SURE_ABOUT_THIS `Non riesco a capire questa figura, l'origne (O) non è sull'oggetto??? La distanza` $\overline{x_p \kern3px x_h}$ `cosa vuol dire? E la distanza` $\overline{x_0 \kern3px x_h}$ `è per caso la deformazione???`
- #NOT_SURE_ABOUT_THIS `Conclusioni/Spiegazione trovata arbitrariamente, non verificata`
	1. Partiamo sapendo la posizione $x_h$, e il triangolo/piano che stiamo toccando.
	2. Troviamo $x_p$ come abbiamo visto [[HCR - Calcoli per la Minimizzazione di una Distanza|precedentemente]].
	3. $F$ è la forza reattiva esercitata sull'**end-effector**, trovata usando la seguente formula: $$F = k_h\left[x_p(k) - x_h(k)\right]$$Dove: $k_h$ è un coefficente elastico stimato dell'oggetto, se l'oggetto è rigido sarà più alto, se l'oggetto è morbido sarà più basso.
	4. L'origine $O$ e la posizione $x_0$ è la posizione passata/precendete dell'**end-effector**.

Si consideri un oggetto **rigido** e si rappresenti il punto di contatto come una sfera di raggio nullo:<br>![[Pasted image 20240904194659.png]]
Cioè:$$x_o(k) = x_p(k)$$Allora $x_o(k+1) = x_p(k)$ e non dipende da $x_h$ in quanto la superficie è non deformabile e l'oggetto è statico.


Si consideri ora un oggetto **deformabile**:$$x_o(k+1) = f(x_h(k))$$(*Con $f$ una funzione qualsiasi*)
Il modello più semplice per gli oggetti deformabile è la molla:<br>![[Pasted image 20240904194853.png]]
Per capire la figura: #NOT_SURE_ABOUT_THIS `Di sotto si trovano tutte spiegazioni che mi sono dato, non sono verificate e probabilemente sbagliate.`
- Nella prima figura definiamo $x_0 = x_p$, in quanto abbiamo considerato una sfera di raggio nullo.
- Nel secondo caso, andimo a deformare l'oggetto, quindi avremo uno spostamento del vettore $x_0$, ovvero $x_0(k+1) \neq x_0(k)$, vediamo ora come definire questo spostamento
%%- Nel secondo caso, andimo a deformare l'oggetto, quindi avremo $x_0 \neq x_p$, e:
	1. $x_0(k$) : punto reale di contatto.
	2. $x_p(k$) : punto sul piano/triangolo su cui stiamo interagendo, rappresenta il punto per il quale la distanza $d = \overline{x_p \kern3px x_h}$ è minima. ([[HCR - Collision Detection (Lecture)|definizione]])
	3. $x_h(k$) : "***vettore avatar***" o "***vettore aptico***", che può essere all'interno della superficie, e se lo è rappresenta un contatto, inoltre possiamo usare la differenza tra $x_p$ ed $x_h$, ovvero tra il vettore che sta sul piano/triangolo e l'altro che lo penetra, e calcolando quanto viene "penetratro", andremo a restituire in feedback una forza più o meno forte ([[HCR - Collision Detection (Lecture)|definizione]])
%%
Definiamo $\Delta x = x_0(k+1) - x_0(k)$ e definiamo inoltre un $k_0$ tale per cui: $$\Delta x = {F \over k_0}$$Dove $k_0$ nella simulazione può essere fissato stimando quello reale della deformazione ma è diverso da quello dell'interfaccia aptica ($k_h$), quindi possiamo dire che:$$\begin{array}{l}   x_0(k+1)   &=&   x_0(k) + \Delta x   \\[-5px] & \kern3px \downarrow & \\[-5px] &=&    x_0(k) + {1 \over k_0}F   \\[-5px] & \kern3px \downarrow & \\[-5px] &=&   x_0(k) + {k_h \over k_0}\left[x_h(k) - x_p(k)\right]    \end{array}$$Dunque la forza necessaria per ottenere tale deformazione è:$$\begin{array}{l}   F   &=&   k_h \cdot \left|x_h(k) -x_p(k)\right|  \\[-5px] & \kern3px \downarrow & \\[-5px] &=&    k_o \cdot \left|x_o(k) -x_o(k+1)\right| \end{array} $$Dove:
- Per ***corpi rigidi***, $k_h \neq 0$ e $k_0 = 0$ in quanto non si deve avere una deformazione, ovvero per $k_0 = 0 \Rightarrow F = \infty$, per deformare un corpo rigido sarebbe necessaria una forza infinita, ma ovviamente per non far male all'utente, (non possiamo rispondere con una forza troppo alta) quindi  è necessario rispondere con una forza finita (ricorda che la forza reattiva è $F = k_h\left[x_p(k) - x_h(k)\right]$).
- Per ***corpi morbidi***, $k_h \neq 0$ e $k_0 \neq 0$, e $k_h = k_0$, allora avremmo lo **stesso spostamento per entrambe**.

Si consideri l'implementazione di questi risultati per creare un simulatore, è necessario costruire un sistema a controreazione che sia asintoticamente stabile:<br>![[Pasted image 20240904195247.png]]

Ovvero:$$\begin{array}{l}   Z[x_0(k+1)]   &=&   {\huge{k_h \over k_0}} {\huge{1 \over 1 + {{\huge k_{\normalsize h}} \over {\huge k_{\normalsize 0}}}z }} \cdot Z[x_0(k)]   \\[-5px] & \kern3px \downarrow & \\[-5px] &=&  {\huge{k_{\normalsize h} \kern1px z \over k_{\normalsize 0} \kern1px z + k_{\normalsize h}}} \cdot Z[x_h(k)] \end{array}$$Si ha un polo in $- {k_h \over k_0}$ che deve essere stabile, dunque:$$\left|{{k_h \over k_0}}\right| < 1 \kern25px \Rightarrow \kern25px k_h < k_0 $$Per stabilità si intende che: ==*al tocco di un oggetto virtuale, la parte di superficie coinvolta si stabilizza ad un certo valore*==.
In realtà il sistema non ha dinamica ma la assume in simulazione, dal momento che i calcolatori campionano e aggiornano il sistema secondo diversi valori della forza.
Come si può vedere in oltre se il corpo è rigido, ergo per $k_0 = 0$ avremo che $x_0(k+1) = x_0(k)$ ovvero non penetremo la superficie iniziale (in quanto non deformabile)
