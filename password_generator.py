import random
import string
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Password Generator")

def generate_password(length):

    #define the characters that can be used in the password
    characters=string.ascii_letters + string.digits + string.punctuation

    #Generate a random password by choosing characters from the defined set
    password= ''.join(random.choice(characters) for _ in range(length))

    #clear the text area and insert the generated password
    text_area.delete("1.0", tk.END)
    text_area.insert("end", password)

def reset_passwd():
    #Clear the text area ,username , and password length fields
    text_area.delete("1.0", tk.END)
    user_input.delete(0 , tk.END)
    user_input.delete(0 , tk.END)
    user_input.focus_set()

def accept_passwd():
    messagebox.showinfo("Generate Password" , f"Password generated succesfully")

#Label for Username
user_name = tk.Label(text = "Username: ")
user_name.place(x=40 , y=60)

#Entry field for username
user_input = tk.Entry(width=30)
user_input.place(x=160 , y=60)

#Label for password Length: 
password_label = tk.Label(text = "Lenght of password : ")
password_label.place(x=40 , y=90)

#Entry for password length 
password_input = tk.Entry(width=30)
password_input.place(x=160 , y=90)

#Text area to display the generated password
text_area =tk.Text(root , font="25" , width=20 , height=1.2)
text_area.place(x=160 , y=120)

#Button to trigger the password genearate function
generate_button = tk.Button(text="Generate password" , command=lambda: generate_password(int(password_input.get())))
generate_button.place(x=40 , y=120)

reset_button= tk.Button(text="RESET" , command=reset_passwd)
reset_button.place(x=190 , y=160)

reset_button = tk.Button(text="Accept" , command=accept_passwd)
reset_button.place(x=185 ,y=200)

root.mainloop()
