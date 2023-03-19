// Arduino IDE:
// File -> Examples -> 04.Communication -> PhysicalPixel

const int ledPin = 13; // pin the LED is attached to
int incomingByte;      // variable stores  serial data
bool responded = false;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    //messageReceived = Serial.readString();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H' && !responded) {
      digitalWrite(ledPin, HIGH);
      Serial.println("SetH"); //print out to serial monitor to check state
      responded = true;
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L' && !responded) {
      digitalWrite(ledPin, LOW);
      Serial.println("SetL");
      responded = true;
      //Serial.println("1234"); //print out to serial monitor to check state
    }
    if (incomingByte == 'J' && !responded){
      Serial.println("5678");
      responded = true;
    }

  }
  responded = false;
}