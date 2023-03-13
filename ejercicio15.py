import math

from fractions import Fraction

radio = float (input ("Radio: "))

area = math.pi * (radio ** 2)

fraccion = Fraction (4,3)

volumen = fraccion * math.pi * (radio ** 3)

print ("El area es de", area,)

print ("El volumen es de", volumen)