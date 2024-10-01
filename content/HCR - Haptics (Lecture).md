---
aliases:
  - haptics
  - interazione tattile
  - misura del movimento
  - processo aptico
---
La tecnologia aptica è l'ultima frontiera della robotica del **grasping** e concerne la restituzione all'utente o l'adattamento della presa in funzione delle forze percepite.
==In altre parole "*haptics*" significa interazione tattile==.


I componenti necessari per tale interazione sono:
1. ***[[HCR - Psychophysical Measurement Methods|Misura del Movimento]]***, specificatamente: misura del movimento di una certa parte del corpo, tramite una tecnologia appropiata.
2. ***[[HCR - Collision Detection (Lecture)|Rilevamento delle Collisioni]]***, tramite un'elaborazione della misura, rispetto ad una rappresentazione dell'oggetto.
3. ***[[HCR - Rendering Aptico (Lecture)|Rendering Aptico]]***, tramite un attuatore per permetter "l'*acknowledgment*" dell'effettività dell'azione svolta, restituendo una sensazione reale o simulata o un display aptico.

==In termini matematici si traduce come==:<br>![[Pasted image 20240904122054.png]]
Dove $\Delta x$ è relativo ad una superficie.$$\text{Input} \to k \cdot \Delta x \to F \to \tau \to \text{Output}$$Ovvero: #NOT_SURE_ABOUT_THIS `Interpretazione mia`
1. **Input**: reading, **misura del movimento** ovvero $\Delta x$)
2. $F = k \cdot \Delta x$ : data una costante trasformiamo la misurazione in una forza)
3. $F \to \tau$ : tramite un algoritmo trasformiamo la forza in momento torcente da restituire come feedback aptico in **Output**.

In generale la quantità di energia scambiata nell'interazione aptica è molto più alta rispetto agli altri tipi di interazione per questo non è un sistema efficiente per comunicare.
Il tocco è essenzialmente uno scambio di forze e per questo la robotica è il campo giusto da cui sviluppare interfaccie aptiche.
==Il processo può essere così schematizzato==:<br>![[Pasted image 20240904122251.png]]
Il [[HCR - Simulation Engine|simulation engine]] è quello che svolge i calcoli, così che si possa rivelare la collisione, restituire un **feedback**, e mostrare a schermo l'ambiente virtuale.
