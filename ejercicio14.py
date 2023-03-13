in_per_feet = 12
cm_per_in = 2.54

feet = int(input("Numero en pies: "))
inches = int(input("Numero en inches: "))

cm = (feet * in_per_feet + inches) * cm_per_in

print ("Tu medida es", cm, "centimetros")
