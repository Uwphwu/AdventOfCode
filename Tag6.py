import numpy as np
from collections import Counter

File = open("Tag6.txt", "r")
Lines=File.readlines()

def BatchEnds():#das ist der Code von Tag 4
    """Bestimmt die Grenzen der Batches und returnt ein Array mit den Startzeilen der Batches und der Schlusszeile des Dokumentes+1."""

    Array=[0]

    for i in range(len(Lines)):
        if Lines[i]=="\n":
            Array.append(i+1)
    Array.append(len(Lines)+1)
    return(Array)

def AnzahlJas(Startzeilen):
    """Fügt die Strings in den einzelnen Batches (entsprechend der Startzeilen) zusammen, entfernt doppelte Jas und sammelt die Anzahl von Jas von jeder einzelnen
    Gruppe in einem Array. Returnt die Summe aller Jas aus diesem Array."""

    AlleJas = [""]*(len(Startzeilen)-1)

    for i in range(len(Startzeilen)-1):
        for j in range(Startzeilen[i], Startzeilen[i+1]-1):
            AlleJas[i] = AlleJas[i] + Lines[j][:-1]

    for i in range(len(AlleJas)):
        AlleJas[i] = "".join(dict.fromkeys(AlleJas[i]))

    for i in range(len(AlleJas)):
        AlleJas[i] = len(sorted(AlleJas[i]))

    return np.sum(AlleJas)

def AnzahlGeteilteJas(Startzeilen):
    """Fügt die Strings zu einzelnen Batches zusammen und zählt die Anzahl der einzelnen Chars in jedem String. Checkt dann, für wie viele Chars die Anzahl mit der
    Länge des Batches übereinstimmt. Returnt diese Anzahl"""

    GeteilteJas = [""]*(len(Startzeilen)-1)
    AnzahlGeteilteJas = 0

    for i in range(len(Startzeilen)-1):
        for j in range(Startzeilen[i], Startzeilen[i+1]-1):
            GeteilteJas[i] = GeteilteJas[i] + Lines[j][:-1]
        AnzahlChars = Counter(GeteilteJas[i])
        for Buchstabe in Lines[j]:
            if AnzahlChars[Buchstabe] == Startzeilen[i+1]-Startzeilen[i]-1:
                GeteilteJas[i] = GeteilteJas[i] + Buchstabe #der Buchstabe wird angefügt, da er sonst mehrfach gezählt wird
                AnzahlGeteilteJas += 1
    return AnzahlGeteilteJas


print(AnzahlJas(BatchEnds()))
print(AnzahlGeteilteJas(BatchEnds()))
