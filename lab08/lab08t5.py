#LAB08T5

import random 

def lotto():
    nrot = 7
    rivi = random.sample(range(1,40), nrot)
    print(rivi)

print(lotto())