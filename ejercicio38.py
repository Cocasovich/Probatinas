
lados = int(input("Introduce el numero de lados de tu polígono: "))

nombre = ""

if lados == 3:
    nombre = "Triangulo"

elif lados == 4:
    nombre = "Cuadrilatero"

elif lados == 5:
    nombre = "Pentagono"

elif lados == 6:
    nombre = "Hexagono"

elif lados == 7:
    nombre = "Heptagono"

elif lados == 8:
    nombre = "Octagono"

elif lados == 9:
    nombre = "Nonagono"

elif lados == 10:
    nombre = "Decagono"

if nombre == "":
    print("Error, el programa no soporta ese numero de lados")

else:
    print("Es un", nombre)