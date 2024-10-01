#TODO Exercise 1, exercise 3b
- ***Exercise 1: Linear Algebra***^exercise-1
	- Find the solution(s) of this linear system:$$\left\{\begin{array}{l} Az = y_1 \\ Ax = y_2 \end{array}\right. $$Where:$$A = \left[\begin{array}{l} 1 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 \end{array}\right] \kern5px, \kern15px y_1= \left[\begin{array}{c} 3 \\ 3 \\ 0 \\ 3 \end{array}\right] \kern5px, \kern15px y_1= \left[\begin{array}{c} 4 \\ -2 \\ 0 \\ 3 \end{array}\right] $$**Tip**: Solve the problem using the concept of [[HCR - Rango Massimo|RANK of matrices]] and discuss how many solutions the system has. 
- ***Exercise 2: Grasping*** 
	- ***(a)*** Discuss how to equilibrate external wrenches $\omega$ appliet on the object with a grasp having matrix $G$. How do you choose contact forces in $\omega = -G \lambda$. ^exercise-2a
	- ***(b)*** Is it possible to equilibrate any external wrench with a single hard-finger contact? With two hard-finger contacts? With three hard-finger contacts placed wherever you want? ^exercise-2b
- ***Exercise 3: Haptics*** 
	- ***(a)*** Why is it important transparency in haptics? ^exercise-3a
	- ***(b)*** Compute the equation of impedance. How do you improve transparency? ^exercise-3b
----
- ***Solutions***:
	- (*[[#^exercise-1|Exercise 1: Linear Algebra]]*) #TODO 
	- (*[[#^exercise-2a|Exercise 2: Grasping - a.]]*)<br>To equilibrate external wrenches it is necessary to exercitate forces with surface tangent components that nullify the external force (in this case the gravity force) and perpendicular components this keeps contact forces in the friction cone.<br>![[Pasted image 20240915185623.png]]<br>Without a proper value for normal components the object could slip from the grasp.<br>In mathematic terms:$$\Gamma = G^{\#}(-\omega) + N(G)\cdot \xi $$Where:
		- $G^{\#}(-\omega)$ are tangent components.
		- $N(G)\cdot \xi$ are normal components.
	- (*[[#^exercise-2b|Exercise 2: Grasping - b.]]*)<br>In general it is only possible to equilibrate any external wrench only if:<br>***1.*** If we have $N(G) \neq 0$, otherwise the system would have only a solution and would not have been normal components.<br>Hence this means it is required $N(G) \neq 0$ to have a grip on the object.<br>***2.*** $G$ must be full rank because is necessary to control all the components of the external wrench.<br>According to these two conditions:<br>• With 1 contact point is impossible beacuse $G$ is a $6\times 3$ matrix and it can't satisfy both conditions.<br>• With 2 contact points is still impossible, because $G$ is a $6 \times 6$ matrix, hence if it has $N(G) \neq 0$, some columns are linearly dependent, so $G$ will not be full rank.<br>  Ohterwise if $G$ is full rank, all columns are linear independent, so $N(G) = 0$.<br>• With 3 contact points it's possible since $G$ is a $6 \times 9$ and with proper placement of these points it is possible to satisfy both conditions.  <br>⇒ In general it is possible to equilibrate my external wrench only if it is possible to squeeze the object, meaning:<br>• With a single finger it is impossible. <br>• With two fingers it could be possible, it depends on the placement of the fingers, they must be able to squeeze the object. <br>• With three fingers it is even more likely that the previous case, since there are even more ways to squeeze the object.
	- ***Extra***:
		- With a single finger, $N(G) = 0$, in fact:$$\left[\begin{array}{c} I_{\tiny 3x3} \\ \begin{array}{c} 0 & -dz & dy \\ dz & 0 & -dx \\ -dy & dx & 0  \end{array}  \end{array}\right]_{\kern-3px \tiny 6x6}$$Because of $I$ every column is linear independent ⇒ **only a solution**.<br>So it is possible to equilibrate only in one case of wrench.<br>(*Imagine this situation, now the finger is acting against the gravity force but the object will fall down for any change of the wrench*).<br>![[Pasted image 20240915185551.png]]
		- With two fingers not every position is good, even if contact points position is manteined:<br>![[Pasted image 20240915185536.png]]<br>In both cases the grasp matric is the same, but what change are the forces applied:
			- In the first case it is possible to manage both tangent and normal component.
			- In the second case the normal component can't be controlled through $\tau$ (torque of the joints).<br>So this means that the object will slip if the external force is high enough to carry the contact forces vector out of the friction cone.
			- With three fingers, the positioning is still important for the same reason but in this case $G$ is a $6 \times 9$ matrix and with proper positioning of the fingers it can be full rank.<br>It is also more likely that we'll have $N(G) \neq 0$ since there are more columns than rows.
	- (*[[#^exercise-3a|Exercise 3: Haptics - a.]]*)<br>Il concetto di trasparenza sta alla base della costruzione delle interfacce aptiche per la simulazione virtuale.<br>Questa consiste nel cercare di minimizzare quanto il più possibile (teoricamente si vorrebbe nulla) l'impedenza dell'interfaccia aptica $(Z_H)$, data dalla presenza di resistenze all'interno degli attuatori, per esempio, o di elementi resistivi dell'interfaccia.<br>Idelamente si vuole muovere liberamente in un ambiente virtuale, in mancanza di collisioni, senza il minimo sforzo, come accade nella realtà, ma questo non è possibile, propio per la presenza di questa impedenza $Z_H$ dovuta all'interfaccia che sto usando.<br>Infatti i costruttori cercano di realizzare un buon disegno meccanico per ridurre $Z_H \to 0$, per riuscirci si inserisce una retroazione sul rendering aptico che comnque non la riduce a $0$, ma grazie a questa retroazione si ottiene comunque un risultato accettabile. 
	- (*[[#^exercise-3b|Exercise 3: Haptics - b.]]*) #TODO 

----
###### Original Files
- ***Exam***:<br>![[Exam_04_04_17.jpeg]]

- ***Solution***:<br>![[IMG_20200108_214908.jpg]]<br>![[IMG_20200108_214933.jpg]]<br>![[IMG_20200108_214946.jpg]]<br>![[WhatsApp Image 2017-11-21 at 12.38.51 (2).jpeg]]<br>![[WhatsApp Image 2017-11-21 at 12.38.52 (1) 1.jpeg]]<br>![[WhatsApp Image 2017-11-21 at 12.38.53.jpeg]]<br>![[WhatsApp Image 2017-11-21 at 12.38.55.jpeg]]

----
###### Old File
![[HCR ~ exam 2017_04_04_220307_151802.jpg]]