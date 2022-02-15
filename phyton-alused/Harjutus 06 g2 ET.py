##############
#Erik Teppan #
# 15.02.2022 #
#  IT - 21   #
###############

re, sde, irl, ke, erakonnad = 0, 0, 0, 0, 0

with open('Poliitikud.txt', 'r') as minu_fail:
    for rida in minu_fail:
        enimi, pnimi, er, likes = rida.split()
        print ("{0:<15}{1:<12}{2:<7}{3:<30}".format(enimi, pnimi, er, likes))
        if er == "RE":
            re += 1
        elif er == "SDE":
            sde += 1
        elif er == "IRL":
            irl += 1
        elif er == "KE":
            ke += 1

if re > 0:
    erakonnad += 1
if sde > 0:
    erakonnad += 1
if irl > 0:
    erakonnad += 1
if ke > 0:
    erakonnad += 1
    
print(f"\nRE= {re}\nSDE= {sde}\nIRL= {irl}\nKE= {ke}")
print(f"\nErakonnad= {erakonnad}")

