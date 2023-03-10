
num_widgets = int(input("¿Cuantos widgets has comprado?"))
num_gizmos = int(input("¿Cuantos gizmos has comprado?"))

total_widgets = float(num_widgets * 0.75)
total_gizmos = float(num_gizmos * 1.12)

total = total_gizmos + total_widgets

print("El total de tu compra pesará {:.2f}".format(total), "gramos")
print("Un total de {:.2f}".format(total_gizmos), "gramos de gizmos")
print("Un total de {:.2f}".format(total_widgets), "gramos de widgets")
