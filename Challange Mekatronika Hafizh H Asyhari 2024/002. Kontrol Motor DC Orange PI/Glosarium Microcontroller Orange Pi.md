# **Kontrol Motor DC menggunakan Mikrokontroler dan Orange Pi**
### Dibuat oleh : Hafizh H Asyhari

## **Kata Kunci pada Program Orange Pi (Python)**

### **1. RPi.GPIO**
Library Python yang digunakan untuk mengontrol pin GPIO di Orange Pi.

```python
import RPi.GPIO as GPIO

### 2. **GPIO.setmode()**
Mengatur mode penomoran pin pada Orange Pi.

BCM: Penomoran berdasarkan GPIO.
BOARD: Penomoran berdasarkan pin fisik.


GPIO.setmode(GPIO.BCM)  # Menggunakan mode BCM

