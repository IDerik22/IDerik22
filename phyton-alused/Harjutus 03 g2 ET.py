###############
# Haarjutus 03#
# Erik Teppan #
# 03.02.2022  #
###############

#Palindroome
palin = input("Sisesta palindroom: ")
print([::-1])

#Tundide ajad
start = input("algusaeg: ")
lopp = input("loppuaeg: ")
#Tükeldus
hh1,mm1 = start.split(":")
hh2,mm2 = lopp.split(":")
#teiselddamine minutiteks
minutid =int(hh1)*60+int(mm1)
minutid2 =int(hh2)*60+int(mm2)
#Absaluutväärtus
ajavahe = abs(minutid-minutid2)
#Teisendamine hh:mm
hh = ajavahe // 60#täisarvuline jagamine
mm = ajavahe % 60 #jääk
#Lause formindamine format abil
print(f"Õpilase päeva pikkus on:  {hh}:{mm}")
print(minutid)

#Email
email = ("erik.teppan@gmail.com: ")
print("@" in email)

#Vandumine
vanne = input("kurat")
vanne = vanne.lower().replace('kurat', '######')
print(vanne)

#Korralik kasutajanimi
nimi =input("Sisesta kasutajanimi: ")
nimi = nimi.strip().capitalized()
print("Tere: "+nimi+"!")
