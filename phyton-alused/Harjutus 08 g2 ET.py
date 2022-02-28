#Erik Teppan
#16.02.2022
#IT - 21


class Auto:
    #atribuudid
    automark = 'teadmata'
    aasta = 0
    hind = 'teadmata'
    värv = input('Mis värvi soovid?: ')
    
    #meetodid
    def __init__(self,x,y):
        self.automark = x
        self.aasta = y
        
    def kuva(self):
        print('Automark: {} \nKui vana on auto: {} \nHind: {}'.format(self.automark, self.aasta, self.hind))
        
    def lisaHind(self,x):
        self.hind = x
        
    def kuvaHind(self):
        print('Hind: {}'.format(self.hind))
        

uusObjekt = Auto("Volvo", 3)
uusObjekt.lisaHind('10'"€")
värv = print
uusObjekt.kuva()
