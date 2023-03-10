coste = float(
    input("¿Cuanto es el total de la comida sin tasas ni impuestos? "))

tasa = float(coste*0.21)
propina = float(coste*0.18)

total = coste + tasa + propina

print("El coste total de la comida será de {:.2f}".format(total), "euros")
print("Pagarás un total de {:.2f}".format(propina), "euros de propinas")
print("Pagarás un total de {:.2f}".format(tasa), "euros de impuestos")
