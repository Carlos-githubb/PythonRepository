def conversor(coin_type, dolar_value):
    coin = input("How many " + coin_type + " do you have? ")
    coin = float(coin)
    dolars = coin/dolar_value
    dolars = round(dolars, 2)
    dolars = str(dolars)
    print(" You have $" + dolars + " dolars")

menu = """

Wellcom to our coins echange

1 - liras
2 - dinars
3 - dirhams

Choice an option:

"""  

option = int(input(menu))

if option == 1:
    conversor("liras", 14.85)
elif option == 2:
    conversor("dinars", 0.30)
elif option == 3:
    conversor("dirhams", 3.75) 
else:
    print( "Enter a right option please") 
                        