#osztály létrehozása
#bekérés
print("_-_-_-_1 F E L A D A T_-_-_-_")
class Haromszog:
    a: int
    b: int
    c: int

    def __init__(self,sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])

    def a ():
            pass
#függvény lezárása
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    def b ():
            pass
#függvény lezárása
    def kerulet(self) -> int:
      return self.a + self.b +self.c

    def c ():
            pass
#függvény lezárása
#File beolvasása
print("_-_-_-_2 F E L A D A T_-_-_-_")
file = open('haromszog.txt','r',)
#lista létrehozása
lista = []
#első sor beolvasása
file.readline()
#bejárom a fájl sorait
for sor in file:
    lista.append(sor.strip().split("*"))
#kiiratás
print(lista)
#A kerulet() metódus segítségével írasd ki az egyes háromszögek kerületét.
print("_-_-_-_3 F E L A D A T_-_-_-_")
def kerulet(self)-> int            :
        return self.a + self.b + self.c
def d ():
            pass
#Az osztálynak már vannak kész metódusai. 
#A haromszoge() metódus segítségével írasd ki listasoronként, 
#hogy háromszöget alkotnak-e a számok.
print("_-_-_-_4 F E L A D A T_-_-_-_")
for item in lista:
    print(item)
    egyHaromszog = Haromszog(item)
#A lista minden eleméből példányosíts egy egyHaromszog nevű,
# Haromszog típusú objektumot.
print("_-_-_-_5 F E L A D A T_-_-_-_")
for item in lista:
      print(item)
      egyHaromszog = Haromszog(item)
      print(egyHaromszog.haromszoge())
      print(egyHaromszog.kerulet())

#1) Kérj be a felhasználótól 3 számot(megfelelő adatszerkezetben), 
#majd írd ki neki, hogy háromszöget alkot e!
#egy logikai érték,ami megmondja hogy a háromszög derékszögű e
print("_-_-_-_6 F E L A D A T_-_-_-_")
lista_haromszog = []
for i in range(3):
      szam : int = int(input("Kérem adjon meg egy számot!"))
      lista_haromszog.append(szam)
teljesharomszog = Haromszog(lista_haromszog)
print(teljesharomszog.haromszoge())

def kerulet(self) -> int:
    return self.a + self.b +self.c

def derekszogu(self) -> bool:
    return self.a*self.a + self.b*self.b + self.c*self.c

      



#if a<b+c and b <a+c and c<a+b:
#	print("Háromszöget alkot!")
#else:
#print("Nem alkot háromszöget!")
