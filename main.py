from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '&', '*', '(', ')', '+']

# Functions ---------------------------------


def handleSearch():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(
                title="Info", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists.")


def generatePassword():
    password_entry.delete(0, END)
    password_combinations = []
    rn_letter = randint(8, 12)
    rn_number = randint(2, 4)
    rn_symbol = randint(2, 4)
    password_letters = [choice(letters) for _ in range(rn_letter)]
    password_numbers = [choice(numbers) for _ in range(rn_number)]
    password_symbol = [choice(symbols) for _ in range(rn_symbol)]
    password_combinations = password_letters + password_numbers + password_symbol
    shuffle(password_combinations)
    new_password = "".join(password_combinations)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


def handleSubmit():
    website = website_entry.get()
    password = password_entry.get()
    email = email_and_username_label_entry.get()
    json_password = {
        website: {
            "email": email,
            "password": password,
        }}
    if website == "" or password == "" or email == "":
        messagebox.showinfo(
            title="Error", message="Unable to save, fields cannot be blank.")
    else:
        user_response = messagebox.askyesno(
            title="Confirm", message=f"Please verify the details below:\nEmail/Username: {email}\nPassword: {password}\nWould you like to save?")
        if user_response:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as new_file_data:
                    json.dump(json_password, new_file_data, indent=4)
                messagebox.showinfo(
                    title="Confirmed", message="Password was saved successfully")
            else:
                data.update(json_password)
                with open("data.json", "w") as write_data:
                    json.dump(data, write_data, indent=4)
                messagebox.showinfo(
                    title="Confirmed", message="Password was saved successfully")
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
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
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()  # allows user to type immediately after the program is launched
email_and_username_label_entry = Entry(width=35)
email_and_username_label_entry.grid(column=1, row=2, columnspan=2)
# prepopulates the email/username in the entry box
email_and_username_label_entry.insert(0, "peterhyh@yahoo.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons ---------------------------------
search_button = Button(text="Search", width=11, command=handleSearch)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password",
                         width=11, command=generatePassword)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=handleSubmit)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
