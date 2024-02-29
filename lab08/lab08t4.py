#LAB08T4

cars = {
    'ABC-445' : 'Skoda',
    'EGG-879' : 'Audi',
    'TRY-975' : 'Volkswagen',
    'JHK-642' : 'Skoda',
    'HHJ-666' : 'Volvo',
    'CBC-868' : 'BMW',
    'IOS-700' : 'Mercedes-Benz',
    'FLY-579' : 'Saab',
    'OIK-273' : 'Volvo',
    'ESA-073' : 'Audi',
}

for key in sorted(cars):
    print(key, cars[key])