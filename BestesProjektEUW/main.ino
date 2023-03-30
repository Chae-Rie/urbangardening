#include <LiquidCrystal_I2C.h>

#include <Wire.h>
#include <Adafruit_HTU21DF.h>

int soilMoisture = 0;
int light = 0;
int relative_hum = 0;
int tempC = 0;

LiquidCrystal_I2C lcd(0x27,20,4);
Adafruit_HTU21DF HTU21 = Adafruit_HTU21DF();

void setup()
{
  lcd.init();
  lcd.backlight();
  
  pinMode(A1, INPUT);
  pinMode(A0, INPUT);
  pinMode(2, OUTPUT);
  // pinMode(3, OUTPUT);

  Serial.begin(9600);

  if (!HTU21.begin()) {
    Serial.println("Sensor not found!");
    while (1);
  }
}

void loop()
{
  lcd.setCursor(0, 0);
  lcd.print("BF");
  lcd.setCursor(6, 0);
  lcd.print("LF");
  lcd.setCursor(12, 0);
  lcd.print("T");

  soilMoisture = analogRead(A0);
  lcd.setCursor(0, 1);
  lcd.print(soilMoisture);

  tempC = HTU21.readTemperature();  

  lcd.setCursor(6, 1);
  lcd.print(tempC);

  lcd.setCursor(9, 1);
  lcd.print("C");

  relative_hum = HTU21.readHumidity();

  lcd.setCursor(12, 1);
  lcd.print(relative_hum);

  light = analogRead(A1);

  if (light > 700) {
    digitalWrite(2, HIGH);
  } else {
    digitalWrite(2, LOW);
  }

  // if (soilMoisture < 300) {
  //  digitalWrite(3, HIGH);
  // } else {
  //  digitalWrite(3, LOW);
  // }
  
  Serial.print(relative_hum);
  Serial.print(",");
  Serial.print(soilMoisture);
  Serial.print(",");
  Serial.println(light);
  Serial.println(",");
  Serial.println(tempC);

  delay(1000);
}