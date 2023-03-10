mpg = float(input("Ingresa el consumo de combustible en millas por galón: "))

km_por_milla = 1.60934
km_por_galon = mpg * km_por_milla

litros_por_galon = 3.78541
litros_por_100km = litros_por_galon / km_por_galon * 100

print("El consumo de combistible es de {:.2f}".format(
    litros_por_100km), "litros")
