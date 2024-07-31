# Stability and Instability
Real World: **Continuous Time**
Computer: **Discrete Time** (Determined by the CPU Clock)

---
# Instability in Haptics
- The Discrete Time introduced a delay, you read and then act after 1 tic (1 tic of the CPU Clock), increased if there is a feedback loop.
- If the delay is too big you cannot use haptics, it breaks the "immersion"
- We want the most realistic haptics (closest to reality as possible)
- The delay should be $t_{delay} \le 13 \ ms$ (the human body cannot recognize a delay lesser than this)

---
# 
Position of z_b i make the difference between z_b - z_a at D.T. k_h, 


---
# Diagram
![[SmartSelect_20220310-093503_Samsung Notes.jpg]]

$x_a(k)$ : INPUT
$y_p(k)$ : OUTPUT
$\frac{G(z)}{1 + G(z)}$
where $G(z) = \frac{1}{z}$
$$
Z(z) = \frac{\Large \frac{h_H}{(k_p z)}}{1 + \Large \frac{h_H}{(k_p z)}}
$$



If $k_H \lt k_p$ : 