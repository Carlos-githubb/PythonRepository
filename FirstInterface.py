from tkinter import *
from tkinter import messagebox 

root = Tk()
my_frame=Frame(root, width=1000, height=500)
my_frame.pack()

my_variable= StringVar()


textPlaceName= Entry(my_frame, textvariable=my_variable)
textPlaceName.grid(row=0, column=1, padx=15, pady=10)

textPlaceLastName= Entry(my_frame)
textPlaceLastName.grid(row=1, column=1, padx=20, pady=15)

textPlaceEmail= Entry(my_frame)
textPlaceEmail.grid(row=2, column=1, padx=15, pady=10)

textPlacePassword= Entry(my_frame)
textPlacePassword.grid(row=3, column=1,padx=15, pady=10)
textPlacePassword.config(show="*")

textPlaceComment= Text(my_frame, width=30, height=15)
textPlaceComment.grid(row=4, column=1,padx=15, pady=10)

scrollBar= Scrollbar(my_frame, command= textPlaceComment.yview)
scrollBar.grid(row=4, column=2, sticky= "nsew")
textPlaceComment.config(yscrollcommand= scrollBar.set)




textLabelName= Label(my_frame, text="Name: ")
textLabelName.grid(row=0, column=0, sticky="e")

textLabelLastName= Label(my_frame, text="Last Name: ")
textLabelLastName.grid(row=1, column=0, sticky="e")

textLabelEmail= Label(my_frame, text="E-mail: ")
textLabelEmail.grid(row=2, column=0, sticky="e")

textLabelPassward= Label(my_frame, text="Passward: ")
textLabelPassward.grid(row=3, column=0, sticky="e")

textLabelComment= Label(my_frame, text="Comments ")
textLabelComment.grid(row=4, column=0, sticky="e")

def function_button():
    #messagebox.showinfo("You are executing Tkinter")
    my_variable.set("Carlos")

buttonSend= Button(root, text="Send", command=function_button)
buttonSend.pack()




root.mainloop()