# dominator4java mutation

Ermöglicht den Benchmark des dominator4java mittels des *MutationInjectionFrameworks* (im Folgenden MIF) von J. Svajlenko und C. K. Roy.

## Install
Das [Repository](https://github.com/jeffsvajlenko/MutationInjectionFramework) für das `MutationInjectionFramework` stellt die Grundlage für meine Arbeit dar. 

Für die Installation des MIF kann das Install-script (momentan noch mit `invoke`) verwendet werden. Damit das MIF jedoch auch funktioniert, müssen noch einige Programme mit der Hand erledigt werden. Das folgende Vorgehen ist für eine frische Ubuntu-Version gedacht.

### Txl installieren

Txl wird am besten manuell installiert. Dafür wird die letzte Version auf der folgenden Seite heruntergeladen: https://www.txl.ca/txl-download.html und installiert mittels:

```shell
$ cd ~/Downloads/txl10.8.linux6"  # oder eine neuere Version
$ sudo chmod 770 InstallTxl
$ sudo ./InstallTxl 
```
### dos2unix installieren

Das Programm `dos2unix` wird vom MIF benötigt und wird installiert mittels:
```shell
sudo apt-get install dos2unix
```
### Stacklimit hochsetzen

Damit Txl richtig läuft wird empholen das Stacklimit hochzusetzen. Dies wird 
mittels des folgenden Befehls getan:
```shell
ulimit -Ss 20480000
```

## Verwendung/Usage

Nach dem das MIF erfolgreich installiert wurde, kann es jetzt eingesetzt werden. Dafür wird normalerweise die `MutationInjectionFramework/run`-Datei in der Bash ausgeführt. Nach der Installtion ist diese überall mittels des Befehls `mifrun` verfügbar.

Nachdem das MIF-Tool gestartet wurde kommen wir zum Root-Menü, in dem wir wir entweder ein Experiment laden oder ein neues Experiment erstellen können.
!(Root-Menü)[docs/assets/MIF_S0_Root_Menu.png].

Das MIF-Tool durchläuft für die Evaluation eines *clone detectors* fünf Schritte. Bei drei dieser Schritte (1, 3, 5) wird angehalten um weitere Informationen zum Ablauf zu erhalten. Genauere Informationen zu den einzelnen Schritten ist in der Readme vom `Reproduce_Paper_2019`-Ordner zu finden. In diesem wurde versucht die Resultate des Papers (*The Mutation and Injection Framework: Evaluating Clone Detection Tools with Mutation Analysis*)[https://www.researchgate.net/publication/332703085_The_Mutation_and_Injection_Framework_Evaluating_Clone_Detection_Tools_with_Mutation_Analysis] zu wiederholen und das MIF-Tool wurde an verschiedenen Schritten "eingefroren" um die Arbeit und den Einstieg in das MIF-Tool zu vereinfachen.

# Reproduktion des Papers von 2019

Es wurde das Vorgehen aus dem Paper (*The Mutation and Injection Framework: Evaluating Clone Detection Tools with Mutation Analysis*)[https://www.researchgate.net/publication/332703085_The_Mutation_and_Injection_Framework_Evaluating_Clone_Detection_Tools_with_Mutation_Analysis] emuliert und verschiedene Stadien in den sich das MIF-Tools befindet werden festgehalten. Dabei gilt:
- Bei allen Eperimenten handelt es sich um *Automatic clon synthesis experiments* in der Sprache *Java* welche die vom MIF zur Verfügung gestellten repositories (vgl. `MutationInjectionFramework/data/repositories/java`)nutzen.
- Als System wurde 
- Der momentane Stand eines Experiments wird mittels der Kombination `SX` dargestellt, wobei `S` für Stage steht und `X` entweder 1, 3 oder 5 ist und den momentanen Zustand angibt.
- Das System wird mit `Empty` oder `Ipscan` angegeben welche auch vom MIF übernommen wurden (vgl. `MutationInjectionFramework/data/systems/java/`).
- Der untersuchte Clonetyp wird als nächstes angegeben. Dies kann *Func* (für Functions) und *Block* sein.
- Wurde ein bestimmtes Werkzeug für die Evaluation verwendet wird dies danach im Namen mit angegeben.

## Phasen (**S**tages)
### S1: Generation Stage
Das Experiment wurde frisch erstellt; die notwendigen Informationen wurden angegeben und der Repository und System wurden vom MIF bereinigt. Beim laden wird die Phase 3 (S3) angeboten.



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

Bevor die Erkennung gestartet wird kann die *Subsume Tolerance*, die *Unit Recall Required Similarity* und die *Unit Precision Required Similarity* eingestellt werden. Im Paper werden hier verschiedene Angegeben, weshalb vorest nur die Defaultwerte verwendet werden

mit [s] kann der Evaluationsprozess für alle ausgewählten Werkzeuge beginnen.

### S4
Stellt nur ein Zwischenschritt dar. Das Experiment wurde whärend der *Evaluation Phase* unterbrochen und kann nun fortgesetzt werden.


### S5 Evaluation Results Stage
Das Experminent hat die *Evaluation Phase* abgeschlossen und die Daten können ausgelesen oder gespeichert werden.

## Benutzung von Tool-Runner

Um die Kommunikation zwischen dem MIF und dem *clone detector* zu organisieren wird ein ToolRunner verwendet. Mehr Informationen dazu ist in der [Readme des MIF-Repos](https://github.com/jeffsvajlenko/MutationInjectionFramework#tool-runners) zu finden.


### Was ist mit `> /dev/null 2> /dev/null`?

Nachdem der ToolRunner gestartet wurde muss die nächste Ausgabe zur Kommandozeile der absolute Pfad zu den Formatierten Daten sein, welche vom MIF dann ausgewertet werden. Deshalb wird jede mögliche andere Ausgabe in die Komandozeile in das Null-Gerät (`/dev/null`) umgeleitet.
Für mehr Infos, siehe: https://qastack.com.de/ubuntu/350208/what-does-2-dev-null-meaon

### Wie soll die Formatierte Datei für das MIF aussehen?
In der Enddatei -- welche vom ToolRunner an das MIF zurückgegeben wird -- müssen die Clones im Format 'srcfile1,startline1,endline1,srcfile2,startline2,endline2' angegeben sein. Ein Beipsiel wäre:
/Path/to/File1.java,5,10,/Path/to/File2,20,25
/Path/to/File2,20,25,/Path/to/File3,50,55

Die Dateipfade werden dabei am besten absolut angegeben.