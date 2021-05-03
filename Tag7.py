import re

File = open("Tag7.txt", "r")
Lines = File.readlines()
#Teil 1

def ParserTeil1():
    """Liest die Farben aus der Datei aus, schreibt diese in ein 2D Array und returnt dieses. Dabei muss eine Tasche der Farbe Array[i][0] die Farben Array[i][j] für
    j>0 beinhalten"""

    Array = [[] for i in range(len(Lines))]

    for i in range(len(Lines)):
         Words=Lines[i].split()
         Array[i].append(Words[0]+Words[1])
         for j in range(len(Words)):
             if Words[j].isdecimal():
                 Array[i].append(Words[j+1]+Words[j+2])
    return Array

def inBag(Array, Farbe, MoegllicheFarben):
    """Nimmt die oben geparste Liste und returnt dann die Anzahl an möglichen Kombinationen für eine gegebene Farbe. Da die Funktion rekursiv arbeitet, benötigt sie
    am Anfang noch ein leeres Array."""
    for i in range(len(Array)):
        for word in Array[i][1:]:
            if word == Farbe and Array[i][0] not in MoegllicheFarben:
                    MoegllicheFarben.append(Array[i][0])
                    MoegllicheFarben.append(inBag(Array, Array[i][0], MoegllicheFarben))
    for element in MoegllicheFarben: #durch die obige Rekursion schreibt appended sich MoegllicheFarben auch selbst. Diese angehangenen Arrays wollen wir her entfernen
        if type(element) != str:
            MoegllicheFarben.remove(element)
    MoegllicheFarben = list(set(MoegllicheFarben))
    return len(MoegllicheFarben)

print(inBag(ParserTeil1(), "shinygold", []))


#Teil 2
def ParserTeil2():
    """Erstellt ein Dict das jedem Farbregel die entsprechendenen Farben und deren Anzahl zuordnet und returnt dieses"""
    Bags = {}
    for Line in Lines:
        Words = Line.split()
        Farbe = Words[0]+" "+Words[1]
        Bags[Farbe] = re.findall(r"(\d+?) (.+?) bags?", Line)
    return Bags

def AnzahlBags(Farbe):
    """Rechnet die Anzahl der benötigten Taschen für eine gegebene Farbe aus und returnt diese. Um die erste Tasche nicht mitzuzählen, muss man am Ende -1 rechnen"""
    Anzahl = 1+sum(int(Anzahl)*AnzahlBags(naechsteFarbe) for Anzahl, naechsteFarbe in ParserTeil2()[Farbe])
    return Anzahl

print(AnzahlBags("shiny gold")-1)
