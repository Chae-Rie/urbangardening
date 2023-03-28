void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read the sensor data
  unsigned int air_humidity = 1;
  unsigned int soil_humidity = 2;
  unsigned int light = 3;

  // im echten Code:
  //unsigned int air_humidity = analogRead(A0);
  //unsigned int soil_humidity = analogRead(A1);
  //unsigned int light = analogRead(A2);  
  

  // Um die Daten auseinanderhalten zu können sind die delimiter "," wichtig
  Serial.print(air_humidity);
  Serial.print(",");
  Serial.print(soil_humidity);
  Serial.print(",");
  Serial.println(light);

  // Der Arduino soll zwischen dem Senden eine Pause bekommen
  delay(500);
}