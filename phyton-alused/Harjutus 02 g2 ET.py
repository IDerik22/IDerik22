#Harjutus 2
#Erik Teppan
#01.02.2022
import math

#Kütusekulu arvutamine
liiter = int(input("Sisesta liitrite arv: "))
km = int(input("Sisesta km arv: "))
kulu = liiter/(km/100)
print("100 km läheks",kulu,"liitrit")

#Arvusüsteemid
print("-----------------------------")
arv = int(input("Sisesta täisarv kümnendsüsteemis: "))
print("Kahendsüsttemis:",bin(arv)) #2-ne süsteem
print("Kuuekümendsüsteemis:",hex(arv)) #16-ne süsteem

#Erik Teppan
#01.02.2022

#Ajateisendus
print("-----------------------------")
minutid = int(input("Sisesta minutid: "))
arv1 = minutid//60
arv2 = minutid % 60
print("minutit on : " ,arv1, ":",arv2)

#Erik Teppan
#01.02.2022

#Kolmnurga hüpotenuus
print("-----------------------------")
a = 16
b = 9
valem = (a*a+b*b)
c = round(math.sqrt(valem),2)
print("Hüpotenuus on " ,c)

#Erik Teppan
#01.02.2022

#Rulluisutajad
print("-----------------------------")
kiirus= 29.9 #km/h
aeg =24 #min
round(((kiirus/60)*aeg),2)

#Erik Teppan
#01.02.2022

#Komnurga ümbermõõt
a,b,c = 15,16,18
p= a+b+c
print("Kolmnurga ümbermõõt on:",p)

#Erik Teppan
#01.02.2022

#Toote hinna leidmine
print("-----------------------------")
hind= 36.75
soodus= 0.4
kogus= 3
summa= round(((hind-(hind*soodus))*kogus),2)
print(kogus, "toote hind on",summa, "€")

#Erik Teppan
#01.02.2022

#Pitsa
print("-----------------------------")
hind= 12.90
Jootraha= 0.1
summa= hind * Jootraha
print("Igaüks peab maksma: ",summa, "€")

#Erik Teppan
#01.02.2022




