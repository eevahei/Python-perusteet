#LAB10T2

vuosi = int(input("Anna vuosi: "))
if (vuosi % 400 == 0) or (vuosi % 100 != 0) and (vuosi % 4 == 0):
    print(f"{vuosi} on karkausvuosi!")
else:
    print(f"{vuosi} ei ole karkausvuosi!")