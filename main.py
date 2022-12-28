import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

entry_username = tk.Entry(width=35)
entry_username.grid(row=2, column=1, columnspan=2)

entry_password = tk.Entry(width=17)
entry_password.grid(row=3, column=1)

# Button
button_generate = tk.Button(text="Generate Password")
button_generate.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=30)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
