Scheinbar ist es unüblich die LED-Stripes mit 5V zu betreiben, weil das entweder a) einfach  nicht geht oder b) zu wenig Saft drauf ist.
Einige Stripes brauchen 12V
- Hr. Greve um einen Upstepper bitten

https://peppe8o.com/neopixel-strip-arduino/

```
#include <Adafruit_NeoPixel.h>
#define PIN 2   // input pin Neopixel is attached to
#define NUMPIXELS      12 // number of neopixels in strip
Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
int delayval = 100; // timing delay in milliseconds
int redColor = 0;
int greenColor = 0;
int blueColor = 0;
void setup() {
  // Initialize the NeoPixel library.
  pixels.begin();
}
```
