#LAB09T1

filename = "sukunimet.txt"
file = open(filename, "w")
nimi = "*"
while nimi !="":
    nimi = input("Anna sukunimi: ")
    if nimi !="":
        file.write(nimi + "\n")
file.close()