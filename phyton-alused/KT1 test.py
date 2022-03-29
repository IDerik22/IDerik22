from random import *

# arv1 = int(randint(1,100)
# arv2 = int(randint(1,100)
def tehe1():
    õige = 0
    n1 = randint(1, 100) #Annab 1-100 suvalise arvu
    n2 = randint(1, 100) #Annab 1-100 suvalise arvu
    tehtevalik = ["+","-"]
    tehe = tehtevalik[randint(0,len(tehtevalik)-1)]

    #print(tehe)

    if tehe == "+":
        kokku = n1 + n2
    else:
        kokku = n1 - n2
    print(n1,tehe,n2,"=",kokku)
    
    kokku1 = input("Sisesta vastus: ")
    
    if kokku1 == kokku:
        print("Õige vastus")
    else:
        print("Vale")
 
tehe1()