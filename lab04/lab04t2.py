# L04T02

ma = int(input("Anna sademäärä maanantailta: "))
ti = int(input("Anna sademäärä tiistailta: "))
ke = int(input("Anna sademäärä keskiviikolta: "))
to = int(input("Anna sademäärä torstailta: "))
pe = int(input("Anna sademäärä perjantailta: "))
la = int(input("Anna sademäärä lauantailta: "))
su = int(input("Anna sademäärä sunnuntailta: "))

viikko = ma + ti + ke + to + pe + la + su

print(f"Sademäärä yhteensä: {viikko}")