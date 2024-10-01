---
aliases:
  - minimizzazione di una distanza
  - problema di minimizzazione sulla distanza
---
***Ricorda***:

> 

> 

----
###### Calcoli per la Minimizzazione di una Distanza
Se $x_h$ si trova all'interno della superficie si può rispondere con una forza normale alla superficie:<br>![[Pasted image 20240904191833.png]]
È necessario ininnazitutto trovare $x_p$ il punto a distanza minore a $x_h$ sulla superficie in quanto:$$F=k(x_h-x_p)$$Trovare $x_p$ è un **problema di minimizzazione sulla distanza**, dunque:$$d = \sqrt{(x_p -x_h)^{\tiny T} \cdot(x_p-x_h)}$$Facendo i seguenti passaggi:
$$\begin{array}{l} 1. \kern15px \min_{\left({x_p}\right)} d = \min_{\left({x_p}\right)} {1\over 2} \kern2px d^2 \\[3px] 2. \kern15px \min_{\left({x_p}\right)} \sqrt{(x_p -x_h)^{\tiny T} \cdot(x_p-x_h)} \\[5px] 3. \kern15px \left(\text{Apllicando il metodo di Lagrange}\right) \\ \to \kern10px \min_{\left({x_p \kern1px ,\ \lambda}\right)} {1 \over 2} \left(x_p -x_h \right)^{\tiny T}\cdot\left(x_p -x_h \right) + \lambda \left[\left(a \ b \ c \right)\kern2px x_p - d \right] \end{array}$$
Dove: 
- $\lambda$ è uno scalare.
- Il "*metodo di Lagrange*" viene anche chiamato "*[[HCR - Metodo di Lagrange|Lagrangiana]]*".
- $x_p$ appartiene al piano/triangolo, quindi possiamo scrivere: come "**condizione**" della lagrangiana: $$g(x) = (a \ b \ c) \kern2px x_p - d = 0$$Che sta a significare appunto che $x_p$ fa parte del piano/triangolo.
- Ricorda che $d$ è una variabile, dipendente da $x_p$, la nostra incognita, ed $x_h$ [[HCR - Collision Detection (Lecture)|vettore avatar]] che conosciamo/abbiamo stimato.
- Ricorda inoltre che il versore normale $\hat n$ del piano/triangolo è definito come:$$\hat n = {1 \over a^2 + b^2 + c^2} \kern2px (a \ b \ c)$$

Definiamo:$$ Q(x_p \kern2px,\ \lambda) = {1 \over 2} \left(x_p -x_h \right)^{\tiny T}\cdot\left(x_p -x_h \right) + \lambda \left[\left(a \ b \ c \right)\kern2px x_p - d \right]$$Troveremo l'ottimo risolvendo il seguente sistema:$$\left\{\begin{array}{l} {\partial Q \over \partial x_p} = \left(x_p -x_h \right) - \lambda \left(a \ b \ c \right)^{\tiny T}  = 0  \\ {\partial Q \over \partial \lambda} =  \left(a \ b \ c \right) \kern2px x_p - d  = 0 \end{array}\right.$$Che possiamo riscrivere come:$$\left\{\begin{array}{l}x_p -  \left(a \ b \ c \right)^{\tiny T} \lambda  = x_h   \\ \left(a \ b \ c \right) \kern2px x_p  + 0 \cdot \lambda  = d \end{array}\right.$$In fine lo possiamo riscrivere in forma di matrice:$$\left[\begin{array}{c} I_{\tiny 3 \times 3} &  \begin{array}{l} a \\ b \\ c  \end{array} \\ \begin{array}{l} a & b & c  \end{array} & 0  \end{array} \right] \left[\begin{array}{c} x_p \\ \lambda \end{array} \right] = \left[\begin{array}{c} x_h \\ d \end{array} \right]$$Ricorda che:
- $d$ è una variabile e si esprime in funzione di $x_p$.


Per quanto riguarda $k$, deve essere alto in modo che la forza sia sufficiente, ma non abbastanza da permettere deformazioni eccessive.
Bisogna però distinguere tra il $k$ del materiale reale e quello assunto dalla simulazione il quale sarà sempre minore per le limitazioni nella rappresentazione.
$k$ deve essere sufficente alto da evitare l'incrocio in quanto si hanno più punti di contatto.
Si usa un ulteriore $k$ diverso se la superficie è deformabile, e se viene deformata.


***N.B.:*** Abbiamo chiamato $k$ in modo generale (coefficiente d'attrito generico), ma nelle prossime formule, andremo a definire:<br> #NOT_SURE_ABOUT_THIS `Non sono sicuro che quello che dico qui sia effettivamente la definizione di` $k_0$ `e` $k_h$
- $k_0$ : coefficiente d'attrito reale (stimato) tra l'end-effector e la superficie da toccare/prendere.
- $k_h$ : **coefficiente aptico**, deciso arbitrariamente, il $k$ di cui si parla poco sopra è probabilmente questo $k_h$.

----