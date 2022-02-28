#Erik Teppan
#16.02.2022
#IT-21

#Ruumala leidmine 
import math

def kuup(a):
    v = a**3
    return v

def kera(b):
    v1 = round(4/3**math.pi*b**3,2)
    return v1

def koonus(c,d):
    v2 = round(1/3**math.pi*c**2*d,2)
    return v2

def silinder(e,f):
    v3 = round(math.pi*e**2*f)
    return v3

print("1.Kuup\n2.Kera\n3.Koonus\n4.Silinder") 
valik = input("Mis kujundit soovid?: ").upper()

if valik == "KUUP":
    arv1 = int(input("Külg: "))
    print(kuup(arv1))
        
elif valik == "KERA":
    b = int(input("Raadius: "))
    print(kera(b))
        
elif valik == "KOONUS":
    c = int(input("Sisesta põhjapindala: "))
    d = int(input("Sisesta raadius: "))
    print(koonus(c,d))
    
elif valik == "SILINDER":
    e = int(input("Sisesta raadius: "))
    f = int(input("Sisesta kõrgus: "))
    print(silinder(e,f))
 
#Tervitus
def minu_tervitus(n,k = "de"):
    if k == "en":
        print('Hi' , n)
    elif k == "et":    
        print('Tere', n)
    else:
        print('Hallo', n)
     
minu_tervitus("Erik")
minu_tervitus("Erik", "et")
minu_tervitus("Erik", "en")



    
    
    