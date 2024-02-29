# L03T02

luku1 = input("Anna kokonaisluku: ")
luku2 = input("Anna toinen kokonaisluku: ")
luku3 = input("Anna kolmas kokonaisluku: ")
if luku1 > luku2 and luku1 > luku3: 
    print("Suurin: " + luku1)
elif luku2 > luku1 and luku2 > luku3: 
    print("Suurin: " + luku2)
else: 
    print("Suurin: " + luku3)