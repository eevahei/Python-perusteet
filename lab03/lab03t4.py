# L03T04

luku = int(input("Pisteet: "))

if luku <= 1:
    print("Arvosana: 0")

elif luku == 2 or luku == 3:
    print("Arvosana: 1")

elif luku == 4 or luku == 5:
    print("Arvosana: 2")

elif luku == 6 or luku == 7:
    print("Arvosana: 3")

elif luku == 8 or luku == 9:
    print("Arvosana: 4")

elif luku >= 10 and luku <= 12:
    print("Arvosana: 5")

else:
    print("Luku ei kelpaa. Yritä uudelleen: Pisteraja 0-12")
