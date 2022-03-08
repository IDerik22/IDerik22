#Erik Teppan
#08.03.2022
#IT-21
#4.1
kuva = int(input("Mitu korda soovid kuvada: "))
def banner(t,k):
    for i in range(k):
        print(t.upper())      
banner("Osta ja Sa ei kahetse!",kuva)
#4.2
def mahlapakkide_arv(kogus):
    arv = round(kogus*0.4/3,0)
    return arv
kogus = int(input("Sisesta õunte kogus: "))
mahlapakkide_arv(kogus)
#4.3
def eelarve(a):
    summa = a*10+55
    return summa
kutsutud = int(input("Mitu inimest kutsutud?: "))
tuleb =  int(input("Mitu inimest tuleb?: "))
print('Maksimaalne eelarve:',eelarve(kutsutud),"€")
print('Minimaalne eelarve:',eelarve(tuleb),"€")
#4.4
kulalised = int(input("Mitu külalist tuleb?: "))
def tervitus(a):
    for i in range(a):
        print('Võõrustaja : "Tere!"')
        print(f"Täna {i+1}. korda tervitada, mõtiskleb võõrustaja")
        print('Külaline: "Tere, suur tänu kutse eest!"')
tervitus(kulalised)
#4.5
def pkarv(a):
    summa=0
    fail = open(a, encoding="UTF-8")
    for i in fail:
        if int(i)<6:
            summa+=int(i)
    return summa
print("Hoiupõrsasse läheb:",pkarv("mündid.txt"),"senti")
#4.6
def kn(a):
    kuud = [",""Jaan","Veeb","Mär","apr"]
    return kuud[a]
print(kn(1))

def kn1(b):
    dd,mm,yyyy=b.split(".")
    print(dd,kn(int(mm)),yyyy)
print(kn1("24.02.1918"))
