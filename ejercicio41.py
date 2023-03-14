
lado_1 = float(input("Introduce el lado 1 del triangulo: "))
lado_2 = float(input("Introduce el lado 2 del triangulo: "))
lado_3 = float(input("Introduce el lado 3 del triangulo: "))

if lado_1 == lado_2 == lado_3:
    print ("Es un triangulo equilatero")

elif lado_1 != lado_2 != lado_3:
    print ("Es un triangulo escaleno")

else:
    print ("Es un triangulo isosceles")
