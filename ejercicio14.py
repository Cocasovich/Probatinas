conv_pie_cm = 38.48
pulgada_a_cm = 2.54 

pies = float(input("Feet: "))
pulgadas = float(input("Inches: "))

cm_1 = pies * conv_pie_cm
cm_2 = pulgadas * pulgada_a_cm

total_en_cm = cm_1 + cm_2

print ("Tu altura es de", total_en_cm, "cm")

