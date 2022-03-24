liras = input("How many turkish lira do you have? ")
liras = float(liras)
dolars_value = 14.80
dolars = liras/dolars_value
dolars = round(dolars, 2)
dolars = str(dolars)
print("You have $ " + dolars + " dolars")