import RPi.GPIO as GPIO
import time

# Setup GPIO untuk motor
motorPin1 = 17
motorPin2 = 18
enablePin = 22  # Pin untuk mengontrol kecepatan motor (PWM)
sensorPin = 0  # ADC channel untuk membaca sensor (gunakan ADC eksternal)

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorPin1, GPIO.OUT)
GPIO.setup(motorPin2, GPIO.OUT)
GPIO.setup(enablePin, GPIO.OUT)

# Setup PWM untuk motor
pwm = GPIO.PWM(enablePin, 1000)  # Frekuensi 1 kHz
pwm.start(0)  # Mulai dengan duty cycle 0

def read_sensor():
    # Fungsi untuk membaca nilai sensor (misalnya dari ADC)
    # Di sini Anda harus menggunakan pustaka ADC untuk mendapatkan nilai analog
    # Asumsikan kita menerima nilai antara 0-1023 dari sensor
    return 512  # Contoh nilai sensor, ganti dengan kode ADC yang sesuai

def set_motor_speed(speed):
    # Mengatur kecepatan motor berdasarkan sensor
    duty = (speed / 1023) * 100  # Mengubah kecepatan menjadi duty cycle 0-100
    pwm.ChangeDutyCycle(duty)
    
    if speed > 512:
        GPIO.output(motorPin1, GPIO.HIGH)  # Motor maju
        GPIO.output(motorPin2, GPIO.LOW)
    else:
        GPIO.output(motorPin1, GPIO.LOW)   # Motor mundur
        GPIO.output(motorPin2, GPIO.HIGH)

try:
    while True:
        sensor_value = read_sensor()
        print(f"Sensor Value: {sensor_value}")

        set_motor_speed(sensor_value)
        
        time.sleep(0.1)

# Program dibuat oleh Hafizh Hilman Asyhari
# Jakarta, Indonesia. 1 Desember 2024

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
