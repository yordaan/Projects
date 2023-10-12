import customtkinter as ctk

calculation = ""

ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Calculator.py')
app.geometry('100X125')
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)


def btn_press(symbol):
    global calculation
    if symbol == "/" and not calculation or symbol == "*" and not calculation:
        print(f"{symbol}\n")
        print(calculation)
        clear()
        result.insert(0, 'Error')
    else:
        calculation += str(symbol)
        result.delete(0, "end")
        result.insert(0, calculation)



def eq():

   try:
       global calculation
       solution = str(float(eval(calculation)))
       result.delete(0, 'end')

       calculation = str(solution)
       result.insert(0, solution)

   except:
       clear()
       result.insert(0, 'Error')





def clear():

    global calculation
    calculation = ""
    result.delete(0, "end")

result = ctk.CTkEntry(app)
result.grid(columnspan=4,  sticky="nsew")

num_0 = ctk.CTkButton(app, text="0", command= lambda: btn_press(0))

num_1 = ctk.CTkButton(app, text="1", command= lambda: btn_press(1))

num_2 = ctk.CTkButton(app, text="2", command= lambda: btn_press(2))

num_3 = ctk.CTkButton(app, text="3", command= lambda: btn_press(3))

num_4 = ctk.CTkButton(app, text="4", command= lambda: btn_press(4))

num_5 = ctk.CTkButton(app, text="5", command= lambda: btn_press(5))

num_6 = ctk.CTkButton(app, text="6", command= lambda: btn_press(6))

num_7 = ctk.CTkButton(app, text="7", command= lambda: btn_press(7))

num_8 = ctk.CTkButton(app, text="8", command= lambda: btn_press(8))

num_9 = ctk.CTkButton(app, text="9", command= lambda: btn_press(9))

plus = ctk.CTkButton(app, text="+", command= lambda: btn_press('+'))

min = ctk.CTkButton(app, text="-", command= lambda: btn_press('-'))

mul = ctk.CTkButton(app, text="x", command= lambda: btn_press('*'))

div = ctk.CTkButton(app, text="/", command= lambda: btn_press('/'))

equals = ctk.CTkButton(app, text="=", command= lambda: eq())

cls = ctk.CTkButton(app, text="C", command= lambda: clear())

num_7.grid(row=1, column=1, pady=2)
num_8.grid(row=1, column=2, pady=2)
num_9.grid(row=1, column=3, pady=2)
num_4.grid(row=2, column=1, pady=2)
num_5.grid(row=2, column=2, pady=2)
num_6.grid(row=2, column=3, pady=2)
num_1.grid(row=3, column=1, pady=2)
num_2.grid(row=3, column=2, pady=2)
num_3.grid(row=3, column=3, pady=2)
num_0.grid(row=4, column=2, pady=2)
plus.grid(row=4, column=1, pady=2)
cls.grid(row=4, column=3, pady=2)
min.grid(row=5, column=1, pady=2)
mul.grid(row=5, column=2, pady=2)
div.grid(row=5, column=3, pady=2)
equals.grid(row=6, columnspan=4, pady=2, sticky='nsew')

if __name__ == '__main__':
    app.mainloop()

