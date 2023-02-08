// Importieren der Bibliothek "FastLED"
// https://draeger-it.blog/led-stripe-am-arduino-uno-steuern/
#include <FastLED.h> // Die muss noch hinzugefügt werden
// Wieviele LEDs sind auf dem LED Stripe?
#define NUM_LEDS 8
// digitaler Pin an welchem der LED Stripe angeschlossen ist
#define DATA_PIN 3
// Ein Array mit den LEDs
CRGB leds[NUM_LEDS];
void setup() {
  //definieren des WS2812B LED Stripe vom Typ GRB (Green, Red, Blue)
  //sollte ggf. ein anderer Typ verwendet werden so muss dieser hier angepasst werden.
  //Mögliche Typen sind im Blonk Beispiel unter https://github.com/FastLED/FastLED/blob/master/examples/Blink/Blink.ino 
  // enthalten.
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
}
void loop() { 
  // eine Schleife von 0 bis NUM_LEDS
  for(int i=0;i<=NUM_LEDS;i++){
    // LED an Position "i" in ROT 
    leds[i] = CRGB::Red;
    // aktivieren der gesetzen Werte
    FastLED.show();
    // eine Pause von 75ms.
    delay(75);
    // deaktivieren der LED / es wird lediglich die Farbe schwarz gesetzt
    leds[i] = CRGB::Black;
    // aktivieren der gesetzen Werte
    FastLED.show();
    // eine Pause von 75ms.
    delay(75);  
  }
}
