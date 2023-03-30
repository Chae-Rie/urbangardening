Referenzen: [[}project Urbangardening]] 
Tags : 
Datum: 2023:01:27 Zeit: 11:37
Author : Sascha Bächer, Michell Teuber
Quelle : 
Status :  
# Notizen 
## Funktionsbeschreibung

Ziel des Konstrukts ist es Pflanzen auch in Abwesenheit ausreichend zu bewässern, beleuchten und zu präsentieren.
Auch der beschäftigte Pflanzenliebhaber wird so in der Lage sein zu jeder Tages und Nachtzeit das Wohlbefinden der Pflanzen sicherzustellen.

Mithilfe eines LCD ist es auch auf einem Blick möglich die aktuellen Umgebungsbedingungen für die Plfanzen zu bewerten. 
Dazu fragen Sensoren die Bodenfeuchte, Luftfeuchte und die Lichtstärke ab, um angemessen darauf zu reagieren.

Es sind folgende Komponenten in dem Kit verbaut:

### Wasserpumpe
Die Wasserpumpe wird mit 5V gespeist und hat zwei Modi: ON und OFF.
Wasserpumpe wird aus externem Wassertank befüllt und leitet das Wasser über einen angeschlossenen Schlauch in das Innere des Kits.

Wasserpumpe ist wie folgt angeschlossen:
- 5V
- GND
- Durch ein Relais gesteuert -> Output: 3
### LCD
Das Display wird mit 5V gespeist und zeigt folgende Informationen an:
- Luftfeuchtigkeit 
- Bodenfeuchtigkeit
LCD ist wie folgt angeschlossen:
- GND
- 5V
- Input: SDA und SCL
### Feuchtigkeitssensor (Erde)
Der Feuchtigkeitssensor wird mit 5V  gespeist und misst in einem festen Intervall  die Feuchtigkeit.
Die Komponente steht in ständigem Austausch mit dem LCD.
Der Feuchtigkeitssensor ist wie folgt angeschlossen:
- GND
- 5V
- Input: A0

Wenn Feuchtigkeit auf bestimmten Level -> Pumpe an!

### Luftfeuchtigkeitssensor
Der Luftfeuchtigkeitssensor wird mit 5V gespeist und misst in einem festen Intervall die Luftfeuchtigkeit.
Die Komponente steht in ständigem Austausch mit dem LCD.
Der Luftfeuchtigkeitssensor ist wie folgt angeschlossen:
- GND
- 5V
- Output:
- SCL und SDA (Clock und Datenleitung)
### Licht und Lichtsensorik
Als Lichtquelle wird ein Lichtband verwendet, welches mit 12 V angeschlossen wird. Verbunden via Lötstelle.

Der verbaute Lichtsensor verändert die vom Arduino gemessenen Widerstand entsprechend der aktuellen Lichtstärke. Bei einem Wert von X Maßeinheit (Lux? Lumen?) Wird der Sensor dem Arduino ermöglichen das Lichtband ON oder OFF zu schalten.
Das Lichtband ist wie folgt angeschlossen:
- 12V
- GND
- Output: 2

Der Lichtsensor ist wie folgt angeschlossen:
- 5V
- GND
- Input: A1

Wenn Lichtsensor auf bestimmten Level -> Licht an
wenn unterschritten -> Licht aus

### Temperatur
Es wird stets und ständig die Temperatur im Behältnis gemessen.
Der Sensor ist wie folgt angeschlossen:
- GND
- 5V
- SCL und SDA (Clock und Datenleitung)
## Technologie Schema
Siehe Anhang
## Zustandsdiagramme
Siehe Anhang
## Sketche
Siehe Anhang

## User Stories
### Licht
Als jemand Vergessliches/Faules möchte ich, dass die Planzen in der Box automatisch/je nach Lichtverhältnis beleuchtet werden. So brauche ich mich nicht darum kümmern und die Planze ist optimal beleuchtet.

### Display
Als Pflanzenliebhaber möchte ich auf Anhieb sehen, wie die Verhältnisse in der Box sind, um mit einem Blick optimal informiert zu sein.

### Bewässerung
Als berufstätiger Pflanzenliebhaber möchte ich, dass die Pflanze auch in meiner Abwesenheit durch das automatische Bewässerungssystem optimal mit Wasser versorgt wird.

### Wartungsschnittstelle
Als alleiniger Benutzer der Box möchte ich möglichst unkompliziert und unabhängig alle Informationen der Box inklusive Fehlerlogs abfragen und durch eine gängige Schnittstelle erhalten. So kann ich zu jeder Zeit auf eventuelle Probleme reagieren.