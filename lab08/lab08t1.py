#LAB8 VALMIIT
#LAB08T1

nimet = []

for i in range(10):
    nimi = str(input("Anna nimi: "))
    nimet.append(nimi)

for nimi in nimet:
    print(nimi)

kaanna = nimet[::-1]
for nimi in kaanna:
    print(nimi)