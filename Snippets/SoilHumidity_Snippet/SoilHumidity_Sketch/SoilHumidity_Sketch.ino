// Arduino Bodenfeuchte messen
// https://iotspace.dev/arduino-bodenfeuchtesensoren---anleitung-und-sketch
//

void setup() {
  pinMode(A0, INPUT);             // A0 als Eingang definieren
  Serial.begin(9600);              // Serielle Kommunikation mit 9600 Baud
  delay(500);
}

void loop() {
  int analogWert = analogRead(A0); // Auslesen des analogen Sensorwertes
  Serial.println(analogWert);      // Ausgabe des Wertes auf der seriellen Konsole
  delay(1000);                     // eine Sekunde warten
}
