# Glosarium Arduino ver 2024
* Oleh :Hafizh H Asyhari
### pinMode()

** Digunakan untuk mengatur pin Arduino sebagai input atau output.
Contoh: pinMode(motorPin1, OUTPUT); **

###analogRead()
Membaca nilai analog dari pin input (0-1023).
Contoh: sensorValue = analogRead(sensorPin);

###map()
Mengonversi suatu rentang nilai menjadi rentang nilai lain. Dalam program ini digunakan untuk mengubah nilai sensor menjadi nilai PWM.
Contoh: motorSpeed = map(sensorValue, 0, 1023, 0, 255);

###digitalWrite()
Menulis nilai HIGH (5V) atau LOW (0V) ke pin digital.
Contoh: digitalWrite(motorPin1, HIGH);

###analogWrite()
Mengatur nilai PWM (0-255) pada pin output untuk mengontrol kecepatan motor.
Contoh: analogWrite(enablePin, motorSpeed);
Serial.begin()

Memulai komunikasi serial antara Arduino dan komputer.
Contoh: Serial.begin(9600);
Serial.print() / Serial.println()

Mengirim data untuk ditampilkan di Serial Monitor Arduino IDE.
Contoh: Serial.println(sensorValue);
