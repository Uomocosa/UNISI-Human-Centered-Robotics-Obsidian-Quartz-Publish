---
aliases:
  - impedenza
  - trasparenza
---
***Ricorda***:

> *La transparenza è un concetto legato alla dinamica dell'ambiente composto da un robot che funge da **interfaccia utente**, ed in questo caso, un **simulatore virtuale** dell'oggetto e della sua dinamica*.

> ***Definizione di Trasparenza***:
> "==*Un sistema si definisce trasparente se l'unica dinamica è quella dell'oggetto virtuale*==".

> ***[[HCR - Definition of 'Impedance'|Impedenza]]***:
> Si definisce impedenza il rapporto tra **forza** e **velocità** di un robot:$$Z = {F \over V}$$

> ***Sistema dinamico di un semplice robot che funge da interfaccia utente***:<br>![[Pasted image 20240905123302 - Copy.png]]
> Di sotto la spiegazionie/passaggi.
> #NOT_SURE_ABOUT_THIS `Credo che in input sia necessaria solo` $-J^{\tiny T} F(s)$ `in quanto` $\tau(s)$ `viene data dalla controreazione, ovvero da` $J^{\tiny T} \cdot F_h(s) = \tau(s)$.

> ***Calcoli/Spiegazione del sistema dinamico***:
>  1. Partiamo dal segeuente robot:<br>![[Pasted image 20240919173300.png]]<br>E definiamo la sua dinamica come:$$M \ddot x_0(t) = F - B \dot x_0(t) - kx_0(t)$$
>  2. Applicando la **trasformata di Laplace** otteniamo:$$Ms^2 X_0(s) = F_h(s) - Bs X_0(s) -kX_o(s)$$
>  3. Definiamo **la dinamica dell'interfaccia**: $$I_{\kern-2px\tiny R} \kern1px \ddot \theta = \tau - J^{\tiny T} \kern-1px F - B_{\kern-2px\tiny R} \kern2px \dot \theta$$Dove:
> 	 - $I_{\kern-2px\tiny R} \kern1px \ddot \theta$ : è il momento torcente complessivo dell'interfaccia.
> 	 - $\tau$ : momento torcente applicato dal robot.
> 	 - $J^{\tiny T} \kern-1px F$ :  momento torcente applicato dell'utente, dove $J$ è la [[HCR - Matrice Jacobiana|Jacobiana]].
> 	 - $B_{\kern-2px\tiny R} \kern2px \dot \theta$ : è l'attrito viscoso dei **joints**.
> 4. Applicando nuovamente **Laplace** a quest'ultima equazione troviamo:$$s \cdot \Theta(s)  = \left(I_{\kern-2px\tiny R} \kern1px s + B_{\kern-2px\tiny R} \kern1px \right)^{-1} \left[ \tau(s) - J^{\tiny T} \kern-1px F(s) \right]$$
> 5. E definiamo l'**impedenza dei joint** come:$$\left(I_{\kern-2px\tiny R} \kern1px s + B_{\kern-2px\tiny R} \kern1px \right) := Z_j$$
> 6. Ricordando la definizone di $x_h$ data [[HCR - Force Feedback (Lecture)|in precedenza]], ovvero "*la posizione dell'end-effector nell'ambiente virtuale*", la definizione di ***impedenza*** data in questa lezione:$$F = Z\cdot V$$Ed infine utilizziamo Lapace per scrivere:$$V(s) = s\cdot X_h(s)$$Quindi, possiamo dire che la dinamica **del solo ambiente virtuale** è data da:$$F_h(s) = Z_{\kern-1px \tiny E}(s) \cdot s \cdot X_h(s) \kern30px$$
> 7. La forza totale percepita invece è:$$F(s) = Z_{\tiny \text{MF}}(s) \cdot s \cdot x_h(s)$$
> 8. Facendo gli opportuni calcoli andremo a trovare:$$F(s) = \underbrace{\kern-2.5px\left(-J^{\tiny T} Z_j J^{-1} + Z_{\kern-1px \tiny E} \right)\kern-7px}_{\huge Z_{\normalsize MF}}\kern5px \cdot s \cdot X_h(s)$$
> 9. In fine per ottenere $Z_{\tiny MF} = Z_E$ ovvero, avere che l'impedenza percepita è uguale alla sola impedenza virtuale, quindi avere un **sistema trasparente**, dovremo portare:$$-J^{\tiny T} \kern1px Z_{\tiny \text{J}} \kern2px J^{-1}=0$$E ciò è possibile solo azzerando l'ineriza, quindi il peso del braccio e l'attrito dei **joints**.<br>==Ovviamente **non è possibile** portare a $0$ il peso del braccio e l'attrito dei joints, possimo solo avvicinarci ad un sistema propiamente trasparente==.

