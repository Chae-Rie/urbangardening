// https://www.reichelt.de/magazin/projekte/arduino-uno-temperatur-luftfeuchtigkeit-messen/

#include <SPI.h> // Bibliothek für die serielle Schnittstelle laden
#include <DHT.h> // Bibliothek für den Sensor laden
 
 // Instanz der Sensorschnittstelle erstellen.
 // A0 ist der Anschluss am Grove Base Shield, DHT22 der Sensortyp
 DHT dht(A0, DHT22); 
 
 void setup() { // Wird einmal beim Start ausgeführt
  Serial.begin(9600); // Serielle Schnittstelle initialisieren
  dht.begin(); // Sensor initialisieren
 }
 
 void loop() { // Wird in einer Endlosschleife ausgeführt
  float humidity = dht.readHumidity(); // Daten auslesen
  float temperature = dht.readTemperature(); // Daten auslesen
 
  if (isnan(temperature) || isnan(humidity)) { // Hat das Auslesen funktioniert?
    Serial.println("Fehler bein lesen von DHT");
  } else {
    // Daten ausgeben
    Serial.print(temperature);
    Serial.print(" | ");
    Serial.print(humidity);
    Serial.println();
  }
  delay(1000); // Programmausführung für 1s anhalten
 }
