from collections import Counter

File = open("Tag10.txt", "r")
Lines = File.readlines()

def SortierteZahlen():
    """Schreibt die Zahlen aus dem Input in ein Array und sortiert dieses. Außerdem steht am Anfang die 0 in diesem Array und am Ende die höchste Zahl aus dem Input +3.
    Das Array wird returnt."""
    Zahlen = [0]
    for Line in Lines:
        Zahlen.append(int(Line))
    Zahlen.sort()
    Zahlen.append(Zahlen[-1]+3)
    return Zahlen

def Aufgabe1(Zahlen):
    """Zählt die Anzahl von Elementen in einem übergebenen Array, die die Differenz 1 zu ihrem Vorgänger haben. Das selbe macht es mit Elementen die Differenz 3 haben.
    Diese beiden Anzahlen werden dann am Ende multipliziert und returnt"""

    EinserSchritt = 0
    DreierSchritt = 0

    for i in range(len(Zahlen)-1):
        if Zahlen[i+1]-Zahlen[i] == 1:
            EinserSchritt += 1
        if Zahlen[i+1]-Zahlen[i] == 3:
            DreierSchritt += 1
    return EinserSchritt*DreierSchritt

def Aufgabe2(Zahlen):
    """Erstellt ein dict das für jeder Zahl in einem Array die Anzahl an Möglichkeiten diese Zahl zu erreichen zuordnet. Returnt die Anzahl an
    Möglichkeiten die höchste Zahl zu erreichen."""

    AnzahlNZuErreichen = {0:1}
    for Zahl in Zahlen:
        AnzahlNZuErreichen[Zahl] = AnzahlNZuErreichen.get(Zahl - 3, 0) + AnzahlNZuErreichen.get(Zahl - 2, 0) + AnzahlNZuErreichen.get(Zahl - 1, 0)

    return AnzahlNZuErreichen[Zahlen[-1]]


Zahlen = SortierteZahlen()
print(Aufgabe1(Zahlen))
Zahlen.remove(0)
print(Aufgabe2(Zahlen))
