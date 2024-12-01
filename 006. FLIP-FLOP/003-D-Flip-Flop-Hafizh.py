# D Flip-Flop: Flip-flop data dengan input tunggal
# Dibuat oleh Hafizh Hilman Asyhari dari Indonesia tahun 2024

class DFlipFlop:
    def __init__(self):
        self.Q = 0  # Output Q

    def input_data(self, D):
        # Input data D ke Q
        self.Q = D
        return self.Q

# Contoh Penggunaan
d = DFlipFlop()
print(d.input_data(1))  # Input 1
print(d.input_data(0))  # Input 0
