#!/usr/bin/env python3

# Konfiguration
ja_nein = ["ja", "nein"]
richtung = ["links", "rechts", "vor", "zurück"]

# Begrüssung
print("Bevor wir loslegen, brauchen wir zuerst mal einen Namen für dich.")
print("Wie soll dein Name lauten, Astronaut/in? ")
print("Bitte gib einen Namen ein.")
name = input("")
print("")
print("Großartig, " + name + ". Lass uns anfangen mit unserem Abenteuer!")
print("Du erwachst in einem Raumschiff.")
print("Mal sehen ob du den Weg nach draußen finden kannst?")
print("")

# Spielanfang
# Part 1 Die Kabine
print("Das Raumschiff sollten wir erstmal inspizieren.")
antwort = ""
while antwort not in ja_nein:
    antwort = input("Möchtest du deine Kabine verlassen?\nja oder nein\n")
    if antwort == "ja":
        print("Du verlässt deine Kabine. Du siehst den Mond.")
    elif antwort == "nein":
        print('''Du bist für dieses Abenteuer nicht bereit.
Tschüß, ''' + name + ".")
        quit()
    else:
        print("Ich verstehe das nicht.")

# Part 2 Das Raumschiff
antwort = ""
while antwort not in richtung:
    print("Links siehst du ein Alien.")
    print("Rechts befindet sich die Komandozentrale.")
    print("Die Aussenwand des Schiffes befindet sich direkt vor dir.")
    print("Zurück geht's wieder in die Kabine. \n")
    antwort = input('''In welche Richtung gehst du?
links/rechts/vor/zurück\n''')
    if antwort == "links":
        print("Das Alien frießt dich. Schade, " + name + ".")
        quit()
    elif antwort == "rechts":
        print("Du betrittst die Komandozentrale.")
    elif antwort == "vor":
        print("Du stoßt mit deinem Kopf gegen die Wand.")
        print("Bitte nimm einen anderen Weg.")
        print("")
        antwort = ""
    elif antwort == "zurück":
        print("Du gehst zurück in deine Kabine. Gute Nacht, " + name + ".")
        quit()
    else:
        print("Ich verstehe das nicht.")
