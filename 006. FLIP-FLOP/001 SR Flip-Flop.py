# SR Flip-Flop: Untuk menyetel dan mereset nilai bit
# Dibuat oleh Hafizh Hilman Asyhari dari Indonesia tahun 2024

class SRFlipFlop:
    def __init__(self):
        self.Q = 0  # Output Q
        self.Q_ = 1  # Output Q negated

    def set_reset(self, S, R):
        # Kondisi SR Flip-Flop
        if S == 0 and R == 0:
            # Tidak ada perubahan
            pass
        elif S == 0 and R == 1:
            # Reset: Q = 0
            self.Q = 0
            self.Q_ = 1
        elif S == 1 and R == 0:
            # Set: Q = 1
            self.Q = 1
            self.Q_ = 0
        elif S == 1 and R == 1:
            # Invalid state, tidak diperbolehkan
            print("Invalid state!")
        return self.Q, self.Q_

# Contoh Penggunaan
sr = SRFlipFlop()
print(sr.set_reset(1, 0))  # Set
print(sr.set_reset(0, 1))  # Reset
