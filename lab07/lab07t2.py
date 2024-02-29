#LAB07T2

class Human:
    name = ""
    age = 0
    def __str__(self):
        return "Nimi: " + self.name + ", ikä " + str(self.age) #koko rakenne tähän
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
    
human1 = Human("Adam", 19)
print(human1)
human2 = Human("Eva", 18)
print(human2)