# Imports
from tkinter import *
from tkinter import messagebox



# Screen
root = Tk()
root.geometry("300x300")
root.title("Python Login Form")



# Show Password Function
def ShowPasswordFunc():
    if CheckedShowPassword.get() == 1:
        PasswordEntry.config(show="")
    elif CheckedShowPassword.get() == 0:
        PasswordEntry.config(show="*")



# Login Function
def LoginFunc():
    if UsernameEntry.get() == "":
        messagebox.showerror("Login Unsuccessful!", "Please enter a Username")
    elif PasswordEntry.get() == "":
        messagebox.showerror("Login Unsuccessful!", "Please enter a Password")
    else:
        messagebox.showinfo("Login Successful", "You have been logged in successfully")



# Username Label
UsernameLabel = Label(root, text="Username:", font=("Arial", 16))
UsernameLabel.pack()



# Username Entry Box
UsernameEntry = Entry(root, font=("Arial", 16))
UsernameEntry.pack()



# Empty Frame
Frame(root, height=25).pack()



# Password Label
PasswordLabel = Label(root, text="Password:", font=("Arial", 16))
PasswordLabel.pack()



# Password Entry Box
PasswordEntry = Entry(root, font=("Arial", 16), show="*")
PasswordEntry.pack()



# Checkbox to Show Password
CheckedShowPassword = IntVar()

ShowPasswordCheckbox = Checkbutton(root, text="Show Password", variable=CheckedShowPassword, command=ShowPasswordFunc) 
ShowPasswordCheckbox.pack(pady=5)



# Login Button
LoginBtn = Button(root, text="Login", font=("Arial", 16), command=LoginFunc)
LoginBtn.pack(pady=20)



# Mainloop
root.mainloop()
