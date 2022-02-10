#Harjutus 04
#Erik Teppan
#03.02.2022 
from time import *
from random import *


#kuup
arv = 1
print("Arv   Ruut   Kuup")
for i in range (1,11):
    ruut = arv * arv
    kuup = arv * arv * arv
    print ("{0:<6}{1:<7}{2:<1}".format(arv, ruut, kuup))
    arv = arv + 1


print("──────────────────────────────────────────────────────────")
#Pank
raha = int(input('Kui palju raha?: '))
aeg = int(input ('Mitmeks aastaks?: '))
print("Aasta             Algsumma           Intrest           Aasta lõpuks")
kasum = 0
aeg = aeg + 1
aeg1 = 1
lopuks1 = 0
for i in range (1, aeg):
    intress = round((raha/100*5), 2)
    lopuks = round((raha + intress), 2)
    print ("{0:<18}{1:<19}{2:<18}{3:<30}".format(aeg1, raha, intress, lopuks))
    raha = lopuks
    aeg1 = aeg1 + 1
    kasum = round((kasum + intress), 2)
lopuks1 = round((lopuks1 + lopuks),2)
print("──────────────────────────────────────────────────────────")
print("Summa kokku:",lopuks1,"€")
print("──────────────────────────────────────────────────────────")
print("Kasum:",kasum,"€")
    


print("──────────────────────────────────────────────────────────")
#Arvamismäng
nr = randint(1,50)
loop = 1
kordade_arv = 0
 
print('Arva ära number 1-50')
 
while loop == 1:
    arva = int(input('Sisesta täisarv: '))
    
    if arva == nr:
        kordade_arv += 1
        print('Tubli, pakkumisi kokku: ',kordade_arv)
        loop = 0
    elif arva < nr:
        kordade_arv += 1
        print('Liiga väike (thats what she said)')
    else:
        kordade_arv += 1
        print('Liiga suur (Has no woman ever said)')

print("──────────────────────────────────────────────────────────")
#Viisikud
arv = 1
for i in range (1,101):
    if arv%5:
        pass
    else:
        print(arv)
    arv = arv + 1

print("──────────────────────────────────────────────────────────")
#Pisike korrutustabel
arvv = 1
for i in range(1,11):
    arvv2 = 5 * arvv
    print("5 x",arvv," =", arvv2)
    arvv = arvv + 1

print("──────────────────────────────────────────────────────────")
#Paaris ja paaritu
arvv = 1
for i in range (1,101):
    if arvv%2:
        print(arvv, " ei ole paaris arv")
    else:
        print(arvv, " on paaris arv")
    arvv = arvv + 1
 
print("──────────────────────────────────────────────────────────")     
#Lotot
from random import *
print(randint(11111,99999))

print("──────────────────────────────────────────────────────────")
#Tärnid
for i in range(1,6):          
    for j in range(1,6):       
        print('* ', end='')
    print()

a = int(input("Mitu rida tahad? "))
for i in range(1,a+1):
    print(i * "*")
    sleep(0.1)
print()

a = int(input("Mitu rida tahad? "))
for i in range(1,a+1):
    print("*" * a)
    a-=1
    sleep(0.1)
print()

print("──────────────────────────────────────────────────────────")
#Jalgpalli meeskond
sugu = input("Sisesta sugu: ").upper()

if sugu == "NAINE":
    print("Ei kõlba")
elif sugu == "MEES":
    vanus = int(input("Sisesta vanus: "))
    if vanus < 16 or vanus > 18:
        print("Ei kõlba pt.2")
    else:
        print("Kõlbab")
else:
    print("vigane sugu")

print("──────────────────────────────────────────────────────────")
#Müük
arv1 = int(input("Sisesta toote hind: "))
if arv1 <= 10:
    ale = 0.1
else :
    ale = 0.2   

hind = arv1 - (arv1 * ale)
print("Toote hind on", hind)

print("──────────────────────────────────────────────────────────")
#Juubel
späev = input("Sisesta oma sünnipäev dd.mm.yyyy: ")
dd, mm, yyyy = späev.split(".")
aasta = 2022
vanus = aasta - int(yyyy)
jaak = vanus %5
if jaak == 0:
    print("juubel")
else:
    print("Sul ei ole juubel")

print("──────────────────────────────────────────────────────────")
#Matemaatika
arv1 = int(input("Sisesta esimene arv: "))
arv2 = int(input("Sisesta teine arv: "))
tehe = input("Vali tehe:\n 1) liitmine\n 2) lahutamine \n3) korrutamine \n4) jagamine ")

if tehe == "1":
    tehe = (print(arv1 ,"+", arv2  ,"=",  arv1 + arv2))
    print(tehe)  #Liitmine

elif tehe == "2":
    tehe = (print(arv1 ,"-", arv2 ,"=",  arv1 - arv2))
    print(tehe1) #Lahutamine

elif tehe == "3":
    tehe = (print(arv1 ,"*", arv2 ,"=",  arv1 * arv2)) 
    print(tehe2) #Korrutamine

elif tehe =="4":
    tehe (print(arv1 ,"/", arv2 ,"=", arv1 / arv2))
    print(tehe3) #Jagamine

#Ruudu kontroll == > < >= !=
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruudugga")
else:
    print("Risttahukas")
    
