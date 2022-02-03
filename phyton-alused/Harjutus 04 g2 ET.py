#Harjutus 04
#Erik Teppan
#03.02.2022

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

#Matemaatika
arv1 = int(input("Sisesta esimene arv: "))
arv2 = int(input("Sisesta teine arv: "))
teha = input("Vali tehe:\n 1) liitmine\n 2) lahutamine \n3) korrutamine \n4")

if tehe == 1:
    tehe = arv1 + arv2
    print(vastus)  #Liitmine
elif tehe == 2:
    tehe = arv1 - arv2
    print(vastus1) #Lahutamine

elif tehe == 3:
    tehe = arv1 * arv2 #Korrutamine


#Ruudu kontroll == > < >= !=
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruudugga")
else:
    print("Risttahukas")
    
