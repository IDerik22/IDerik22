#Erik Teppan

from random import *
import datetime
import os
def clear():
    os.system("cls")
arv = int(input("Mitme tehteni lahendame?\n"))
clear()

def tehe1(arv, oige):
    for i in range (arv):
        n1 = randint(1, 100) #Annab 1-100 suvalise arvu
        n2 = randint(1, 100) #Annab 1-100 suvalise arvu
        tehtevalik = ["+","-"]
        tehe = tehtevalik[randint(0,1)]

        if tehe == "+":
            kokku = n1 + n2
            kokku = str(kokku);
        elif tehe == "-":
            kokku = n1 - n2
            kokku = str(kokku);
        print(n1,tehe,n2,"= ?")
        
        kokku1 = input("Sisesta vastus: ")
        print("───────────")
        if kokku == kokku1:
            print("Õige vastus")
            oige += 1
        else:
            print("Vale")
        print("───────────")
    protsent = oige * 100 / arv
    print(f"{protsent}%")
    print(f"Õiged {oige}/{arv} ")
    
    if protsent >= 90:
        print("Tubli said 5!")
    elif protsent >= 85:
        print("Tubli said 4!")
    elif protsent >= 65:
        print("Tubli said 3!")
    else:
        print("Said 2!")
    
    uuesti = input("Kas soovid uuesti proovida (Ja,Ei)?").upper()
    if uuesti == "JA":
        tehe1(arv, 0)
    elif uuesti == "EI":
        if protsent <= 61:
            print("Harjuta veel ja proovi uuesti!!!")
        elif protsent == 100:
            paev = datetime.datetime.now()        
            print(f"""


                AUKIRI
            ────────────────
            Tubli said 100%
                  {oige}/{arv}
            ────────────────
       {paev}


            
    """)
    
tehe1(arv, 0)
