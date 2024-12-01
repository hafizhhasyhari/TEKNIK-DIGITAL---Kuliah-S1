# T Flip-Flop: Flip-flop toggle untuk fungsi pembalik logika
# Dibuat oleh Hafizh Hilman Asyhari dari Indonesia tahun 2024

class TFlipFlop:
    def __init__(self):
        self.Q = 0  # Output Q

    def toggle(self, T):
        # Jika T = 1, toggle Q
        if T == 1:
            self.Q = not self.Q
        # Tidak ada perubahan jika T = 0
        return self.Q

# Contoh Penggunaan
t = TFlipFlop()
print(t.toggle(1))  # Toggle
print(t.toggle(1))  # Toggle
print(t.toggle(0))  # No change
