botellas_1 = float(input("¿Cuantas botellas de 1L o menos tienes? "))
botellas_2 = float(input("¿Cuantas botellas de más de 1L tienes? "))

precio_1 = botellas_1 * 0.10
precio_2 = botellas_2 * 0.25

total = precio_1 + precio_2

print("Ganarás {:.2f}".format(total), "euros")
