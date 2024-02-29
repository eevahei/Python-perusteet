#LAB10T4

nimet = []

filename = "lab10/names.txt"
try: #saadaan luettua tiedosto
    file = open(filename, "r")
    for nimi in file:
        nimet.append(nimi) #tiedoston nimet listaan
    print("Tiedosto names.txt luettu.")
    print(f"Tiedostossa sijaitsevien nimien määrä: {len(nimet)}")
    nimet.sort(key = len) #järejestellään merkkijonojen mukaan
    print(f"Tiedoston pisin nimi on: {nimet[-1]}")
    file.close()
except: #ei saada luettua tiedostoa
    print("Sinulla ei ole oikeuksia tähän tiedostoon.")
    