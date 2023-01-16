// Vorab definierte Konstanten

const int LIGHT_SENSOR_PIN = A0; 
const int LED_PIN          = 3;  
// Können die PIN-Belegungen so bleiben?
const int ANALOG_THRESHOLD = 500; // Ab welchem Wert soll die LED angehen?
int analogValue = 0;


void setup() {
  pinMode(LED_PIN, OUTPUT); // set arduino pin to output mode
}

void loop() {
  analogValue = analogRead(LIGHT_SENSOR_PIN);
  if(analogValue < ANALOG_THRESHOLD)
    digitalWrite(LED_PIN, HIGH);
  else
    digitalWrite(LED_PIN, LOW); 

    // Einfachste Möglichkeit die Werte abzufragen und zu vergleichen. Wollen wir ggf.
    // ein delay nutzen? 
}
