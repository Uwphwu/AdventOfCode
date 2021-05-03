File = open("Tag5.txt", "r")
Lines=File.readlines()

def BuchstabeToBinary(BuchArray):
    """Wandelt die BoardingNummern aus dem 'FBRL'-Format erst in Binärzahlen und dann in Dezimalzahlen um. Returnt 2 Arrays mit den Reihennummern und Spaltennummern im
    Dezimalsystem."""
    BinArray1=[]
    BinArray2=[]
    for i in range(len(Lines)):
        BinArray1.append(BuchArray[i][:7])
        BinArray1[i]=BinArray1[i].replace("F","0")
        BinArray1[i]=BinArray1[i].replace("B","1")
        BinArray1[i] = int(BinArray1[i], 2)
    for i in range(len(Lines)):
        BinArray2.append(BuchArray[i][7:-1])
        BinArray2[i]=BinArray2[i].replace("L","0")
        BinArray2[i]=BinArray2[i].replace("R","1")
        BinArray2[i] = int(BinArray2[i], 2)
    return BinArray1, BinArray2

def MaxSeatId(Reihen, Spalten):
    """Berechnet aus den Reihen und Spaltennummern die BoardingNummern und returnt die maximale BoardingID"""
    Id=[]
    for i in range(len(Reihen)):
        Id.append(8*Reihen[i]+Spalten[i])
    return max(Id)

def SeatId(Reihen, Spalten):
    """Berechnet aus den Reihen und Spaltennummern die BoardingNummern und sortiert diese. Checkt dann, ob die Liste nur aus aufeinaderfolgenden Zahlen besteht. Falls
    ja, dann return es 'Vollständig'. Falls nein, dann returnt die Funktion die erste fehlende Zahl in der Kette."""
    Id=[]
    for i in range(len(Reihen)):
        Id.append(8*Reihen[i]+Spalten[i])
    Id.sort()
    for i in range(len(Id)-1):
        if Id[i] != Id[i+1]-1:
            return Id[i]+1
    return "Vollständig"


Reihen, Spalten = BuchstabeToBinary(Lines)
print(MaxSeatId(Reihen, Spalten))
print(SeatId(Reihen, Spalten))
