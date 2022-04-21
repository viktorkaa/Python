# Írasd ki az összes sort
f = open('adatok.txt', 'r')
for i in range(6):
  print("Sor:", f.readline())
# Olvasd be a fájl első sorát, amely megadja, hogy összesen hány adatsor van.    
f.seek(0.0)
print("Sorok száma:", f.readline())
# Írasd ki egy sorokszama.txt fájlba a sorok számát. 
file2 = open('sorokszama.txt', 'w')
f.seek(0.0)
file2.write(f.readline())
# Írasd ki külön az adatsorokat és külön az összes sorok számát.
f.seek(0.0)
f.readline()
for i in range(5):
    print("A sorok száma a 2. sortól:", f.readline())
# a sorokban levő 3 szám szorzatát írd ki. Csak az adatsorokkal dolgozz!
f.seek(0.0)
f.readline()
sorok = []
for i in range(5):
    sorok = f.readline().strip().split(";")
    szorzat = int(sorok[0]) * int(sorok[1]) * int(sorok[2])
    print("Szorzat:", szorzat)

