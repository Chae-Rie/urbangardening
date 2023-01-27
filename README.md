# urbangardening M. L. Ebert
Gruppe 1 Urban Gardening EVP MGreve

---

# Aufgaben
Bewässerungssystem 
Grundsätzlich auf C/C++ der Einfachheit geeinigt -> Alle großen Arduino Libs sind C/C++ geschrieben.
Die Arduino IDE selbst arbeitet mit C++ welche in den .ino files die C++ .h und .cpp Files verknüpft.


Auslesen der gerade arbeitenden Komponenten (Status OK/ Nicht OK) 
Auslesen der aktuell gültigen Daten (Wasserstand OK/Nicht OK) -> Zwischenspeichern

Wasserpumpe fängt mit 5V direkt an loszupumpen -> Scheint kein seperates Interface oder so zu geben.
---
# Offene Fragestellung

Wie kommen wir an den Wert des Wasserspiegels? Wir haben eine einfache China Wasserpumpe; Aber keinen Schwimmer oder irgendeinen anderen Indikator um zu
bewerten, dass genug Wasser in dem Wassertank drin ist. 

> Schleife im Code, der periodisch auf dem Display warnt. "Wasserstand könnte niedrig sein"-Type Beat.
> Periode bestimmen anhand der Durchflussgeschwindigkeit der Pumpe und der Regelmäßigkeit, wie oft gegossen wird. 

---

# Links

https://forum.arduino.cc/t/wasserpumpe-mit-uno-steuern/302520

---

# Funktionsbeschreibung

Wasserpumpe wird mit 5V gespeist und hat nur zwei Modi, on and off. 
Wasserpumpe wird aus externem Wassertank/-behälter gefüttert und leitet das Wasser über einen angeschlossenen Schlauch ins Innere des Kits.
Bewässerung von oben per Tropfbewässerung. Kurze Seiten des Deckels werden mit Lichtstreifen bestückt und die langen Seiten werden mit dem Schlauch bestückt. 
Der Schlauch bekommt kleine Löcher direkt über den Pflanzen, um Tropf- oder Regenbewässerung zu simulieren. (Druck der Pumpe testen!!)
