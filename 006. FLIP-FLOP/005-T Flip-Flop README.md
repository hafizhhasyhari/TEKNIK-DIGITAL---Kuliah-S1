
---

### **4. T Flip-Flop**

**Penjelasan:**
- Jika input **T = 1**, maka output **Q** dibalik (toggle).
- Tidak ada perubahan jika input **T = 0**.

**README - T Flip-Flop Example:**

```markdown
# T Flip-Flop Implementation

This repository contains an implementation of the **T Flip-Flop** in Python. The T Flip-Flop toggles the output when the input is active.

## Concept

- If **T = 1**, the output **Q** is toggled.
- If **T = 0**, there is no change in the output.

## Code Explanation

```python
class TFlipFlop:
    def __init__(self):
        self.Q = 0

    def toggle(self, T):
        if T == 1:
            self.Q = not self.Q
        return self.Q
