print("----E l s ő feladat----")
#file megnyitása
file = open('ub2017egyeni.txt', 'r',encoding='utf-8')
# lista létrehozása a sorok számára
lista = []
# első sor beolvasása (fejléc, nem csinálunk vele semmit)
file. read()
#fájl sirainak bejárása 
for sor in file:
     #listához hozzáfűzöm
    lista.append(sor.strip().split(";"))
print(lista) 

#2
print("----M á s o d i k feladat----")
van_e = False
for i in lista:
    if "Zsolt":
        van_e = True
if van_e == True:
 print("A listában szerepel a név!")
else:
 print("A listában nem szerepel a név!")
#Hány női induló volt
print("----H a r m a d i k feladat----")
count2 = 0
for i in lista:
    if i[2] =="Noi":
        count2 += 1
print(count2)
#Átlagosan hány % futották le a távnak
print("----N e g y e d i k feladat----")
ossz = 0
for f in range(len(lista)):
    ossz += int(lista[f][4])
print(ossz / len(lista),"%-a az átlag")
#5
print("----Ö t ö d i k feladat----")

















