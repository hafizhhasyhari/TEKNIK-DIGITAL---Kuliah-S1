# SR Flip-Flop Implementation

This repository contains an implementation of the **SR Flip-Flop** in Python. The SR Flip-Flop is a basic digital logic circuit that is used to store a single bit of information.

## Concept

- **Set** (`S=1, R=0`): The output **Q** is set to `1` and **Q'** is set to `0`.
- **Reset** (`S=0, R=1`): The output **Q** is set to `0` and **Q'** is set to `1`.
- **No change** (`S=0, R=0`): No change in the output state.
- **Invalid state** (`S=1, R=1`): The state is invalid and not allowed as both inputs are active.

## Code Explanation

```python
class SRFlipFlop:
    def __init__(self):
        self.Q = 0  # Output Q
        self.Q_ = 1  # Output Q negated

    def set_reset(self, S, R):
        if S == 0 and R == 0:
            pass
        elif S == 0 and R == 1:
            self.Q = 0
            self.Q_ = 1
        elif S == 1 and R == 0:
            self.Q = 1
            self.Q_ = 0
        elif S == 1 and R == 1:
            print("Invalid state!")
        return self.Q, self.Q_
