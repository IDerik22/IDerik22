##############
#Erik Teppan #
#17.92.2022  #
#IT - 21     #
##############

#Kuupäev
import locale
from datetime import datetime

dt = datetime.now()
ts = datetime.timestamp(dt)
date_time = datetime.fromtimestamp(ts)

d = date_time.strftime("%d %B, %Y")
print("Inglise keeles:", d)

locale.setlocale(locale.LC_ALL, '')
d = date_time.strftime("%d %B, %Y")
print("Eesti keeles:", d)

#Isikukood
code = input("Sisesta isikukood: ")

date = code[5] + code[6]
month = code[3] + code[4]
 
if code[0] == "1" or code[0] == "2":
    century = "18"
elif code[0] == "3" or code[0] == "4":
    century = "19"
else:
    century = "20"
 
year = century + code[1] + code[2]
 
print ("Sünnipäev on", date+"."+month+"."+year)