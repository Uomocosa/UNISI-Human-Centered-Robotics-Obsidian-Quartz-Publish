# Chains of joints that refers to the same end-effector
![[Pasted image 20220404113202.png]]
![[Pasted image 20220404113214.png]]

The selection of the contact velocities depends on the model of the contact that we used.

-> There are 3 main **contact models**:
1. *Hard finger with friction*
2. *Hard finger without friction*
3. *Soft finger*

We will use the 1-st one (*Hard finger with friction*)

-> To understand the difference between the first and the second model let's consider us holding a pen and wanting to write on a piece of paper:
- If the paper is normal (it has friction) I can easily write on it (1-st case)
- If the paper is oily (it has no friction) I cannot write on it, I can only impose a vertical force, I slip away when I apply tangential forces (2-nd case)
- In case of *Soft fingers* we have reduced control on it, instead of having for its wrench 3 forces and 3 moments we only have 3 forces and 1 moment:
$$
W_{\text{soft finger}} = 
\left[
\begin{array}{l}
\left.\overrightarrow{F} \kern 7px \right|_{[3 \times 1]}
\\[5px]
\left.\overrightarrow{M} \kern 7px \right|_{[1 \times 1]}
\end{array}
\right]_{[4 \times 1]}
$$
