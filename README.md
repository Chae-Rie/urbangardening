# urbangardening S. Baecher
Gruppe 1 Urban Gardening EVP MGreve

---
# Aufgaben
Display + Ausgabe der Werte des LuftfeuchteMessers sowie BodenfeuchteMessers

Grundsätzlich auf C/C++ der Einfachheit geeinigt -> Alle großen Arduino Libs sind C/C++ geschrieben.
Die Arduino IDE selbst arbeitet mit C++ welche in den .ino files die C++ .h und .cpp Files verknüpft.


Auslesen der gerade arbeitenden Komponenten (Status OK/ Nicht OK) 
Auslesen der aktuell gültigen Daten (Luftfeuchte X, Bodenfeuchte Y) -> Zwischenspeichern und im regelmäßigen Abständen an das Display übertragen

Verdrahten -> Werte auslesen/ pollen -> Werte speichern -> Werte ausgeben
---
# Offene Fragestellung

Ideen sammeln 

---
Sammlung:

Display (QAPASS)
  - https://starthardware.org/lcd/
  - https://docs.arduino.cc/learn/electronics/lcd-displays

Luftfeuchtigkeitsmesser (gy-21)
  - https://github.com/JonasGMorsch/GY-21/blob/master/examples/GY-21_test/GY-21_test.ino

Bodenfeuchtigkeitsmesser (iduino moisture sensor)
  - https://funduino.de/wp-content/uploads/2019/04/001616242-an-01-en-BODENFEUCHTE_SENS__MOD__IDUINO_ME110-1.pdf
