# L04T03

luvut = []

while True:
    luku = input("Anna kokonaisluku: ")

    if luku == "":
        break

    try:
        inLuku = int(luku)
        luvut.append(inLuku)
    except ValueError:
        break

summa = int()

for i in range(0, len(luvut)):
    summa = summa + luvut[i]

print("Lukuja annettu:", len(luvut))
print("Lukujen summa:", summa)