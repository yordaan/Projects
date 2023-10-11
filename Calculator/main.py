import customtkinter as ctk


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.title('Calculator.py')


def btn_press(num):
    current = result.get()
    result.delete(0, 'end')
    result.insert(0, str(current) + str(num))

def add():
    global num1, operation
    num1 = result.get()
    operation = '+'
    result.delete(0, 'end')
def sub():
    global num1, operation
    num1 = result.get()
    operation = '-'
    result.delete(0, 'end')
def mult():
    global num1, operation
    num1 = result.get()
    operation = '*'
    result.delete(0, 'end')
def divi():
    global num1, operation
    num1 = result.get()
    operation = '%'
    result.delete(0, 'end')
def eq():
    global num2

    num2 = result.get()
    result.delete(0, 'end')
    if operation == '+':
        sum = int(num1) + int(num2)
    elif operation == '-':
        sum = int(num1) - int(num2)
    elif operation == '*':
        sum = int(num1) * int(num2)
    elif operation == '%':
        sum = int(num1) / int(num2)
    result.insert(0, str(sum))
def clear():
    result.delete(0, 'end')

result = ctk.CTkEntry(app)
result.grid(column=0, row= 0, columnspan=4, sticky='nsew')

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

plus = ctk.CTkButton(app, text="+", command= lambda: add())

min = ctk.CTkButton(app, text="-", command= lambda: sub())

mul = ctk.CTkButton(app, text="*", command= lambda: mult())

div = ctk.CTkButton(app, text="%", command= lambda: divi())

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
equals.grid(row=6, columnspan=4, pady=2, sticky='ew')

if __name__ == '__main__':
    app.mainloop()

