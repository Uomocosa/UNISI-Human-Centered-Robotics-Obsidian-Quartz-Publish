# Impedance
**Impedance**: $Z(s)$
-> $F(s) = Z(s) \cdot \Large \dot{\normalsize X}\normalsize(s)$

For a given force the smaller the impedance -> the higher is the velocity and viceversa.

###### ~ Ex.: Mass-Spring Problem:
$$
\begin{array}{l}
M\ddot x(t) + \beta \dot x(t) + kx(t) = F(t)
\\
\kern 15px \mathcal{L}\left[\dot x(t)\right] = \Large \dot{\normalsize X}\normalsize(s)
\\
\kern 15px \mathcal{L}\left[\ddot x(t)\right] = s\Large \dot{\normalsize X}\normalsize(s)
\\
\kern 15px \mathcal{L}\left[x(t)\right] = \Large \frac{1}{s}\dot{\normalsize X}\normalsize(s)
\\
\\
\Rightarrow Ms\Large \dot{\normalsize X}\normalsize(s) + \beta \Large \dot{\normalsize X}\normalsize(s) + \Large \frac{k}{s} \dot{\normalsize X}\normalsize(s) = F(s)
\\
\\
\Rightarrow F(s) = \underbrace{\left[Ms + \beta + \Large \frac{k}{s} \normalsize \right]}_{\Large Z(s)} \cdot \Large \dot{\normalsize X}\normalsize(s)
\end{array}
$$

---
### Impedance:
For a given system the higher is the **impedance**, the lower will be its velocity.
$$
Z(s) := \frac{F(s)}{\Large \dot{\normalsize X}\normalsize(s)}
$$
An higher impedance brings more stability to the system.
