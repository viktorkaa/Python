# osztály létrehozása
class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])

# fájl megnyitása        
file = open('ub2017egyeni.txt', 'r')


noiDb = 0
minSzazalek = 100

# első sort beolvasom, hogy a 2.-ra ugorjon a mutató (az első sor csak fejléc)
file.readline()
for sor in file:
    # egyAdat nevű, Eredmeny típusú objektum létrehozása, a konstruktornak a beolvasott sort adjuk át
    egyAdat = Eredmeny(sor)
    # objektum tulajdonságainak elérése
    print("Neve: ",egyAdat.nev, " ideje: ", egyAdat.ido)
    # hány női versenyző van
    if egyAdat.kategoria == "Noi":
        noiDb = noiDb + 1
    # mennyi a legkevesebb százalék?
    if egyAdat.tavSzazalek < minSzazalek:
        minSzazalek = egyAdat.tavSzazalek

print(noiDb)
print(minSzazalek)        
