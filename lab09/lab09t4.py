#LAB09T4

nimet_dict = {}

filename = "lab09/nimet.txt"
file = open(filename, "r")

for i in file:
    nimi = i[:-1] #pois rivinvaihdot
    nimet_dict[nimi] = nimet_dict.get(nimi, 0) + 1

print(f"Nimien määrä: {len(nimet_dict)}")
print("Kaikki nimet ja määrä:")
for key,value in nimet_dict.items():
    print(f"{key}: {value}")