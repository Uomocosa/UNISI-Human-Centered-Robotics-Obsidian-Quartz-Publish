---
aliases:
  - cinematica diretta di un manipolatore robotico
  - direct kinematics of a robotic manipulator
  - Jacobiana analitica
---
***Ricorda***:

> Formule importanti da ricordare$$\begin{array}{l} 1.& \dot \theta = J \cdot V_e \\[4px]  2.& \tau^{\tiny T} \cdot \dot \theta = F_e^{\tiny T} \cdot V_e \\[7px] 3.& \tau  = J^{\tiny T} F_e \end{array}$$Dove:
> - $\dot \theta$ : **velocità angolare** dei **joints**.
> - $J$ : la [[HCR - Matrice Jacobiana|matrice Jacobiana]].
> - $\tau$ : **momento torcente**. $\left(\vec \tau = \vec b \times \vec F\right)$
> - $\tau \cdot \dot \theta$ : **potenza meccanica** di un giunto.
> - $F_e$ : forza dell'**end effector**.
> - $V_e$ : velocità (lineare) dell'**end effector**.

> Per essere più chiari dato una [[HCR - Catena Cinemantica|catena cinematica]], del tipo:<br>![[Pasted image 20240922004222.png]]
> Definiamo:
> - Il vettore della velocità dell'**end-effector** come:$$V_{e} = \left[\begin{array}{c} \dot F_x \\ \dot F_y \\ \dot F_z\end{array}\right] = J(\alpha ,\ \beta) \left[\begin{array}{c} \dot \alpha \\ \dot \beta \end{array}\right] $$
> - E la Jacobiana come:$$J(\alpha ,\ \beta) = \left[\begin{array}{c} {\large{\partial F_x \over \partial \alpha}} & {\large{\partial F_x \over \partial \beta}} \\ {\large{\partial F_y \over \partial \alpha}} & {\large{\partial F_y \over \partial \beta}} \\ {\large{\partial F_z \over \partial \alpha}} & {\large{\partial F_z \over \partial \beta}} \end{array}\right]$$Dove:
> 	- $F_x ,\ F_y ,\ F_z$ sono funzioni che descrivono la posizione dell'**end-effector** in funzione dei parametri dei vari **joints**, ovvero le loro lunghezze $\left(\rho_1 ,\ \rho_2\right)$ e i loro angoli $\left(\alpha ,\ \beta \right)$, in quanto stiamo trattando di **joint revoluti** la jacobiana sarà sulle derivate degli angoli, di sotto troverete un esempio.

> Sempre guardando il precedente esempio, per cambiare il [[HCR - Cambio del Sistema di Riferimento|sistema di riferimento]], portando l'end-effector in riferimonto all'origine/'*world reference*' prima definiamo come cambiamo il sistema di riferimento, ovvero rotazioni e traslazioni per portare il vettore dell'end-effector da ${}^{2}E \to {}^{0}E$, quindi:$$\begin{array}{l} \begin{array}{l} {}^{0}E &=& {}^{0}O_2 + {}^{0}R_2 \cdot {}^{2}E  \\[-5px]&\kern3px\downarrow&\\[-5px] &=&    {}^{0}O_2 + {}^{0}R_1 \cdot {}^{1}R_2 \cdot {}^{2}E \end{array}\end{array}$$Dopodichè definiamo i vari vettri e matrici:$$\begin{array}{l} {}^{0}O_2 = \left[\begin{array}{c} \rho_1 \cos(\alpha) \\ \rho_1 \sin(\alpha) \\ 0 \end{array}\right] \kern15px,&&{}^{2}E = \left[\begin{array}{c} \rho_2  \\ 0 \\ 0 \end{array}\right]  \\[5px] {}^{1}R_2 = \left[\begin{array}{c} \cos(\beta) & -\sin(\beta) & 0 \\ \sin(\beta) & \cos(\beta) & 0 \\ 0 & 0 & 1 \end{array}\right] \kern15px,&& {}^{0}R_1 = \left[\begin{array}{c} \cos(\alpha) & -\sin(\alpha) & 0 \\ \sin(\alpha) & \cos(\alpha) & 0 \\ 0 & 0 & 1 \end{array}\right] \end{array}  $$Dopo tutti i calcoli otteremo:$${}^{0}E_2 = \left[\begin{array}{c} \rho_1 \cos(\alpha) + \rho_2 \cos(\alpha + \beta)  \\ \rho_1 \sin(\alpha) + \rho_2\sin(\alpha + \beta) \\ 0 \end{array}\right] = \left[\begin{array}{c} F_x (\alpha,\ \beta) \\ F_y (\alpha,\ \beta) \\ F_z (\alpha,\ \beta)  \end{array}\right]$$

