#include "lightsensor.h"

// Vorab definierte Konstanten
// Können die PIN-Belegungen so bleiben?

const int LIGHT_SENSOR_PIN = A0; 
const int LED_PIN          = 3;  
const int ANALOG_THRESHOLD = 500; // Ab welchem Wert soll die LED angehen?

int analogValue = 0;

// does it even makes sense to create a class?
