Pages
 - Landing Page: Login Möglichkeit
   nach erfolgreichem Login zu folgender Page:
   - Challenge Browsing:
      nach Auswählen einer Challenge kommt man auf die Challenge Page
      - Challenge Page

#### Landing Page
Hier soll es die Möglichkeit geben sich einzuloggen oder sich zu registrieren

Backend: Hier muss man man schauen welchen Auth-Mechanismus wir benötigen und was man dann noch so braucht.

#### Challenge Browsing
Hier erhält man eine Übersicht über die ersten x Challenges und kann durch alle Challenges blättern,
am besten mit einer Art Seitenanzahl

Backend: greift auf einen noch zu bauenden Endpunkt `all_challenges` zu und listet die zurückerhaltenen Challenges auf.
         Das Backend holt sich diese Information aus dem `challenges` Table.

#### Challenge Page
Das ist die Sicht, die wir schon haben (`challenge`/`new_challenge`). Hier löst man die Challenge.
Es muss die Möglichkeit geben eine neue Challenge anzufordern und die aktuelle Lösung abzuschicken

Backend: schreibt das Ergebnis in einen noch zu definierend Table `user_challenges`. Hierzu benötigen wir die
         `user_id`, `session_id`, `solution` (die solution funktion als json) und einen aktuellen `timestamp`.

### Übergreifende Elemente
Wir brauchen eine Navigationsbar mit der man jederzeit zur Challenge Browsing zurückkehren kann. In dieser Navigationsbar sollte man auch den Usernamen sehen.