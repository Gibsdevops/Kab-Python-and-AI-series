from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def button_click(number):
    #e.delete(0, END)
    
    current = e.get()
    e.delete(0, END)

    e.insert(0, str(current) + str(number))

#define a clear function for the clear button
def button_clear():
    e.delete(0, END)   

#defining the function for addition
def button_add():
    firstNumber = e.get()
    global f_num 
    global operator
    operator = "addition"
    f_num = int(firstNumber)
    e.delete(0, END)
    
#defining the function for the subtract
def button_subtract():
    firstNumber = e.get()
    global f_num 
    global operator
    operator = "subtraction"
    f_num = int(firstNumber)
    e.delete(0, END)

#defining the function for multiply
def button_multiply():
    firstNumber = e.get()
    global f_num 
    global operator 
    operator = "mutliplication"
    f_num = int(firstNumber)
    e.delete(0, END)
#defining the function for divide
def button_divide():
    firstNumber = e.get()
    global f_num 
    global operator 
    operator = "division"
    f_num = int(firstNumber)
    e.delete(0, END)

#defining the function for the equal
def button_equal():
    #taking the second number
    second_number = e.get()
    e.delete(0, END)

    #to carryout the arithmetic operation
    if operator == "addition":
        e.insert(0, f_num + int(second_number))
    elif operator == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif operator == "mutliplication":
        e.insert(0, f_num * int(second_number))
    else:
        e.insert(0, f_num / int(second_number))
    

#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="grey", fg="cyan", command=lambda: button_click(0))

button_clr = Button(root, text="clear", padx=77, pady=20, bg="dark olive green", fg="MediumOrchid1", command=button_clear)
button_eql = Button(root, text="=", padx=85, pady=20, bg="peach puff", fg="dark green", command=button_equal)


button_addi = Button(root, text="+", padx=40, pady=20, bg="peach puff", fg="dark green", command=button_add)
button_subrct = Button(root, text="-", padx=41, pady=20, bg="peach puff", fg="dark green", command=button_subtract)
button_multi = Button(root, text="*", padx=40, pady=20, bg="peach puff", fg="dark green", command=button_multiply)
button_divi = Button(root, text="/", padx=41, pady=20, bg="peach puff", fg="dark green", command=button_divide)


#putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1, columnspan=2) 

button_addi.grid(row=5, column=0) 
button_eql.grid(row=5, column=1, columnspan=2) 

button_subrct.grid(row=6, column=0)
button_multi.grid(row=6, column=1)
button_divi.grid(row=6, column=2)




root.mainloop()