#LAB07T5

class Car:
    brand = ""
    model = ""
    price = 0
    def __str__(self):
        return "auto: " + self.brand + " " + self.model + " " + str(self.price)
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
    def hinta(self): #tehdään yhteishinnalle oma metodi
        return car1.price + car2.price + car3.price 
    
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

print(car1)
print(car2)
print(car3)
print("Autojen hinta yhteensä:", car1.hinta()) #ei ilmeisesti väliä, millä auto-oliolla haetaan hinta-metodi, vastaus sama