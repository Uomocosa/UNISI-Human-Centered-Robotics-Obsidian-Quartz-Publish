---
aliases:
  - direzione normale
  - vettore normale
  - normale
---
- ***Direzione Normale o Vettore Normale, definizione, spiegazione ed esempi***:<br>(*ChatGPT 4o*)
	- ***Definizione***:<br>Il **vettore normale** (o **direzione normale**) è un vettore perpendicolare a una superficie in un dato punto.<br>Questo vettore è fondamentale in molti campi della matematica, fisica e ingegneria, come la meccanica, la robotica, la computer grafica, e viene spesso utilizzato per descrivere la direzione di una forza o di una interazione che agisce su una superficie.
	- ***Spiegazione***:<br>Per capire cosa sia un vettore normale, immagina di avere una superficie piana o curva in uno spazio tridimensionale:
		- In ogni punto di questa superficie, è possibile definire una tangente, che rappresenta la direzione in cui ci si può muovere "senza lasciare" la superficie.
		- Il **vettore normale** è invece un vettore perpendicolare a questa tangente, e quindi perpendicolare alla superficie nel punto in questione.
		- In altre parole, il vettore normale è il vettore che "punta fuori" dalla superficie in una direzione ortogonale (90° rispetto alla tangente alla superficie).
		- ***Formula***:
		- Matematicamente, il vettore normale $\mathbf{n}$ a una superficie $S$ è definito come:
			- Se la superficie $S$ è descritta da una funzione $f(x, y, z) = 0$, allora il vettore normale può essere trovato calcolando il **gradiente** della funzione:$$\mathbf{n} = \nabla f(x, y, z)$$dove $\nabla f$ rappresenta il vettore gradiente di $f$, che contiene le derivate parziali di $f$ rispetto a $x$, $y$ e $z$.
		- ***Superficie piana***:
		- Per una superficie piana, il vettore normale è costante in ogni punto.<br>Se ad esempio abbiamo un piano dato dalla seguente equazione cartesiana:$$ax + by + cz = d$$Il vettore normale a questo piano sarà $\mathbf{n} = (a, b, c)$.
		- ***Superficie curva***:<br>Nel caso di una superficie curva, il vettore normale varia da punto a punto.<br>Per esempio, la normale a una sfera in un punto qualsiasi è il vettore che punta radialmente verso l'esterno della sfera, perpendicolare alla superficie della sfera in quel punto.
	- ***Esempi***:
		1. **Superficie piana**: 
		   - Considera un piano nello spazio tridimensionale con equazione $2x + 3y + z = 5$.<br>Il vettore normale a questo piano sarà $\mathbf{n} = (2, 3, 1)$.<br>Questo vettore è perpendicolare in ogni punto alla superficie del piano.
		2. **Sfera**: 
		   - Consideriamo una sfera centrata nell'origine e con raggio $r$, la cui equazione è $x^2 + y^2 + z^2 = r^2$.<br>In ogni punto della superficie della sfera, il vettore normale è dato dalla direzione del raggio che parte dal centro della sfera e passa attraverso quel punto.<br>Se $P = (x_1, y_1, z_1)$ è un punto sulla superficie, il vettore normale in $P$ sarà $\mathbf{n} = (x_1, y_1, z_1)$, poiché questo vettore è perpendicolare alla superficie della sfera in $P$.
		3. **Grasping robotico**:
		   - Nel contesto della robotica, quando un robot afferra un oggetto, le forze applicate dalle dita del robot sono spesso scomposte in una componente **normale** e una componente **tangenziale**.<br>La componente normale è la forza applicata perpendicolarmente alla superficie dell'oggetto afferrato, mentre la componente tangenziale è parallela alla superficie.<br>In questo contesto, il vettore normale rappresenta la direzione in cui la forza è applicata per evitare che l'oggetto scivoli via (spesso legato al concetto di cono d'attrito).
	- ***Importanza in robotica e meccanica***:<br>Il vettore normale è fondamentale in vari contesti:
		- **Robotica**: Nel contatto tra un robot e un oggetto, la forza applicata deve essere scomposta in componente normale e tangenziale per gestire la presa.
		- **Fisica**: Per calcolare forze come la pressione o l'attrito, la direzione normale è spesso essenziale per capire come agiscono queste forze.
		- **Grafica 3D**: Nei rendering 3D, il vettore normale è utilizzato per calcolare come la luce colpisce una superficie e come questa dovrebbe apparire all'osservatore (shading).
		- Il vettore normale è quindi un concetto chiave in molte discipline per descrivere la relazione tra una superficie e le forze che agiscono su di essa.
----
