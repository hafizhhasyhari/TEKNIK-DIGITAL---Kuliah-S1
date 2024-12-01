#include <Servo.h>  // Memasukkan library untuk kontrol servo

Servo wristServo;  // Membuat objek servo untuk pergelangan tangan

int sensorPin = A0;  // Pin untuk sensor potensiometer atau sensor flex
int sensorValue = 0;  // Nilai sensor
int angle = 0;  // Sudut pergelangan tangan

void setup() {
  wristServo.attach(9);  // Menghubungkan servo dengan pin 9 pada Arduino
  Serial.begin(9600);  // Menginisialisasi komunikasi serial
}

void loop() {
  // Membaca nilai dari sensor (misalnya, potensiometer)
  sensorValue = analogRead(sensorPin);
  
  // Mengubah nilai sensor menjadi sudut servo (dalam rentang 0 hingga 180)
  angle = map(sensorValue, 0, 1023, 0, 180);

  // Menggerakkan servo sesuai dengan sudut yang diinginkan
  wristServo.write(angle);

  // Menampilkan nilai sensor dan sudut pada Serial Monitor
  Serial.print("Sensor Value: ");
  Serial.print(sensorValue);
  Serial.print(" -> Angle: ");
  Serial.println(angle);

  delay(100);  // Delay untuk kestabilan pembacaan

  // create by Hafizh Hilman Asyhari  @hafizhhasyhari
  // 12 Desember Tahun 2024 
}
