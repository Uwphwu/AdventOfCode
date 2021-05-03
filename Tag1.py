def Zahlen():
    """Liest die Zahlen aus der Angabe zum ersten Rätsel aus und returnt diese als int Array"""
    File = open("Tag1.txt", "r")
    Werte = File.readlines()
    for i in range(len(Werte)):
        Werte[i] = Werte[i].replace("\n", "")
        Werte[i] = int(Werte[i])
    return Werte

def Tag1Raetsel1 (Zahlen):
    """Checkt für ein gegebenes Array, ob 2 Elemente zu 2020 addiert werden können und returnt gegebenenfalls deren Produkt
        Bei mehreren Möglichkeiten auf 2020 zu kommen wird die erste returnt """
    for i in range(len(Zahlen)):
        for j in range(len(Zahlen)):
            if Zahlen[i]+Zahlen[j]==2020:
                return (Zahlen[i]*Zahlen[j])

def Tag1Raetsel2 (Zahlen):
    """Checkt für ein gegebenes Array, ob 3 Elemente zu 2020 addiert werden können und returnt gegebenenfalls deren Produkt
        Bei mehreren Möglichkeiten auf 2020 zu kommen wird die erste returnt """
    for i in range(len(Zahlen)):
        for j in range(len(Zahlen)):
            for k in range(len(Zahlen)):
                if Zahlen[i]+Zahlen[j]+Zahlen[k]==2020:
                    return (Zahlen[i]*Zahlen[j]*Zahlen[k])

Werte = Zahlen()
print(Tag1Raetsel1(Werte))
print(Tag1Raetsel2(Werte))
