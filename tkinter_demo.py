from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image  # to import image

#USERNAME=ABHI@123
#PASS=1234
def handel_login():
    email= email_input.get()

    password= pass_input.get()

    if email=="abhi@123" or password=="1234":
        messagebox.showinfo("Login Successful","You are logged in")
    else:
        messagebox.showerror("Login Failed","You are not logged in")



root = Tk()

root.title("Login form")  # title of screen
root.iconbitmap('CRAMGINEER.png')  # iconbitmap usually works with .ico files

root.minsize(300, 400)  # corrected: minsize width <= maxsize width
root.maxsize(400, 400)  # corrected: maxsize must be >= minsize

root.geometry("300x400")  # specific size window

root.configure(background="blue")

# Open image and resize
img = Image.open('CRAMGINEER.png')
resized_img = img.resize((70, 70))  # Resize image
img_tk = ImageTk.PhotoImage(resized_img)  # Convert to Tkinter format

# Display image
image_label = Label(root, image=img_tk, bg="blue")
image_label.pack(pady=10)

text_label = Label(root, text=" Cramgineer", fg='white', bg="black")
text_label.pack()
text_label.config(font=("verdana", 20))

email_label= Label(root, text="Enter your email", fg='white', bg="black")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana", 10))

email_input = Entry(root, width=40)
email_input.pack(ipady=4,pady=(1,15))

pass_label= Label(root, text="Enter your pass", fg='white', bg="black")
pass_label.pack(pady=(20,5))
pass_label.config(font=("verdana", 10))

pass_input = Entry(root, width=40)
pass_input.pack(ipady=4,pady=(1,15))

login_btn = Button(root, text="Login", fg='white', bg="black", command=handel_login)
login_btn.pack(ipady=4,pady=(1,15))
login_btn.config(font=("verdana", 20))





root.mainloop()
