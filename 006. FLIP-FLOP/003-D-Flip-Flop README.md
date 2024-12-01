
---

### **3. D Flip-Flop**

**Penjelasan:**
- Menyimpan nilai dari input **D** ke output **Q**.

**README - D Flip-Flop Example:**

```markdown
# D Flip-Flop Implementation

This repository contains an implementation of the **D Flip-Flop** in Python. The D Flip-Flop captures and stores a single data bit.

## Concept

- The **D Flip-Flop** takes a single data input **D** and stores its value as the output **Q**.

## Code Explanation

```python
class DFlipFlop:
    def __init__(self):
        self.Q = 0

    def input_data(self, D):
        self.Q = D
        return self.Q
