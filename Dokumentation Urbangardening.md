Referenzen: [[}project Urbangardening]] 
Tags : 
Datum: 2023:01:27 Zeit: 11:37
Author : 
Quelle : 
Status :  #WIP 
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
### LCD
Das Display wird mit 5V gespeist und zeigt folgende Informationen an:
- Luftfeuchtigkeit 
- Bodenfeuchtigkeit
- Status der Komponenten (einzeln) -> Idee: Anfangsbuchstaben der Komponenten nebeeinander und dann ein eindeutiges Symbol für OK/Nicht OK
LCD ist wie folgt angeschlossen:
- GND
- 5V
- Output: 
- Input: A4, A5
### Feuchtigkeitssensor (Erde)
Der Feuchtigkeitssensor wird mit 5V  gespeist und misst in einem Intervall von X die Feuchtigkeit.
Wie macht er das?
Wie wird das ausgelesen?
Die Komponente steht in ständigem Austausch mit dem LCD.
Der Feuchtigkeitssensor ist wie folgt angeschlossen:
- GND
- 5V
- Output:
- Input: A3

Wenn Feuchtigkeit auf bestimmten Level -> Pumpe an!

### Luftfeuchtigkeitssensor
Der Luftfeuchtigkeitssensor wird mit 5V gespeist und misst in einem Intervall von X die Luftfeuchtigkeit.
Wie macht er das?
Wie wird das ausgelesen?
Die Komponente steht in ständigem Austausch mit dem LCD.
Der Luftfeuchtigkeitssensor ist wie folgt angeschlossen:
- GND
- 5V
- Output:
- Input: A2
### Licht und Lichtsensorik
Als Lichtquelle wird ein Lichtband verwendet, welches mit X V angeschlossen wird. Verbunden ist dieses via Lötstelle mit dem Arduino? Oder mit Klammer?

Der verbaute Lichtsensor verändert die vom Arduino gemessenen Widerstand entsprechend der aktuellen Lichtstärke. Bei einem Wert von X Maßeinheit (Lux? Lumen?) Wird der Sensor dem Arduino ermöglichen das Lichtband ON oder OFF zu schalten.
Das Lichtband ist wie folgt angeschlossen:
- xV
- GND
- Output:
- Input:

Der Lichtsensor ist wie folgt angeschlossen:
- xV
- GND
- Output:
- Input: A1

Wenn Lichtsensor auf bestimmten Level -> Licht an
wenn unterschritten -> Licht aus
## Technologie Schema
 Aus TinkerCAD hinzugefügt
## Zustandsdiagramme
Sascha B. =)
## Sketche
Wird nachgreicht

## User Stories
### Licht
Als jemand Vergessliches/Faules möchte ich, dass die Planzen in der Box automatisch/je nach Lichtverhältnis beleuchtet werden. So brauche ich mich nicht darum kümmern und die Planze ist optimal beleuchtet.

### Display
Als Pflanzenliebhaber möchte ich auf Anhieb sehen, wie die Verhältnisse in der Box sind, um mit einem Blick optimal informiert zu sein.

### Bewässerung
Als berufstätiger Pflanzenliebhaber möchte ich, dass die Pflanze auch in meiner Abwesenheit durch das automatische Bewässerungssystem optimal mit Wasser versorgt wird.

### Wartungsschnittstelle
Als alleiniger Benutzer der Box möchte ich möglichst unkompliziert und unabhängig alle Informationen der Box inklusive Fehlerlogs abfragen und durch eine gängige Schnittstelle erhalten. So kann ich zu jeder Zeit auf eventuelle Probleme reagieren.