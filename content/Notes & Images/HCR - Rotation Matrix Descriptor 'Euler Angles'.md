# Euler Angles
I have to specify beforehand in which axis i will rotate: ~ex.: **ZXZ**
Also all Euler Angles will do 3 [[HCR - Definition of 'Elementary Rotation'|elementary rotations]]: $[\varphi, \ \theta, \ \psi]$

Where for formality:
- "**ROLL**" : always means a rotation along the $z$ axis
- "**PITCH**" : always means a rotation along the $y$ axis
- "**YAW**" : always means a rotation along the $x$ axis
> This are names that sailor uses for rotating the ships

---
###### ~ Examples of Euler Angles Rotations:
- **ZXZ** (Most used for the Euler Angles, *Standard for Euler Angles*): 
$$
R^O_{O \kern 1px '} = R_z(\varphi) \kern 1px R_x(\theta) \kern 1px R_z(\psi)
$$
- **ZYX** (Roll Pitch and Yaw):
$$
R^O_{O \kern 1px '} = R_z(\varphi) \kern 1px R_y(\theta) \kern 1px R_x(\psi)
$$