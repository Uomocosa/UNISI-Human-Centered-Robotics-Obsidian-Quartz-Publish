---
aliases:
  - metodo di Lagrange
  - Lagrangiana
---
- ***Metodo di Lagrange, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- Il **metodo dei moltiplicatori di Lagrange** è una tecnica per risolvere problemi di **ottimizzazione vincolata**.<br>Questo metodo permette di trovare i punti di massimo o minimo di una funzione obiettivo, soggetta a uno o più vincoli.
	- ***Definizione del metodo di Lagrange***:<br>Il problema generale che si risolve con il metodo dei moltiplicatori di Lagrange è:
		- **Funzione obiettivo**: vuoi minimizzare (o massimizzare) una funzione $f(x)$.
		- **Vincolo**: devi rispettare una condizione espressa da $g(x) = 0$.
		- Per trovare il minimo (o massimo) della funzione $f(x)$ sotto il vincolo $g(x) = 0$, si introduce una nuova variabile $\lambda$, chiamata **moltiplicatore di Lagrange**, e si costruisce la **funzione lagrangiana**:$$\mathcal{L}(x, \lambda) = f(x) + \lambda \cdot g(x)$$L'idea è che, invece di risolvere il problema originale direttamente, risolvi il problema non vincolato derivato dalla funzione lagrangiana, imponendo che le derivate parziali rispetto a $x$ e $\lambda$ siano uguali a zero.
	- ***Passi generali del metodo***:
		1. Scrivi la funzione lagrangiana $\mathcal{L}(x, \lambda) = f(x) + \lambda \cdot g(x)$.
		2. Trova le derivate parziali di $\mathcal{L}(x, \lambda)$ rispetto a $x$ e $\lambda$.
		3. Risolvi il sistema di equazioni derivato impostando tutte le derivate uguali a zero.
----



- ***Come abbiamo visto nella lezione per l'algoritmo del [[HCR - Collision Detection (Lecture)|Collision Detection]], ecco la spiegazione delle formule usate***<br>(*ChatGPT 4o*)
	- ***Applicazione alla tua formula***:<br>Vediamo come viene applicato il metodo di Lagrange nel problema che stai studiando.
		- ***Passo 1: Formulazione del problema***:<br>Vuoi minimizzare la distanza tra due punti $x_p$ e $x_h$.<br>La funzione da minimizzare è la **distanza euclidea** tra questi due punti:$$f(x_p) = \sqrt{(x_p - x_h)^{T} \cdot (x_p - x_h)}$$
			- Solitamente, per comodità si lavora con il quadrato della distanza, per evitare la radice quadrata:$$f(x_p) = \frac{1}{2} (x_p - x_h)^{T} \cdot (x_p - x_h)$$
		- ***Passo 2: Vincolo del piano***:<br>Hai il vincolo che $x_p$ deve trovarsi su un piano, il cui vincolo è dato dall'equazione:$$g(x_p) = (a \ b \ c) \cdot x_p - d = 0$$
		- ***Passo 3: Costruzione della funzione lagrangiana***:<br>Introduci un moltiplicatore di Lagrange $\lambda$ per il vincolo, e costruisci la **funzione lagrangiana**:$$\mathcal{L}(x_p, \lambda) = \frac{1}{2} (x_p - x_h)^{T} \cdot (x_p - x_h) + \lambda \left[ (a \ b \ c) \cdot x_p - d \right]$$
		- ***Passo 4: Risoluzione***:<br>Per trovare il minimo, prendi le derivate parziali della funzione lagrangiana rispetto a $x_p$ e $\lambda$, e poni queste derivate uguali a zero:
			1. Derivata rispetto a $x_p$:$$\frac{\partial \mathcal{L}}{\partial x_p} = (x_p - x_h) + \lambda (a \ b \ c) = 0$$Da cui puoi risolvere per $x_p$:$$x_p = x_h - \lambda (a \ b \ c)$$
			2. Derivata rispetto a $\lambda$ (il vincolo):$$\frac{\partial \mathcal{L}}{\partial \lambda} = (a \ b \ c) \cdot x_p - d = 0$$Sostituendo $x_p = x_h - \lambda (a \ b \ c)$ nell'equazione del vincolo, puoi trovare il valore di $\lambda$ che soddisfa il vincolo.<br>Una volta trovato $\lambda$, lo sostituisci nella prima equazione per ottenere $x_p$, il punto minimo che soddisfa il vincolo.
		- ***Esempio pratico***:<br>Immagina di voler trovare il punto più vicino a una superficie piana (un triangolo) da un punto $x_h$ nello spazio tridimensionale.<br>Usi la distanza euclidea come funzione obiettivo, e applichi il vincolo che il punto cercato $x_p$ si trovi sul piano.
			- Seguendo i passi descritti sopra:
			1. Minimizza la distanza.
			2. Rispetta il vincolo che il punto si trovi sul piano.
			3. Usa il moltiplicatore di Lagrange per combinare il problema di minimizzazione con il vincolo del piano.
			- Il risultato ti darà il punto $x_p$ sul piano che è il più vicino a $x_h$.
----
