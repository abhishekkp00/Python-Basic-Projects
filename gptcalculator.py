from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text="")

def get_operator(op):
    global first_number, operator
    try:
        first_number = float(result_label['text'])
        operator = op
        result_label.config(text="")
    except ValueError:
        result_label.config(text="Error")

def get_result():
    global first_number, second_number, operator
    try:
        second_number = float(result_label['text'])
        if operator == '+':
            result_label.config(text=str(first_number + second_number))
        elif operator == '-':
            result_label.config(text=str(first_number - second_number))
        elif operator == '*':
            result_label.config(text=str(first_number * second_number))
        elif operator == '/':
            if second_number == 0:
                result_label.config(text='Error')
            else:
                result_label.config(text=str(first_number / second_number))
    except ValueError:
        result_label.config(text="Error")

root = Tk()
root.title("Calculator")
root.geometry("280x380")
root.resizable(width=0, height=0)
root.configure(background="black")

result_label = Label(root, text='', fg="white", bg="black")
result_label.grid(row=0, column=0, columnspan=4, pady=(50, 40), sticky='w')
result_label.config(font=('Verdana', 30, "bold"))

# Row 1
Button(root, text="7", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(7)).grid(row=1, column=0)
Button(root, text="8", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(8)).grid(row=1, column=1)
Button(root, text="9", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(9)).grid(row=1, column=2)
Button(root, text="+", fg="white", bg="green", width=5, height=2, command=lambda: get_operator("+")).grid(row=1, column=3)

# Row 2
Button(root, text="4", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(4)).grid(row=2, column=0)
Button(root, text="5", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(5)).grid(row=2, column=1)
Button(root, text="6", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(6)).grid(row=2, column=2)
Button(root, text="-", fg="white", bg="green", width=5, height=2, command=lambda: get_operator("-")).grid(row=2, column=3)

# Row 3
Button(root, text="1", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(1)).grid(row=3, column=0)
Button(root, text="2", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(2)).grid(row=3, column=1)
Button(root, text="3", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(3)).grid(row=3, column=2)
Button(root, text="×", fg="white", bg="green", width=5, height=2, command=lambda: get_operator("*")).grid(row=3, column=3)

# Row 4
Button(root, text="C", fg="white", bg="red", width=5, height=2, command=clear).grid(row=4, column=0)
Button(root, text="0", fg="white", bg="green", width=5, height=2, command=lambda: get_digit(0)).grid(row=4, column=1)
Button(root, text="=", fg="white", bg="blue", width=5, height=2, command=get_result).grid(row=4, column=2)
Button(root, text="÷", fg="white", bg="green", width=5, height=2, command=lambda: get_operator("/")).grid(row=4, column=3)

root.mainloop()
