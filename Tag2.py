def Parser (Adresse):
    """Liest die Daten aus der angegebenen txt-Datei aus und returnt 2 Arrays, die die mindest und maximale Anzahl der Buchstaben beinhalten.
    Außerdem returnt die Funktion ein Array mit dem Buchstaben dessen Anzahl beschränkt ist und ein Array mit den Passwörtern"""

    File = open(Adresse, "r")
    Lines = File.readlines()
    ersteZahl = ""
    zweiteZahl = ""
    Wort = ""
    Zahl1 = []
    Zahl2 = []
    Buchstaben = []
    Passwoerter = []

    for i in range(len(Lines)):
        j=0
        while Lines[i][j] != "-":
            ersteZahl = ersteZahl + Lines[i][j]
            j+=1

        j+=1
        while Lines[i][j] != " ":
            zweiteZahl = zweiteZahl + Lines[i][j]
            j+=1

        j+=1
        Buchstaben.append(Lines[i][j])
        j+=3
        while j<(len(Lines[i])-1):
            Wort = Wort + Lines[i][j]
            j+=1

        Zahl1.append(int(ersteZahl))
        Zahl2.append(int(zweiteZahl))
        Passwoerter.append(Wort)

        ersteZahl = ""
        zweiteZahl = ""
        Wort = ""

    return Zahl1, Zahl2, Buchstaben, Passwoerter

def Anzahl1(Zahl1, Zahl2, Buchstaben, Passwoerter):
    """Zählt die Anzahl von richtigen Passwörtern nach Regel 1 und returnt diese. Dafür benötigt die Funktion ein Array mit den minimalen
        zugelassenen Werten, eins mit den maximal zugelassenen Werten, ein mit den beschränkten Buchstaben und eins mit den Passwörtern."""

    gueltigePasswoerter = 0

    for i in range(len(Zahl1)):
        k=0
        for j in range(len(Passwoerter[i])):
            if Passwoerter[i][j] == Buchstaben[i]:
                k+=1
        if Zahl1[i]<=k<=Zahl2[i]:
            gueltigePasswoerter+=1
    return(gueltigePasswoerter)

def Anzahl2(Zahl1, Zahl2, Buchstaben, Passwoerter):
    """Zählt die Anzahl von richtigen Passwörtern nach Regel 2 und returnt diese. Dafür benötigt die Funktion ein Array mit den minimalen
        zugelassenen Werten, eins mit den maximal zugelassenen Werten, ein mit den beschränkten Buchstaben und eins mit den Passwörtern."""

    gueltigePasswoerter = 0

    for i in range(len(Zahl1)):
        if Passwoerter[i][Zahl1[i]-1]==Buchstaben[i] and Passwoerter[i][Zahl2[i]-1]!=Buchstaben[i]:
            gueltigePasswoerter+=1
        if Passwoerter[i][Zahl1[i]-1]!=Buchstaben[i] and Passwoerter[i][Zahl2[i]-1]==Buchstaben[i]:
            gueltigePasswoerter+=1
    return(gueltigePasswoerter)


Zahl1, Zahl2, Buchstaben, Passwoerter = Parser("Tag2.txt")
print(Anzahl1(Zahl1, Zahl2, Buchstaben, Passwoerter))
print(Anzahl2(Zahl1, Zahl2, Buchstaben, Passwoerter))
