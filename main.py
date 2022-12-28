import tkinter as tk
import tkinter.messagebox as mb

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


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
            # entry_username.delete(0, "end")
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
button_generate = tk.Button(text="Generate Password")
button_generate.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=30, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
