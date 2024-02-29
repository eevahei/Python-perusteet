#LAB10T1

import datetime

vuosi = int(input("Anna syntymävuotesi: "))
x = datetime.datetime.now()
ika = x.year - vuosi

def kerro3(ika):
    if ika < 1:
        print("baby")
    elif ika >= 1 and ika < 13:
        print("child")
    elif ika >= 13 and ika <= 19:
        print("teen")
    elif ika >= 20 and ika <= 65:
        print("adult")
    else:
        print("senior")
    
print(kerro3(ika))