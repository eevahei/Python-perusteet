#LAB07T3

class Cat:
    name = ""
    color = ""
    def __str__(self):
        return self.name + ", color: " + self.color
    def __init__(self, name = "", color = ""):
        self.name = name
        self.color = color
    def miau(self):
        return self.name + " says: Meoooooow!"
cat1 = Cat("Kit", "black")
cat2 = Cat("Kat", "white")

print(cat1)
print(cat2)
print(cat1.miau())
print(cat2.miau())