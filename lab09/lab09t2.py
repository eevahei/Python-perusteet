#LAB09T2

filename = "lab09/sukunimet.txt"
with open(filename, "r") as file:
    print(file.read())
with open(filename, "r") as file:
    for line in sorted(file):
        print(line, end="")