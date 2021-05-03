def AnzahlBaeume(Adresse, xSchritt, ySchritt):
    """Zählt die Anzahl von Bäumen bei einer Route 'Right: xSchritt, Down: ySchritt'.
    Die dazugehörige Karte ist unter Adresse gespeichert."""

    File = open(Adresse, "r")
    Lines=File.readlines()
    Anzahl = 0

    for i in range(int(len(Lines)/ySchritt)):
        if Lines[ySchritt*i][(xSchritt*i)%(len(Lines[0])-1)]=="#":
            Anzahl+=1
    return(Anzahl)

Aufgabe1 = AnzahlBaeume("Tag3.txt", 3, 1)
Aufgabe2 = AnzahlBaeume("Tag3.txt", 1, 1)*AnzahlBaeume("Tag3.txt", 3, 1)*AnzahlBaeume("Tag3.txt", 5, 1)*AnzahlBaeume("Tag3.txt", 7, 1)*AnzahlBaeume("Tag3.txt", 1, 2)
print(Aufgabe1)
print(Aufgabe2)
