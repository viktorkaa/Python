#létrehozni az osztályt.
class buszjarat:
    ulesszam : str
    kmszam: str
    meddigmegy = int
    
def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.ulesszam = str(adatok[0])
        self.kmszam = str(adatok[1])
        self.meddigmegy = int(adatok[2])
 
#fájl megnyitása olvasásra
f = open('eladott.txt', 'r',encoding='utf-8')
f.readline()
#objektumlista deklalárása
busz: list[Buszjarat] = []
#fájl sorainak objektummá alakítása
for sor in file:
    busz.append=(buszjarat(sor))
print(len(busz))






  

