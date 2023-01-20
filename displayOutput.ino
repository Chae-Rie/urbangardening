#include <LiquidCrystal.h>
#include <GY21.h>
#include <Wire.h>

// Connect VIN to 3-5VDC
// Connect GND to ground
// Connect SCL to I2C clock pin
// Connect SDA to I2C data pin

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

GY21 sensor;

int moisturePin = 0;

void setup() {
  lcd.begin(16, 3);

  Serial.begin(9600);
  Wire.begin();
}

void loop() {
  float temperatur = sensor.GY21_Temperature();
  float humidity = sensor.GY21_Humidity();
  int moisture = analogRead(moisturePin);

  lcd.setCursor(0, 0);
  lcd.print('Temp.: ' + temperatur);

  lcd.setCursor(0, 1);
  lcd.print('Luftfeuch.:' + humidity);

  lcd.setCursor(0, 2);
  lcd.print('Bodenfeuch.:' + moisture);

  delay(500);
}
