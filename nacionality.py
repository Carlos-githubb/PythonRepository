


nationality = input(" Are you turkish? (answer yes or no) ")


if response == 'yes':
    echange_to_liras = 14.85
    dolars = str(round(float(input(" How many liras do you have? "))/echange_to_liras, 2))
    print("So you have " + dolars + " dolars.")
elif response == 'no':
    echange_to_dolars = 0.0673
    liras = str(round(float(input(" Wellcome to Turkey. How many dolars do you have? "))/ echange_to_dolars, 2))  
    print("So you have " + liras + " liras.")          
else:
    print("Write only yes or no, please. ")                