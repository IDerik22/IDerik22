from random import *
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
        print(n1,tehe,n2,"=",kokku)
        
        kokku1 = input("Sisesta vastus: ")
        print("───────────")
        if kokku == kokku1:
            print("Õige vastus")
            oige += 1
        else:
            print("Vale")
        print("───────────")
    print(f"Õiged {oige}/{arv}")
 
tehe1(arv, 0)
