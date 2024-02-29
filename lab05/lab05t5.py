# L05T05

def get_cost(km, kulutus, hinta):
    return (((km / 100) * kulutus) * hinta)

print(("Tulos: {:.2f}".format(get_cost(100, 7.5, 1.88)) + " €"))
print(("Tulos: {:.2f}".format(get_cost(220, 6.9, 1.88)) + " €"))