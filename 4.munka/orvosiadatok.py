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


for sor in file:
 egyember = nobelDijasok(sor) 
print('Nevek:',(egyember.sor))


file.seek(0,0)
nobelCount = 0
file.readline()

for sor in file:
    nobelCount += 1
    print("Összesen ennyi Nóbel díjas van",int(nobelCount))


magyarCount = 0
file.seek(0,0)
file.readline()
darab = 0
for sor in file:
    orszagKod = nobelDijasok(sor.strip())
    if orszagKod.orszagkod == "H":
        magyarCount += 1
print(magyarCount, "Magyar nóbel díjas szerepel a listában.",sep="")

file.seek(0)
file.readline()
elsoNobelDij = 2022
evszamok = []
for sor in file:
    nobelEv = nobelDijasok(sor)
    evszamok.append(int(nobelEv.ev))
    elsoNobelDij = nobelEv

print(' Az első Nobel-díjat' , min(evszamok), '-ben adták ki.', sep='')

file.seek(0)
file.readline()
szerepele = False
for sor in file:
    egy_ember = nobelDijasok(sor.strip())
    if ('Archibald' in egy_ember.nev):
        szerepele = True
if (szerepele):
    print('Szerepel a listában Archibald nevű díjazott.')
else:
    print('Nem szerepel a listában Archibald nevű díjazott.')


file.seek(0)
file.readline()
for sor in file:
    egyember = nobelDijasok(sor.strip())
    evek = egyember.szulhal.split("-")
    if(evek[1] != ""):
        print(egyember.nev,": ", int(evek[1])-int(evek[0]))
