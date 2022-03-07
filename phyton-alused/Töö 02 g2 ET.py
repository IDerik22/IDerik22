#Erik Teppan
# 02.03.2022
#IT-21

import random

#2.1
def aratus():
    korrad = int(input("Mitu korda on vaja äratada: "))
    while korrad >= 1:
        print("Tõuse ja sära!")
        korrad += -1
aratus()

#2.2
def mure():
    ringid = int(input("Mitu ringi läbiti: "))
    porgandid = 0
    while ringid >= 1:
        if ringid%2 == 0:
            porgandid += ringid
        ringid += -1
    print(f"porgandite koguarv on {porgandid}")
mure()

#2.3
def taringud():
    kogus = int(input("Mitut täringut lähed vaja: "))
    for q in range(kogus):
        vastus = random.randint(1,6)
        print(vastus)
taringud()

#2.4
def male():
    taisarv = int(input("Mitmes ruut: "))
    i = 1
    terad = 1
    while i <= taisarv-1:
        terad *= 2
        i += 1
    print(f"nisu teri {taisarv}. ruudu eest: {terad}")
male()
