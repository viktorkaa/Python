class Focimeccs:
    fordulo: int
    hazaiGol: int
    vendegGol: int
    hazaiFelidoGol: int
    vendegFelidoGol: int
    hazaiCsapat: str
    vendegCsapat: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.fordulo = int(adatok[0])
        self.hazaiGol = int(adatok[1])
        self.vendegGol = int(adatok[2])
        self.hazaiFelidoGol = int(adatok[3])
        self.vendegFelidoGol = int(adatok[4])
        self.hazaiCsapat = str(adatok[5])
        self.vendegCsapat = str(adatok[6])

    def a ():
            pass

        
f = open("meccs.txt", 'r', encoding='utf-8')
f.readline()
osszesEredmeny: list[Focimeccs] = []

# 1. feladat -------------------------------------------------------------------------------
print("\n----1. feladat----\n")


for sor in f:
    egyMeccs = Focimeccs(sor.strip())
    osszesEredmeny.append(egyMeccs)
print(len(osszesEredmeny))

# 2. feladat --------------------------------------------------------------------------------
print("\n----2. feladat----\n")


forduloInput = int(input("Forduló száma? (1 és 20 között) "))

for egyAdat in osszesEredmeny:
    if egyAdat.fordulo == forduloInput:
        print(egyAdat.hazaiCsapat,"-",egyAdat.vendegCsapat,": ",egyAdat.hazaiGol,"-",egyAdat.vendegGol," (",egyAdat.hazaiFelidoGol,"-",egyAdat.vendegFelidoGol,")",sep='')
        

# 3. feladat --------------------------------------------------------------------------------
print("\n----3. feladat----\n")

keresett_csapat = input("Adjon meg egy csapatnevet!")
Van_e = False
for egyAdat in osszesEredmeny:
    if keresett_csapat == egyAdat.hazaiCsapat or keresett_csapat == egyAdat.vendegCsapat:
      Van_e = True
print(Van_e,"Igen,szerepel benne")


#4. feladat: 1)Határozza meg, hogy a meccs során mely csapatoknak sikerült megfordítani a meccs állását
print("\n----4. feladat----\n")

for egyAdat in osszesEredmeny:
    if egyAdat.hazaiGol > egyAdat.vendegGol or egyAdat.hazaiGol < egyAdat.vendegGol and egyAdat.hazaiFelidoGol or egyAdat.vendegFelidoGol:
        print(egyAdat.hazaiCsapat,',', egyAdat.vendegCsapat,sep =',')

# 5.feladat: Hány gólt lőttek a nyulak vendéggént

print("\n----5. feladat----\n")
gol = 0
for egyAdat in osszesEredmeny:
    if egyAdat.vendegCsapat == 'Nyulak':
        gol += egyAdat.vendegGol
print(gol)

#vagy
#def forditottake(a:int,b:int,c:int,d:int,)--> bool:
    #return (c > d and b > a) or (d > c and a > b)