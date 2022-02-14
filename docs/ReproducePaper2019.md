
# Reproduktion des Clone-Benchmark Papers von 2019

Es wurde das Vorgehen aus dem Paper [*The Mutation and Injection Framework: Evaluating Clone Detection Tools with Mutation Analysis*](https://www.researchgate.net/publication/332703085_The_Mutation_and_Injection_Framework_Evaluating_Clone_Detection_Tools_with_Mutation_Analysis) emuliert. 
Dabei wurden das MIF-Tool in verschiedenen Stadien der Verarbeitung festgehalten.

Bei allen Eperimenten handelt es sich um *Automatic clon synthesis experiments* in der Sprache *Java* welche die vom MIF zur Verfügung gestellten repositories (siehe `MutationInjectionFramework/data/repositories/java`)nutzen.

Um die festgehaltenen Stadien besser organisieren zu können, wurden Informationen in den Namen der jeweiligen Projekt-Ordner codiert.
Dabei ist jede Information mittels eines Unterstrichs (`_`) voneinander getrennt.
Die Informationen kommen in der selben Reihenfolge im Namen vor, wie sie hier präsentiert werden:
1. **SX**: Der momentane Stand eines Experiments wird mittels der Kombination `SX` dargestellt, wobei _S_ für Stage steht und _X_ entweder 1, 3 oder 5 ist und den momentanen Zustand des Experiments angibt.
2. **empty|ipscan**: Stellen das System für die Klone dar und werden mit _empty_ oder _ipscan_ angegeben, welche auch vom MIF übernommen wurden (siehe. `MutationInjectionFramework/data/systems/java/`).
3. **functions|blocks**: Beschreibt die untersuchte Größe der Klone. Dies kann _functions_ (für Funktionen) und _blocks_ (für Blöcke) sein.
4. **default-mutators**: gibt an, dass die Defaulteinstellung bei der Auswahl der Mutatoren verwendet wurde.
5. **3750|37500**: Damit ist die Zahl an erzeugten Klonen gemeint. Diese repräsentieren die Daten aus dem Paper.
6. **nicad|spoon|nicad-spoon**: Damit wird für Phasen S5 angegeben, welches Tool für die Evaluation verwendet wurde.
7. **sim-0|60**: Damit wird für Phase S5 die *Unit Recall Required Similarity* und *Unit Precision Required Similarity* angegeben. 

## Hinweise zur Durchführung der einzelnen Schritte (Stages)

### S1: Generation Stage
Es wurden -- wie auch im Paper (@svalenko2019, S.15) -- die folgenden Einstellungen vorgenommen:
|Schalter| Name | Wert| Bemerkung|
|--------|------|-----|----------|
| [c] | Mutator and Mutations      | [r]                           | Damit werden die Standard (default) Optionen ausgewählt                          |
| [2] | Max Fragments              | 250                           |                                                                                  |
| [3] | Clone Granuality           | 1/2                           | Ist vom jeweiligen Werkzeug abhängig -- für beides sind Beispielordner vorhanden |
| [4] | Clone Size                 | Tokens: 100-2000; Lines: 15-200 |                                                                                  |
| [5] | Minimum Clone Similarity   | 0.7                           | 70 Prozent (nach Typ-1 und Typ-2 *normalization*)                                |
| [6] | Mutation Containment       | 0.15                          | 15 Prozent                                                                       |
| [7] | Injection Number           | 10                            | Erstellt verschiedene *Mutation Systems* Hinweis: für das `empty` System ist die Zahl 10 nicht möglich (es wurde 1 verwendet)                                      |
| [8] | Mutation Operator Attempts | 10                            | Wurde nicht im Paper festgelegt, weshalb der Defaultwert von 10 genutzt wird     |
| [9] | Mutator Attempts           | 100                           | Wurde nicht im Paper festgelegt, weshalb der Defaultwert von 100 genutzt wird    |
|     |                            |                               |                                                                                  |
|     |                            |                               |                                                                                  | 

*Hinweis:* Die Erzeugung der Clones kann mehrere Stunden in Anspruch nehmen.

### S3: Evaluation Setup Stage
Das Experiment hat die Generations Phase abgeschlossen und befindet sich im *Evaluation Phase Setup*.
In dieser werden dem Projekt die *Clone Detectors* mitgeteilt.
Dabei können beliebig viele Tools mit aufgenommen und gespeichert werden.
Für jeden Clone Detector werden dabei die folgenden Informationen benötigt:
- Name des Tools 
- Beschreibung des Tools und dessen Anwendung
- absoluter Pfad zum Installationsordner des Tools
- absoluder Pfad zum Tool-Runner

Bevor die Erkennung gestartet wird können noch die folgenden Werte eingestellt werden:
- *Subsume Tolerance*: wurde nicht angegen, muss aber mindestens *Mutation Containment* sein und wird daher auf den selben Wert gesetzt (@svalenko2019, S.12).
- *Unit Recall Required Similarity*: Im Paper wurde 0% und 60% genommen.
- *Unit Precision Required Similarity*: Im Paper wurde 0% und 60% genommen.

*Hinweis:* Es wurde explizit von der Verwendung von 70% (was den Default-Wert darstellt) abgeraten, da es sonst zu anomalien kommen kann. (@svalenko2019, S.17)

mit [s] kann der Evaluationsprozess für alle ausgewählten Werkzeuge beginnen.

# Ergebnisse 

Bei allen Ergebnissen sind die folgenden Informationen immer gleich:
- Es wurde immer mit dem Typ `funtions` gearbeitet
- Es wurden immer die `default-mutators` verwendet
- Die Anzahl der erzeugten Klone ist vom jeweiligen Ausgangssystem abhängig (empty -> 3750; ipscan -> 37500)
- es sind immer beide Clone Detectoren (SPOON und NiCad) enthalten
Es muss also nur unterschieden werden nach dem Ausgangssystem und der Similarity:
- [Empty_Similarity-0](empty_functions_default-mutators_3750_nicad-spoon_sim-0)
- [Empty_Similarity-60](empty_functions_default-mutators_3750_nicad-spoon_sim-60)
- [Ipscan_Similarity-0](ipscan_functions_default-mutators_37500_nicad-spoon_sim-0)
- [Ipscan_Similarity-60](ipscan_functions_default-mutators_37500_nicad-spoon_sim-60)

