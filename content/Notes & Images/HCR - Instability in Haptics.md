---
aliases:
  - instability in haptics
---
- The Discrete Time introduced a delay, you read and then act after 1 tic (1 tic of the CPU Clock), increased if there is a feedback loop.
- If the delay is too big you cannot use haptics, it breaks the "immersion"
- We want the most realistic haptics (closest to reality as possible)
- The delay should be $t_{delay} \le 13 \ ms$ (the human body cannot recognize a delay lesser than this)
