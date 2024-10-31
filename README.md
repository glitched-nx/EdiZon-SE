# EdiZon SE

Dieser Fork basiert auf der Grundlage von EdiZon 3.1 Nightly. Die vorgenommenen Änderungen betreffen hauptsächlich den Aspekt des Spielspeicher-Hackings.

Hier sind die hinzugefügten Funktionen:
1. Bereichssuche.
2. Vergleich mit vorherigem Wert bei der Suche.
3. Lesezeichen für gefundene Speicherorte.
4. Geschwindigkeitsverbesserung, um kleine Ganzzahlen bei der ersten Suche praktikabel zu machen.
5. Lesezeichen passen sich an die sich ändernde Haupt- und Heap-Startadresse bei erneutem Spielstart an. Lesezeichen mit angehängter Zeigerkette aktualisieren die Speicheradresse dynamisch, wenn die Kette in eine gültige Speicheradresse aufgelöst werden kann.
6. Extrahiere Speicheradressen aus dmnt-Cheat-Codes und füge sie dem Lesezeichen zur Erkundung des Speicherorts hinzu.
7. Rebase-Funktion, um potenzielle Zeigerketten aus dmnt-Cheat-Codes zu extrahieren, die für frühere Versionen des Spiels erstellt wurden.
8. In-App-Zeigerkettensuche für Adressen im Lesezeichen.
9. Exportiere Dump zur PC-App (abgeleitet von Pointersearcher 0.4) für eine leistungsfähigere Zeigerkettensuche.
10. Importiere Suchergebnisse der PC-App zur Validierung und Prüfung.
11. Erstelle dmnt-Cheat-Codes aus gefundenen Zeigerketten.
12. Möglichkeit, dmnt vom Spielprozess zu trennen.
13. Hinzufügen/Entfernen von Bedingungstasten zu Cheat-Codes.
14. Mehrzielsuche für schnellere Konvergenz, wenn die Datenstruktur bekannt ist.
15. Speicher-Explorer, um die Speicher-Datenstruktur zu betrachten, Zeigerketten zu folgen und Zeigerketten zu bearbeiten.

PS: Bitte besuche https://github.com/tomvita/EdiZon-SE/wiki für Anleitungen zur Nutzung der App.

Um eine gemeinsame Basis für den Support zu schaffen, starte bitte mit einem sauberen Boot mit der neuesten Atmosphère-Version und nur den Sigpatches, die zum Ausführen des Spiels benötigt werden, sowie den neuesten Releases von https://github.com/tomvita. Bitte gib die URL an, von der Du heruntergeladen hast. Keine zusätzliche Software, es sei denn, sie steht im Zusammenhang mit dem Thema der Diskussion.

Für Unterstützung bei der Nutzung von EdiZon SE tritt meinem Discord-Server bei: https://discord.gg/bEFfp7MZUD

Die ursprüngliche Funktionalität von Edizon für Spielstände ist verfügbar, wenn es ohne laufendes Spiel gestartet wird.

<p align="center"><img src="https://user-images.githubusercontent.com/68505331/94226638-aa5aad00-ff2a-11ea-8b39-151c41bbc774.jpg"><br />
<a href="https://github.com/tomvita/EdiZon-SE/releases/latest"><img src="https://img.shields.io/github/downloads/tomvita/EdiZon-SE/total.svg" alt="Latest Release" /></a>
</p>

Der Teil der Speicherverwaltung und -bearbeitung des Originals ist größtenteils unverändert, außer dass Du die Speicherfunktionalität nur siehst, wenn Du eintrittst, wenn kein Spiel läuft, und nur das letzte Spiel angezeigt wird, wenn es ein letztes Spiel gab. Um alle Spiele zu sehen, gehe in den "Cheat"-Modus, wenn kein Spiel läuft, und beim nächsten Start von EdiZon SE werden alle Spielstände angezeigt.

# Ursprüngliche Funktionalität vorhanden, aber nicht weiterentwickelt:

- **Speicherdateiverwaltung**
  - Extraktion von Spielständen.
  - Einspeisung von extrahierten Spielständen (Deine eigenen und die Deiner Freunde).
  - Hochladen von Speicherdateien direkt auf https://anonfile.com.
  - Stapelweise Extraktion aller Speicherdateien aller Spiele auf dem System.
