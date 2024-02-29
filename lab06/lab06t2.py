#LAB06T2
#valmis

#celsius muutetaan fahrenheitiksi
def celToFah(c):
    return(round((c*1.8)+32, 1)) #yhtälö netistä

#fahrenheit muutetaan celsius-asteeksi
def fahToCel(f):
    return(round((f-32)*5/9, 1)) #yhtälö netistä

print("Tulos:", celToFah(10.0)) 
print("Tulos:", fahToCel(38.0)) 