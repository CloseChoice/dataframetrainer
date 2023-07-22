- [ ] Python Environment in Browser laufen lassen -> brauchen wir das wirklich?
  - sieht für mich schon so aus, ansonsten kann man unsere Seite super leicht hacken
  - PyScript! ->
      Nächster Schritt: hole py-click inhalt über API und execute das in "py-click"
      <button id="new-task-btn" class="py-button" type="submit" py-click="test_transform(df_test.copy(deep=True))">
    -> PyScript verträgt sich nicht gut mit React -> ist es möglich die Website einfach ohne React zu machen?=
  - können wir pyodide direkt verwenden? vllt sogar direkt mit react: https://blog.pyodide.org/posts/react-in-python-with-pyodide/
  - Geht das auch einfach ohne React, sondern nur mit HTML, JS und pyscript?
  - Wäre dies eine Möglichkeit, dass immer auf dem Server gerechnet wird: https://github.com/openedx/codejail?
    Im Endeffekt brauchen wir sowieso die Möglichkeit Code sicher auszuführen
  - Um Python Abschnitte zu Text zu machen können wir `compile` benutzen:
    We can pass a multi-line input program to the exec() method with the help of \n. But we need to use the compile() method to compile the program first.
- [x] welche Datenbank
  - ~[x] Mongo db checken -> Nope, das machen wir nicht~
  - [x] Postgres mit Json Spalte -> Testen und Dockerisieren
- [ ] Hypothesis um dynamische Einträge zu generieren/testen
  - [ ] wie bekommen wir hypothesis in pyscript/pyodide? -> Benutzen wir überhaupt PyScript? Einfach über micropip probieren
- [ ] 100 Questions/Answers
  - [x] 1 Datetime Bsp. -> Datetimes sind schwierig darzustellen (.to_json konvertiert diese immer integers, etc.)
  - [ ] 1 einfaches additives Beispiel
  - [x] 1 groupBy Bsp.
  - [x] erstelle Standard zum Anlegen von Tests
  - [ ] vllt. brauchen wir das hier gar nicht: erstelle Skript um anschließend Tests ins Datenbankformat zu bekommen (escape " -> '', alles muss in eine Zeile)! Wir könnten evtl. direkt den code compilen und per json verschicken! Aber eine DB ist vllt doch besser, dann hat man Sachen auch historisiert!
  - [ ] lade Daten in die Datenbank (hierzu: autoincrement id)

Nützliches:
 - https://wiki.selfhtml.org/wiki/JavaScript/Tutorials/DOM/Einbindung_in_HTML

next step:
 - [x] 1 additives Beispiel -> checke ob Flask damit funktioniert -> Frontend bauen!
 - [x] lasse expected anzeigen
 - [ ] css header/css trenne
 - [x] Konzept für Challenges
 - [x] example 2 ist falsch. Für generisches Template von Python Functions müssen wir auf jeden fall checken ob pd.DataFrame(json.loads(df.to_json())) funktioniert
 - [x] Flask Backend dockerisieren und in docker-compose aufnehmen
 - [ ] evtl hypothesis teil in pyscript/frontend auslagern
 - [ ] Save bei F5


Nice to Haves:
- [ ] CI/CD
- [ ] https -> so wie bei pegsolitairetrainer.com
  - [ ] https für Flask?
  - [ ] Frontend
  - [ ] Userdata Backend
- [ ] "Stay logged in"-Feature
- [ ] Responsive Design
- [ ] Komplett dockerisiert bzw. Kubernetes
- [ ] Whitepaper über Prediction!

- Backend
  - [ ] Postgres Docker Container: bisher sind die Informationen nur im Container gespeichert und dort von Hand eingetragen. Sinnvoll wäre ein Format in dem man die Aufgaben ablegt und ein Skript, das dann automatisch in diesen
  Container reinschreibt.
  - [x] Womit serven wir die Ergebnisse aus dem Docker Container? -> Flask, da wir auch noch Beispiele generieren müssen + das Ergebnis generieren können müssen.

- Anderes
  - [ ] Datetimes sind schwierig zu erzeugen und schwierig zu testen, da df.to_json() diese in unix timestamps konvertiert.

- [x] Text aus editor auslesen
- [x] Editor ist neues Eingabefeld
- [x] Code-Highlighting
- [x] Breite anpassen
- [x] Editor hat Standardchallenge
- [ ] im Editor definierte ausgaben werden angezeigt, wie ein Jupyter Notebook
- [x] Ausgabe von python returns irgendwohin
- [ ] Ausgabe von prints irgendwohin (später dann wie jupyter notebook) (schaue hierzu auf write_stdout von py-script stdio.ts und pyterminal.ts)


Basic verständnis von svelte:
 - [x] wo lege ich js files ab mit utils
 - [x] Komponente kreieren und reusen
 - [x] Kombiniere mehrere Komponenten miteinander!

ELO:
 - [ ] wir brauchen vermutlich einen regelmäßigen job, der das elo einzelner Challenges updated, ich denke, das geht nicht live, da wir sonst 
       in errors laufen.
Dokumentation:
 - [ ] dokumentiere wie tabellen erstellt werden
 - [ ] dokumentiere wie das elo system funktioniert