- **Speicherdateibearbeitung**
  - Einfach zu bedienende, skriptbare und leicht erweiterbare On-Console-Speicherbearbeitung.
    - Unterstützung für Lua- und Python-Skripte.
  - Integrierter Speicher-Editor-Updater.

# Installation

1. Lade die neueste Version von https://github.com/tomvita/EdiZon-SE/releases/latest herunter.
2. Entpacke die heruntergeladene ZIP-Datei, lege die Dateien auf die SD-Karte Deiner Nintendo Switch und lasse die Ordner zusammenführen.
3. Verwende eine kostenlose Open-Source-CFW wie [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere), um das hbmenu zu starten und EdiZon von dort aus zu starten.
   1. Wenn Du den Cheat-Manager verwenden möchtest, musst Du unbedingt [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere) verwenden, da nur deren Cheats unterstützt werden.
   2. Für das beste Erlebnis öffne die Datei `/atmosphere/system_settings.ini` und ändere `dmnt_cheats_enabled_by_default = u8!0x1` zu `dmnt_cheats_enabled_by_default = u8!0x0`. Wenn die Datei nicht existiert, kannst Du die Vorlage aus /atmosphere/config_templates/system_settings.ini kopieren und die Zeile ändern, denke daran, das ";" davor zu entfernen.

# Fehlerbehebung

Es gibt einige Dinge, die Deine Switch-Umgebung beeinflussen.
1. Atmosphère-Version. Alle Versionen vor 3.8.17 sind nicht kompatibel mit atm 19.
2. Wie Du bootest. Ich verwende fusee primary. Versuche, fusee primary zu verwenden, bis die Fehlerbehebung abgeschlossen ist.
3. Atmosphère- und Sept-Verzeichnisse, die Inhalte von vorherigen Installationen enthalten. Wenn Du diese beiden Verzeichnisse nicht gelöscht hast, bevor Du die neuen kopierst, können Überreste von vorherigen Installationen Probleme verursachen.
4. SD-Karten-Korruption. Wenn Du exfat verwendest, ist Korruption nur eine Frage der Zeit.
5. Sysmodule, die im Hintergrund laufen. Sysmodule können EdiZon SE stören. Verwende den Sysmodule-Manager in EdiZon SE (verfügbar ab 3.8.16), um alle Sysmodule zu deaktivieren und zu sehen, ob das Problem dadurch gelöst wird.
6. Gelöschte EdiZon-Dateien. Du kannst alles in \switch\edizon löschen, aber wenn Du einige löschst und andere behältst, kann EdiZon in einer Endlosschleife stecken bleiben, wenn es nach den gelöschten Dateien sucht. Um zu wissen, was Du sicher löschen kannst, kannst Du es durch Ausprobieren lernen oder einfach alles löschen und von den Standardeinstellungen aus neu starten.
7. Fehlende /atmosphere/config/system_settings.ini. Wenn Du diese Datei nicht hast, sind alle Cheat-Codes standardmäßig aktiviert und die meisten Cheat-Codes sind nicht dafür ausgelegt, alle gleichzeitig aktiviert zu sein. Wenn Du keine Ahnung hast, wie Du diese Datei erstellen kannst, bietet der Sysmodule-Manager an, sie für Dich zu erstellen (verfügbar ab 3.8.17) mit Code standardmäßig ausgeschaltet und Umschaltdatei-Erstellung aktiviert.
8. Schlechte Datei in /atmosphere/config/. Stelle sicher, dass Du weißt, was Du tust. Alles, was hier falsch ist, kann die Funktion von Atmosphère erheblich beeinträchtigen.
9. Der Cheat-Code, den Du verwendest. Überprüfe die Cheat-Datei, die Du verwendest. Deaktiviere alle Cheats, bevor Du das Spiel startest. Du kannst EdiZon SE schnell aufrufen, während das Spiel noch startet, um zu überprüfen, ob alle Cheats deaktiviert sind. Nachdem das Spiel an der Stelle gestartet ist, an der Du die Cheats verwenden möchtest, überprüfe, welcher möglicherweise das Problem verursacht. Du solltest jeden Cheat-Code verdächtigen, bis Du ihn gründlich getestet hast.

