# JK Flip-Flop: Penyempurnaan dari SR dengan kondisi toggle
# Dibuat oleh Hafizh Hilman Asyhari dari Indonesia tahun 2024

class JKFlipFlop:
    def __init__(self):
        self.Q = 0  # Output Q

    def toggle(self, J, K):
        # Kondisi JK Flip-Flop
        if J == 0 and K == 0:
            # Tidak ada perubahan
            pass
        elif J == 0 and K == 1:
            # Reset: Q = 0
            self.Q = 0
        elif J == 1 and K == 0:
            # Set: Q = 1
            self.Q = 1
        elif J == 1 and K == 1:
            # Toggle: Q dibalik
            self.Q = not self.Q
        return self.Q

# Contoh Penggunaan
jk = JKFlipFlop()
print(jk.toggle(1, 0))  # Set
print(jk.toggle(0, 1))  # Reset
print(jk.toggle(1, 1))  # Toggle
