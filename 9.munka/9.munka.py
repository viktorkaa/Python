#file megnyitása
file = open('ub2017egyeni.txt', 'r',encoding='utf-8')

# lista létrehozása a sorok számára
lista = []

# első sor beolvasása (fejléc, nem csinálunk vele semmit)
file.readline()

#fájl sirainak bejárása 

for sor in file:
     #listához hozzáfűzöm
    lista.append(sor.strip().split(";"))
print(lista) 
