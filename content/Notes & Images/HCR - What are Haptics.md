# Haptics
La tecnologia aptica è l'ultima frontiera della robotica del grasping e concerne la restituzione all'utente o l'adattamento della presa in funzione delle forze percepite, in altre parole "haptic" significa interazione tattile.

I componenti necessari per tale interazione sono:
1. **Misura** del movimento di una certa parte del corpo tramite una tecnologia appropriata.
2. **Rilevamento delle Collisioni** tramite l'elaborazione della misura, rispetto ad una rappresentazione (virtuale) dell'oggetto.
3. **Rendering aptico** tramite un attuatore per permettere l'*acknowledgment* e l'effettività dell'azione svolta, restituendo una sensazione reale o stimolata o un display aptico.

In termini matematici si traduce in:
$$
\text{Input} \kern 10px
\rightarrow \kern 10px
k \cdot \Delta x \kern 10px
\rightarrow \kern 10px
F \kern 10px
\rightarrow \kern 10px
\tau \kern 10px
\rightarrow \kern 10px
\text{Output}
$$
Dove:
-> $\Delta x$ è relativo ad una superficie

In generale la quantità di energia scambiata nell'interazione aptica è molto più alta rispetto agli altri tipi di interazione per questo **non** è un sistema efficace per comunicare.
Il tocco è essenzialmente uno scambio di froze e per questo la robotica è il campo giusto da cui sviluppare interfacce aptiche.

Il processo può essere così schematizzato:
![[SmartSelect_20220310-093503_Samsung Notes.jpg]]
Dove:
-> Il *simulation engine* è il module che si occupa dello svolgimento di calcoli, al fine di rivelare la collisione (*collision detection*), e dunque restituire il *force response* (attraverso l'*end effector*, manovrato da un *control algorithm*), e di mostrare a *video* l'ambiente virtuale (attraverso un *graphic engine*).