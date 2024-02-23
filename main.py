from tkinter import *

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
email_and_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Entries ---------------------------------
website_entry = Entry(width=35)
email_and_username_label_entry = Entry(width=35)
password_entry = Entry(width=20)

# Buttons ---------------------------------
generate_button = Button(text="Generate Password", width=11)
add_button = Button(text="Add", width=32)

# Grids ---------------------------------
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)
email_and_username_label.grid(column=0, row=2)
email_and_username_label_entry.grid(column=1, row=2, columnspan=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
