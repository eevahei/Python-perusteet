#LAB08T3

arvosanat = []

while True:
    arvosana = input("Anna arvosana (1-5): ")
    try:
        arvosana = int(arvosana)
    except:
        break
    arvosanat.append(arvosana)
    if arvosana > 5 or arvosana <= -1:
        print("Anna kelvollinen arvosana")
        arvosanat.pop()


print("Annoit:", len(arvosanat), "arvosanaa")
keskiarvo = sum(arvosanat) / len(arvosanat)
print("Arvosanojen keskiarvo on:", keskiarvo)