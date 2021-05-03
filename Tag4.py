import re

File = open("Tag4.txt", "r")
Lines=File.readlines()

#Das ist zu Teil 1 der Aufgabe. Da habe ich noch gedacht, dass ich um das Parsen herumkomme.

def BatchEnds():
    """Bestimmt die Grenzen der Batches und returnt ein Array mit den Startzeilen der Batches und der Schlusszeile des Dokumentes+1."""

    Array=[0]

    for i in range(len(Lines)):
        if Lines[i]=="\n":
            Array.append(i+1)
    Array.append(len(Lines)+1)
    return(Array)

def AnzahlValideDokumente1(Startzeilen):
    """Zählt und returnt die Anzahl an ':' ohne ein 'cid' davor in den einzelnen Batches. Um die Batches zu unterscheiden benötigt die Funktion ein Array mit
    den Startzeilen der Batches und der Schlusszeile des Dokuments+1."""

    Anzahl=0

    for i in range(len(Startzeilen)-1):
        validation=0
        for j in range(Startzeilen[i], Startzeilen[i+1]-1):
            for k in range(3, len(Lines[j])):
                if Lines[j][k]==":"and (Lines[j][k-3]!="c" or Lines[j][k-2]!="i" or Lines[j][k-1]!="d"):
                    validation+=1
        if validation>=7:
            Anzahl+=1
    return Anzahl

#Das ist Teil 2 der Aufgabe. Da kam ich dann nicht mehr um das Parsen herum :(

def Parser(Startzeilen):
    """Schreibt die Daten aus der txt-Datei in ein Array und returnt dieses. Dabei sind die Daten von Person i in Datenarray[i] zusammengefasst.
    Datenarray[i][0] beinhaltet das Geburtsdatum als int, Datenarray[i][1] beinhaltet das Ausstellungsjahr als int, Datenarray[i][2] beinhaltet das Auslaufjahr als int
    Datenarray[i][3] beinhaltet die Größe als int, Datenarray[i][4] beinhaltet die Einheit der Größe als str (falls keine Einheit angegebenen wurde, dann stehen da
    die letzten 2 Ziffern der Größe, das sollte hier aber nicht weiter stören), Datenarray[i][5] beinhaltet die Haarfarbe als str, Datenarray[i][6] beinhaltet
    die Augenfarbe als str und Datenarray[i][7] beinhaltet die LandesID als str"""

    Datenarray=[[0, 0, 0, 0, "", "", "", ""] for i in range(len(Lines))]


    for i in range(len(Startzeilen)-1):
        for j in range(Startzeilen[i], Startzeilen[i+1]-1):
            Words = Lines[j].split()
            for Word in Words:
                if "byr" in Word:
                    Datenarray[i][0]=int(Word[4:])
                if "iyr" in Word:
                    Datenarray[i][1]=int(Word[4:])
                if "eyr" in Word:
                    Datenarray[i][2]=int(Word[4:])
                if "hgt" in Word:
                    Datenarray[i][3]=int(re.findall(r'\d+', Word)[0])
                    Datenarray[i][4]=Word[-2:]
                if "hcl" in Word:
                    Datenarray[i][5]=Word[4:]
                if "ecl" in Word:
                    Datenarray[i][6]=Word[4:]
                if "pid" in Word:
                    Datenarray[i][7]=re.findall(r'\d+', Word)[0]
    return Datenarray

def checkGroesse(Zahl, Einheit):
    """Checkt ob ein Tupel aus Zahl und Einheit zwischen 150cm und 193cm oder 59in und 76in liegt. Returnt True falls ja, sonst False."""
    if Einheit == "cm":
        if 150<=Zahl<=193:
            return True
    if Einheit == "in":
        if 59<=Zahl<=76:
            return True
    return False

def checkHaarfarbe(hcl):
    """Checkt ob ein gegebener String mit einem '#' beginnt und danach aus exakt 6 hex-Ziffern besteht (a-f muss klein geschrieben sein). Returnt 'True' falls alles
    zutrifft, sonst 'False'."""
    if len(hcl[1:])==6:
        if hcl[0]=="#":
            for Buchstabe in hcl[1:]:
                if Buchstabe not in "0123456789abcdef":
                    return False
                else:
                    return True

def AnzahlValideDokumente2(Datenarray):
    Anzahl=0
    for i in range(len(Datenarray)):
        if 1920<=Datenarray[i][0]<=2002:
            if 2010<=Datenarray[i][1]<=2020:
                if 2020<=Datenarray[i][2]<=2030:
                    if checkGroesse(Datenarray[i][3], Datenarray[i][4]):
                        if checkHaarfarbe(Datenarray[i][5]):
                            if Datenarray[i][6]=="amb" or Datenarray[i][6]=="blu" or Datenarray[i][6]=="grn" or Datenarray[i][6]=="brn" or Datenarray[i][6]=="gry" or Datenarray[i][6]=="hzl" or Datenarray[i][6]=="oth":
                                if len(Datenarray[i][7])==9:
                                    Anzahl+=1
    return Anzahl

print(AnzahlValideDokumente1(BatchEnds()))
print(AnzahlValideDokumente2(Parser(BatchEnds())))
