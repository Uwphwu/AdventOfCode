import numpy as np

File = open("Tag8.txt", "r")
Lines = File.readlines()

def Teil1():
    """Zählt den AccumulatorScore für den ersten Loop beginnened bei Line[0] und returnt diesen."""
    running = True
    WarSchonDran = [0]*len(Lines)
    AccumulatorScore = 0
    i = 0

    while running:
        if WarSchonDran[i] == 0:
            WarSchonDran[i] = 1
            Words = Lines[i].split()
            if Words[0] == "acc":
                AccumulatorScore += int(Words[1])
                i +=1
            if Words[0] == "jmp":
                i += int(Words[1])
            if Words[0] == "nop":
                i += 1
        else:
            running = False
    return AccumulatorScore

def PositionenJmpNop():
    """Checkt ob eine Zeile mit 'jmp' oder 'nop' beginnt. Wenn ja, dann wird die Position der Zeile in ein Array geschrieben. Dieses Array wird dann return."""

    Positionen = []

    for i in range(len(Lines)):
        Words=Lines[i].split()
        if Words[0] == "jmp" or  Words[0] == "nop":
            Positionen.append(i)
    return Positionen

def ScorevonLoop(Positionen):
    """Benötigt die Positionen der Lines, welche 'nop' oder 'jmp' beinhalten. Tauscht dann nacheinander ein 'nop' für ein 'jmp' (oder umgekehrt) aus. Berechnet für diese
    neuen Anweisungen den AccumulatorScore und returnt den Score, sobald ein Programm die letzte Zeile erreicht."""

    running = True
    WarSchonDran = [0]*len(Lines)
    AccumulatorScore = 0
    j = 0

    for i in range(len(Positionen)):
        running = True
        WarSchonDran = [0]*len(Lines)
        AccumulatorScore = 0
        j = 0
        while running:
            if j == len(WarSchonDran)-1:
                return AccumulatorScore
            if j<len(Lines) and WarSchonDran[j] == 0:
                WarSchonDran[j] = 1
                Words = Lines[j].split()
                if Positionen[i] == j:
                    if Words[0] == "jmp":
                        Words[0] = "nop"
                    else:
                        Words[0] = "jmp"
                if Words[0] == "acc":
                    AccumulatorScore += int(Words[1])
                    j +=1
                if Words[0] == "jmp":
                    j += int(Words[1])
                if Words[0] == "nop":
                    j += 1
            else:
                running = False

print(Teil1())
print(ScorevonLoop(PositionenJmpNop()))
