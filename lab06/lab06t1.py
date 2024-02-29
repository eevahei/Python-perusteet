# L06T01

def showtime(sekunti):
    tunti = sekunti // 3600
    minuutti = (sekunti % 3600) // 60
    sekunti = sekunti % 60
    return f"{tunti:02}:{minuutti:02}:{sekunti:02}" #muotoilu

print(showtime(500))
print(showtime(10000))
print(showtime(121000))