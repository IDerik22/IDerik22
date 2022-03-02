#Erik Teppan
#02.03.2022
#IT-21
tulemused = []
tul1 = 0
for _ in range(3):# Küsib 3 korda tulemust
    tulemus1 = int(input("Sisesta tulemus: "))
    tulemused.append(tulemus1)#loeb massiivi
for tul in tulemused:#Tsükkel
    if tul1 < 0:
        tul1 = tul
        continue
    else:
        if (tul > tul1): 
            tul1 = tul
print("─────────────────────────────────────")            
print('Kõrgeim tulemus on:', tul1)#Väljastab kõrgeima tulemuse
test = (round(((tulemused[0] + tulemused[1] + tulemused[2])/3),2))#Arvutab aritmeetilise keskmise
print('Tulemuste aritmeetiline keskmine:',(test))#Prindib aritmeetilise keskmise
print("─────────────────────────────────────")