## So schaltest Du das Sysmodule aus
1. Starte EdiZon SE ohne Spiel. Drücke L. Drücke Y. Verwende A, um Sysmodule auszuschalten. Drücke "Home", um zum Startbildschirm zurückzukehren.

# Kompilierung

1. Klone das EdiZon SE-Repo auf Deinen Computer mit `git clone https://github.com/tomvita/EdiZon-SE`.
2. Lade devkitA64 herunter und installiere es. Es wird mit der [devkitPro](https://devkitpro.org) Toolchain gebündelt.
3. Verwende den Pacman-Paketmanager, der mit devkitPro geliefert wird, um libNX, Portlibs (`switch-portlibs`) und freetype2 (`switch-freetype`) herunterzuladen und zu installieren.
4. Der Rest der Kompilierung erfolgt mit dem `make`-Befehl.
5. Du musst dies von libnx zurücksetzen oder die Quelle selbst aktualisieren aufgrund dieses [Commits](https://github.com/switchbrew/libnx/commit/637dd12b2df58c469d4e87a48aa3ebf0bc359766).

# Discord

Für Unterstützung bei der Nutzung von EdiZon SE tritt meinem Discord-Server bei: https://discord.gg/bEFfp7MZUD
oder für Unterstützung bei der Erstellung von Speicher-Editor-Konfigurationen und Skripten tritt dem ursprünglichen EdiZon-Server auf Discord bei: https://discord.gg/qyA38T8

# Credits

Danke an...

- [devkitPro](https://devkitpro.org) für ihre großartige Toolchain!
- [3096](https://github.com/3096) für das Speichern und Laden von Spielständen ([save dumping/injecting](https://github.com/3096/nut)).
- [Bernardo Giordano](https://github.com/BernardoGiordano) für einige Codes von [Checkpoint](https://github.com/BernardoGiordano/Checkpoint).
- [SwitchBrew](https://switchbrew.org/) für den [Homebrew Launcher](https://github.com/switchbrew/nx-hbmenu) GUI und den gemeinsamen Schriftcode.
- [thomasnet-mc](https://github.com/thomasnet-mc/) für den größten Teil des Speicher-Backup- und Wiederherstellungscodes und das Updater-Skript.
- [trueicecold](https://github.com/trueicecold) für Batch-Backups und den nur editierbaren Modus.
- [onepiecefreak3](https://github.com/onepiecefreak3) für den EdiZon-Debugger und viele Überarbeitungen der Implementierungen.
- [Jojo](https://github.com/drdrjojo) für die Travis CI-Konfiguration und den Konfigurations-Ersteller.
- [Ac_K](https://github.com/AcK77) für die Hilfe bei den serverseitigen Update-Skripten und der EdiZon-Speicher-Website.
- [jakibaki](https://github.com/jakibaki) für ihre massive Hilfe bei der Implementierung der RAM-Bearbeitung und sys-netcheat, die als Inspiration diente.
- [SciresM](https://github.com/SciresM) für den aarch64 hardwarebeschleunigten SHA256-Code, seine Implementierung der Atmosphère-Cheat-Engine und seine Unterstützung während der Entwicklung.
- **kardch** für das schöne aktuelle Icon.
- **bernv3** für das schöne alte Icon.
- **Alle Konfigurations-Ersteller** für das Leben dieses Projekts!

- [nlohmann](https://github.com/nlohmann) für seine großartige JSON-Bibliothek.
- [Martin J. Fiedler](https://svn.emphy.de/nanojpeg/trunk/nanojpeg/nanojpeg.c) für die nanojpeg JPEG-Dekodierungsbibliothek.
- [Lua](https://www.lua.org/) für ihre Skriptsprache.
- [Python](https://www.python.org/) und [nx-python](https://github.com/nx-python) für ihre Skriptsprache bzw. ihren Python-Port für die Switch.

  <br>
  <p align="center"><img src="https://www.lua.org/images/logo.gif">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"><p>
