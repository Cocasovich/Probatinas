cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime =    10
cents_per_nickel =   5
cents_per_pennie =   1

cents = int(input("Introduce los centimos: "))

toonies = cents//cents_per_toonie
resto_toonies = cents % cents_per_toonie

loonies = cents//cents_per_loonie
resto_loonies = cents % cents_per_loonie

quarters = cents//cents_per_quarter
resto_quarters = cents % cents_per_quarter

dimes = cents//cents_per_dime
resto_dimes = cents % cents_per_dime

nickels = cents//cents_per_nickel
resto_nickels = cents % cents_per_nickel

pennies = cents


# print ("{:.2f}".format(toonies), "Toonies")
# print ("{:.2f}".format(loonies), "Loonies")
# print ("{:.2f}".format(quarters), "Quarters")
# print ("{:.2f}".format(dimes), "Dimes")
# print ("{:.2f}".format(nickels), "Nickels")
# print ("{:.2f}".format(pennies), "Pennies")

print (toonies, "Toonies")
print (loonies, "Loonies")
print (quarters, "Quarters")
print (dimes, "Dimes")
print (nickels, "Nickels")
print (pennies, "Pennies")