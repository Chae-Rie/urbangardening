void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read the sensor data
  int air_humidity = 1;
  int soil_humidity = 2;
  int light = 3;

  // Send the sensor data as plain text over serial
  Serial.print(air_humidity);
  Serial.print(",");
  Serial.print(soil_humidity);
  Serial.print(",");
  Serial.println(light);

  // Wait for a moment before sending the next data
  delay(1000);
}