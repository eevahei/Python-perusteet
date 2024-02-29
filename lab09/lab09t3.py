#LAB09T3

filename = "luvut.txt"
luku = "*"
summa = 0
with open("luvut.txt", "w") as file:
    while luku !="":
        luku = input("Anna kokonaisluku: ")
        if luku !="" and luku.isdigit() == True:
            file.write(str(luku) + "\n")
            summa += 1
            file.close
print("Syötetty", summa, "lukua.")