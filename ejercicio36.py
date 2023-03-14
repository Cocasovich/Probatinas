anyos_humano = int(input("Introduce la edad en edad humana: "))

if anyos_humano < 0:
    print("Error: no puedes introducir una edad negativa")

elif anyos_humano == 1:
    anyos_perro = 10.5

elif anyos_humano == 2:
    anyos_perro = 21

else:
    anyos_perro = 21 + (anyos_humano -2) * 4


print ("Tendrá", anyos_perro, "en edad de perro")