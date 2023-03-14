
mes = str(input("Introduce el mes del año: "))

if mes == "Enero" or mes == "Marzo" or mes == "Mayo" or mes == "Julio" or mes == "Agosto" or mes == "Octubre" or mes == "Diciembre":
    print ("El mes tiene 31 días")

elif mes == "Febrero":
    print("Puede tener 28 o 29 días")

else:
    print("El mes tiene 30 diasE")