from tkinter import *
from tkinter import messagebox
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '&', '*', '(', ')', '+']


# Functions ---------------------------------

def generatePassword():
    password_entry.delete(0, END)
    password_combinations = []
    rn_letter = random.randint(8, 12)
    rn_number = random.randint(2, 4)
    rn_symbol = random.randint(2, 4)

    for _ in range(rn_letter):
        password_combinations.append(random.choice(letters))

    for _ in range(rn_number):
        password_combinations.append(random.choice(numbers))

    for _ in range(rn_symbol):
        password_combinations.append(random.choice(symbols))

    random.shuffle(password_combinations)

    new_password = ""
    for char in password_combinations:
        new_password += char

    password_entry.insert(0, new_password)


def handleSubmit():
    website = website_entry.get()
    password = password_entry.get()
    email = email_and_username_label_entry.get()

    if website == "" or password == "" or email == "":
        messagebox.showinfo(
            title="Error", message="Unable to save, fields cannot be blank.")
    else:
        user_response = messagebox.askyesno(
            title="Confirm", message=f"Please verify the details below:\nEmail/Username: {email}\nPassword: {password}\nWould you like to save?")

        if user_response:
            with open("./passwords.txt", "a") as passwords:
                passwords.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(
                title="Confirmed", message="Password was saved successfully")
        else:
            messagebox.showinfo(title="Confirmed", message="Canceled")


# UI ---------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Labels ---------------------------------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_and_username_label = Label(text="Email/Username:")
email_and_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries ---------------------------------
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # allows user to type immediately after the program is launched
email_and_username_label_entry = Entry(width=35)
email_and_username_label_entry.grid(column=1, row=2, columnspan=2)
# prepopulates the email/username in the entry box
email_and_username_label_entry.insert(0, "peterhyh@yahoo.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons ---------------------------------
generate_button = Button(text="Generate Password",
                         width=11, command=generatePassword)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=handleSubmit)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
