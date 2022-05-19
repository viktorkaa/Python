#osztály létrehozása
#bekérés
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
def kerulet(self)-> int            :
        return self.a + self.b + self.c
def d ():
            pass
#Az osztálynak már vannak kész metódusai. 
#A haromszoge() metódus segítségével írasd ki listasoronként, 
#hogy háromszöget alkotnak-e a számok.
for item in lista:
    print(item)
    egyHaromszog = Haromszog(item)
#A lista minden eleméből példányosíts egy egyHaromszog nevű,
# Haromszog típusú objektumot.
class Triangle:
    
  def __init__(self, angle1, angle2, angle3):
    haromszogoldala = 3

  def check_angles(self):
    if self.a + self.b + self.c == 180:
      return True
    else: 
      return False

my_triangle = Triangle(90, 30, 60)

print(my_triangle.haromszogoldal)
print(my_triangle.check_angles)