----
La transparenza è un concetto legato alla dinamica dell'ambiente composto da un robot, che funge da interfaccia utente, e in questo caso, in simulatore virtuale dell'oggetto e della sua dinamica.
Si definisce:<br>![[Pasted image 20240905122606.png]]<br>![[Pasted image 20240905122802.png]]
La dinamica nel simulatore è descrivibile attraverso:$$M \ddot x_0(t) = F - B \dot x_0(t) - kx_0(t)$$Il problema viene affrontato utilizzando la **Trasformata di Laplace**, la quale permette di transformare equazioni differenziali in algebriche.
La trasformata di Laplace della derivata di una funzione, per condizioni iniziali nulle è la seguente:$$\begin{array}{l} L\left[ x_0(t) \right] = X_0(s) \\ L\left[ \dot x_0(t) \right] = s \cdot X_0(s) \\ L\left[ \ddot x_0(t) \right] = s^2 \cdot X_0(s) \\[3px] \kern0px \Rightarrow Ms^2 X_0(s) = F_h(s) - Bs X_0(s) -kX_o(s)  \end{array}$$Si definisce **impedenza** il rapporto tra forza e velocità dell'oggetto:$$Z = {F\over V}$$Quindi possiamo scrivere la formula di prima come:$$\begin{array}{l}   &\Rightarrow& F(s) &=&  Z(s) \cdot V(s)   \\[-5px]&\kern3px\downarrow&\\[-5px]   &\Rightarrow& F_h(s) &=&  Z(s)\cdot s \cdot X_0(s)   \\[-5px]&\kern5.3px|\kern3px&\\[-5px]  &\kern5.3px|& F_h(s) &=&  MsV(s) + BV(s) + k \kern1px {\large{V(s) \over s}} \\[-5px]&\kern3px\downarrow&&\kern3px\downarrow&\\[-5px]   &\Rightarrow& F_h(s) &=&   \underbrace{\left(Ms + B + \large{{k\over s}} \right)}_{Z\text{ : impedenza della dinamica}} \kern-18px \cdot s \cdot X_0(s) \end{array}$$Il problema è che esistono due dinamiche:
1. **La dinamica del robot**, la quale deve essere impercettibile.
2. **La dinamica del simulatore**, che è quella interessante.


==Un sistema si definisce trasparente se l'unica dinamica è quella dell'oggetto virtuale==.

Consideriamo ora questo sistema:
![[Pasted image 20241001005132.png|333]]
La dinamica reale è data da:$$I_{\kern-2px\tiny R} \kern1px \ddot \theta = \tau - J^{\tiny T} \kern-1px F - B_{\kern-2px\tiny R} \kern2px \dot \theta $$Dove:
- $I_{\kern-2px\tiny R} \kern1px \ddot \theta$ è il momento torcente complessivo dell'interfaccia.
- $\tau$ quello applicato dal robot
- $J^{\tiny T} \kern-1px F$ quello dell'utente, dove $J$ è la [[HCR - Matrice Jacobiana|Jacobiana]].
- $B_{\kern-2px\tiny R} \kern2px \dot \theta$ è l'attrito viscoso dei **joints**.

Applicando **Laplace** a questa equazione:$$\begin{array}{l}   I_{\kern-2px\tiny R} \kern1px s^2 \kern1px \Theta(s) &=& \tau(s) - J^{\tiny T} \kern-1px F(s) - B_{\kern-2px\tiny R} \kern1px s \kern1px \Theta(s) \\[-5px]&\kern3px\downarrow&\\[-5px]    \left(I_{\kern-2px\tiny R} \kern1px s + B_{\kern-2px\tiny R} \kern1px \right) s \kern1px \Theta(s)  &=& \tau(s) - J^{\tiny T} \kern-1px F(s)   \\[-5px]&\kern3px\downarrow&\\[-5px]     s \cdot \Theta(s)  &=& \left(I_{\kern-2px\tiny R} \kern1px s + B_{\kern-2px\tiny R} \kern1px \right)^{-1} \left[ \tau(s) - J^{\tiny T} \kern-1px F(s) \right] \end{array}$$Dove, possiamo definire l'**impedenza dei joint*** come:$$\left(I_{\kern-2px\tiny R} \kern1px s + B_{\kern-2px\tiny R} \kern1px \right) := Z_j$$Dunque il sistema dinamico diventa:<br>![[Pasted image 20240905123302 - Copy.png]]
Se si assume $k_h$ molto alto, allora: $k_h(t) = k_p (t)$ e $\dot x_h(t) = \dot x_p(t) = \dot x_0(t)$ 
In quanto più rigido:$$\begin{array}{l} &\begin{array}{l}   F_h(s) &=&   k_h\left[X_h(s) - X_p(s)\right]   \\[-5px]&\kern3px\downarrow&\\[-5px] &=&    Z(s) \cdot s \cdot X_0(s)  \\[-5px]&\kern3px\downarrow&\\[-5px] &=&    Z(s) \cdot s \cdot X_h(s) \end{array} \\[7px] \Rightarrow & F_h(s) \kern13px = \kern12px Z_{\kern-1px \tiny E}(s) \cdot s \cdot X_h(s) \kern30px  \text{(dinamica dell'ambiente virtuale )} \end{array}$$In realtà la forza percepita è:$$F(s) = Z_{\tiny \text{MF}}(s) \cdot s \cdot x_h(s)$$Si riprende lo studio dell'effetto complessivo:<br>![[Pasted image 20240905123548.png]]
Per ottenere $F_{h}$ $\left(= Z_{\kern-1px \tiny E}(s) \cdot s \cdot X_h(s)\right)$ si deve quindi portare$$-J^{\tiny T} \kern1px Z_{\tiny \text{J}} \kern2px J^{-1}=0$$E ciò è possobile riducendo l'ineriza, quindi il peso del braccio e l'attrito dei **joints**.
