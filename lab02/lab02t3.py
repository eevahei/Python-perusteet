# L02T03

name = input("Anna etu- ja sukunimesi: ")
i = name.find(" ")
fname, lname = name.split(name[i])
print("Etunimesi:", fname)
print("Sukunimesi:", lname)
