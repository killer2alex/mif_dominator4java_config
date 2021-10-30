
# Reproduktion des Clone-Benchmark Papers von 2019

Es wurde das Vorgehen aus dem Paper (*The Mutation and Injection Framework: Evaluating Clone Detection Tools with Mutation Analysis*)[https://www.researchgate.net/publication/332703085_The_Mutation_and_Injection_Framework_Evaluating_Clone_Detection_Tools_with_Mutation_Analysis] emuliert und verschiedene Stadien (in den sich das MIF-Tools befindet) festgehalten. Dabei gilt:
- Bei allen Eperimenten handelt es sich um *Automatic clon synthesis experiments* in der Sprache *Java* welche die vom MIF zur Verfügung gestellten repositories (vgl. `MutationInjectionFramework/data/repositories/java`)nutzen. 
- Der momentane Stand eines Experiments wird mittels der Kombination `SX` dargestellt, wobei `S` für Stage steht und `X` entweder 1, 3 oder 5 ist und den momentanen Zustand des Experiments angibt.
- Das System wird mit `Empty` oder `Ipscan` angegeben welche auch vom MIF übernommen wurden (vgl. `MutationInjectionFramework/data/systems/java/`).
- Der untersuchte Clonetyp wird als nächstes angegeben. Dies kann *Func* (für Functions) und *Block* sein.
- Bei allen gespeicherten Stadien S3 und S5 wurde NiCad verwendet, was jedoch neu hinzugefügt werden muss.

## Phasen (**S**tages)

### S1: Generation Stage
Es wurden -- wie auch im Paper -- die folgenden Einstellungen vorgenommen(Option) um in die Phase 3 zu kommen:
|Schalter| Name | Wert| Bemerkung|
|--------|------|-----|----------|
| [c] | Mutator and Mutations      | [r]                           | Damit werden die Standard (default) Optionen ausgewählt                          |
| [2] | Max Fragments              | 250                           |                                                                                  |
| [3] | Clone Granuality           | 1/2                           | Ist vom jeweiligen Werkzeug abhängig -- für beides sind Beispielordner vorhanden |
| [4] | Clone Size                 | Tokens: 100-2000; Lines: 15-200 |                                                                                  |
| [5] | Minimum Clone Similarity   | 0.7                           | 70 Prozent (nach Typ-1 und Typ-2 *normalization*)                                |
| [6] | Mutation Containment       | 0.15                          | 15 Prozent                                                                       |
| [7] | Injection Number           | 10                            | Erstellt verschiedene *Mutation Systems*                                         |
| [8] | Mutation Operator Attempts | 10                            | Wurde nicht im Paper festgelegt, weshalb der Defaultwert von 10 genutzt wird     |
| [9] | Mutator Attempts           | 100                           | Wurde nicht im Paper festgelegt, weshalb der Defaultwert von 100 genutzt wird    |
|     |                            |                               |                                                                                  |
|     |                            |                               |                                                                                  | 

Die Erzeugung der Clones kann mehrere Stunden in Anspruch nehmen.

### S3: Evaluation Setup Stage
Das Experiment hat die Generations Phase abgeschlossen und befindet sich im *Evaluation Phase Setup* .
In dieser werden die *clone detectors* dem Projekt mitgeteilt.
Dabei können beliebig viele Tools mit aufgenommen und gespeichert werden. Benötigt wird:
- Name des Tools 
- Beschreibung des Tools und dessen Anwendung
- absoluter Pfad zum Installationsordner des Tools
- absoluder Pfad zum Tool-Runner

Bevor die Erkennung gestartet wird kann die *Subsume Tolerance*, die *Unit Recall Required Similarity* und die *Unit Precision Required Similarity* eingestellt werden. Im Paper werden hier verschiedene Angaben(0%, 60%), weshalb vorest nur die Defaultwerte verwendet werden

mit [s] kann der Evaluationsprozess für alle ausgewählten Werkzeuge beginnen.