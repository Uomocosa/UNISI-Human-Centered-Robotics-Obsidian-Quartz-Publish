---
aliases:
  - basi del movimento
---
Il movimento è lo spostamento di un insieme di punti, di materia, secondo un qualche sistema di riferimento di 3 assi.
I movimenti possibili sono:
- **La traslazione**.
- **La rotazione**.

==Il problema che affrontiamo è quello di conoscere la posizione e l'orientamento degli oggetti, **in riferimento ad un [[HCR - Cambio del Sistema di Riferimento|sistema di riferimento]] esterno**==:<br>![[Pasted image 20240828191241.png]]

Se due vettori sono nello stesso sistema di riferimento si possono sommare tramite la [[HCR - Regola del Parallelogramma|regola del parallelogramma]] per stabilire il vettore risultante.
Per [[HCR - Cambio del Sistema di Riferimento|trasporre il vettore in un altro sistema di riferimento]] si opera la somma tra il vettore, che dal secondo punta al corrente sistema nell'origine, e viene rapprensetato poi secondo il nuovo sistema.
Vediamo degli esempi per capire meglio:<br>![[Pasted image 20240828191527.png]]<br>![[Pasted image 20240828191541.png]]

Secondo [[HCR - Metodo di Eulero|Eulero]] le 3 componenti del vettore possono essere espresse come:$$\begin{array}{l}       a \times x_1 = |a| \cdot |x_1| \cdot \cos \alpha \\ a \times y_1 = |a| \cdot |y_1| \cdot \sin \alpha \end{array}$$Dove:
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

==**⇒ Se: $\left(\det(R)\right)^2 = \det(I)$, allora: $\det(R) = \det(R^{\tiny T}) = 1$**==.

Le operazioni di roto-traslazione sono la combinazione di una traslazione e di una rotazione, vediamo un esempio:<br>![[Pasted image 20240831182042.png]]

Esiste per queste operazioni una tecnica più diretta, ovvero la [[HCR - Trasformazione Omogenea|funzione di trasformazione omogenea]].

Per applicarla è necessario avere i [[HCR - Vettori Omogenei|vettori omogenei]], i quali hanno un elemento aggiuntivo pari ad $1$ come ultimo elemento rispetto al vettore originale:<br>![[Pasted image 20240831182213.png]]

Esiste anche un'altra forma della [[HCR - Matrice di Rotazione|matrice di rotazione]], la quale ha come riferimento l'angolo tra l'asse delle ascisse di un sistema di riferimento e quello dell'altro sistema:<br>![[Pasted image 20240831182311.png]]
