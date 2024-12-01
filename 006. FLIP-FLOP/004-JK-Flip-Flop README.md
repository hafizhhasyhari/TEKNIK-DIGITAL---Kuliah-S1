
---

### **2. JK Flip-Flop**

**Penjelasan:**
- **Set** (`J=1, K=0`): Output `Q = 1`.
- **Reset** (`J=0, K=1`): Output `Q = 0`.
- **Toggle** (`J=1, K=1`): Output `Q` dibalik.
- **No change** (`J=0, K=0`): Output tidak berubah.

**README - JK Flip-Flop Example:**

```markdown
# JK Flip-Flop Implementation

This repository contains an implementation of the **JK Flip-Flop** in Python. The JK Flip-Flop is an improvement over the SR Flip-Flop with toggle capability.

## Concept

- **Set** (`J=1, K=0`): The output **Q** is set to `1`.
- **Reset** (`J=0, K=1`): The output **Q** is set to `0`.
- **Toggle** (`J=1, K=1`): The output **Q** is toggled (flips between 0 and 1).
- **No change** (`J=0, K=0`): No change in the output state.

## Code Explanation

```python
class JKFlipFlop:
    def __init__(self):
        self.Q = 0

    def toggle(self, J, K):
        if J == 0 and K == 0:
            pass
        elif J == 0 and K == 1:
            self.Q = 0
        elif J == 1 and K == 0:
            self.Q = 1
        elif J == 1 and K == 1:
            self.Q = not self.Q
        return self.Q
