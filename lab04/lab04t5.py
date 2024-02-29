# L04T05

fname = input("Anna etunimesi: ")
lname = input("Anna sukunimesi: ")

f_alt = str()
l_alt = str()

for i in range(len(fname)):
    f_alt += fname[0]

for i in range(len(lname)):
    l_alt += lname[len(lname) -1 - i]

print(f_alt, l_alt)