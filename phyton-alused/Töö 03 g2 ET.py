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
#3.4 Minu versioon mis töötab teist moodi õigesti
import re;
fpointer = open("jukebox.txt", "r");
for i in fpointer.readlines():
   line= re.findall(r'Journey', i);
   if line:
    print(i);
fpointer.close();
fail1 = input("Sisesta faili nimi: ")
fail3 = fail1;
fail1 = open("jukebox.txt")
lines = fail1.readlines()
for line in lines:
     print(line)
fpointer = open(fail3, "r");
fail2 = input("Mis laulu soovid?: ")
for i in fpointer.readlines():
   line= re.findall(fail2, i);
   if line:
    print("Sinu valitud laul on:",i);    
fpointer.close();
#3.5
fail = open("nimed.txt", encoding="UFT-8")
from datetime import * 
kp = datetime.now().day
for i in fail:
    if jrk==kp:
        print(i)
    jrk +=1