> ***NOTE***: #IMPORTANTE #NOT_SURE_ABOUT_THIS `Da rivedere`
> In realà fare così non del tutto corretto, sarebbe necessario prima definire le [[HCR - Homogeneous Transformation Matrix|'homogeneous transformation matrices']] e poi calcolare la posizione dell'end-effector con quelle. 
> Quindi, se volessimo usare le **trasformation matrices**, potremmo definire:$$ {}^{2}E = {}^{1}_{2}T \cdot {}^{0}_{1}T \cdot {}^{0}E$$Dove:$$\begin{array}{l} {}^{0}_{1}T = \left[\begin{array}{c} \cos(\alpha) & -\sin(\alpha) & 0 & \rho_1 \cos(\alpha) \\ \sin(\alpha) & \cos(\alpha) & 0 & \rho_1 \sin(\alpha) \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array}\right] \\[7px] {}^{1}_{2}T = \left[\begin{array}{c} \cos(\beta) & -\sin(\beta) & 0 & \rho_2 \cos(\beta) \\ \sin(\beta) & \cos(\beta) & 0 & \rho_2 \sin(\beta) \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array}\right]  \end{array}$$Infine per trovare ${}^{0}E$ sapendo ${}^{2}E$ calcoliamo:$$ {}^{0}E =  \left({}^{0}_{1}T\right)^{-1}\cdot \left({}^{1}_{2}T\right)^{-1} \cdot {}^{2}E$$Ricorda che c'è [[HCR - Homogeneous Transformation Matrix#^inverse-of-a-transformation-matrix|un modo semplice]] per calcolare l'**inversa** di una **transformation matrix**

----

In generale un manipolatore robotico è un braccio robotico, ed in genere si rappresenta così:<br>![[Pasted image 20240910193537.png]]
Esso è generalmentee composto da **linkers**, i quali sono copri rigidi, e da **joints**, i quali contengono meccanismi che permettono il moviemetno relativo tra i linkers.
Esistono due categorie di joints:
1. **Joints Prismatici**: i quali permettono una **traslazione**.
2. **Joints Revoluti**: i quali permettono una **rotazione**.

Entrambi i tipi di joints conferiscono [[HCR - Gradi di Libertà|1 grado di libertà]] al manipolatore.
L'insieme di linkers a di joints formano una [[HCR - Catena Cinemantica|catena cinemantica]] che in questo caso è **aperta**, mentre, se il manipolatre operasse un oggetto si diretta **connessa**.
![[Pasted image 20240922004222.png]]

L'interesse principale della [[HCR - Cinematica Diretta|cinematica diretta]] è quello di stabilire a priori la posizione dell'**end effector**, data una sequenza di comandi espressi sotto forma di angoli (si considerano solo **joints revoluti**).
Più utile è la [[HCR - Cinenamtica Inversa|cinenamtica inversa]] per cui, a partire dalla posizione che si vuole raggiungere, si determina la sequenza di comandi necessari ma è molto più complessa e non verra trattata.

