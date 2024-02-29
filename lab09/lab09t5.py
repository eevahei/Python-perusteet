#LAB09T5

import random
filename = "lotto.txt"
file = open(filename, "w")

riveja = int(input("Valitse rivien määrä: "))
nrot_rivissa = 7

for i in range(riveja):
    rivi= random.sample(range(1,41), nrot_rivissa)
    file.write(" ".join(map(str, rivi)) + "\n")

file.close()