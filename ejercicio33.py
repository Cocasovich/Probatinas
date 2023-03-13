num_1= int(input("Introduce el primer numero: "))
num_2 = int(input("Introduce el segundo numero: "))
num_3 = int(input("Introduce el tercer numero: "))

menor = min ((num_1), (num_2), (num_3))
mayor = max ((num_1), (num_2), (num_3))
med = num_1 + num_2 + num_3 - menor - mayor

print (menor,med,mayor)
