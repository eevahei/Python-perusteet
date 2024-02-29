#LAB07 VALMIIT
#LAB07T1

#luokka pelikortti
class Pelikortti:
    maa = ""
    arvo = 0
    def __str__(self): #liian iso homma, joten tehdään muodostaja
        return self.maa + " " + str(self.arvo)
    def __init__(self, maa ="", arvo = 0):
        self.maa = maa
        self.arvo = arvo
#luodaan viisi erilaista korttia
kortti1 = Pelikortti("Hertta", 13)
print(kortti1)
kortti2 = Pelikortti("Pata", 2)
print(kortti2)
kortti3 = Pelikortti("Ruutu", 6)
print(kortti3)
kortti4 = Pelikortti("Hertta", 7)
print(kortti4)
kortti5 = Pelikortti("Risti", 9)
print(kortti5)