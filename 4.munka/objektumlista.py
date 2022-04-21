class nobelDijasok: 
   nev: str
   szulhal: str
   orszagkod: str
   ev :int

   def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.ev = int(adatok)[0]
        self.nev = adatok[1]
        self.szulhal = adatok[2]
        self.orszagkod = adatok[3]

file = open('orvosi_nobeldijak.txt','r',encoding = 'utf-8')
file.readline() 

osszesNobelDijas : list[nobelDijasok] = []


file.readline()
for sor in file:
    egyember = nobelDijasok(sor.strip())
    osszesNobelDijas.append(egyember)

print(len(osszesNobelDijas[10].nev))


for egy in osszesNobelDijas:
    print(egy.ev)

for i in range (int(nobelDijasok)):
    print(i.szulhal)
