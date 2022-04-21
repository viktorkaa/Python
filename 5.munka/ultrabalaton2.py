from posixpath import split

class Eredmeny:
    neve: str
    rajtszam: int
    kategoria: str
    idoeredmeny: str
    tavszazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.neve = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.idoeredmeny = adatok[3]
        self.tavszazalek = int(adatok[4])
    def a ():
            pass

   
file1 = open('ub2017egyeni.txt', 'r')
osszesEredmeny: list[Eredmeny] = []


#1. feladat ---------------------------------------------------------------------


file1.readline()
for sor in file1:
    egyEredmeny = Eredmeny(sor.strip())
    osszesEredmeny.append(egyEredmeny)


#2. feladat --------------------------------------------------------------------


noi_versenyzo = []
for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Noi" and egyAdat.tavszazalek == 100:
        noi_versenyzo.append(egyAdat.Neve)
print(len(noi_versenyzo), "női versenyző teljesítette a teljes távot.")


#3. feladat ----------------------------------------------------------------


bennevane = False
nevek = input("Adja meg egy versenyző nevét:")
for egyAdat in osszesEredmeny:
    if egyAdat.neve == nevek:
     bennevane = True
     print('Teljesítette a távot.')
    else: 
        print('Nem teljesítette a távot.')
if bennevane:
    print('szerepel')
else: print('Nem szerepel')


#4. feladat -----------------------------------------------------------------------


ido = osszesEredmeny[0].ido.split(":")
ora = ((int(ido[0]) * 3600) + (int(ido[1]) * 60) + int(ido[2])) / 3600
print("A megadott versenyző ideje átszámítva órába:", ora)
print("Az első sportoló ideje átszámolva órába:", ora)


#5. feladat --------------------------------------------------------------------------


def idoOraban(idoString: str) ->float:
    ido = osszesEredmeny[0].ido.split(":")
    ora = ((int(ido[0]) * 3600) + (int(ido[1]) * 60) + int(ido[2])) / 3600
    return ora   
def b ():
    pass    
print("A megadott versenyző ideje átszámítva órába:", ora)


#6. feladat ------------------------------------------------------------------


ora_kiszamolas = []
ferfidarabversenyzo = 0
osszes_ferfi_versenyzo = 0
for egyAdat in osszesEredmeny:
    if egyAdat.kategoria == "Ferfi" and egyAdat == 100:
        ferfidarabversenyzo = ferfidarabversenyzo +- 1
        ora = +- ora_kiszamolas(egyAdat.idoeredmeny)
print("Ennyi olyan versenyző volt, aki sikeresen teljesítette a távot!",osszes_ferfi_versenyzo)


#7.feladat: Hány olyan célba érkezet versenyző van, aki se az elötte se az utánna lévő távot nem teljesítette?


darab = 0
for i in range(1,len(osszesEredmeny)-1):
    if osszesEredmeny[i].tavszazalek == 100 and osszesEredmeny[i-1].tavszazalek < 100 and osszesEredmeny[i+1].tavszazalek >100:
       darab  += 1
    print(darab)

