import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin kontrol untuk motor servo
servo_pin = 17
GPIO.setup(servo_pin, GPIO.OUT)

# Membuat objek PWM untuk kontrol servo
pwm = GPIO.PWM(servo_pin, 50)  # Frekuensi PWM 50Hz
pwm.start(0)  # Mulai dengan duty cycle 0

def set_angle(angle):
    # Mengubah sudut servo dengan duty cycle
    duty = (angle / 18) + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Membaca nilai dari sensor (gunakan sensor analog ke GPIO atau ADC)
        sensor_value = input("Masukkan nilai sensor (0 hingga 180): ")
        angle = int(sensor_value)

        # Set sudut servo berdasarkan nilai sensor
        set_angle(angle)

        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
