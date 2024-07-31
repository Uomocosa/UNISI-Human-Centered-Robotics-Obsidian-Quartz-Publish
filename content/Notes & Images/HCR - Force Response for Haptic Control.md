# Force Response for Haptic Control
![[SmartSelect_20220310-093503_Samsung Notes.jpg]]

Consideriamo un oggetto (tenendo conto dell'attrito), ed una forza **non** diretta lungo la normale, la forza reattiva, la quale è esattamente uguale ed opposta, deve ricadere nel cono d'attrito.
![[Pasted image 20220407154527.png]]
Essa dunque è esprimibile come la somma dei componenti normale e tangente alla superficie:
$$
F_N = N^T \cdot F \cdot N
$$
Dove:
-> $N^T \cdot F$ è il module della componente normale ed $N$ il vettore normale

Quindi, sapendo che: $F = F_N + F_T$
$$
\begin{array}{l}
F_T &= F - F_N
\\[-7px] &\ | \\[-7px]
&= F - NN^TF
\\[-7px] &\ | \\[-7px]
&= (I - NN^T) \kern 2px F
\end{array}
$$
Dove:
-> $I$ è la matrice di identità
-> $F$ : vettore forza completo
-> $F_N$ : vettore forza con versore definito dalla normale
-> $F_T$ : vettore forza con versore definito dalla **perpendicolare** della normale

Secondo l'algoritmo di rendering:
$$
F = k_h \left[x_p\left(k\right) - x_h\left(k\right) \right]
$$

^d956d8

-> Definisce la forza reattiva esercitata dagli attuatori sulle dita
$$
- F = k_h \left[x_h\left(h\right) - x_p\left(h\right) \right]
$$

^039a5a

-> Definisce la forza esercitata per muovere l'oggetto virtuale.
![[Pasted image 20220407155912.png]]

Nelle formula sopra si definisce:
-> $k_p$ : coefficiente elastico deciso arbitrariamente (trasforma il discostamento tra $x_p(k)$ ed $x_h(k)$ in una forza)
-> $x_p$ : proxy point (dove si trova la mano nella realtà virtuale che sta toccando l'oggetto) all'istante $k$
-> $x_h$ : human point (dove si trova realmente la mano dell'utente) all'istante $k$

Vengono definiti: $x_h$ , $x_p$ ed alcuni algoritmi per calcolarli qui:
- #TODO
- #TODO
- #TODO

---
###### ~Es.:
Un esempio dell'utilizzo delle formule ([[#^d956d8|prima]] e [[#^039a5a|seconda]]) sopra riportate si può vedere con:
$$
\begin{array}{l}
J^T F = \tau 
\\
F = M\ddot x 
\end{array}
$$
Dove la prima forza è relativa all'end-effector del robot.
La seconda è la formula della forza base usata nel mondo virtuale (a seconda di quanto viene misurata la prima dell'e.e.).

---
# Oggetto deformabile
Si consideri ora un oggetto rigido e si rappresenti il punto di contatto come una sfera di raggio nullo, cioè $x_p(k) = x_p(h)$
![[Pasted image 20220407160738.png]]

-> Allora $x_0(k+1) = x_0(k)$ e non dipende da $x_h$ in quanto la superficie è **non deformabile** e l'oggetto è statico.

Si consideri ora un oggetto deformabile:
$$
x_0(k+1) = \mathcal{F}\left(x_h\left(k\right)\right)
$$

Il modello più semplice per gli oggetti deformabili è una molla:
![[Pasted image 20220407161039.png]]

Per la quale $\Delta x = \frac{F}{k_0}$  
Dove $k_0$ nella simulazione può essere fissato stimando quello reale della deformazione ma è diverso da quello dell'interfaccia aptica.
$$
\begin{array}{l}
x_0(k+1) &= x_0(k) + \Delta x
\\[-7px] &\ | \\[-7px]
&= x_0(k) + \large \frac{F}{k_0}
\\[-7px] &\ | \\[-7px]
&= x_0(k) + \huge \frac{
k_h\left(x_h\left(k\right) - x_p\left(k\right)\right)
}{k_0}
\end{array}
$$
Dunque la forza necessaria per ottenere tale deformazione è:
$$
\begin{array}{l}
F &= k_h(x_h(k) - x_p(k))
\\[-7px] &\ | \\[-7px]
&= k_0(x_0(k) - x_0(k))
\end{array}
$$
Dove, per corpi rigidi:
-> $k_h \neq 0$
-> $k_0 = 0$
Mentre per corpi morbidi:
-> $k_h \neq 0$
-> $k_0 \neq 0$
-> $k_h = k_0$ (-> stesso spostamento $\Delta x$ per entrambe)

---
# Diagramma per il Force Response
Si consideri l'implementazione di questi risultati per creare un simulatore: è necessario costruire un sistema a controreazione che sia asintoticamente stabile.
![[Pasted image 20220407162420.png]]

$$
\begin{array}{l}
Z[x_0(k+1)] &= \Huge \frac{ \frac{h_h}{(k_0)}}{1 +  \frac{h_h}{(k_0)}z} \normalsize Z[x_h(k)]
\\[-7px] &\ | \\[-7px]
&= \Huge \frac{k_h \kern 3px z}{k_0 \kern 3px z + k_h} \normalsize Z[x_h(k)]
\end{array}
$$
Si ha un polo in $- \large \frac{k_h}{k_0}$ che deve essere stabile, dunque:
$$
\left| \frac{k_h}{k_0}\right| < 1
\kern 30px \Rightarrow \kern 30px
k_h < k_0
$$
Per stabilità si intende che al tocco di un oggetto virtuale la parte di superficie coinvolta si stabilizza per un certo valore.
In realtà il sistema non ha dinamica ma la assume in simulazione dal momento che i calcolatori compiono ed aggiornano il sistema secondo diversi valori della forza.