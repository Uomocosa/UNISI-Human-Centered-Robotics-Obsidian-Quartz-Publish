# Human Centered Robotics
- Corso del 1° Anno di Magistrale (1° Semestre). 
- Docente: **Domenico Prattichizzo**. 
- [Link to Drive with Video Lectures](https://drive.google.com/drive/u/1/folders/1pAW73AgqAlQBOK8exP3sQbLQG0yAlR8j) 
- [[HCR - Handwritten Notes (Not Mine)|Handwritten Notes]] 
- [[HCR - Index for the 2020 Online Lectures|Old index]] (*not so good notes not so bad notes, they need to be revised, but at least they are written in english, a not-so-grammatically-correct english*)
----
## Introduzione Generale al Corso
(*ChatGPT 4o*)
1. **Basi del Movimento e Sistemi di Riferimento**: Qui si affronta il problema di descrivere la posizione e l'orientamento degli oggetti in uno spazio tridimensionale, utilizzando vettori e matrici di trasformazione per passare da un sistema di riferimento a un altro.<br>La traslazione e la rotazione sono le operazioni principali, e si fa uso delle matrici di rotazione (come la matrice di rotazione $Rz$) per descrivere il cambiamento di coordinate tra sistemi diversi.
2. **Cinematica Diretta dei Manipolatori Robotici**: Viene descritta la struttura di un manipolatore robotico, costituito da "link" (rigidi) e "joint" (prismatici o revoluti).<br>La cinematica diretta permette di calcolare la posizione dell'end-effector del robot dati gli angoli di giunzione, mentre la cinematica inversa serve per calcolare i comandi necessari per raggiungere una certa posizione (anche se questa è considerata più complessa).
3. **Grasping**: Questo concetto riguarda l'atto di afferrare e manipolare oggetti tramite un robot.<br>Si distingue tra due tipi di grasping:
	- **Grasping di potenza**: mira a mantenere stabile un oggetto.
	- **Grasping di precisione**: permette movimenti più raffinati tra l'oggetto e il palmo del robot.
	- L'applicazione delle forze durante il grasping viene descritta matematicamente, ad esempio con l'uso della matrice Jacobiana, che lega le forze applicate all'oggetto ai momenti torcenti nei giunti del robot.
4. **Aptica e Rilevamento delle Collisioni**: L'aptica è una tecnologia che permette ai robot di "sentire" e interagire tramite il tatto.<br>Si utilizzano algoritmi per il rilevamento delle collisioni e per restituire un feedback tattile all'utente, spesso con la creazione di una bounding box intorno a oggetti virtuali per rilevare il contatto.<br>La parte del rendering aptico riguarda la risposta in termini di forza che un robot dà quando tocca un oggetto.
5. **Trasparenza**: La trasparenza è un concetto che indica la capacità di un sistema robotico di simulare in modo realistico la dinamica di un oggetto, minimizzando l'effetto delle dinamiche del robot stesso.<br>Si cerca di rendere la dinamica dell'ambiente virtuale percepibile, riducendo l'inerzia e l'attrito del braccio robotico, per garantire che l'interfaccia sembri il più naturale possibile.
----
## Concepts
- ***[[HCR - Basi del Movimento (Lecture)|Basi del Movimento]]***:
	- [[HCR - Regola del Parallelogramma]]
	- [[HCR - Cambio del Sistema di Riferimento]]
	- [[HCR - Catena Cinemantica]]
	- [[HCR - Metodo di Eulero]]
	- [[HCR - Trasformazione Omogenea]]
	- [[HCR - Vettori Omogenei]]
	- [[HCR - Matrice di Rotazione]]
- ***[[HCR - Cinematica Diretta di un Manipolatore Robotico (Lecture)|Cinematica Diretta di un Manipolatore Robotico]]***:
	- [[HCR - Gradi di Libertà]]
	- [[HCR - Catena Cinemantica]]
	- [[HCR - Cinematica Diretta]]
	- [[HCR - Convezione di Denavit-Hartenberg]]
- ***[[HCR - Grasping (Lecture)|Grasping]]***:
	- [[HCR - Matrice Jacobiana]]
	- [[HCR - Screw Matrix]]
	- [[HCR - Regola della Mano destra]]
	- [[HCR - Catena Cinemantica]]
	- [[HCR - Calcolo della Matrice Jacobiana 'della Mano']]
	- [[HCR - Calcolo della Potenza di Contatto]]
	- [[HCR - Kernel • Nullspace]]
- ***[[HCR - Grasp Matrix (Lecture)|Grasp Matrix]]***:
	- [[HCR - Grasp Matrix • Matrice di Grasp]]
	- [[HCR - Baricentro]]
	- [[HCR - Momento Torcente]]
	- [[HCR - Kernel • Nullspace]]
	- [[HCR - Attrito Statico]]
	- [[HCR - Cono d'Attrito]]
	- [[HCR - Direzione Normale]]
	- [[HCR - Coefficiente d'Attrito]]
	- [[HCR - Enveloping Grasping]]
	- [[HCR - Kernel • Nullspace]]
	- [[HCR - Rango Massimo]]
- ***[[HCR - Haptics (Lecture)|Haptics]]***:
	- [[HCR - Simulation Engine]]. #IMPORTANTE 
	- [[HCR - Processo Aptico]]:
		1. ***[[HCR - Psychophysical Measurement Methods|Misura del Movimento]]***.
		2. ***[[HCR - Collision Detection (Lecture)|Rilevamento delle Collisioni]]***. #IMPORTANTE 
		3. ***[[HCR - Rendering Aptico (Lecture)|Rendering Aptico]]***. #IMPORTANTE 
- ***[[HCR - Force Feedback (Lecture)|Force Feedback]]***.
- ***[[HCR - Oggetti Dinamici (Lecture)|Oggetti Dinamici]]***.
- ***[[HCR - Transparency (Lecture)|Transparency]]***.
----
## Exercises:
- [[HCR ~ Exam 2022-01-26]] #TODO 
- [[HCR ~ Exam 2017-04-04 (with Solutions)]] #TODO 
- [[HCR ~ Exam 2017-02-27 (with Solutions)]] #TODO 
- [[HCR ~ Exam 2017-01-25 (with Solutions)]] #TODO 
	- [[HCR ~ Loop Aptico con Retroazione]] 
	- [[HCR ~ Trovare la Grasp Matrix senza Calcoli]]
- ***Original Files***:![[Human Centered Robotics-20240827T093604Z-001 1.zip]]

----
###### All My Notes
For the best experience in reading these and all other notes, and also if you wish to EDIT them, do as follows: 
1. Install [Obsidian](https://obsidian.md), or another markdown editor.
2. Go to the Github link of this or another note
3. Download all the repo or if you know git just the 'content/' folder
4. Extract just the 'content/' folder from the repo zip file
5. Open Obsidian >> Menage Vaults >> Open Folder as Vault >> and select the 'content/' folder you just extracted

==PLEASE NOTE==:
- These notes were not revised by the professors, so take all of them with a grain of salt.
- However if you download them since they are made in markdown you can EDIT them, please do so.
- If you edit and "upgrade" them, please pass the new ones to the other students and professors.

Here are all the links to my notes:
- ***Github***: [UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Sensors-and-Microsystems-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Complex-Dynamic-Systems-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Discrete-Event-Systems-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-System-Identification-and-Data-Analysis-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Multivariable-NonLinear-and-Robust-Control-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Artificial-Intelligence-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Human-Centered-Robotics-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Machine-Learning-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Machine-Learning-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Machine-Learning-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Machine-Learning-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Bioinformatics-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Bioinformatics-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Bioinformatics-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Bioinformatics-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Network-Optimization-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Network-Optimization-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Network-Optimization-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Network-Optimization-Obsidian-Quartz-Publish).
- ***Github***: [UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish](https://github.com/Uomocosa/UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish);<br>***Quartz Publish***: [UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish](https://uomocosa.github.io/UNISI-Mathematical-Methods-for-Engineering-Obsidian-Quartz-Publish).
