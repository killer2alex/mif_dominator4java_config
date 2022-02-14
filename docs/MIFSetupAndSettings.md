# Setup and Settings

In diesem Dokument wird die Vorbereitung zur Verwendung des _MutationInjectionFrameworks_ (im weiteren _MIF_) präsentiert.

Zur Installation wird **nicht** das [Haupt-Repository](https://github.com/jeffsvajlenko/MutationInjectionFramework) empfohlen.
Dieses erhielt seit einiger Zeit keine Updates mehr und einige Bugs, welche auch nicht gekennzeichnet sind.
Im Rahmen dieses Projekt wurde daher ein [Folk](https://github.com/killer2alex/MutationInjectionFramework) erstellt.
Bisher wurden lediglich einige Bugs markiert und Hinweise für die mögliche Fehlersuche hinzugefügt.
Die beiden Versionen unterscheiden sich daher unwesentlich.  

Für eine allgemeine Installationsanweisung verweise ich auf die README-Datei des MIF-Repos.
Im folgenden wird eine spezifische Installationsanleitung im Rahmen dieses Projekts gegeben.
Dabei wird von einem Ubuntu-Server-System ausgegangen, wobei die Anweisungen bei _Ubuntu 20.04.3 LTS_ getestet wurden.

1. **Das MIF herunterladen und im persönlichen Home-Verzeichnis installieren**
    ``` bash
    # Das Git-Repo herunterladen
    cd ~
    git clone git@github.com:killer2alex/MutationInjectionFramework.git

    # Das MIF compilieren
    cd ~/MutationInjectionFramework
    make

    # `astyle` compilieren
    cd ~/MutationInjectionFramework/dependencies/astyle/build/gcc
    make clean
    make

    # `astyle`zugänglich machen ($PATH hinzufügen)
    # Vorsicht! die Verwendung von `sudo` kann Einfluss auf das ganze System nehmen
    # Es können auch alternative Möglichkeiten verwendet werden.
    cd ~/MutationInjectionFramework/dependencies/astyle/build/gcc/bin
    sudo cp astyle /usr/local/bin/astyle
    ```

2. **Txl installieren**
    Dafür wird die letzte Version auf der folgenden Seite heruntergeladen: https://www.txl.ca/txl-download.html und installiert mittels: 
    ```bash
    # Hier den Namen in Abhängigkeit von der Version anpassen!
    cd ~/Downloads/txl10.8.linux6" 
    sudo chmod 770 InstallTxl
    sudo ./InstallTxl 
    ```
3. **Das Stacklimit hochsetzen**
    wird empfohlen, damit Txl richtig läuft. Dies wird mittels `ulimit -Ss 20480000` ermöglicht.

4. **dos2unix installieren**
    mittels `sudo apt install dos2unix`.

Nachdem das MIF erfolgreich installiert wurde, kann es jetzt eingesetzt werden.
