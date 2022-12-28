import tkinter as tk
import tkinter.messagebox as mb
from random import randint, choices, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [letter for letter in choices(letters, k=randint(8, 10))]
    password_list += [symbol for symbol in choices(symbols, k=randint(2, 4))]
    password_list += [number for number in choices(numbers, k=randint(2, 4))]

    shuffle(password_list)
    password_list = "".join(password_list)
    entry_password.delete(0, "end")
    entry_password.insert(0, password_list)
    pyperclip.copy(password_list)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        mb.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = mb.askokcancel(title=website, message=f"There are the details entered: \n"
                                                      f"Username: {username} \nPassword: {password} \nIs ok to save?")

        if is_ok:
            with open("data.txt", 'a') as data:
                data.write(f"{website} | {username} | {password}\n")
            entry_website.delete(0, "end")
            entry_password.delete(0, "end")
            entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
label_website = tk.Label(text="Website:")
label_website.grid(row=1, column=0)

label_username = tk.Label(text="Email/Username:")
label_username.grid(row=2, column=0)

label_password = tk.Label(text="Password:")
label_password.grid(row=3, column=0)

# Entry
entry_website = tk.Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_username = tk.Entry(width=35)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(0, "iago.pontes@outlook.com")

entry_password = tk.Entry(width=17)
entry_password.grid(row=3, column=1)

# Button
button_generate = tk.Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=30, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
