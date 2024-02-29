#LAB08T2

rekkarit = []

while True:
    rnro = input("Anna rekisterinumero muodossa ABC-123: ")
    if rnro == "":
        break

    rekkarit.append(rnro)

rekkarit.sort()
for rnro in rekkarit:
    print(rnro)