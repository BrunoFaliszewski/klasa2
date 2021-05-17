from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root, width=35)
display.grid(row=0, column=0, columnspan=3)

def display_insert(number):
    display_text = display.get() + str(number)
    display.delete(0, END)
    display.insert(0, display_text)

def clear_pressed():
    display.delete(0, END)

def equal_pressed():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, result)
    except SyntaxError:
        display.delete(0, END)
        display.insert(0, "Invalid Syntax")

Button1 = Button(root, text="1", padx=40, pady=20, command=lambda: display_insert(1))
Button2 = Button(root, text="2", padx=40, pady=20, command=lambda: display_insert(2))
Button3 = Button(root, text="3", padx=40, pady=20, command=lambda: display_insert(3))
Button4 = Button(root, text="4", padx=40, pady=20, command=lambda: display_insert(4))
Button5 = Button(root, text="5", padx=40, pady=20, command=lambda: display_insert(5))
Button6 = Button(root, text="6", padx=40, pady=20, command=lambda: display_insert(6))
Button7 = Button(root, text="7", padx=40, pady=20, command=lambda: display_insert(7))
Button8 = Button(root, text="8", padx=40, pady=20, command=lambda: display_insert(8))
Button9 = Button(root, text="9", padx=40, pady=20, command=lambda: display_insert(9))
Button0 = Button(root, text="0", padx=40, pady=20, command=lambda: display_insert(0))

Buttonadd = Button(root, text="+", padx=39, pady=20, command=lambda: display_insert('+'))
Buttonsubtract = Button(root, text="-", padx=40, pady=20, command=lambda: display_insert('-'))
Buttonmultiply = Button(root, text="*", padx=40, pady=20, command=lambda: display_insert('*'))
Buttondivide = Button(root, text="/", padx=40, pady=20, command=lambda: display_insert('/'))
Buttonequal = Button(root, text="=", padx=85, pady=20, command=lambda: equal_pressed())
Buttonclear = Button(root, text="Clear", padx=79, pady=20, command=lambda: clear_pressed())

Button1.grid(row=1, column=0)
Button2.grid(row=1, column=1)
Button3.grid(row=1, column=2)
Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
Button7.grid(row=3, column=0)
Button8.grid(row=3, column=1)
Button9.grid(row=3, column=2)
Button0.grid(row=4, column=1)

Buttonadd.grid(row=1, column=3)
Buttonsubtract.grid(row=1, column=4)
Buttonmultiply.grid(row=2, column=3)
Buttondivide.grid(row=2, column=4)
Buttonequal.grid(row=3, column=3, columnspan=2)
Buttonclear.grid(row=4, column=3, columnspan=2)

root.mainloop()