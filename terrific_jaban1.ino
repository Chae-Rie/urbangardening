#include <LiquidCrystal_I2C.h>

//#include <LiquidCrystal.h>

// C++ code
//
//#include <Adafruit_LiquidCrystal.h>

int seconds = 0;

int Bodenfeuchte = 0;

int Luftfeuchte = 0;

int licht = 0;

//Adafruit_LiquidCrystal lcd_1(0);

//Adafruit_LiquidCrystal lcd_3(0);

//Adafruit_LiquidCrystal lcd_5(0);

//Adafruit_LiquidCrystal lcd_6(0);

//Adafruit_LiquidCrystal lcd_2(0);

//Adafruit_LiquidCrystal lcd_4(0);

LiquidCrystal_I2C lcd(7, 8, 9, 10, 11, 12);

void setup()
{
  lcd.begin(16, 2);
  lcd.print('Hallo');
  pinMode(LED_BUILTIN, OUTPUT);
  //lcd_3.begin(16, 2);
  //lcd_5.begin(16, 2);
  pinMode(A2, INPUT);
  //lcd_6.begin(16, 2);
  pinMode(A0, INPUT);
  //lcd_2.begin(16, 2);
  pinMode(A1, INPUT);
  //lcd_4.begin(16, 2);
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  lcd.setBacklight(1);
  lcd.setCursor(0, 0);
  lcd.print("SH");
  lcd.setCursor(5, 0);
  lcd.print("AH");
  lcd.setCursor(10, 0);
  lcd.print("L");

  licht = analogRead(A2);
  lcd.setCursor(10, 1);
  lcd.print(licht);

  Bodenfeuchte = analogRead(A0);
  lcd.setCursor(0, 1);
  lcd.print(Bodenfeuchte);

  Luftfeuchte = analogRead(A1);
  lcd.setCursor(5, 1);
  lcd.print(Luftfeuchte);

  if (licht > 50) {
    digitalWrite(3, HIGH);
  } else {
    digitalWrite(3, LOW);
  }

  if (Bodenfeuchte < 50) {
    digitalWrite(2, HIGH);
    delay(1000); // Wait for 1000 millisecond(s)
  } else {
    digitalWrite(2, LOW);
    delay(1000); // Wait for 1000 millisecond(s)
  }
}