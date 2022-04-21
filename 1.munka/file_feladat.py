# FELADAT: Olvasd be a mellékelt fájlt, majd soronként döntsd el, hogy vajon háromszög oldalai-e a számok.
# Kiírni elegendő annyit, hogy igen/nem vagy true/false stb.
# 3 szám akkor alkot háromszöget, ha mindegyik oldala kisebb a másik kettő összegénél.

# függvény deklarálása, ami eldönti, hogy alkotnak-e háromszöget a számot
def haromszoge(a: int, b: int, c: int) -> bool:
    return (a+b > c and a+c > b and b+c > a)

# fájl megnyitása    
f = open("haromszogek.txt", "r")

# üres lista létrehozása, amiben majd egy sor számait tárolom a feldolgozás idejére
szamok = []
for sor in f:
    # beleteszem a sorban található számokat a listába
    szamok = sor.strip().split(" ")
    # meghívom a függvényemet a lista 3 számával (a vizsgálat eredménye logikai érték)
    if (haromszoge(int(szamok[0]), int(szamok[1]), int(szamok[2]))):
        print("Háromszöget alkot.")
    else: print("Nem háromszög.")
   