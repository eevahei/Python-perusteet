#LAB06T4

pisteet = []
piste = int

for i in range(5):
    while True:
        try:
            piste = int(input("Anna pisteet (väliltä 1-20): "))
            if piste >= 1 and piste <= 20:
                pisteet.append(piste)
                break
            else: 
                print("Anna pisteet väliltä 1-20")
        except ValueError:
            print("Anna pisteet väliltä 1-20")
pisteet.remove(max(pisteet))
pisteet.remove(min(pisteet))
print("Pisteet yhteensä: ", sum(pisteet))