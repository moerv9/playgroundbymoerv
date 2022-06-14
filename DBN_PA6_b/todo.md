Erstelle eine Anwendung, die wahlweise entweder in Java, JavaScript oder Python programmiert ist, auf die Datenbank zum Anwendungsszenario zugreift und die folgenden Anwendungsfälle 1-3 umsetzt. 

*Ausgaben der Anwendung sollen auf der Konsole erfolgen.*

- Anwendungsfall 1:
    Die Rückgabe der ersten View aus PA4 soll in einer Methode/Funktion der gewählten Programmiersprache aus der Datenbank abgefragt und ausgegeben werden. 
    Die Ausgabe soll über einen Suchbegriff, den der Anwender über die Konsole eingibt, auf wenige (oder keine) Datensätze gefiltert werden können.
- Anwendungsfall 2: 
    Die Fachlichkeit der ersten Stored Procedure aus PA6a ist in einer Methode/Funktion der gewählten Programmiersprache zu implementieren. 
    Die erforderlichen Eingaben werden in einer Hilfsmethode von der Konsole eingelesen. Diese Hilfsmethode soll in Anwendungsfall 3 wiederverwendet werden.
- Anwendungsfall 3: 
    Die in der Datenbank bereits vorhandene erste Stored Procedure aus PA6a soll nun als solche aus der Programmiersprache einfach aufgerufen werden.
    
Achte auf die Robustheit der Anwendung gegenüber unzulässigen Eingaben (**fehlende oder ungültige Werte**) und **leeren Ergebnissen**. 
Die Anwendung sollte nicht anfällig für sog. SQL-Injections sein.

Lade die erstellte Anwendung in einem Zip-Archiv, das das zugehörige Projekt aus der Entwicklungsumgebung enthält, in den LMS-Kurs hoch.
Achte darauf, dass die hochgeladene Anwendung sich mit **der Datenbank auf dem DBS der FH Kiel verbindet** und die notwendigen Tabellen, Datensätze, Views und Stored Procedures in dieser Datenbank vorhanden sind oder vorab programmatisch angelegt werden.

--TODO:
1. Unser aktuelles DBS auf FH KIEL SERVER hochladen