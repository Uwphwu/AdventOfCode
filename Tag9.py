File = open("Tag9.txt", "r")
Lines = File.readlines()

def Parser():
    """Macht aus dem Input ein Array aus ints und returnt dieses."""
    Zahlen = []
    for Line in Lines:
        Zahlen.append(int(Line))
    return Zahlen

def TestZahl(Zahlen, PositionZahl):
    """Checkt ob eine Zahl aus dem Array Zahlen als Summe der vorherigen 25 Zahlen geschrieben werden kann. Dabei muss die Position der Summanden im Zahlenarray
    unterschiedlich sein. Returnt False, wenn es eine solche Zahl gibt. Returnt True, wenn es im gesamten Array (ohne die ersten 25 Zahlen) keine solche Zahl gibt."""
    for i in range(1, 26):
        for j in range(1, 26):
            if i != j:
                if Zahlen[PositionZahl-i]+Zahlen[PositionZahl-j]==Zahlen[PositionZahl]:
                    return False
    return True

def FindeZahl():
    """Geht das geparste Array durch und checkt ob TestZahl() für eine Zahl True returnt. Falls ja, dann returnt die Funktion diese Zahl."""
    for i in range(len(Lines[25:])):
        if TestZahl(Parser(), i+25):
            return Parser()[i+25]

def Aufgabe2 (Zahlen, ZielZahl):
    """Addiert die Zahlen im Array bis diese >= ZielZahl sind. Ist die Summe == ZielZahl, so returnt die Funktion die Summe aus dem maximalen und dem minimalen Summanden.
    Ist die Summe größer als ZielZahl, so setzt die Funktion die Summe auf 0 und beginnt die Summe einen Summanden später von vorn."""

    Summe = 0
    i = 0
    Startzahl = 0
    running = True
    ZsmMenge = []

    while running:
        if Summe < ZielZahl:
            Summe += Zahlen[Startzahl + i]
            i += 1
        elif Summe == ZielZahl:
            for j in range(i):
                ZsmMenge.append(Zahlen[Startzahl + j])
            running = False
        else:
            Startzahl += 1
            Summe = 0
            i = 0
    return min(ZsmMenge) + max(ZsmMenge)

Zahl = FindeZahl()
print(Zahl)
print(Aufgabe2(Parser(), Zahl))
