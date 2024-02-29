#LAB10T4

filename = "C:/ayho.txt"
try:
    file = open(filename, "w", encoding = "UTF-8")
    file.write("Kyllä toimii jeejee!")
    file.close()
    print("Kirjoitus onnistui!")
except: 
    print("Sinulla ei ole oikeuksia tähän tiedostoon.")