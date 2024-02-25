from tkinter import *
from tkinter import messagebox

# Functions ---------------------------------


def handleSubmit():
    website = website_entry.get()
    password = password_entry.get()
    email = email_and_username_label_entry.get()

    user_response = messagebox.askyesno(
        title="Confirm", message=f"Please verify the details below:\nEmail/Username: {email}\nPassword: {password}\nWould you like to save?")
    print(user_response)

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
generate_button = Button(text="Generate Password", width=11)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=handleSubmit)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
