personajes = {
    1: 'George Washington',
    2: 'Thomas Jefferson',
    5: 'Abraham Lincoln',
    10: 'Alexander Hamilton',
    20: 'Andrew Jackson',
    50: 'Ulysses S. Grant',
    100: 'Benjamin Franklin'
}

billete = int(input("Introduce la cantidad del billete: "))

if billete in personajes:
    print("El personaje que aparece en el billete es", personajes[billete])

else: 
    print("Error: no existe esa representacion")