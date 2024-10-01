---
aliases:
  - algoritmo di possibilità virtuale
  - possibilità virtuale
---

***Ricorda***:

>

>

----
###### Algoritmo di Possibilità Virtuale
Si consideri ora un oggetto fino (sottile): se $x_h$ è troppo in profondità l'algoritmo di [[HCR - Collision Detection (Lecture)|collision detection]] riconoscerebbe dove più vicina la superficie inferiore e si avrebbe una forza diretta nel senso opposto:<br>![[Pasted image 20240904193732.png]]
Perciò va tenuta in memoria dello stato passato.
Per risolvere il problema, invece di prendere $x_p$ sulla superficie, si considera come centro di una sfera di raggio trascurabile, si traccia il segmento:$$\overline{x_h(k+1)\kern7px x_h(k)}$$Ed il piano intersecato è quello su cui unicamente va svolto l'algoritmo di collision detection:<br>![[Pasted image 20240904194056.png]]
Questa tecnica è detta **algoritmo di possibilità virtuale**.
