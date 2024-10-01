---
aliases:
  - composition of elementary rotation
---
Each [[HCR - Pose of a Rigid Body|orientation]] could be composed by elementary rotations of the object frame with respect to the [[HCR - Reference Frame|reference frame]].
- Successive rotations of an object about the **object frame** is obtained by ==**premultiplication**== of [[HCR - Rotation Matrix|rotation matrices]].
- Successive rotations of an object about the **reference frame** is obtained by ==**postmultiplication**== of rotation matrices.

Where *premultiplication* and *postmultiplication* only mean *when* the [[HCR - Definition of 'Elementary Rotation'|elementary rotation matrix]] is multiplied (if at the *beginning* or at the *end*).

> **NOTE**:
> The object frame is referenced to the reference frame

The composition of various [[HCR - Definition of 'Elementary Rotation'|elementary rotation matrices]] gives form to a complete [[HCR - Rotation Matrix|rotation matrix]]

> We need also to define ==**how** the elementary rotation are composed==, to do this we use the [[HCR - Rotation Matrices Descriptors|rotation matrix descriptors]].