In generale, secondo tale configurazione, la posizione dell'end effector può essere espressa come:$$\begin{array}{l} \begin{array}{l} {}^{0}E &=& {}^{0}O_2 + {}^{0}R_2 \cdot {}^{2}E  \\[-5px]&\kern3px\downarrow&\\[-5px] &=&    {}^{0}O_2 + {}^{0}R_1 \cdot {}^{1}R_2 \cdot {}^{2}E \end{array}\end{array}$$Dove:$$\begin{array}{l} {}^{0}O_2 = \left[\begin{array}{c} R_1 \cos(\alpha) \\ R_1 \sin(\alpha) \\ 0 \end{array}\right] \kern15px,&&{}^{2}E = \left[\begin{array}{c} \rho_2  \\ 0 \\ 0 \end{array}\right]  \\[5px] {}^{1}R_2 = \left[\begin{array}{c} \cos(\beta) & -\sin(\beta) & 0 \\ \sin(\beta) & \cos(\beta) & 0 \\ 0 & 0 & 1 \end{array}\right] \kern15px,&& {}^{0}R_1 = \left[\begin{array}{c} \cos(\alpha) & -\sin(\alpha) & 0 \\ \sin(\alpha) & \cos(\alpha) & 0 \\ 0 & 0 & 1 \end{array}\right] \end{array}  $$Possiamo poi calcolare ${}^{0}R_2$:$$\begin{array}{l}   {}^{0}R_2 &=&   \left[\begin{array}{c} \cos(\alpha) \cos(\beta) - \sin(\alpha) \sin(\beta) & -\cos(\alpha) \sin(\beta) - \sin(\alpha) \cos(\beta) && 0 \\ \sin(\alpha) \cos(\beta) - \cos(\alpha) \sin(\beta) & -\sin(\alpha) \sin(\beta) - \cos(\alpha) \cos(\beta) && 0 \\ 0 & 0 && 1 \end{array}\right]   \\[-5px]&\kern3px\downarrow&\\[-5px] &=&    \left[\begin{array}{c} \cos(\alpha+\beta) & -\sin(\alpha+\beta)  && 0 \\ \sin(\alpha + \beta) & \cos(\alpha + \beta) && 0 \\ 0 & 0 && 1 \end{array}\right]\end{array}$$Ed infine possiamo scrivere il vettore $E$ rispetto al [[HCR - Cambio del Sistema di Riferimento|sistema di riferimento]] $0$:$$\begin{array}{l}   {}^{0}E &=&   \left[\begin{array}{c} \rho_1 \cos(\alpha) \\ \rho_1 \sin(\alpha) \\ 0\end{array}\right] + {}^{0}R_2  \left[\begin{array}{c} \rho_2 \\ 0 \\ 0\end{array}\right]   \\[-5px]&\kern3px\downarrow&\\[-5px] &=&  \left[\begin{array}{c} \rho_1 \cos(\alpha) + \rho_2 \cos(\alpha + \beta)  \\ \rho_1 \sin(\alpha) + \rho_2\sin(\alpha + \beta) \\ 0 \end{array}\right] \end{array}$$In questo caso si poteva arrivare al risultato anche attraverso la trigonometria, ma nel caso tridimensionale, si può procedere solo in questo modo e si fa uso della [[HCR - Convezione di Denavit-Hartenberg|convenzione delle tavole di Denavit-Hartenberg]] ([Wikipedia: 'Convenzione di Denavit-Hartenberg](https://it.wikipedia.org/wiki/Convenzione_di_Denavit-Hartenberg))

Oltre alla posizione e all'orientamento dell'end effector, spesso si controlla anche la sua velocità, espressa in funzione della velocita dei joints, quindi dato:$${}^{0}E_2 = \left[\begin{array}{c} \rho_1 \cos(\alpha) + \rho_2 \cos(\alpha + \beta)  \\ \rho_1 \sin(\alpha) + \rho_2\sin(\alpha + \beta) \\ 0 \end{array}\right] = \left[\begin{array}{c} F_x (\alpha,\ \beta) \\ F_y (\alpha,\ \beta) \\ F_z (\alpha,\ \beta)  \end{array}\right]$$Possiamo scrivere la velocità come:$$V_{\tiny E} = \left[\begin{array}{c} \dot F_x \\ \dot F_y \\ \dot F_z\end{array}\right] = J(\alpha ,\ \beta) \left[\begin{array}{c} \dot \alpha \\ \dot \beta \end{array}\right] $$Dove:
- $V_{\tiny E}$ è la **velocità lineare**.
- $\dot \alpha ,\ \dot \beta$ sono le **velocià angolari** dei **giunti revoluti**.
- $J(\alpha ,\ \beta)$ è una [[HCR - Matrice Jacobiana|jacobiana analitica]], ovvero:$$J(\alpha ,\ \beta) = \left[\begin{array}{c} {\large{\partial F_x \over \partial \alpha}} & {\large{\partial F_x \over \partial \beta}} \\ {\large{\partial F_y \over \partial \alpha}} & {\large{\partial F_y \over \partial \beta}} \\ {\large{\partial F_z \over \partial \alpha}} & {\large{\partial F_z \over \partial \beta}} \end{array}\right]$$E dove:$$\begin{array}{l}   \dot F_x &=& {\large{d \over dt}} F_x(\alpha ,\ \beta)    \\[-5px]&\kern3px\downarrow&\\[-5px] &=&    {\large{dF_x \over d\alpha}}{\large{d\alpha \over dt}} + {\large{dF_x \over d\beta}}{\large{d\beta \over dt}}   \end{array}$$

A partire da ciò si può stabilire la forza esercitata sull'end effector, conoscendo i **momenti torcenti** dei joints e la loro potenza:<br>![[Pasted image 20240831183535.png]]$$\begin{array}{l}   &\Rightarrow& \tau^{\tiny T} \cdot \dot \theta &=&F_e^{\tiny T} \cdot V_e   \\[-5px]&\kern3px\downarrow&\\[-5px]   &\Rightarrow& \tau^{\tiny T} \cdot \dot \theta&=&F_e^{\tiny T} \cdot J  \cdot \kern2px \dot\theta  \\[-5px]&\kern3px\downarrow&\\[-5px]   &\Rightarrow& \tau &=&J^{\tiny T} F_e   \end{array} $$Dove:
- $\tau \cdot \dot \theta$ : **potenza meccanica** di un giunto, con:
	- $\tau$ : **momento torcente** $\left(\vec \tau = \vec b \times \vec F\right)$.
	- $\dot \theta$ : **velocità angolare**.
- $F_e$ : forza dell'**end effector**.
- $V_e$ : velocità (lineare) dell'**end effector**.
- #NOT_SURE_ABOUT_THIS `Abbiamo introdotto questa formula come se potessimo facilmente stabilire la forza sull'end effector conosendo i momenti torcenti dei joints, ma abbiamo trovato il contrario, ovvero i momenti torcenti data la forza dell'end effector, questa cosa non ha molto senso.`
- #NOT_SURE_ABOUT_THIS `Quindi per trovare la forza dell'end effector, dovremo usare la suguente formula??? Non so se è corretta:` $F_e = \left(J^{\tiny T}\right)^{-1} \cdot \tau$
