



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
