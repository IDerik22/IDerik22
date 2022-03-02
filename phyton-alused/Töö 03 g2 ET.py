#Erik Teppa
#02.03.2022
#IT-21

#3.1
fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
aasta = input("Sisesta, milliste aastate andmeid on vaja: ")
print(f"{aasta}. aastal oli vastuvõetud{vastuvoetud} [int(aasta[3])-1]")
#3.2
ringid = int(input("sisestage ringide arv: "))
porgand = 0
for i in range(1,ringid+1):
    if i%2==0:
        porgand +=i
print(f"porganite koguarv on {porgand}")
#3.3
fail = open("konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 0:
        print(rida,end="")
    print(rida)
#Rohkem ei jõudnud teen tunnis edasi
