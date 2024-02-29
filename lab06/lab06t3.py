# L06T03

nimet = []
while True:
    nimi = input("Anna oppilaan nimi: ")

    if nimi == "":
        break

    try:
        innimi = str(nimi)
        nimet.append(innimi)
    except ValueError:
        break

print("Oppilaita:", len(nimet)) #nimien määrä
print(", ".join(nimet)) #nimet lueteltuna